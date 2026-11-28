def run():
    import os
    from dotenv import load_dotenv

    from langchain_google_genai import ChatGoogleGenerativeAI
    from langchain_core.prompts import ChatPromptTemplate
    from langchain_core.output_parsers import StrOutputParser

    load_dotenv() # zczytujemy z .env klucz do gemini

    gemini_api_key = os.getenv("GEMINI_API_KEY")

    # klient LLM - tutaj gemini
    # https://docs.langchain.com/oss/python/integrations/chat/google_generative_ai
    llm = ChatGoogleGenerativeAI(
        model="gemini-flash-lite-latest",
        google_api_key=gemini_api_key,
        temperature=0.3,
        transport="rest"
    )

    input_from_user = "Hello Bob, how do I make the best scrambled eggs?"

    # Budujemy prompt - szablon rozmowy
    # system - rola modelu
    # user - użytkownik
    prompt = ChatPromptTemplate([
        ("system", "You are a helpful AI bot. Your name is Bob and you are a master egg chef."),
        ("user", "{question}"),
    ])

    # Łańcuch przetwarzania prompta
    # prompt -> LLM analizuje -> parser odsyła tekst
    chain = prompt | llm | StrOutputParser()

    # niestety ten fragment nie jest zbyt atrakcyjny - to struktura łańcucha
    print(chain)

    # Aby użyć łańcucha używamy invoke
    # dajemy dane wejściowe i odpowiedź
    response = chain.invoke({"question": input_from_user})

    print(response)