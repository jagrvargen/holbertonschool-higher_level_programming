#!/usr/bin/python3
"""
   A Python script that takes your Github credentials (username and password)
   and uses the Github API to display your id.
"""


if __name__ == "__main__":
    import requests
    from sys import argv

    url = "https://api.github.com/user"
    user = str(argv[1])
    pswd = str(argv[2])

    r = requests.Session()
    r = requests.get(url, auth=(user, pswd))

    try:
        JSON = r.json()
        print(JSON["id"])
    except:
        print("None")
