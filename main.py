import streamlit as st
import functions

# Initialize todos
todos = functions.get_todos()

st.title('My To-Do App')
st.subheader('This is my tasks')

# Track which todos to remove
todos_to_remove = []

# Show existing todos
for index, todo in enumerate(todos):
    stripped_todo = todo.strip()
    if stripped_todo:  # Only show non-empty todos
        checkbox = st.checkbox(stripped_todo, key=f"todo_{index}")
        if checkbox:
            todos_to_remove.append(index)

# Remove completed todos (iterate in reverse to maintain correct indices)
if todos_to_remove:
    for index in reversed(todos_to_remove):
        todos.pop(index)
    functions.write_todos(todos)
    st.rerun()

# Add new todo
with st.form('add_todo_form', clear_on_submit=True):
    new_todo = st.text_input("Add new Todo...")
    submitted = st.form_submit_button('Add')
    
    if submitted and new_todo.strip():
        cleaned_todo = new_todo.strip()
        # Check if todo already exists (compare cleaned versions)
        existing_todos = [todo.strip() for todo in todos]
        
        if cleaned_todo not in existing_todos:
            todos.append(cleaned_todo + "\n")
            functions.write_todos(todos)
            st.rerun()
        else:
            st.warning("This todo already exists!")