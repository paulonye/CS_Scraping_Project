import pandas as pd 

def useful_links():
#This function extracts only the blog links from all the links
#scrapped and then returns it in a list format to be used for faulted_blog_links.py file
	tests = pd.read_csv('cs_blogs1.csv')
	new_list = []
	for link in tests['links']:
		if 'blog' not in link:
			pass
		else:
			new_list.append(link)
	new_list = list(set(new_list))
#ensuring that duplicates are removed from the list
	return new_list
#returns a list of 2124 records








