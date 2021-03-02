import requests
import pandas as pd

headers = {"Authorization": "Bearer cf392d62e1d448f9e9f9036125472d8adee879c7"}
def run_query(query):  # A simple function to use requests.post to make the API call. Note the json= section.
    url = 'https://api.github.com/graphql'

    request = requests.post(url=url, json={'query': query}, headers=headers)
    print(request.status_code)
    # if request.status_code == 200:
    return request.json()
    # else:
    #     raise Exception("Query failed to run by returning code of {}. {}".format(request.status_code, query))

# The GraphQL query (with a few aditional bits included) itself defined as a multi-line string.
query = """
{
repository(owner: "Abdurrahman512", name: "Practice") {
    name
    defaultBranchRef {
      target {
        ... on Commit {
          history(first: 0) {
            totalCount
          }
        }
      }
    }
  }
}
"""
r = run_query(query)  # Execute the query
print(r)
result = []

for data1 in r['data']['repository']:
    # print(data1)
    output = {}
    output['name'] = r['data']['repository']['name']
    for data2 in r['data']['repository']['defaultBranchRef']['target']['history']:
        # print(data2)
        output['totalCount'] = r['data']['repository']['defaultBranchRef']['target']['history']['totalCount']
result.append(output)
# print(result)
df = pd.DataFrame(result)
print(df)