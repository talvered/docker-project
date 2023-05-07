Kashrag's Docker project.

1. Create a directory called "Docker-project" under home directory
2. Create a Flask web app
2.1 Create the following python script called app.py
from flask import Flask

app = Flask(__name__)

@app.route('/directeam', methods=['GET'])
def hello_world():
    return "I'm alive!"

@app.route('/')
def display_error():
    return "Error! Wrong request"

3.Create the following Dockerfile
FROM python
COPY ./app.py .
EXPOSE 8080
RUN pip3 install -U Flask
CMD flask run --port=8080

4. Build the docker image:
docker build -t webapp:testing2 .

5. Run the webapp container:
docker run -it --name testing -p 8080:8080 webapp:testing2

6. In order for the webapp to be accessible from the container, ports in the Rancher Desktop need to be opened.
...
