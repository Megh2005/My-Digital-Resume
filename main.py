from pathlib import Path
import streamlit as st
from PIL import Image

current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "style.css"
resume_file = current_dir / "assets" / "Resume.pdf"
profile_pic = current_dir / "assets" / "profile.png"


PAGE_TITLE = "Digital Resume | Megh Deb"
PAGE_ICON = "🙋‍♂️"
NAME = "Megh Deb"
DESCRIPTION = """
Artificial Intellegence & Machine Learning Expert.
"""
EMAIL = "debmegh2005@gmail.com"
SOCIAL_MEDIA = {
    "LinkedIn" : "https://www.linkedin.com/in/megh-deb-a53461295",
    "GitHub" : "https://github.com/Megh2005",
    "Twitter" : "https://twitter.com/MEGHDEB009",
    "Facebook" : "https://www.facebook.com/profile.php?id=100064490472111",
}
PROJECTS = {
    "🏆 House Price Checker" : "https://github.com/Megh2005/House-Price-Predictor.git",
    "🏆 Air Quality Checker" : "https://github.com/Megh2005/Air-Qualitye-Predict.git",
    "🏆 Snake Game" : "https://github.com/Megh2005/Snake-Game.git",
    "🏆 Basic Weather Website" : "https://github.com/Megh2005/Basic-Weather-Website.git",
    "🏆 AI Based Library Management System" : "https://github.com/Megh2005/AI-LMS.git",
}


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file,"rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


col1 , col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic,width=300)
with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label="📂Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📧",EMAIL)

    st.write("#")
    cols = st.columns(len(SOCIAL_MEDIA))
    for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
        cols[index].write(f"[{platform}]({link})")
    
    st.write("#")
    st.subheader("Education")
    st.write("---")
    st.write(
        """
- 🎓 BTech from HIT, Kolkata
- 👨‍💻 UG Value Course in ML from PW
- 🎒 Higher Secondary from SCCS, Kolkata
- 🚸 Secondary from BRKMAHS, Kolkata
"""
    )
    st.write("#")
    st.subheader("Experties")
    st.write("---")
    st.write(
        """
- ✅ 2 years experience in Machine Learning
- ✅ Strong hands on experience in Python
- ✅ Good understanding of statistical principles
- ✅ Excellent team player and collaborative
"""
    )

    st.write("#")
    st.subheader("Hard Skills")
    st.write("---")
    st.write(
        """
- 👨‍💻 Programming: Python (Scilit-Learn), SQL
- 📊 Data Visualization: PowerBi, Plotly
- 📚 Modeling: Regression, Decision Tree
- 📝 Databases: MySQL, MongoDB
"""
    )

    st.write("#")
    st.subheader("Successfull Projects")
    st.write("---")
    for project, link in PROJECTS.items():
        st.write(f"[{project}]({link})")