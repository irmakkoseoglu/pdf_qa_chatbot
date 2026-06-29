# LLM Configurations
LLM_PROVIDER = "ollama"        # "ollama" 
OLLAMA_MODEL = "tinyllama"

# Embedding from HuggingFace
EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"

# ChromaDB Vector Database Configurations
CHROMA_COLLECTION = "pdf_collection"

# Chunk configurations for text splitting
CHUNK_SIZE = 1000
CHUNK_OVERLAP = 200