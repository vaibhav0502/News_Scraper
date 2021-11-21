# News_Scraper
Scraping news from ```inshorts``` websites using Python SeleniumBase.

## Setup project environment with virtualenv and pip:

- Install [virtualenv](https://pypi.org/project/pipenv/) using ```pip install --user pipenv```. 
- Enter virtualenv using ```pipenv shell```
- Run ```pipenv install -r requirements.txt ```
- Install ```pip``` dependencies inside the virtualenv : ```pipenv install dep==```


## Install SeleniumBase:
- [Seleniumbase](https://pypi.org/project/seleniumbase/) for web scraping .
- [Visit for more info ](https://seleniumbase.io/)


## Features:
- Collect NEWS from [inshorts](https://inshorts.com/en/read)

  ![news_sample](https://user-images.githubusercontent.com/42543380/142772408-5b0ea56b-e6b8-4947-900c-34338f9348da.PNG)

- Collect NEWS Heading, Content, Author of different categories like ```World, Sports, Science, Politics etc```
   
   ![category](https://user-images.githubusercontent.com/42543380/142772468-e5331322-5f47-4aa7-964e-273e6ccf96c5.PNG)

## Run News Scrapper:
- Open config.yml
    - file_name: Define csv filename to strore news data      # eg. news_with_category.csv 
    - url_file_name: Define csv filename to news URL          # eg. url_file.csv 
    - inshort_url: Set inshorts URL                           # https://inshorts.com/en/read

- Run ```pytest test_news_scrapper.py -s --headless```
- CSV file will have following columns
    - [title, content, author, url, category]

![news](https://user-images.githubusercontent.com/42543380/142772456-2e67e998-5b40-4dcd-bc5a-d131a4109877.PNG)

- CSV files will be stored inside ```dataset``` folder

---------
