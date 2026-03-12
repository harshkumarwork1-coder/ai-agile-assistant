from fastapi import APIRouter
from backend.database import projects_collection
from backend.services.ai_services import generate_agile_plan
from bson import ObjectId

router = APIRouter(prefix="/project")

@router.post("/create")
def create_project(project: dict):

    # Generate AI plan
    ai_output = generate_agile_plan(
        project["title"],
        project["description"],
        project["deadline"],
        project["team_size"]
    )

    # attach AI plan to project
    project["ai_plan"] = ai_output

    # save to MongoDB
    result = projects_collection.insert_one(project)

    return {
        "message": "project created",
        "project_id": str(result.inserted_id),
        "ai_plan": ai_output
    }




@router.get("/all")
def get_all_projects():
    projects = list(projects_collection.find())

    for project in projects:
        project["_id"] = str(project["_id"])

    return {"projects": projects}

@router.get("/{project_id}")
def get_project(project_id: str):

    project = projects_collection.find_one(
        {"_id": ObjectId(project_id)}
    )

    if not project:
        return {"error": "Project not found"}

    project["_id"] = str(project["_id"])

    return project

@router.delete("/{project_id}")
def delete_project(project_id: str):

    result = projects_collection.delete_one(
        {"_id": ObjectId(project_id)}
    )

    if result.deleted_count == 0:
        return {"error": "Project not found"}

    return {"message": "Project deleted successfully"}