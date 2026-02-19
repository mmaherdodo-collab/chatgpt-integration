import os
from openai import OpenAI

# Initialize the OpenAI client with API key from environment variable
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def chat_with_gpt(message):
    """Send a message to ChatGPT and get a response"""
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "user", "content": message}
        ]
    )
    return response.choices[0].message.content

if __name__ == "__main__":
    # Example: Send a message to ChatGPT
    user_message = "Hello! What are the top 3 benefits of using GitHub Actions?"
    
    print(f"User: {user_message}")
    print("-" * 50)
    
    response = chat_with_gpt(user_message)
    print(f"ChatGPT: {response}")