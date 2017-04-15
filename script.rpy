# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.

    "Hello, world."

    e "You've created a new Ren'Py game."

    e "Once you add a story, pictures, and music, you can release it to the world! Once you add a story, pictures, and music, you can release it to the world!"

menu: 
    "yo yo yo":
        jump choice1
    "yo yo yo 2": 
        jump choice2
    "yo yo yo 3":
        jump choice3
    "yo yo yo 4": 
        jump choice4

label choice1:
    ":D"
    
label choice2:
    ":DD"

label choice3:
    ":DDD"
    
label choice4:
    ":DDDD"




    return
