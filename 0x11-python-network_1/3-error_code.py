#!/usr/bin/python3
"""
   A Python script that takes in a URL, sends a request to the URL and
   displays the body of the response (decoded in utf-8).
"""


if __name__ == "__main__":
    import urllib.request
    import urllib.error
    from sys import argv

    url = argv[1]
    req = urllib.request.Request(url)

   try:
       with  urllib.request.urlopen(req) as response:
           page = response.read()
           print("{}".format(page.decode("utf-8")))
    except urllib.error.HTTPError as err:
        print("Error code: {}".format(err.code))
