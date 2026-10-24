def parseSearchResults(search_results: dict) -> dict:

    parsed = {}

    for result in search_results.get("Results", {}):
        name = result.get("Name", "")
        result_id = result.get("Identity", "")

        parsed.update({name: result_id})

    return parsed


# TODO: Handle multiple selections
def parseTimetable(ids: dict) -> dict:

    data = ids.get("CategoryEvents", {})[0]

    name = data.get("Name", "N/A")
    results = data.get("Results", [{}])

    details = []
    for booking in results:
        booking_details = {}

        booking_details.update({"start": booking.get("StartDateTime", "")})
        booking_details.update({"end": booking.get("EndDateTime", "")})
        booking_details.update({"location": booking.get("Location", "")})
        booking_details.update({"name": booking.get("Name", "")})

        properties = booking.get("ExtraProperties", [{}])

        booking_details.update(
            {
                "booking_properties": {
                    info.get("DisplayName", "DisplayName"): info.get("Value", "Value")
                    for info in properties
                }
            }
        )

        details.append(booking_details)

    return {name: details}
