import bs4, requests

def getAmazonPrice(productUrl):
    res = requests.get(productUrl)
    # res = requests.get(productUrl, headers={
    #    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.110 Safari/537.36"
    #    })
    res.raise_for_status()



    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    #elems = soup.select('#buyNewSection > h5 > div > div.a-column.a-span8.a-text-right.a-span-last > div > span.a-size-medium.a-color-price.offer-price.a-text-normal')
    elems = soup.select('#edit-attributes-1 > div:nth-child(1) > label')
    print(elems)
    # return elems
    return elems[0].text.strip()


#price = getAmazonPrice('https://www.amazon.com/Automate-Boring-Stuff-Python-2nd/dp/1593279922/')
price = getAmazonPrice('https://nostarch.com/automatestuff')
print('The price is ' + price)
