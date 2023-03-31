import openai


openai.api_key = "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"

messages = [{"role": "system", "content": "You are an empathetic friend that listens and provides guidance only, you respond to no other questions other than emotional ones."}]

def CustomChatGPT(user_input):
    messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply

print("Type your concerns here! I will hear them out!\nType 'Exit' to exit.")
user_input = input("\n")
if user_input == "Exit":
    exit()
print()
while(user_input != "Exit"):
    response = CustomChatGPT(user_input)
    print(response)
    print()

    user_input = input("")
    print()