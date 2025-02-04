import streamlit as st
from datetime import datetime
import math

# Set title
st.set_page_config(
   page_title='Timestamp',
   page_icon='📚'
)

st.title('📚 Timestamp')

# Initialize session state for logs
if 'logs' not in st.session_state:
    st.session_state.logs = []

# Function to generate grid layout
def create_grid(names, cols=3):
    rows = math.ceil(len(names) / cols)
    grid = []
    for i in range(rows):
        grid.append(names[i*cols:(i+1)*cols])
    return grid

# Stage 1: Input names
if 'stage' not in st.session_state:
    st.session_state.stage = 'input'

if st.session_state.stage == 'input':
    st.subheader("Enter Names")
    names_input = st.text_area("Enter one name per line:", height=200)
    if st.button("Submit"):
        # Split names by line and remove empty lines
        names = [name.strip() for name in names_input.strip().split('\n') if name.strip()]
        if names:
            st.session_state.names = names
            st.session_state.stage = 'buttons'
        else:
            st.warning("Please enter at least one name.")
            
# Stage 2: Display buttons
if st.session_state.get('stage') == 'buttons':
    st.subheader("Press a Name to Log Timestamp")
    cols = 3  # Number of columns in grid
    grid = create_grid(st.session_state.names, cols)
    
    for row in grid:
        cols_widgets = st.columns(cols)
        for idx, name in enumerate(row):
            if cols_widgets[idx].button(name):
                current_time = datetime.now().strftime("%H:%M:%S")
                st.session_state.logs.append(f"{current_time} {name}")
    
    st.markdown("---")
    if st.button("Complete"):
        if st.session_state.logs:
            st.subheader("Logged Entries")
            for log in st.session_state.logs:
                st.text(log)
        else:
            st.info("No entries have been logged.")
            
    st.markdown("---")
    if st.button("Reset"):
        st.session_state.stage = 'input'
        st.session_state.logs = []
