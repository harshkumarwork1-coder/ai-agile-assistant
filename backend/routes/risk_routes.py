from fastapi import APIRouter
from bson import ObjectId
from backend.database import projects_collection

router = APIRouter(prefix="/risk")


@router.get("/{project_id}")
def get_project_risk(project_id: str):

    project = projects_collection.find_one(
        {"_id": ObjectId(project_id)}
    )

    if not project:
        return {"error": "project not found"}

    ai_plan = project.get("ai_plan", {})

    risks = ai_plan.get("risk_analysis", [])

    high = 0
    medium = 0
    low = 0

    for r in risks:
        severity = r.get("severity", "").lower()

        if severity == "high":
            high += 1
        elif severity == "medium":
            medium += 1
        elif severity == "low":
            low += 1

    total = len(risks)

    risk_score = (high * 3 + medium * 2 + low * 1)

    return {
        "project_id": project_id,
        "total_risks": total,
        "high_risk_count": high,
        "medium_risk_count": medium,
        "low_risk_count": low,
        "risk_score": risk_score
    }