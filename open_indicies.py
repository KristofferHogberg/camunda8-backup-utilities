import requests

# Elasticsearch endpoint
elasticsearch_url = "http://localhost:9200"

# Fetch the list of indices, filtering for those with a status of 'close'
response = requests.get(f"{elasticsearch_url}/_cat/indices?h=index,status&s=index&format=json")
indices_info = response.json()

# Filter for closed indices
closed_indices = [index_info['index'] for index_info in indices_info if index_info['status'] == 'close']

# Open closed indices
for index in closed_indices:
    open_response = requests.post(f"{elasticsearch_url}/{index}/_open")
    if open_response.status_code == 200:
        print(f"Successfully opened index: {index}")
    else:
        print(f"Failed to open index: {index}. Error: {open_response.text}")
