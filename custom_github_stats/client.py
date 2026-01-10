import requests

class GitHubClient:
    def __init__(self, token):
        self.token = token
        self.endpoint = "https://api.github.com/graphql"

    def run_query(self, query, variables):
        headers = {"Authorization": f"Bearer {self.token}"}
        request = requests.post(self.endpoint, json={'query': query, 'variables': variables}, headers=headers)
        if request.status_code == 200:
            result = request.json()
            if "errors" in result:
                raise Exception(f"GraphQL Query failed: {result['errors']}")
            return result
        else:
            raise Exception(f"Query failed to run by returning code of {request.status_code}. {request.text}")
