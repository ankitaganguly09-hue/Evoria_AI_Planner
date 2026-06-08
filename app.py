import streamlit as st
from graph.workflow import graph

# -------------------------------
# PAGE CONFIG
# -------------------------------
st.set_page_config(
    page_title="Evoria AI Planner",
    page_icon="🎉",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -------------------------------
# CUSTOM CSS (DARK + GRADIENT THEME)
# -------------------------------
st.markdown("""
<style>

/* App background */
.main {
    background-color: #0e1117;
    color: white;
}

/* Title gradient */
.title {
    font-size: 44px;
    font-weight: 800;
    background: linear-gradient(90deg, #7F7FD5, #86A8E7, #91EAE4);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

/* Subtitle */
.subtitle {
    font-size: 18px;
    color: #a0a0a0;
    margin-bottom: 10px;
}

/* Text area */
.stTextArea textarea {
    background-color: #161b22;
    color: white;
    border-radius: 10px;
    border: 1px solid #30363d;
}

/* Button */
.stButton button {
    background: linear-gradient(90deg, #7F7FD5, #86A8E7);
    color: white;
    font-weight: bold;
    border-radius: 10px;
    padding: 10px 20px;
    border: none;
}

.stButton button:hover {
    transform: scale(1.02);
    transition: 0.2s;
}

/* Section headers */
h2 {
    color: #ffffff;
}

</style>
""", unsafe_allow_html=True)

# -------------------------------
# HEADER (LOGO + TITLE)
# -------------------------------
col1, col2 = st.columns([1, 6])

with col1:
    st.image(
        "https://cdn-icons-png.flaticon.com/512/4727/4727424.png",
        width=85
    )

with col2:
    st.markdown('<div class="title">Evoria AI Planner</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="subtitle">From idea to execution — intelligently orchestrated by AI agents</div>',
        unsafe_allow_html=True
    )

st.markdown("---")

# -------------------------------
# SIDEBAR
# -------------------------------
with st.sidebar:
    st.title("⚙️ How It Works")

    st.write("""
    1. Enter event description  
    2. Requirement Agent extracts details  
    3. Venue & Vendor search (RAG)  
    4. Budget & Schedule creation  
    5. Final AI orchestration  
    """)

    st.markdown("---")
    st.info("Powered by LangGraph + Mistral AI + RAG")

# -------------------------------
# INPUT SECTION
# -------------------------------
st.subheader("📝 Describe Your Event")

query = st.text_area(
    "Example: Plan a wedding in Bangalore for 300 guests with a budget of 5 lakhs",
    height=120
)

# -------------------------------
# GENERATE BUTTON
# -------------------------------
if st.button("🚀 Generate Event Plan"):

    if query.strip() == "":
        st.warning("Please enter an event description.")
    else:

        with st.spinner("Evoria AI is orchestrating agents... ⏳"):

            result = graph.invoke({
                "query": query
            })

        st.success("🎉 Event Plan Generated!")

        # -------------------------------
        # OUTPUT SECTIONS
        # -------------------------------
        st.markdown("## 📍 Venue Recommendations")
        st.write(result.get("venues", ""))

        st.markdown("## 🧑‍💼 Vendor Suggestions")
        st.write(result.get("vendors", ""))

        st.markdown("## 💰 Budget Breakdown")
        st.write(result.get("budget", ""))

        st.markdown("## 📅 Event Schedule")
        st.write(result.get("schedule", ""))

        st.markdown("## 📄 Final Event Plan")
        st.write(result.get("final_plan", ""))

# -------------------------------
# FOOTER CREDIT
# -------------------------------
st.markdown("---")
st.markdown(
    """
    <div style='text-align: center; color: gray; font-size: 14px;'>
        Built with ❤️ by <b style='color:white;'>Ankita Ganguly</b> • Evoria AI Planner
    </div>
    """,
    unsafe_allow_html=True
)