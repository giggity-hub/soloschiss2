# Interacting
```bash
# start the docker container (if it isn't already running)
sudo docker compose up -d

# enter into the docker container
sudo docker compose exec myapp bash

# start the soloist server (inside docker bash)
python3 app.py <model_name>
# Example:
python3 app.py model_schmodel

# start the chatbot (inside local shell)
python3 -m stuttbard.chatbot.chat
```

# Training
```bash
# Generate json training data
python3 -m scripts.create_data <dataset_name>
# Example
python3 -m scripts.create_data data_schmata

# Build the Docker Image
sudo docker compose up -d --build

# Enter the Shell of the docker container
sudo docker compose exec myapp bash

# Train the model (from inside docker bash)
source scripts/train_kbbot.sh <training-data> <model_name>
# Example:
source scripts/train_kbbot.sh kb.soloist.json model_schmodel

# exit docker bash
exit

# Deactivate the Container
docker compose down
```
# Testing
```bash
# run all tests
py.test tests

# run specific test file
py.test tests/<filename>.py
```