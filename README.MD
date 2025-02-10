### Prerequsites
It is important to have the Allure installed before viewing the test results.
run  
```npm install -g allure-commandline --save-dev``` to install allure cli.

### Steps to run the tests
1. clone the repo
2. install the packages by running pip install -r requirements.txt --user at the root folder
3. execute python -m pytest -s

### Framework
#### env vars arrangement
This framework is set to run locally, in an environment, and by the CI/CD pipeline. test run data like base url, headless execution and browser type are fed through the .env file. These vars would be consumed from the env vars fed by the pipeline during pipeline test runs. 
manual runs can have these data in the .env or pytest.ini or config.toml files. This is the fallback options order. 
#### BDD
1. BDD is implemented using pytest-bdd
2. Scenario Outline enables multiple input and output files to be used seamlessly
#### Reports
To generate the allure report run ```allure serve reports/allure-results```. This file path is added in the pytest.ini. This can be overridden by giving a different path with the run command. e.g ```python -m pytest  --alluredir=reports/allure-results -s```

## Limitations 
Using the prod systems of motorway.co.uk and webuyanycar.com found some rate limiting and automatically sensing the emails used repeatedly by the systems. 
Ability to build a framework, using BDD in the framework, and reading and working with files can be asses using many other ways. 

