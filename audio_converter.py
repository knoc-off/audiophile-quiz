import os
import hashlib
import ffmpeg
import json

def calculate_file_hash(file_path):
    sha256_hash = hashlib.sha256()
    with open(file_path, "rb") as file:
        for chunk in iter(lambda: file.read(4096), b""):
            sha256_hash.update(chunk)
    return sha256_hash.hexdigest()

def create_directory(directory_name):
    if not os.path.exists(directory_name):
        os.makedirs(directory_name)

def convert_audio(input_file, output_file, codec, bitrate):
    if codec == "opus":
        codec = "libopus"
    try:
        if not os.path.exists(output_file):
            stream = ffmpeg.input(input_file)
            stream = ffmpeg.output(stream, output_file, acodec=codec, audio_bitrate=bitrate)
            ffmpeg.run(stream)
        else:
            print(f"Skipping conversion for {output_file}. File already exists.")
    except ffmpeg.Error as e:
        print(f"Skipping conversion for {codec} codec. Error: {e}")
        return codec
    return None

def load_codecs_and_qualities(json_file):
    with open(json_file, "r") as file:
        data = json.load(file)
    return data

def main():
    input_file = "input.wav"
    json_file = "codecs_and_qualities.json"

    # Load codecs and qualities from the JSON file
    codecs_and_qualities = load_codecs_and_qualities(json_file)

    # Calculate the hash of the input file
    file_hash = calculate_file_hash(input_file)

    # Create a directory with the file hash as the name
    output_directory = file_hash
    create_directory(output_directory)

    # Initialize a list to store skipped formats
    skipped_formats = []

    # Convert the input file to various codecs and qualities
    for codec, bitrates in codecs_and_qualities.items():
        codec_directory = f"{output_directory}/{codec}"
        create_directory(codec_directory)

        for bitrate in bitrates:
            output_file = f"{codec_directory}/{bitrate}.{codec}"
            skipped_codec = convert_audio(input_file, output_file, codec, bitrate)
            if skipped_codec is not None:
                skipped_formats.append(skipped_codec)

    print("Audio conversion completed.")

    # Display the list of skipped formats
    if skipped_formats:
        print("\nSkipped Formats:")
        for format in set(skipped_formats):
            print(format)
    else:
        print("\nNo formats were skipped.")

if __name__ == "__main__":
    main()

