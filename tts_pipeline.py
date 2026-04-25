import os
import re
import subprocess
from pathlib import Path
from dotenv import load_dotenv
import requests

load_dotenv()

VOICE_ID = "14gmCJYwaD310oqFSc7p"
API_URL = f"https://api.elevenlabs.io/v1/text-to-speech/{VOICE_ID}"
MODEL = "eleven_multilingual_v2"
VOICE_SETTINGS = {
    "stability": 0.5,
    "similarity_boost": 0.85,
    "style": 0.3,
    "use_speaker_boost": True,
}
MAX_CHARS = 2500


def split_into_chunks(text: str) -> list[str]:
    sentences = re.split(r"(?<=[.!?])\s+", text.strip())
    chunks = []
    current = ""

    for sentence in sentences:
        if len(current) + len(sentence) + 1 <= MAX_CHARS:
            current = (current + " " + sentence).strip()
        else:
            if current:
                chunks.append(current)
            # Oración muy larga: partir por coma
            if len(sentence) > MAX_CHARS:
                parts = re.split(r"(?<=,)\s+", sentence)
                sub = ""
                for part in parts:
                    if len(sub) + len(part) + 1 <= MAX_CHARS:
                        sub = (sub + " " + part).strip()
                    else:
                        if sub:
                            chunks.append(sub)
                        sub = part
                current = sub
            else:
                current = sentence

    if current:
        chunks.append(current)

    return chunks


def tts_chunk(text: str, output_path: str, api_key: str) -> None:
    headers = {
        "xi-api-key": api_key,
        "Content-Type": "application/json",
        "Accept": "audio/mpeg",
    }
    payload = {
        "text": text,
        "model_id": MODEL,
        "voice_settings": VOICE_SETTINGS,
    }

    response = requests.post(API_URL, headers=headers, json=payload, timeout=60)
    response.raise_for_status()

    with open(output_path, "wb") as f:
        f.write(response.content)

    print(f"  Guardado: {output_path}  ({len(text)} chars)")


def concatenate_mp3s(files: list[str], output: str) -> None:
    list_file = "_ffmpeg_list.txt"
    with open(list_file, "w", encoding="utf-8") as f:
        for fp in files:
            f.write(f"file '{fp}'\n")

    subprocess.run(
        ["ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", list_file, "-c", "copy", output],
        check=True,
    )
    os.remove(list_file)


def main():
    api_key = os.getenv("ELEVENLABS_API_KEY")
    if not api_key:
        raise ValueError("ELEVENLABS_API_KEY no encontrada en .env")

    guion_path = Path("guion.txt")
    if not guion_path.exists():
        raise FileNotFoundError("guion.txt no encontrado en el directorio actual")

    text = guion_path.read_text(encoding="utf-8").strip()
    if not text:
        raise ValueError("guion.txt esta vacio")

    chunks = split_into_chunks(text)
    total = len(chunks)
    print(f"Total chunks: {total}")
    for i, c in enumerate(chunks, 1):
        print(f"  [{i}/{total}] {len(c)} chars")
    print()

    mp3_files = []
    for i, chunk in enumerate(chunks, 1):
        output = f"out_{i:03d}.mp3"
        print(f"Generando chunk {i}/{total}...")
        tts_chunk(chunk, output, api_key)
        mp3_files.append(output)

    if len(mp3_files) > 1:
        print("\nConcatenando con ffmpeg...")
        concatenate_mp3s(mp3_files, "final.mp3")
        print("final.mp3 listo.")
    else:
        os.rename(mp3_files[0], "final.mp3")
        print("final.mp3 listo.")


if __name__ == "__main__":
    main()
