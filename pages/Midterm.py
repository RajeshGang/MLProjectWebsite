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

st.title("Potential Results and Discussion")


st.header("Data Preprocessing Methods")

st.write("""
Data preprocessing is crucial for ensuring that the dataset is suitable for machine learning algorithms. Below are the identified methods:
- **Feature Engineering**: Create new features like rivalry records, win streaks, and compute key statistics such as yards gained, yards allowed, and third down conversions.
  
- **Data Management**: Handle missing values using techniques like mean, median, and mode imputations. Also manage inconsistent data, duplicates, and data gaps.
  
- **Data Standardization**: Since different statistics are on different scales, apply techniques like min-max scaling and z-scores to standardize the data.
""")

st.header("Machine Learning Algorithms")

st.write("""
Several machine learning models are proposed for this project, each selected based on their effectiveness in predicting NFL game outcomes:

**Supervised Learning Algorithms (CS 4641 and CS 7641):**
1. **Logistic Regression**: A simple yet effective algorithm for binary classification, such as win/loss predictions. It will serve as a baseline model.
2. **K-Nearest Neighbors (K-NN)**: This classification algorithm will utilize proximity to neighbors and regression techniques to classify a data point.
3. **Random Forest**: This ensemble method will aggregate the outcomes of multiple decision trees, improving classification performance and reducing overfitting.

**Unsupervised Learning Algorithms (CS 7641):**
1. **Hierarchical Clustering**: This bottom-up clustering approach merges similar points based on increasing differences, useful for discovering patterns in team performances.
2. **K-Means Clustering**: Groups points into predefined clusters based on similarity, useful for grouping teams or players with similar attributes.
3. **Density-Based Clustering**: Forms clusters based on proximity and density, ideal for identifying outliers in performance data.
""")
st.header("Justification for the Proposed Methods")

st.write("""
The proposed models are effective for the following reasons:
- **Logistic Regression** provides a simple, interpretable model that can gauge the quality of other algorithms.
- **K-NN** uses proximity-based classification, making it intuitive and efficient for small to medium datasets.
- **Random Forest** can handle a large number of features and automatically capture complex interactions between them.
  
In unsupervised learning:
- **Hierarchical Clustering** allows for flexible cluster formation without predetermining the number of clusters.
- **K-Means Clustering** is fast and effective when the number of clusters is known.
- **Density-Based Clustering** is well-suited to handle noisy data and find clusters of arbitrary shapes.
""")
st.header("Quantitative Metrics")
st.write("""
The performance of our models will be evaluated using the following metrics:
1. **Accuracy**: Measures how often the model correctly predicts the winning team. A higher value (closer to 1) indicates better overall performance in predicting the correct outcome.
2. **Precision**: Focuses on the ratio of correctly predicted wins to the total number of predicted wins. A higher precision means fewer false positives (incorrect win predictions).
3. **F1 Score**: Balances precision and recall, giving insight into the model’s ability to avoid both false positives and false negatives. A higher F1 score indicates better balance between identifying wins and minimizing incorrect predictions.
""")
st.header("Project Goals")
st.write("""
- **Create an interpretable model** that provides accurate insights for NFL analysts and sports enthusiasts:
    - **Accuracy > 0.7**
    - **Precision > 0.75**
    - **F1 Score > 0.75**
- **Design an efficient model** that maximizes computational efficiency by using methods such as logistic regression and K-means clustering.
""")
st.header("Overall Expectation")
st.write("""
Achieve a reliable, interpretable, and accurate model for predicting which NFL team is likely to win a game.
""")

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