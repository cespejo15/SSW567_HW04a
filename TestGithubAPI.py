import unittest
from unittest import mock

from GithubAPI import Repositories
class TestGithubAPI(unittest.TestCase):
    #My other github account and a user with no repos
    @mock.patch('GithubAPI.requests')
    def testNoRepo(self, mock_requests):
        mock_response = mock.MagicMock()
        mock_response.status_code = 200
        mock_response.text = '[]'
        mock_requests.get.return_value = mock_response
        self.assertEqual(Repositories("AlanAtrach"), "User has no repositories.")
        self.assertEqual(Repositories("ALEDSUS"), "User has no repositories.")

    #Some random letters that shouldn't result in any repos
    @mock.patch('GithubAPI.requests')
    def testNotExist(self, mock_requests):
        mock_response = mock.MagicMock()
        mock_response.status_code = 404
        mock_requests.get.return_value = mock_response
        self.assertEqual(Repositories("ALKHFJKJ"), "Repository retrieval failure or Repository not found")
        self.assertEqual(Repositories("1831hndjnwu"), "Repository retrieval failure or Repository not found")

    @mock.patch('GithubAPI.requests.get')
    def test_mock_request(self, mock_response):
        #repo
        mock_repo = mock.MagicMock()
        mock_repo.status_code = 200
        mock_repo.text = '[{"name": "anything"}]'
        #commit
        mock_commit = mock.MagicMock()
        mock_commit.status_code = 200
        mock_commit.text = '[{"one": 1}, {"two":1}, {"three":1}]'

        mock_response.side_effect = [mock_repo, mock_commit]
        result = Repositories("anyone")
        self.assertEqual(result, "Repo: anything Number of commits: 3")



if __name__ == '__main__':
    unittest.main()
