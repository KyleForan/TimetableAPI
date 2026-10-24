from .constants import BASE_URL, CATEGORY_IDS, COLLEGE_ID

# Search Modules
# https://scientia-eu-v4-api-d4-01.azurewebsites.net/api/Public/CategoryTypes/525fe79b-73c3-4b5c-8186-83c652b3adcc/Categories/FilterWithCache/50a55ae1-1c87-4dea-bb73-c9e67941e1fd?pageNumber=1&query=

# Search Room
# https://scientia-eu-v4-api-d4-01.azurewebsites.net/api/Public/CategoryTypes/1e042cb1-547d-41d4-ae93-a1f2c3d34538/Categories/FilterWithCache/50a55ae1-1c87-4dea-bb73-c9e67941e1fd?pageNumber=1&query=
# https://scientia-eu-v4-api-d4-01.azurewebsites.net/api/Public/CategoryTypes/1e042cb1-547d-41d4-ae93-a1f2c3d34538/Categories/FilterWithCache/50a55ae1-1c87-4dea-bb73-c9e67941e1fd?pageNumber=1&query=

# Search Course
# https://scientia-eu-v4-api-d4-01.azurewebsites.net/api/Public/CategoryTypes/241e4d36-93f2-4938-9e15-d4536fe3b2eb/Categories/FilterWithCache/50a55ae1-1c87-4dea-bb73-c9e67941e1fd?pageNumber=1&query=

# Get Timetable
# https://scientia-eu-v4-api-d4-01.azurewebsites.net/api/Public/CategoryTypes/Categories/Events/Filter/50a55ae1-1c87-4dea-bb73-c9e67941e1fd?startRange=2026-10-17T23:00:00.000Z&endRange=2026-10-27T23:59:59.999Z

def getURL(category: str, query: str) -> str:
    if category not in CATEGORY_IDS:
        return ""

    url = BASE_URL
    url += "/CategoryTypes/"
    url += CATEGORY_IDS.get(category, "")
    url += "/Categories/FilterWithCache/"
    url += COLLEGE_ID
    url += "?pageNumber=1&query="
    url += query

    print(f"{url = }")

    return url


def getTimetableURL() -> str:
    url = BASE_URL
    url += "/CategoryTypes/Categories/Events/Filter/"
    url += COLLEGE_ID

    # TODO: make dynamic
    # NOTE: Monday - Friday, day filtering with week arg
    url += "?startRange=2026-10-17T23:00:00.000Z&endRange=2026-10-27T23:59:59.999Z"

    return url


def generateJSON(week: list[str], ids: dict[str, list[str]]) -> dict:
    return {
        "ViewOptions": {
            "Days": [
                {
                    "Name": day,
                    "DayOfWeek": n,
                    "Default": True,
                }
                for n, day in enumerate(week, 1)
            ],
            "Weeks": [],
            "TimePeriods": [
                {
                    "Description": "All Day",
                    "StartTime": "00:00",
                    "EndTime": "23:59",
                    "IsDefault": True,
                }
            ],
        },
        "CategoryTypesWithIdentities": [
            {
                "CategoryTypeIdentity": typeid,  # Type ID: course, module, Room
                "CategoryIdentities": [
                    identity for identity in identities  # Individual ID: TU863, AG-111
                ],
            }
            for typeid, identities in ids.items()
        ],
        "FetchBookings": False,
        "FetchPersonalEvents": False,
        "PersonalIdentities": [],
    }


