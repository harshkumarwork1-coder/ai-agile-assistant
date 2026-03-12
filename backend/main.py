from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.routes import auth, project, ai_routes, dashboard_routes, task_routes, risk_routes,workload_routes,retrospective_routes, analytics_routes,risk_predictor_routes
from dotenv import load_dotenv


load_dotenv()
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(auth.router)
app.include_router(project.router)
app.include_router(ai_routes.router)
app.include_router(dashboard_routes.router)
app.include_router(task_routes.router)
app.include_router(risk_routes.router)
app.include_router(workload_routes.router)
app.include_router(retrospective_routes.router)
app.include_router(analytics_routes.router)
app.include_router(risk_predictor_routes.router)


@app.get("/")
def home():
    return{"message": "AI Agile Assistant Backend Running"}