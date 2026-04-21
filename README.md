# Gaydar

Quick web app that takes a selfie, shows a "Calculate Gay %" button, displays **100% gay**, and plays a random audio file from the root directory on each press.

## Deploy to Vercel

1. Drop any audio files (`.mp3`, `.wav`, `.ogg`, `.m4a`, `.aac`, `.flac`, `.opus`, `.webm`) in the project root.
2. Commit and push — Vercel runs `node build.js` on deploy, which scans the root and writes `audio-list.json` with the list of audio filenames.
3. No framework config needed; `vercel.json` serves the repo root as static content.

## Local dev

Either:

```
npm run build && python3 server.py
```

or just use the included Python helper (which generates the audio list on the fly):

```
python3 server.py
```

Then open http://localhost:8000. Camera access requires HTTPS or `localhost`.

## Behavior

- Header + photo + buttons + result fit on a mobile screen without scrolling.
- Camera prompt appears once per load; the selfie displays below the header.
- Press **Calculate Gay %** to show `100% gay` and play a random audio file.
- Volume warning shows once per page load.
- Button presses are throttled to 1 second apart.
