from langchain_community.vectorstores import Chroma
from langchain_mistralai import MistralAIEmbeddings
from dotenv import load_dotenv

load_dotenv()
from langchain_core.documents import Document

docs= [ 
    Document(page_content="python is widely used in ai.", metadata={"source": "ai_book"}),
    Document(page_content="pandas is used for data analysis in python", metadata={"source": "datascience_book"}),
    Document(page_content="neural networks are a used in deep learning", metadata={"source": "deeplearning_book"} )]

embeddings_model = MistralAIEmbeddings(model="mistral-embed")
vectorstore = Chroma.from_documents(documents=docs, embedding=embeddings_model,persist_directory="chroma_db")
result =vectorstore.similarity_search("what is used for data analysis in python?", k=1)
for r in result :
    print(r)

