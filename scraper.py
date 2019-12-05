from bs4 import BeautifulSoup
import requests
import csv

url = "http://quotes.toscrape.com/page/"
page_no = 1
with open("quote_data.csv","w") as file:
    csv_writer = csv.writer(file)
    csv_writer.writerow(["QUOTE","AUTHOR",'author_link'])
    while(True):
        response = requests.get(url+str(page_no))
        print("Scrapping data from:",url+str(page_no),"........")

        soup = BeautifulSoup(response.text, "html.parser")
        quotes = soup.find_all(class_="quote")
        for quote in quotes:
            q_text = quote.find(class_ = "text").get_text() # quote text 
            author,author_link = quote.find(class_ = "author").get_text(),quote.find('a')['href']
            csv_writer.writerow([q_text,author,"http://quotes.toscrape.com"+author_link])
        if(soup.find(class_ = 'next')==None):
            break;
        page_no += 1












