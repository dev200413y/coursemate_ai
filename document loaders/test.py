from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import CharacterTextSplitter
from langchain_text_splitters import TokenTextSplitter
from langchain_community.document_loaders import PyPDFLoader
"""
spiltter = CharacterTextSplitter(
    separator="",
    chunk_size=10,
    chunk_overlap=1)

data = TextLoader("document loaders/notes.txt")
docs = data.load()
chunks = spiltter.split_documents(docs)
print(len(chunks))

for i in chunks:
    print(i.page_content)
    print()
    print()
    print()

"""
data = PyPDFLoader("document loaders\GRU.pdf")
docs = data.load()
splitter = TokenTextSplitter(chunk_size=1000, chunk_overlap=100)
chunks = splitter.split_documents(docs)
print(len(chunks))
for i in chunks:
    print(i.page_content)
    print()
    print()
    print()
    print()