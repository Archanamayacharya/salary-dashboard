import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title("💰 Salary Dashboard")
# ----------------------------
# Page Setup
# ----------------------------
st.set_page_config(page_title="💰 Salary Dashboard", layout="wide")
st.title("💰 Interactive Salary Trends Dashboard")

# ----------------------------
# Sample Dataset
# ----------------------------
data = {
    'Country': ['USA', 'India', 'Germany', 'UK', 'Canada', 'France', 'Australia', 'Japan'],
    'Salary': [120000, 25000, 90000, 70000, 85000, 65000, 95000, 80000],
    'Experience_Level': ['Senior', 'Junior', 'Senior', 'Mid', 'Mid', 'Junior', 'Senior', 'Mid'],
    'Remote_Ratio': [80, 50, 60, 40, 70, 30, 50, 60]
}
df = pd.DataFrame(data)

# ----------------------------
# Sidebar Filters
# ----------------------------
st.sidebar.header("Filter Options")
countries = st.sidebar.multiselect("Select Countries", df['Country'].unique(), default=df['Country'].tolist())
levels = st.sidebar.multiselect("Select Experience Levels", df['Experience_Level'].unique(), default=df['Experience_Level'].unique())

# Apply filters
filtered_df = df[(df['Country'].isin(countries)) & (df['Experience_Level'].isin(levels))]

# ----------------------------
# Main Dashboard
# ----------------------------
st.subheader("Filtered Salary Data")
st.dataframe(filtered_df)

# Bar Chart: Salary by Country
st.subheader("💹 Salary by Country")
fig, ax = plt.subplots(figsize=(8,4))
sns.barplot(x='Country', y='Salary', hue='Experience_Level', data=filtered_df, ax=ax)
plt.xticks(rotation=45)
st.pyplot(fig)

# Scatter Plot: Salary vs Remote Ratio
st.subheader("📊 Salary vs Remote Work Ratio")
fig2, ax2 = plt.subplots(figsize=(8,4))
sns.scatterplot(x='Remote_Ratio', y='Salary', hue='Experience_Level', data=filtered_df, s=100, ax=ax2)
ax2.set_xlabel("Remote Work Ratio (%)")
ax2.set_ylabel("Salary (USD)")
st.pyplot(fig2)

# Summary Metrics
st.subheader("🔍 Summary Metrics")
col1, col2, col3 = st.columns(3)
col1.metric("Average Salary", f"${filtered_df['Salary'].mean():,.0f}")
col2.metric("Max Salary", f"${filtered_df['Salary'].max():,.0f}")
col3.metric("Min Salary", f"${filtered_df['Salary'].min():,.0f}")
