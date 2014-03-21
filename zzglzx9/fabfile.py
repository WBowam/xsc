#!/usr/bin/python

from fabric.api import local

def r():
	local('pwd&&python manage.py runserver')

def d():
	local('python manage.py syncdb')
