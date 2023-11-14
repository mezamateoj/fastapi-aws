import wikipedia


def wiki(name="Apple III", length=1):
    """Wikipedia fetcher function"""

    try:
        return wikipedia.summary(name, length)
    except Exception as e:
        print(e)
        return "ERROR: Could not get the info..."

def search_wiki(name):
    """Search Wikipedia articles by title, name"""
    
    try:
        return wikipedia.search(name)
    except Exception as e:
        print(e)
        return "ERROR: Could not get the info..."

