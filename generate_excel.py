import yaml
import os

with open("nodepools.yaml") as f:
    data = yaml.safe_load(f)

nodepools = data["customer_nodepools"]

# Create markdown table
table = "| Name | Size | Node Count | Min | Max | Disk |\n"
table += "|------|------|------------|-----|-----|------|\n"

for key, val in nodepools.items():
    table += f"| {val.get('name')} | {val.get('size')} | {val.get('node_count')} | {val.get('min_nodes')} | {val.get('max_nodes')} | {val.get('disk_type')} |\n"

# Print in logs
print(table)

# Write to GitHub Summary
summary_file = os.environ.get("GITHUB_STEP_SUMMARY")

with open(summary_file, "a") as f:
    f.write("## Nodepool Report\n\n")
    f.write(table)