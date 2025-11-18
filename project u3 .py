print("""
░██╗░░░░░░░██╗███████╗██╗░░░░░░█████╗░░█████╗░███╗░░░███╗
░██║░░██╗░░██║██╔════╝██║░░░░░██╔══██╗██╔══██╗████╗░████║
░╚██╗████╗██╔╝█████╗░░██║░░░░░██║░░╚═╝██║░░██║██╔████╔██║
░░████╔═████║░██╔══╝░░██║░░░░░██║░░██╗██║░░██║██║╚██╔╝██║
░░╚██╔╝░╚██╔╝░███████╗███████╗╚█████╔╝╚█████╔╝██║░╚═╝░██║
░░░╚═╝░░░╚═╝░░╚══════╝╚══════╝░╚════╝░░╚════╝░╚═╝░░░░░╚═╝
""")
print("Welcom to my island !")
door=input("""
There are 3 doors in fornt of you. A🚪red door and ,🚪Blue door and,🚪Yellow door
Which door do you want to open ?
""").lower()
if door == "red":
    print("Great! now you entered the room")
    boxes= input("You found three boxes: 🎁 White box, 🎁Black box,🎁Green box\n").lower()
    if boxes == "green":
        print("Congratulations! You found the treasure! 🏆")
    elif boxes == "white":
        print("Sorry, The box is empty. Game over! 💀")
    elif boxes == "black":
        print("Oops! This box is full of snakes! Game over! 🐍💀")
    else:
        print("Invalid choice! Game over! 💀")
elif door == "blue":
    print("Oh no! You entered a room full of sharks! Game over! 🦈💀")
elif door == "yellow":
    print("Oh no! You entered the room empty! Game over! 💀")
else:
    print("Invalid choice!, Game over! 💀")