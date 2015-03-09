import requests
from titleextract import title
from bs4 import BeautifulSoup
from fabric.api import local
from nameextracter import extract
def download(url="http://www.songspk.name/indian-mp3-songs/badlapur-2015-mp3-songs.html"):
    request = requests.get(url)
    soup = BeautifulSoup(request.content)
    nam = extract(soup)
    titles = title(soup)
    count = 1
    local("mkdir /home/zeroonehacker/"+titles)
    links = soup.find_all("div",{"class":"download"})
    for flevel in links:
        s =flevel.find_all("a")
        for slevel in s:
            url = slevel.get("href")
            print "Downloading file.........."
            local("wget "+"%s" % url)
            local("mv ./song*"+" /home/zeroonehacker/"+titles+"/"+nam[count-1]+".mp3")
            count +=1
