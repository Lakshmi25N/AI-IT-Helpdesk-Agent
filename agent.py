from langchain_ollama import ChatOllama
from langchain_core.tools import tool
from langchain.agents import create_agent

from rag import retrieve_documents
from tools import network_diagnostic


# ==============================
# LLM
# ==============================

llm = ChatOllama(
    model="Qwen2.5:3b",
    temperature=0
)


# ==============================
# RAG TOOL
# ==============================

@tool
def search_it_knowledge(query: str) -> str:
    """
    Search the IT Helpdesk knowledge base for
    relevant troubleshooting information.
    """

    print("\n🔎 RAG TOOL CALLED")
    print("Query:", query)

    documents = retrieve_documents(query)

    print("Retrieved:", len(documents), "documents")

    if not documents:
        return "No relevant information found in the knowledge base."

    context = "\n\n".join(
        document.page_content
        for document in documents
    )

    return context


# ==============================
# NETWORK TOOL
# ==============================

@tool
def diagnose_network(
    connection_type: str,
    internet_status: str
) -> str:
    """
    Diagnose basic WiFi or Ethernet connectivity.
    """

    print("\n🛠️ NETWORK DIAGNOSTIC TOOL CALLED")
    print("Connection:", connection_type)
    print("Status:", internet_status)

    return network_diagnostic(
        connection_type,
        internet_status
    )


tools = [
    search_it_knowledge,
    diagnose_network
]


# ==============================
# SYSTEM PROMPT
# ==============================

SYSTEM_PROMPT = """
You are an AI IT Helpdesk Agent.

You diagnose common IT problems and recommend
troubleshooting steps.

AVAILABLE TOOLS:

1. search_it_knowledge
Searches the IT Helpdesk knowledge base.

2. diagnose_network
Diagnoses basic WiFi or Ethernet connectivity.

MANDATORY WORKFLOW:

For every technical support question:

FIRST:
Call search_it_knowledge using the user's complete
problem description.

SECOND:
If the problem involves WiFi or Ethernet,
call diagnose_network.

IMPORTANT:

The user saying:

"My laptop is connected to WiFi but internet is not working"

means:

connection_type = WiFi
internet_status = no internet

It does NOT mean:
internet_status = Not Connected.

Use the meaning of the user's sentence, not just
individual words.

FINAL ANSWER:

Use ONLY information returned by the tools.

Do not invent troubleshooting steps.

Do not recommend:
- Google DNS
- driver updates
- network scans
- firmware updates

unless those are explicitly present in the knowledge base.

Format the answer as:

Diagnosis:
...

Possible Causes:
...

Recommended Troubleshooting:
1. ...
2. ...
3. ...

Escalation:
...
"""


# ==============================
# CREATE AGENT
# ==============================

agent = create_agent(
    model=llm,
    tools=tools,
    system_prompt=SYSTEM_PROMPT
)

# ==============================
# HELPDESK FUNCTION
# ==============================

def ask_helpdesk(question: str):

    # 1. ALWAYS retrieve from knowledge base
    print("\n🔎 RAG TOOL CALLED")
    print("Query:", question)

    documents = retrieve_documents(question)

    print("Retrieved:", len(documents), "documents")

    context = "\n\n".join(
        document.page_content
        for document in documents
    )

    # 2. Let the Agent use the diagnostic tool
    result = agent.invoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content": f"""
User IT Problem:
{question}

Knowledge Base Results:
{context}

Use the knowledge base results above to answer the
user's problem.

If this is a WiFi or Ethernet problem, use the
diagnose_network tool.

Do not add troubleshooting steps that are not present
in the Knowledge Base Results.
"""
                }
            ]
        }
    )

    return result["messages"][-1].content