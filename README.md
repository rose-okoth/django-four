# Project Name

HoodWatch
​
# Project Description

An application that allows you to be in the loop about everything happening in your neighborhood. From contact information of different handyman to meeting announcements or even alerts. 

# Author(s) Information

> Rose Okoth.
​
# Screenshots

[Alt text](media/Screenshot.png?raw=true "Landing Page")


# BDD

* Users should be able to:
    - Sign in to the application to start using it.
    - Set up a profile which contains:
        - My name 
        - My location 
        - My neighborhood name 
    - Find a list of different businesses in my neighborhood.
    - Find Contact Information for the emergency services (health department, fire department, and Police authorities) near my neighborhood.
    - Create Posts that will be visible to everyone in my neighborhood.
    - Change My neighborhood when I decide to move out.
    - Users can only belong to one neighborhood at a time.
    - Only view details of a single neighborhood.

* The system administrator should be able to:
    - Create neighborhoods.
    - Delete neighborhoods.
    - Edit neighborhood information.
    - See all users.
    - Change user statuses: Either from neighborhood admin to regular user, or the opposite.
    - Remove users.

* A neighborhood admin should be able to:
    - Add information about neighborhoods for example: Add businesses, health care centers, police stations, etc.
    - Perform all the operations of a normal user


# Setup Instructions

1. Clone the repo:
   * `git clone https://github.com/rose-okoth/django-four.git`
​
1. Switch into the directory:
   * `cd django-four`
​
# Running the Application

1. Create the virtual environment
   * ` $ python3 -m venv venv `
   * ` $ source venv/bin/env `

1. Installing dependencies
   * ` $ pip install -r requirements.txt`

1. Setting up the database
    * `$ setup your database`
    * `$ python3 manage.py makemigrations`
    * `$ python3 manage.py migrate`

1. To run the application, in your terminal:
    * `python3 manage.py runserver`

# Testing the Application

1. To run the tests for app:
    * `$ python3 manage.py test`

# API Endpoints

* [http://boonwatch.heroku.com/api/hoods/](http://boonwatch.heroku.com/api/hoods/)
* [http://boonwatch.heroku.com/api/view_hoods/](http://boonwatch.heroku.com/api/view_hoods/)
    
# Technologies Used

* Python3.
* Django.
* HTML.
* Bootstrap.
* JS.
* JQuery.
* CSS.
​
# Contact Information

* Email: [Email](mailto:okoth.rose0@gmail.com)
* Phone number: [Phone](tel:+254712476547)
​
# License and Copyright Information
​
Copyright(c) 2021 - Rose Okoth.  
​
Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
​
The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
​
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
​
Reference: [MIT License](https://opensource.org/licenses/MIT)