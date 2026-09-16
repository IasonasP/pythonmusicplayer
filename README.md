# Music Player

A simple Python music player that asks for the artist and song title, then plays the first 30 seconds of the corresponding MP3 file.

## Requirements

- Python 3.14 or newer
- pygame-ce
- An MP3 file

## Installation

Install `pygame-ce`:

```powershell
py -m pip install pygame-ce
```

## File Structure

```text
music player/
├── main.py
├── README.md
└── music/
    └── Artist-Song.mp3
```

## File Naming

The MP3 file must follow this format:

```text
Artist-Song.mp3
```

Example:

```text
test-test.mp3
```

## Usage

Open `main.py` with IDLE and press `F5`.

The program will ask for:

```text
Artist:
Song:
```

Example:

```text
Artist: test
Song: test
```

The program will search for:

```text
music/test-test.mp3
```

If the file is found, the first 30 seconds will be played.

## Features

- Asks for the artist's name.
- Asks for the song title.
- Checks whether the corresponding MP3 file exists.
- Plays the first 30 seconds of the file.
- Displays a message if the file cannot be found.

## Limitations

- Only local MP3 files are supported.
- The program does not search for songs on the Internet.
- MP4 video playback is not supported.
- File names must match the entered artist and song exactly.

## License

This project is licensed under the ΜΙΤ License.
