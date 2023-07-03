from sqlmesh

# Create an instance of the SQLMesh class
mesh = SQLMesh(config_path='config.yaml')

# Define the model
model_name = 'full_model'

# Run the model
mesh.run_model(model_name)
