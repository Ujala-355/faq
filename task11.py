from task5 import get_movie_list_details
import json

generate_total=get_movie_list_details()
 
def analyse_movies_genre():
    dict={}
    c=0
    for i in generate_total:
        for j in i["Genre"]:
            # print(j)
            if j in dict:
                dict[j]=dict[j]+1
            if j  not in dict:
                dict[j]=1
    # print(dict)
    with open("task11.json","w+") as f11:
        json.dump(dict,f11,indent=4)
analyse_movies_genre()
 