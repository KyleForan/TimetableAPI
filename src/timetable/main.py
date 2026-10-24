import requests

from .utils.constants import CATEGORY_IDS, WEEK
from .utils.request_handlers import getURL, generateJSON, getTimetableURL
from .utils.parsers import parseSearchResults, parseTimetable


def main() -> None:

    # TODO: User input
    query = "AG-003"
    category = "rooms"

    # TODO: Handle Null
    url = getURL(category, query) 

    # TODO: Handle API error
    response = requests.post(url)
    results = parseSearchResults(response.json())

    # TODO: better handling
    x = list(results.items())[0][1]
    payload = {CATEGORY_IDS.get(category, ""): [x]}

    url = getTimetableURL()
    payload = generateJSON(["Monday"], payload)

    # TODO: Handle API error
    response = requests.post(url, json=payload)
    data = parseTimetable(response.json())

    # TODO: Actual Output
    try:
        import json
        print(json.dumps(data, indent=2))
    except Exception as e:
        print(f'{ e = }')
        print(response.content)
