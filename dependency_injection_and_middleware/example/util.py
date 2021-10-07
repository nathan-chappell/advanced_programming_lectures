from dataclasses import dataclass, field


@dataclass
class Message:
    """What the server handles"""
    path: str
    content: str
    context: dict = field(default_factory=dict)


@dataclass
class Response:
    """What the server responds with"""
    content: str

    def __str__(self):
        return self.content
