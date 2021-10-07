from dataclasses import dataclass


@dataclass
class Message:
    subject: str
    path: str
    content: str


@dataclass
class Response:
    content: str
