from django.shortcuts import render
import urllib.request, json 
# Create your views here.
import requests


# Caching function for json data
def fetch_data(*, update: bool=False, json_cache: str, url: str):
            
    '''
    Fetches data from the SpaceX API, or uses cached data if available

    Note: Cached data is wiped out every hour of server runtime

    Parameters
    ----------
        update : bool
            Specifies whether to use cached JSON or make a new request

        json_cache : str
            Directory to cached data 

        url : str
            SpaceX API url endpoint
    '''

    if update:
        json_data = None

    else:
        try:
            with open(json_cache, 'r') as file:
                json_data = json.load(file)

        except(FileNotFoundError, json.JSONDecodeError) as e:
            json_data = None

    if not json_data:
        json_data = requests.get(url).json()

        with open(json_cache, 'w') as file:
            json.dump(json_data, file)
    
    return json_data


def index(request):
    
    with urllib.request.urlopen('https://api.spacexdata.com/v5/launches/past') as url:
        past_launch = json.loads(url.read().decode())[-1]

    past_launchpad: dict = fetch_data(
        update=False,
        json_cache = 'cache/past_launchpad.json',
        url = f"https://api.spacexdata.com/v4/launchpads/{past_launch['launchpad']}"
    )

    next_launch: dict = fetch_data(
        update=False,
        json_cache = 'cache/next_launch.json',
        url = 'https://api.spacexdata.com/v5/launches/next'
    )

    next_launchpad: dict = fetch_data(
        update=False,
        json_cache = 'cache/next_launchpad.json',
        url = f"https://api.spacexdata.com/v4/launchpads/{next_launch['launchpad']}"
    )

    crew_data: dict = fetch_data(
        update=False,
        json_cache = 'cache/crew.json',
        url = 'https://api.spacexdata.com/v4/crew'
    )

    context = {
        'next_launch': next_launch,
        'crew_data': crew_data,
        'next_launchpad': next_launchpad,
        'past_launch': past_launch,
        'past_launchpad': past_launchpad
    }

    return render(request, 'main/home.html', context)


def launches(request):
    rocket_data: dict = fetch_data(
        update=False,
        json_cache = 'cache/rockets.json',
        url = 'https://api.spacexdata.com/v4/rockets'
    )

    launchpads: dict = fetch_data(
        update=False,
        json_cache = 'cache/launchpads.json',
        url = 'https://api.spacexdata.com/v4/launchpads'
    )

    past_launch_data: dict = fetch_data(
        update=False,
        json_cache = 'cache/past.json',
        url = 'https://api.spacexdata.com/v5/launches/past'
    )

    upcoming_launch_data: dict = fetch_data(
        update=False,
        json_cache = 'cache/upcoming.json',
        url = 'https://api.spacexdata.com/v5/launches/upcoming'
    )

    # Length of ['success'] == True/False
    success_count = len(list(filter(lambda launch: launch['success'] == True, past_launch_data)))
    failure_count = len(past_launch_data) - success_count

    # Loop through launchdata, matching rocket id to rocket name
    # Could be written more gracefully, but page load times are adequate
    for launch in past_launch_data:
        for rocket in rocket_data:
            launch.update({'rocket_name': rocket['name']}) if launch['rocket'] == rocket['id'] else None

    for launch in past_launch_data:
        for launchpad in launchpads:
            launch.update({'launchpad_name': launchpad['name']}) if launch['launchpad'] == launchpad['id'] else None

    # Do the same for upcoming launches
    for launch in upcoming_launch_data:
        for rocket in rocket_data:
            launch.update({'rocket_name': rocket['name']}) if launch['rocket'] == rocket['id'] else None

    for launch in upcoming_launch_data:
        for launchpad in launchpads:
            launch.update({'launchpad_name': launchpad['name']}) if launch['launchpad'] == launchpad['id'] else None
                

    past_launch_data.reverse()

    context = {'past_launch_data': past_launch_data,
                'upcoming_launch_data': upcoming_launch_data,
                'success_count': success_count,
                'failure_count': failure_count,
                }

    return render(request, 'main/launches.html', context)



def history(request):

    history_data: dict = fetch_data(
        update=False,
        json_cache = 'cache/history.json',
        url = 'https://api.spacexdata.com/v4/history'
    )

    return render(request, 'main/history.html', {'history_data': history_data})


def starlink(request):
    return render(request, 'main/starlink.html', {})


def rockets(request):

    rockets: dict = fetch_data(
        update=False,
        json_cache = 'cache/rockets.json',
        url = 'https://api.spacexdata.com/v4/rockets'
    )

    return render(request, 'main/rockets.html', {'rockets': rockets})


def roadster(request):

    roadster_data: dict = fetch_data(
        update=False,
        json_cache = 'cache/roadster.json',
        url = 'https://api.spacexdata.com/v4/roadster'
    )

    return render(request, 'main/roadster.html', {'roadster_data':roadster_data})

def extra(request):
    return render(request, 'main/extra.html', {})