from agents.llm import llm


def requirement_agent(state):

    query = state["query"]

    prompt = f"""
    Extract event requirements.

    User Request:
    {query}

    Return JSON:
    event_type
    guest_count
    city
    budget
    date
    """

    result = llm.invoke(prompt)

    return {
        "requirements": result.content
    }