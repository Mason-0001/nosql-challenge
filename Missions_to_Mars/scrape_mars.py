#!/usr/bin/env python
# coding: utf-8

# # Mission_to_Mars initial scraping for use in app

# ## Scrape the [Mars News Site](https://redplanetscience.com/) and collect the latest News Title and Paragraph Text. Assign the text to variables for use later.

# In[2]:


# Dependencies
from splinter import Browser
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager


# In[12]:

def scrape():
    # URL of page to be scraped
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)
    url = 'https://redplanetscience.com/#'
    browser.visit(url)


    # In[49]:


    # HTML object
    html = browser.html
    # Parse HTML with Beautiful Soup
    soup = BeautifulSoup(html, 'html.parser')
    # Retrieve all elements that contain book information
    articles = soup.find_all('html')


    # In[44]:


    # Iterate through each article
    for article in articles:
        # Use Beautiful Soup's find() method to navigate and retrieve attributes
        news_title = article.find('div', class_='content_title').text
        news_p = article.find('div', class_='article_teaser_body').text
        
        print(news_title)
        print(news_p)


    # In[46]:


    # URL of page to be scraped
    url = 'https://spaceimages-mars.com'
    browser.visit(url)


    # In[50]:


    # HTML object
    html = browser.html
    # Parse HTML with Beautiful Soup
    soup = BeautifulSoup(html, 'html.parser')
    # Retrieve all elements that contain book information
    articles = soup.find_all('html')


    # In[65]:


    featured_image_url = "https://spaceimages-mars.com/" + soup.find("img", class_="headerimage")["src"]
    print(featured_image_url)


    # In[52]:


    # Dependencies
    import pandas as pd


    # In[53]:


    # URL of page to be scraped
    url = 'https://galaxyfacts-mars.com'
    tables = pd.read_html(url)
    tables


    # In[55]:


    table1_df = tables[0]
    table1_df


    # In[56]:


    html_table = table1_df.to_html()
    html_table



    # In[43]:


    # URL of page to be scraped
    url = 'https://marshemispheres.com/'
    browser.visit(url)

    # make dictionaries to append
    mars_maps = {"img_url": [], "title": []}


    # In[45]:


    # Go to first link
    browser.links.find_by_partial_text('Cerberus Hemisphere Enhanced').click()
    # HTML object
    html = browser.html
    # Parse HTML with Beautiful Soup
    soup = BeautifulSoup(html, 'html.parser')
    # Retrieve link that contains img png.
    articles = soup.find_all('html')
    cerb_img_url = "https://marshemispheres.com/" + soup.find("a", text="Sample")["href"]
    title_c = soup.find('h2', class_="title").text
    mars_maps["img_url"].append(cerb_img_url)
    mars_maps["title"].append(title_c)

    print(mars_maps)


    # In[46]:


    # go back, then to next link
    browser.back()
    browser.links.find_by_partial_text('Schiaparelli Hemisphere Enhanced').click()

    # HTML object
    html = browser.html
    # Parse HTML with Beautiful Soup
    soup = BeautifulSoup(html, 'html.parser')
    # Retrieve link that contains img png.
    articles = soup.find_all('html')
    schia_img_url = "https://marshemispheres.com/" + soup.find("a", text="Sample")["href"]
    title_s = soup.find('h2', class_="title").text

    mars_maps["img_url"].append(schia_img_url)
    mars_maps["title"].append(title_s)

    print(mars_maps)


    # In[47]:


    # go back, then to next link
    browser.back()
    browser.links.find_by_partial_text('Syrtis Major Hemisphere Enhanced').click()

    # HTML object
    html = browser.html
    # Parse HTML with Beautiful Soup
    soup = BeautifulSoup(html, 'html.parser')
    # Retrieve link that contains img png.
    articles = soup.find_all('html')
    syrtis_img_url = "https://marshemispheres.com/" + soup.find("a", text="Sample")["href"]
    title_sy = soup.find('h2', class_="title").text
    mars_maps["img_url"].append(syrtis_img_url)
    mars_maps["title"].append(title_sy)

    print(mars_maps)


    # In[48]:


    # go back, then to next link
    browser.back()
    browser.links.find_by_partial_text('Valles Marineris Hemisphere Enhanced').click()

    # HTML object
    html = browser.html
    # Parse HTML with Beautiful Soup
    soup = BeautifulSoup(html, 'html.parser')
    # Retrieve link that contains img png.
    articles = soup.find_all('html')
    valles_img_url = "https://marshemispheres.com/" + soup.find("a", text="Sample")["href"]
    title_v = soup.find('h2', class_="title").text
    mars_maps["img_url"].append(valles_img_url)
    mars_maps["title"].append(title_v)

    print(mars_maps)
    browser.quit()

    # In[ ]:
     # Store data in a dictionary
    mars_data = {
        "news_title": news_title, 
        "news_text": news_p, 
        "featured_image": featured_image_url, 
        "html_table": html_table, 
        "mars_maps": mars_maps 
    }
    return mars_data

    # %%
