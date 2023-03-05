## Installation guide


Currently working only locally, install with poetry using "poetry install", and running it with the command "poetry run flask run" while inside the "app" directory. Note that you need to have a psql server running. Remember to input your own server (and a secret key!) in a .env file to connect your own database. Do also remember to create the tables from the schema.sql file.


(Don't worry about the ".. does not contain any element" error after poetry install, it's related to a new feature in poetry that can be circumvented by using command "poetry install --no-root", but the error doesn't affect the installation anyways.)


.env file example:

DATABASE_URL="postgresql://name:password@localhost"

SECRET_KEY=any random string