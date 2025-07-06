"""API routes for DevSpace."""

from fastapi import APIRouter
from typing import Dict, Any, List

router = APIRouter()


@router.get("/")
async def api_root() -> Dict[str, Any]:
    """API root endpoint."""
    return {
        "message": "DevSpace API v1",
        "endpoints": [
            "/ai - AI/ML operations",
            "/data - Data operations", 
            "/hardware - Hardware operations",
            "/workflows - Workflow operations",
            "/jobs - Background job operations"
        ]
    }


@router.get("/ai")
async def ai_operations() -> Dict[str, Any]:
    """AI/ML operations endpoint."""
    return {
        "message": "AI/ML Operations",
        "available_operations": [
            "agents - AI agent management",
            "trainers - Model training",
            "evals - Model evaluation",
            "actions - Agent actions"
        ],
        "status": "ready"
    }


@router.get("/data")
async def data_operations() -> Dict[str, Any]:
    """Data operations endpoint."""
    return {
        "message": "Data Operations",
        "available_operations": [
            "extractors - Data extraction",
            "transformers - Data transformation",
            "pipelines - Data pipelines"
        ],
        "status": "ready"
    }


@router.get("/hardware")
async def hardware_operations() -> Dict[str, Any]:
    """Hardware operations endpoint."""
    return {
        "message": "Hardware Operations",
        "available_operations": [
            "sensors - Sensor management",
            "actuators - Actuator control",
            "devices - Device provisioning"
        ],
        "status": "ready"
    }


@router.get("/workflows")
async def workflow_operations() -> Dict[str, Any]:
    """Workflow operations endpoint."""
    return {
        "message": "Workflow Operations",
        "available_operations": [
            "ai - AI workflows",
            "processes - Business processes",
            "automation - Automated workflows"
        ],
        "status": "ready"
    }


@router.get("/jobs")
async def job_operations() -> Dict[str, Any]:
    """Background job operations endpoint."""
    return {
        "message": "Job Operations",
        "available_operations": [
            "queue - Job queue management",
            "schedule - Scheduled jobs",
            "monitor - Job monitoring"
        ],
        "status": "ready"
    }


@router.get("/status")
async def system_status() -> Dict[str, Any]:
    """System status endpoint."""
    return {
        "system": "DevSpace",
        "version": "0.1.0",
        "components": {
            "ai": "ready",
            "data": "ready", 
            "hardware": "ready",
            "workflows": "ready",
            "jobs": "ready"
        },
        "overall_status": "operational"
    }
