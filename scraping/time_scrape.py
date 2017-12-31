# Grabbing text from a famous newspaper
import urllib
from BeautifulSoup import BeautifulSoup as bs

# URLs
# Depending on how many URLs are input this could take some time.
urls = ["https://www.nytimes.com/2017/12/29/style/modern-love-new-years-kiss-priest.html?rref=collection%2Fcolumn%2Fmodern-love&action=click&contentCollection=fashion&region=rank&module=package&version=highlights&contentPlacement=1&pgtype=collection&_r=0",
        "https://www.nytimes.com/2017/09/08/style/modern-love-finding-god-in-a-hot-slice-of-pizza.html?action=click&contentCollection=Style&module=RelatedCoverage&region=EndOfArticle&pgtype=article"]

text = ''
for url in urls:
    soup = bs(urllib.urlopen(url))
    for link in soup.findAll('p', {'class': 'story-body-text story-content'}):
            text += link.string

# Send the txt to a file
text_file = open('output.txt', 'w')
text_file.write(text.encode('utf-8'))
text_file.close()
