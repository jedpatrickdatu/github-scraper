# github-scraper

github-scraper is a small Python library that can request unlimited amounts of data from GitHub repositories through [GitHub's REST API](https://developer.github.com). 

## How to Use

One only needs to import and instantiate the class "GitHub" and then use its single function, "read()," to get a stream of data from repositories.

Specify in the constructor three arguments: the repository owner's name, the repositories of that user that you wish to scrape, and the resources of those repositories that you want to get the data of. Here is an example of the initialization in code:

```python
from github-scraper import GitHub

owner = 'jedpatrickdatu'
repo = [
    'squirrel-sync',
    'blue-moss-storage',
    'nuke-and-duke',
]
resources = [
    'issues',
    'commits',
    'users',
]

gh = GitHub(owner, repo, resources)
```

Then, you may call the GitHub object's "read()" method. The first use of this function which will return a JSON string containing the data from the first page of the first resource of the first repository specified in the constructor. Subsequent calls would iterate through the pages, resources, and repositories in order until the last page of the last resource of the final repository was returned, after which further calls would only give "None." Below is an example of how one would use the method:

```python
data = gh.read()
while data is not None:
    print(data)
    data = gh.read()
```

The following is the list of resources that the library can extract, along with the keyword for the constructor argument. Including an invalid string to the array parameter raises an exception.
- Projects: 'projects'
- Pull Requests: 'pulls'
- Branches: 'branches'
- Collaborators: 'collaborators'
- Comments: 'comments'
- Forks: 'forks'
- Issues: 'issues'
- Commits: 'commits'

### Prerequisites

- [Python v.>=2.7](https://www.python.org/downloads/)


### Installing

Clone the repository, cd into it, and then run "[pip](https://pip.pypa.io/en/stable/installing/) install ." like so:

```
git clone https://github.com/jedpatrickdatu/github-scraper
cd github-scraper
pip install .
```

You should then be able to import it like in the above section.

## Running the tests

You may run the tests in the "tests" folder using the usual Python syntax:
```
python -m unittest <test_file>
```

To make it easy to run all tests in one command, use [nose](https://nose.readthedocs.io/en/latest/).