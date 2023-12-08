import time
import random
import sys

def type_text_slowly(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.1)
    print()  # Move to the next line after typing the text

def follow_generator():
    type_text_slowly("█▀▀ █░░ █░░░█   ▀█░█▀ █▀▀█")
    type_text_slowly("█▀▀ █░░ █▄█▄█   ░█▄█░ ░░▀▄")
    type_text_slowly("▀░░ ▀▀▀ ░▀░▀░   ░░▀░░ █▄▄█")
    num_followers = int(input("How many followers do you want to generate? "))
    type_text_slowly("Initializing Follow API v2...")

    for _ in range(num_followers):
        fake_username = generate_fake_username()
        type_text_slowly(f"Loading... Follower {fake_username} added")
        time.sleep(random.uniform(0.2, 0.7))  # Random delay between 0.2 and 0.7 seconds

def generate_fake_username():
    prefixes = ["john", "jane", "cool", "super", "mega", "ultra", "awesome"]
    suffix = random.randint(100, 999)
    return random.choice(prefixes) + "guy" + str(suffix)

if __name__ == "__main__":
    follow_generator()
