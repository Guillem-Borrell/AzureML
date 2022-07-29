# Azure Machine Learning devops

This repository contains code and notes about how to do decent devops with Azure Machine Learning. This is an experiment executed before the final client engagement, that wanted us to guide them to make data scientists productive in this managed setup.

I've created a free tier subscription in Azure with the following components:

* Azure Machine Learning
* Azure Container Registry
* Azure Key Vault
* Azure Storage Account
* Azure Application Insights

On the local machine

1. Clone the repo
2. Create a virtual environment
3. With the latest version of pip, run `pip install -e .`
4. Create a workspace configuration file: https://docs.microsoft.com/en-us/azure/machine-learning/how-to-configure-environment#workspace
5. To create a job, execute the `helloworld-script` that will be installed in the environment as part of the package installation.

This repo also includes a Github pipeline that tries to log into the azure subscription.

To connect Github to Azure with this tutorial: https://docs.microsoft.com/en-us/azure/developer/github/connect-from-azure?tabs=azure-portal%2Cwindows#use-the-azure-login-action-with-a-service-principal-secret. To set up this connection, access to the Azure AD or to the service principal is required. The Github project's secret has to be updated accordingly.
