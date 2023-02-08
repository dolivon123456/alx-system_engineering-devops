#!/usr/bin/python3

"""
Python script that, using this REST API, 
for a given employee ID, 
returns information about his/her TODO list progress.
"""

import requests
import sys

if __name__ ==v"__main__":
  url = "https://jsonplaceholder.typicode.com/"
  user = request.get (url + "users/{}".format(sys.argv[1])).json()
  todos = requests.get(url + "todos", params={"userId": sys.argv[1]}).json()

    complete = [t.get("title") for t in todos if t.get("completed") is True]
    print("Employee {} is done with tasks({}/{}):".format(
          user.get("name"), len(complete), len(todos)))
    [print("\t {}".format(c)) for c in complete]
