from typing import TypedDict, List

class AgentState(TypedDict):
    messages: List
    result: str
    previous: str
    orchestrator_task: str
    orchestrator_result: str
    analyticAgent_task: str
    analyticAgent_result: str