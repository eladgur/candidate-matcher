# Matcher Project

## Dep's versions:
* python: 3.6.8
* django: 3.1.7

## Running Instructions

* cd into project root folder
* `source newenv/bin/activate`
* `pip install -r requirements.txt`
* `python manage.py migrate`
* `python manage.py test matcher`

## Notes:
* This is a core and minimal implementation of candidate matching algorithm for the web app
* I assumed that not routes or REST API should be exposed
* Logic tested by tests in the matcher tests file

## Possible Improvements / not tested
* Consider skill level for scoring* expose REST API for create and update of all entities
* expose endpoint for the candidate matcher util (by job id)
* I didn't handle or tested all edge cases, possible failures can be:
    * no results for a job/skills/candidates or handling such case (it should raise some error or stuff
    
### Author: Elad Gur