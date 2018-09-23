import unittest
import requests
import requests_mock

from scraper import GitHub

class GitHubTestCase(unittest.TestCase):
    ghApiBaseUrl = 'https://api.github.com/repos/'
    owner = 'jedpatrickdatu'

    @requests_mock.mock()
    def test_read_iterates_over_repo_resources(self, requestsMock):
        repos = [
            'go-linter',
            'balloon-bust',
        ]
        resources = [
            'issues',
            'commits',
        ]

        self.gh = GitHub(self.owner, repos, resources)

        expectedRequestURL = self.ghApiBaseUrl+self.owner+'/'+repos[0]+'/'+resources[0]
        expectedDataResult = {'sampleKey': 'sampleData'}

        requestsMock.get(expectedRequestURL, json=expectedDataResult)
        result = self.gh.read()
        self.assertEqual(result, expectedDataResult)
