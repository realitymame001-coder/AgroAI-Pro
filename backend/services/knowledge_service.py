import json

def load_diseases():
    with open("knowledge-base/diseases/fungal.json") as f:
        return json.load(f)
