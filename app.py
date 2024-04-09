import streamlit as st
import pandas as pd
import base64

# Function to download data as CSV
def download_data(data):
    csv = data.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()  # Convert to base64 encoding
    href = f'<a href="data:file/csv;base64,{b64}" download="filtered_data.csv">Download as CSV</a>'
    return href

# Main app
def main():
    st.title("Tech Sisters Data Analysis")

    # File uploader for Excel sheet
    uploaded_file = st.file_uploader("Upload Excel file", type=["xlsx", "xls"])

    if uploaded_file is not None:
        # Read Excel file
        try:
            df = pd.read_excel(uploaded_file, sheet_name='All members')
        except Exception as e:
            st.error(f"An error occurred while reading the Excel file: {e}")
            return

        # Set title and logo
        st.title("Tech Sisters")
        #st.image('https://raw.githubusercontent.com/ElizabethWaithera/Tech_sisters/main/Tech%20Sisters.jpg', width=200)  # Using the raw URL of the logo image

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

        # Display filtered data
        st.subheader("Filtered Data:")
        st.write(filtered_df)

        # Display total count for each category
        st.subheader("Total Count for Each Category:")
        if years_experience == "None":
            total_count = filtered_df['Tech Role'].value_counts()
            st.write(total_count)
        else:
            total_count = filtered_df['Years of Experience in Tech (Please select one):'].value_counts()
            st.write(total_count)

        # Download button for filtered data
        st.markdown(download_data(filtered_df), unsafe_allow_html=True)

if __name__ == "__main__":
    main()