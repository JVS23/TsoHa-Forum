# TsoHa-Forum

A generic web forum which will possibly be later modified to have a theme of some sort.

## Installation guide

Currently working only locally, install with poetry using "poetry install", and running it with the command "poetry run flask run" while inside the "app" directory. Note that you need to have a psql server running. Remember to input your own server (and a secret key!) in a .env file to connect your own database. Do also remember to create the tables from the schema.sql file.

.env file example:

DATABASE_URL="yourinfohere"

SECRET_KEY=any random string

## Current state

The forum is currently still a work in progress, with features like creating and viewing threads and using personal accounts working. The forum is only available locally at the moment due to the security flaws being still in place. Most of the main features are working expect the replying, which should be a quick fix when I get back to continue working on the project.

To do:

- Come up with 2 more tables for the database to fill the criteria
- Add poetry tasks to improve installation & usage
- Replying to threads
- Improve visuals (possibly back to css, more personalization)
- Categories(?)
- Code structure cleanup to modules
- Testing
- Security (fix vulnerabilities, add CSRF protection, etc.)
- Edge cases (name & password parameters, etc.)
- Admin account creation

## Documentation

Created as a submission for the course **Aineopintojen harjoitustyö: Tietokantasovellus (periodi III, 2022-2023), Helsingin Yliopisto**
