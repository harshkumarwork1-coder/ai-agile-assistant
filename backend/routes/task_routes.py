from fastapi import APIRouter
from bson import ObjectId
from backend.database import projects_collection

router= APIRouter(prefix="/task")

@router.get("/{project_id}")
def get_project_tasks(project_id: str):

    project = projects_collection.find_one({"_id": ObjectId(project_id)})

    if not project:
        return {"error": "project not found"}
    
    ai_plan = project.get("ai_plan",{})

    if isinstance(ai_plan, str):
        return {"error":"AI plan not generated yet"}
    
    task_breakdown = ai_plan.get("task_breakdown", [])

    tasks = []

    for story in task_breakdown:
        story_name = story.get("story")

        for task in story.get("tasks", []):
            tasks.append({
                "story":story_name,
                "task_name":task.get("assigned_role"),
                "estimated_effort": task.get("estimated_effort"),
                "unit": task.get("unit"),
                "assigned_role": task.get("assigned_role")
            })

    return {
        "project_id": project_id,
        "total_tasks": len(tasks),
        "tasks": tasks
    }