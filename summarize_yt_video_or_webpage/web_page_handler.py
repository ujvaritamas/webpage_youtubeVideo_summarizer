import bs4 as bs
import urllib.request as url
from string import punctuation      #!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
import nltk
nltk.download('punkt')
nltk.download('stopwords')

import summary


page = 'https://www.york.ac.uk/teaching/cws/wws/webpage1'

#scraped_data = url.urlopen('https://en.wikipedia.org/wiki/Natural_language_processing')

#screp pragraphs from the page
request_site = url.Request(page, headers={"User-Agent": "Mozilla/5.0"})
article = url.urlopen(request_site).read().decode('utf8')
soup = bs.BeautifulSoup(article, 'html.parser')
paragraphs = soup.find_all('p')
article_text = ""
for p in paragraphs:
    article_text += p.text

print("Original text: \n")
print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\n")
print(article_text)
print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\n")

#create summary
summary_obj = summary.Summarizer(article_text)
summary_obj.print_summary()