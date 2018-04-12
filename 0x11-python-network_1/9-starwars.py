#!/usr/bin/python3
"""
   A Python script that takes in a string and sends a search request to the
   Star Wars API.
"""


if __name__ == "__main__":
    import requests
    from sys import argv

    url = "https://swapi.co/api/people/?search=" + str(argv[1])
    results = 0
    names = []

    r = requests.get(url)
    JSON = r.json()

    for item in JSON["results"]:
        for key, value in item.items():
            if key == "name":
                results += 1
                names.append(value)

    print("Number of results: {}".format(results))
    for item in names:
        print(item)
