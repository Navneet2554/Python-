import random
user_action=input("Enter a choice(rock,paper,scissor):")
possible_action=["rock","paper","scissor"]
computer_action=random.choice(possible_action)
print("\n You choice{user_action},computer chose{computer_action}\n")
if user_action == computer_action:
    print("both players selected{user_actions}.Its's a tie!")
elif user_action =="rock":
    if computer_action == "scissor":
        print("Rock smahes scissor !You win!")
    else:
        print("Paper covers rock!You lose")
elif user_action =="paper":
    if computer_action=="rock":
        print("Paper covers rock!you win!")
    else:
        print("Scissor cuts paper!you lose")
elif user_action == "Scissor":
    if computer_action == "paper":
        print("Scissor cuts paper!You win!")
    else:
        print("rock smahes scissor!You lose")