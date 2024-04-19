from setuptools import setup

setup(
    name="audio-converter",
    version="0.1.0",
    py_modules=["audio_converter", "audio_comparison"],
    entry_points={
        "console_scripts": [
            "audio-converter = audio_converter:main",
            "audio-comparison = audio_comparison:main",
        ],
    },
)

