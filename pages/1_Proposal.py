import streamlit as st

st.set_page_config(
    page_title="NFL Prediction Model Proposal"
)

st.title("Potential Results and Discussion")

# Quantitative Metrics Section
st.header("Quantitative Metrics")
st.write("""
The performance of our models will be evaluated using the following metrics:
1. **Accuracy**: Measures how often the model correctly predicts the winning team. A higher value (closer to 1) indicates better overall performance in predicting the correct outcome.
2. **Precision**: Focuses on the ratio of correctly predicted wins to the total number of predicted wins. A higher precision means fewer false positives (incorrect win predictions).
3. **F1 Score**: Balances precision and recall, giving insight into the model’s ability to avoid both false positives and false negatives. A higher F1 score indicates better balance between identifying wins and minimizing incorrect predictions.
""")

# Project Goals Section
st.header("Project Goals")
st.write("""
- **Create an interpretable model** that provides accurate insights for NFL analysts and sports enthusiasts:
    - **Accuracy > 0.7**
    - **Precision > 0.75**
    - **F1 Score > 0.75**
- **Design an efficient model** that maximizes computational efficiency by using methods such as logistic regression and K-means clustering.
""")

# Overall Expectation Section
st.header("Overall Expectation")
st.write("""
Achieve a reliable, interpretable, and accurate model for predicting which NFL team is likely to win a game.
""")
