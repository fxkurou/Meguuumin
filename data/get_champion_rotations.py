import requests

def get_champion_rotations(region, api_key):
    """Get the current champion rotations from the Riot Games API."""
    url = f"https://{region}.api.riotgames.com/lol/platform/v3/champion-rotations"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:135.0) Gecko/20100101 Firefox/135.0",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Charset": "application/x-www-form-urlencoded; charset=UTF-8",
        "X-Riot-Token": api_key
    }
    response = requests.get(url, headers=headers)
    return response.json()


def get_champion_data():
    """Fetch champion data from Data Dragon."""
    version = "13.1.1"  # Replace with the current version
    url = f"http://ddragon.leagueoflegends.com/cdn/{version}/data/en_US/champion.json"

    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        champions = data["data"]
        # Create a mapping of key -> champion info
        id_to_name = {}
        for champ_name, champ_info in champions.items():
            id_to_name[int(champ_info["key"])] = champ_name
        return id_to_name
    else:
        print(f"Failed to fetch champion data: {response.status_code}")
        return {}


def get_champion_name(champion_id, id_to_name):
    """Get the champion name by ID."""
    return id_to_name.get(champion_id, "Unknown Champion")
