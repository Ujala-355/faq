# task2
from task1 import scrape_movie
import json
movies=scrape_movie()
# print(data)
def group_by_year():   
    years=[]
    for i in movies:
        year=i["Year"] 
        if year not in years:
            years.append(year)
    # print(years)
    movie_dict={i:[] for i in years}    
    for i in movies:
        year=i["Year"]
        # print(year)
        for x in movie_dict:
            if str(x)==str(year):
                movie_dict[x].append(i)
    # print(movie_dict)
    with open("task2.json","w") as fd:
        json.dump(movie_dict,fd,indent=4)
    return movie_dict
(group_by_year())
