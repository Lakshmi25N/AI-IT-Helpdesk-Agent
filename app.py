import streamlit as st

from agent import ask_helpdesk
from memory import add_message, get_history, clear_history


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="AI IT Helpdesk Agent",
    page_icon="🤖",
    layout="wide"
)


# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown("""
<style>

.main-title {
    font-size: 38px;
    font-weight: 700;
    margin-bottom: 5px;
}

.subtitle {
    font-size: 17px;
    margin-bottom: 25px;
}

.status-box {
    padding: 10px;
    border-radius: 8px;
    margin-bottom: 8px;
    border: 1px solid #ddd;
}

.section-title {
    font-size: 20px;
    font-weight: 600;
}

</style>
""", unsafe_allow_html=True)


# ============================================================
# HEADER
# ============================================================

st.markdown(
    '<div class="main-title">🤖 AI IT Helpdesk Agent</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Intelligent IT troubleshooting using Agent + RAG + Tools'
    '</div>',
    unsafe_allow_html=True
)


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.header("⚙️ System Components")

    st.markdown(
        '<div class="status-box">🟢 <b>Ollama</b><br>'
        'Local AI Runtime</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="status-box">🧠 <b>Qwen2.5:3b</b><br>'
        'AI Language Model</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="status-box">📚 <b>RAG</b><br>'
        'ChromaDB Knowledge Base</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="status-box">🔎 <b>Embeddings</b><br>'
        'nomic-embed-text</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="status-box">🛠️ <b>Tool</b><br>'
        'Network Diagnostic</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="status-box">💾 <b>Memory</b><br>'
        'Conversation History</div>',
        unsafe_allow_html=True
    )

    st.divider()

    st.subheader("📖 Knowledge Base")

    st.write("• Wi-Fi Troubleshooting")
    st.write("• Printer Troubleshooting")
    st.write("• Password & Account")
    st.write("• Windows/System Issues")

    st.divider()

    if st.button(
        "🗑️ Clear Conversation",
        use_container_width=True
    ):
        clear_history()
        st.rerun()


# ============================================================
# MAIN CHAT AREA
# ============================================================

st.markdown(
    '<div class="section-title">💬 IT Support Chat</div>',
    unsafe_allow_html=True
)

st.write(
    "Describe your technical problem below. "
    "The AI agent will analyze it and provide troubleshooting steps."
)


# ============================================================
# DISPLAY PREVIOUS CONVERSATION
# ============================================================

history = get_history()

for message in history:

    if message["role"] == "user":

        with st.chat_message("user"):
            st.write(message["content"])

    elif message["role"] == "assistant":

        with st.chat_message("assistant"):
            st.markdown(message["content"])


# ============================================================
# USER INPUT
# ============================================================

question = st.chat_input(
    "Example: My laptop is connected to WiFi but internet is not working"
)


# ============================================================
# PROCESS USER QUESTION
# ============================================================

if question:

    # Display user question
    with st.chat_message("user"):
        st.write(question)

    add_message(
        "user",
        question
    )

    # Generate AI response
    with st.chat_message("assistant"):

        with st.spinner(
            "🧠 AI Agent is analyzing your problem..."
        ):

            try:

                answer = ask_helpdesk(question)

                st.markdown(answer)

                add_message(
                    "assistant",
                    answer
                )

            except Exception as e:

                st.error(
                    "⚠️ An error occurred while processing "
                    "your request."
                )

                st.code(str(e))