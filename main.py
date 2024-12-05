import pandas as pd
import turtle

screen = turtle.Screen()
screen.title("Indian States")
image = "india.gif"
screen.addshape(image)
turtle.shape(image)

one_option = (screen.textinput(title="Choose One option !!",prompt="State or Union Territory ?")).title()
data = pd.read_csv("india_states.csv") #it will read the data
all_states = data["state"].to_list()  #converting the data of state to the list
guessed_state = []


if one_option == "State":
#for State
    while len(guessed_state) < 28:
        answer_states = (screen.textinput(title=f"{len(guessed_state)}/28 Correct States", prompt="Give a state !!")).title()
        if answer_states == "Exit":
            break
        if answer_states in all_states:
            t = turtle.Turtle()
            t.hideturtle()
            t.penup()
            state_data = data[data.state == answer_states]
            t.goto(state_data.x.item(), state_data.y.item())
            t.write(answer_states)
            guessed_state.append(answer_states)

#For Union Territory
elif one_option == "Union Territory":
    while len(guessed_state) < 8:
        answer_states = (screen.textinput(title=f"{len(guessed_state)}/8 Correct Union Territory", prompt="Give a Territory !!")).title()
        if answer_states == "Exit":
            break
        if answer_states in all_states:
            t = turtle.Turtle()
            t.hideturtle()
            t.penup()
            state_data = data[data.state == answer_states]
            t.goto(state_data.x.item(), state_data.y.item())
            t.write(answer_states)
            guessed_state.append(answer_states)
else:
    print("Message not recognised")

# def mouse_click(x,y):
#     print(x,y)
# turtle.onscreenclick(mouse_click)
# turtle.mainloop()

screen.exitonclick()









