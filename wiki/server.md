* gunicorn http://gunicorn.org/
* flask http://flask.pocoo.org/
* (nginx)

#installing the server
## Mac os

### for starters
clone/pull the iOS_vote project

`$ cd project_location`

`$ git clone https://github.com/TheTwon/iOS_vote.git`

### installing Homebrew 
You need to get [homebrew](http://brew.sh/) installed for easy package management.
To install home brew type in your termial:

`ruby -e "$(curl -fsSL https://raw.github.com/mxcl/homebrew/go/install)"` 

### installing virtualenv
> [virtualenv](https://pypi.python.org/pypi/virtualenv) is a tool to create isolated Python environments.

To install virtualenv just type in your terminal:

`
$ sudo pip install virtualenv
`

### creating the project's virtualenv

First, you'll want to create a folder to contain your virtualenv:

`
$ cd
`

`
$ mkdir .virtualenv/poll_app
`

then to create the virtualenv:

`$ virtualenv .virtualenv/poll_app`

to activate the virtualenv:

`$ source .virtualenv/poll_app/bin/activate`

your prompt should look something like this:

`(poll_app)$`

### updating the virtualenv

here are the required packages:
<pre><code>
Flask==0.10.1
Jinja2==2.7.1
MarkupSafe==0.18
MySQL-python==1.2.4
Werkzeug==0.9.4
argparse==1.2.1
distribute==0.6.34
gunicorn==18.0
itsdangerous==0.23
wsgiref==0.1.2

</code></pre>

if you have the up to date requirements.txt file (iOS_vote/requirements.txt):

`$ pip install -r requirements.txt`

to check if all the packages are correctly installed type in:

`$ pip freeze`

you should get the following result:

<pre><code>
(poll_app)computer:~ user$ pip freeze
Flask==0.10.1
Jinja2==2.7.1
MarkupSafe==0.18
MySQL-python==1.2.4
Werkzeug==0.9.4
argparse==1.2.1
distribute==0.6.34
gunicorn==18.0
itsdangerous==0.23
wsgiref==0.1.2

</code></pre>

if MySQL-python does not install properly you may want to [try](http://stackoverflow.com/questions/17599830/installing-mysql-python-on-mac):

`$ pip uninstall MySQL-python`

`$ brew install mysql`

`$ pip install MySQL-python`

you can also manually install a package using:

`$ pip install my-package`


## Linux

The procedure is very much the same as mac os:

### for starters
clone/pull the iOS_vote project

`$ cd project_location`

`$ git clone https://github.com/TheTwon/iOS_vote.git`

### installing virtualenv
> [virtualenv](https://pypi.python.org/pypi/virtualenv) is a tool to create isolated Python environments.

To install virtualenv just type in your terminal:

`
$ sudo pip install virtualenv
`

### creating the project's virtualenv

First, you'll want to create a folder to contain your virtualenv:

`
$ cd
`

`
$ mkdir .virtualenv/poll_app
`

then to create the virtualenv:

`$ virtualenv .virtualenv/poll_app`

to activate the virtualenv:

`$ source .virtualenv/poll_app/bin/activate`

your prompt should look something like this:

`(poll_app)$`

### updating the virtualenv


First of all you should try and install MySQL-python [manually](http://stackoverflow.com/questions/5486122/installing-mysql-python-via-pip-virtualenv-for-python-2-5-on-a-linux-system-wit):

`$ aptitude install python2.5-dev`

`$ pip install MySQL-python`

Now on to the next step: 

Here are the required packages:
<pre><code>
Flask==0.10.1
Jinja2==2.7.1
MarkupSafe==0.18
MySQL-python==1.2.4
Werkzeug==0.9.4
argparse==1.2.1
distribute==0.6.34
gunicorn==18.0
itsdangerous==0.23
wsgiref==0.1.2

</code></pre>

if you have the up to date requirements.txt file (iOS_vote/requirements.txt):

`$ pip install -r requirements.txt`

to check if all the packages are correctly installed type in:

`$ pip freeze`

you should get the following result:

<pre><code>
(poll_app)computer:~ user$ pip freeze
Flask==0.10.1
Jinja2==2.7.1
MarkupSafe==0.18
MySQL-python==1.2.4
Werkzeug==0.9.4
argparse==1.2.1
distribute==0.6.34
gunicorn==18.0
itsdangerous==0.23
wsgiref==0.1.2

</code></pre>



you can also manually install a package using:

`$ pip install my-package`

# setup database

the database system used for this project is [mysql](http://www.mysql.com/).
Don't forget to update the database after a pull request.
The database file can be found here `iOS_vote/db/<dd>-<mm>-<yy>.sql`

Don't forget to launch mysql.

# launch server


`
$ cd iOS_vote/server 
`

launch the server with http:

`
$ gunicorn -w3  flask_test:app -b 0.0.0.0
`


launch the server with https:

`
$ gunicorn -w3 --certfile=../cert/key-cert.pem --keyfile=../cert/key.pem flask_test:app -b 0.0.0.0
`

swell!
