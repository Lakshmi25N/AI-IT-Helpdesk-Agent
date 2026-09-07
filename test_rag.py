from rag import retrieve_documents


query = "My laptop is connected to WiFi but internet is not working"


print("\nUSER QUERY:")
print(query)

print("\nRETRIEVED DOCUMENTS:")
print("=" * 60)

documents = retrieve_documents(query)

for i, document in enumerate(documents):

    print(f"\nRESULT {i + 1}")
    print("-" * 60)

    print(document.page_content)