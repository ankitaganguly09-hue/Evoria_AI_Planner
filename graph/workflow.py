from langgraph.graph import StateGraph, END
from graph.state import EventState

from agents.requirement_agent import requirement_agent
from agents.venue_agent import venue_agent
from agents.budget_agent import budget_agent
from agents.vendor_agent import vendor_agent
from agents.schedule_agent import schedule_agent
from agents.planner_agent import planner_agent


builder = StateGraph(EventState)

# Nodes
builder.add_node("requirements", requirement_agent)
builder.add_node("venue", venue_agent)
builder.add_node("vendors", vendor_agent)
builder.add_node("budget", budget_agent)
builder.add_node("schedule", schedule_agent)
builder.add_node("planner", planner_agent)

# Entry point
builder.set_entry_point("requirements")

# 🔥 FIXED LINEAR FLOW (NO PARALLEL EDGES)
builder.add_edge("requirements", "venue")
builder.add_edge("venue", "vendors")
builder.add_edge("vendors", "budget")
builder.add_edge("budget", "schedule")
builder.add_edge("schedule", "planner")
builder.add_edge("planner", END)

graph = builder.compile()