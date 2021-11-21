import os
import yaml
from bs4 import BeautifulSoup
import requests
from csv import DictWriter
from seleniumbase import BaseCase

dataset_path = f"{os.getcwd()}/dataset/" 
if not os.path.exists(dataset_path):
    os.mkdir(dataset_path)

file_path = f"{os.getcwd()}/config.yml"    
with open(file_path) as data:
    config_data = yaml.safe_load(data)

FILE_NAME = dataset_path + config_data['file_name']
URL_FILE_NAME = dataset_path  + config_data['url_file_name']
URL = config_data['inshort_url']

class TestScrapeNews(BaseCase):
    category_list = []
    PAGE_COUNT = 1   # count to load page

    def test_news(self):        
        self.get_news_category()

        self.inshort_news_scraper(self.category_list)

    def get_news_category(self):
        '''
        Get all news category URL
        '''
        url = URL
        self.open(url)
        category_xp = '//ul[@class="category-list"]//a'
        category_ele = self.find_elements(category_xp)
        category_url = []
        for category in category_ele:
            link = category.get_attribute('href')
            self.category_list.append(link)
            category_url.append({'URL': link})
        
        # write to csv file
        self.write_csv(category_url, URL_FILE_NAME)
        print("##"*30)
        print(f"Able to get URL's of all category {self.category_list} and write to csv file !!\n")
        print("##"*30)

    def inshort_news_scraper(self, category_list):
        '''
        Open all url's and get data.
        '''
        print("Start NEWS scraping")
        for url in category_list[1:2]:
            news_category = url.split("/")[-1]
            self.open(url)
            self.get_news_data(news_category)
            self.sleep(2)
            print(f"Done NEWS scraping for {url} !!")
        print("Completed NEWS scraping for all URL!!")
        print("##"*30)

    def get_news_data(self, category):
        '''
        Get data from URL using Selenium
        '''
        try:
            '''
            Thic block is to click on load more news button
            '''
            load_button = '//div[@class="load-more-wrapper"]'
            for i in range(self.PAGE_COUNT):
                self.find_element(load_button, timeout=20)
                self.click(load_button)
                self.sleep(2)
        except Exception as exception:
            print(f"Exception while clicking load more news button: Error is {exception}")

        try:
            headline_xp = '//span[@itemprop="headline"]'
            headline_ele = self.find_elements(headline_xp)
            
            content_xp = '//div[@itemprop="articleBody"]'
            content_ele = self.find_elements(content_xp)
            
            author_xp = '//div[@class="news-card-author-time news-card-author-time-in-title"]//span[@class="author"]'
            author_ele = self.find_elements(author_xp)

            newsurl_xp = '//a[@class="clickable"]'
            newsurl_ele = self.find_elements(newsurl_xp)

            news_to_csv = []
            for title, content, author, newsurl in zip(headline_ele, content_ele, author_ele, newsurl_ele):
                news_dict = {
                    "title": title.text,
                    "content": content.text,
                    "author": author.text,
                    "url": newsurl.get_attribute('href'),
                    "category": category}
                    # FIELD_NAME = ['title', 'content', 'author', 'url', 'category']
                news_to_csv.append(news_dict)
        except Exception as exception:
            print(f"Exception while loading news data: Error is {exception}")
        
        self.sleep(2)

        # write to csv file
        self.write_csv(news_to_csv, FILE_NAME)

    def write_csv(self, df, file_name):
        '''
        Function to write news data to csv file.
        '''
        keys = df[0].keys()
        with open(file_name, 'a+', newline='', encoding="utf-8") as output_file:
            dict_writer = DictWriter(output_file, keys)
            dict_writer.writeheader()
            dict_writer.writerows(df)
        print(f"Successfully write data to {file_name}")

    def get_news_data_soup(self, url):
        '''
        Get news data from URL using BeautifulSoup
        '''
        soup = self.read_url(url)

        results = soup.find("div", {"class":"container"})
        news_data = results.find_all("div", {"class":"news-card z-depth-1"})
        news_to_csv = []
        for item in news_data:
            title = item.find("span", {"itemprop":"headline"}).text
            content = item.find("div", {"itemprop":"articleBody"}).text
            link = "inshorts.com" + item.find("a", {"class":"clickable"})['href']
            
            news_dict = {
                "title": title,
                "content": content,
                "link": link}
            news_to_csv.append(news_dict)
        
        # write to csv file
        self.write_csv(news_to_csv)

    def read_url(self, url):
        '''
        Read URL using BeautifulSoup
        '''
        page = requests.get(url)
        print("Status code:", page.status_code)
        soup = BeautifulSoup (page.text, "html.parser")
        return soup
