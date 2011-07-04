import urllib2
import BeautifulSoup

base_url = "http://www.timeoutdubai.com"

def browse(url):

    if url.find("http") == -1 :
        url = "%s/%s" % ( base_url, url  )

    html = urllib2.urlopen(url).read()
    soup = BeautifulSoup.BeautifulSoup(html)


    urls = []

    for link in soup.findAll('a'):
        try:
            urls.append( link.get('href') )
        except:
            print 'nothing here'
        pass

    return urls


urls = browse( base_url )

for link in urls:
    print link
    browse( link )

