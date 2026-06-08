from agents.llm import llm

def vendor_agent(state):

    venues = state.get("venues", "")

    prompt = f"""
    Suggest vendors based on venues:

    {venues}

    Return structured vendor list.
    """

    result = llm.invoke(prompt)

    return {
        "vendors": result.content   # 🔥 MUST BE "vendors"
    }