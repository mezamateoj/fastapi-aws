import wikipedia


def wiki(name="Apple III", length=1):
    "Wikipedia fetcher function"

    try:
        return wikipedia.summary(name, length)
    except Exception as e:
        print(e)
        return "Could not get the info..."
