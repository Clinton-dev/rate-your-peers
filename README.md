# Rate-your-peers
An application like [Awwards](https://www.awwwards.com/). The application allows users to post a project that they have created and get it reviewed by their peers. The users can:

1. View posted projects and their details
2. Post a project to be rated/reviewed
3. Rate/ review other users' projects
4. Search for projects
5. View projects overall score
6. View my profile page

### Screenshot
![](./screenshot.png)


## Getting Started

- Clone this repository to your computer. `git clone https://github.com/Clinton-dev/rate-your-peers.git`
- Open terminal command line then navigate to the root folder `cd rate-your-peers`
- Create virtual environment `python3 -m venv --without-pip <virtual environment name>`
- Run your virtual environment `source <virtual environment name>/bin/activate`
- Install Django in your environment `python -m pip install Django`
- Install other extensions required for the app to run `pip install -r requirements.txt`
- requirements.txt is in the root folder
- Run `python manage.py runserver`

### Prerequisites

Django requires Python and you can install python for your specific operating system by following this documentation [Python download](https://www.python.org/downloads/)

## API END POINT
Here are a list of the available endpoints:
1. For the general over view: `https://rate-your-peers.herokuapp.com/api/`
2. For list of projects: `https://rate-your-peers.herokuapp.com/api/project-list/`
3. For individual project details: `https://rate-your-peers.herokuapp.com/api/project-detail/<str:pk>/`
4. For deleting an individual project: `https://rate-your-peers.herokuapp.com/api/project-delete/<str:pk>/`


## Running the tests

Run test using the following command

1. For projects app: ```./manage.py test projects```
1. For users app: ```./manage.py test user```

## Deployment

Follow this resource if you want to deploy the app [deployment](https://github.com/bernie-haxx/Deployment_to_heroku_django)

## Built With

* [Django 4.0.4](https://docs.djangoproject.com/en/4.0/) - Backend framework used
* [Django Rest Framework 3.13.1](https://www.django-rest-framework.org/topics/documenting-your-api/) - Rest framework used
* [Bootstrap 5.2 ](https://getbootstrap.com/docs/5.2/getting-started/introduction/) - frontend framework

### Link to Live Site
[Link to live site](https://rate-your-peers.herokuapp.com/)

## Author

* **Clinton Wambugu** - *Initial work* - [Clinton-dev](https://github.com/Clinton-dev)


## copyright & License Info
MIT Copyright (c) 2022 Clinton Wambugu

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

