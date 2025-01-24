import requests
from .websocket_handler import connect_to_websocket


def search(query, language="fr_FR", streamed=False, debug=False):
    """
    Search Qwant and get results either as a single text or streamed.

    Args:
        query (str): The search query to send to Qwant.
        language (str): The language for the search results (default: "en_US").
        streamed (bool): If True, results are streamed. If False, they are returned as one big text.

    Returns:
        str: The full response as text if streamed is False.
    """
    session = requests.Session()

    homepage_url = "https://www.qwant.com/"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
        "Accept-Language": "fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7",
    }
    session.get(homepage_url, headers=headers)

    search_url = "https://api.qwant.com/v3/search/web"
    params = {
        "q": query,
        "count": 10,
        "locale": language,
        "offset": 0,
        "device": "desktop",
        "tgp": 1,
        "safesearch": 0,
        "displayed": "true",
        "llm": "true"
    }
    search_headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
        "Accept": "application/json, text/plain, */*",
        "Referer": "https://www.qwant.com/",
    }
    response = session.get(search_url, params=params, headers=search_headers)

    if response.status_code == 200:
        try:
            json_response = response.json()
            token_detailed = json_response['data']['result']['items']['mainline'][0]['data']['tokenDetailed']
            if streamed:
                connect_to_websocket(token_detailed, session, debug=debug)
            else:
                return fetch_full_response(token_detailed, session, debug=debug)
        except Exception as e:
            raise Exception("An error occurred while processing the Qwant search.") from e
    else:
        raise Exception(f"Qwant search error: {response.status_code}")

def fetch_full_response(token_detailed, session, debug=False):
    """
    Fetch the entire response as a single string using WebSocket.

    Args:
        token_detailed (str): The token for WebSocket communication.
        session (requests.Session): The session with cookies.

    Returns:
        str: The full response as text.
    """
    full_response = []

    def collect_response(delta):
        full_response.append(delta)

    connect_to_websocket(token_detailed, session, callback=collect_response)
    return "".join(full_response)
