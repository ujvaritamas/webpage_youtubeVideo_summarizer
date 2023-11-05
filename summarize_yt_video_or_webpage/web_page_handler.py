import bs4 as bs
import urllib.request as url
from string import punctuation      #!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
import nltk
nltk.download('punkt')
nltk.download('stopwords')


page = 'https://www.york.ac.uk/teaching/cws/wws/webpage1'

#scraped_data = url.urlopen('https://en.wikipedia.org/wiki/Natural_language_processing')

#screp pragraphs from the page
request_site = url.Request(page, headers={"User-Agent": "Mozilla/5.0"})
article = url.urlopen(request_site).read()
parsed_article = bs.BeautifulSoup(article, 'html.parser')
paragraphs = parsed_article.find_all('p')

article_text = ""

for p in paragraphs:
    article_text += p.text


import summary

summary_obj = summary.Summarizer(article_text)
summary_obj.print_summary()