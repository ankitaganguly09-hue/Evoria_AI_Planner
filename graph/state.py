from typing import TypedDict

class EventState(TypedDict, total=False):
    query: str

    requirements: str
    venues: str
    vendors: str
    budget: str
    schedule: str
    final_plan: str