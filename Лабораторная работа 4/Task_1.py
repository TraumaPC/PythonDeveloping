# TODO решите задачу
import json

FILENAME = "input.json"


def task() -> float:
    with open(FILENAME, 'r') as f:
        data = json.load(f)
        result = sum(i['score'] * i['weight'] for i in data)
        return round(result, 3)


print(task())
