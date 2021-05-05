# ec500-final-project: Legislator

This repository contains a web application, programmed in Python and configured using Flask, that provides up-to-date information about the United States Congress. It provides a sortable menu of all current members of Congress, each of which can be clicked on for more information. It also has a list of all recent bills that have seen action in either the Senate or House. This list is also sortable and filterable. Finally, an analytics page provides graphical data regarding where Congress members fall on the political spectrum and how this data relates to voting percentages.

## Technologies Used:
 - Flask
 - [congress-api](https://projects.propublica.org/api-docs/congress-api/)
 - [newsapi](https://newsapi.org/)
 - [Images of Congress](https://github.com/unitedstates/images)
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

## Screenshots:

Below are images of the web application while it's being used.

### Home Page

![](https://github.com/mdamschroder/ec500-final-project/blob/main/images/home.PNG?raw=true)

### Congress Members

This is the top of the list of current members that is provided when you select the "Current Congress" option from the home screen.

![](https://github.com/mdamschroder/ec500-final-project/blob/main/images/members_default.PNG?raw=true)

Congress members can be filtered and sorted. You can filter by party and/or state. Sorting options include sorting by: last name, party, age, percentage of votes along party line, percentage of votes missed, and seniority. The image below depicts the members list after it has been filtered by state (PA) and sorted by age. 

![](https://github.com/mdamschroder/ec500-final-project/blob/main/images/members_filtered.PNG?raw=true)

### Member Page

Clicking on a Congress member's name takes you to a page with more information about that member. Note: Screenshots below are taken from two different member pages (Alexandria Ocasio-Cortez and Cory Booker).

![](https://github.com/mdamschroder/ec500-final-project/blob/main/images/member_1.PNG?raw=true)
![](https://github.com/mdamschroder/ec500-final-project/blob/main/images/member_2.PNG?raw=true)
![](https://github.com/mdamschroder/ec500-final-project/blob/main/images/member_3.PNG?raw=true)
![](https://github.com/mdamschroder/ec500-final-project/blob/main/images/member_4.PNG?raw=true)

### Recent Bills

Selecting the "Recent Bills" option on the home screen will take you to a list of the 20 most recently acted upon bills in the House and Senate. 

![](https://github.com/mdamschroder/ec500-final-project/blob/main/images/bills.PNG?raw=true)

The lists can be filtered by the party that introduced them and sorted by latest major action date, party, committee, or date introduced. The list below has been sorted by committee.

![](https://github.com/mdamschroder/ec500-final-project/blob/main/images/bills_house_sorted.PNG?raw=true)

### Analytics

Selecting the "Analytics" button on the home screen takes you to the analytics page where graphical data about all Congress members and their place on the political spectrum is displayed.

![](https://github.com/mdamschroder/ec500-final-project/blob/main/images/analytics_1.PNG?raw=true)

![](https://github.com/mdamschroder/ec500-final-project/blob/main/images/analytics_2.PNG?raw=true)

