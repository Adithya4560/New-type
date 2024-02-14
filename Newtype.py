game = [0,1,2]

def mygame(game):
    print('Here is the list:')
    print(game)
    
def pos():
    
    choice = 'wrong'
    
    while choice not in ['0','1','2']:
        
        choice = input('Pick up the number (0,1,2)')
        
        if choice not in ['0','1','2']:
            print('sorry invalid number')
            
    return int(choice)

def replace(game,position):
    user = input("Type the string to place:")
    game[position] = user
    return game

def poscon():
    
    choice = 'wrong'
    
    while choice not in ['Y','N']:
        
        choice = input('Do you want to continue [Y/N]:')
        
        if choice not in ['Y','N']:
            print('Sorry I cant understand')
            
    if choice == 'Y':
        return True
    else:
        return False
    
game = [0,1,2]
game_con = True

while game_con:
    mygame(game)
    
    position = pos()
    
    game = replace(game,position)
    
    mygame(game)
    
    game_con = poscon()
    
