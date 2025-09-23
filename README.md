# 💰 Salary Trends Dashboard

An **interactive Streamlit dashboard** to visualize salary trends across different countries and experience levels. Users can filter by country and experience level to explore data interactively and gain insights into salary distributions and remote work trends.

---

## **Features**

* **Interactive Filters:** Filter data by country and experience level using the sidebar.
* **Data Table:** View the filtered salary data in a table.
* **Bar Chart:** Compare salaries across countries with experience level distinction.
* **Scatter Plot:** Visualize salary versus remote work ratio.
* **Summary Metrics:** Quick insights with average, minimum, and maximum salary.

---

## **Installation & Setup**

1. Clone the repository:

   ```bash
   git clone https://github.com/Archanamayacharya/salary-dashboard.git
   cd salary-dashboard
   ```

2. Install dependencies:

   ```bash
   pip install streamlit pandas matplotlib seaborn
   ```

3. Run the Streamlit app:

   ```bash
   streamlit run app.py
   ```

---

## **Live Dashboard**

A **permanent live version** of this app is hosted on Streamlit Cloud:
(https://salary-dashboard-mrotrttexsgrrzxjr3vusr.streamlit.app/)

---

## **Sample Dataset**

The dashboard uses a sample dataset with the following columns:

* `Country` – Country of the employee
* `Salary` – Salary in USD
* `Experience_Level` – Junior, Mid, Senior
* `Remote_Ratio` – Percentage of remote work

---

## **License**

This project is open-source and available under the MIT License.
