# TsoHa-Forum

A web forum for sharing, rating and discussing ASCII art with others. The forum is created as a project for the course **Aineopintojen harjoitustyö: Tietokantasovellus (periodi III, 2022-2023), Helsingin Yliopisto**. The forum is created using Python, Flask, HTML, CSS and PostgreSQL. The forum is currently only available locally, but will be available online in the future.

## Installation guide

**For peer-reviewers:** If for some reason you cannot use poetry, make an issue saying that you can't use Poetry, and I'll make changes to accomodate ASAP.

Currently working only locally, install with poetry using "poetry install", and running it with the command "poetry run flask run" while inside the "app" directory. Note that you need to have a psql server running. Remember to input your own server (and a secret key!) in a .env file to connect your own database. Do also remember to create the tables from the schema.sql file.


(Don't worry about the ".. does not contain any element" error after poetry install, it's related to a new feature in poetry that can be circumvented by using command "poetry install --no-root", but the error doesn't affect the installation anyways.)


.env file example:

DATABASE_URL="postgresql://name:password@localhost"
SECRET_KEY=any random string

## Current state

The forum is currently still a work in progress, with features like creating and viewing threads and using personal accounts working. The forum is only available locally at the moment due to the security flaws being still in place. Most of the main features are working except the replying, which should be a quick fix when I get back to continue working on the project.


To do:

- Replying to threads
- Editing and removing posts
- New tables, Categories and saved threads
- Testing
- Admin account creation
- Deploy to fly.io
