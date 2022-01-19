import requests
import os
import subprocess
import sys

URL = "https://api.github.com/repos/nikil-sigmoid/authenticate_demo/pulls/1/files"
PARAMS= {"base": "main"}
HEADERS = {}
HEADERS["Authorization"] = f"Bearer {sys.argv[1]}"

def get_closed_pr_list_without_auth():
    data = requests.get(url=URL, params=PARAMS)
    return data.json()

def get_closed_pr_list_with_auth():
    data = requests.get(url=URL, params=PARAMS, headers=HEADERS)
    return data.json()

def main():
    closed_pr_list_wo_auth = get_closed_pr_list_without_auth()
    print("Without auth:")
    print(closed_pr_list_wo_auth)
    
    closed_pr_list_wi_auth = get_closed_pr_list_with_auth()
    print("With auth:")
    print(closed_pr_list_wi_auth)


if __name__ == "__main__":
    main()
