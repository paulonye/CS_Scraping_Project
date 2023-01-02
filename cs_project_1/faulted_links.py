import requests
from urllib3.exceptions import LocationParseError, RequestError
from bs4 import BeautifulSoup
import pandas as pd 
from requests.exceptions import Timeout, ConnectionError, InvalidSchema, RequestException
from time import time
from useful_links import useful_links
start = time()

def extract_all_links(site):
#This function extract all links/urls within any particular link/blog post    
    html = requests.get(site).text
    status_code = requests.get(site).status_code
    soup = BeautifulSoup(html, 'html.parser').find_all('a')
    links = [link.get('href') for link in soup]
    return links, status_code

def test_link(link):
#This function tests to see if a link works, and returns the status_code
    status_code = requests.get(link).status_code
    return status_code

new_list = useful_links()
#This is used to import the bloglinks that have been extracted from the previous scripts
#The links were extracted in batches

print('completed phase one')

dic = {}
#Creating an empty link that will be used to store the faulted Urls

count = 1
for url in new_list:
    all_links, status_code = extract_all_links(url)
#Returns tuple of all the links extracted from current bloglink and the status code of the bloglink
#It was observed that all bloglinks have a status_code of 200    
    all_links = list(set(all_links))
#Removing all duplicated links from the extracted links so as to improve performance
    link_list = {}
    print('CHECKING LINK {} - {}'.format(url, count))
    for link in all_links:
        try:
            if link == None:
                pass
            elif len(link) < 6:
                pass
            elif '/blog' in link:
                pass
            elif 'commonshare.com' in link:
                pass
            elif '/tag/' in link:
                pass
            elif '/categories/' in link:
                pass
            elif 'linkedin.com/' in link:
                pass
            elif 'twitter.com/' in link:
                pass
            elif link[0] == 'w':
                pass
            elif 'http' not in link:
                print('testing {}'.format(link))
                link = 'https://news.commonshare.com{}'.format(link)
                print('changed {}'.format(link))
                try:
                    requests.get(link, timeout = 5)
                    error_code = test_link(link)
                    if error_code == 404 or error_code == 504:
                        link_list[link] = error_code
                    else:
                        pass
                except Timeout:
                    link_list[link] = 'Timeout Error'

            else:
                print('testing {}'.format(link))
                try:
                    requests.get(link, timeout = 10)
                    error_code = test_link(link)
                    if error_code == 404 or error_code == 504:
                        link_list[link] = error_code
                    else:
                        pass
                except Timeout:
                    link_list[link] = 'Timeout Error'

        except LocationParseError as lpe:
            link_list[link] = lpe
            
        except ConnectionError as ce:
            link_list[link] = ce
          
        except InvalidSchema:
            link_list[link] = 'InvalidSchema'

        except TypeError as e:
            link_list[link] = e

        except RequestException as err:
            link_list[link] = err

        except RequestError as urerr:
            link_list[link] = urerr

    dic[url] = link_list
    count = count + 1



blog_links = [i for i in dic.keys()]
broken_links = [i for i in dic.values()]
final_data = pd.DataFrame({'blog_links': blog_links, 'broken_links': broken_links})
#Converting the dictionary that stored the faulted links for each blog links into a dataframe
final_data.to_csv('broken_links.csv')
#Saving the final file as csv

#print(dic)
print(f'Time taken to run: {time() - start} seconds')