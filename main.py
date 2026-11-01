import requests

BASE_URL = "https://calendar.newsbihani.com/api/calendar"

for year in [2082, 2083, 2084]:
    response = requests.get(
        BASE_URL,
        params={"year": year, "month": 1},
        timeout=15
    )

    print(f"\nBS Year: {year}")
    print("Status:", response.status_code)

    if response.ok:
        data = response.json()

        for day in data.get("days", []):
            for event in day.get("events", []):
                print(
                    day["key"],
                    event.get("titleEn"),
                    event.get("type")
                )
    else:
        print(response.text[:300])
