def check_ans(ques_num,answer,attemps,player):
    correct_ans = quiz[ques_num]["answer"]
    if correct_ans.lower() == answer.lower():
        print(f"Correct answer! One point added")
        return True
    else:
        print(f"Wrong answer! You have {attemps-1} Attemps left! Please try again!")
        return False
            
print("There are a total of 6 questions, you can skip a question anytime by typing skip")
player = input("Enter 2 player with a space : ")
player_list = player.split(" ")
player_score = dict.fromkeys(player_list,0)
current_player = player_list[0]
for question in quiz:
    print(f"\nIt is {current_player}'s turn")
    attemps = 2
    while attemps>0:
        print(quiz[question]["question"])
        ans = input("Enter answer (If you want to skip, please type skip)")
        if ans=="skip":
            break
    
