import turtle as t
import pandas

screen = t.Screen()
screen.title("U.S. States Game")
image = "./U.S_States_Game/blank_states_img.gif"
screen.addshape(image)
t.shape(image)
pencil = t.Turtle()
pencil.ht()
pencil.penup()
pencil.speed("slow")
data = pandas.read_csv("./U.S_States_Game/50_states.csv")
state_list = data["state"].to_list()

state_count = []
while len(state_count) < 50:
    answer_state = screen.textinput(title=f"{len(state_count)}/50 States Correct", prompt="What's the name of a state?")
    if answer_state == "Exit":
        missing_states = []
        for state in state_list:
            if state not in state_count:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("./U.S_States_Game/new_data.csv")
        break
    if answer_state in state_list and answer_state not in state_count:
        state_count.append(answer_state)
        state_str = answer_state
        state_row = data[data["state"] == answer_state]
        x = state_row.x.item()
        y = state_row.y.item()
        pencil.goto(x, y)
        pencil.write(state_str, align="center", font=("Courier", 10, "bold"))

