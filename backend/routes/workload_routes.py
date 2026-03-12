from fastapi import APIRouter
from bson import ObjectId
from backend.database import projects_collection

router = APIRouter()


@router.get("/workload/{project_id}")
def analyze_workload(project_id: str):

    project = projects_collection.find_one({"_id": ObjectId(project_id)})

    if not project:
        return {"error": "project not found"}

    ai_plan = project.get("ai_plan")

    if not ai_plan:
        return {"error": "AI plan not generated"}

    tasks = ai_plan.get("task_breakdown", [])

    team_size = project.get("team_size", 1)

    # Create team members
    team = [f"Developer {i+1}" for i in range(team_size)]

    distribution = {member: [] for member in team}

    index = 0

    for story in tasks:
        for task in story.get("tasks", []):
            member = team[index % team_size]
            distribution[member].append(task["task_name"])
            index += 1

    return {"workload_distribution": distribution}