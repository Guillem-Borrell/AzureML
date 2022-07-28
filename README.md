# Azure Machine Learning devops

This repository contains code and notes about how to do decent devops with Azure Machine Learning. This is an experiment executed before the final client engagement, that wanted us to guide them to make data scientists productive in this managed setup.

I've created a free tier subscription in Azure with the following components:

* Azure Machine Learning
* Azure Container Registry
* Azure Key Vault
* Azure Storage Account
* Azure Application Insights

On the local machine

1. Install az command with `choco install azure-cli`
2. INstall Azure Machine learning extension with `az extension add -n ml -y`
3. Create a virtual environment
4. Install azure Machine learning sdk with `pip install --upgrade azureml-core`
5. Install the vscode extension for azure machine learning
6. Create a workspace configuration file: https://docs.microsoft.com/en-us/azure/machine-learning/how-to-configure-environment#workspace
7. Add the config.json file to .gitignore

Now we can switch to the tutorial: https://docs.microsoft.com/en-us/azure/machine-learning/tutorial-1st-experiment-hello-world

