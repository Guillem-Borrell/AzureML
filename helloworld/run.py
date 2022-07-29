from pathlib import Path
from azure.ai.ml import MLClient, command
from azureml.core import Workspace, Experiment
from azure.identity import DefaultAzureCredential

import helloworld


def test_job():
    base_path = Path(helloworld.__file__).parent
    config = base_path / "config.json"
    print(config.resolve())

    ws = Workspace.from_config(config)
    default_azure_credential = DefaultAzureCredential()

    ml_client = MLClient(
        default_azure_credential, ws.subscription_id, ws.resource_group, ws.name
    )

    experiment = Experiment(ws, "test_experiment")

    # Assumes a previously created compute cluster
    compute_name = "compute-cluster"

    job = command(
        code=base_path / "src",
        command="python hello.py",
        environment="AzureML-sklearn-1.0-ubuntu20.04-py38-cpu@latest",
        compute=compute_name,
        display_name="hello-world-example-1",
        experiment_name=experiment.name,
    )

    returned_job = ml_client.create_or_update(job)
    print(returned_job.studio_url)
