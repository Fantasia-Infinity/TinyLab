import random
import copy
import urllib
import urllib.request
import requests
from bs4 import BeautifulSoup
import re
import string

philosoherstone='https://zh.wikipedia.org/wiki/%E8%B3%A2%E8%80%85%E4%B9%8B%E7%9F%B3'
chemhistory='https://zh.wikipedia.org/wiki/%E4%BC%A0%E8%AF%B4'
lengend='https://zh.wikipedia.org/wiki/%E4%BC%A0%E8%AF%B4'
epic='https://zh.wikipedia.org/wiki/%E5%8F%B2%E8%AF%97'
chemicalelem='https://zh.wikipedia.org/wiki/%E5%8C%96%E5%AD%B8%E5%85%83%E7%B4%A0'
metal='https://zh.wikipedia.org/wiki/%E9%87%91%E5%B1%9E'
background='https://zh.wikipedia.org/wiki/%E8%83%8C%E6%99%AF'
xushishi='https://zh.wikipedia.org/wiki/%E5%8F%99%E4%BA%8B%E8%AF%97'
glass='https://zh.wikipedia.org/wiki/%E7%8E%BB%E7%92%83'
xilawen='https://zh.wikipedia.org/wiki/%E5%B8%8C%E8%85%8A%E8%AF%AD'
proxies = {
    'https': 'https://127.0.0.1:1080',
    'http': 'http://127.0.0.1:1080'
}
class Node:
    def __init__(self,url,father_node):
        self.url=url
        self.father_node=father_node

def get_all_links_inside_wiki(node):
    html=requests.get(node.url,proxies=proxies).text
    bsobj=BeautifulSoup(html,"html.parser")
    links=[]
    for a in bsobj.find_all('a'):
        link_url=a.get("href")
        if type(link_url)==str:
            if link_url.startswith("/wiki/") and "https://zh.wikipedia.org"+link_url!=node.url:
                if not link_url.startswith('/wiki/Special'):
                    if not link_url.startswith('/wiki/Wikipedia'):
                        if not link_url.startswith('/wiki/Project'):
                            if not link_url.startswith('/wiki/Help'):
                                if not link_url.startswith('/wiki/Category'):
                                    if not link_url.startswith('/wiki/Talk'):
                                        if not link_url.startswith('/wiki/File'):
                                            if not link_url.startswith('/wiki/Template'):
                                                if not link_url.startswith('/wiki/Portal'):
                                                    links.append(Node("https://zh.wikipedia.org"+link_url,node))
    return links

def print_path(node,begin_url):
    now=node
    while now.father_node!=None:
        if now.url==begin_url:
            print(now.url)
            return
        else:
            print(now.url)
            now=now.father_node
    print(begin_url)

def bfs_a_path_between_two_node(begin_node,end_node):
    visited=[]
    ready=[begin_node]
    count=0
    while True:
        now_node=ready.pop(0)
        if now_node.url==end_node.url:
            print_path(now_node,begin_node.url)
            return
        else:
            links=get_all_links_inside_wiki(now_node)
            for link in links:
                if [l for l in visited if l.url==link.url]!=[] or link.url==now_node.url:
                    continue
                elif link.url!=now_node.url and link!=now_node:
                    if link.url==end_node.url:
                        link.father_node=now_node
                        print_path(link,begin_node.url)
                        return
                    print('visited:'+link.url)
                    ready.append(link)
                    count+=1
                    print(count)
            visited.append(now_node)

""" for link in get_all_links_inside_wiki(Node(philosoherstone,None)):
    html=requests.get(link.url,proxies=proxies).text
    #bsobj=BeautifulSoup(html)
    #title=bsobj.title
    print(link.url) """

if __name__=="__main__":
    bfs_a_path_between_two_node(Node(philosoherstone,None),Node(xilawen,None))
    pass
