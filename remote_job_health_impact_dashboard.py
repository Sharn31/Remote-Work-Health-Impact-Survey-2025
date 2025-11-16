import numpy as np
import pandas as pd 
import streamlit as st 
import matplotlib.pyplot as plt
import seaborn as sns 
from streamlit_option_menu import option_menu
from Dashboard_footer import dashboard_footer
import plotly.express as px
import re
import requests
from streamlit_lottie import st_lottie
import json
import html

def load_lottie_file(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)

#def load_lottie_url(url: str):
    #r = requests.get(url)
    #if r.status_code != 200:
    #    return None
    #return r.json()


def show_dashboard(username):
    import streamlit as st

    st.set_page_config(
        page_title="Dashboard | Remote Wellbeing Health Dashboard",
        page_icon="🧑‍💻",
        layout="centered"
    )
    #st.title("🧑‍💻Remote Work Health Impact Survey 2025")
    #st.markdown("<title>Dashboard | Remote Work Health Survey</title>", unsafe_allow_html=True)

    st.write(f"Welcome, {username} 👋")
    st.write("You are now logged into the Remote Wellbeing Health Dashboard.")
    
    

    # Sidebar buttons
    #st.sidebar.title("🧑‍💻Remote Work Health Impact Survey 2025")
    # Inject CSS to color the entire sidebar
    
    st.markdown("""
        <style>
            [data-testid="stSidebar"] {
                background-color: #667eea;
                padding-top: 30px;
            }
            [data-testid="stSidebar"] img {
                display: block;
                margin-left: auto;
                margin-right: auto;
                width: 180px;
                border-radius: 20px;
                border: 3px solid rgba(255,255,255,0.3);
                padding: 10px;
            }
            [data-testid="stSidebarNav"]::before {
                content: "";
                display: block;
                margin-bottom: 20px;
            }
            .css-1d391kg {
                background-color: transparent !important;
            }
            .css-1lcbmhc {
                background-color: transparent !important;
            }
            div[data-baseweb="select"] {
                background-color: transparent !important;
            }
            .stSelectbox > div > div {
                background-color: transparent !important;
            }
            .stSidebar .css-1d391kg {
                background-color: transparent !important;
            }
            .stSidebar .css-1lcbmhc {
                background-color: transparent !important;
            }
            div[class*="option-menu"] {
                background-color: transparent !important;
            }
            div[class*="OptionMenu"] {
                background-color: transparent !important;
            }
            .stSidebar > div > div {
                background-color: transparent !important;
            }
            [class*="option-menu-container"] {
                background-color: transparent !important;
            }
        </style>
    """, unsafe_allow_html=True)
    with st.sidebar:
            st.sidebar.image("logo (3).png", width=180)
            selected = option_menu( 
                menu_title = "",
                options=["Description",
                         "Overview",
                         "Analyzing the Dataset" 
                         ,"Visualizations",
                         "Feedback / Query Form",
                         "Chatbot",
                         "Log Out"],
                icons=["book", "bar-chart", "lightbulb", "graph-up-arrow","chat-dots","bi-chat-dots","box-arrow-right"],
                menu_icon="cast",
                default_index=0,
                orientation="vertical",
                styles={
                    "container": {
                        "padding": "10px",
                        "background": "transparent"
                    },
                    "icon": {
                        "color": "white",
                        "font-size": "22px",
                        "margin-right": "10px"
                    },
                    "nav-link": {
                        "font-size": "16px",
                        "color": "white",
                        "text-align": "left",
                        "margin": "8px 0",
                        "padding": "12px 15px",
                        "border-radius": "10px"
                    },
                    "nav-link-selected": {
                        "background-color": "rgba(255,255,255,0.2)",
                        "font-weight": "bold",
                        "color": "white"
                    }
                }

            )

            
