from pyhub import Pyhub
from os import environ

# Python Github Client
# PyHub by Dylan Legendre
# https://www.dylanlegendre.com/

# This is simply for my testing purposes.
def test():
  client = Pyhub(environ.get('GITHUB_TOKEN'))
  prs = client.getOpenPullRequestsForOrg("TEST")
  print(prs[0]['user'])

test()