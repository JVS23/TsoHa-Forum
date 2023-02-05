# TsoHa-Forum

A generic web forum which will possibly be later modified to have a theme of some sort.

## Installation guide

Currently working only locally, install with poetry using "poetry install", and running it with the command "poetry run flask run" while inside the "app" directory. Note that you need to have a psql server running. Remember to input your own server (and a secret key!) in a .env file to connect your own database. Do also remember to create the tables from the schema.sql file.

## Current state

The forum is currently in an early stage, with features like account creation and management working. The forum itself is WIP, and will be added soon.

To do:

- Come up with 2 more tables for the database to fill the criteria
- Threads (and respective SQL table changes)
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
