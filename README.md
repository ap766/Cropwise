# Cropwise

## Problem Statement: Enhancing Agricultural Productivity and Decision-Making through an Integrated Agricultural Portal
In the rapidly evolving agricultural landscape, there is a critical need for a comprehensive and user-friendly agricultural portal that leverages data analytics, predictive modeling, and real-time information to empower farmers, researchers, advisors, and businesses to make informed decisions.

## Solution: 
We have built a portal that provides:-
* Crop prediction based on weather and soil conditions(uses supervised learning ml algorithm)
* Graph generator for studying different factors across crops
* Information about crops including fertilizers
*  A customer support chatbot.

In the future we plan to further enhance its utility and impact, the portal aims to incorporate additional features such as a robust pest and disease management system leveraging real-time data and image recognition, market insights tool to offer actionable data for optimized supply chains and pricing strategies.Other tools for Sustainability like an assessment tool for environmental impact, intuitive dashboard and integrated seed purchasing simplify operations. With Natural Language Processing, chatbot offering personalized assistance in local languages and responds to voice commands. To encourage diversification, a predictive model suggesting secondary crops. Through innovation, we would shape a resilient and sustainable future for global agriculture."

The enhanced agricultural portal will serve as a one-stop solution for stakeholders across the agricultural spectrum. Farmers will make well-informed decisions on crop selection, resource allocation, and pest management. Researchers and advisors will access valuable insights for studies and recommendations. Agricultural businesses will optimize supply chains and respond to market trends. Policy makers will have access to data for informed regulatory decisions. Consumers will benefit from transparent information about food sources. Ultimately, the portal's impact will extend to enhancing agricultural productivity, sustainability, and resilience in the face of changing conditions.

## Tech Stack
* Frontend - HTML,CSS,Javascript
* Backend - Flask Framework (Python)
* ML - Python

## ML Model 
We used Logistic Regression , Decision Trees and Random Forest to train our model.
We got a maximum accuracy of 99.3 percent using Random Forest
However,in the future we would use more metrics to determine the best fitting algorithm for this purpose and all train our model using other algorithms like KNN, XGBoost ,etc

## OUTPUT

### 1. Home Page
![f2](https://github.com/ap766/Cropwise/assets/79255079/3c5b76a8-6b84-4ff4-b78b-e13ca56f90c5)
### 2. About Page
![about](https://github.com/ap766/Cropwise/assets/79255079/25c94a27-1d66-4cb4-beac-167984797786)
### 3. Crop Predictor - Input Values of N,P,K,Rainfall,Temperature,PH of Soil,Humidity And a pop up Appears with Predicted Crop and details about it.
![q2](https://github.com/ap766/Cropwise/assets/79255079/9c683ff0-1522-4bba-a687-148ea3e37445)

![croppred](https://github.com/ap766/Cropwise/assets/79255079/4c35e2af-17e7-49b7-b386-b1e6cf9da81b)
### 4.Graph Predictor - Select N/P/K/Rainfall/Temperature/PH/Humidity and a graph is created showing the relationship using Seaborn Library.
![graph1](https://github.com/ap766/Cropwise/assets/79255079/b56da592-b4e7-4e70-8a90-c665aa6089f1)

![graph](https://github.com/ap766/Cropwise/assets/79255079/d0720bd3-07cb-4698-8319-0b02ab837fb1)
### 5.Customer Support Chatbot - Has been created using a nocode tool for the time being , we will guide users on how to use our website
![q1](https://github.com/ap766/Cropwise/assets/79255079/077f8c21-3873-4fe4-8dd7-513c61ecf282)

## RUN THE PROGRAM
run `python model.py ` to train our model.
run `python app.py ` to run our flask application.
It will be up and running!


