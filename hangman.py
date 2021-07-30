
import random 


class Player:
    def __init__(self):
        self.geusses = []
        
    def get_move(self):

        try:
          mode = input('Geuss a letter or the word (1 for letter, 2 for word: ')
          mode = int(mode)
        except ValueError:
          modes = ['1','2']
          while mode not in modes:
            mode = input('Please select a valid mode: ')
          mode = int(mode) 
            
          
        if mode == 1:
          l = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
          letters = list(l)
          letter = input('Input a letter: ')
          while letter not in letters or letter in self.geusses:
              letter = input('Invalid input please try again: ')
          self.geusses.append(letter)
          print(f'Your guesses so far are {self.geusses} ')
          return letter
      
        if mode == 2:
          l = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
          letters = list(l)
          word = input('Enter a word: ')
          for i in range(len(word)):
              while word[i] not in letters or word in self.geusses:
                  word = input('Invalid input please try again: ')
          self.geusses.append(word)
          print(f'Your guesses so far are {self.geusses} ')
          return word
 

class PhraseBook:
    
    def __init__(self):
        pass 
    def generate_phrase(self):
        phrases = ['Pig','Bear','Wolf','Animal','Puzzles','Book','Loo']
        phrase = random.choice(phrases)
        return phrase 




class Hangman:
    
    def __init__(self,phrase):
        self.phrase = phrase 
        self.board = ['_' for _ in range(len(self.phrase))]
        self.fail = 0
        
    def print_board(self):
        print(self.board)
        self.man = '-----'
        print(self.man)
    
    def empty_spaces(self):
        for i in range(len(self.phrase)):
            if self.board[i] == '_':
                return True
        return False
    
    def geuss_limit(self,limit=10):
        if limit > 0:
            limit-=1
            return True
        return False
    
    def make_move(self,letter):
        
        if len(letter) == 1:
            if str(letter) in str(self.phrase):
                place = [i for i, x in enumerate(list(self.phrase)) if x == letter]
                for i in range(len(place)):
                   self.board[(place[i])] = letter 
            else:
               print("Good try but geuss again: ")
               self.fail += 1
            return self.fail
     
        if len(letter) > 1:
            if str(letter) == str(self.phrase):
                for i in range(len(self.phrase)):
                    self.board[i] = letter[i]
            else:
                print("Good try but geuss again: ")
                self.fail += 1
            return self.fail
     
    def print_hangman(self,fail):
        if fail == 0:
            pass 
        if fail == 1:
            print('''
                  _______
                  |      |
                  O      |
                         |
                         |
                 ________|___''')
        if fail == 2:
            print('''
                  _______
                  |      |
                  O      |
                  |      |
                         |
                 ________|___''')
        if fail == 3:
            print('''
                  _______
                  |      |
                  O      |
                  |/     |
                         |
                 ________|___'''
                    )
        if fail == 4:
            print('''
                  _______
                  |      |
                  O      |
                 \\|/     |
                         |
                 ________|___''')
        if fail == 5:
            print('''
                  _______
                  |      |
                  O      |
                 \\|/     |
                   \\    |
                 ________|___''')
        if fail == 6:
            print('''
                  _______
                  |      |
                  O      |
                 \\|/     |
                 / \\     |
                 ________|___''')
            print(f'The phrase was {self.phrase}')
   
   
player = Player()
p = PhraseBook()
phrase = p.generate_phrase() 
h = Hangman(phrase)    
        

result = 0
fail = 0
 
while h.empty_spaces() and result < 6:
    # validation check 
    h.print_board()
    letter = player.get_move()
    result = h.make_move(letter)
    h.print_hangman(result)
    if  not h.empty_spaces():
        print('You win')
    if result == 6:
        print('You lose')
        
        
  