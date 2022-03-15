
from task1 import scrape_movie
from task4 import scrape_movie_details
import json
movies_data=scrape_movie()
def get_movie_list_details():
    movie_list=[]
    for i in movies_data:
        url=i["Url"]
        # print(url)
        d=scrape_movie_details(url)
        # print(d)
        movie_list.append(d)
    # print(movie_list)
    with open("task5.json","w") as f:
        json.dump(movie_list,f,indent=5)
    return movie_list
get_movie_list_details()

