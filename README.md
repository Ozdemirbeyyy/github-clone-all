# github-clone-all

A python script to clone all the repositories of a given user if they are the owner.

## Usage
`python github-clone-all.py <user name> [path]`

## Requirements

This software has only been tested on Linux Mint 17.3

1. Python
2. Have git installed and accesible from the terminal

## Process
1. Uses the GitHub API to get a [list of user repositories](https://developer.github.com/v3/repos/#list-user-repositories)
2. Parses the JSON data returned from GitHub to get the links for all the user repos
3. Clones all the repos in series by calling git
