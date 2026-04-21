# Gaydar

Quick web app that takes a selfie, shows a "Calculate Gay %" button, displays **100% gay**, and plays a random audio file from the root directory on each press.

## Usage

1. Drop any audio files (`.mp3`, `.wav`, `.ogg`, `.m4a`, `.aac`, `.flac`, `.opus`, `.webm`) in the root directory.
2. Run the server:
   ```
   python3 server.py
   ```
3. Open http://localhost:8000 in a browser. Camera access requires HTTPS or `localhost`.

## Behavior

- Header + photo + buttons + result fit on a mobile screen without scrolling.
- Camera prompt appears once on load; take a selfie and it displays below the header.
- Press **Calculate Gay %** to display `100% gay` and play a random audio file.
- Volume warning shows once per page load.
- Button presses are throttled to 1 second apart.
