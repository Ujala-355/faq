# task4
from bs4 import BeautifulSoup
import requests,json
def scrape_movie_details(url):
    x=requests.get(url)
    soup=BeautifulSoup(x.text,"html.parser")
    main=soup.find("ul",class_="content-meta info")
    li=main.find_all("li")
    d={}
    movie_name=soup.find("h1",class_="scoreboard__title").get_text()
    d["Name"]=movie_name
    for i in li:
        f=i.text.split()
        # print(f)
        if "Rating:" in f:
            d["Rating"]=f[1]
        # print(d)
        if  "Genre:" in f:
            e=f[1:]
            str=""
            for k in e:
                str+=k
            str=str.split(",")
            d["Genre"]=str
        if "Language:" in f:
            d["Language"]=f[2]
        if "Director:" in f:
            a=f[1:]
            b=""
            for h in a:
                b+=h
            b=b.split(",")
            d["Director"]=b
        if "Producer:" in f:
            d["Producer"]=f[1:]
        if "Writer:" in f:
            d["Writer"]=f[1:]
        if "Runtime:" in f:
            time=f[1:]
            i=0
            while i<len(time):
                hour=time[0][0]
                mint=time[1]
                min=mint[:-1]
                # print(mint)
                i+=1
            tom=int(hour)*60+int(min)
            # print(tom)
            d["Runtime"]=tom
        if "Distributor:" in f:
            d["Distributor"]=f[1:]
    with open("task4.json","w") as f:
        json.dump(d,f,indent=4)
    return d
scrape_movie_details("https://www.rottentomatoes.com/m/spider_man_into_the_spider_verse")

