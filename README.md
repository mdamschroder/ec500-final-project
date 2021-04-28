# ec500-final-project: Legislator

## Technologies Used:
### - Flask
### - [congress-api](https://projects.propublica.org/api-docs/congress-api/)
### - [newsapi](https://newsapi.org/)
### - Python package for CI / CD using unittest and coverage


## How to run:
1) Clone the repo, navigate to it, run `pipenv shell`
2) Install dependencies with `pipenv install`
3) Then, run `flask run` and navigate to [the application](http://127.0.0.1:5000/)

## Features:
- Can list all current senators and house members
- Can provide information about each member, such as their seniority, committees, and party line voting percentages
- Can provide 3 top headlines for each member
- Can list all recent, active bills for senate and house
