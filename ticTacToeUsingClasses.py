import os
class init:
    arr = [" "," "," "," "," "," "," "," "," "]
    def change(self,pos,player):
        init.arr[pos]=player
    def prnt(self):
        print(f" {init.arr[0]} | {init.arr[1]} | {init.arr[2]}")
        print("-----------")
        print(f" {init.arr[3]} | {init.arr[4]} | {init.arr[5]}")
        print("-----------")
        print(f" {init.arr[6]} | {init.arr[7]} | {init.arr[8]}")

    
        if (init.arr[0] == init.arr[1] and init.arr[1] == init.arr[2]):
            if init.arr[0] != " ":
                print(init.arr[0], 'is won')
        elif (init.arr[3] == init.arr[4] and init.arr[4] == init.arr[5]):
            if init.arr[3] != " ":
                print(init.arr[3], 'is won')
        elif (init.arr[6] == init.arr[7] and init.arr[7] == init.arr[8]):
            if init.arr[6] != " ":
                print(init.arr[6], 'is won')
        elif (init.arr[0] == init.arr[4] and init.arr[4] == init.arr[8]):
            if init.arr[0] != " ":
                print(init.arr[0], 'is won')
        elif (init.arr[6] == init.arr[4] and init.arr[4] == init.arr[2]):
            if init.arr[6] != " ":
                print(init.arr[6], 'is won')
        # else:
        #     print("Draw")

class playerX(init):
    def __init__(self,choice):
        self.choice = choice
        init.change(self,self.choice,'x')


class computer(init):
    def __init__(self):
        
        if init.arr[:3].count('x')>=2  and " " in init.arr[:3]:
            init.arr[init.arr.index(" ",0,3)] = 'o'
        elif init.arr[3:6].count('x')>=2 and " " in init.arr[3:6]:
            init.arr[init.arr.index(" ",3,6)] = 'o'
        elif init.arr[6:9].count('x')>=2 and " " in init.arr[6:9]:
            init.arr[init.arr.index(" ",6,9)] = 'o'
        elif init.arr[0:7:3].count('x')>=2 and " " in init.arr[0:7:3]:
            if init.arr[0] == ' ':
                init.arr[0] = 'o'
            elif init.arr[3] == ' ':
                init.arr[3] = 'o'
            elif init.arr[6] == ' ':
                init.arr[6] = 'o'
        elif init.arr[1:8:3].count('x')>=2 and " " in init.arr[1:8:3]:
            if init.arr[1] == ' ':
                init.arr[1] = 'o'
            elif init.arr[4] == ' ':
                init.arr[4] = 'o'
            elif init.arr[7] == ' ':
                init.arr[7] = 'o'
        elif init.arr[2:9:3].count('x')>=2 and " " in init.arr[2:9:3]:
            if init.arr[2] == ' ':
                init.arr[2] = 'o'
            elif init.arr[5] == ' ':
                init.arr[5] = 'o'
            elif init.arr[8] == ' ':
                init.arr[8] = 'o'
        elif init.arr[4] == ' ':
            init.arr[4] = 'o'
        elif " " not in init.arr:
            print("Draw")
        else:
            init.arr[init.arr.index(" ")]='o'
        
        
I = init()
I.prnt()
while(True):
    ch = int(input("Enter your Choice: "))
    os.system('cls')
    px = playerX(ch)
    com= computer()
    I.prnt()
    



