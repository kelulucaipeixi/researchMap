import urllib.request
from bs4 import BeautifulSoup
import urllib.parse
import csv
import time
titles=[]

#from url of certain paper to url of papers cited the paper
def getCitedUrl(origin_url):
	headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.75 Safari/537.36'}  
	request=urllib.request.Request(origin_url,headers=headers)
	response=urllib.request.urlopen(request)
	source_code=response.read()
	soup=BeautifulSoup(source_code,'html.parser')
	hrefs=soup.find('div',id="gs_res_ccl_mid").findAll('a')
	for a in hrefs:
		if "被引用次数" in str(a.find(text=True)):
			div=str(a['href'])
	return div


def crawler(url):
	global titles
	headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.75 Safari/537.36'}  
	request=urllib.request.Request(url,headers=headers)
	response=urllib.request.urlopen(request)
	source_code=response.read()
	soup=BeautifulSoup(source_code,'html.parser')
	mid_div=soup.find('div',id='gs_res_ccl_mid')
	h3=mid_div.findAll('h3')
	for title in h3:
		res=title.find('a')
		if res:
			res=res.find(text=True)
			titles.append(res)
		# print(res)
	bot_div=soup.find('div',id='gs_res_ccl_bot')
	try:
		next_page=bot_div.find('td',align='left')
		link=next_page.find('a')['href']
		link="https://scholar.google.com.hk"+link
		return link
	except:
		print("crawler over.")
if __name__=="__main__":
	names=["Asking clarifying questions in open-domain information-seeking conversations","Towards conversational search and recommendation: System Ask, user respond","Towards conversational recommender systems"]
	pre_url="https://scholar.google.com.hk/scholar?hl=zh-CN&as_sdt=0%2C5&q="
	pre_url2="https://scholar.google.com.hk"
	f=open('outcome.csv','w',newline='')
	writer=csv.writer(f)
	writer.writerow(["source","target"])
	for paperName in names:
		titles=[]
		enc_paperName=paperName.encode('utf-8')
		suf_url = urllib.parse.quote(enc_paperName)
		url=pre_url+suf_url
		url=pre_url2+getCitedUrl(url)
		print(url)
		while url:
			url=crawler(url)
		for title in titles:
			for name in names:
				if str(name)==str(title):
					writer.writerow([title,paperName])
