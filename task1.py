from bs4 import BeautifulSoup
import requests ,json
a=requests.get("https://www.rottentomatoes.com/top/bestofrt/top_100_animation_movies/")
soup=BeautifulSoup(a.text,"html.parser")   
def scrape_movie() :
    main_div=soup.find("div",class_="panel-body content_body allow-overflow")
    table=main_div.find("table", class_="table")
    trs=table.find_all("tr")
    l=[]
    for i in trs:
        dic={}
        td=i.find_all("td")
        for j in td:
            rank=i.find("td",class_="bold").get_text()[:-1]
            dic["Rank"]=int(rank)
            rating=i.find("span",class_="tMeterScore").get_text()[1:3]
            dic["Rating"]=rating
            a=i.find("a",class_="unstyled articleLink")["href"][3:]
            dic["Name"]=a
            a=i.find("a",class_="unstyled articleLink").get_text()[-5:-1]
            dic["Year"]=int(a)
            movie_url=a=i.find("a",class_="unstyled articleLink")["href"]
            url="https://www.rottentomatoes.com/"+movie_url
            dic["Url"]=url
        l.append(dic)
        if {} in l:
            l.remove({})
    with open("text1.json","w") as f:
        json.dump(l,f,indent=4)
    return l
scrape_movie()