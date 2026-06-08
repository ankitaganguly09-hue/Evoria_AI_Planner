from agents.llm import llm

def budget_agent(state):

    req = state.get("requirements", "")

    prompt = f"""
    Create budget breakdown:

    {req}
    """

    result = llm.invoke(prompt)

    return {
        "budget": result.content
    }