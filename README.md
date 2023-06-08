LLMCurator is a web based tool to interact with Large language model and curate training data for it.

![Demo](./demo.png)

## Key features
1. Interact with LLM- LLMCurator acts a user friendly frontend to interact with large language models. Very useful during model development.
2. Annotate data- LLMCurator turns into an annotation tool to curate training data for LLMs in just few clicks.
3. Easy to setup- The tool has been dockerized so that it can be setup in just few of commands.

## Setup
1. Install docker and docker-compose
2. Download LLMCurator
```
git clone https://github.com/pushpankar/LLMCurator.io.git
```

3. Start LLMCurator
``` 
docker-compose up
````


## Configuration
#### Host on specific port
To run the app on specific port, update the port mapping in docker-compose.yml. For example, to run the app on port 4456 update the port mapping to 
```
ports:
  - 4456:3000
```