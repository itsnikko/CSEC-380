import urllib
import urllib2
import threading
from bs4 import BeautifulSoup


def courses():
    url = "https://www.rit.edu/programs/computing-security-bs"
    page = urllib2.urlopen(url).read()
    soup = BeautifulSoup(page, "html.parser")

    for tr in soup.find_all("tr"):
        td = tr.find_all("td")
        if not td or td[0].attrs or td[0].text == u"\xa0":
            continue
        print "Course: %s\n" \
              "Description: %s\n" \
              % (td[0].text, td[1].text)


def pictures():
    floc = "./images/"
    url = "http://www.rit.edu/gccis/computingsecurity/people"
    src = urllib2.urlopen(url).read()

    image = urllib.FancyURLopener()

    soup = BeautifulSoup(src, "html.parser")

    for img in soup.find_all("img"):
        sauce = img.get("src")
        print "http://www.rit.edu%s" % sauce
        image.retrieve("http://www.rit.edu%s" % sauce, floc + sauce.replace("/", "_"))


if __name__ == "__main__":
    thread = threading.Thread(target=pictures, args=())
    courses()
    pictures()
