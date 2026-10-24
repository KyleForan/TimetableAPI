from fastapi import FastAPI, Header
import requests

from timetable.utils.constants import CATEGORY_IDS, WEEK
from timetable.utils.parsers import parseSearchResults, parseTimetable
from timetable.utils.request_handlers import generateJSON, getTimetableURL, getURL

app = FastAPI()


@app.get("/course/{course_name}")
def get_course(course_name: str):

    url = getURL("course", course_name)
    response = requests.post(url)

    if response.status_code != 200:
        return {"Error": response.json()}

    parsed_response = parseSearchResults(response.json())

    return {"response": parsed_response}


@app.get("/rooms/{room_name}")
def get_room(room_name: str):

    url = getURL("rooms", room_name)
    response = requests.post(url)

    if response.status_code != 200:
        return {"Error": response.json()}

    parsed_response = parseSearchResults(response.json())

    return {"response": parsed_response}


@app.get("/timetable/{category}/{id}")
def get_timetable(category: str, id: str, group: str = "", days: str = "MtWTF"):

    payload = {CATEGORY_IDS.get(category, "FAILED"): [id]}
    week = [WEEK[day] for day in days if day in WEEK]

    url = getTimetableURL()
    payload = generateJSON(week, payload)

    response = requests.post(url, json=payload)
    data = parseTimetable(response.json())

    filtered_response = []

    if group:
        for key in data:
            for booking in data[key]:
                properties = booking.get("booking_properties", {})
                groups = properties.get("Class Group", "")

                if groups and not any(
                    [
                        group in class_group or "All" in class_group
                        for class_group in groups.split(" + ")
                    ]
                ):
                    continue
                filtered_response.append(booking)
    else:
        filtered_response = data

    return {"response": filtered_response}
