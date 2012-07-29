import BeautifulSoup
from BeautifulSoup import BeautifulSoup
import sys
import urllib2

if __name__ == '__main__':
    url = sys.argv[1]
    content = urllib2.urlopen(url).read()

    soup = BeautifulSoup(content)
    items = soup.findAll(attrs={'class':'bg2 cGreen'}) + soup.findAll(attrs={'class':'cGreen'})
    for i in items:
        print i.get('id')
