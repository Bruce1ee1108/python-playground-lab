from pathlib import Path
import plistlib


PROJECT_DIR = Path(__file__).parent
INPUT_PATH = PROJECT_DIR / "samples" / "playlist_a.xml"

with INPUT_PATH.open("rb") as input_file:
    playlist_data = plistlib.load(input_file)

tracks = playlist_data["Tracks"]
print(f"Loaded {len(tracks)} tracks.")