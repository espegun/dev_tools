import requests

# Call as URl
result = requests.get("http://localhost:5000/?msg=Helleau")
print(result.json())

# Call with GET
result = requests.get("http://localhost:5000/", params = {"msg": "Helleau with GET"})
print(result.json())

# Call with POST
result = requests.post("http://localhost:5000/", params = {"msg": "Helleau with POST"})
print(result.json())
