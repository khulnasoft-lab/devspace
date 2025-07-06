"""HTTP server for DevSpace API."""

import uvicorn
from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from typing import Dict, Any

from app.http.routes import router as api_router


def create_app() -> FastAPI:
    """Create and configure the FastAPI application."""
    app = FastAPI(
        title="DevSpace API",
        description="A comprehensive AI/ML, robotics, and distributed systems development environment API",
        version="0.1.0",
        docs_url="/docs",
        redoc_url="/redoc",
    )
    
    # Add CORS middleware
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],  # Configure appropriately for production
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    
    # Include API routes
    app.include_router(api_router, prefix="/api/v1")
    
    @app.get("/")
    async def root() -> Dict[str, Any]:
        """Root endpoint providing API information."""
        return {
            "message": "Welcome to DevSpace API",
            "version": "0.1.0",
            "docs": "/docs",
            "redoc": "/redoc",
            "status": "running"
        }
    
    @app.get("/health")
    async def health_check() -> Dict[str, str]:
        """Health check endpoint."""
        return {"status": "healthy"}
    
    return app


def start_server(host: str = "127.0.0.1", port: int = 8000, debug: bool = False) -> None:
    """Start the HTTP server."""
    app = create_app()
    
    uvicorn.run(
        app,
        host=host,
        port=port,
        reload=debug,
        log_level="info" if not debug else "debug"
    )


if __name__ == "__main__":
    start_server(debug=True)
