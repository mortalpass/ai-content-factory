import json
import os
from datetime import datetime

def save_results(results):
    os.makedirs("outputs", exist_ok=True)
    filename = f"outputs/content_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"

    with open(filename, "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)

    return filename
