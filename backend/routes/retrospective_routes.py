from fastapi import APIRouter
from bson import ObjectId
from backend.database import projects_collection

router = APIRouter()


@router.get("/retrospective/{project_id}")
def generate_retrospective(project_id: str):

    project = projects_collection.find_one({"_id": ObjectId(project_id)})

    if not project:
        return {"error": "project not found"}

    ai_plan = project.get("ai_plan")

    if not ai_plan:
        return {"error": "AI plan not generated"}

    tasks = ai_plan.get("task_breakdown", [])

    total_tasks = 0

    for story in tasks:
        total_tasks += len(story.get("tasks", []))

    # Simple AI-like logic
    went_well = []
    went_wrong = []
    improvements = []

    if total_tasks > 5:
        went_well.append("Good task breakdown and sprint planning")

    if total_tasks < 5:
        went_wrong.append("Too few tasks planned for sprint")

    improvements.append("Improve estimation accuracy")
    improvements.append("Add buffer time for integration tasks")

    return {
        "sprint_retrospective": {
            "total_tasks": total_tasks,
            "went_well": went_well,
            "went_wrong": went_wrong,
            "improvements": improvements
        }
    }