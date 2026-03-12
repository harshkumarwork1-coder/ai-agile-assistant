from fastapi import APIRouter
from backend.database import projects_collection
from bson import ObjectId


router = APIRouter()


@router.get("/dashboard/{project_id}")
def get_dashboard(project_id: str):
    

    project = projects_collection.find_one({"_id": ObjectId(project_id)})

    if not project:
        return {"error":"Project not found"}
    
    ai_plan = project.get("ai_plan", {})

    if not isinstance(ai_plan, dict):
        return{
            "project_title": "Unkonwn",
            "dashboard_metrics": {},
            "note":  "AI plan not generated yet"
        }

    metrics = ai_plan.get("dashboard_metrics", {})

    return{
        "project_title": ai_plan.get("project_title"),
        "dashboard_metrics": metrics
    }