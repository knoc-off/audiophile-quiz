# Audio Conversion Script

This repository contains a Python script that converts audio files to various codecs and bitrates. It aims to provide a wide range of options for compressing audio, including popular formats like MP3, AAC, and Opus, as well as some lesser-known codecs.

## Disclaimer: Audiophile Myths and Misconceptions

it's important to address some common misconceptions in the audiophile community. Many audiophiles believe that higher bitrates and lossless formats always result in better audio quality. However, this is not entirely true.

While higher bitrates and lossless formats can indeed provide better audio quality, the differences may not always be perceptible to the average listener. In fact, many people struggle to distinguish between high-bitrate lossy formats and lossless formats in blind listening tests.

Moreover, some audiophiles tend to overhype certain formats or codecs, claiming that they offer superior sound quality. However, these claims are often subjective and not backed by scientific evidence. It's crucial to approach audio quality discussions with a critical mindset and rely on objective measurements and controlled listening tests.

## Features

- Converts audio files to various codecs and bitrates
- Supports popular formats like MP3, AAC, and Opus
- Allows customization of codecs and bitrates through a JSON configuration file
- Provides a list of skipped formats at the end of the conversion process

## Requirements

- Python 3.x
- FFmpeg

## Usage

1. Install the required dependencies:
   ```
   pip install ffmpeg-python
   ```

2. Prepare your audio file:
   - Place your input audio file in the same directory as the script.
   - Ensure that the audio file is in a format supported by FFmpeg (e.g., WAV, MP3, FLAC).

3. Configure the codecs and bitrates:
   - Open the `codecs_and_qualities.json` file.
   - Modify the JSON structure to include the desired codecs and bitrates.
   - Save the changes.

4. Run the script:
   ```
   python audio_converter.py
   ```

5. Wait for the conversion process to complete.
   - The script will convert the input audio file to the specified codecs and bitrates.
   - It will create a directory named after the hash of the input file to store the converted files.
   - If a converted file already exists, the script will skip the conversion for that particular codec and bitrate.

6. Check the output:
   - The converted audio files will be saved in the corresponding directories based on the codec and bitrate.
   - At the end of the conversion process, the script will display a list of skipped formats, if any.
