import requests
import pandas as pd

API_TOKEN = "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6ImQzMmY3OGZlLWIzYWEtNDhhYy04NGM5LWQzZjZjMmY1OTE4MyIsImlhdCI6MTc0NTU4NzMzNCwic3ViIjoiZGV2ZWxvcGVyL2M5YzEwYjAyLTJlMDktZDUwMC0xOTZkLWFmZTY5YTEyYTcwNCIsInNjb3BlcyI6WyJyb3lhbGUiXSwibGltaXRzIjpbeyJ0aWVyIjoiZGV2ZWxvcGVyL3NpbHZlciIsInR5cGUiOiJ0aHJvdHRsaW5nIn0seyJjaWRycyI6WyIxNTkuMjAuNjkuMyJdLCJ0eXBlIjoiY2xpZW50In1dfQ.skJ362rYjVY7LewmijqnKRRfMCs4eh_LIobYKmlfdmhswJm_tEK7IELA1X8n4JNILXMdRtKSlMIUsrxI7QwQzg"
HEADERS = {"Authorization": API_TOKEN}

res = requests.get("https://api.clashroyale.com/v1/cards", headers=HEADERS).json()

cards = []
for card in res["items"]:
    cards.append({
        "name": card["name"],
        "elixirCost": card.get("elixirCost", 0)  # Set as 0 if it is missing.
    })

df = pd.DataFrame(cards)
df.to_excel("card_elixir_costs.xlsx", index=False)
print("Saved: card_elixir_costs.xlsx")
