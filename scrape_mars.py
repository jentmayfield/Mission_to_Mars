from splinter import Browser
from bs4 import BeautifulSoup as bs
import time
import pandas as pd


def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {"executable_path": "/usr/local/bin/chromedriver"}
    return Browser("chrome", **executable_path, headless=False)

def scrape_info_news():
    browser = init_browser()
    # Visit twitter.com/marswxreport?lang=en
    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)
  
    time.sleep(1)

    # Scrape page into Soup
    html = browser.html
    soup = bs(html, "html.parser")

    # Get the temperature of Mars
    news_title = soup.find('div', class_='content_title').text
    news_p = soup.find('div', class_='article_teaser_body').text

    # Store data in a dictionary
    mars_news_data = {
        "news_title": news_title,
        "news_p": news_p
    }

      # Close the browser after scraping
    browser.quit()

    # Return results
    return mars_news_data

def scrape_image():
    browser = init_browser()
    # Visit twitter.com/marswxreport?lang=en
    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url)
  
    time.sleep(1)

    for x in range(1, 2):

        html = browser.html
        soup = bs(html, 'html.parser')

        articles = soup.find_all('article', class_='carousel_item')
    
        for article in articles:
          featured_image_url= "https://www.jpl.nasa.gov/" + article['style'].split('background-image:')[-1][7:-3]


    # Store data in a dictionary
    mars_image_data = {
        "featured_image_url": featured_image_url
    }

      # Close the browser after scraping
    browser.quit()

    # Return results
    return mars_image_data

def scrape_info_weather():
    browser = init_browser()
    # Visit twitter.com/marswxreport?lang=en
    url = 'https://twitter.com/marswxreport?lang=en'
    browser.visit(url)

    time.sleep(1)

    # Scrape page into Soup
    html = browser.html
    soup = bs(html, "html.parser")

    # Get the temperature of Mars
    tweets = soup.find_all('p', class_='TweetTextSize TweetTextSize--normal js-tweet-text tweet-text')
    tweet = (tweets[0].text)


    # Store data in a dictionary
    mars_data = {
        "tweet": tweet
    }

      # Close the browser after scraping
    browser.quit()

    # Return results
    return mars_data

def scrape_info_facts():
    browser = init_browser()
    # Visit twitter.com/marswxreport?lang=en
    url = 'https://space-facts.com/mars/#facts'
    browser.visit(url)

    time.sleep(1)

    # Scrape page into Soup
    html = browser.html
    soup = bs(html, "html.parser")

    # Get the temperature of Mars
    tables = pd.read_html(url)

    df = tables[0]
    df.columns = ['', 'Value']
    df.head()
    df.set_index('', inplace=True)
    df.head()
    html_table = df.to_html()
    # html_table = replace("\n","")
    

    # Store data in a dictionary
    mars_facts_data = {
        "html_table": html_table
    }

      # Close the browser after scraping
    browser.quit()

    # Return results
    return mars_facts_data

def scrape_hemi_image():
    browser = init_browser()
    # Visit twitter.com/marswxreport?lang=en
    url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url)
  
    time.sleep(1)

    dict_list=[]
    html = browser.html
    soup = bs(html, 'html.parser')
    headings = soup.find_all('h3')

    image_links = []
    for heading in headings:
      new_dict={}
      clicklink=heading.text
      time.sleep(1)
      browser.click_link_by_partial_text(clicklink)
      time.sleep(1)
      html = browser.html
      soup = bs(html, 'html.parser')
      imageurl=soup.find('div', class_='downloads')
      urllink=imageurl.find('a')['href']
      print(urllink)
      image_links.append(urllink)
      time.sleep(1)
      browser.click_link_by_partial_text('Back')
      new_dict.update({'title':heading.text,'img_url':urllink})
      dict_list.append(new_dict)
      time.sleep(2)

    # Store data in a dictionary
    mars_hemi_image_data = {
        "dict_list": dict_list
    }

      # Close the browser after scraping
    browser.quit()

    # Return results
    return mars_hemi_image_data

