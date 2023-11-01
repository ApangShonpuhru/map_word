import turtle
import pandas

screen = turtle.Screen()
screen.title("Indian States Guessing game")
image = "india_map.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("India States.csv")
all_states = data.state.to_list()

guess_states = []

while len(guess_states) < 29:

    answer_state = screen.textinput(title= f"{len(guess_states)}/29 States Correct",
                                    prompt= "What's another State name.? \nType Exit to Exit the game").title()
    # print(answer_state)
    if answer_state == "Exit":
        missing_state = []
        for state in all_states:
            if state not in guess_states:
                missing_state.append(state)
        new_data = pandas.DataFrame(missing_state)
        new_data.to_csv("Missing States Name.csv")
        break
    if answer_state in all_states:
        guess_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(state_data.iloc[0, 1], state_data.iloc[0, 2])
        t.write(answer_state)


