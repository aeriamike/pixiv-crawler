#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
from PIL import Image
import io
import csv
import random

'''
source = requests.get('https://web.archive.org/web/20160614144700/https://www.pixiv.net/tags.php').text
soup = BeautifulSoup(source, 'lxml').find('ul')
print(soup.prettify())
'''

import requests
import re
import http.cookiejar
from bs4 import BeautifulSoup
from PIL import Image


class PixivSpider(object):
    def __init__(self):
        self.session = requests.Session()
        self.headers = {
             'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.96 Safari/537.36',
             'Referer': 'https://www.pixiv.net/member_illust.php?mode=medium&illust_id=69845158'}
        self.session.headers = self.headers
        self.session.cookies = http.cookiejar.LWPCookieJar(filename='cookies')
        try:
            # 加载cookie
            self.session.cookies.load(filename='cookies', ignore_discard=True)
        except:
            print('cookies不能加载')

        self.params ={
            'lang': 'en',
            'source': 'pc',
            'view_type': 'page',
            'ref': 'wwwtop_accounts_index'
        }
        self.datas = {
            'pixiv_id': '',
            'password': '',
            'captcha': '',
            'g_reaptcha_response': '',
            'post_key': '',
            'source': 'pc',
            'ref': 'wwwtop_accounts_indes',
            'return_to': 'https://www.pixiv.net/'
            }

    def get_postkey(self):
        login_url = 'https://accounts.pixiv.net/login' # 登陆的URL
        # 获取登录页面
        res = self.session.get(login_url, params=self.params)
        # 获取post_key
        pattern = re.compile(r'name="post_key" value="(.*?)">')
        r = pattern.findall(res.text)
        self.datas['post_key'] = r[0]

    def already_login(self):
        # 请求用户配置界面，来判断是否登录
        url = 'https://www.pixiv.net/setting_user.php'
        login_code = self.session.get(url, allow_redirects=False).status_code
        if login_code == 200:
            return True
        else:
            return False

    def login(self, account, password):
        post_url = 'https://accounts.pixiv.net/api/login?lang=en' # 提交POST请求的URL
        # 设置postkey
        self.get_postkey()
        self.datas['pixiv_id'] = account
        self.datas['password'] = password
        # 发送post请求模拟登录
        result = self.session.post(post_url, data=self.datas)
        print(result.json())
        # 储存cookies
        self.session.cookies.save(ignore_discard=True, ignore_expires=True)
        return self
        
    def image (self):
        '''
        url2 = 'https://www.pixiv.net/bookmark.php?type=reg_user'
        #referer = 'https://www.pixiv.net/ranking.php?mode=oversea&date=20180729'
        req2 = requests.get(url2, headers=self.session.headers, cookies=self.session.cookies).text
        print(req2)
        print("am i here?"+'\n')
        bs = BeautifulSoup(req2, 'lxml').find('div',class_='members')
        
        print(bs.prettify())
        '''
        '''
        source = requests.get('https://www.pixiv.net/tags.php').text
        soup = BeautifulSoup(source, 'lxml')
        for a in soup.find('div', class_='column-content'):
            print(a.prettify())
        '''
        date = ['201401','201402','201403',
                '201404','201405','201406',
                '201407','201408','201409',
                '201410','201411','201412',
                '201501','201502','201503',
                '201504','201505','201506',
                '201507','201508','201509',
                '201510','201511','201512',
                '201601','201602','201603',
                '201604','201605','201606',
                '201607','201608','201609',
                '201610','201611','201612',
                '201701','201502','201503',
                '201704','201505','201506',
                '201707','201508','201509',
                '201710','201511','201512',
                '201801','201802','201603',
                '201804','201805']
        taglist = []
        countlist = []
        datalist = []
        
        i = 1
        for i in range(1,len(date)):

            source = requests.get('https://web.archive.org/web/' + date[i] +'01/http://www.pixiv.net/tags.php').text
            soup = BeautifulSoup(source, 'lxml')
            #for access in soup.find('div', class_='column-content'):
                #print(access.prettify())
                #print(access)
            #print('the date is ' + date[i])
            
            num = 0
            #for access in soup.find_all('a',class_='tag-name icon-text'):
            for access in soup.find_all('li'):
                if num < 25:
                    
                    tag = access.find('a',class_='tag-name icon-text')
                    count = access.find('span',class_='count-badge')
                    datenow =  date[i][:4]+"-"+date[i][4:] + "-01"
                    try:
                       # print(tag.string)
                       # print(count.string)
                       # print(datenow)
                        
                        #print(count.string)
                        #print(access.prettify())
                        
                        num = num+1
                        taglist.append(tag.string)
                        countlist.append(count.string)
                        datalist.append(datenow)
        
                    
                    except AttributeError:
                        pass;

                   
                else:
                    break;

        #print (taglist)
        #print (countlist)
        #print (datalist)
       

        thefile = open("pixiv_tag.txt",'w')
        for item in taglist:
            thefile.write("%s\n" %item)
        thefile = open("pixiv_count.txt",'w')
        for item in countlist:
            thefile.write("%s\n" %item)

        thefile = open("pixiv_date.txt",'w')
        for item in datalist:
            thefile.write("%s\n" %item)

        thefile2 = open("pixiv_tagresult.txt",'w')
        thefile2.write("name,type,value,date\n")
        ii = 0
        for ii in range(0,len(taglist)):
            thefile2.write("%s," %(taglist[ii]))
            radi = random.choice("vwxyz")
            thefile2.write(radi+",")
            thefile2.write("%s,%s\n" %(countlist[ii],datalist[ii]))
            
        '''
        with open("pixiv_tag.csv", "w") as f:
            writer = csv.writer(f)
            writer.writerows(taglist)
       '''
        
       # print(bs.prettify())

if __name__ == "__main__":
    spider = PixivSpider()
    if spider.already_login():
        print('用户已经登录')

        
    else:

        account = input('请输入用户名\n> ')
        password = input('请输入密码\n> ')
        spider.login(account, password)
    spider.image()

   

