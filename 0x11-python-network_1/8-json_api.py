#!/usr/bin/python3
"""
   A Python script that takes in a letter and sends a POST request to
   http://0.0.0.0:5000/search_user with the letter as a parameter.
"""


if __name__ == "__main__":
    import requests
    from sys import argv

    url = "http://0.0.0.0:5000/search_user"

    if len(argv) == 2:
        payload = {"q": str(argv[1])}
    else:
        payload = {"q": ""}

    r = requests.post(url, data=payload)

    if r.json():
        JSON = r.json()
        print("[{}] {}".format(JSON["id"], JSON["name"]))
    else:
        print("No result")
