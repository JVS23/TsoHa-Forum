# TsoHa-Forum

A web forum for sharing, rating and discussing ASCII art with others. The forum is created as a project for the course **Aineopintojen harjoitustyö: Tietokantasovellus (periodi III, 2022-2023), Helsingin Yliopisto**. The forum is created using Python, Flask, HTML, CSS and PostgreSQL. The forum is currently only available locally, but will be available online in the future.

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
