from fastapi import APIRouter
from bson import ObjectId
from backend.database import projects_collection

router = APIRouter()

@router.get("/risk-predictor/{project_id}")
def predict_risk(project_id: str):

    project = projects_collection.find_one({"_id": ObjectId(project_id)})

    if not project:
        return {"error": "Project not found"}

    ai_plan = project.get("ai_plan")

    if not ai_plan:
        return {"error": "AI plan not generated"}

    sprint_plan = ai_plan.get("sprint_plan", [])
    task_breakdown = ai_plan.get("task_breakdown", [])
    team_size = project.get("team_size", 1)

    # ── Risk Factor 1: Task Overdue Pattern ──
    total_tasks = sum(len(story.get("tasks", [])) for story in task_breakdown)
    overdue_tasks = sum(
        1 for story in task_breakdown
        for task in story.get("tasks", [])
        if task.get("status") == "overdue"
    )
    overdue_score = (overdue_tasks / total_tasks * 100) if total_tasks > 0 else 0

    # ── Risk Factor 2: Team Workload Level ──
    if team_size > 0:
        tasks_per_member = total_tasks / team_size
        workload_score = min((tasks_per_member / 10) * 100, 100)
    else:
        workload_score = 0

    # ── Risk Factor 3: Sprint Velocity Trend ──
    total_sprints = len(sprint_plan)
    total_stories = sum(len(sprint.get("stories", [])) for sprint in sprint_plan)
    avg_stories = (total_stories / total_sprints) if total_sprints > 0 else 0

    if avg_stories > 6:
        velocity_score = 80  # overloaded
    elif avg_stories < 3:
        velocity_score = 60  # underutilized
    else:
        velocity_score = 20  # balanced

    # ── Risk Factor 4: Retrospective Data ──
    retrospective = project.get("retrospective", {})
    went_wrong = len(retrospective.get("went_wrong", []))
    improvements = len(retrospective.get("improvements", []))
    retro_score = min((went_wrong + improvements) * 15, 100)

    # ── Final Weighted Risk Score ──
    risk_score = round(
        (overdue_score * 0.30) +
        (workload_score * 0.25) +
        (velocity_score * 0.25) +
        (retro_score * 0.20),
        2
    )

    # ── Risk Category ──
    if risk_score <= 33:
        risk_category = "Low"
    elif risk_score <= 66:
        risk_category = "Medium"
    else:
        risk_category = "High"

    # ── Affected Team Members ──
    affected_members = []
    if tasks_per_member > 10:
        for i in range(team_size):
            affected_members.append({
                "member": f"Developer {i+1}",
                "reason": "Overloaded with tasks beyond capacity"
            })

    # ── Mitigation Actions ──
    mitigation_actions = []

    if overdue_score > 40:
        mitigation_actions.append("Re-prioritize overdue tasks and assign additional resources.")
    if workload_score > 60:
        mitigation_actions.append("Redistribute workload — some members are overloaded.")
    if velocity_score >= 60:
        mitigation_actions.append("Review sprint scope — velocity trend indicates planning issues.")
    if retro_score > 40:
        mitigation_actions.append("Schedule a team health check based on retrospective signals.")
    if len(mitigation_actions) >= 3:
        mitigation_actions.append("Multiple risk factors active — escalate to project manager.")
    if not mitigation_actions:
        mitigation_actions.append("No immediate actions required. Continue monitoring project health.")

    return {
        "risk_predictor": {
            "project_name": project.get("project_name", "Unknown"),
            "risk_score": risk_score,
            "risk_category": risk_category,
            "affected_tasks_percentage": round(overdue_score, 2),
            "affected_team_members": affected_members,
            "suggested_mitigation_actions": mitigation_actions,
            "summary": (
                f"Project has a risk score of {risk_score}/100 ({risk_category} Risk). "
                f"Overdue tasks: {round(overdue_score)}%, "
                f"Workload pressure: {round(workload_score)}%, "
                f"Velocity risk: {round(velocity_score)}%, "
                f"Retrospective concern: {round(retro_score)}%."
            )
        }
    }