from requests import get

class GitHub:
    def __init__(self, owner, repos, resources):
        self.owner = owner
        self.repos = repos
        self.resources = resources

        self.numRepos = len(repos)
        self.numResources = len(resources)
        self.repoIndex = 0
        self.resourceIndex = 0
        self.resourcePageIndex = 1
        
    def read(self):
        if self.repoIndex >= self.numRepos:
            return None

        requestUrl = 'https://api.github.com/repos/'+self.owner+'/'+self.repos[self.repoIndex]+'/'+self.resources[self.resourceIndex]+'?page='+str(self.resourcePageIndex)
        ghData = get(requestUrl).json()

        if ghData:
            self.resourcePageIndex += 1
        else:
            self.resourcePageIndex = 1
            self.resourceIndex += 1

            if self.resourceIndex >= self.numResources:
                self.repoIndex += 1
                self.resourceIndex = 0
        
        return ghData
