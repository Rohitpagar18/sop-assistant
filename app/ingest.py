#load + chunk + embed documents
from pathlib import Path
import time
import chromadb
DB_DIR = 'chroma_db'
COLLECTION_NAME="sops"
SOP_DIR = Path("data/sops")

def load_documents():
    """Read all .md files and return a list of {text, source} dicts"""
    documents = []

    for file_path in SOP_DIR.glob("*.md"):
        text = file_path.read_text(encoding="utf-8")
        documents.append({
            "text": text,
            "source":file_path.name
        })
    return documents

def split_into_chunks(doc):
    """Split one document into chunks one per '## ' section."""
    text = doc['text']
    sections = text.split("\n## ")
    title = sections[0].strip().splitlines()[0]

    chunks = []

    for i, section in enumerate(sections[1:],start=1):
        chunks.append({
            "text": f"{title}\n## {section.strip()}",
            "source": doc["source"],
            "chunk_id": f"{doc['source']}_{i}"
        })
    return chunks

def store_chunks(chunks):
    """Store the the chunks in chromaDB with embedings chromadbs default embedings"""
    
    client = chromadb.PersistentClient(path=DB_DIR) # Save to disk not memory
    collection = client.get_or_create_collection(name=COLLECTION_NAME)
    
    ids = [c["chunk_id"] for c in chunks]
    documents = [c["text"] for c in chunks]
    metadatas = [{"source": c["source"]} for c in chunks]

    collection.upsert(
        ids = ids,
        documents = documents,
        metadatas = metadatas,
    )
    print("Upsert Done")
    return collection.count()



if __name__ == "__main__":
    docs = load_documents()
    print(f"Loaded {len(docs)} documents")
    # for d in docs:
    #     print(f"- {d['source']}: {len(d['text'])} characters")

    all_chunks=[]
    for doc in docs:
        all_chunks.extend(split_into_chunks(doc))
    print(f"Created {len(all_chunks)} chunks")
    # print("\n---sample chunk---")
    # print(all_chunks[0]["chunk_id"])
    # print(all_chunks[0]['text'])

    total = store_chunks(all_chunks)
    print(f"Total stored chunks are {total} in chromaDB")