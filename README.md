# AWS_Group_Project_B5
Private repo containing all the code used for the AWS Group Assignment - MiBA Section B 2022/2023.
Here is a brief explanation of the content of each file. The code have been commented in detail, thus further technical explanations can be found in the respective files.

- Sagemaker_notebook_FINAL_demand contains the Jupyter Notebook used in the Notebook instance of Sagemaker to fit and deploy the model used for Demand Forecasting
- Sagemaker_notebook_FINAL_price contains the Jupyter Notebook used in the Notebook instance of Sagemaker to fit and deploy the model used for Price Forecasting
- Visualization_Demand contains the Jupyer Notebook used to locally visualize the insights after running some predictions with the previously deployed model (Demand Forecasting)
- Visualization_Price contains the Jupyer Notebook used to locally visualize the insights after running some predictions with the previously deployed model (Price Forecasting)
- downloadbucketdemand contains the Jupyter Notebook used to downloads the demand prediction csv from the S3 bucket (also runs the naive verions of the Streamlit app related to the predictions of the Demand Forecasting Model).
- downloadbucketprice contains the Jupyter Notebook used to downloads the price prediction csv from the S3 bucket (also runs the naive version of the Streamlit app related to the predictions of the Price Forecasting Model).
- finalselectmonth contains the script to run a Demand Forecasting interactive Streamlit app.
- pricepercitymonth contains the script to run a Price Forecasting more flexbile Streamlit app.
- lambda function example contains a skecth script to leverage and call the trained model endpoints. NB: It has not been tested!
