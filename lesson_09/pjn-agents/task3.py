def run():
    import os
    from dotenv import load_dotenv

    from langchain_google_genai import ChatGoogleGenerativeAI
    from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
    from langchain_core.output_parsers import StrOutputParser
    from langchain.tools import tool
    from langchain_classic.agents import AgentExecutor, create_openai_tools_agent


    load_dotenv() # zczytujemy z .env

    gemini_api_key = os.getenv("GEMINI_API_KEY")

    # teraz używamy argumentu w funkcji
    # dlatego że używamy llma możemy wyciagnąć konkretny task
    # np pomijając "please", "remind me" etc
    @tool("task-tool")
    def add_task(task):
        """
        Add a new task for user's task list. Use this when user wants to add or update list.
        """
        print("I'm adding a task")
        print("Task: ", task)

    @tool("call-tool")
    def call_someone(contact):
        """
        Call a contact from user's contact list. Use this when user want's to call someone.
        """
        print("I am calling someone")
        print("Contact: ", contact)

    @tool("play-music")
    def play_music(song):
        """
        Try to play a song from user's library.
        """
        # Przykład z returnem
        return "Music player is out of reach"

    tools = [add_task, call_someone, play_music]

    llm = ChatGoogleGenerativeAI(
        model="gemini-flash-lite-latest",
        google_api_key=gemini_api_key,
        temperature=0.3
    )

    #input_from_user = "Call my mom"
    input_from_user = "Add task to buy grandma flowers"
    #input_from_user = "Play Despacito"

    prompt = ChatPromptTemplate([
        ("system", "You are a helpful AI bot. Your name is Bob."),
        ("user", "{question}"),
        MessagesPlaceholder("agent_scratchpad") 
    ])

    agent = create_openai_tools_agent(llm, tools, prompt)
    agent_executor = AgentExecutor(agent = agent, 
                                   tools=tools, 
                                   verbose=True) 

    response = agent_executor.invoke({"question": input_from_user})

    print(response)