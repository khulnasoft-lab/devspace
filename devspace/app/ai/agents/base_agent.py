"""Base AI agent class for DevSpace."""

from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional
from pydantic import BaseModel


class AgentConfig(BaseModel):
    """Configuration for AI agents."""
    name: str
    model_name: str = "gpt-3.5-turbo"
    max_tokens: int = 4096
    temperature: float = 0.7
    system_prompt: Optional[str] = None
    tools: List[str] = []


class AgentState(BaseModel):
    """State representation for AI agents."""
    agent_id: str
    status: str  # active, idle, error, stopped
    current_task: Optional[str] = None
    context: Dict[str, Any] = {}
    message_history: List[Dict[str, str]] = []


class BaseAgent(ABC):
    """Base class for all AI agents in DevSpace."""
    
    def __init__(self, config: AgentConfig):
        """Initialize the agent with configuration."""
        self.config = config
        self.state = AgentState(
            agent_id=f"{config.name}_{id(self)}",
            status="idle"
        )
    
    @abstractmethod
    async def process_message(self, message: str, context: Optional[Dict[str, Any]] = None) -> str:
        """Process a message and return a response."""
        pass
    
    @abstractmethod
    async def execute_action(self, action: str, parameters: Dict[str, Any]) -> Dict[str, Any]:
        """Execute an action with given parameters."""
        pass
    
    def get_status(self) -> Dict[str, Any]:
        """Get current agent status."""
        return {
            "agent_id": self.state.agent_id,
            "name": self.config.name,
            "status": self.state.status,
            "current_task": self.state.current_task,
            "model": self.config.model_name
        }
    
    def update_status(self, status: str, task: Optional[str] = None) -> None:
        """Update agent status."""
        self.state.status = status
        if task is not None:
            self.state.current_task = task
    
    def add_to_history(self, role: str, content: str) -> None:
        """Add message to conversation history."""
        self.state.message_history.append({
            "role": role,
            "content": content
        })
    
    def clear_history(self) -> None:
        """Clear conversation history."""
        self.state.message_history = []
    
    def get_context(self, key: str) -> Any:
        """Get context value by key."""
        return self.state.context.get(key)
    
    def set_context(self, key: str, value: Any) -> None:
        """Set context value."""
        self.state.context[key] = value
    
    def clear_context(self) -> None:
        """Clear all context."""
        self.state.context = {}
