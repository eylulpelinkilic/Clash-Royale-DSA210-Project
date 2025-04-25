
import requests
import pandas as pd

API_TOKEN = "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6ImQzMmY3OGZlLWIzYWEtNDhhYy04NGM5LWQzZjZjMmY1OTE4MyIsImlhdCI6MTc0NTU4NzMzNCwic3ViIjoiZGV2ZWxvcGVyL2M5YzEwYjAyLTJlMDktZDUwMC0xOTZkLWFmZTY5YTEyYTcwNCIsInNjb3BlcyI6WyJyb3lhbGUiXSwibGltaXRzIjpbeyJ0aWVyIjoiZGV2ZWxvcGVyL3NpbHZlciIsInR5cGUiOiJ0aHJvdHRsaW5nIn0seyJjaWRycyI6WyIxNTkuMjAuNjkuMyJdLCJ0eXBlIjoiY2xpZW50In1dfQ.skJ362rYjVY7LewmijqnKRRfMCs4eh_LIobYKmlfdmhswJm_tEK7IELA1X8n4JNILXMdRtKSlMIUsrxI7QwQzg"
HEADERS = {
    "Authorization": API_TOKEN,
    "Accept": "application/json"
}

PLAYER_TAGS = ["YQUV2UUG", "RURUGGV9V", "UROQVJL9", "Q00JJQR", "UJPGR28PJ"]

card_data_url = "https://api.clashroyale.com/v1/cards"
card_res = requests.get(card_data_url, headers=HEADERS).json()
card_costs = {card["name"]: card["elixirCost"] for card in card_res["items"]}

def avg_elixir(cards):
    return sum(card_costs.get(card["name"], 0) for card in cards) / len(cards)

records = []
for tag in PLAYER_TAGS:
    url = f"https://api.clashroyale.com/v1/players/%23{tag}/battlelog"
    res = requests.get(url, headers=HEADERS)
    if res.status_code != 200:
        print(f"Error fetching for {tag}: {res.status_code}")
        continue
    battles = res.json()
    for battle in battles:
        player_cards = battle["team"][0]["cards"]
        opponent_cards = battle["opponent"][0]["cards"]
        records.append({
            "playerTag": tag,
            "battleTime": battle["battleTime"],
            "playerDeck": ",".join([c["name"] for c in player_cards]),
            "playerAvgElixir": avg_elixir(player_cards),
            "opponentDeck": ",".join([c["name"] for c in opponent_cards]),
            "opponentAvgElixir": avg_elixir(opponent_cards),
            "win": battle["team"][0]["crowns"] > battle["opponent"][0]["crowns"]
        })

df = pd.DataFrame(records)
df.to_excel("last_5_players_battles.xlsx", index=False)
print("Dataset created: last_5_players_battles.xlsx")
