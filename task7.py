from task5 import get_movie_list_details
import json
m_directors=get_movie_list_details()
def analyse_movies_language():
    dic={}
    for i in m_directors:
        # if "Director" in i:
        for j in i["Director"]:
            # print(j)
                if j in dic:
                    dic[j]=dic[j]+1
                if j not in dic:
                    dic[j]=1
    # print(dic)
    with open("task7.json","w+") as f1:
        json.dump(dic,f1,indent=4)
analyse_movies_language()

