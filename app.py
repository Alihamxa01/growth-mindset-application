import streamlit as st
import uuid

if 'tasks' not in st.session_state:
    st.session_state.tasks = []
if 'incompleted_tasks' not in st.session_state:
    st.session_state.incompleted_tasks = []
if 'priority_tasks' not in st.session_state:
    st.session_state.priority_tasks = []

st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "About", "Contact Us"])

if page == "Home":
    st.title("Complete Growth Mindset - To-Do List")

    task_input = st.text_input("Enter a new task:")
    priority = st.selectbox("Select Priority:", ["High", "Medium", "Low"], index=1)
    if st.button("Add Task") and task_input:
        priority_color = "red" if priority == "High" else "orange" if priority == "Medium" else "yellow"
        st.session_state.tasks.append({"id": str(uuid.uuid4()), "task": task_input, "completed": False, "priority": priority, "color": priority_color})

    st.subheader("Your Tasks")
    for index, task in enumerate(st.session_state.tasks):
        col1, col2, col3, col4, col5 = st.columns([0.3, 5.4, 1, 1, 1])
        task_color = "green" if task['completed'] else "white"
        with col1:
            priority_dot = "🔴" if task['priority'] == "High" else "🟠" if task['priority'] == "Medium" else "🟡"
            st.markdown(f"<span style='font-size:20px;'>{priority_dot}</span>", unsafe_allow_html=True)
        with col2:
            st.markdown(f"<span style='color:{task_color}; font-weight:bold;'>{'✔️' if task['completed'] else '❌'} {task['task']}</span>", unsafe_allow_html=True)
        with col3:
            if st.button("✅", key=f"complete_{task['id']}"):
                st.session_state.tasks[index]['completed'] = not task['completed']
                st.rerun()
        with col4:
            if st.button("❌", key=f"delete_{task['id']}"):
                st.session_state.incompleted_tasks.append(task)
                st.session_state.tasks = [t for t in st.session_state.tasks if t['id'] != task['id']]
                st.rerun()

    # Display incompleted tasks
    if st.session_state.incompleted_tasks:
        st.subheader("INCOMPLETED TASKS")
        for task in st.session_state.incompleted_tasks:
            st.markdown(f"<span style='color:red; font-weight:bold;'>❌ {task['task']}</span>", unsafe_allow_html=True)

    if st.button("Clear All"):
        st.session_state.tasks = []
        st.session_state.incompleted_tasks = []
        st.session_state.priority_tasks = []
        st.rerun()
elif page == "About":
    st.title("📌 About the To-Do List Manager")
    
    st.markdown("""
        This **To-Do List application** helps users efficiently manage their daily tasks.  
        It allows you to **add, track, and prioritize** tasks to stay organized.

        ### 🔹 **Key Features:**
        - ✅ **Task Management:** Add, edit, and delete tasks.
        - ✅ **Priority Levels:**
            - 🔴 **High Priority (Red)** – Urgent tasks that need immediate attention.
            - 🟠 **Medium Priority (Orange)** – Important but not urgent tasks.
            - 🟡 **Low Priority (Yellow)** – Tasks that can be done later.
        - ✅ **Task Completion Tracking:** Easily mark tasks as completed.
        - ✅ **User-Friendly Interface:** Simple and intuitive for efficient task handling.

        🚀 Stay productive with this To-Do List app and never miss an important task!
    """, unsafe_allow_html=True)

    st.markdown("---") 
    st.subheader("👨‍💻 About Me")
    st.write("""
        I am **Ali Hamza**, a passionate developer with expertise in building web applications.  
        My focus is on creating **efficient, user-friendly, and visually appealing** projects  
        to help people manage their tasks easily.
        
        📩 Feel free to reach out for collaborations or discussions!
    """)

elif page == "Contact Us":
    st.title("📞 Contact Us")
    st.write("For any queries or support, please email us at **hellohamzaa.01@gmail.com**.")
