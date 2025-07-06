"""Main application entry point for DevSpace."""

import sys
import click
from typing import Optional

from app.cli import cli
from app.http.main import start_server


@click.command()
@click.option(
    "--mode",
    type=click.Choice(["cli", "server", "interactive"]),
    default="interactive",
    help="Run mode: cli, server, or interactive",
)
@click.option("--host", default="127.0.0.1", help="Host to bind the server to")
@click.option("--port", default=8000, type=int, help="Port to bind the server to")
@click.option("--debug", is_flag=True, help="Enable debug mode")
@click.version_option(version="0.1.0", prog_name="DevSpace")
def main(mode: str, host: str, port: int, debug: bool) -> None:
    """DevSpace - AI/ML, Robotics, and Distributed Systems Development Environment."""
    
    click.echo("🚀 Welcome to DevSpace!")
    click.echo("A comprehensive development environment for intelligent applications.")
    click.echo()
    
    if mode == "cli":
        click.echo("Starting CLI mode...")
        cli()
    elif mode == "server":
        click.echo(f"Starting HTTP server on {host}:{port}...")
        start_server(host=host, port=port, debug=debug)
    elif mode == "interactive":
        click.echo("DevSpace is ready! Choose your next action:")
        click.echo()
        click.echo("Available commands:")
        click.echo("  • devspace --mode=cli        - Start CLI interface")
        click.echo("  • devspace --mode=server     - Start HTTP API server")
        click.echo("  • devspace-cli               - Direct CLI access")
        click.echo()
        click.echo("Project structure created successfully!")
        click.echo("Check README.md for detailed usage instructions.")


if __name__ == "__main__":
    main()
