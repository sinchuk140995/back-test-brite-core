# back-test-brite-core
back-test-brite-core is a project that represents API using Django REST framework. The actual code of the project's apps implements creating, editing and deleting risk types and policies.

* Python 3.6.7
* Django 1.11
* Django REST framework 3.9.0

This tutorial passes through all the steps to build the app, while the rest of the documentation describes the app structure and tests.

# Directory layout

back-test-brite-core directory structure looks as follows:

    back_test_brite_core/
    ├── back_test_brite_core
    ├── clients
    └── risks

The 3 root level directories separate the **project folder** (back_test_brite_core) and **two app folders** (clients, risks).

The root level directory contains the following files:

    back_test_brite_core/
    ├── manage.py
    ├── Procfile
    ├── requirements.txt
    └── runtime.txt

# The back-test-brite-core projects directory

The inner **back-test-brite-core** directory is the actual Python package for the project.

The content:

    back-test-brite-core/
    ├── __init__.py
    ├── settings.py
    ├── urls.py
    └── wsgi.py

* **__init__.py:** An empty file that tells Python that this directory should be considered a Python package.
* **settings.py:** Settings/configuration for this Django project. Django settings will tell you all about how settings work.
* **urls.py:** The URL declarations for this Django project; a “table of contents” of your Django-powered site.
* **wsgi.py:** An entry-point for WSGI-compatible web servers to serve your project.

# The app clients

The app contains models, views, serializers, etc for managing the policies.

App's source code directory layout:

    clients/
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── models.py
    ├── serializers.py
    ├── views.py
    ├── urls.py
    └── tests.py

The models.py file contains next models:
* **ClientInsuranceRisk** - stores clients policies.
* **ClientField** - stores the inputted by clients values of policies:
  * field _value_ stores text and number values.
  * field _select_option_ is a foreign key to the model SelectOption and stores enum option.

# The app risks

The app contains models, views, serializers, etc for managing the risk types.

App's source code directory layout:

    risks/
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── models.py
    ├── serializers.py
    ├── views.py
    ├── urls.py
    └── tests.py

The models.py file contains next models:
* **InsuranceRisk** - describes a general risk type information.
* **Field** - describes a risk type fields.
* **SelectOption** - describes enum fields options.

# Entity-Attribute-Value (EAV) models

Basic object-relational models in Python Django do not allow users to modify the data model within the application. For example, insurance risk type involve variables such as name, date, etc. The basic model for collecting that data in Django would define every one of those variables in advance in our Python code, from which Django creates an object-relational mapping that amounts to a database table with one column for each variable.

This is a particularly common request for applications involving collection of data in the field. From this demand arises a desire to use Entity-Attribute-Value (EAV) models. The promise of an infinite number of user-defined variables combined in infinite ways tempts users seeking to maximize the value and longevity of an application.

In our case accordingly to EAV models: _entity_ is **risks/InsuranceRisk**, _attribute_ is **risks/Field** and _value_ is **clients/ClientField**.

# Database diagram

![Database diagram](database_diagram.png)


# Tests

* **clients/test.py** contains unit tests for clients app's API views
* **risks/test.py** contains unit tests for risks app's API views

Run the following command to start the testing:
```console
python manage.py tests
```

# Deploy

Project contains all necessary files for deploy to the PasS-platform **Heroku**:

* **Procfile** - a file is used to explicitly declare your application’s process types and entry points.
* **requirements.txt** - a file that contains the required versions of dependent packages.
* **runtime.txt** - a file that declares the exact Python version number.

Web applications relies on several number of parameters to run properly on different environments. To name a few from a Django app settings: database url, password, secret key, debug status, email host, allowed hosts. Most of these parameters are environment-specific. On a development environment you might want to run your application with debug mode on. Also, it’s a clever idea to keep your secret key in a safe place (not in your git repository).

Python Decouple is a great library that helps you strictly separate the settings parameters from your source code.

In the project python-decouple is using to hide some settings variables: _SECRET_KEY_, _DEBUG_, _ALLOWED_HOSTS_, _DB_NAME_, _DB_USER_, _DB_PASSWORD_, _DB_HOST_. So you have to add this keys and their values to the **Heroku Config Vars** or create a file named **.env** in the project root for local development.

Let’s get the deployment started.

First, clone the repository you want to deploy:
```console
git clone git@github.com:sinchuk140995/back-test-brite-core.git
```

Login to Heroku using the heroku toolbelt:
```console
heroku login
```

Inside the project root, create a Heroku App:
```console
heroku create <heroku-app-name>
```

Add a PostgreSQL database to your app:
```console
heroku addons:create heroku-postgresql:hobby-dev
```

Push to deploy:
```console
git push heroku master
```

Migrate the database:
```console
heroku run python manage.py migrate
```

And there you go!
