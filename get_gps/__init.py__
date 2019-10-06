import requests
import re
from bs4 import BeautifulSoup


def get_lat_lon(id):
    r = requests.get("https://api.openstreetmap.org/api/0.6/node/"+str(id))
    bf = BeautifulSoup(r.text, features='lxml')
    string = str(bf.find('node'))
    tag_list = re.split(" |=|\"" ,string)
    # print(tag_list)
    # print (tag_list[11],tag_list[15])
    return float(tag_list[11]), float(tag_list[15])


if __name__=='__main__':
    print(get_lat_lon(25585093))
