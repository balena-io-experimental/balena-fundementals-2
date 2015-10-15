# Basic tutorial 2

This is a barebone resin.io application to demonstrate persisting data through updates and using environment variables. 

It's a basic [Flask](http://flask.pocoo.org/) app that uses [psutil](https://pypi.python.org/pypi/psutil) to read CPU usage on the device and save it to an SQL database using [Flask-SQLAlchemy](https://pythonhosted.org/Flask-SQLAlchemy/). That db is stored in `/data` as this directory is essentially a [docker data `VOLUME`](https://docs.docker.com/userguide/dockervolumes/) and is therefore maintained through container restarts.

Note: that this folder is not mounted when your project is building on our build server, so you can't access it from your Dockerfile. It is only created once your project is deployed to the actual devices.

The interval is set by resin.io environmental variable `INTERVAL`(defaults to 20s).
