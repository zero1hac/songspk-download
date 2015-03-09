__author__ = 'zeroonehacker'
import re
def title(soup):
    title = ""
    i = soup.find_all("div",{"class":"single-album-info"})
    for gh in i:
        h1=gh.find_all("h1")
        for final in h1:
            title+=final.text
    title = re.sub(r'\(.*?\)','', title)
    title = title.replace(" ","_")

    return title

