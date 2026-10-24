#load + chunk + embed documents
from pathlib import Path
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
if __name__ == "__main__":
    docs = load_documents()
    print(f"Loaded {len(docs)} documents")
    for d in docs:
        print(f"- {d['source']}: {len(d['text'])} characherts")