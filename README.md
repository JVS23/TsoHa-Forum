# TsoHa-Forum

A web forum for sharing, rating and discussing ASCII art with others. The forum is created as a project for the course **Aineopintojen harjoitustyö: Tietokantasovellus (periodi III, 2022-2023), Helsingin Yliopisto**. The forum is created using Python, Flask, HTML, CSS and PostgreSQL. The user interface was created using Bootstrap, and some layered CSS on top of it. You can access the forum from [here](https://still-lake-4125.fly.dev/). (https://still-lake-4125.fly.dev/) **The database might not start up on the first reload thanks to Fly.io, so you might have to refresh the page once to access it.**

## Usage

You can use the forum by creating you own account on the main page, and then you're free to share your own masterpieces and check out what others have made.
You can also give likes to the art that others (and yourself, if you feel that way) have made, and reply below their posts with a comment. The forum also has subpages for filtering categories that can be accessed from the navigation bar.

The forum can also be used by installing it locally. You need to only get the main branch if doing so, since there is a fly.io deployment branch too with different configs which don't work locally. You can find the local installation guide [here](documentation/installation.md).


## Current state

The forum is currently working fairly well, and the main thing missing is the deletion of posts, but I'll say that it's a very innovative feature
to help people come to terms with small mistakes and overcoming them. The admin privileged accounts didn't have enough developement time allocated though, so they are still missing from the final release. Deploying to Fly took longer than expected, but I also learned a lot of useful things when dealing with it. I also managed to have all the vulnerabilities fixed, which was a big priority since I wanted to deploy the app online before the deadline.
