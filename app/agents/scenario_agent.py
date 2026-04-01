from app.utils.llm import call_llm

def generate_scenario(role: str, level: str = "beginner") -> str:
    
    messages = [
        {
            "role": "system",
            "content": "You are an expert creating realistic job scenarios for learners."
        },
        {
            "role": "user",
            "content": f"""
                Create a realistic scenario for a {level} {role}.

                Include:
                - Context (where they are working)
                - Problem (what went wrong or needs to be solved)
                - Stakes (why it matters)

                Keep it practical and real-world. No generic teaching.
                """
        }
        ]

    return call_llm(messages)