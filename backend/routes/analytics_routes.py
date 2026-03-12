from fastapi import APIRouter
from bson import ObjectId
from backend.database import projects_collection

router = APIRouter()

@router.get("/analytics/{project_id}")
def sprint_analytics(project_id: str):

    project = projects_collection.find_one({"_id": ObjectId(project_id)})

    if not project:
        return {"error": "project not found"}

    ai_plan = project.get("ai_plan")

    if not ai_plan:
        return {"error": "AI plan not generated"}

    sprint_plan = ai_plan.get("sprint_plan", [])

    stories_per_sprint = []

    total_stories = 0

    for sprint in sprint_plan:

        story_count = len(sprint.get("stories", []))

        stories_per_sprint.append({
            "sprint": sprint.get("sprint_number"),
            "stories": story_count
        })

        total_stories += story_count

    total_sprints = len(sprint_plan)

    if total_sprints > 0:
        avg_stories = total_stories / total_sprints
    else:
        avg_stories = 0

    # Simple AI interpretation
    if avg_stories < 3:
        efficiency = "Low Sprint Utilization"
    elif avg_stories <= 6:
        efficiency = "Balanced Sprint Planning"
    else:
        efficiency = "Overloaded Sprint"

    return {
        "sprint_analytics": {
            "total_sprints": total_sprints,
            "stories_per_sprint": stories_per_sprint,
            "average_stories_per_sprint": avg_stories,
            "efficiency_indicator": efficiency
        }
    }