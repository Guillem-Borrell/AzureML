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
2. Install Azure Machine learning extension with `az extension add -n ml -y`
3. Create a virtual environment
4. With the latest version of pip, run `pip install -e .`
5. Install the vscode extension for azure machine learning
6. Create a workspace configuration file: https://docs.microsoft.com/en-us/azure/machine-learning/how-to-configure-environment#workspace

Now we can switch to the tutorial: https://docs.microsoft.com/en-us/azure/machine-learning/tutorial-1st-experiment-hello-world

To create a job, just run the `run-hello.py` script in the `helloworld` module.

Then you need to connect Github to Azure with this tutorial: https://docs.microsoft.com/en-us/azure/developer/github/connect-from-azure?tabs=azure-portal%2Cwindows#use-the-azure-login-action-with-a-service-principal-secret. To set up this connection, access to the Azure AD or to the service principal is required. The Github project's secret has to be updated accordingly.
