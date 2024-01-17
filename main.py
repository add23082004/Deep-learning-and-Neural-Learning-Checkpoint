import openai

openai.api_key = "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"

messages = [{"role": "system", "content": "You are a financial experts that specializes in real estate investment and negotiation"}]


def CustomChatGPT(user_input):
    messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply



