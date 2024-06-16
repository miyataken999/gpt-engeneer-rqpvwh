from dataclasses import dataclass

@dataclass
class User:
    """Represents a user"""
    id: int
    name: str
    email: str