{ pkgs ? import <nixpkgs> {} }:

pkgs.python3Packages.buildPythonApplication {
  pname = "audio-converter";
  version = "0.1.0";

  src = ./.;

  propagatedBuildInputs = with pkgs.python3Packages; [
    ffmpeg-python
    simpleaudio
  ];

  meta = with pkgs.lib; {
    description = "A Python script for converting audio files to various codecs and qualities";
    license = licenses.mit;
    maintainers = [ "your-name" ];
  };
}

