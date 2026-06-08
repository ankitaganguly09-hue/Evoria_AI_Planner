from agents.llm import llm

def schedule_agent(state):

    req = state.get("requirements", "")

    prompt = f"""
    Create event schedule:

    {req}
    """

    result = llm.invoke(prompt)

    return {
        "schedule": result.content
    }