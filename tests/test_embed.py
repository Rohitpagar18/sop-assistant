import time
from chromadb.utils import embedding_functions
ef = embedding_functions.DefaultEmbeddingFunction()
start = time.time()
vector = ef(["reset my password"])
print(f"vector length : {len(vector[0])}")
print(f"Took {time.time() - start:.2f} seconds")