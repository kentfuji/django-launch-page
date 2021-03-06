django-launch-page
==================

A launch page for a Django project to collect e-mail addresses and more.

Master Build Status
-------------------

[![Build Status](https://travis-ci.org/RyanBalfanz/django-launch-page.png?branch=master)](https://travis-ci.org/RyanBalfanz/django-launch-page)

Develop Build Status
--------------------

[![Build Status](https://travis-ci.org/RyanBalfanz/django-launch-page.png?branch=develop)](https://travis-ci.org/RyanBalfanz/django-launch-page)


Installing `launch_page` to your Django project will give you a simple teaser page for collecting e-mail addresses, names, and IP addresses.

The IP address can be geolocated with GeoIP. For more information, see the GeoIP documentation.

Installation
------------

Install from PyPI:

	pip install django-launch-page

Add `launch_page` to your `INSTALLED_APPS`:

	INSTALLED_APPS = (
		...
		'launch_page',
	)

Include the `launch_page` URLconf in your project urls.py:

	urlpatterns = patterns('',
		...
		url(r'^launch_page/', include('launch_page.urls')),
	)

or, bind it to the root domain, as in the example project:

	urlpatterns = patterns('',
		url(r'', include('launch_page.urls')),
		...
	)

Migrate the application:

	python manage.py migrate launch_page

The use of custom templates is similar to overriding admin templates.

Contributing
------------

Create a new virtualenv:

	pyvenv venv

Install the development packages

	pip install -r requirements.txt

Then install the application's package:

	python setup.py develop

Run the example project:

	cd example_project/
	foreman start
	# Or, with Django's development server
	python manage.py runserver

Testing across multiple Python versions is support with tox. To run the tests:

	make test

[GeoIP]: https://docs.djangoproject.com/en/dev/ref/contrib/gis/geoip/
[tox]: http://tox.readthedocs.org/en/latest/
[Overriding admin templates]: https://docs.djangoproject.com/en/dev/ref/contrib/admin/#overriding-admin-templates
