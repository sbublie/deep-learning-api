# Deep Learning API

## Overview
This is the implementation of an API for handling data from a Deep Learning validation pipeline. 

After starting the server, Tensorflow analyses the test batches and models. 
The metadata and results of this operation can be accessed via GET requests at the API endpoints specified in the ```.yaml``` file.


The app uses the [Connexion](https://github.com/zalando/connexion) library on top of Flask.

## Requirements
Python 3.5.2+ (Tested only on Python 3.10)

## Usage
To run the server, please execute the following from the root directory:

```
pip3 install -r requirements.txt
python3 -m openapi_server
```

and open your browser to here:

```
http://localhost:8080/ui/
```

The OpenAPI definition lives here:

```
http://localhost:8080/openapi.json
```

## Running with Docker

To run the server on a Docker container, please execute the following from the root directory:

```bash
# building the image
docker build -t openapi_server .

# starting up a container
docker run -p 8080:8080 openapi_server
```