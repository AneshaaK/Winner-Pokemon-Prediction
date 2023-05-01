# Winner-Pokemon-Prediction
<img width="576" alt="image" src="https://user-images.githubusercontent.com/131211098/235377790-ca4eea88-eec6-44a5-b4fc-9a1a64c64927.png" class="center">

This project aim is to use machine learning for predicting the winner of Pokémon among player choices. Potential audiences are the general public interested in playing the game and company management.

### Project Plan:
<img width="804" alt="image" src="https://user-images.githubusercontent.com/131211098/235377666-7beefd40-293a-45ec-aaab-ad0389f4fbfa.png">

### Machine Learning Project Phases:
- Data Collection: 
  - Pokemon and Battles dataset from Kaggle
- Data Exploration: 
  - Data Quality (Categorical and Continuous features)
  - Box plots, Bar plots and Histograms
  - Correlation Matrix
- Data Preprocessing:
  - Join csv files
  - Replace null values to NONE
  - Transformed to desired format
  - Normalize required features
  - Feature hashing
- Data Preparation:
  - Split training and testing data into 75% and 25% respectively
- Data Modeling:
  - 10-fold Cross Validation for Model selection
  - Trained Models:
    - Decision Tree
    - Random Forest
    - SVM
    - Logistic Regression
    - ADA Boost
- Evaluating using metrics such as Accuracy score, Confusion matrix and Area Under Curve (AUC) 
- Parameter tunning using RandomSearchCV
- Live Demo

### Conclusion
The accuracy of this model exceeds 95% when both Pokémon names are inputted into the function. We used PyTorch library to build out this functionality into a small Python function, which can be saved locally and called upon whenever needed. While our goal was to create a tool that assists Pokémon Go players in determining whether they will win a battle against a peer. While our current tool is limited to running within a Python environment, we plan to develop a small executable with a basic user interface that can even run on a mobile environment in the future.Moreover, our model only considers the base stats of the Pokémon, but they also have individual statistics called IVs (individual values) that can impact the battle's outcome. By incorporating IVs into the model, we can expect an accuracy of over 99%, since the battle's outcome is highly dependent on them. Therefore, we can further improve our model's accuracy by allowing input of more than just the Pokémon names, but also the IVs.

### Contributors
Aneshaa Kasula, Viritha Vanama, Andrew Kehl  and Harshini Gadige
