import pandas
import turtle

game_on = True
LIVES = 5
GUESS = 0

data = pandas.read_csv("50_states.csv")
states = data['state'].to_list()

all_states = []
guessed_states = []

for items in states:
    all_states.append(items.lower())

screen = turtle.Screen()
screen.title("U.S. States Quiz")

screen.addshape("blank_states_img.gif")
turtle.shape("blank_states_img.gif")
## Adding an image in turtle

write_turtle = turtle.Turtle()
write_turtle.penup()
write_turtle.hideturtle()


def get_cords(state_name):
    x = int(data[data.state == str(state_name)].x)
    y = int(data[data.state == str(state_name)].y)

    return int(x), int(y)


def send_turtle(x, y, this_turtle):
    current_x = this_turtle.xcor()
    current_y = this_turtle.ycor()

    move_x = x - current_x
    move_y = y - current_y

    this_turtle.setheading(90)

    this_turtle.right(90)
    this_turtle.forward(move_x)
    this_turtle.left(90)
    this_turtle.forward(move_y)


while game_on:
    if len(guessed_states) >= 50:
        game_on = False
    else:

        answer_state = screen.textinput(title=f"{str(GUESS)}/50 states correct | {str(LIVES)} lives remaining",
                                        prompt="Mention a state's name")
        if answer_state:
            if answer_state == "exit":
                game_on = False
            if LIVES > 0:
                if answer_state.lower() in all_states and answer_state.lower() not in guessed_states:
                    guessed_states.append(answer_state.lower())
                    GUESS += 1

                    CAPITALIZE = answer_state.capitalize()

                    if " " in answer_state:
                        first = answer_state.split(" ")[0].capitalize()
                        second = answer_state.split(" ")[1].capitalize()
                        CAPITALIZE = first + " " + second

                    cords = get_cords(CAPITALIZE)

                    send_turtle(cords[0], cords[1], write_turtle)
                    write_turtle.write(CAPITALIZE)

                elif answer_state.lower() in guessed_states:
                    pass

                else:
                    LIVES -= 1
            else:
                game_on = False
                screen.exitonclick()

screen.exitonclick()

GUESS_DICT = {}


def Diff(li1, li2):
    return list(set(li1) - set(li2)) + list(set(li2) - set(li1))


unguessed = Diff(all_states, guessed_states)


capitalized = []

for items in unguessed:
    if " " not in items:
        capitalized.append(items.capitalize())

    else:
        first = items.split(" ")[0].capitalize()
        second = items.split(" ")[1].capitalize()

        capitalized.append(first + " " + second)


capitalized.sort()
GUESS_DICT["States that you left out"] = capitalized

if len(capitalized) != 0:
    data = pandas.DataFrame(GUESS_DICT)
    print("\n---SCORE REPORT---\n")
    data.to_csv("Score Report.csv")
    print(pandas.read_csv("Score Report.csv"))
    print("\n---CHECK OUT 'Score Report.csv' TO GET A CSV FILE REPORT---\n")
else:
    print("Congratulations!! You could remember all the states in the U.S.")
    fs = open("Score Report.csv", "w")
    fs.write("Congratulations!! You could remember all the states in the U.S.")
    fs.close()
