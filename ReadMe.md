# Marvel Comics Analysis

Here lies a program that takes Marvel Comics data and creates data structures that compile elements for analysis. 

marvel_comics.py find a random marvel comics characters and presents some facts on that character. There is room to make this interactive or a simple Api that gets character information. Another idea is to make generate a storyline from the information. 

get_data.py loads the data from a csv file. 

model_build.py builds a RandomForestClassifer that determines whether or not a character should have blue eyes or not. The F1 score of this classifier is .82, its recall score is .98. 

server.py is a simple flask app that runs in a docker container. 

To run the docker container run these lines :
    docker build -t test_ml_api .  
    docker run --rm -p 5000:8080 test_ml_api

to run the blue eyes app in a new terminal, run:
    curl -X POST -H 'content-type:application/json' --data '{"id": 4325 }' http://127.0.0.1:5000/api

where "id" is the id of a marvel character in the "UNKNOWN eye color dataset". If "id" fails, a random id will be generated and a prediction on that character will return. 

--------------------

In the notebooks folder there are two jupyter notebooks that do more in depth analysis on the dataset. One is focused on queer characters. The other is prep-work for some machine learning on whether or not a given marvel character will have blue eyes, based on some features. 

In the images folder, there are any graphs and plots generated from the data. Most of that code is reproducible and primed to adapted for other uses.

Overall, this repo hope to showcase various technical abilities and point out some quirks of the marvel universe: not enough queer characters and too many characters with blues eyes (a third of known marvel characters have blue eyes). 

There were some interesting quirks with the data and I can talk more about how I worked around missing values and thoughts for future use of the data.  
