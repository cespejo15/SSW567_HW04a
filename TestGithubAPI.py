
import unittest

from GithubAPI import Repositories

class TestGithubAPI(unittest.TestCase):
    #My other github account with no repos
    def testNoRepo(self):
        self.assertEqual(Repositories("AlanAtrach"), "User has no repositories.")

    #Some random letters that shouldn't result in any repos
    def testNotExist(self):
        self.assertEqual(Repositories("ALKHFJKJ"), "Repository retrieval faliure or Repository not found")

    

if __name__ == '__main__':
    unittest.main()