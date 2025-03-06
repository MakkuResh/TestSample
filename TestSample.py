import streamlit as st
import pandas as pd
import plotly.express as px

# Load Data
file_path = "university_student_dashboard_data.csv"
df = pd.read_csv(file_path)

# Set page config for a better layout
st.set_page_config(page_title="University Dashboard", layout="wide")

# Title with a colored background
st.markdown("""
    <style>
    .title {
        text-align: center;
        font-size: 36px;
        color: white;
        background-color: #4CAF50;
        padding: 10px;
        border-radius: 10px;
    }
    </style>
    <div class='title'>University Admissions & Student Satisfaction Dashboard</div>
""", unsafe_allow_html=True)

# KPI Metrics with colorful cards
st.subheader("📊 Key Metrics")
col1, col2, col3 = st.columns(3)
col1.metric("Total Applications", df['Applications'].sum(), "📌")
col2.metric("Total Admitted", df['Admitted'].sum(), "✅")
col3.metric("Total Enrolled", df['Enrolled'].sum(), "🎓")

# Retention Rate Trends
st.subheader("📈 Retention Rate Trends")
grouped_year = df.groupby("Year")["Retention Rate (%)"].mean().reset_index()
fig_retention = px.line(grouped_year, x="Year", y="Retention Rate (%)", 
                         title="Retention Rate Over Time", markers=True, 
                         color_discrete_sequence=["#FF5733"])
st.plotly_chart(fig_retention, use_container_width=True)

# Satisfaction Trends
st.subheader("😊 Student Satisfaction Trends")
fig_satisfaction = px.line(df, x="Year", y="Student Satisfaction (%)", color="Term", 
                           title="Student Satisfaction Over Time", markers=True, 
                           color_discrete_map={"Spring": "#FFA07A", "Fall": "#20B2AA"})
st.plotly_chart(fig_satisfaction, use_container_width=True)

# Enrollment Breakdown by Department
st.subheader("🎓 Enrollment Breakdown by Department")
department_cols = ["Engineering Enrolled", "Business Enrolled", "Arts Enrolled", "Science Enrolled"]
department_data = df.melt(id_vars=["Year", "Term"], value_vars=department_cols, var_name="Department", value_name="Enrollment")
fig_enrollment = px.bar(department_data, x="Year", y="Enrollment", color="Department", 
                         barmode="group", title="Enrollment by Department", 
                         color_discrete_sequence=["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728"])
st.plotly_chart(fig_enrollment, use_container_width=True)

# Spring vs Fall Comparison
st.subheader("🔄 Spring vs Fall Enrollment Comparison")
fig_term_comparison = px.bar(df, x="Year", y="Enrolled", color="Term", 
                             barmode="group", title="Enrollment Trends: Spring vs Fall", 
                             color_discrete_map={"Spring": "#17BECF", "Fall": "#9467BD"})
st.plotly_chart(fig_term_comparison, use_container_width=True)

# Insights Section
st.subheader("🔍 Key Insights")
st.markdown("""
- 📈 **Retention and satisfaction have steadily increased over the years.**
- 🎓 **Engineering sees the highest enrollment, followed by Business.**
- 🍂 **Fall enrollments are generally higher than Spring enrollments.**
""")
