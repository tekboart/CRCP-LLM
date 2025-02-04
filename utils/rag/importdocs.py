# XXX: from "https://github.com/technovangelist/videoprojects/tree/main/2024-09-10-buildrag/python" (but fixed bugs so that it works with chromadb v0.6.0)
import chromadb
from functions import readtextfiles, chunksplitter, getembedding


# XXX: ******* Run "chroma run --port 8000" in terminal before running this file

# TODO: Check whether the "host:port" exists and works
chromaclient = chromadb.HttpClient(host="localhost", port=55555)
# E.g.,
# textdocspath = "../../scripts"
textdocspath = "./data/literature"

text_data = readtextfiles(textdocspath)
print(f'{text_data = }')

# Method 1: Gives error
# NAME_OF_THE_COLLECTION = "buildragwithpython"
# collection = chromaclient.get_or_create_collection(name=NAME_OF_THE_COLLECTION, metadata={"hnsw:space": "cosine"}  )
# if any(collection.name == collectionname for collection in chromaclient.list_collections()):
#   chromaclient.delete_collection(NAME_OF_THE_COLLECTION)


# Method 2: (ME)
# TODO: Use "https://docs.trychroma.com/docs/overview/getting-started" to implement a chromadb collection properly
collection_names = chromaclient.list_collections()
print(f'{collection_names = }')
collections = [
  chromaclient.get_or_create_collection(name=name, metadata={"hnsw:space": "cosine"})
  for name in collection_names
]
collection_names = chromaclient.list_collections()
print(f'{collection_names = }')

# if any(collection.name == collectionname for name in chromaclient.list_collections()):
#   chromaclient.delete_collection(NAME_OF_THE_COLLECTION)

for filename, text in text_data.items():
  chunks = chunksplitter(text)
  print(f"{chunks[0] = }")
  embeds = getembedding(chunks)
  chunknumber = list(range(len(chunks)))
  ids = [filename + str(index) for index in chunknumber]
  metadatas = [{"source": filename} for index in chunknumber]
  collections.add(ids=ids, documents=chunks, embeddings=embeds, metadatas=metadatas)
