from rag.retriever import retriever
from agents.llm import llm

def venue_agent(state):

    req = state.get("requirements", "")

    docs = retriever.invoke(req)

    context = "\n".join([d.page_content for d in docs])

    prompt = f"""
    Suggest best venues.

    Requirements:
    {req}

    Context:
    {context}
    """

    result = llm.invoke(prompt)

    return {
        "venues": result.content
    }