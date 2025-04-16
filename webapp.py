import streamlit as st
import functions

todos = functions.read_todos()

def add_todo():
    new_todo = st.session_state["input"] + "\n"
    todos.append(new_todo)
    functions.write_todos(todos)



st.title("Your Todo List App")
st.subheader("Your Todo List:")
st.write("This app should increase your productivity In Sha Allah")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key = todo)
    if checkbox == True:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()
        #Theoretically it should work fine, but it's a bit buggy
        #Slightly buggy

st.text_input(label = "", placeholder="Enter a todo",
              on_change=add_todo, key= "input")
#the "on_change" parameter is for when the Enter key is pressed

st.session_state