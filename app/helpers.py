import os
import re

def string_sanitizer(filename):
    return re.sub(r'[^a-zA-Z0-9_.-]', '_', str(filename))


def file_helper(token, action="create"):
    sanitized_token = string_sanitizer(token)
    filename = f"{sanitized_token}.txt"
    directory = "tokens"
    os.makedirs(directory, exist_ok=True)
    file_path = os.path.join(directory, filename)

    if action == "create":
        if not os.path.exists(file_path):
            open(file_path, 'w').close()
    elif action == "delete":
        if os.path.exists(file_path):
            os.remove(file_path)
    elif action == "validate":
        return os.path.exists(file_path)
    return False


def validate_and_stringify(data, required_keys):
    try:
        return {key: str(data[key]) for key in required_keys}
    except KeyError:
        return None