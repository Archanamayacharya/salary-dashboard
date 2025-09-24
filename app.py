import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ----------------------------
# Page Setup
# ----------------------------
st.set_page_config(page_title="💰 Salary Dashboard", layout="wide")
st.title("💰 Interactive Salary Trends Dashboard")

# ----------------------------
# Load Dataset
# ----------------------------
@st.cache_data
def load_data():
    return pd.read_csv("engineered_data (1).csv")

df = load_data()

# ----------------------------
# Sidebar Filters
# ----------------------------
st.sidebar.header("Filter Options")
countries = st.sidebar.multiselect(
    "Select Countries", 
    df['employee_residence'].unique(), 
    default=df['employee_residence'].unique()
)
levels = st.sidebar.multiselect(
    "Select Experience Levels", 
    df['experience_level'].unique(), 
    default=df['experience_level'].unique()
)

# Apply filters
filtered_df = df[
    (df['employee_residence'].isin(countries)) & 
    (df['experience_level'].isin(levels))
]

# ----------------------------
# Main Dashboard
# ----------------------------
st.subheader("Filtered Salary Data")
st.dataframe(filtered_df[['employee_residence', 'experience_level', 'salary_in_usd', 'remote_ratio']])

# ----------------------------
# Bar Chart: Salary by Country
# ----------------------------
st.subheader("💹 Salary by Country")
fig, ax = plt.subplots(figsize=(8, 4))
sns.barplot(
    x='employee_residence', 
    y='salary_in_usd', 
    hue='experience_level', 
    data=filtered_df, 
    ax=ax,
    errorbar=None
)
plt.xticks(rotation=45)
ax.set_ylabel("Salary (USD)")
ax.set_xlabel("Country")
st.pyplot(fig)

# ----------------------------
# Scatter Plot: Salary vs Remote Ratio
# ----------------------------
st.subheader("📊 Salary vs Remote Work Ratio")
fig2, ax2 = plt.subplots(figsize=(8, 4))
sns.scatterplot(
    x='remote_ratio', 
    y='salary_in_usd', 
    hue='experience_level', 
    data=filtered_df, 
    s=100, 
    ax=ax2
)
ax2.set_xlabel("Remote Work Ratio (%)")
ax2.set_ylabel("Salary (USD)")
st.pyplot(fig2)

# ----------------------------
# Summary Metrics
# ----------------------------
st.subheader("🔍 Summary Metrics")
col1, col2, col3 = st.columns(3)
col1.metric("Average Salary", f"${filtered_df['salary_in_usd'].mean():,.0f}")
col2.metric("Max Salary", f"${filtered_df['salary_in_usd'].max():,.0f}")
col3.metric("Min Salary", f"${filtered_df['salary_in_usd'].min():,.0f}")
