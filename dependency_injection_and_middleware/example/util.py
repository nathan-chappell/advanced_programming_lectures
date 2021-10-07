from dataclasses import dataclass


@dataclass
class Message:
    path: str
    content: str


@dataclass
class Response:
    content: str
