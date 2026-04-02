from app.utils.llm import call_llm

def tutor_guidance(scenario: str) -> str:

    messages = [
        {
            "role": "system",
            "content": "You are a senior mentor guiding a junior professional before they take action."
        },
        {
            "role": "user",
            "content": f"""
A user is about to handle this situation:

{scenario}

Before they act, guide their thinking.

Include:
- How they should approach the problem
- Key things to consider
- Common mistakes to avoid

Rules:
- Do NOT give the solution
- Keep it concise
- Focus on thinking, not instructions
"""
        }
    ]

    return call_llm(messages)