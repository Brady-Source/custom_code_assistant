
import os
from dotenv import load_dotenv
from openai import OpenAI
import argparse

# Loading our env variables and establishing the link to the API key
load_dotenv()
api_key = os.environ.get("OPENROUTER_API_KEY")
if api_key == None:
    raise RuntimeError("Check API Key, Nothing was found.")

# Setting API url to OpenRouter.
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key,
)

# Our Chatbot selection, message instruction, and data.
def chat():
    # PARSER - Adding an argument option for addition message data, of which will be declared later in args.verbose.
    parser = argparse.ArgumentParser(description="Chatbot") 
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    args = parser.parse_args()

    # Standard OpenAI semantics for LLM communications: Messangers role, Instructions, Content, ...ect
    messages = [{"role": "user", "content": args.user_prompt},]

    response = client.chat.completions.create(
        model="openrouter/free", # Selecting the free tier models on Open Routers platform.
        messages=messages
    )
    if args.verbose: # Return LLM query data prior to the LLM response.
        return f"User prompt: {args.user_prompt}\nPrompt tokens: {response.usage.prompt_tokens}\nResponse tokens: {response.usage.completion_tokens}\nResponse:\n{response.choices[0].message.content}"
    else: # Just resturns the LLM response if --verbose is NOT called.
        return f"Response:\n{response.choices[0].message.content}"

def main():
    print(chat())


if __name__ == "__main__":
    main()
