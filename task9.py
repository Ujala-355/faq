from task1 import scrape_movie
import random,time,json
import os
caching=scrape_movie()
def caching_movie_details():
     random_sleep=random.randint(1,3)
     for i in caching:
          if "Name" in i:
               path="/home/admin123/task9/task9"+i["Name"]+".json"
          print(path)
          if os.path.exists(path):
               pass
          else:
               a=open(path,"w+")
               json.dump(i,a,indent=4)
          time.sleep(random_sleep)
caching_movie_details()