from openai import OpenAI
#client = OpenAI(api_key="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")
client = OpenAI(api_key="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")
f = open("rec.txt", "r")
text = f.read()
response = client.chat.completions.create(
  model="davanci-002",
  messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Who won the world series in 2020?"},
    {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
    {"role": "user", "content": "Where was it played?"}
  ]
)