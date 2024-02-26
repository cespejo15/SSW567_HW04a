
import unittest

from GithubAPI import Repositories

class TestGithubAPI(unittest.TestCase):
    #My other github account with no repos
    def testNoRepo(self):
        self.assertEqual(Repositories("AlanAtrach"), "User has no repositories.")

    #Some random letters that shouldn't result in any repos
    def testNotExist(self):
        self.assertEqual(Repositories("ALKHFJKJ"), "Repository retrieval faliure or Repository not found")

    def testing(self):
        expected_output = """Repo: csp Number of commits: 2
        Repo: hellogitworld Number of commits: 30
        Repo: helloworld Number of commits: 6
        Repo: Mocks Number of commits: 10
        Repo: Project1 Number of commits: 2
        Repo: richkempinski.github.io Number of commits: 9
        Repo: threads-of-life Number of commits: 1
        Repo: try_nbdev Number of commits: 2
        Repo: try_nbdev2 Number of commits: 5
        """
        self.assertEqual(Repositories("richkempinski"), expected_output)


if __name__ == '__main__':
    unittest.main()
