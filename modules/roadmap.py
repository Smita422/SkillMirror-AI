from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

def generate_roadmap(role):

    prompt = f"""
    Create an advanced 6-month roadmap
    for becoming a successful {role}.

    Include:
    - weekly goals
    - tools
    - projects
    - certifications
    - interview preparation
    - GitHub strategy
    """

    completion = client.chat.completions.create(

        model="llama-3.3-70b-versatile",

        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],

        temperature=0.7
    )

    return completion.choices[0].message.content