import os


def clean_text(text):
    """
    Remove extra spaces, tabs, and newlines.
    """

    if not text:
        return ""

    text = text.replace("\n", " ")
    text = text.replace("\t", " ")

    return text.strip()


def ensure_directory(directory_path):
    """
    Create directory if it does not exist.
    """

    if not os.path.exists(directory_path):
        os.makedirs(directory_path)

    return directory_path