# Clash-Royale-DSA210-Project
**Clash Royale Data Science Project Report**

# **Introduction (Motivation)**
Clash Royale is a popular real-time strategy game that requires deck-building and tactical decision-making. The objective of this project is to analyze the performance of different decks and identify key factors that contribute to winning a match. By leveraging data science methodologies, we aim to optimize deck composition, understand opponent strategies, and improve overall gameplay performance.

For this project, I will play Clash Royale **five days a week using the five most played decks**. The focus will be on analyzing match outcomes against different opponent decks and extracting insights on the most effective strategies. This study will help players make data-driven decisions when choosing their decks and card combinations.

# **Data Sources and Collection Methods**
## **Data Sources**
The data for this project will be collected from the following sources:
- **Clash Royale API**: Provides match history, player statistics, and card usage data.
- **Manual Data Logging**: Additional observations, such as in-game decisions and strategies, will be recorded manually.

## **Data Collection Process**
- The **five most played decks** will be used for ranked matches.
- Match data will be collected through Clash Royale API calls, including:
  - Deck compositions
  - Opponent decks
  - Match results (win/loss)
  - Battle durations
  - Crown counts (score)
- Data will be cleaned and structured for analysis.

# **Exploratory Data Analysis (EDA)**
To gain initial insights, the following analyses will be performed:
- **Win Rate Analysis**: Understanding which decks have the highest win rates against different opponent decks.
- **Card Performance**: Identifying which individual cards contribute most to victories.
- **Pair and Trio Synergies**: Analyzing which **two-card and three-card combinations** work best together.
- **Average Elixir Cost Impact**: Evaluating whether decks with high or low elixir costs affect performance.
- **Card Type Effectiveness**: Examining how different card types (e.g., air attack, tank, defense) influence match outcomes when used together.

### **Hypotheses**
- **H0 (Null Hypothesis)**: Deck composition has no significant impact on match outcomes.
- **H1 (Alternative Hypothesis)**: Certain deck compositions significantly increase the probability of winning.
- **H0 (Null Hypothesis)**: Average elixir cost does not affect match performance.
- **H1 (Alternative Hypothesis)**: Extremely high or low elixir costs impact match performance significantly.

# **Machine Learning Applications**
To further analyze the data, the following machine learning techniques will be applied:
- **Classification Models**: 
  - **Logistic Regression**: Predicting match outcomes based on deck composition.
  - **Random Forest**: Evaluating the importance of different features in predicting match results.
  - **Decision Tree**: Identifying key decision points that impact winning chances.
- **Clustering Analysis**:
  - **K-Means Clustering**: Grouping similar deck types and analyzing their effectiveness.
- **Feature Engineering**:
  - Encoding deck compositions into numerical representations.
  - Creating new variables such as synergy scores for two-card and three-card combinations.
- **Performance Metrics**:
  - Accuracy, Precision, Recall, F1-Score for classification models.

# **Findings and Insights**
After conducting the analysis, key insights will be summarized:
- **Effective Deck Combinations**: Identifying which deck compositions yield the highest win rates.
- **Best Card Synergies**: Determining which **pairs and trios of cards** contribute most to victories.
- **Impact of Elixir Cost**: Evaluating whether decks with extreme elixir costs (too high or too low) perform better or worse.
- **Card Type Combinations**: Understanding how different types of cards (e.g., air attack + defense, tank + spell) influence match success.
- **Opponent Deck Analysis**: Studying which deck matchups are most favorable or unfavorable.

# **Limitations and Future Work**
## **Limitations**
- **Data Completeness**: API limitations may restrict access to certain player data.
- **External Factors**: The impact of real-time in-game decision-making is difficult to quantify.
- **Sample Size**: The dataset may be limited in scope due to time constraints.

## **Future Work**
- Expanding data collection over a longer period to improve statistical reliability.
- Implementing reinforcement learning models to simulate and improve deck-building strategies.
- Analyzing the impact of in-game events and balance changes on strategy effectiveness.

# **Conclusion**
This project aims to leverage data science methodologies to analyze Clash Royale match data and extract meaningful insights for players. By identifying successful strategies, deck compositions, and card synergies, players can make data-driven decisions to enhance their gameplay. The findings will provide a foundation for future research and potential optimizations in competitive Clash Royale play.

