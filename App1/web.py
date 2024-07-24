

import streamlit as st
from functions import get_todos, write_todos

def add_todo():
    todo = st.session_state.new_todo
    if todo:  # Ensure todo is not empty
        todos = get_todos()
        todos.append(todo)
        write_todos(todos)
        st.session_state.new_todo = ""  # Clear the input after adding

def delete_todos(todos_to_delete):
    todos = get_todos()
    # Remove todos that need to be deleted
    todos = [todo for todo in todos if todo not in todos_to_delete]
    write_todos(todos)

# Initialize the list of todos to delete
todos_to_delete = []

st.title('To Do App')
st.subheader("Keep track of your to-dos")
st.write("Click on a to-do to delete it")

todos = get_todos()
if len(todos) == 0:
    st.write("No to-do yet")
else:
    for idx, todo in enumerate(todos):
        # Use a unique key for each checkbox
        key = f"checkbox_{idx}_{todo}"
        checkbox = st.checkbox(todo, key=key)
        if checkbox:
            # Track the todos that need to be deleted
            todos_to_delete.append(todo)
    
    if todos_to_delete:
        delete_todos(todos_to_delete)
        st.experimental_rerun()  # Re-run the script to update the list

st.text_input(label="", placeholder="Enter a to-do ...",
              on_change=add_todo, key="new_todo")

