import os
import random
import hashlib
import subprocess
import json

def calculate_file_hash(file_path):
    sha256_hash = hashlib.sha256()
    with open(file_path, "rb") as file:
        for chunk in iter(lambda: file.read(4096), b""):
            sha256_hash.update(chunk)
    return sha256_hash.hexdigest()

def get_audio_duration(file_path):
    result = subprocess.run(["ffprobe", "-v", "quiet", "-print_format", "json", "-show_format", file_path], stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)
    output = json.loads(result.stdout.decode('utf-8'))
    duration = float(output['format']['duration'])
    return duration

def play_audio_sample(file_path, duration, position):
    subprocess.run(["ffplay", "-nodisp", "-autoexit", "-ss", str(position), "-t", str(duration), file_path], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

def main():
    input_file = "input.wav"

    # Calculate the hash of the input file
    file_hash = calculate_file_hash(input_file)
    output_directory = file_hash

    # Get a list of all the files in the hash folder
    hash_files = []
    for root, dirs, files in os.walk(output_directory):
        for file in files:
            hash_files.append(os.path.join(root, file))

    if not hash_files:
        print("No files found in the hash folder.")
        return

    # Get the duration of the input file
    input_duration = get_audio_duration(input_file)

    # Initialize variables for tracking score and missed files
    total_files = len(hash_files)
    correct_guesses = 0
    missed_files = []

    # Play each file once
    while hash_files:
        # Randomly select a file from the hash folder
        selected_file = random.choice(hash_files)
        hash_files.remove(selected_file)

        # Determine the random position and duration
        duration = 5  # Play audio for 5 seconds
        max_position = input_duration - duration
        random_position = random.uniform(0, max_position)

        # Randomly decide the order of playing the original and selected file
        play_order = random.sample([input_file, selected_file], 2)

        # Play the audio samples in the shuffled order
        for i, file_path in enumerate(play_order, start=1):
            print(f"Playing audio sample {i}...")
            play_audio_sample(file_path, duration, random_position)

        # Ask the user to identify which is which
        answer = input("Which audio sample is the original? (1 or 2): ")
        if play_order[int(answer) - 1] == input_file:
            print("Correct! You identified the original audio sample.")
            correct_guesses += 1
        else:
            print("Incorrect! You did not identify the original audio sample.")
            missed_files.append(selected_file)

        print("\nPlayed audio samples:")
        print(f"Audio sample 1: {play_order[0]}")
        print(f"Audio sample 2: {play_order[1]}")
        print()

    # Calculate the average score
    average_score = correct_guesses / total_files * 100

    # Print the breakdown
    print("Breakdown:")
    print(f"Total files: {total_files}")
    print(f"Correct guesses: {correct_guesses}")
    print(f"Missed files: {len(missed_files)}")
    print(f"Average score: {average_score:.2f}%")

    if missed_files:
        print("\nMissed files:")
        for file in missed_files:
            print(file)

if __name__ == "__main__":
    main()

