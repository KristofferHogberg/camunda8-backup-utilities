import requests

# Define the Elasticsearch server URL
elasticsearch_url = "http://localhost:9200"

# Define the snapshot repository and snapshot name
snapshot_repository = "my_backup_repository"  # Update this to your snapshot repository name
snapshot_name = "my_snapshot_1"  # Update this to your snapshot name

# Fetch the list of indices from the snapshot
snapshot_details_url = f"{elasticsearch_url}/_snapshot/{snapshot_repository}/{snapshot_name}"
snapshot_response = requests.get(snapshot_details_url)

if snapshot_response.status_code == 200:
    snapshot_details = snapshot_response.json()
    indices = snapshot_details['snapshots'][0]['indices']
    indices_list = ','.join(indices)  # Convert the list of indices to a comma-separated string

    # Define the restore configuration with dynamic indices
    restore_config = {
        "indices": indices_list,  # Use the dynamically fetched list of indices
        "ignore_unavailable": True,
        "include_global_state": False,  # Set to False unless you specifically want to restore global state
        # Remove rename_pattern and rename_replacement unless you need to rename the indices
    }

    # Define the restore URL
    restore_url = f"{elasticsearch_url}/_snapshot/{snapshot_repository}/{snapshot_name}/_restore"

    # Send the restore request
    response = requests.post(restore_url, json=restore_config)

    if response.status_code == 200:
        print("Restore request successful.")
        print(response.json())
    else:
        print(f"Restore request failed with status code {response.status_code}")
        print(response.text)
else:
    print(f"Failed to fetch snapshot details with status code {snapshot_response.status_code}")
    print(snapshot_response.text)
