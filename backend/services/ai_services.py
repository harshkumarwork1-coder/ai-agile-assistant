from groq import Groq
import os
import json
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def generate_agile_plan(title, description, deadline, team_size):
    prompt = f"""
You are a Senior Agile Project Manager.

Generate a COMPLETE Agile plan in STRICT JSON format.

IMPORTANT RULES:
- Return ONLY valid JSON.
- Do NOT include explanations.
- Do NOT wrap in markdown or code blocks.
- All effort estimates must be realistic.
- Use hours for tasks (if small) or days (if larger).
- Include risk severity as Low, Medium, or High.
- Also calculate dashboard metrics including workload distribution and risk score.

Structure:

{{
    "project_title": "",
    "epics": [
        {{
            "epic_name": "",
            "description": ""
        }}
    ],
    "user_stories": [
        {{
            "epic": "",
            "story": "",
            "acceptance_criteria": []
        }}
    ],
    "task_breakdown": [
        {{
            "story": "",
            "tasks": [
                {{
                    "task_name": "",
                    "estimated_effort": "",
                    "unit": "hours or days",
                    "assigned_role": ""
                }}
            ]
        }}
    ],
    "sprint_plan": [
        {{
            "sprint_number": 1,
            "duration_weeks": 2,
            "stories": []
        }}
    ],
    "risk_analysis": [
        {{
            "risk_title": "",
            "description": "",
            "severity": "Low/Medium/High",
            "impact": "",
            "mitigation_plan": ""
        }}
    ],
    "timeline_weeks": 0,
    "dashboard_metrics": {{
        "total_stories": 0,
        "total_tasks": 0,
        "estimated_total_hours": 0,
        "average_task_time_hours": 0,
        "team_workload": [
            {{
                "role": "",
                "estimated_hours": 0
            }}
        ],
        "risk_score": 0
    }}
}}

PROJECT DETAILS:
Title: {title}
Description: {description}
Deadline: {deadline}
Team Size: {team_size}
"""

    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.3,
            max_tokens=4000,
        )

        raw_text = response.choices[0].message.content.strip()

        # Clean markdown if present
        if raw_text.startswith("```"):
            raw_text = raw_text.split("```")[1]
            if raw_text.startswith("json"):
                raw_text = raw_text[4:]

        return json.loads(raw_text)

    except json.JSONDecodeError:
        return {{"error": "AI returned invalid JSON. Please try again."}}
    except Exception as e:
        return {"error": str(e)}


def generate_sprint_plan(project_title, sprint_number, team_size):
    prompt = f"""
You are a Senior Scrum Master.

Generate a Sprint Plan in STRICT JSON format.

IMPORTANT:
- Return ONLY JSON
- No explanations
- No markdown or code blocks

Structure:

{{
    "sprint_number": {sprint_number},
    "sprint_goal": "",
    "sprint_tasks": [
        {{
            "task_name": "",
            "assigned_role": "",
            "estimated_hours": 0
        }}
    ],
    "risks": [
        {{
            "risk": "",
            "severity": "Low/Medium/High",
            "mitigation": ""
        }}
    ]
}}

Project Title: {project_title}
Sprint Number: {sprint_number}
Team Size: {team_size}
"""

    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.3,
            max_tokens=2000,
        )

        raw_text = response.choices[0].message.content.strip()

        if raw_text.startswith("```"):
            raw_text = raw_text.split("```")[1]
            if raw_text.startswith("json"):
                raw_text = raw_text[4:]

        return json.loads(raw_text)

    except json.JSONDecodeError:
        return {"error": "AI returned invalid JSON. Please try again."}
    except Exception as e:
        return {"error": str(e)}


