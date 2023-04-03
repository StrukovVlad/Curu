# import requests
#
# payload={'username': 'vladon','password':'always'}
#
# r=requests.post('https://bamper.by/', data=payload)
# r_dict=r.json()
# print(r_dict(['form']))
# ______________________________________________________________________________
import requests

response = requests.get("https://google.com")

response.raise_for_status()

print(response.text)
# _______________________________________________________________________________
import requests
from bs4 import BeautifulSoup

def parser(url):
    response = requests.get(url).content
    soup = BeautifulSoup(response, 'html.parser')
    title = soup.find_all("a", attrs={'class': 'js-product-title-link'})
    print(title)
    t = []
    for div in title:
        t.append(div.text)
    return t

result = parser("https://catalog.onliner.by/notebook?in_stock=1&utm_source=pc_tile&utm_medium=notebook")
print(result)
# [<a class="js-product-title-link" data-bind="attr: {href: product.html_url_with_region}">
# <span data-bind="html: product.extended_name || product.full_name"></span>
# </a>]
# ['\n\n']
# _______________________________________________________________________________
from bs4 import BeautifulSoup

soup = BeautifulSoup('<html>'
                     '<body>'
                     '  <p>'
                     '       Слава РОССИИ!!!!'
                     '  </p>'
                     '  <p>'
                     '      Слава нашему великому народу !!!!'
                     '  </p>'
                     '  <p>'
                     '      Победа будет только за нами!!!!'
                     '  </p>'
                     '</body>'
                     '</html>', 'html.parser')

elements = soup.find_all("p")

for element in elements:
    print(element.text.strip())

# Слава РОССИИ!!!!
# Слава нашему великому народу !!!!
# Победа будет только за нами!!!!
# _______________________________________________________________________________________