import requests
from sqlalchemy import create_engine
import os

dbname = 'devops'
port = 5432
user = os.getenv('dbuser')
password = os.getenv('dbpassword')
host = os.getenv('dbhost')
engine = create_engine('postgresql+psycopg2://{0}:{1}@{2}:5432/{3}'.format(user, password, host, dbname))
token = os.getenv('token')

org = "FrontlineEducation"
headers = {'Authorization': "Token " + token}


def run_query(query):
    request = requests.post('https://api.github.com/graphql', json={'query': query}, headers=headers)
    if request.status_code == 200:
        return request.json()
    else:
        raise Exception("Query failed to run by returning code of {}. {}".format(request.status_code, query))


pagination_token = 'Y3Vyc29yOjEwMA=='
hasnextpage = True

conn = engine.raw_connection()
cur = conn.cursor()
while hasnextpage:
    query = """
    query MyQuery {
      organization(login: "FrontlineEducation") {
        teams(first: 20, after: "%s") {
          edges {
            node {
              name
              repositories {
                edges {
                  permission
                  node {
                    id
                    name
                  }
                }
              }
            }
          }
          pageInfo {
            startCursor
            hasNextPage
            endCursor
          }
        }
      }
    }
    """ % (pagination_token,)
    result = run_query(query)
    edges = result['data']['organization']['teams']['edges']
    for edge in edges:
        team_name = edge['node']['name']
        data = edge['node']['repositories']['edges']
        if len(data) > 0:
            for repo in data:
                repository_name = repo['node']['name']
                permission = repo['permission']
                print(repository_name, team_name, permission)
                cur.execute("""insert into devops.github_repository_team_permissions values ('{0}','{1}','{2}') on 
                                        conflict do nothing""".format(repository_name, team_name, permission))
        else:
            repository_name = ''

    pagination_token = result['data']['organization']['teams']['pageInfo']['endCursor']
    hasnextpage = result['data']['organization']['teams']['pageInfo']['hasNextPage']
    print(result['data']['organization']['teams']['pageInfo'])

conn.commit()
conn.close()
