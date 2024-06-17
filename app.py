import streamlit as st
import os

def app():
    st.title('Menu')
    with st.form("path_form"):
        path_folder = st.text_input('Enter your name')
        if path_folder:
            file_in_folder = os.listdir(path_folder)
            for file in file_in_folder:
                st.write(file)
        if st.form_submit_button(label='Submit'):
            if not path_folder:
                st.warning('Please enter a path')
            if not file_in_folder:
                st.warning('No file in the folder')
            with st.spinner('Wait for it...'):
                # create a new folder
                path_new_folder = os.path.join(path_folder, 'new_folder')
                os.makedirs(path_new_folder, exist_ok=True)
                st.success('Done!')

if __name__ == '__main__':
    app()