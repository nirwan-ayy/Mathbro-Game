import random

#Defining functions
def cal_answer(n1,n2,ope):
    if ope == '+':
        c_ans = n1 + n2
    elif ope == '-':
        c_ans = n1 - n2
    else :
        c_ans = n1 * n2
    return c_ans

#Run the game on the selected mode
def game(mode,file):
    num1_list=[]
    num2_list=[]
    operator_list=[]
    user_answer_list=[]
    correct_answer_list=[]
    num1=0
    num2=0
    correct_count=0
#Demo mode
    q_count=3
    operators=['+']
    intiger_range=5
#easy mode
    if mode == "-e":
        q_count=5
        operators=['+','-']
        intiger_range=10            
#medium mode
    elif mode == "-m":
        q_count=10
        operators=['+','-']
        intiger_range=10
#hard mode            
    elif mode == "-h":
        q_count=10
        operators=['+','-','*']
        intiger_range=20
#demo mode       
    print("# YOU HAVE TO SOLVE",q_count,"QUESTIONS")
    print()
    for i in range(q_count):
        num1=random.randint(0,intiger_range)
        num2=random.randint(0,intiger_range)
        operator=random.choice(operators)
        question= f"{i+1}) {num1} {operator} {num2} {' = '}"
        answer=int(input(question))
        num1_list.append(num1)
        num2_list.append(num2)
        user_answer_list.append(answer)
        operator_list.append(operator)
        real_ans = cal_answer(num1,num2,operator)
        correct_answer_list.append(real_ans)
        
    print()
    print("<<<RESULTS>>>")
    file.write("RESULT SHEET\n")
    print()
    i=0
    for i in range (q_count):
        if user_answer_list[i] == correct_answer_list[i]:
            correct_count+=1
            print("√) ",num1_list[i],operator_list[i],num2_list[i]," = ",user_answer_list[i])
            symble='\u221a'
            file.write(f"{symble}) {num1_list[i]} {operator_list[i]} {num2_list[i]} = {user_answer_list[i]}\n")
        else:
            print("X) ",num1_list[i],operator_list[i],num2_list[i]," = ",user_answer_list[i],"   correct answer is ",correct_answer_list[i])
            file.write(f"X) {num1_list[i]} {operator_list[i]} {num2_list[i]} = {user_answer_list[i]} correct answer is {correct_answer_list[i]}\n")

    print()
    file.write(f"\nTOTAL QUESTIONS : {q_count}\n")
    print("# CORRECT QUESTIONS : ",correct_count)
    file.write(f"CORRECT QUESTIONS : {correct_count}\n")
    print("# MARKS : ",round(correct_count/q_count*100,2),"%")
    file.write(f"MARKS : {round(correct_count/q_count*100,2)} %\n")

