import random
a=['rock','paper','scissor']
''''
rock vs paper -> paper wins
rock vs scissor -> rock wins
scissor vs paper -> scissor wins
'''

while True:
    b=int(input('''
    1 yes
    2 no / exit
    '''))
    if b==1:
        for c in range (1,6):
            userinput=int(input('''
            1 rock 
            2 paper 
            3 scissor
            '''))
            if userinput==1:
                uc='rock'
            elif userinput==2:
                uc='paper'
            elif userinput==3:
                uc='scissor'
            choice=random.choice(a)
            print('computer :-',choice)
            print('user:-',uc)
    else:
       break





