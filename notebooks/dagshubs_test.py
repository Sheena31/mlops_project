import dagshub
import mlflow
dagshub.init(repo_owner='sheenatks', repo_name='mlops_project', mlflow=True)
mlflow.set_tracking_uri("https://dagshub.com/sheenatks/mlops_project.mlflow ")

with mlflow.start_run():
  mlflow.log_param('parameter name', 'value')
  mlflow.log_metric('metric name', 1)