"""Movie recommendation based on user's emotion using web scraping tools"""
import re
import requests as HTTP
from bs4 import BeautifulSoup as SOUP

def recommend(emotion):
    if emotion=="Sad":
        urlhere = 'http://www.imdb.com/search/title?genres=drama&title_type=feature&sort=moviemeter, asc'
    elif(emotion == "Disgust"): 
        urlhere = 'http://www.imdb.com/search/title?genres=musical&title_type=feature&sort=moviemeter, asc'
    elif(emotion == "Anger"): 
        urlhere = 'http://www.imdb.com/search/title?genres=family&title_type=feature&sort=moviemeter, asc'
    elif(emotion == "Anticipation"): 
        urlhere = 'http://www.imdb.com/search/title?genres=thriller&title_type=feature&sort=moviemeter, asc'
    elif(emotion == "Fear"): 
        urlhere = 'http://www.imdb.com/search/title?genres=sport&title_type=feature&sort=moviemeter, asc'
    elif(emotion == "Enjoyment"): 
        urlhere = 'http://www.imdb.com/search/title?genres=thriller&title_type=feature&sort=moviemeter, asc'
    elif(emotion == "Trust"): 
        urlhere = 'http://www.imdb.com/search/title?genres=western&title_type=feature&sort=moviemeter, asc'
    elif(emotion == "Surprise"): 
        urlhere = 'http://www.imdb.com/search/title?genres=film_noir&title_type=feature&sort=moviemeter, asc'
    
    ##web scraping to get HTML
    response=HTTP.get(urlhere)
    info=response.text
    soup=SOUP(info,"lxml") ##parsing to form tree
    name=soup.find_all("a",attrs={"href":re.compile(r'\/title\/tt+\d*\/')})
    return name

if __name__=='__main__':
    print("Enter your current mood ---->")
    emotion=input()
    res=recommend(emotion)
    c=0
    for i in res:
        temp=str(i).split('>') ##removing HTML tags 
        if len(temp)==3:
            print(temp[1][:-3])##printing the name of the movie
       if c>11:
           break
       c+=1
    
    