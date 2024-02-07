import requests

# Elasticsearch endpoint
elasticsearch_url = "http://localhost:9200"

# Define the snapshot repository and snapshot name
repository_name = "my_backup_repository"
snapshot_name = "my_snapshot_1"

# Create the snapshot
create_snapshot_response = requests.put(
    f"{elasticsearch_url}/_snapshot/{repository_name}/{snapshot_name}?wait_for_completion=true",
    headers={"Content-Type": "application/json"},
    json={}
)

if create_snapshot_response.status_code == 200:
    print(f"Snapshot {snapshot_name} created successfully in repository {repository_name}.")
else:
    print(f"Failed to create snapshot {snapshot_name}. Error: {create_snapshot_response.text}")
