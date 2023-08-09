import urllib3
import requests
from bs4 import BeautifulSoup
from win10toast import ToastNotifier
n = ToastNotifier()
def getdata(url):
    r = requests.get(url)
    return r.text
htmldata = getdata("https://weather.com/en-IN/weather/today/l/d8957d01281fef701a5fa057bfd5da7f9674a11f991de86e8a482fd0c92480c8")
soup = BeautifulSoup(htmldata,'html.parser')
print(soup.prettify())