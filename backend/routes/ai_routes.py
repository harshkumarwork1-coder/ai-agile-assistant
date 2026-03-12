from fastapi import APIRouter
from backend.services.ai_services import generate_sprint_plan

router = APIRouter()

@router.post("/ai/generate-sprint")
def generate_sprint(data: dict):

    project_title = data.get("project_title")
    sprint_number = data.get("sprint_number")
    team_size = data.get("team_Size")

    result = generate_sprint_plan(
        project_title,
        sprint_number,
        team_size
    )

    return{
        "message": "Sprint plan generated",
        "sprint_plan": result
    }