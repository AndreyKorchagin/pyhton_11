import sys
import requests
import warnings

warnings.filterwarnings("ignore")


def getBranchFromPR(prBranch):
    prBranch = "/".join(prBranch.split("/")[0:2])
    prNumber = prBranch.split("/")[1]

    json = requests.get(
        "https://bitbucket.region.vtb.ru/rest/api/1.0/projects/SCRP/repos/SwiftCorp.2.0/pull-requests/%s?limit=100" % prNumber,
        auth=(login, password), verify=False).json()

    sourceBranch = json.get("fromRef").get("displayId")
    modifySourceBranch = "-".join(sourceBranch.split("-")[0:2])
    targetBranch = json.get("toRef").get("displayId")

    return targetBranch, modifySourceBranch


def getBranchFromBranchName(prBranch):
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
        print("There is no PR with the name of the %s branch" % prBranch)
        sys.exit()

    modifySourceBranch = "-".join(prBranch.split("-")[0:2])

    return targetBranch, modifySourceBranch


#
#

login = sys.argv[1]
password = sys.argv[2]
prBranch = sys.argv[3]
print("login = '%s'" % login)
print("password = '%s'" % password)
print("prBranch = '%s'" % prBranch)

if prBranch.find("release/") == 0:
    print("env_branch = '%s'" % prBranch)
    sys.exit()
elif prBranch.find("feature/") == 0 or \
        prBranch.find("bugfix") == 0 or \
        prBranch.find("hotfix/") == 0:
    targetBranch, modifySourceBranch = getBranchFromBranchName(prBranch)
elif prBranch.find("pull-requests/") == 0:
    targetBranch, modifySourceBranch = getBranchFromPR(prBranch)
else:
    sys.exit("Not found!!!")

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
