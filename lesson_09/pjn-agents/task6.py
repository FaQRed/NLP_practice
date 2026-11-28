# Zadanie 3
# Utwórz agenta z dwoma narzędziami dostępnymi:
# - ładowarką pdfów
# - narzędzie do streszcznia tekstów (tu moze być inny llm, dowolnie)
# Agent dostaje pdf (przykłąd w folderze: example.pdf) i zwraca streszczoną wersję użytkownikowi

def run():
    import os
    from pathlib import Path
    from dotenv import load_dotenv
    from pypdf import PdfReader

    from langchain_google_genai import ChatGoogleGenerativeAI
    from langchain.tools import tool
    from langchain.agents import create_agent

    load_dotenv()
    gemini_api_key = os.getenv("GEMINI_API_KEY")


    llm = ChatGoogleGenerativeAI(
        model="gemini-flash-lite-latest",
        google_api_key=gemini_api_key,
        temperature=0.3
    )


    @tool("load-pdf")
    def load_pdf(file_path: str) -> str:
        """Load and extract all text from a PDF file given its path."""
        print(f"[load-pdf] Reading: {file_path}")
        reader = PdfReader(file_path)
        return "\n".join(page.extract_text() or "" for page in reader.pages)


    @tool("summarize-text")
    def summarize_text(text: str) -> str:
        """Summarize the provided text into a concise overview."""
        print("[summarize-text] Summarizing text...")
        res = llm.invoke(f"Summarize the following text concisely:\n\n{text}")
        content = res.content
        return content[0]["text"] if isinstance(content, list) else content


    agent = create_agent(
        model=llm,
        tools=[load_pdf, summarize_text],
        system_prompt="You are a helpful assistant. When asked to summarize a PDF, first use 'load-pdf' to read it, "
                      "then use 'summarize-text' to create the summary. Answer without makdown formatting"
    )

    pdf_path = "./example.pdf"
    user_request = f"Please load the PDF file at '{pdf_path}' and summarize its content."

    response = agent.invoke({"messages": [{"role": "user", "content": user_request}]})

    last_msg = response["messages"][-1].content
    final_text = last_msg[0]["text"] if isinstance(last_msg, list) else last_msg
    print("\nSummary:\n", final_text)