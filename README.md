## Agoda QA Assignment

Set up a test automation framework to test APIs listed here: https://github.com/lukePeavey/quotable#examples-1

## Task 1: Automation Framework Overview

A brief about the project repository structure:

- `src/` contains project helper functions and payload data being used within test scripts.
- `test_scripts/` contains test cases written using the pytest framework
- `ci_run_results/` contains snapshots to test result html report and CI pipeline results.

### Instructions to Setup locally and Run tests

- Clone the repository: `git@github.com:ernestomehra/agoda_qa.git`
- Create a virtual environment with the command: `python3 -m venv venv` on the project root.
- Activate the virtual environment by running command: `source venv/bin/activate`
- Install project dependencies: `pip install -r requirements.txt`
- Run tests (without generating reports: `pytest -v`
- Run tests (with test result generation): `pytest --html=report.html`

### CI/CD  


The project CI/CD pipeline has been set up on CircleCI to be run whenever any PR is merged to master.  For every PR 
merged, the CI pipeline is triggered on circleCI. An example run can be referred by visiting 
URL: 

`https://app.circleci.com/pipelines/github/ernestomehra/agoda_qa/17/workflows/f463f32c-53ef-49f9-9e2c-73160666bdd4/jobs/17`

This is a run that was run for a code check-in. Test results are generated under the Artifacts tab and called as `report.html`

## Task 2: API test plan

As part of the second task, an API testing plan was asked to be created. This test plan can be found at path
`agoda_qa/plans/api_test_plan.pdf`

 
