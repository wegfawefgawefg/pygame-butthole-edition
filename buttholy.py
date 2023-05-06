import os
import re

source_folder = "/path/to/pygame/source"


def rename_function_defs(match):
    name = match.group(1)
    return f"def butthole_{name}"


def rename_function_calls(match):
    name = match.group(1)
    return f"butthole_{name}"


def process_file(file_path):
    with open(file_path, "r") as f:
        content = f.read()

    # Rename function definitions with the format "def function_name", excluding those starting with underscores
    content = re.sub(r"def (?<!_)(\w+)", rename_function_defs, content)

    # Rename function calls, excluding those starting with underscores
    content = re.sub(
        r"(?<![\w_])(?<!butthole_)(?<!_)(\w+)\(", rename_function_calls, content
    )

    with open(file_path, "w") as f:
        f.write(content)


for root, _, files in os.walk(source_folder):
    for file in files:
        if file.endswith(".py"):
            file_path = os.path.join(root, file)
            process_file(file_path)
