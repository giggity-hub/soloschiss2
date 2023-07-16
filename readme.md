# Running Commands
All python scripts must be run as modules from the root folder
```bash
# create the training data
python3 -m stuttbard.scripts.create_data
# Run the tests
python3 -m pytest tests
```

# Running tha docker
```bash
# Train the model
source scripts/train_kbbot.sh <training-data> <model_name>
# Example:
source scripts/train_kbbot.sh kb.soloist.json model_schmodel

# Serve the model
python3 app.py <model_name>
# Example:
python3 app.py model_schmodel
```