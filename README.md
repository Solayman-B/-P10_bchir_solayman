# P10_bchir_solayman

Summaries
---------

* General description
* Requirements
* Installation
* Run the script

General description
-------------

The SoftDesk API, is an issue tracking system REST API developped by SoftDesk limited.


Requirements
---------

This application uses the following packets:

* apiwrapper==0.1.8
* asgiref==3.4.1
* certifi==2021.10.8
* charset-normalizer==2.0.10
* Django==4.0
* django-filter==21.1
* djangorestframework==3.13.1
* djangorestframework-simplejwt==5.0.0
* drf-nested-routers==0.93.4
* idna==3.3
* importlib-metadata==4.10.0
* Markdown==3.3.6
* PyJWT==2.3.0
* pytz==2021.3
* requests==2.27.1
* sqlparse==0.4.2
* urllib3==1.26.8
* zipp==3.7.0


Installation
------------

First, you can download this project by :

clicking on « code » then « download ZIP »

or [click here to download it directly](https://github.com/Solayman-B/P10_bchir_solayman/archive/refs/heads/main.zip)

Unzip the file when the download is completed

You can also install [Git via this link](https://git-scm.com/downloads) and use :

    gh repo clone Solayman-B/P10_bchir_solayman


To use this application properly, you need to use [python3](https://www.python.org/downloads/)

Then you can create a virtual environment:

    python3 -m venv env # env is the name of the directory, but you can choose another one if you want

On Windows, run:

    env\Scripts\activate.bat

On Unix or macOS, run:

    source env/bin/activate

And to deactivate, simply use:

    deactivate

You can install all the required paquets with:

    pip install -r requirements.txt


Run
---

Go to the folder containing the project and use `python3 main.py runserver` then open Postman or another program of your choice and go to [http://127.0.0.1:8000/signup/](http://127.0.0.1:8000/signup/
) to register. You can read [the postman documentation here](https://documenter.getpostman.com/view/19329986/UVeJJPpX) to see examples of all the URIs of the project.


