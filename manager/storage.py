import json
def save(data, filename="passwords.json"):
    with open(filename, "w") as f:
        json.dump(data, f)
def load(filename="passwords.json"):
    try:
        with open(filename) as f:
            return json.load(f)
    except:
        return []
