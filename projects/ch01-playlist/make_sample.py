from pathlib import Path
import plistlib

PROJET_DIR = Path(__file__).parent
OUTPUT_PATH = PROJET_DIR / "samples" / "playlist_a.xml"

playlist_data = {
    "Tracks": {
        "101": {
            "Name": "Harbour Lights",
            "Artist": "Studio North",
            "Total Time": 180000,
        },
        "102": {
            "Name": "Habour Lights",
            "Artist": "Studio North",
            "Total Time": 180000,
        },
        "103": {
            "Name": "Harbour Lights",
            "Artist": "Coastal Trio",
            "Total Time": 180000,
        },
    },
}


OUTPUT_PATH.parent.mkdir(exist_ok=True)

with OUTPUT_PATH.open("wb") as output_file:
    plistlib.dump(playlist_data, output_file)

print(f"Created sample playlist: {OUTPUT_PATH}")