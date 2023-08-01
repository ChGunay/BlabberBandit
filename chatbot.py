import openai
from dotenv import dotenv_values
import argparse


config = dotenv_values(".env")

openai.api_key=config["OPENAI_API_KEY"] 

res = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages = [
        {"role": "user", "content": "Hello, who are you?"}
    ],
)


def main():
    parser = argparse.ArgumentParser(description='Chatbot')
    parser.add_argument("--personalty", type=str, help="Personality of the chatbot")
    
    args = parser.parse_args()
    mesages = []
    while True:
        try:
            userInput: str = input("You: ")
            mesages.append({"role":"user", "content": userInput})
            res = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages = mesages,
            )
            mesages.append(res["choices"][0]["message"].to_dict())
            print("Assistant: ",res["choices"][0]["message"]["content"])
        except KeyboardInterrupt:
            break
        

if __name__ == "__main__":
    main()