import openai
from dotenv import dotenv_values
import argparse


def bold(text):
    bold_start = "\033[1m"
    bold_end = "\033[0m"
    return bold_start + text + bold_end


def blue(text):
    blue_start = "\033[34m"
    blue_end = "\033[0m"
    return blue_start + text + blue_end


def red(text):
    red_start = "\033[31m"
    red_end = "\033[0m"
    return red_start + text + red_end


def main():
    config = dotenv_values(".env")

    parser = argparse.ArgumentParser(description='Chatbot')
    parser.add_argument("--personalty", type=str,
                        help="Personality of the chatbot", default="friendly")
    parser.add_argument("--aiKey", type=str,
                        help="OpenAI API Key", default=config["OPENAI_API_KEY"])

    args = parser.parse_args()
    openai.api_key = args.aiKey
    print("openai.api_key", openai.api_key)

    initial_message = f"You are a conversation partner. Your personality is. {args.personalty}"
    mesages = [{"role": "user", "content": initial_message}]
    while True:
        try:
            userInput: str = input(bold(blue("You: ")))
            mesages.append({"role": "user", "content": userInput})
            res = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=mesages,
            )
            mesages.append(res["choices"][0]["message"].to_dict())
            print(bold(red("Assistant: ")),
                  res["choices"][0]["message"]["content"])
        except KeyboardInterrupt:
            break


if __name__ == "__main__":
    main()
