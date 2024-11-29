import random
import sys
from datetime import datetime
import MYGAMEFUNCTION

#Main programme

print()
print()
print("*****  WELCOME TO MATH - BRO GAME  *****")
mode="Demo"
arg = ""
if len(sys.argv) > 1:
    arg = sys.argv[1].lower()

if arg == "-e":
    mode = "Easy"
elif arg == "-m":
    mode = "Medium"
elif arg == "-h":
    mode = "Hard"
print()
print("# GAME MODE = ",mode)

timestamp = datetime.now()
filename = f"{timestamp.strftime('%Y%m%d_%H%M')}_{random.randint(100, 999)}.txt"
file=open(filename,"w",encoding='utf-8')
file.write(f"DATE : {timestamp.strftime('%Y-%m-%d')}\n")
file.write(f"TIME : {timestamp.strftime('%H:%M')}\n\n")
# file.close()

session=0
while(True):
    session+=1
    file.write(f"SESSION : {session}\n")
    print("# SESSION : ",session)
    MYGAMEFUNCTION.game(arg,file)
    file.write(f"MODE : {mode}\n\n")
    print()
    choice=input("# DO YOU WANT TO PLAY AGAIN ? (Y/N) " )
    print()
    while(True):
        if choice in ['y','Y','n','N']:
            break
        else:
            print('INCORRECT INPUT')
            print()
            choice=input("# DO YOU WANT TO PLAY AGAIN ? (Y/N) " )

    if choice.lower() == "n":
        break 
file.close()