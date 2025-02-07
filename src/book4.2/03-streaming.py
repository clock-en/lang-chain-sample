from langchain_core.messages import SystemMessage, HumanMessage
from langchain_google_genai import ChatGoogleGenerativeAI

llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0.0)

messages = [
    SystemMessage("You are a helpful assistant."),
    HumanMessage("こんにちは!"),
]

response = llm.stream(messages)
for chunk in response:
    print(chunk.content, end="", flush=True)
