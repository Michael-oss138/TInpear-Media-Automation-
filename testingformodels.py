from groq import Client

client = Client(api_key="GROQ_API_KEY")

try:
    models = client.models.list()
    print("API key works! Models available:")
    for model in models.data:
        print(model.id)
except Exception as e:
    print("Error with API key:", e)
