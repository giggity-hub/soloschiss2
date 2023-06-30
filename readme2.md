# Setup
### Install Dependencies
- Do a Fresh install of Ubuntu 18.04.06
- sudo apt-get install curl python-dev python3-dev python3-pip
---
- pip3 install --upgrade pip
- pip3 install -r requirements.txt
---
- cd soloist
- (download the gtg_pretrained.tar.gz file into this folder)
- tar -xvf gtg_pretrained.tar.gz
---
- curl -fsSL https://deb.nodesource.com/setup_16.x | sudo -E bash
- sudo apt-get install -y nodejs
- cd html
- npm install

### Install NLTK Package
- `python3`
- `import nltk`
- `nltk.download('punkt')` 
- `exit()`

### Some small Code Fixes
Go to line 122 in `examples/knowledgebasebot/kbbot_server.py` and add the workdir to the path
```
if __name__ == "__main__":
    # Add these two lines
    import sys
    sys.path.insert(0, '../..')
```
---
Go to line 87 in `soloist/html/src/components/chat.vue` and replace the ip adress in the request with `0.0.0.0:8081`
```
axios({
        method: 'POST',
        url: 'http://0.0.0.0:8081/generate',
        data: {'msg':this.all_data},
        
    })
```
# Train the Model
- alias python=/usr/bin/python3.6
- cd examples/knowledgebasebot
- python3 convert_rasa.py
- cd ../../soloist
- source scripts/train_kbbot.sh

# Interact with the Model
### Backend
- cd examples/knowledgebasebot
- python3 kbbot_server.py
### Frontend
- cd soloist/html
- npm run serve