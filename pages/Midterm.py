import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="NFL Prediction Model Proposal"
)
st.title("Introduction/Background")
st.write("This project predicts NFL game outcomes using machine learning, building on existing sports prediction models by leveraging historical game data with features like team stats, player performance.")

st.header("Literature Review")

st.write("""
Several studies have employed machine learning techniques to predict NFL game outcomes. One study utilized a Bayesian linear regression model to estimate an individual player’s impact, controlling for the influence of other players on the field, and incorporating a wide range of performance indicators over an extended timeframe [1].
Another study replaced Total Play Margin with values of a new marginal statistic, which were then input into point spread and logistic models using OLS regression, logistic regression, discriminant analysis, and proportional odds models [2].Research from the University of New Hampshire found that linear regression models were the most accurate, by modeling the relationship between various independent variables and a dichotomous dependent variable [3].
""")

st.header("Dataset Description")

st.write("""
The dataset contains various attributes regarding NFL game characteristics. These key features include:
- **Team win percentage**
- **Pass yards**
- **Sack yards**
- **Rush yards**
- **Amount of downs**
- **Interceptions**
- **Fumbles**
""")


st.subheader("Dataset Link")
st.write("https://www.kaggle.com/datasets/cviaxmiwnptr/nfl-team-stats-20022019-espn")

st.title("Problem")
st.write("Problem - Predicting the outcome of NFL games is complex due to numerous factors.Accurately forecasting wins and losses using machine learning poses a significant challenge, but it can offer valuable insights for fans and analysts.")

st.write("Motivation -  The motivation behind this project is to create a model that maximizes the excitement and entertainment value of NFL games by providing accurate score predictions. This can help fans and analysts better understand team performance trends and make better decisions on aspects like attendance and game expectations.")

st.title("Methods")

st.header("Data Preprocessing Methods Implemented")
st.write("""
    - **Missing Data Handling**: Filled missing values with the mean of numeric columns to maintain dataset integrity.
    - **Feature Engineering**: 
        - Created a new win column indicating if the away team won or lost.
        - Converted possession times to total seconds for consistent numerical analysis.
    - **Data Cleaning**: Removed duplicates to ensure each game is uniquely represented.
    - **Feature Selection**: Retained key performance metrics for training the model.
    """)
st.header("ML Algorithms/Models Implemented")
st.write("""
    These are the ML algorithms we implemented for this midterm checkpoint. 
    - **Logistic Regression (Supervised)**: 
    - **K-Means Clustering (Unsupervised)**: 
""")




st.title("Results and Discussion")
st.header("Visualizations")
st.write("These are our visualizations")
st.header("Analysis of Quantitative Metrics:")
st.header("Analysis of Algorithms/Models:")
st.write("Comparative Analysis and Recommendations")
st.write("Why did your model perform well?")


st.header("Next Steps")



st.title("References")
st.write("""
[1] M. Gifford and Tuncay Bayrak, “A predictive analytics model for forecasting outcomes in the National Football League games using decision tree and logistic regression,” *Decision Analytics Journal*, vol. 8, pp. 100296–100296, Aug. 2023. Available: https://doi.org/10.1016/j.dajour.2023.100296.

[2] J. Roith et al., “Predicting NFL football games based on simulation and modeling,” *International Journal of Statistics and Applied Mathematics*, vol. 3, no. 2, pp. 101–106, 2018. Available: https://www.mathsjournal.com/pdf/2018/vol3issue2/PartB/3-1-45-589.pdf.

[3] S. Bouzianis, “Predicting the Outcome of NFL Games Using Logistic Regression.” Available: https://scholars.unh.edu/cgi/viewcontent.cgi?article=1472&context=honors.
""")
st.header("Team Contributions")
data = {
    "Name": ["Ishaan", "Rahul", "Vishnu", "Rohan", "Sattwik"],
    "Proposal Contribution": [
        "Literature review, Introduction,presentation slides, and problem and motivation",
        "I made the gantt chart, the entire streamlit website, the streamlit repo, the presentation. came up with the project idea and worked on the problem.",
        "Algorithms for supervised and unsupervised learning to classify data points into winning/losing, literature review",
        "Results and Discussion, Video Recording, GitHub Setup",
        "Data Preprocessing methods, presentation slides, problem, motivation",
    ]
}
df = pd.DataFrame(data)
st.table(df)

st.image("gantt.png", caption="Current Gantt Chart for Team", use_column_width=True)