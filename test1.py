import sys
import requests
import warnings

warnings.filterwarnings("ignore")

login = sys.argv[1]
password = sys.argv[2]
prBranch = sys.argv[3]
print("login = '%s'")
print("password = '%s'")
print("prBranch = '%s'" % prBranch)

if prBranch.find("release/") == 0:
    print("env_branch = '%s'" % prBranch)
    sys.exit()

json = requests.get(
    "https://bitbucket.region.vtb.ru/rest/api/1.0/projects/SCRP/repos/SwiftCorp.2.0/pull-requests?limit=100",
    auth=(login, password), verify=False).json()

status = False
for value in json["values"]:
    displayId = value.get("fromRef").get("displayId")
    if prBranch == displayId:
        targetBranch = value.get("toRef").get("displayId")
        status = True
        break

if not status:
    print("PR c названием ветки %s нет" % prBranch)
    sys.exit()

modifySourceBranch = "-".join(prBranch.split("-")[0:2])

jsonEnv = requests.get(
    "https://bitbucket.region.vtb.ru/rest/api/1.0/projects/SCRP/repos/SwiftCorp.2.0.env/pull-requests?limit=100",
    auth=(login, password), verify=False).json()

env_branch = None
for value in jsonEnv["values"]:
    displayId = value.get("fromRef").get("displayId")
    modifyDisplayId = "-".join(displayId.split("-")[0:2])
    if (modifyDisplayId == modifySourceBranch):
        env_branch = displayId
        break

if env_branch is None:
    print("env_branch = '%s'" % targetBranch)
else:
    print("env_branch = '%s'" % env_branch)
