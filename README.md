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
- Collect NEWS Heading, Content, Author of different categories like ```World, Sports, Science, Politics etc```

## Run News Scrapper:
- Open config.yml
    - file_name: Define csv filename to strore news data      # eg. news_with_category.csv 
    - url_file_name: Define csv filename to news URL          # eg. url_file.csv 
    - inshort_url: Set inshorts URL                           # https://inshorts.com/en/read

- Run ```pytest test_news_scrapper.py -s --headless```
- CSV file will have following columns
    - [title, content, author, url, category]
- CSV files will be stored inside ```dataset``` folder
