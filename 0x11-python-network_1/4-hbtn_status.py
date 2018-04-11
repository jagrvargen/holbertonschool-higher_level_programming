#!/usr/bin/python3
"""
   A Python script that fetches https://intranet.hbtn.io/status
"""


if __name__ == "__main__":
    import requests

    url = "https://intranet.hbtn.io/status"
    r = requests.get(url)

    print("Body reponse:")
    print("\t- type: {}".format(type(r.text)))
    print("\t- content: {}".format(r.text))
