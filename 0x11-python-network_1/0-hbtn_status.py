#!/usr/bin/python3
"Fetches https://alx-intranet.hbtn.io/status using urllib package."


import urllib.request


if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'

    with urllib.request.urlopen(url) as response:
        body = response.read()
        body_decoded = body.decode("utf-8")
        print("Body response:")
        print("    - type: {}".format(type(body)))
        print("    - content: {}".format(body))
        print("    - utf8 content: {}".format(body_decoded))
