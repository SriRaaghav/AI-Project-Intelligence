from rag.retriever import get_retriever

retriever = get_retriever()

query = "What are the key objectives of this project?"

results = retriever.invoke(query)

print("=" * 80)

for i, doc in enumerate(results, 1):
    print(f"\nResult {i}\n")
    print(doc.page_content[:500])