import re
def extract(soup):
    names=[]
    for i in soup.find_all("ul",{"class": "single-album"}):
        d = i.find_all("div",{"class": "song-title"})
        for hf in d:
            a = hf.find_all("a")
            for it in a:
                if it.text:
                    r = it.text
                    r = r.decode("utf-8")
                    r = re.sub(r'[()]','',r)
                    r = r.replace(" ","_")
                    names.append(r)
    return names

