from task5 import get_movie_list_details
import json
m_directors=get_movie_list_details()
def analyse_language_and_directors():
    di={}
    list=[]
    for i in m_directors:   
        # if "Director" in i:
        for j in i["Director"]:
            if j not in di:
                list.append(j)
    for y in list:
        dic={}
        for x in m_directors:
            if y in x["Director"]:
                if "Language" in x:
                    # for z in x["Language"]:
                        # print(x["Language"])
                        if x["Language"] in dic:
                            dic[x["Language"]]=dic[x["Language"]]+1
                        if "Language" not in dic:
                            dic[x["Language"]]=1
                            # print(dic)
        di[y]=dic
    # print(di)
    with open("task10.json","w+") as f1:
        json.dump(di,f1,indent=4)
analyse_language_and_directors()
