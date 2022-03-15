# task3
from task2 import group_by_year
import json
movies=group_by_year()
def group_by_decade():
    movies_decade={}
    list1=[]
    for index in movies:
        # print(type(index))
        Mod=(index)%10  #mod=3
        decade=(index)-Mod #1973-3=1970
        if decade not in list1:
            list1.append(decade)
    list1.sort()
    for i in list1:
        movies_decade[i]=[]
    for i in movies_decade:
        dec10=i+9 #dec10=1959
        for x in movies:
            if x<=dec10 and x>=i:
                for v in movies[x]:
                    movies_decade[i].append(v)
    with open("task3.json","w") as fd:
        json.dump(movies_decade,fd,indent=4)
    return(movies_decade)
group_by_decade()