pip install plotly
import streamlit as st
import pandas as pd
import plotly.express as px

# Load Data
file_path = "university_student_dashboard_data.csv"
df = pd.read_csv(file_path)

# Title
st.title("University Admissions & Student Satisfaction Dashboard")

# KPI Metrics
st.subheader("Key Metrics")
st.metric("Total Applications", df['Applications'].sum())
st.metric("Total Admitted", df['Admitted'].sum())
st.metric("Total Enrolled", df['Enrolled'].sum())

# Retention Rate Trends
grouped_year = df.groupby("Year")["Retention Rate (%)"].mean().reset_index()
fig_retention = px.line(grouped_year, x="Year", y="Retention Rate (%)", title="Retention Rate Over Time")
st.plotly_chart(fig_retention)

# Satisfaction Trends
fig_satisfaction = px.line(df, x="Year", y="Student Satisfaction (%)", color="Term", title="Student Satisfaction Over Time")
st.plotly_chart(fig_satisfaction)

# Enrollment Breakdown by Department
department_cols = ["Engineering Enrolled", "Business Enrolled", "Arts Enrolled", "Science Enrolled"]
department_data = df.melt(id_vars=["Year", "Term"], value_vars=department_cols, var_name="Department", value_name="Enrollment")
fig_enrollment = px.bar(department_data, x="Year", y="Enrollment", color="Department", barmode="group", title="Enrollment by Department")
st.plotly_chart(fig_enrollment)

# Spring vs Fall Comparison
fig_term_comparison = px.bar(df, x="Year", y="Enrolled", color="Term", barmode="group", title="Enrollment Trends: Spring vs Fall")
st.plotly_chart(fig_term_comparison)

st.write("### Insights:")
st.write("- Retention and satisfaction have increased steadily over the years.")
st.write("- Engineering sees the highest enrollment, followed by Business.")
st.write("- Fall enrollments are generally higher than Spring enrollments.")
