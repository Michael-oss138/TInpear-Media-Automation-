from groq import Client

client = Client(api_key="GROQ_API_KEY")

models = client.models.list()
print("Available models for this API key:")
for model in models.data:
    print(model.id)
