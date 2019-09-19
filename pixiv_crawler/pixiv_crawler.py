
'''
import requests
from bs4 import BeautifulSoup
url = "http://www.google.com/"
req = requests.get(url)
tex = req.text
soup = BeautifulSoup(tex,"lxml")
print(soup.prettify())
'''
'''
import urllib2
import re

def req(url):
    response = urllib2.urlopen(url)  # import urllib2
    return response

def decode(response):
    card_root_div = r'<div class="groom-module home-card">(.*?)</div>'
    card_title_p = r'<p class="title">(.*?)</p>'
    card_author_p = r'<p class="author">(.*?)</p>'
    card_play_p = r'<p class="play">(.*?)</p>'
    all_card_root = re.findall(card_root_div, response, re.S|re.M)  # import re
    for c in all_card_root:
        title = re.search(card_title_p, c, re.S|re.M).group(1)
        author = re.search(card_author_p, c, re.S|re.M).group(1)
        play = re.search(card_play_p, c, re.S|re.M).group(1)
        print title, author, play


bilibili_url = 'https://www.bilibili.com/'
decode(req(bilibili_url).read())
'''
#! -*- coding:utf-8 -*-

"""
Author:Lz1y

2017.6.6
"""


import re
import requests
from bs4 import BeautifulSoup as bs

def getAv():
    try:
        av = input("«Î ‰»ÎAv∫≈:")
        url = "http://www.bilibili.com/video/av"+str(av)+"/"
        getHTMLText(url,av)
    except:
        print(" ‰»Î¥ÌŒÛ.")

def getHTMLText(url,av):
    headers={'User-Agent':"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)",}
    u = requests.get(url=url,headers=headers)
    html = u.text
    cid = re.findall(r'cid=(.*?)&aid=',html)[0]
    print(cid)
    getDanmu(cid,av)
    
    
def getDanmu(cid,av):
    dmurl = "http://comment.bilibili.com/18299471.xml"
    
    dmhtml = requests.get(dmurl).text
    soup = bs(dmhtml,'lxml')
    dmlist = soup.find_all('d')

    
    printDanmu(dmlist,av)
    
    
def printDanmu(dmlist,av):
    filename = "av"+str(av)+ ".txt"
      
        
    
    with open(filename,'w',encoding="utf-8") as t:
        for dm in dmlist:
            
            t.write(str(dm.string)+'\n')
            print("Loading...\n")
    
    

if __name__ == "__main__":
    getAv()

r=requests.get("http://www.baidu.com")
r.encoding='utf-8'
html=r.text
with open('test6.txt','w',encoding="utf-8") as f:
    f.write(html)


r=requests.get("http://comment.bilibili.com/279786.xml")
r.encoding='utf-8'
html=r.text
with open('test6.txt','w',encoding="utf-8") as f:
    f.write(html)
'''
import requests
from bs4 import BeautifulSoup

res = requests.get('https://www.pixiv.net/member_illust.php?id=333556&type=illust')
res.raise_for_status()  # this line trows an exception if an error on the 
                     # connection to the page occurs.

plain_text = res.text      


soup = BeautifulSoup(plain_text, "lxml")
for link in soup.findAll("a"):
    href=link.get('href')
    tit = link.string

    print(href)
    print(tit)
    print (link.text)
'''

'''
import requests
from bs4 import BeautifulSoup



url = 'https://www.ebay.ca/sch/i.html?_from=R40&_trksid=p2380057.m570.l1313.TR0.TRC0.A0.H0.Xmiku.TRS3&_nkw=miku&_sacat=0' 
source_code = requests.get(url)
plain_text = source_code.text
soup = BeautifulSoup(plain_text,"lxml")
for link in soup.findAll('a', {'class' : "w-item__info clearfix"}):
    href=link.get('href')
    print(href)
'''
