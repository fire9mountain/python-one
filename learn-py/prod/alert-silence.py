#!/usr/bin/python3.6
# -*- coding: utf-8 -*-

import json
import requests


def create_silence(host):
    """
    :return dict: A dictionary containing the silence ID.
    """
    # Ensure endsAt is after startsAt
    payload = {
        "matchers": [
            {
                "name": "alertname",
                "value": "CPU使用情况",
                "isRegex": False
            }
        ],
        "startsAt": "2024-11-18T02:00:00.334Z",
        "endsAt": "2024-11-30T10:00:00.334Z",  # Corrected end time to be after start time
        "createdBy": "admin",
        "comment": "ops",
        "id": None
    }

    # Use the host parameter to construct the URI
    uri = f"http://{host}:9093/api/v2/silences"

    response = requests.post(uri, json=payload)

    if response.status_code == 200:
        return response.json()  # Return the JSON response which includes the silence ID
    else:
        print(f"Failed to create silence. Status code: {response.status_code}")
        return {}


# Example usage
result = create_silence("34.146.186.219")
print(result)