import os
from dotenv   import load_dotenv
load_dotenv()

ENV_ENVIRONMENT = "ENVIRONMENT"
ENV_DEV = "DEV"
ENV_PRO = "PRO"

if os.environ.get(ENV_ENVIRONMENT) == ENV_DEV:
    # imports on development
    from CobraMetabolicModel import CobraMetabolicModel
else:
    # imports on release
    from findCPcore.CobraMetabolicModel import CobraMetabolicModel


def read_model(model_path, objective=None, processes=None):
    model = CobraMetabolicModel(model_path)
    if objective is not None:
        model.set_objective(objective)
    if processes is not None:
        model.processes = processes
    return model

def write_file(path, string):
    text_file = open(path, "w")
    n = text_file.write(string)
    text_file.close()

def read_file(path):
    with open(path, 'r') as file:
        data = file.read()
        return data
