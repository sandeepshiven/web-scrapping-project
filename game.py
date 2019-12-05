from bs4 import BeautifulSoup
import requests
import csv
from random import choice

def start():
    play_again = 'y'
    with open('quote_data.csv','r') as file:
        csv_reader = list(csv.DictReader(file))
        while play_again is 'y':
            
            item = choice(list(csv_reader))
            response = requests.get(item["author_link"])
            game_board(item,response.text)
            play_again = playing_status()

def game_board(item , response):
    print("Who said this quote?","\n",item["QUOTE"])
    gueses = 3
    hints = get_hints(response)
    ans = input(f"[gueses remaining:{gueses}] Answer: ")
   # print(item["AUTHOR"])
    while(gueses):
        if ans == str(item["AUTHOR"]):
            print("Your answer is correct!!!!")
            break
        else:
            
            print("Incorrect answer: Here's a hint:",hints.pop())
            ans = input(f"[gueses remaining:{gueses}] Answer: ")
            gueses -= 1

    if ans == str(item["AUTHOR"]):
        print("Your answer is correct!!!!")

    if gueses is 0:
        print("You lose!! The correct answer is:",item["AUTHOR"])


def get_hints(response):
    soup = BeautifulSoup(response, "html.parser")
   # print(soup.find(class_="author-born-date").get_text())
    hint1 = "Author was born in "+soup.find(class_="author-born-date").get_text()+" "+ soup.find(class_="author-born-location").get_text()
    hint_2_3 = soup.find(class_ ="author-title").get_text().split()
    hint2 = "Author's first name starts with:"+hint_2_3[0][0]
    hint3 = "Author's last name starts with:"+hint_2_3[-1][0]
    return [hint3,hint2,hint1]


def playing_status():
    play = input("Do you wanna play again?(y/n): ")
    if(play=='y'):
        print("Here we go again!!")
        return play
    else:
        print("Thanks for playing")
        return play


if __name__ == "__main__":
    start()









