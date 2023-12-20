from openai import OpenAI

client = OpenAI(
    api_key="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"
)

response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": "how are you?"}],
)

print(response)
