# TODO решите задачу
import json


def task(json_file_path) -> float:
    with open(json_file_path, 'r') as file:
        data = json.load(file)
    total_sum = sum([item['score'] * item['weight'] for item in data])
    return round(total_sum, 3)


print(task('input.json'))
