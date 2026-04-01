import json
def save(data, filename="passwords.json"):
    with open(filename, "w") as f:
        json.dump(data, f)
