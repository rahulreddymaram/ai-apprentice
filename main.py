from app.utils.llm import call_llm

def main():
    prompt = """
You are a mentor.

Explain what an AI engineer does:
- in simple terms
- with a real-world example
- in under 150 words
"""

    response = call_llm(prompt)

    print("\n--- AI Response ---\n")
    print(response)

if __name__ == "__main__":
    main()