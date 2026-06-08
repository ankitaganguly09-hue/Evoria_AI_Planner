# 🎉 Evoria AI Planner

> A Multi-Agent AI system that turns a single idea into a complete, structured event plan using LangGraph, Mistral AI, and RAG.

---

## 🚀 What is Evoria AI Planner?

Evoria AI Planner is an intelligent event planning system that takes a natural language input like:

> “Plan a wedding in Bangalore for 300 guests with a budget of 5 lakhs”

and transforms it into a complete, structured event plan covering venues, vendors, budget breakdown, schedule, and execution details.

Instead of relying on a single AI response, Evoria simulates a coordinated system of specialized AI agents working together, just like a real event planning team.

Each agent focuses on a specific part of the planning process, and all agents are orchestrated using a graph-based workflow powered by LangGraph.

---

## 🧠 How It Works

When a user submits an event request, Evoria breaks it down into multiple steps and processes it through a chain of AI agents.

First, the system analyzes the user’s input to extract structured requirements such as event type, budget, location, and guest count.

Based on these requirements, the system searches for suitable venues using a Retrieval-Augmented Generation (RAG) pipeline powered by ChromaDB, ensuring that recommendations are contextually relevant and grounded in stored knowledge.

Next, it suggests vendors such as caterers, decorators, photographers, and DJs based on the selected venue and event type. This ensures all recommendations are aligned with the event context.

After that, a budget planning step distributes the total budget across different categories like venue, food, decoration, photography, and miscellaneous expenses.

Then a scheduling step creates a structured timeline for the entire event, ensuring smooth execution from start to finish.

Finally, a planner agent combines all outputs into a single coherent event plan, formatted for easy understanding and real-world use.

---

## ⚙️ System Architecture (Conceptual Flow)

The system follows a structured pipeline:

User Input → Requirement Analysis → Venue Selection (RAG) → Vendor Selection (RAG) → Budget Planning → Schedule Creation → Final Plan Generation

Each stage is handled by a dedicated AI agent, and all communication between agents is managed using LangGraph, which ensures structured execution flow instead of random LLM chaining.

---

## 🧩 AI Agents in the System

Evoria is powered by multiple specialized agents working together:

The Requirement Agent interprets the user’s natural language input and converts it into structured data that the system can use.

The Venue Agent uses a RAG pipeline to search a vector database of venues and suggests the most relevant options based on budget, location, and event type.

The Vendor Agent similarly retrieves and suggests service providers such as catering, decoration, photography, and entertainment vendors.

The Budget Agent takes the full event context and generates a realistic breakdown of how the budget should be distributed across different categories.

The Schedule Agent builds a detailed timeline for the event, ensuring proper sequencing of all activities.

Finally, the Planner Agent acts as the orchestrator that merges all outputs into a final structured event plan.

---

## 🧰 Tech Stack

Evoria AI Planner is built using modern AI and orchestration tools:

LangGraph is used to manage the multi-agent workflow and define execution order between agents.

Mistral AI powers the reasoning and generation capabilities of each agent.

ChromaDB is used as the vector database for storing and retrieving venue and vendor knowledge in the RAG pipeline.

LangChain provides the underlying framework for working with LLMs and embeddings.

Streamlit is used to build a simple and interactive user interface.

Python serves as the core backend language connecting all components.

---

## 💡 Key Features

Evoria allows users to plan complete events using a single prompt.

It provides intelligent venue recommendations using retrieval-augmented generation instead of static lists.

It generates structured vendor suggestions tailored to the event type and location.

It automatically creates a realistic and balanced budget distribution.

It produces a detailed event schedule from start to finish.

It combines all outputs into a single professional-grade event plan.

The entire system is powered by a multi-agent architecture rather than a single prompt-based LLM response.

---

## 🖥️ Example Input

A user can simply type:

> Plan a corporate event in Bengaluru for 500 people with a budget of 10 lakhs. We need an auditorium, catering, stage setup, and photography.

---

## 📊 Example Output

Evoria generates a complete event blueprint including:

Venue recommendations based on requirements and budget

A structured list of vendors for catering, decoration, and photography

A detailed budget breakdown across all categories

A step-by-step event timeline

A final consolidated event execution plan

---

## 🧪 How to Run the Project

Clone the repository and set up the environment:

Install dependencies using pip.

Set your Mistral API key in a .env file.

Run the ingestion script to build the vector database for RAG.

Finally, launch the Streamlit application.

Once running, enter your event description in natural language and generate a complete AI-powered event plan instantly.

---

## 🧠 What Makes This Project Unique

Unlike traditional AI chatbots, Evoria is not a single-model system.

It is a coordinated multi-agent system where each agent has a defined responsibility.

It uses graph-based orchestration instead of linear prompting.

It integrates retrieval-augmented generation for grounded recommendations.

It behaves like a real-world event planning team rather than a chatbot.

---

## 🚀 Future Improvements

The system can be extended with parallel agent execution for faster performance.

It can support PDF export of event plans.

It can include memory to store past events and reuse preferences.

It can integrate Google Maps for real venue data.

It can support voice-based event planning.

It can be deployed as a cloud-based SaaS product.

---

## 🏆 Final Vision

Evoria AI Planner demonstrates how multiple AI agents can collaborate to solve complex real-world tasks.

From a single idea, it builds structured execution plans through coordinated intelligence.

It represents a shift from simple LLM usage to full AI system design.

---

## 🤝 Author

Ankita Ganguly

