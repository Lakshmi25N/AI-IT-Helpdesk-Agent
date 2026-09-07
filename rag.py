from langchain_community.document_loaders import DirectoryLoader, TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma


DATA_PATH = "knowledge"
DB_PATH = "chroma_db"


def get_embeddings():

    return OllamaEmbeddings(
        model="nomic-embed-text"
    )


def create_vector_store():

    print("Loading knowledge documents...")

    loader = DirectoryLoader(
        DATA_PATH,
        glob="**/*.txt",
        loader_cls=TextLoader,
        loader_kwargs={"encoding": "utf-8"}
    )

    documents = loader.load()

    print(f"Loaded {len(documents)} documents")

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100
    )

    chunks = splitter.split_documents(documents)

    print(f"Created {len(chunks)} chunks")

    print("Creating Ollama embeddings...")

    embeddings = get_embeddings()

    print("Creating Chroma vector database...")

    vectorstore = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=DB_PATH,
        collection_name="it_helpdesk"
    )

    print("Vector database created!")

    return vectorstore


def get_vector_store():

    embeddings = get_embeddings()

    vectorstore = Chroma(
        persist_directory=DB_PATH,
        embedding_function=embeddings,
        collection_name="it_helpdesk"
    )

    return vectorstore


def retrieve_documents(query):

    vectorstore = get_vector_store()

    retriever = vectorstore.as_retriever(
        search_kwargs={"k": 3}
    )

    documents = retriever.invoke(query)

    return documents