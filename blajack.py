import random
import speech_recognition as sr
from gtts import gTTS
import os
import requests
import webbrowser

class Card(object):
    RANKS = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13)
    SUITS = ('Spades', 'Diamonds', 'Hearts', 'Clubs')
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
    def __str__(self):
        if self.rank == 1:
            rank = 'Ace'
        elif self.rank == 11:
            rank = 'Jack'
        elif self.rank == 12:
            rank = 'Queen'
        elif self.rank == 13:
            rank = 'King'

        else:
            rank = self.rank
        return str(rank) + ' of ' + self.suit.lower()
        
class Deck(object):
    def __init__(self):
        self._cards = []
        for suit in Card.SUITS:
            for rank in Card.RANKS:
                c = Card(rank, suit)
                self._cards.append(c)
    def shuffle(self):
        random.shuffle(self._cards)
    def deal(self):
        if len(self) == 0:
           return None
        else:
           return self._cards.pop(0)
    def __len__(self):
        return len(self._cards)
    def __str__(self): 
         result = ''
         for c in self._cards:
             result = result + str(c) + '\n'
         return result


class Player(object):
    def __init__(self, cards):
        self._cards = cards
        self.pts=''
    def __str__(self):
        result = " ".join(map(str, self._cards))
        result+= "  you have " + str(self.getPoints()) + " points"
        return result
    def getPoints(self):
        count = 0
        for card in self._cards:
            if card.rank > 9:
                count += 10
            elif card.rank == 1:
                count += 11
            else:
                count += card.rank
        # Deduct 10 if Ace is available and needed as 1
        for card in self._cards:
            if count <= 21:
                break
            elif card.rank == 1:
                count -= 10
        return count
    def hit(self, card):
        self._cards.append(card)
        if self.getPoints() > 21:
           print ("You bust and lose")
           out=gTTS(text="You bust and lose",lang='en-us')
           out.save("hang.mp3")
           os.system("mpg321 hang.mp3")
    def hasBlackjack(self):
        return len(self._cards) == 2 and self.getPoints() == 21 




class Dealer(Player):
    def __init__(self, cards):
        Player.__init__(self, cards)
        self._showOneCard = True
    def __str__(self):
        if self._showOneCard:
            return str(self._cards[0])
        else:
            return Player.__str__(self)
    def _getPoints(self):
        count = 0
        for card in self._cards:
            if card.rank > 9:
                count += 10
            elif card.rank == 1:
                count += 11
            else:
                count += card.rank
        # Deduct 10 if Ace is available and needed as 1
        for card in self._cards:
            if count <= 21:
                break
            elif card.rank == 1:
                count -= 10
        return count
    def hit(self, deck):
        self._showOneCard = False
        while self._getPoints() < 17:
            self._cards.append(deck.deal())


class Blackjack(object):
    def __init__(self):
        self._deck = Deck()
        self._deck.shuffle()
        # Pass the player and the dealer two cards each
        self._player = Player([self._deck.deal(),self._deck.deal()])
        self._dealer = Dealer([self._deck.deal(),self._deck.deal()])
    def play(self):
        print ("Player:\n",self._player)
        out = gTTS(text="you have "+str(self._player), lang='en-us')
        out.save("hang.mp3")
        os.system("mpg321 hang.mp3")
        #print (str(self._player.pts))
        print ("Dealer:\n",self._dealer)
        out = gTTS(text="dealer has "+str(self._dealer), lang='en-us')
        out.save("hang.mp3")
        os.system("mpg321 hang.mp3")

        # print (str(self._dealer.pts))
        # Player hits until user says NO
        while True:
            out = gTTS(text='do you want to hit?', lang='en-us')
            out.save("hang.mp3")
            os.system("mpg321 hang.mp3")
            r = sr.Recognizer()
            with sr.Microphone() as source:
                print("Say something!")
                audio = r.listen(source)
                res = r.recognize_google(audio)
                print("You said: " + res)

            #choice = input("Do you want a hit? [y/n]: ")
            if res=="no":
                choice='n'
            else:
                choice='y'
            if choice in ("Y", "y"):
                self._player.hit(self._deck.deal())
                points = self._player.getPoints()
                print ("Player:\n", self._player)
                out = gTTS(text="now you have " + str(self._player), lang='en-us')
                out.save("hang.mp3")
                os.system("mpg321 hang.mp3")
                if points >= 21:
                    break
            else:
                break
        playerPoints = self._player.getPoints()
        if playerPoints > 21:
            print ("You bust and lose")
            out=gTTS(text="You bust and lose",lang='en-us')
            out.save("hang.mp3")
            os.system("mpg321 hang.mp3")
        else:
            # Dealer's turn to hit
            self._dealer.hit(self._deck)
            print ("Dealer:\n", self._dealer)
            dealerPoints = self._dealer.getPoints()
        
            # Determine the outcome
            if dealerPoints > 21:
                print ("Dealer busts and you win")
                out=gTTS(text="Dealer busts and you win",lang='en-us')
                out.save("hang.mp3")
                os.system("mpg321 hang.mp3")
            elif dealerPoints > playerPoints:
                print ("Dealer wins")
                out=gTTS(text="Dealer wins",lang='en-us')
                out.save("hang.mp3")
                os.system("mpg321 hang.mp3")
            elif dealerPoints < playerPoints and playerPoints <= 21:
                print ("You win")
                out=gTTS(text="You win",lang='en-us')
                out.save("hang.mp3")
                os.system("mpg321 hang.mp3")
            elif dealerPoints == playerPoints:
                if self._player.hasBlackjack() and not self._dealer.hasBlackjack():
                   print ("You win")
                   out=gTTS(text="You win",lang='en-us')
                   out.save("hang.mp3")
                   os.system("mpg321 hang.mp3")
                elif not self._player.hasBlackjack() and self._dealer.hasBlackjack():
                   print ("Dealer wins")

                   out=gTTS(text="Dealer wins",lang='en-us')
                   out.save("hang.mp3")
                   os.system("mpg321 hang.mp3")
                else:
                   print ("There is a tie")
                   out=gTTS(text="There is a tie",lang='en-us')
                   out.save("hang.mp3")
                   os.system("mpg321 hang.mp3")

        print("you had "+str(self._player.getPoints())+"points")
        g="you had "+str(self._player.getPoints())+"points"
        out = gTTS(text=g, lang='en-us')
        out.save("hang.mp3")
        os.system("mpg321 hang.mp3")
        print("dealer had "+str(self._player.getPoints())+" points")
        h="dealer had "+str(self._dealer.getPoints())+" points"
        out = gTTS(text=h, lang='en-us')
        out.save("hang.mp3")
        os.system("mpg321 hang.mp3")

game=Blackjack()
game.play()
