from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from langchain_google_genai import ChatGoogleGenerativeAI

llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0.0)

messages = [
    SystemMessage("You are a helpful assistant."),
    HumanMessage("こんにちは!私はジョンと言います!"),
    AIMessage(content="こんにちは、ジョンさん!どのようにお手伝いできますか?"),
    HumanMessage(content="私の名前がわかりますか?"),
]

ai_message = llm.invoke(messages)
print(ai_message.content)