from colorama import Fore, Style, Back
for i in range(1,10):
    for j in range(1,10):
        print(i * j, end=' ') # if you don't put end it will print one by one in each line 
    print() # line changes every turn 

for i in range(1,10):
    for j in range(1,10):
        print(f'{i * j:2d}', end=' ') # line up each column 
    print() 

print('**********************************')

def my99():
    print(Back.WHITE, end ='')
    print('   ',end='')
    for i in range(1, 10):
        print(f'{i:2d}', end = ' ')
    print()
    print('  +', end='')
    for i in range(1,10):
        print('---', end = '')
    print()
    for i in range(1,10):
        print('\033[39m', end = '')
        print(i, '|', end='')
        for j in range(1,10):
            mult = i * j
            #print(f'{i * j:2d}', end=' ')
            if (mult % 2) == 0:
                print(Back.RED + Fore.WHITE + f'{mult:2d}', end=' ')
                print(Back.WHITE, end = '')
            elif (mult % 5) == 0:
                print(Fore.BLUE + f'{mult:2d}', end=' ')
            elif (mult) % 3 == 0:
                print(Fore.GREEN + f'{mult:2d}', end=' ')
            else:
              print('\033[39m' + f'{mult:2d}', end=' ')  
        print()
    print('\033[39m', end = '')

my99()
print('complete!!')

        
