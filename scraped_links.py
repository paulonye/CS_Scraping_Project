import requests
from bs4 import BeautifulSoup
import pandas as pd

def extract_all_links(site):
#This function extract all links/urls within any particular link/blog post
    html = requests.get(site).text
    status_code = requests.get(site).status_code
    soup = BeautifulSoup(html, 'html.parser').find_all('a')
    links = [link.get('href') for link in soup]
    return links

t_link= []
url = 'https://news.commonshare.com/?page='
for page in range(0,360):
#359 web pages were identified for the blog
	l1 = extract_all_links(url+str(page))
#the l1 is used to extract certain(not all) links within each page of the commonshare blog website
#based on the for loop below
	for link in l1:
		if link == None:
			pass
		elif len(link) < 5:
			pass
		elif 'https' not in link:
			link = 'https://news.commonshare.com{}'.format(link)
			t_link.append(link)
		else:
			t_link.append(link)

	
all_links = pd.DataFrame({'links':t_link})
#the list is then converted to a dataframe
all_links.to_csv('cs_blogs1.csv')
#the dataframe is then saved in a csv file 
#which will be used in useful_links.py and faulted_blog_links.py files
print(all_links)



