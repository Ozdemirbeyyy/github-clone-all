import urllib2
import sys
import os
import json
from subprocess import call

if len(sys.argv) == 2:
    path = os.getcwd()
elif len(sys.argv) != 3:
    path = sys.argv[2]
    print "Usage: <user> <path>"
    print "user - The username"
    print "path - The path to clone to"
elif len(sys.argv) == 3:
    if sys.argv[2] == ".":
        path = os.getcwd()
    else:
        path = sys.argv[2]

user = sys.argv[1]

print "Current Working Directory: %s " % path

print "Fetching user repos from %s ..." % user
req = urllib2.Request("https://api.github.com/users/%s/repos" % user)

try: 
    response = urllib2.urlopen(req)
except urllib2.HTTPError as e:
    print "HTTP Error: %i" % e.code
    print "User probably does not exist"
    sys.exit(1)
except urllib2.URLError as e:
    print e.reason
    sys.exit(1)
else:
    json_data = response.read()

data = json.loads(json_data)

#for i in range(0, len(data)):
#    print data[i]["clone_url"]

os.chdir(path)

for i in range(0, len(data)):
    print "Cloning %i / %i" % (i+1, len(data))
    print "Cloning repository: %s" % data[i]["name"]
    call(["git", "clone", data[i]["clone_url"]])
