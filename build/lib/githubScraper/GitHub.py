from requests import get

class GitHub:
    supportedResources = [
        'projects',
        'pulls',
        'branches',
        'collaborators',
        'comments',
        'forks',
        'issues',
        'commits',
    ]

    def __init__(self, owner, repos, resources):
        self.owner = owner
        self.repos = repos

        for resource in resources:
            if resource not in self.supportedResources:
                print (self.supportedResources)
                raise Exception('The value "'+resource+'" passed to the parameter for GitHub resources is unsupported. Please see the documentation for a list of supported values.')

        self.resources = resources

        self.numRepos = len(repos)
        self.numResources = len(resources)

        self.currentRepoIndex = 0
        self.currentResourceIndex = 0
        self.resourcePageIndex = 1
        
    def read(self):
        if self.currentRepoIndex >= self.numRepos:
            return None

        requestUrl = 'https://api.github.com/repos/'+self.owner+'/'+self.repos[self.currentRepoIndex]+'/'+self.resources[self.currentResourceIndex]+'?page='+str(self.resourcePageIndex)
        ghData = get(requestUrl).json()

        if ghData:
            self.resourcePageIndex += 1
        else:
            self.resourcePageIndex = 1
            self.currentResourceIndex += 1

            if self.currentResourceIndex >= self.numResources:
                self.currentRepoIndex += 1
                self.currentResourceIndex = 0
        
        return ghData
