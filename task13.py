from task4 import scrape_movie_details
from task12 import scrape_movie_cast
import json
l=[]
url=("https://www.rottentomatoes.com/m/spider_man_into_the_spider_verse")

def scrape_cast():
    details=scrape_movie_details(url)
    cast=scrape_movie_cast(url)
    details["cast"]=cast
    l.append(details)
    with open("task13.json","w") as f1:
        json.dump(l,f1,indent=4)
scrape_cast()


































# from bs4 import BeautifulSoup
# import requests,json
# def scrape_movie_details(url):
#     req=requests.get(url)
#     soup=BeautifulSoup(req.text,"html.parser")
#     main=soup.find("ul",class_="content-meta info")
#     li=main.find_all("li")
#     d={}
#     movie_name=soup.find("h1",class_="scoreboard__title").get_text()
#     d["Name"]=movie_name
#     main_d=soup.find("div",class_="castSection")
#     d1=main_d.find_all("div",class_="cast-item media inlineBlock")
#     d2=main_d.find_all("div",class_="cast-item media inlineBlock moreCasts hide")
#     l=[]
#     for i in li:
#         f=i.text.split()
#         # print(f)
#         if "Rating:" in f:
#             d["Rating"]=f[1]
#         # print(d)
#         if  "Genre:" in f:
#             e=f[1:]
#             str=""
#             for k in e:
#                 str+=k
#             str=str.split(",")
#             d["Genre"]=str
#         if "Language:" in f:
#             d["Language"]=f[2]
#         if "Director:" in f:
#             a=f[1:]
#             b=""
#             for h in a:
#                 b+=h
#             b=b.split(",")
#             d["Director"]=b
#         if "Producer:" in f:
#             d["Producer"]=f[1:]
#         if "Writer:" in f:
#             d["Writer"]=f[1:]
#         if "Runtime:" in f:
#             time=f[1:]
#             i=0
#             while i<len(time):
#                 hour=time[0][0]
#                 mint=time[1]
#                 min=mint[:-1]
#                 # print(mint)
#                 i+=1
#             tom=int(hour)*60+int(min)
#             # print(tom)
#             d["Runtime"]=tom
#         if "Distributor:" in f:
#             d["Distributor"]=f[1:]
#             # return d
#     for i in d1:
#         dic={}
#         a=i.find("a")["href"][11:]
#         dic["name"]=a
#         l.append(dic)
#     # print(l)
#     for j in d2:
#         dic1={}
#         a1=j.find("a")["href"][11:]
#         dic1["name"]=a1
#         l.append(dic1)
#     with open("task13.json","w+") as file:
#         json.dump(l,file,indent=4)
#     return d,l
# print(scrape_movie_details("https://www.rottentomatoes.com/m/spider_man_into_the_spider_verse"))

