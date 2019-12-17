import bs4, requests

def getHeading(url):
    res = requests.get(url)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    elems = soup.select('body > div.navPusher > div > div.container.mainContainer > div > div.post > article > div > span > h1:nth-child(2)')
    return elems[0].text.strip()

heading = getHeading('https://mobx.js.org/README.html')
print('The heading is ' + heading)
