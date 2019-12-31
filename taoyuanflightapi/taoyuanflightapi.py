#!/usr/bin/env python
import json
import requests
from datetime import datetime, timedelta
from typing import Mapping, Sequence, Any


def get_flights(start: datetime, end: datetime) -> Sequence[Any]:
    endpoint: str = 'https://www.taoyuan-airport.com/api/chinese/Flight/Arrival'
    datetime_format: str = "%Y/%m/%d %H:%M:%S"
    headers: Mapping[str, str] = {
        'Origin': 'https://www.taoyuan-airport.com',
        'Content-Type': 'application/json; charset=UTF-8',
        'Referer': 'https://www.taoyuan-airport.com/chinese/flight_arrival',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors'
    }
    data_raw: Mapping[str, Any] = {
        "StartDT": start.strftime(datetime_format),
        "EndDT": end.strftime(datetime_format),
        "ODate": start.strftime('%Y/%m/%d'),
        "BNo": "0",
        "ACode": {"originalObject": {}},
        "CityName": {"originalObject": {}},
        "airname": {"originalObject": {}}
    }
    data = json.dumps(data_raw)
    response = requests.post(
        endpoint,
        data=data,
        headers=headers
    )
    return response.json()


def get_current_flights() -> Sequence[Any]:
    now = datetime.now()
    start_hour = now.hour // 2 * 2
    start = now.replace(hour=start_hour, minute=0, second=0, microsecond=0)
    end = start + timedelta(hours=2) - timedelta(seconds=1)
    return get_flights(start, end)


if __name__ == "__main__":
    from pprint import pprint
    pprint(get_current_flights())
