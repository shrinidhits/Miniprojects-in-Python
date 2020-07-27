#Probabilistic analysis of winning a tennis match vs winning a point in tennis

"""Suppose in every point of a match you 
had a 50% probability of winning every point. 
If you played thousands of such matches you would expect to win as many games, sets, 
and matches as you lose. Furthermore, you expect that much more of the time the 
scores will be close, like 6-4 rather than 6-0. 
What are the scores like and how often do you win for other probabilities 
of winning each point? The following graphs show the results for relevant probabilities. 
For example, if your probability of winning each point were 70%, your 
probability of winning a game is 91%, you virtually never lose a set, 
and 60% of the time you win a set at 6-0."""

import random
from matplotlib import pyplot as plt
prob = [0.01*i for i in range(1,100,4)]
win=[] #list containing winners of each match
win1=[] #list for appending winners by counting number of sets won
win60=[]  #list to know how many matches were won by 6-0
win61=[]  #list to know how many matches were won by 6-1
win62=[]  #list to know how many matches were won by 6-2
win63=[]  #list to know how many matches were won by 6-3
win64=[]  #list to know how many matches were won by 6-4
win75=[]  #list to know how many matches were won by 7-5
win76=[]  #list to know how many matches were won by 7-6
for x in range(len(prob)):
    win=[]
    win60t=0 #taking count of each win by 6-0
    win61t=0  #taking count of each win by 6-1
    win62t=0  #taking count of each win by 6-2
    win63t=0  #taking count of each win by 6-3
    win64t=0  #taking count of each win by 6-4
    win75t=0  #taking count of each win by 7-5
    win76t=0  #taking count of each win by 7-6
    for i in range(0, 10000):
#Adjust range limits for the desired number of sets played, we consider a match won by best of three here
        game, A, B, = 3, 0, 0
#A set begins with the usual scoring for a game and zero games for the players
        while True:
            a, b = 0, 0
#Start game with zero points for each player
            while True:
                if(random.random() < prob[x]):
                    a = a + 1
                else:
                    b = b + 1
                if(a > game and a - b >= 2):
                    A = A + 1
                    break
                if(b > game and b - a >= 2):
                    B = B + 1
                    break
#This logic handles games that do or do not reach deuce as well as tiebreakers
#           print a, b, A, B
            if((A > 5 and A - B >= 2) or (B > 5 and B-A >= 2)):
#A set is won by "First to six, leading by at least 2"
        	    break
            if((A == 7 and B == 6) or (B == 7 and A == 6)):
        	    break
            if(A == 6 and B == 6):
                game = 6
#At 6 games all, a tiebreak game is to be played, and minimum score to
#win the "tiebreak game" becomes 7.
            else:
                continue
        if A==6 and B==0:
            win60t+=1
            win.append(1)
        elif A==6 and B==1:
            win61t+=1
            win.append(1)
        elif A==6 and B==2:
            win62t+=1
            win.append(1)
        elif A==6 and B==3:
            win63t+=1
            win.append(1)
        elif A==6 and B==4:
            win64t+=1
            win.append(1)
        elif A==7 and B==5:
            win75t+=1
            win.append(1)
        elif A==7 and B==6:
            win76t+=1
            win.append(1)
    
        else:
            win.append(2)
    win60.append(win60t/10000) #appending probabilities
    win61.append(win61t/10000)
    win62.append(win62t/10000)
    win63.append(win63t/10000)
    win64.append(win64t/10000)
    win75.append(win75t/10000)
    win76.append(win76t/10000)
    win1.append(win.count(1)/10000)



#plotting graphs
g=['6-0','6-1','6-2','6-3','6-4','7-5','7-6']
fig = plt.figure()
ax = fig.add_axes([0.1, 0.1, 0.6, 0.75])
for i in range(12,20):
    f=[win60[i],win61[i],win62[i],win63[i],win64[i],win75[i],win76[i]]
    
    ax.plot(g,f, marker='o', label="Probability of winning a point= "+str(prob[i]))
    ax.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)
plt.title("Probability of winning a game in 6-0, 6-1 etc.,. given probability of winning each point")    
plt.show()

plt.plot(prob,win1)
plt.title("Probability of winning a match against probability of winning a point")
plt.xlabel("Probability of winning a point")
plt.ylabel("Probability of winning a match")
plt.show()

