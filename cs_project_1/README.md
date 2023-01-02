# CS_Scraping_Project_1

The aim of this project is to check all the links within all the blog posts listed on Common Share ('https://news.commonshare.com/?page=') and return the broken links

The project was divided into 2
- Extract all the blog post links (scraped_links.py and useful_links.py)
- Check each blog post and return the broken links (faulted_links.py)

## Options for Handling Scripts

#1

Run the script in the ff order as seen below and ensure the csv file (cs_blogs1) created from the scraped_links.py is in the same directory as the python scripts:

scraped_links.py --> useful_links.py --> faulted_links.py

#2

Run the script in the ff order using the already uploaded csv file (which contains the blog links)

useful_links.py --> faulted_links.py
