import yaml
import pandas as pd

with open("nodepools.yaml") as f:
    data = yaml.safe_load(f)

nodepools = data["customer_nodepools"]

rows = []

for key, val in nodepools.items():
    rows.append({
        "Name": val.get("name"),
        "Size": val.get("size"),
        "Node Count": val.get("node_count"),
        "Min Nodes": val.get("min_nodes"),
        "Max Nodes": val.get("max_nodes"),
        "Disk Type": val.get("disk_type")
    })

df = pd.DataFrame(rows)
df.to_excel("nodepool_report.xlsx", index=False)

print("Excel file created successfully!")