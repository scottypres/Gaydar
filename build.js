const fs = require('fs');
const path = require('path');

const AUDIO_EXTS = new Set([
  '.mp3', '.wav', '.ogg', '.m4a', '.aac', '.flac', '.opus', '.webm',
]);

const root = __dirname;
const files = fs
  .readdirSync(root)
  .filter((f) => {
    const full = path.join(root, f);
    return (
      fs.statSync(full).isFile() &&
      AUDIO_EXTS.has(path.extname(f).toLowerCase())
    );
  })
  .sort();

fs.writeFileSync(
  path.join(root, 'audio-list.json'),
  JSON.stringify(files),
);
console.log(`Wrote ${files.length} audio file(s) to audio-list.json`);
