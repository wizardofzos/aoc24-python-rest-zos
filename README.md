# AOC 2024 on z/OS


Based on  https://github.com/wizardofzos/flask-rest-zos/

## What's this?

Repo for my solutions to Advent of Code. More info: https://adventofcode.com/2024
Wanted to have some extra practice on flask-rest and also do some REXX, some python and maybe some COBOL. 

So I've made this REST API that either runs python code, COBOL or REXX and shows the result...


## Requirements

- Python available
- Network connectivity to the outside world    

If you need python on your z/OS system, just follow the EPLS installer guide via https://www.ibm.com/docs/en/python-zos/3.10?topic=configuration-installing-configuring-pax-format.
Don't let the hardware requirements fool you, it will run on your ZPDT/ZD&T environment without any issues.

## Preparing for first run

    git clone git@github.com:wizardofzos/aoc2024.git
    cd aoc2024
    python -m venv .
    . bin/activate  
    pip install --upgrade pip
    python -m pip install -r requirements.txt

## Running it 

    cd /path/to/the/thing
    . bin/activate
    # Optional if you want another port than 12345
    export PORT=<port-you-want>
    python aoc.py

## Get it without my solutions

If you want to work with this, and not have my solutions in, make sure to checkout the 'no-solutions' branch

Then point your browser to http://<ip_or_dns_of_your_mainframe>:12345/swagger-ui and...


       
    
## Adding endpoints to the REST-API

Every endpoint has it's own file in /endpoints. 

If you want to do REXX, copy the rexx.py endpoint for that day (copy it to rexxd01p1.py for instance).
Make sure to change the class name to REXXD01P1 (or other) and include that in you aoc.py
(see the comments in the `endpoints/__init__.py` and `aoc.py`)

Also make sure to add the new classes to `endpoints\__init__.py`

Then the rexx also needs to be stored in the `rexxes` folder. (change path to where you store your rexxess in `constants/__init__.py`)