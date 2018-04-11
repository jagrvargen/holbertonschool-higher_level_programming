#!/usr/bin/python3
"""
   A Python script that takes in a URL and an email, sends a POST request to
   the passed URL with the email as a parameter, and displays the body of
   the response (decoded in utf-8).
"""


if __name__ == "__main__":
    import urllib.request
    import urllib.parse
    from sys import argv

    url = argv[1]
    values = {"email": "{}".format(argv[2])}

    data = urllib.parse.urlencode(values)
    data = data.encode("utf-8")
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        page = response.read()
    print("{}".format(page.decode("utf-8")))
