# Sentiment Analysis Project

## Summary

This project represents a successful journey in training and evaluating sentiment analysis models, implementing a robust voting ensemble, and creating a Flask web application with these sentiment analysis models.

## Model Training and Evaluation

In this project, I successfully trained various sentiment analysis models on the IMDb movie dataset. The approach involved meticulous examination of different methods to enhance accuracy and evaluation metrics, ensuring a comprehensive understanding of model performance. To gain deeper insights, LIME was integrated, proving instrumental in interpreting and refining the models.

## Voting Ensemble Development

During the validation phase, I took the initiative to develop a custom voting ensemble comprising Naive Bayes, Random Forests, and Logistic Regression models. This involved careful implementation on the validation set, allowing for the assessment of the ensemble's accuracy and performance analysis through confusion matrices.

Upon successful validation, the ensemble was applied to a challenging test set, showcasing notable performance. Detailed comparisons were made with the results achieved by the best individual model, namely Logistic Regression. Observations were made on cases where the ensemble outperformed, highlighting instances of significant improvements in sentiment analysis compared to individual models.

## Web Application Development

Moving on to Part Two, efforts were extended to create a user-friendly web application. The Flask framework within the 2022-ca337-master repository's src folder, specifically in the "flask" directory, was explored for this purpose. The home page warmly welcomes users and provides a link to a page featuring a Naive Bayes model. This model, along with its vocabulary, accurately predicts the sentiment polarity of a sample review, such as "I love it."

Taking user experience into account, additional models, namely Random Forest and Logistic Regression, were introduced, allowing users to choose between them on the app. This enhancement broadened the application's capabilities, providing users with a more versatile sentiment analysis experience.

## Interface Improvements

Furthermore, interface improvements were made to the web app. This included cosmetic enhancements through the incorporation of external CSS files, significantly improving the app's visual appeal. Additionally, the utilization of sentiment lexicon dictionaries was explored, adopting a lexicon-based approach to classification for a more nuanced sentiment analysis.
