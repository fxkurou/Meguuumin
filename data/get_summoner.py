import requests

def get_summoner(region, summoner_name, api_key):
    """Get summoner information from the Riot Games API."""
    url = f"https://{region}.api.riotgames.com/lol/summoner/v4/summoners/by-name/{summoner_name}"
    headers = {
        "X-Riot-Token": api_key
    }
    response = requests.get(url, headers=headers)
    return response.json()