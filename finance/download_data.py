import sys
import urllib2

URL = 'http://table.finance.yahoo.com/table.csv?s=%s&a=%d&b=%d&c=%d&d=%d&e=%d&f=%d&g=d&ignore=.csv'

if __name__ == '__main__':
    param = (sys.argv[1], 7, 26, 2011, 7,26, 2012)
    url = URL % param
    content = urllib2.urlopen(url).read()
    print content
    data = content.split('\n')[1:-1]
    close_price = [float(i.split(',')[-1]) for i in data]
    delta = [close_price[i] - close_price[i+1] for i in range(len(close_price) - 1)]
    for d in delta:
        print d