# Cached data loading
    import pandas as pd 
    @st.cache_data
    def load_data():
        return pd.read_csv("post_pandemic_remote_work_health_impact_2025.csv")

    df = load_data()

    if selected == "Description":
        st.header("Welcome to the **Remote Wellbeing Health Solutions Dashboard**! 🌍💼")
        
            
        st.markdown("""
        

        This project explores how different work arrangements — **Remote 🏠**, **Hybrid 🔀**, and **Onsite 🏢** — affect the **mental 🧠** and **physical 💪** health of employees around the world.

        ### 🔍 What this dataset covers:
        - 🧠 **Mental Health**: Burnout, anxiety, depression, PTSD  
        - 💪 **Physical Health**: Back pain, eye strain, neck discomfort  
        - ⚖️ **Work-Life Balance**: Flexibility, workload, social isolation  
        - 💼 **Work Factors**: Job roles, industries, salary range, and hours worked

        ### 📅 Collected in:
        **June 2025**, from a diverse global workforce across multiple age groups, job roles, and sectors.

        ### 🎯 Purpose:
        This dashboard is designed for **data analysts, researchers, HR teams, and policy makers** to:
        - Identify risk vs protective factors 🧩  
        - Benchmark well-being across industries 📊  
        - Improve organizational policies and remote work strategies 🏆

        ### 📂 Dataset Link:
        [🔗 Click here to view the dataset](https://www.kaggle.com/datasets/pratyushpuri/remote-work-health-impact-survey-2025)
        """)
        

    elif  selected == "Overview":
        st.title("Dataset Overview")
        

        st.markdown("""
        The **Remote Work Health Impact 2025** dataset explores the relationship between work arrangements and employee well-being.

        Collected in **June 2025**, it contains survey responses from employees across different job roles, industries, regions, and work setups.

        ---
        ### 📁 About the Dataset

        - **File Name:** `post_pandemic_remote_work_health_impact_2025.csv`
        - **Total Responses:** 1,000+
        - **Total Columns:** 14
        """)
        df = pd.read_csv("post_pandemic_remote_work_health_impact_2025.csv")
        ### ⬇️ DOWNLOAD BUTTON
        st.markdown("### 📂 Download the Full Dataset")
        st.download_button(
        label="📥 Download CSV",
        data=df.to_csv(index=False).encode('utf-8'),
        file_name="remote_work_health_2025.csv",
        mime="text/csv"
        )

        
        st.markdown("""
        ### 🧾 Dataset Structure
        Each row in the CSV file represents a **single employee's survey response**.
        """)

        # Create table for column descriptions
        import pandas as pd

        column_data = {
            "Column Name": [
                "Survey_Date", "Age", "Gender", "Region", "Industry", "Job_Role",
                "Work_Arrangement", "Hours_Per_Week", "Mental_Health_Status",
                "Burnout_Level", "Work_Life_Balance_Score", "Physical_Health_Issues",
                "Social_Isolation_Score", "Salary_Range"
            ],
            "Description": [
                "Date of survey submission (YYYY-MM-DD)",
                "Age of the respondent",
                "Gender identity of the respondent",
                "Region of employment",
                "Industry sector",
                "Specific job role/title",
                "Work mode (Remote/Onsite/Hybrid)",
                "Average hours worked per week",
                "Self-reported mental health condition",
                "Burnout level (Low, Medium, High)",
                "Work-life balance score (1–5)",
                "Physical health complaints (semicolon-separated)",
                "Social isolation score (1–5)",
                "Annual salary range in USD"
            ],
            "Example Values": [
                "2025-06-01", "27, 40, 52", "Female, Male, Non-binary", "Asia, Europe", 
                "Technology, Healthcare", "Data Analyst, HR Manager", "Remote, Onsite", 
                "36, 55, 64", "Anxiety, Burnout, None", "High, Medium", "3, 4, 5", 
                "Back Pain; Eye Strain", "1, 2, 5", "$40K-60K, $80K-100K"
            ]
        }

        df_structure = pd.DataFrame(column_data)
        st.dataframe(df_structure, use_container_width=True)

        st.markdown("---")

        example_row = {
        "Survey_Date": "2025-06-01",
        "Age": 27,
        "Gender": "Female",
        "Region": "Asia",
        "Industry": "Professional Services",
        "Job_Role": "Data Analyst",
        "Work_Arrangement": "Onsite",
        "Hours_Per_Week": 64,
        "Mental_Health_Status": "Stress Disorder",
        "Burnout_Level": "High",
        "Work_Life_Balance_Score": 3,
        "Physical_Health_Issues": "Shoulder Pain; Neck Pain",
        "Social_Isolation_Score": 2,
        "Salary_Range": "$40K-60K"
        }
        example_df = pd.DataFrame(list(example_row.items()), columns=["Column", "Value"])
        example_df["Value"] = example_df["Value"].astype(str)
        st.markdown("### 🧪 Example Data Row")
        st.table(example_df)
        st.markdown("""
        ### 🔑 Key Features
        - 🌍 **Global Coverage**: Responses from Asia, Europe, North America, Africa, Oceania  
        - 🧠 **Rich Health Metrics**: Captures mental & physical health in detail  
        - 👥 **Demographic Diversity**: Includes age, gender, and salary brackets  
        - 🏢 **Work Arrangement Detail**: Differentiates Remote, Hybrid, and Onsite models  
        - 🔒 **Privacy-Safe**: Fully anonymized with no personal identifiers  
        """)

    elif  selected == "Analyzing the Dataset":
        #st.title("Analyzing the Dataset")

        st.markdown("## 🧹 Data Overview & Cleaning")
        st.markdown("This section helps you explore the basic structure of the dataset and handle missing values.")
        # Show DataFrame head
        df = pd.read_csv("post_pandemic_remote_work_health_impact_2025.csv")
        with st.expander("📌 View First Few Rows"):
            st.dataframe(df.head())
        # Show DataFrame tail
        with st.expander("📌 View Last Few Rows"):
            st.dataframe(df.tail())
        # Show shape
        st.markdown(f"🔢 **Dataset Shape:** {df.shape[0]} rows × {df.shape[1]} columns") 

        # Describe
        st.markdown("### 📊 Statistical Summary")
        st.dataframe(df.describe(include='all'))
        # Show missing values
        st.markdown("### ⚠️ Missing Values per Column")
        missing = df.isnull().sum()
        missing_df = pd.DataFrame({'Column': missing.index, 'Missing_Values': missing.values})
        missing_df = missing_df[missing_df['Missing_Values'] > 0]
        if not missing_df.empty:
            st.dataframe(missing_df)
        else:
            st.success("✅ No missing values found in the dataset!")
        
        import io

        st.subheader("🧠 Data Info (Data Types & Memory Usage)")

        # Capture df.info() output
        buffer = io.StringIO()
        df.info(buf=buffer)  # Redirect info output to the buffer
        info_str = buffer.getvalue()

        # Display as plain text
        st.text(info_str)
        st.subheader("🧹 Missing Values Handling")

        # Display missing values before
        st.write("🔍Missing Values Before Filling:")
        missing = df.isnull().sum().reset_index()
        missing.columns = ['Column_Name', 'Missing_Values']
        st.dataframe(missing)

        # Fill missing values with mode
        df['Mental_Health_Status'].fillna(df['Mental_Health_Status'].mode()[0], inplace=True)
        df['Physical_Health_Issues'].fillna(df['Physical_Health_Issues'].mode()[0], inplace=True)

        # Display success message
        st.success("✅ Missing values filled using Mode (most frequent value) for categorical columns.")

        # Display missing values after
        st.write("✅ Missing Values After Filling:")
        missing = df.isnull().sum().reset_index()
        missing.columns = ['Column_Name', 'Missing_Values']
        st.dataframe(missing)

        
        st.write("🔎 Sample Data After Filling Nulls:")
        st.dataframe(df.head())


    elif selected =="Visualizations":
        st.title("Visualizations")
        

        #Chart 1
        # Title
        st.subheader("📊 Work Arrangement vs Social Isolation Score")

        # Load data
        df = pd.read_csv("post_pandemic_remote_work_health_impact_2025.csv")

        

        # Box Plot
        fig = px.box(
        df,
        x='Work_Arrangement',
        y='Social_Isolation_Score',
        color='Work_Arrangement',
        title='Work Arrangement vs Social Isolation Score'
        )
        fig.update_layout(title_x=0.3)

        # Show plot
        st.plotly_chart(fig)
        
    # Title
        st.subheader(" Social Isolation Score - Outlier Removal with Boxplot")

    # Load dataset
        df = pd.read_csv("post_pandemic_remote_work_health_impact_2025.csv")

    # Calculate IQR and remove outliers
        q1 = df['Social_Isolation_Score'].quantile(0.25)
        q3 = df['Social_Isolation_Score'].quantile(0.75)
        iqr = q3 - q1
        min_r = q1 - (1.5 * iqr)
        max_r = q3 + (1.5 * iqr)

        st.write(f"📉 Lower Limit: {min_r:.2f}")
        st.write(f"📈 Upper Limit: {max_r:.2f}")

        df_clean = df[(df['Social_Isolation_Score'] >= min_r) & (df['Social_Isolation_Score'] <= max_r)]

        # Boxplot (Cleaned)
        fig = px.box(
        df_clean,
        x='Work_Arrangement',
        y='Social_Isolation_Score',
        color='Work_Arrangement',
        title='Work Arrangement vs Social Isolation Score (Cleaned Data)',
        points='all'
        )

        fig.update_layout(
        title_x=0.3,
        xaxis_title='Work Arrangement',
        yaxis_title='Social Isolation Score'
        )

        # Display the plot
        st.plotly_chart(fig)
        # Insights
        st.subheader("🔍 Key Insights")

        # Automatic insights
        group_medians = df_clean.groupby("Work_Arrangement")["Social_Isolation_Score"].median().sort_values()

        insight_text = ""
        for i, (role, score) in enumerate(group_medians.items()):
            insight_text += f"- **{role}** median isolation score: `{score:.2f}`\n"

            most_isolated = group_medians.idxmax()
            least_isolated = group_medians.idxmin()

        summary = f"""
        - 💡 The **highest median** social isolation score is observed in **{most_isolated}**.
        - 🧘 The **lowest median** isolation score is in **{least_isolated}**, indicating better social well-being.
        """

        st.markdown(insight_text)
        st.markdown(summary)
        st.markdown("""---""")

        ##Chart 2
        st.subheader("🧠 Mental Health Status by Gender")

        df_gender_mental_health = df.groupby(['Mental_Health_Status', 'Gender']).size().reset_index(name='Count')
        
        # Plot polar area chart
        fig = px.bar(df_gender_mental_health,x='Mental_Health_Status',y='Count',color='Gender',
                    barmode='group',
                    title='Mental Health Status by Gender')
                    
        fig.update_layout(title_x=0.3)
        st.plotly_chart(fig)

        st.subheader("🔍 Key Insights")


        # Gender totals for mental health issues (excluding 'Healthy')
        issue_counts = df_gender_mental_health.groupby('Gender')['Count'].sum()
        gender_1, count_1 = issue_counts.index[0], issue_counts.iloc[0]
        gender_2, count_2 = issue_counts.index[1], issue_counts.iloc[1]

        st.write(f"• Mental health challenges are reported **almost equally** across genders: {gender_1} - {count_1}, {gender_2} - {count_2}.")
        st.write("• This near parity highlights that **mental health struggles are not gender-biased** and affect both males and females at nearly the same rate — indicating a universal need for support and resources.")
        st.markdown("""---""")

        #Chart 3
        st.subheader(" Age vs  Social Isolation Score")
        age_isolation=df.groupby('Age')['Social_Isolation_Score'].mean().reset_index()
        fig = px.line(
        age_isolation,
        x='Age',
        y='Social_Isolation_Score',
        title='Age vs Social Isolation Score',
        markers=True
        )

        fig.update_layout(
        title_x=0.3,
        xaxis_title='Age',
        yaxis_title='Average Social Isolation Score'
        )

        # Display chart in Streamlit
        st.plotly_chart(fig)

        # Optional insight
        st.subheader("🔍 Insight")
        st.write("• The line chart shows how social isolation scores vary with age.")
        st.write("• Any sudden increases or decreases may indicate **age groups more prone to isolation**.")
        st.write("• This can help organizations focus support programs for the most vulnerable age groups.")
        st.markdown("""---""")

        #Chart 4 
        st.subheader("📈Job Role Vs Burnout Level")
        df_count=df.groupby(['Job_Role','Burnout_Level']).size().reset_index(name='Count')
        fig = px.line(
        df_count,
        x='Job_Role',
        y='Count',
        color='Burnout_Level',
        markers=True,
        title=' Job Role vs Burnout Level'
        )

        fig.update_layout(
        title_x=0.3,
        xaxis_tickangle=-45
        )

        st.plotly_chart(fig)

        # 🔍 Insight Section
        st.subheader("🔍 Insight")
        st.write("• This chart shows how burnout levels vary across different job roles.")
        st.write("• Helps identify job roles with consistently high burnout trends.")
        st.markdown("""---""")

        # Chart 5
                
        st.subheader("Industry vs Mental Health Status🧠")
        industry_mental_health = df.groupby(['Industry', 'Mental_Health_Status']).size().reset_index(name='Count')

        # Optional Filters
        status_options = industry_mental_health['Mental_Health_Status'].unique()
        selected_status = st.multiselect("Select Mental Health Status", status_options, default=status_options)

        industry_options = industry_mental_health['Industry'].unique()
        selected_industry = st.multiselect("Select Industry", industry_options, default=industry_options)

        # Filter the data
        filtered_df = industry_mental_health[
            (industry_mental_health['Mental_Health_Status'].isin(selected_status)) &
            (industry_mental_health['Industry'].isin(selected_industry))
        ]

        #Plot
        fig = px.sunburst(
        filtered_df,
        path=['Industry', 'Mental_Health_Status'],
        values='Count',
        title='Mental Health Distribution Across Industries')
        fig.update_layout(title_x=0.3,height=800,width=1000)
        st.plotly_chart(fig)

        # 🔍 Insights
        st.subheader("🔍 Insights")
        st.write(f"• Explore how mental health status is distributed within each industry.")
        st.write(f"• Outer ring shows mental health categories nested inside industries.")
        st.write(f"• Use the filters above to explore specific industries or statuses.")
        st.markdown("""---""")

        #Chart 6
        st.subheader("Region Vs Burnout Level")
        
        # Group the data
        mental_region = df.groupby(["Mental_Health_Status", "Region"]).size().reset_index(name="Count")

        # Add "All" option to dropdown
        regions = ["All"] + sorted(mental_region["Region"].unique().tolist())

        # Streamlit dropdown
        selected_region = st.selectbox("Select Region", regions)

    # Filter data if a specific region is selected
        if selected_region != "All":
            filtered_data = mental_region[mental_region["Region"] == selected_region]
        else:
            filtered_data = mental_region  # no filter

        # Plot
        fig = px.bar(
        filtered_data,
        x="Region",
        y="Count",
        color="Mental_Health_Status",
        barmode="group",
        orientation='v',
        title=f"Mental Health Status by Region" if selected_region == "All" else f"Mental Health Status in {selected_region}"
        )

        fig.update_layout(
        xaxis_title="Region",
        yaxis_title="Number of Respondents",
        title_x=0.3,
        template="plotly_white"
        )

        st.plotly_chart(fig)



        ## 🔍 Insights
        
        st.subheader("🔍 Hidden Insights")
        st.markdown(
        "- **PTSD is the most reported issue globally**, indicating widespread trauma impact.\n"
        "- **Asia shows highest burnout**, Europe has a **balanced spread**, and South America reports **most ADHD cases**."
                )
        st.markdown("""---""")

    #Chart 7
        st.subheader("Physical Health Issues Vs Work Arrangement")

        df_exploded = df.assign(Physical_Issue_Split=df['Physical_Health_Issues'].str.split('; ')).explode('Physical_Issue_Split')
        grouped = df_exploded.groupby(['Physical_Issue_Split', 'Work_Arrangement']).size().reset_index(name='Count')
        fig = px.treemap(grouped,path=['Work_Arrangement','Physical_Issue_Split'],values='Count',
                title='Physical Health Issues Across Work Arrangements')

        fig.update_layout(title_x=0.3)
        st.plotly_chart(fig)
        

        st.markdown("""
        ### 🧠 Hidden Insights: Physical Health Issues by Work Arrangement

        - **Onsite workers** report the highest rates of **Eye Strain**, **Shoulder Pain**, and **Back Pain**, likely due to prolonged desk and screen exposure without ergonomic setups.
        - **Hybrid workers** face a mix of issues, with a balanced pattern across all physical complaints, indicating inconsistency in workspace setups.
        - **Remote workers** experience relatively fewer complaints, but **Eye Strain** and **Back Pain** still stand out, possibly from poor home-office ergonomics.
        - **Wrist and Neck Pain** are the least reported across all types, but still relevant for long-term device usage.
        - These patterns highlight the importance of **ergonomic awareness and preventive exercises** for all work modes.
        """)
        st.markdown("""---""")

        #Chart 8
        st.subheader("Work Arrangement Vs Burnout Leve")
        grouped = df.groupby(['Work_Arrangement', 'Burnout_Level']).size().reset_index(name='Count')
        fig=px.pie(grouped,'Burnout_Level', values='Count',facet_col='Work_Arrangement',color='Burnout_Level',
            title='Work Arrangement vs Burnout Level'
            )
        fig.update_layout(title_x=0.3)
        fig.update_traces(textinfo='percent+label')
        st.plotly_chart(fig)
        st.markdown("""
        ### 🔍 Hidden Insights: Burnout Patterns by Work Arrangement

        - **Remote workers** report the **highest percentage of High Burnout (46.4%)**, suggesting that isolation, overworking, or blurred work-life boundaries might be contributing factors.
        - **Hybrid workers** have the **most balanced burnout distribution**, but still show a **notably high Medium Burnout (45.1%)**, indicating moderate stress from switching environments.
        - **Onsite workers** experience the **highest Low Burnout rate (30.2%)**, possibly due to structured routines, in-person support, and clearer work boundaries.

        📌 These insights suggest that **remote work needs more support mechanisms** (like check-ins and wellness programs), while hybrid setups must ensure consistency and stability.
        """)
        st.markdown("""---""")

        #Chart 9
        
        import seaborn as sns 
        st.subheader("Correlation Heatmap of Numerical Feature")
        # Convert Burnout_Level to numeric if it's categorical
        df['Burnout_Level'] = df['Burnout_Level'].map({'Low': 1, 'Medium': 2, 'High': 3})

        numeric_data = df.select_dtypes(include=['number'])
        plt.figure(figsize=(10,8))
        sns.heatmap(numeric_data.corr(), annot=True, cmap='coolwarm')
        plt.title('Correlation Heatmap')
        st.pyplot(plt)

        st.markdown(""" 🔺 **Social Isolation** shows slight positive correlation → More isolation = slightly higher burnout.
        - 🔻 **Work-Life Balance** has a weak negative correlation → Better balance = slightly lower burnout.
        - ⚠️ **Hours Worked** surprisingly shows very weak correlation → Suggests qualitative stress may be more important.
        - 👥 **Age & Demographics** have negligible impact in this dataset.
        """)
        st.markdown("""---""")

        #Chart 10
        st.subheader("Distribution of Weekly Hours by Salary Range")
        salary_order = [
        "$40K-60K",
        "$60K-80K",
        "$80K-100K",
        "$100K-120K",
        "$120K+"
        ]
        df['Salary_Range'] = df['Salary_Range'].str.replace('–', '-', regex=False)  # Replace en-dash
        df['Salary_Range'] = df['Salary_Range'].str.replace(' ', '')
        df['Salary_Range'] = pd.Categorical(df['Salary_Range'], categories=salary_order, ordered=True)

        fig = px.violin(
        df,
        x='Salary_Range',
        y='Hours_Per_Week',
        color='Salary_Range',
        category_orders={"Salary_Range": salary_order},
        box=True,
    
        title='Distribution of Weekly Hours by Salary Range'
        )

        fig.update_layout(
        xaxis_title='Salary Range',
        yaxis_title='Hours per Week',
        showlegend=False,
        title_x=0.3
        )

        st.plotly_chart(fig)

        st.markdown("""
                    - **Higher salary doesn’t reduce work hours:**  
    Individuals in the **$120K+ salary bracket** still tend to work **55–60+ hours/week**, suggesting that **higher income often demands longer hours**.

    - **Workload remains high across salary ranges:**  
    Most employees, regardless of salary, report **45–60 hours/week**, highlighting a widespread **culture of long working hours**.

    - **Risk of underpaid overwork:**  
    Even in the **$40K–60K group**, some work over **50 hours/week**, indicating **potential exploitation or high stress** roles.

    - **Tight clustering = normalized overwork:**  
    Violin shapes are narrow at the center across all salary ranges, revealing a **common expectation of extended working hours** in most job roles.

                    """)

        st.markdown("""---""")

        #Chart 11
        st.subheader("Physical Health Issues vs Mental Health Issues")
        grouped = df_exploded.groupby(['Physical_Issue_Split', 'Mental_Health_Status']).size().reset_index(name='Count')

        fig = px.scatter(
        grouped,
        x='Physical_Issue_Split',
        y='Mental_Health_Status',
        size='Count',
        color='Mental_Health_Status',
        title=' Physical vs Mental Health Distribution',
        size_max=10
        )
        fig.update_layout(
        title_x=0.3,
        xaxis_title='Physical Issues',
        yaxis_title='Mental Health Status'
        )
        st.plotly_chart(fig)
        st.markdown("### 🔍 Hidden Insights from Physical vs Mental Health Bubble Chart")

        st.markdown("""
        **Eye Strain is Common Across All Mental Health Issues**  
        - Eye strain appears across ADHD, Anxiety, Burnout, Depression, PTSD, and Stress Disorder.  
        - Indicates universal strain likely due to screen exposure in remote work.

        **Burnout Strongly Linked to Neck & Shoulder Pain**  
        - Burnout shows higher counts for neck and shoulder issues.  
        - Suggests poor posture or ergonomic strain among burned-out individuals.

        **Depression Correlates with Back Pain**  
        - Depression reports higher back pain frequency.  
        - Indicates possible psychosomatic links or sedentary behavior impact.

        **Low Wrist Pain Across All Groups**  
        - Minimal wrist-related complaints across mental health statuses.  
        - Could be due to improved devices or reduced manual input.

        **Stress Disorder Mirrors PTSD Physical Symptoms**  
        - Similar patterns for both categories suggest shared physical stress responses.
        """)
        
    elif  selected == "Feedback / Query Form":
        import sqlite3
        from datetime import datetime
        @st.cache_resource
        def get_connection():
            conn = sqlite3.connect("form.db", check_same_thread=False)
            return conn
        conn = get_connection()
        cursor = conn.cursor()

        
        
        # Create table
        cursor.execute('''CREATE TABLE IF NOT EXISTS form(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT,
                    email TEXT,
                    feedback_type TEXT,
                    message TEXT,
                    submitted_on TIMESTAMP
                    )'''
                    )
        conn.commit()
    
    
    

    

        ###Streamlit UI
        
        st.subheader("📝 Feedback / Query Form")
        name=st.text_input("Enter Your Name")
        email=st.text_input("Enter your Email")
        feedback_type=st.selectbox("Feedback Type",["Query","Suggestion","Complaint","Compliment","Other"])
        message=st.text_area("Your Message")

        
        if st.button("Submit"):
            if name and email and message:
                if not re.match(r"^[\w\.-]+@[\w\.-]+\.\w+$", email):
                    st.warning("⚠️ Please enter a valid email address.")
                else:
                    # ✅ Email is valid, insert into DB
                    cursor.execute(
                "INSERT INTO form(name, email, feedback_type, message, submitted_on) VALUES (?, ?, ?, ?, ?)",
                (name, email, feedback_type, message, datetime.now())
                    )
                    conn.commit()
                    st.success("✅ Thank you! Your feedback has been submitted.")
            else:
                st.warning("⚠️ Please fill all fields before submitting.")


                # View feedback section
        with st.expander("🔍 View Submitted Feedback"):
            username = st.session_state.get("username")  # Get current user's username

            if username:
                cursor.execute("""
                SELECT name, email, feedback_type, message, submitted_on 
                FROM form 
                WHERE name = ? 
                ORDER BY submitted_on DESC
                """, (username,))
                rows = cursor.fetchall()

                if rows:
                    for row in rows:
                        st.markdown(f"**Name:** {row[0]}  \n📧 **Email:** {row[1]}")
                        st.markdown(f"🔹 **Type:** `{row[2]}`")
                        st.write(f"> 💬 {row[3]}")
                    st.caption(f"🕒 Submitted on {row[4]}")
                    st.markdown("---")
                else:
                    st.info("You haven’t submitted any feedback yet.")
            else:
                st.warning("⚠️ No username found in session. Please log in again.")
    elif selected == "Chatbot":
        # Add custom CSS for chatbot
        st.markdown("""
        <style>
            .chat-container {
                max-width: 800px;
                margin: 0 auto;
            }
            .user-message {
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                color: white;
                padding: 15px 20px;
                border-radius: 20px 20px 5px 20px;
                margin: 10px 0;
                margin-left: 20%;
                box-shadow: 0 4px 15px rgba(102, 126, 234, 0.3);
            }
            .ai-message {
                background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
                color: white;
                padding: 15px 20px;
                border-radius: 20px 20px 20px 5px;
                margin: 10px 0;
                margin-right: 20%;
                box-shadow: 0 4px 15px rgba(245, 87, 108, 0.3);
            }
            .chat-header {
                text-align: center;
                padding: 20px;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                color: white;
                border-radius: 15px;
                margin-bottom: 30px;
                box-shadow: 0 4px 15px rgba(102, 126, 234, 0.3);
            }
            .stTextInput > div > div > input {
                border-radius: 25px;
                padding: 12px 20px;
                border: 2px solid #667eea;
            }
        </style>
        """, unsafe_allow_html=True)

        # Initialize chat history
        if "chat_history" not in st.session_state:
            st.session_state.chat_history = []

        if "last_message" not in st.session_state:
            st.session_state.last_message = ""

        # Dataset knowledge base
        dataset_info = {
            "columns": {
                "Survey_Date": "Date of survey submission (YYYY-MM-DD format)",
                "Age": "Age of the respondent",
                "Gender": "Gender identity (Female, Male, Non-binary)",
                "Region": "Geographic region (Asia, Europe, North America, Africa, Oceania, South America)",
                "Industry": "Industry sector (Technology, Healthcare, Finance, etc.)",
                "Job_Role": "Specific job title/role (Data Analyst, HR Manager, etc.)",
                "Work_Arrangement": "Work mode: Remote, Hybrid, or Onsite",
                "Hours_Per_Week": "Average hours worked per week",
                "Mental_Health_Status": "Mental health condition (Anxiety, Depression, Burnout, PTSD, Stress Disorder, ADHD, or None)",
                "Burnout_Level": "Burnout severity: Low, Medium, or High",
                "Work_Life_Balance_Score": "Work-life balance rating from 1-5 (1=Poor, 5=Excellent)",
                "Physical_Health_Issues": "Physical complaints (Back Pain, Eye Strain, Neck Pain, Shoulder Pain, Wrist Pain - semicolon separated)",
                "Social_Isolation_Score": "Social isolation rating from 1-5 (1=Very Isolated, 5=Well Connected)",
                "Salary_Range": "Annual salary in USD ($40K-60K, $60K-80K, $80K-100K, $100K-120K, $120K+)"
            },
            "insights": {
                "remote_workers": "Remote workers report highest burnout (46.4% High), suggesting need for better work-life boundaries and support systems.",
                "hybrid_workers": "Hybrid workers show balanced burnout but high Medium burnout (45.1%), indicating stress from environment switching.",
                "onsite_workers": "Onsite workers have highest Low burnout rate (30.2%), possibly due to structured routines and in-person support.",
                "physical_health": "Onsite workers report most Eye Strain, Shoulder Pain, and Back Pain. Remote workers have fewer complaints but still face Eye Strain and Back Pain.",
                "mental_health": "PTSD is the most reported mental health issue globally. Mental health challenges are nearly equal across genders.",
                "isolation": "Social isolation varies by work arrangement - remote workers tend to have higher isolation scores."
            }
        }

        def generate_response(user_message: str) -> str:
            """Simple rule-based chatbot that understands project context"""
            msg_lower = user_message.lower().strip()
            
            # Greetings
            if any(word in msg_lower for word in ["hi", "hello", "hey", "greetings"]):
                return "👋 Hello! I'm your AI assistant for the Remote Work Health Impact Dashboard. I can help you understand:\n\n• Dataset columns and their meanings\n• Key insights from the data\n• Solutions and recommendations\n• Project information\n\nWhat would you like to know?"
            
            # Help
            if any(word in msg_lower for word in ["help", "what can you do", "capabilities"]):
                return "I can help you with:\n\n📊 **Dataset Information:**\n• Explain all 14 columns in the dataset\n• Describe what each column means\n• Provide examples of values\n\n💡 **Insights & Analysis:**\n• Key findings about remote vs onsite work\n• Mental and physical health patterns\n• Burnout trends by work arrangement\n\n💼 **Solutions & Recommendations:**\n• Suggestions for improving remote work health\n• Strategies to reduce burnout\n• Tips for better work-life balance\n\nJust ask me about columns, insights, or solutions!"
            
            # Columns information
            if any(word in msg_lower for word in ["column", "columns", "dataset", "data", "fields", "variables"]):
                response = "📊 **Dataset Columns (14 total):**\n\n"
                for col, desc in dataset_info["columns"].items():
                    response += f"• **{col}**: {desc}\n"
                response += "\n💡 Ask me about any specific column for more details!"
                return response
            
            # Specific column queries
            for col_name, description in dataset_info["columns"].items():
                if col_name.lower().replace("_", " ") in msg_lower or col_name.lower() in msg_lower:
                    examples = {
                        "Work_Arrangement": "Examples: Remote, Hybrid, Onsite",
                        "Mental_Health_Status": "Examples: Anxiety, Depression, Burnout, PTSD, Stress Disorder, ADHD, None",
                        "Burnout_Level": "Examples: Low, Medium, High",
                        "Work_Life_Balance_Score": "Scale: 1 (Poor) to 5 (Excellent)",
                        "Social_Isolation_Score": "Scale: 1 (Very Isolated) to 5 (Well Connected)",
                        "Physical_Health_Issues": "Common issues: Back Pain, Eye Strain, Neck Pain, Shoulder Pain, Wrist Pain (can have multiple)"
                    }
                    response = f"📋 **{col_name}**\n\n{description}\n"
                    if col_name in examples:
                        response += f"\n{examples[col_name]}"
                    return response
            
            # Insights
            if any(word in msg_lower for word in ["insight", "finding", "trend", "pattern", "analysis"]):
                response = "💡 **Key Insights from the Data:**\n\n"
                for key, insight in dataset_info["insights"].items():
                    response += f"• {insight}\n"
                return response
            
            # Solutions and recommendations
            if any(word in msg_lower for word in ["solution", "recommendation", "suggest", "advice", "help", "improve", "reduce", "prevent"]):
                solutions = {
                    "burnout": "🔥 **To Reduce Burnout:**\n• Set clear work boundaries and stick to regular hours\n• Take regular breaks and practice mindfulness\n• Communicate workload concerns with managers\n• Use time management techniques (Pomodoro, time blocking)\n• Ensure adequate rest and recovery time",
                    "remote": "🏠 **For Remote Workers:**\n• Create a dedicated workspace with ergonomic setup\n• Schedule virtual coffee breaks with colleagues\n• Join online communities or coworking spaces\n• Set strict start/end times for work\n• Use video calls to maintain social connections",
                    "physical": "💪 **Physical Health Solutions:**\n• Invest in ergonomic furniture (chair, desk, monitor stand)\n• Follow 20-20-20 rule for eye strain (every 20 min, look 20 feet away for 20 sec)\n• Do regular stretching exercises\n• Take walking breaks throughout the day\n• Consider standing desk or desk exercises",
                    "mental": "🧠 **Mental Health Support:**\n• Access employee assistance programs (EAP)\n• Practice stress management techniques\n• Maintain social connections outside work\n• Seek professional help when needed\n• Practice work-life balance activities",
                    "isolation": "👥 **Reduce Social Isolation:**\n• Schedule regular team meetings and check-ins\n• Join virtual team building activities\n• Participate in online professional communities\n• Maintain regular communication with colleagues\n• Consider hybrid work arrangements"
                }
                
                if "burnout" in msg_lower:
                    return solutions["burnout"]
                elif "remote" in msg_lower or "work from home" in msg_lower:
                    return solutions["remote"]
                elif "physical" in msg_lower or "pain" in msg_lower or "strain" in msg_lower:
                    return solutions["physical"]
                elif "mental" in msg_lower or "anxiety" in msg_lower or "depression" in msg_lower:
                    return solutions["mental"]
                elif "isolation" in msg_lower or "lonely" in msg_lower or "social" in msg_lower:
                    return solutions["isolation"]
                else:
                    return "💡 **General Recommendations:**\n\n" + "\n\n".join([f"{key.replace('_', ' ').title()}:\n{val}" for key, val in solutions.items()])
            
            # Project information
            if any(word in msg_lower for word in ["project", "about", "what is this", "dashboard", "purpose"]):
                return """📊 **Remote Work Health Impact Dashboard**

This project analyzes how different work arrangements (Remote 🏠, Hybrid 🔀, Onsite 🏢) affect employee mental and physical health.

**Dataset:** 1,000+ survey responses from June 2025
**Columns:** 14 features covering demographics, work arrangements, health metrics
**Purpose:** Help organizations understand work arrangement impacts and improve employee wellbeing

**Key Areas Analyzed:**
• Mental health (burnout, anxiety, depression, PTSD)
• Physical health (back pain, eye strain, neck/shoulder issues)
• Work-life balance scores
• Social isolation levels
• Burnout patterns by work arrangement

Ask me about specific columns, insights, or solutions!"""
            
            # Default response
            return "I understand you're asking about: '" + user_message + "'\n\nI can help you with:\n• Dataset columns and their meanings\n• Key insights and findings\n• Solutions and recommendations\n• Project information\n\nTry asking about columns, insights, or solutions! 💡"

        # Chat header
        st.markdown("""
        <div class="chat-header">
            <h1>🤖 Remote Work Health Dashboard Assistant</h1>
            <p>Ask me about dataset columns, insights, or solutions for remote work health!</p>
        </div>
        """, unsafe_allow_html=True)

        # Display chat history with styled messages
        chat_container = st.container()
        with chat_container:
            if not st.session_state.chat_history:
                st.info("👋 Hi! I'm your AI assistant. I can help you understand the dataset columns, key insights, and provide solutions. Try asking:\n\n• 'What are the columns?'\n• 'Tell me about Work_Arrangement'\n• 'What are the insights?'\n• 'Suggest solutions for burnout'")
            else:
                for chat in st.session_state.chat_history:
                    # Escape HTML to prevent rendering issues, then convert newlines to <br>
                    user_msg = html.escape(str(chat['user']))
                    ai_msg = html.escape(str(chat['ai'])).replace('\n', '<br>')
                    
                    # User message
                    st.markdown(f"""
                    <div class="user-message">
                        <strong>👤 You:</strong><br>
                        {user_msg}
                    </div>
                    """, unsafe_allow_html=True)
                    
                    # AI message
                    st.markdown(f"""
                    <div class="ai-message">
                        <strong>🤖 AI Assistant:</strong><br>
                        {ai_msg}
                    </div>
                    """, unsafe_allow_html=True)

        # Input area using form to handle input clearing
        with st.form(key="chat_form", clear_on_submit=True):
            col1, col2 = st.columns([5, 1])
            with col1:
                user_input = st.text_input(
                    "Type your message:",
                    placeholder="Ask about columns, insights, or solutions...",
                    label_visibility="collapsed"
                )
            with col2:
                send_button = st.form_submit_button("Send 💬", use_container_width=True, type="primary")

            # Handle form submission
            if send_button:
                if user_input and user_input.strip() and user_input != st.session_state.get("last_message", ""):
                    st.session_state.last_message = user_input
                    ai_response = generate_response(user_input)
                    st.session_state.chat_history.append({
                        "user": user_input,
                        "ai": ai_response
                    })
                    st.rerun()
                elif not user_input or not user_input.strip():
                    st.warning("Please enter a message before sending.")

        # Clear chat button (outside form)
        if st.session_state.chat_history:
            if st.button("🗑️ Clear Chat History", use_container_width=True):
                st.session_state.chat_history = []
                st.session_state.last_message = ""
                st.rerun()

        
    elif selected =="Log Out": 
        st.session_state.logged_in = False
        st.session_state.username = ""
        st.rerun()  # This reloads the app and redirects to SignIn/SignUp



    dashboard_footer()





