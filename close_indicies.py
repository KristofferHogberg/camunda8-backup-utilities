import requests

# Elasticsearch endpoint
elasticsearch_url = "http://localhost:9200"

# Get the list of open indices
response = requests.get(f"{elasticsearch_url}/_cat/indices?v&h=index,status")
indices = [line.split()[0] for line in response.text.splitlines() if "open" in line]

# response = requests.get(f"{elasticsearch_url}/_cat/indices?")
# indices = [line.split()[0] for line in response.text.splitlines() if "open" in line]

# Close open indices
for index in indices:
    close_response = requests.post(f"{elasticsearch_url}/{index}/_close")
    if close_response.status_code == 200:
        print(f"Closed index: {index}")
    else:
        print(f"Failed to close index: {index}")
