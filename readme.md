# Prerequisites
- Docker Installation
- Python 3
- Unzip the pretrained soloist model inside the soloist folder as `soloist/gtg_pretrained`
- Unzip all models you wish to use in the /models folder

# Training

Note: Sample train and test data is provided in the `data` folder. 

```bash
# Build the Docker Image
sudo docker compose up -d --build

# Enter the Shell of the docker container
sudo docker compose exec myapp bash

# Train the model (from inside docker bash)
source scripts/train_kbbot.sh <training-data> <model_name>
# Example:
source scripts/train_kbbot.sh data/final_train.json model_schmodel

# exit docker bash
exit

# Deactivate the Container
docker compose down
```

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

# Evaluating
```bash
# generate the predictions (the server should be started)
python3 -m evaluation.save_test_results <test-data>
# Example:
python3 -m evaluation.save_test_results data/final_test.json

# evaluate the predictions
python3 -m evaluation.eval <predictions-file>
# Example:
python3 -m evaluation.eval data/finaL_test_out.json
```

# Testing
```bash
# run all tests
py.test tests

# run specific test file
py.test tests/<filename>.py
```
