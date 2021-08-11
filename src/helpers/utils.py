import requests


def get_data(url, params):
    """
    url: Add the url endpoint to get API response from
    params: params to be sent alongwith the GET request.
    """
    data = requests.get(url=url, params=params)
    return data


def get_json_data(response, key):
    """
    get response in JSON data format, pass response as an argument.
    key: get the value for key passed into as an argument
    """
    return response.json()[key]
