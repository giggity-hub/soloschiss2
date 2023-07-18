# Running Commands
All python scripts must be run as modules from the root folder
```bash
# create the training data
python3 -m stuttbard.scripts.create_data
# Run the tests
python3 -m pytest tests
```

# Commands
```bash
# Generate json training data
python3 -m scripts.create_data

# Build the Docker Image
sudo docker compose up -d --build

# Enter the Shell of the docker container
sudo docker compose exec myapp bash

# Train the model (from inside docker bash)
source scripts/train_kbbot.sh <training-data> <model_name>
# Example:
source scripts/train_kbbot.sh kb.soloist.json model_schmodel

# Serve the model (from inside docker bash)
python3 app.py <model_name>
# Example:
python3 app.py model_schmodel

# exit docker bash
exit

# Deactivate the Container
docker compose down
```