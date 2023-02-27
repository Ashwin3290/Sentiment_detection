import requests
data = {"string": "I am happy"}
response = requests.post("http://0.0.0.0:7860/?token=qzq35s37exvylasgddj7f4mogqhv72z2/sentiment", json=data)
print(response.json())