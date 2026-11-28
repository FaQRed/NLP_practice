def run():
    import os
    from dotenv import load_dotenv

    from langchain_google_genai import ChatGoogleGenerativeAI
    from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
    from langchain_core.output_parsers import StrOutputParser
    from langchain.tools import tool
    from langchain_classic.agents import AgentExecutor, create_openai_tools_agent


    load_dotenv() 

    gemini_api_key = os.getenv("GEMINI_API_KEY")

    # Dekorator tool zamienia funkcję w narzędzie,
    # które może być użyte przez agenta
    @tool("task-tool")
    def add_task():
        """
        Add a new task for user's task list. Use this when user wants to add or update list.
        """
        print("I'm adding a task") #Tutaj możemy dodać jakąś logikę - np odwołanie do API naszej aplikacji notatnika i dopisanie zadania

    @tool("call-tool")
    def call_someone():
        """
        Call a contact from user's contact list. Use this when user want's to call someone.
        """
        print("I am calling someone")

    # Wszystkie narzędzie które zna agent
    tools = [add_task, call_someone]

    llm = ChatGoogleGenerativeAI(
        model="gemini-flash-lite-latest",
        google_api_key=gemini_api_key,
        temperature=0.3
    )

    input_from_user = "Call my mom"

    # Placeholder na wiadomości agenta - musi być
    # Agent_scratchpad - agent przechowuje tam mysli, polecenia narzedzi, wyniki zwrócone przez narzędzia
    prompt = ChatPromptTemplate([
        ("system", "You are a helpful AI bot. Your name is Bob."),
        ("user", "{question}"),
        MessagesPlaceholder("agent_scratchpad")
    ])

    # Tworzenie agenta
    # podajemy llm'a, narzędzia dostępne oraz prompt
    agent = create_openai_tools_agent(llm, tools, prompt)

    # Executor to nasz silnik
    # obsługuje pętle LLM -> narzędzia -> LLM....
    # zarządza wykonywaniem narzędzi
    agent_executor = AgentExecutor(agent = agent, 
                                   tools=tools, 
                                   verbose=True) # zoabaczymy co agent myśli

    # Wywołujemy agenta z danym pytaniem / poleceniem
    response = agent_executor.invoke({"question": input_from_user})

    print(response)