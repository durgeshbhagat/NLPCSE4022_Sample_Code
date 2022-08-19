"""A tool for reading text files with an unknown encoding."""

from pathlib import Path
import sys

import cchardet as chardet


def read_confidently(filename):
    """Detect encoding and return decoded text, encoding, and confidence level."""
    filepath = Path(filename)

    # We must read as binary (bytes) because we don't yet know encoding
    blob = filepath.read_bytes()

    detection = chardet.detect(blob)
    encoding = detection["encoding"]
    confidence = detection["confidence"]
    text = blob.decode(encoding)

    return text, encoding, confidence


def main():
    """Command runner."""
    filename = sys.argv[1]  # assume first command line argument is filename
    text, encoding, confidence = read_confidently(filename)
    print(text)
    print(f"Encoding was detected as {encoding}.")
    if confidence < 0.6:
        print(f"Warning: confidence was only {confidence}!")
        print("Please double-check output for accuracy.")


if __name__ == "__main__":
    main()
