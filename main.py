from langchain_ollama import ChatOllama
# from langchain_core.prompts import ChatPromptTemplate

llm = ChatOllama(
    model="llama3.1:8b",
    temperature=0
)

msg = llm.invoke("hello!")
print(msg.content)