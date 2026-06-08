from agents.llm import llm

def planner_agent(state):

    prompt = f"""
    FINAL EVENT PLAN

    Requirements:
    {state.get('requirements', 'N/A')}

    Venue:
    {state.get('venues', 'N/A')}

    Vendors:
    {state.get('vendors', 'N/A')}

    Budget:
    {state.get('budget', 'N/A')}

    Schedule:
    {state.get('schedule', 'N/A')}

    Create a professional event plan document.
    """

    result = llm.invoke(prompt)

    return {
        "final_plan": result.content
    }