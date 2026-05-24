import json


def read_text_file(file_path):
    file = open(file_path, "r", encoding="utf-8")
    text = file.read()
    file.close()

    return text


def save_result_as_json(result, output_path):
    file = open(output_path, "w", encoding="utf-8")
    json.dump(result, file, indent=4)
    file.close()