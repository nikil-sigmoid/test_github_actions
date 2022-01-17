import requests
import os
import subprocess

DAG_ID = "catchup_backfill"

URL = "https://api.github.com/repos/nikil-sigmoid/test_github_actions/pulls?state=closed"
PARAMS= {"base": "main"}


def get_closed_pr_list():
    data = requests.get(url=URL, params=PARAMS)
    return data.json()



def main():
    closed_pr_list = get_closed_pr_list() 

    num = len(closed_pr_list)


    os.environ['INITIAL_SHA'] = closed_pr_list[0]["merge_commit_sha"]
    # print("Initial_sha:")
    


    # os.putenv("INITIAL_SHA", closed_pr_list[0]["merge_commit_sha"])
    # # print(os.environ['INITIAL_SHA'])


    # print()
    # print("final_sha:")
    os.environ['FINAL_SHA'] = closed_pr_list[1]["merge_commit_sha"]
    # print(os.environ['FINAL_SHA'])

    for item in range(0, 2):
        print(closed_pr_list[item]["url"])
        print(closed_pr_list[item]["number"])
        print(closed_pr_list[item]["merged_at"])
        print(closed_pr_list[item]["merge_commit_sha"])
        print()



    # return (os.environ['INITIAL_SHA'], os.environ['FINAL_SHA'])

    print()
    print(f"{os.environ['INITIAL_SHA']},{os.environ['FINAL_SHA']}")
    # print()
    # return f"{os.environ['INITIAL_SHA']},{os.environ['FINAL_SHA']}"


# p1 = subprocess.run("echo $INITIAL_SHA", shell=True, capture_output=True, text=True)
# print("initial_sha:")
# print(p1.stdout)

# print("env:")
# print(os.environ)



if __name__ == "__main__":
    main()





