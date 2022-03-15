from task5 import get_movie_list_details
import json
m_language=get_movie_list_details()
def analyse_movies_language():
    d={}
    for i in m_language:
        if "Language" in i:
                # print(i["Language"])
                if i["Language"] in d:
                    d[i["Language"]]=d[i["Language"]]+1
                if i["Language"] not in d:
                    d[i["Language"]]=1
    # print(d)
    with open("task6.json","w+") as f1:
        json.dump(d,f1,indent=4)
analyse_movies_language()

