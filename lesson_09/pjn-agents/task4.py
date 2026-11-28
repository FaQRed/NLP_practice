# Zadanie 1
# Uwaga: zadanie może być wykonane na przeróżne sposoby
# Stwórz Agenta AI, który zapamięta konwersacje - zarówno prompty użytkownika jak i własne odpowiedzi
# Przetestuj na podanej kowersacji

def run():
    import os
    from dotenv import load_dotenv

    from langchain_google_genai import ChatGoogleGenerativeAI
    from langchain.agents import create_agent
    from langgraph.checkpoint.memory import InMemorySaver

    load_dotenv()
    gemini_api_key = os.getenv("GEMINI_API_KEY")

    llm = ChatGoogleGenerativeAI(
        model="gemini-flash-lite-latest",
        google_api_key=gemini_api_key,
        temperature=0.3,
    )

    agent = create_agent(
        model=llm,
        tools=[],
        system_prompt="You are a helpful AI assistant. Remember details from the conversation.",
        checkpointer=InMemorySaver()
    )

    messages = [
        "My name is John",
        "I live in Berlin",
        "Where do I live and what is my name?"
    ]

    config = {"configurable": {"thread_id": "john_thread"}}

    for msg in messages:
        print(f"User: {msg}")
        response = agent.invoke(
            {"messages": [{"role": "user", "content": msg}]},
            config=config
        )
        last_msg = response["messages"][-1].content
        text = last_msg[0]["text"] if isinstance(last_msg, list) else last_msg
        print(f"Bot:  {text}\n")