# Jarvys
A speech query based server used for Ynov Ydays in order to create a campus-centered PDA

# Introduction

This is a school project based of MozillaDeepseech engine. We are here aiming to create a serverside application which may be used to receive and answer queries from a mobile application.
The application purpose will be to get a vocal query, send it to the server then display the result.

This repo is juste the backend structure, based on Flask which is used to answer queries and also to serve the main site landingpage


# Prerequisite

You only need to have virtualenv installed on you computer

In order to launch the project in the actual state you'll have to do the following:

<code> virtualenv $HOME/tmp/jarvis-site/</code>

This will create a virtualenv for our project to run into.

Then activate this virtualenv:

<code> source $HOME/tmp/jarvis-site/bin/activate</code>

**If you may work a lot with this you may have to create an alias to make your life easier**

Install Flask:

<code> pip install flask </code>

You may now browse the repo you just checkout:

<code> cd JarvysSiteWeb </code>

<code>  export FLASK_APP=jarvysSite.py</code>

<code> flask run</code>

You may now access the web site on **localhost:5000**

### Tech
 
 While working with Flask on this project you may want to :
 <ul>
    <li> Create a new route</li>
    <li> Change the computing of a route</li>
    <li> Change the landing page structure/style</li>
 </ul>

For the firsts two you may find information on Flask site.

For the last one, just change the following file:
<ul>
    <li> templates/Jarvys2.html    </li>
    <li> static/css/Jarvys.css</li>
 </ul>
**NB : WHILE CHANGING THE HTML, DON'T FORGET TO SPECIFY STATIC FILES (IMAGES, STYLE, SCRIPTS) USING FLASK DIRECTIVE({{ <code>url_for('static', filename='path_to_my_file/myfile.ext') }}</code> where path_to_my_file is the path reffering to myfile.ext from the static folder)**
