from requests import get
from base64 import b64encode

# Python Github Client
# PyHub by Dylan Legendre
# https://www.dylanlegendre.com/

# Represents the PyHub Client
class Pyhub:

  # Default Constructor
  # pat: string - Personal Access Token that you want to use on behalf of your account.
  def __init__(self, pat):
    self.personalAccessToken = pat
    self.githubBaseUrl = 'https://api.github.com'

  # Get the value of the personal access token that the client is using.
  def getPersonalAccessToken(self):
    return self.personalAccessToken

  # Return all open pull requests against the specified organization for the authorized user.
  def getOpenPullRequestsForOrg(self, orgName):
    url = self.githubBaseUrl + '/search/issues?q=is:open+is:pr+sort:created-asc+org:' + orgName
    credentials = b64encode(("pyhub:" + self.personalAccessToken).encode('UTF-8')).decode('UTF-8')
    headers = { 'Authorization': 'Basic ' + credentials }
    r = get(url, headers=headers)
    data_dict = r.json()

    # Create a list of the PRs we want to return.
    # Iterate the returned items and parse out the properties we care about.
    prs = []
    for data in data_dict['items']:
      prs.append(PullRequest(data['created_at'], data['html_url'], data['user']['login']))

    return prs

# Represents the properties of a pull request that we care about.
class PullRequest:

  # Default Constructor
  # created_at: date - The datetime the PR was created.
  # url: string - The URL to the HTML page on Github for this PR.
  # user: string - The Username of the user that created this PR.
  def __init__(self, created_at, url, user):
    self.created_at = created_at
    self.url = url
    self.user = user

  # Provide the ability to return the properties directly using bracket notation.
  def __getitem__(self, key):
    return getattr(self,key)    


