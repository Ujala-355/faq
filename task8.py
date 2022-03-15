from task1 import scrape_movie
import  requests
import os
caching=scrape_movie()

def caching_movie_details():
     for i in caching:
          p=("/home/admin123/Task8"+i["Name"])+".text"
          if os.path.exists(p):
               pass
          else:
               with open(("/home/admin123/Task8"+i["Name"])+".text","w") as f:
                    url=requests.get(i["Url"])
                    f=f.write(url.text)               
caching_movie_details()
