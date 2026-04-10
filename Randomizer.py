import csv
import random
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
CSV_PATH = BASE_DIR / "Sluggers Characters.csv"

with CSV_PATH.open(newline="", encoding="utf-8-sig") as file:
    rows = [row[0].strip() for row in csv.reader(file) if row and row[0].strip()]

if rows and rows[0].lower() == "name":
    rows = rows[1:]

# Header is removed above. If stadiums begin at CSV row 73, that is index 71 here.
STADIUM_START_INDEX = 71

# 12 captains at the top of the list.
captains_pool = rows[:12]
# All draftable characters (captains + players), excluding stadium rows.
character_pool = rows[:STADIUM_START_INDEX]

# If stadiums are appended to the CSV, use them; otherwise fall back gracefully.
stadium_pool = rows[STADIUM_START_INDEX:] if len(rows) > STADIUM_START_INDEX else []


def ranTeam():
    if len(captains_pool) < 2 or len(character_pool) < 18:
        raise ValueError("CSV does not contain enough captains/players to build two teams.")

    captain1, captain2 = random.sample(captains_pool, 2)
    # Keep the two chosen captains fixed, but allow all other captains in the draft pool.
    draft_pool = [name for name in character_pool if name not in (captain1, captain2)]
    roster = random.sample(draft_pool, 16)

    team1 = [captain1] + roster[:8]
    team2 = [captain2] + roster[8:]

    print("Team 1:")
    for player in team1:
        print(player)

    print("\nTeam 2:")
    for player in team2:
        print(player)


def ranStadium():
    print("\nStadium:")
    if stadium_pool:
        print(random.choice(stadium_pool))
    else:
        print("No stadium list found in CSV (teams were still randomized).")


def main():
    ranTeam()
    ranStadium()


if __name__ == "__main__":
    main()
