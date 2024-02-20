from unittest import result
import requests 
from bs4 import BeautifulSoup
import re #regular expression
#from urllib.request import urlretrive #downliading mp4
import sys #for argument parsing
#exception handlind

if len(sys.argv) > 1:
    url = sys.argv[1]
else:
        sys.exit("error:please enter the TED talk URL")
#url = ""
#url = ""
r = requests.get(url)  # url gets stored in object 
print("Download about to start")

soup = BeautifulSoup(r.content, features= "lxml")

for val in soup.findAll("script"):
    if(re.search("talkPage.init",str(val))) is not None:
        result = str(val)

result_mp4 =  re.search("(?P<url>https?://[^\s]+)(mp4)", result).group("url")
mp4_url = result_mp4.split('"') [0]

print("Downloading video from ...."+ mp4_url)
file_name= mp4_url.split("/")[len(mp4_url.split("/"))-1].split('?')[0] # to generate file name automatically from video name

print("Storing vide in ..."+ file_name)
r = requests.get(mp4_url)
with open(file_name, 'wb') as f:
    f.write(r.content)

#alternate method
#url retrieve(mp4 url, file name)

print("Download Process Finished")
