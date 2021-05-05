# ec500-final-project: Legislator

This repository contains a web application, programmed in Python and configured using Flask, that provides up-to-date information about the United States Congress. It provides a sortable menu of all current members of Congress, each of which can be clicked on for more information. It also has a list of all recent bills that have seen action in either the Senate or House. This list is also sortable and filterable. Finally, an analytics page provides graphical data regarding where Congress members fall on the political spectrum and how this data relates to voting percentages.

## Technologies Used:
 - Flask
 - [congress-api](https://projects.propublica.org/api-docs/congress-api/)
 - [newsapi](https://newsapi.org/)
 - Python package for CI / CD using unittest and coverage


## How to run:
1) Clone the repo, navigate to it, run `pipenv shell`
2) Install dependencies with `pipenv install`
3) Then, run `flask run` and navigate to [the application](http://127.0.0.1:5000/)

## Features:
- Can list all current senators and house members; the lists are sortable and can be filtered by state and/or party.
- Can provide information about each member, such as their seniority, committees, and party line voting percentages. Graphs depicting party-line voting and where they the member lies on the political spectrum are also provided.
- Can provide 3 top headlines for each member.
- Can list all recent, active bills for senate and house. List of bills can also be sorted and filtered.
- Can provide an analytics page with various graphs depicting Congress members on the political spectrum.
