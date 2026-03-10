import requests
from datetime import datetime

# ======== KONFIGURATION ========
TOKEN = input("Klistra in din Fine-grained GitHub token: ").strip()
OWNER = "PatrikYousef"
REPO = "PortfolioProgrammingProjects"
# ==============================

url = f"https://api.github.com/repos/{OWNER}/{REPO}/traffic/clones"
headers = {
    "Accept": "application/vnd.github.v3+json",
    "Authorization": f"token {TOKEN}"
}

response = requests.get(url, headers=headers)

if response.status_code == 401:
    print("Fel: Bad credentials. Kontrollera token.")
    exit()
elif response.status_code == 403:
    print("Fel: Resource not accessible. Kontrollera att token har Read access till Metadata och Traffic.")
    exit()
elif response.status_code != 200:
    print("Fel vid hämtning av data:", response.status_code, response.text)
    exit()

data = response.json()

print(f"\nTotala kloner: {data['count']}")
print(f"Unika kloner: {data['uniques']}\n")
print("Dag-för-dag kloner:")
for c in data['clones']:
    datum = datetime.fromisoformat(c['timestamp'][:-1]).strftime('%Y-%m-%d')
    print(f"{datum} -> Totalt: {c['count']}, Unika: {c['uniques']}")