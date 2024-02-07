import requests

# Define the Elasticsearch server URL
elasticsearch_url = "http://localhost:9200"

# Define the snapshot repository and snapshot name
snapshot_repository = "backup_optimize"
snapshot_name = "my_snapshot_1"

# Define the restore configuration
restore_config = {
    "indices": "*.ds-.logs-deprecation.elasticsearch-default-2024.02.06-000001",  # Specify the index to restore
    "ignore_unavailable": True,
    "include_global_state": True,
    "rename_pattern": "(.+)",  # Capture the entire index name
    "rename_replacement": "restored_$1"  # Replace with a new name, e.g., "restored_index_name"
}

# Define the restore URL
restore_url = f"{elasticsearch_url}/_snapshot/{snapshot_repository}/{snapshot_name}/_restore"

# Send the restore request
response = requests.post(restore_url, json=restore_config)

print(response.json())

# Check the response status code
if response.status_code == 200:
    print("Restore request successful.")
else:
    print(f"Restore request failed with status code {response.status_code}")
    print(response.text)
