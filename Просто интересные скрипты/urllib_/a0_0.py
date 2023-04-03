import urllib
from urllib import request, error
from functools import lru_cache

@lru_cache(maxsize=24)
def get_webpage(module):

    webpage = "https://docs.python.org/3/library/{}.html".format(module)
    try:
        with urllib.request.urlopen(webpage) as req:
            return req.read()
    except urllib.error.HTTPError:
        return None

if __name__=="__main__":
    modules = ['functools','collections','os','sys']
    for module in modules:
        page = get_webpage(module)
        if page:
            print("{} module page found".format(module))


# functools module page found
# collections module page found
# os module page found
# sys module page found

