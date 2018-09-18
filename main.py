from github import GitHub

owner = 'jaunesarmiento'
repo = [
    'fries',
    'redux-thunk',
    'HelloFries',
]
resources = [
    'issues',
    'commits',
    'users',
]

gh = GitHub(owner, repo, resources)

data = gh.read()
while data is not None:
    print(data)
    data = gh.read()