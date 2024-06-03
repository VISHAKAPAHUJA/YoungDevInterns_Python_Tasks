from pathlib import Path
import streamlit as st
from PIL import Image

# Path settings
current_dir=Path(__file__).parent if  "__file__" in locals() else Path.cwd()
css_file=current_dir /"styles"/"a1.css"
resume_file=current_dir /"assets"/"cv.pdf"
profile_pic=current_dir /"assets"/"profile(1).png"


# General Settings
title="DIGITAL RESUME"
page_icon="random"
name="VISHAKA PAHUJA"
Description="""
As a computer science student, I possess strong analytical and problem-solving skills, with proficiency in
various programming languages. My eagerness to learn and adapt to new technologies makes me valuable
asset to any organization.
"""

st.set_page_config(page_title="Digital Resume", page_icon="📄")


# LOAD CSS,PDF & PROFILE PIC
with open(css_file) as f:
    st.markdown("<style>{}<style".format(f.read()),unsafe_allow_html=True)


with open(resume_file,"rb") as r:
    PDFbyte=r.read()
    profile_pic=Image.open(profile_pic)


 # Hero section
col1, col2 = st.columns([2, 2])  # Adjust the column widths and ratio as needed
with col1:
    st.image(profile_pic, width=320)

with col2:
    st.title(name)
    st.write(Description)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
    )



# Contact Information
st.write("📧 Email: vishakapahuja976@gmail.com")
st.write("🌐 LinkedIn: [Vishaka Pahuja](http://linkedin.com/in/vishakapahuja)")
st.write("💼 GitHub: [Vishaka Pahuja](https://github.com/VISHAKAPAHUJA?tab=repositories)")


# EDUCATION  
st.write('#')
st.header('EDUCATION')
st.write("""
Bachelor Of Science in Computer Science \n
Sukkur IBA University \n
Sukkur, Pakistan \n
11/2021 - Present \n
-----------------------------------------------
Intermediate, Pre-Medicine/Pre-Medical Studies \n
Govt. Girls Higher Secondary School \n
Kandhkot,Pakistan \n
2018 - 2020\n
""") 


# DIGITAL SKILLS
st.write('#')
st.header("DIGITAL SKILLS")
st.write("""
- 💻 DATA STRUCTURES AND ALGORITHMS WITH JAVA
- 📊 Microsoft Office package: Microsoft Word, Excel, PowerPoint, Access
- ☕ Java
- 🌐 Html / CSS / JavaScript
- 🐍 Python
- 📝 Knowledge of SQL
- 🖥️ C++ programming language
- 🌐 Wordpress
- 🐍 Python (Tkinter, Matplotlib, NumPy, Pandas)
- 🐍 Python and Streamlit
         """)

# PROJECTS
projects_with_descriptions = {
    "🍽️ RESTAURANT MANAGEMENT SYSTEM USING JAVA": {
        "description": "A comprehensive system for managing restaurant operations, including orders, inventory, and staff management.",
        "link": "https://github.com/VISHAKAPAHUJA/2ND-SEMESTER-FINAL-PROJECT-BY-VISHAKA-PAHUJA-MUSKAN-NARANG.git"
    },
    "📚 Library Management System Using Cpp": {
        "description": "An efficient system for managing library resources, including books, patrons, and borrowing records.",
        "link": "https://github.com/VISHAKAPAHUJA/LMS_.git"
    },
    "🌦️ Open Weather App Using Python": {
        "description": "An application that retrieves and displays weather information from OpenWeatherMap API based on user input.",
        "link": "https://github.com/VISHAKAPAHUJA/WeatherApp.git"
    },
    "✅ TO DO LIST APPLICATION USING PYTHON": {
        "description": "A simple to-do list application for organizing tasks and tracking completion status.",
        "link": "https://github.com/VISHAKAPAHUJA/ToDoList_App.git"
    },
}

# PROJECTS
st.header("PROJECTS")
for project, data in projects_with_descriptions.items():
    st.write(f"{project}")
    st.write(data["description"])
    st.write(f"[GitHub Repository]({data['link']})")
    st.write("")  # Add an empty line for spacing between projects

# ACHIEVEMENTS
st.write('#')
st.header("ACHIEVEMENTS")
st.write("""
🎓 Merit Based Scholarship 
Currently I am seeking my bachelor degree in computer science at Sukkur IBA University on a merit based scholarship. 

🏆 Winner of Data Pirates competition in Java 
This achievement underscored my unwavering dedication, as well as the persistent hard work I invested in mastering Java. 

🎉 Organizer in Bivenue party event 

📚 CGPA: 3.57 

🚀 Participated in "Code Sprint Competition" at Procom'24 
         """)

