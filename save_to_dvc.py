from yaml import safe_load 
from os.path import join
import os

# Get DVC Credentials 
dvc_config = safe_load(open("params.yaml"))["dvc_config"]
DVC_REMOTE_URL = dvc_config["https://dagshub.com/ravikirankiran097/GithubActionsMLOps.dvc"]
USERNAME = dvc_config["ravikirankiran097"]
PASSWORD = dvc_config["a6218961dad1404d4865c8400c5535c1a8cd103d"]

# Data Path 
meta_data = safe_load(open("params.yaml"))["model_data_config"]
DATA = meta_data["DATA_PATH"]
VECTOR = meta_data["VECTOR_PATH"]
MODEL = meta_data["MODEL_PATH"]

# Configure DVC
os.system("dvc remote add origin {DVC_REMOTE_URL}")
os.system("dvc remote modify origin --local auth basic")
os.system("dvc remote modify origin --local user {USERNAME}}")
os.system("dvc remote modify origin --local password {PASSWORD}")

# Add Model Metadata to DVC
os.system("dvc add {DATA} {VECTOR} {MODEL}")
os.system("dvc push")