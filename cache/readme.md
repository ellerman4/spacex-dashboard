Cached JSON data is stored here. Cache will be wiped every hour of server runtime with our custom Django management command, [update_data](https://github.com/ellerman4/spacex-dashboard/blob/master/main/management/commands/update_data.py), forcing our [fetch_data](https://github.com/ellerman4/spacex-dashboard/blob/master/main/views.py) function to update data via the
[SpaceX API](https://github.com/r-spacex/SpaceX-API) and then saving to cache for later use.

Other methods for running background processes/caching API calls seemed overly complex so I made my own...

Runserver and update_data commands can be run simultaneously by running our final custom management command, [startup](https://github.com/ellerman4/spacex-dashboard/blob/master/main/management/commands/startup.py):
```python
python manage.py startup
```
