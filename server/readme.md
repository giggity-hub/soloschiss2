# Setup
- You need to have Docker installed. The easiest way is to install it through docker desktop
- place the `gtg_pretrained.tar.gz` inside the `server` folder

# Building the docker image
```bash
# Build the Image and launch container
# the -d indicates detached mode, which means it will not occupy your shell
# Add --build to make sure it really rebuilds from local files and not cache
sudo docker compose up -d

# Enter the shell of the docker container
docker compose exec myapp bash

# Launch the server. It will listen for get requests on http://127.0.0.1:800/
cd examples/knowledgebasebot
python3 kbbot_server.py
```
# Querying the Server
To test the Server i'd advise you to install an API debugger (like Insomnia).
A call to the endpoint from python could look like this
```python
import requests

url = "http://localhost:8000"
#The payload is a json object with a history field
data = {"history": ["user: Show me some italian restaurants"]}
# The headers will be set automatically by your API debugger
headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
r = requests.post(url, data=json.dumps(data), headers=headers)
# df = domain['restaurant'].query('cuisine == "italian"') ; names = df['name'].tolist()system : Sure, here are some italian restaurants {templates.list({names})}
```
# Stopping the Server
- hit `ctrl + C` to stop the flask server
- type `exit` or hit `ctrl + D` to leave the interactive docker shell
- stop the container by running `docker compose down` (optional)
# Training the model
Not yet supported, working on it
```bash
cd soloist
source /scripts/train_kbbot.sh
```