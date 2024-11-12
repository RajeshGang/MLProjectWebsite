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
# Logistic Regression
st.subheader("Logistic Regression (Supervised)")
st.markdown("""
- **Reason for Selection**: Chosen for its simplicity and speed in training, making it an excellent baseline model for predicting binary outcomes (win/loss).
- **Insights Provided**: Offers insights into feature importance and the type of relationships between features and game outcomes (e.g., positive or negative influences).
""")

# K-Means Clustering
st.subheader("K-Means Clustering (Unsupervised)")
st.markdown("""
- **Reason for Selection**: Useful for identifying natural groupings in the dataset without prior labels, helping uncover hidden patterns in game data.
- **Insights Provided**: Helps group games based on feature similarity, which can assist in understanding game patterns and trends.
""")




st.title("Results and Discussion")
st.header("Visualizations")
st.markdown("Here is a link to our visualizations: [Midterm Visualizations](https://mlfootballproject.streamlit.app/MidtermVisualizations)")
st.header("Analysis of Quantitative Metrics:")
st.subheader("Logistic Regression")
st.markdown("""
- **Accuracy (0.9000)**: This high value means that the model was able to correctly predict the outcome of the NFL match 90 percent of the time.
- **Precision (0.8817)**: Among the games the model predicted as winners, 88.17 percent of them were actual winners, indicating relatively high precision.
- **Recall (0.88)**: The model correctly identified 88 percent of actual winners from all the games, proving its effectiveness.
- **F1-score (0.8823)**: The balance between precision and recall is 88.23 percent, showcasing great performance.
""")

# K-Means Metrics
st.subheader("K-Means")
st.markdown("""
- **Accuracy (0.67)**: The clustering algorithm properly grouped similar outcomes 67 percent of the time, showing slightly above-average performance but room for improvement.
- **Precision (0.61)**: Of the predicted clusters for winning teams, 61 percent were actual winners, indicating moderate results but needing improvement.
- **Recall (0.68)**: The model successfully captured 68 percent of all actual winning team clusters.
- **F1-score (0.64)**: The balance of precision and recall attained is 64 percent, indicating decent performance.
""")
st.header("Analysis of Algorithms/Models:")
st.subheader("Logistic Regression")
st.markdown("""
- **Description**: Logistic regression is a supervised learning model that applies a logistic function to classify a binary target variable, and it can be adapted for multiclass classification tasks.
- **Mechanism**: It calculates probabilities using the logistic function, making it effective when a linear decision boundary exists between classes.
- **Optimization**: The model’s coefficients are optimized to predict the log-odds of the target variable, assuming a linear relationship between the independent variables and the log-odds of the outcome.
""")

st.subheader("K-Means Clustering")
st.markdown("""
- **Description**: K-Means is an unsupervised learning algorithm used to partition data into a predefined number of clusters based on feature similarity.
- **Mechanism**: It minimizes variance within clusters by iteratively assigning data points to the nearest cluster center, then updating the center based on the mean of assigned points.
- **Stability**: The algorithm continues until cluster assignments stabilize, making it effective for finding natural groupings in data without prior labels.
""")
st.header("Comparative Analysis and Recommendations")
st.markdown("""
Both models produced verifiable results, with Logistic Regression having a slight edge over K-Means in terms of accuracy, precision, recall, and F1-score. The high values associated with Logistic Regression metrics suggest that it is well suited for predicting the winner of an NFL game based on the feature data provided.
""")
st.header("Why did your model perform well?")
st.markdown("""
- **Relevant Features**: The features used (passing yards, rushing yards, touchdowns, sacks, etc.) are good indicators of NFL teams’ success, allowing the models to make accurate predictions.
- **Appropriate Model Choice**: Both models are resilient classifiers that effectively manage the variability and complexity within the dataset.
""")


st.header("Next Steps")
st.markdown("""
- **Hyperparameter Tuning**: Testing and tuning the model’s hyperparameters would optimize performance, ensuring an ideal balance of accuracy, recall, and precision.
- **Feature Engineering**: Discovering and incorporating different features to enhance model accuracy and precision, such as including niche metrics.
- **Explore Additional Models**: Testing other types of models to combine results, optimize outcomes, and identify specific methods for further improvements.
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
        "Visualizations, Results & Discussions",
        "Gantt chart, Model Implementations, Data Preprocessing",
        "Model Implementations, Data Preprocessing",
        "Website, Data Preprocessing, Visualizations",
        "Results & Discussions, Visualizations",
    ]
}
df = pd.DataFrame(data)
st.table(df)


st.image("gantt2.png", caption="Current Gantt Chart for Team", use_column_width=True)
