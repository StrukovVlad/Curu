from collections import deque

sites = ("google.com","yahoo.com","bing.com")
pages = deque(maxlen=3)

for site in sites:
    pages.appendleft(site)

print(pages)
# deque(['bing.com', 'yahoo.com', 'google.com'], maxlen=3)

pages.appendleft("facebook.com")

print(pages)
# deque(['facebook.com', 'bing.com', 'yahoo.com'], maxlen=3)

pages.remove("yahoo.com")

print(pages)
# deque(['facebook.com', 'bing.com'], maxlen=3)

pages.extend([1,2,3])

pages.reverse()

print(pages)
# deque([3, 2, 1], maxlen=3)

pages.clear()

pages.extendleft(["mail.ru","rambler.ru","yandex.ru"])

print(pages)
# deque(['yandex.ru', 'rambler.ru', 'mail.ru'], maxlen=3)

pages.pop()

print(pages)
# deque(['yandex.ru', 'rambler.ru'], maxlen=3)

pages.insert(2,"twitter.com")

print(pages)
# deque(['yandex.ru', 'rambler.ru', 'twitter.com'], maxlen=3)