
import streamlit as st
import pandas as pd

# Load your data from Excel
excel_file = r"C:\Users\hp\Desktop\Tech Sisters\Copy of TechSisters_revised.xlsx"  # Replace with the path to your Excel file
df = pd.read_excel(excel_file, sheet_name='All members')

# Set title and logo
st.title("Tech Sisters")
st.image(r"C:\Users\hp\Desktop\Tech Sisters\Tech Sisters.jpg", width=200)  # Replace with the path to your logo image file

# Sidebar filters
st.sidebar.title('Filters')
tech_role = st.sidebar.selectbox('Select Tech Role', df['Tech Role'].unique())

# Extract unique years of experience options
years_experience_options = df['Years of Experience in Tech (Please select one):'].unique().tolist()
# Add "None" option
years_experience_options.insert(0, "None")
years_experience = st.sidebar.selectbox('Select Years of Experience', years_experience_options)

# Filter data based on selected filters
if years_experience == "None":
    filtered_df = df[df['Tech Role'] == tech_role]
else:
    filtered_df = df[(df['Tech Role'] == tech_role) & (df['Years of Experience in Tech (Please select one):'] == years_experience)]

# Display filtered data in a table
st.write(filtered_df)

# Display total count for each category
st.write("Total Count for Each Category:")
if years_experience == "None":
    total_count = filtered_df['Tech Role'].value_counts()
    st.write(total_count)
else:
    total_count = filtered_df['Years of Experience in Tech (Please select one):'].value_counts()
    st.write(total_count)