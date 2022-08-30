<p align="center"><img src="https://user-images.githubusercontent.com/106990217/187055035-3f1b96ec-65a4-49e8-a513-d44d78d1b386.png" width="400px"></p>

<h1 align="center">SpaceX Dashboard</h1>

<h3 align="center">
A SpaceX Dashboard site built with the <a href="https://github.com/r-spacex/SpaceX-API">SpaceX API</a>.
</h3>


<br/>

<h3 align="center">
Made with
</h3>

<p align="center"><a href="https://www.djangoproject.com/">Django</a> as a backend with simple function based views, making api calls</p>

<p align="center"><a href="https://tailwindcss.com/">Tailwind CSS</a> for for styling</p>

<p align="center"><a href="https://alpinejs.dev/">Alpine.js</a> for for simplified javascript functions</p>

<p align="center">The <a href="https://github.com/r-spacex/SpaceX-API">SpaceX-API</a> as a data source</p>


## Usage
Clone Repository
```
$ git clone https://github.com/ellerman4/spacex-dashboard
```

Create and activate a virtual environment 
```cmd

...\> py -m venv env

...\> env\Scripts\activate.bat

```
Pip install Django
```cmd

...\> pip install django

```

Run server with custom management command
```cmd
...\> python manage.py startup

```

The above startup command includes a scheduled function to delete the cached json data every hour, as well as the standard Django runserver command, read more [here](https://github.com/ellerman4/spacex-dashboard/blob/master/cache/readme.md).

##

<h3 align="center">
    Disclaimer from <a href="https://github.com/r-spacex/SpaceX-API">SpaceX API</a> -
</h3>

<h4 align="center">
  <i>
    We are not affiliated, associated, authorized, endorsed by, or in any way officially connected with Space Exploration Technologies Corp (SpaceX), or any of its subsidiaries or its affiliates. The names SpaceX as well as related names, marks, emblems and images are registered trademarks of their respective owners.
  </i>
</h4>

<h5 align="center">
  ... and neither is this project.
</h5>

##
</br>
<p align="center">
<a href="https://github.com/ellerman4/"><img alt="alt_text" width="400px" src="https://user-images.githubusercontent.com/106990217/187327102-c4e9ef1b-3c14-4b9f-b814-c6d5b2ae8529.png" /></a></p>

##
</br>
<p align="center">
<a href="https://github.com/ellerman4/"><img alt="alt_text" width="400px" src="https://user-images.githubusercontent.com/106990217/187055083-ceeb562c-3bed-45ef-937b-4d9b5af5455c.png" /></a></p>
