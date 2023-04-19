import turtle
import pandas as pd


screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


# answer_state = screen.textinput(title="Guess the state:", prompt="What's another state's name?").title()
data = pd.read_csv("50_states.csv")
all_states = data['state'].to_list()
guessed_states = []

game_is_on = True
while game_is_on:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                    prompt="Enter the state name:").title()

    if answer_state == 'Exit':
        missing_states = [state for state in all_states if state not in guessed_states]
        new_data = pd.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in all_states:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)
        if answer_state not in guessed_states:
            guessed_states.append(answer_state)

        if len(guessed_states) == 50:
            t.color("red")
            t.goto(0, 0)
            t.write("Congrats, you've guessed all the states!",align='center',font=('Arial', 20, 'bold'))
            game_is_on = False

# screen.exitonclick()
