from asyncio import sleep
from random import random

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


# artificial delays for simulation

def small_delay():
    return sleep(random())

def medium_delay():
    return sleep(1 + .5 * random())

def big_delay():
    return sleep(2 + random())

