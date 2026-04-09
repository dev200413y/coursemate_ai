from langchain_community.document_loaders import Document
from langchain_community.vectorstores import Chroma
from langchain_cummuntiy.embeddings import HuggingFaceEmbeddings

docs = [
    Document(page_content="gradient descent is an optimization algorithm used in machine learing"),
    Document(page_content="gradient descent is used to minimize the loss function"),
    Document(page_content="gradient descent is an op-ptimaztion that minimizes the loss function by iteratively updating the model parameters in the direction of the negative gradient of the loss function with respect to the parameters"),
    Document(page_content="neaural netwosk use gradient descent for trainig"),
    Document(page_content="support  vector machines are supervised leaning algorithms")
    

]
embeddings_model = HuggingFaceEmbeddings()
vectorstore = Chroma.from_documents(docs, embeddings)
similarity_retriever = vectorstore.as_retriever(
    search_type="similarity",
    search_kwargs={"k": 2}  #top 2 similar search
)
print("-\n similarity search results:   ")
similarity_docs = similarity_retriever.invoke("what is gradient descent?")
for doc in similarity_docs:
    print(doc.page_content)

'''mmr_retriever = vectorstore.as_retriever(
    search_type="mmr",
    search_kwargs={"k": 3}
)'''