#!/usr/bin/python3
"""
   A Python script that lists 10 commits of a repository and its owner passed
   as the first and second argument respectively.
"""


if __name__ == "__main__":
    import requests
    from sys import argv

    repo = str(argv[1]) + "/"
    owner = str(argv[2]) + "/"
    url = "https://api.github.com/repos/" + owner + repo + "commits"
    payload = {"per_page": 10}

    r = requests.get(url, params=payload)
    JSON = r.json()

    for item in JSON:
        print("{}: {}".format(item["sha"], item["commit"]["author"]["name"]))
