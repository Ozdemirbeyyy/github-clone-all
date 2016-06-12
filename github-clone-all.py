import requests
import sys
import os
import json
from subprocess import call

printHelp = False

if (len(sys.argv) == 1):
    printHelp = True
elif (len(sys.argv) == 2):

    if (sys.argv[1] == '-h' or sys.argv[1] == '--help'):
        printHelp = True
    else:
        path = os.getcwd()

elif (len(sys.argv) == 3):
    if sys.argv[2] == ".":
        path = os.getcwd()
    else:
        path = sys.argv[2]

if (printHelp == True):
    print('Usage: github-clone-all.py <username> [path]')
    print('Clone all public repositories of the given username from GitHub\n')

    print('username - username of the user to clone all publix repos')
    print('path     - The path to clone to. If no path if given current dir is used')
    exit(0)

user = sys.argv[1]

print('Cloning to: %s ' % path)

print('Fetching user repos from %s ...\n' % user)

# TODO: String concat?
url = 'https://api.github.com/users/{0}/repos'.format(user)

error = False

try:
    r = requests.get(url, timeout=10)

except requests.Timeout as e:
    print("[ERROR] Request timed out while fetching statistics!")
    error = True
except requests.ConnectionError as e:
    print('[ERROR] Connection error while fetching statistics!')
    error = True
except socket.error as e:
    print('[ERROR] Socket error while fetching statistics!')
    error = True
except exception as e:
    print(e.message)
    error = True

if (error == True):
    print('Unable to fetch repository list. Exiting')
    exit(1)

if (r.status_code == 404):
    print('[ERROR] Username not found. (Server returned status 404)')
    exit(1)

json_data = r.text

data = json.loads(json_data)

os.chdir(path)

for i in range(0, len(data)):
    print('Cloning %i / %i' % (i+1, len(data)))
    print('Cloning repository: %s' % data[i]['name'])

    call(['git', 'clone', data[i]['clone_url']])
    print('')
