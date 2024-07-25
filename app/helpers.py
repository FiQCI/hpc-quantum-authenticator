import os
import re

def string_sanitizer(filename):
    """
    Sanitizes a given filename by replacing disallowed characters with underscores.

    Args:
        filename (str): The filename to sanitize.

    Returns:
        str: The sanitized filename.
    """
    return re.sub(r'[^a-zA-Z0-9_.-]', '_', str(filename))


def file_helper(token, action="create"):
    """
    Performs file operations such as create, delete, and validate based on the action specified. The default action is create

    Args:
        token (str): The token used to generate the filename.
        action (str): The action to perform ('create', 'delete', 'validate'). Defaults to 'create'.

    Returns:
        bool: True if the file exists (only for 'validate' action), otherwise False.
    """

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
    """
    Validates and converts specified keys in a dictionary to strings.

    Args:
        data (dict): The dictionary (request_obj) containing the data.
        required_keys (list): The list of keys that need to be validated and converted.

    Returns:
        dict: A dictionary with the required keys.
        None: If any required key is missing in the data.
    """

    try:
        return {key: str(data[key]) for key in required_keys}
    except KeyError:
        return None