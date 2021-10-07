from dataclasses import dataclass, field


@dataclass
class Message:
    path: str
    content: str
    context: dict = field(default_factory=dict)


@dataclass
class Response:
    content: str

    def __str__(self):
        return self.content
