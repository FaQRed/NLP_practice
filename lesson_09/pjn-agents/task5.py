# Zadanie 2
# 1) Załaduj klucz Gemini API key
# 2) Stwórz funkcję wiki-search, która przyjmuje temat zapytania i zwraca krótki opis z wikipedii
# 3) Tworzymy Agenta LangChain sugerowany model="gemini-2.5-flash"
# 4) Agent korzysta z narzędzia jeśli nie zna odpowiedzi
# 5) Agent zwraca odpwiedź 

def run():
    import os
    import wikipedia
    from dotenv import load_dotenv
    from langchain_google_genai import ChatGoogleGenerativeAI
    from langchain.tools import tool
    from langchain.agents import create_agent

    load_dotenv()

    @tool("wiki-search")
    def wiki_search(topic: str) -> str:
        """Search Wikipedia for a topic and return a short summary."""
        print(f"[wiki-search] Searching: {topic}")
        return wikipedia.summary(topic, sentences=2)

    llm = ChatGoogleGenerativeAI(
        model="gemini-flash-lite-latest",
        google_api_key=os.getenv("GEMINI_API_KEY"),
    )

    agent = create_agent(
        model=llm,
        tools=[wiki_search],
        system_prompt="Always use wiki-search to look up facts about topics, people, or places. Base your answer on its result. Keep your answers concise (2-3 sentences)."
    )


    user_inputs = [
        "Remind me to buy milk",
        "Tell me about Python programming",
        "Tell me about the Eiffel Tower"
    ]

    for query in user_inputs:
        res = agent.invoke({"messages": [{"role": "user", "content": query}]})
        msg = res["messages"][-1].content
        text = msg[0]["text"] if isinstance(msg, list) else msg
        print(f"User: {query}\nBot:  {text}\n")