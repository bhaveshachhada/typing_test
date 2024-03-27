import argparse
import string
import time
import random
import keyboard


def fetch_text_from_file(filepath: str) -> str:
    with open(filepath, 'r') as file:
        content = file.read()
    return content


def start_typing(text: str, wpm: int = 60):
    words = text.split()
    num_words = len(words)
    minutes = num_words / wpm
    unit_delay = (minutes * 60) / (num_words - 1)
    for word in words:
        keyboard.write(word, unit_delay)


def add_noise(original_text: str, accuracy: float = 0.5) -> str:
    words = original_text.split()
    total_words = len(words)
    noisy_indexes = random.sample(range(total_words), int(total_words * (1 - accuracy)))
    for index in noisy_indexes:
        words[index] += random.choice(string.ascii_letters)
    return " ".join(words)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Automatic typing helper")
    parser.add_argument("--file", type=str, help="Path of text file to type", default="test")
    args = parser.parse_args()

    time.sleep(5)

    file_content = fetch_text_from_file(args.file)

    text_to_be_typed = add_noise(file_content, accuracy=0.1)
    start_typing(text_to_be_typed, wpm=62)
