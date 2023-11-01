import json


def output_response(response) -> None:
    if not response:
        print("There's no response.")
    else:
        print(response)
    print("-----")


def is_answer_formatted_in_json(answer):
    try:
        json.loads(answer, strict=False)
        return True
    except ValueError:
        return False


def format_escape_characters(s):
    return s.replace('"', '\\"').replace("\n", "\\n")


def transform_source_docs(result):
    formatted_result_string = format_escape_characters(result["result"])
    if 'source_documents' in result.keys():
        return f"""
            {{
            "result": "{formatted_result_string}",
            "sources": {json.dumps([i.metadata for i in result['source_documents']])}
            }}"""
    return f"""
        {{
        "result": "{formatted_result_string}",
        "sources": []
        }}"""
