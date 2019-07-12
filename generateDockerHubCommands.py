import requests
import argparse
import json
import time
import threading
import sys
import datetime


def getConfig(config):
    f = open(config, "r")
    content = json.loads(f.read(), strict=False)
    f.close()
    return content

parser = argparse.ArgumentParser()
parser.add_argument('--newTag', "-t", help='new timestamp EG: 1906281234')
args = parser.parse_args()

if args.newTag == None:
    tag = datetime.datetime.now().strftime("%y%m%d%H%M")
else:
    tag = args.newTag

config = "blessedImageConfig-dev.json"

buildRequests = getConfig(config)
print("az login")
print("az acr login --name blimpacr")
for br in buildRequests:
    prefix = "-apache"
    print("docker pull blimpacr.azurecr.io/{}".format(br["outputImageName"]))
    print("docker tag blimpacr.azurecr.io/{} appsvctest/{}:{}{}_{}".format(br["outputImageName"], br["stack"], br["version"], prefix, tag))
    print("docker tag blimpacr.azurecr.io/{} appsvc/{}:{}{}_{}".format(br["outputImageName"], br["stack"], br["version"], prefix, tag))
    print("docker push appsvctest/{}:{}{}_{}".format(br["stack"], br["version"], prefix, tag))
    print("docker push appsvc/{}:{}{}_{}".format(br["stack"], br["version"], prefix, tag))
    prefix = "-apache-xdebug"
    print("docker pull blimpacr.azurecr.io/{}".format(br["outputImageName"]))
    print("docker tag blimpacr.azurecr.io/{} appsvctest/{}:{}{}_{}".format(br["outputImageName"], br["stack"], br["version"], prefix, tag))
    print("docker tag blimpacr.azurecr.io/{} appsvc/{}:{}{}_{}".format(br["outputImageName"], br["stack"], br["version"], prefix, tag))
    print("docker push appsvctest/{}:{}{}_{}".format(br["stack"], br["version"], prefix, tag))
    print("docker push appsvc/{}:{}{}_{}".format(br["stack"], br["version"], prefix, tag))

    ### LATEST / LTS ###
    if br["version"] == "7.3":
        print("docker pull blimpacr.azurecr.io/{}".format(br["outputImageName"]))
        print("docker tag blimpacr.azurecr.io/{} appsvctest/{}:latest_{}".format(br["outputImageName"], br["stack"], tag))
        print("docker tag blimpacr.azurecr.io/{} appsvctest/{}:latest".format(br["outputImageName"], br["stack"]))
        print("docker push appsvctest/{}:latest_{}".format(br["stack"], tag))
        print("docker push appsvc/{}:latest".format(br["stack"]))

        print("docker pull blimpacr.azurecr.io/{}".format(br["outputImageName"]))
        print("docker tag blimpacr.azurecr.io/{} appsvctest/{}:latest-xdebug_{}".format(br["outputImageName"], br["stack"], tag))
        print("docker tag blimpacr.azurecr.io/{} appsvctest/{}:latest-xdebug".format(br["outputImageName"], br["stack"]))
        print("docker push appsvctest/{}:latest-xdebug_{}".format(br["stack"], tag))
        print("docker push appsvc/{}:latest-xdebug".format(br["stack"]))
