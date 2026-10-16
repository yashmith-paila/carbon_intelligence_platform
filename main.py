from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from database.mongodb import client
from routes import auth_routes, emissions_routes, analytics_routes, simulation_routes, user_routes, organization_routes, report_routes, recommendation_routes
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(title="AI Carbon Intelligence Platform")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://localhost:5173",
        "http://127.0.0.1:3000",
        "http://127.0.0.1:5173",
        "http://localhost:3000/"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content={"detail": "Internal Server Error"},
    )

app.include_router(auth_routes.router, prefix="/api/auth", tags=["Auth"])
app.include_router(user_routes.router, prefix="/api/users", tags=["Users"])
app.include_router(organization_routes.router, prefix="/api/organization", tags=["Organization"])
app.include_router(emissions_routes.router, prefix="/api/emissions", tags=["Emissions"])
app.include_router(analytics_routes.router, prefix="/api/analytics", tags=["Analytics"])
app.include_router(simulation_routes.router, prefix="/api/simulation", tags=["Simulation"])
app.include_router(report_routes.router, prefix="/api/reports", tags=["Reports"])
app.include_router(recommendation_routes.router, prefix="/api/recommendations", tags=["Recommendations"])

@app.get("/")
def read_root():
    return {"message": "Welcome to AI Carbon Intelligence Platform API"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
