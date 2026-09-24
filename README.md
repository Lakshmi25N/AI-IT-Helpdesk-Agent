# AI IT Helpdesk Agent

An AI-powered IT Helpdesk Agent that helps users troubleshoot common technical issues using **Agentic AI, RAG, ChromaDB, Ollama, and local LLMs**.

## Features

* Agentic AI for analyzing user problems
* RAG-based knowledge retrieval using ChromaDB
* Qwen2.5:3B local LLM through Ollama
* `nomic-embed-text` for text embeddings
* Network diagnostic tool
* Conversation memory
* Streamlit-based chat interface
* No paid API required

## Supported Issues

The agent can provide help for:

* Wi-Fi and network problems
* Printer problems
* Password and account issues
* Windows and system problems
* Basic IT troubleshooting

## Tech Stack

| Component     | Technology           |
| ------------- | -------------------- |
| Programming   | Python               |
| AI Model      | Qwen2.5:3B           |
| Local Runtime | Ollama               |
| RAG           | ChromaDB             |
| Embeddings    | nomic-embed-text     |
| Interface     | Streamlit            |
| Memory        | Conversation History |

## Project Structure

```text
AI-IT-Helpdesk-Agent/
│
├── app.py
├── agent.py
├── rag.py
├── tools.py
├── memory.py
├── requirements.txt
├── README.md
│
├── knowledge_base/
│   ├── wifi.txt
│   ├── printer.txt
│   ├── password.txt
│   └── windows.txt
│
└── chroma_db/
```

## How It Works

```text
User Problem
     ↓
Streamlit Chat Interface
     ↓
AI Helpdesk Agent
     ↓
RAG Knowledge Base
     ↓
ChromaDB + Embeddings
     ↓
Qwen2.5:3B
     ↓
Troubleshooting Response
```

## Example Queries

My Wi-Fi is connected but there is no internet.
My printer is not responding.
I forgot my account password.
My Windows system is running very slowly.

## Project Highlights

* Uses a local LLM instead of a paid API
* Combines Agentic AI with RAG
* Uses a vector database for knowledge retrieval
* Includes a practical network diagnostic tool
* Maintains conversation context
* Provides an interactive Streamlit interface

## Future Improvements

* Add more IT troubleshooting knowledge
* Add system health monitoring
* Add automatic issue detection
* Add multilingual support
* Add more diagnostic tools

## Author

**Lakshmi N**
B.E. Computer Science and Engineering

---

**Technologies:** Python | Agentic AI | RAG | ChromaDB | Ollama | Qwen2.5 | Streamlit
