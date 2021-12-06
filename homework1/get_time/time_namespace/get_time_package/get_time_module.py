import requests

try:
    from time_namespace.pp_package.pp_module import pretty_time
except ImportError:
    pretty_time = None

def time():
    url = "http://worldtimeapi.org/api/timezone/Europe/Moscow"
    resp = requests.get(url)
    unixtime = resp.json().get("unixtime", 0)
    return unixtime
def main():
    try:
        from time_namespace.pp_package.pp_module import pretty_time
        print(pretty_time())
    except ImportError:
        print(time())





