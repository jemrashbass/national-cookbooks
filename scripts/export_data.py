#!/usr/bin/env python3
"""
Export CSV cookbook data into JSON formats for visualisations:
- map.json      (GeoJSON for Google Maps)
- timeline.json (TimelineJS / chronological views)
- graph.json    (nodes + edges for D3 graph)
"""

import csv
import json
from pathlib import Path

# Paths
DATA_DIR = Path(__file__).resolve().parents[1] / "data"
MASTER_CSV = DATA_DIR / "national_cookbooks_master.csv"
REL_CSV = DATA_DIR / "cookbook_relationships.csv"

MAP_JSON = DATA_DIR / "map.json"
TIMELINE_JSON = DATA_DIR / "timeline.json"
GRAPH_JSON = DATA_DIR / "graph.json"

# --- Load master dataset ---
def load_master():
    rows = []
    with open(MASTER_CSV, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row["id"].startswith("#") or not row["id"].strip():
                continue  # skip comments/empty
            rows.append(row)
    return rows

# --- Load relationships ---
def load_relationships():
    edges = []
    with open(REL_CSV, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row["source_id"].startswith("#") or not row["source_id"].strip():
                continue
            edges.append(row)
    return edges

# --- Export to GeoJSON ---
def export_map(data):
    features = []
    for row in data:
        try:
            lat, lon = float(row["latitude"]), float(row["longitude"])
        except ValueError:
            continue
        feature = {
            "type": "Feature",
            "geometry": {"type": "Point", "coordinates": [lon, lat]},
            "properties": {
                "id": row["id"],
                "title": row["title"],
                "author": row["author"],
                "year": row["year"],
                "country": row["country"],
                "notes": row["notes"],
                "cover_image_url": row["cover_image_url"],
                "sources": row["sources"],
            },
        }
        features.append(feature)
    geojson = {"type": "FeatureCollection", "features": features}
    MAP_JSON.write_text(json.dumps(geojson, indent=2, ensure_ascii=False), encoding="utf-8")

# --- Export to Timeline JSON (simplified TimelineJS schema) ---
def export_timeline(data):
    events = []
    for row in data:
        if row.get("timeline_display", "true").lower() in ("true", "1", "yes"):
            event = {
                "start_date": {"year": row["year"]},
                "text": {
                    "headline": row["title"],
                    "text": f"{row['author']} – {row['notes']}",
                },
            }
            if row.get("cover_image_url"):
                event["media"] = {"url": row["cover_image_url"]}
            events.append(event)
    timeline = {"events": events}
    TIMELINE_JSON.write_text(json.dumps(timeline, indent=2, ensure_ascii=False), encoding="utf-8")

# --- Export to Graph JSON ---
def export_graph(data, edges):
    nodes = []
    for row in data:
        nodes.append({
            "id": row["id"],
            "label": row["title"],
            "type": row.get("graph_node_type", "cookbook"),
            "year": row["year"],
            "country": row["country"],
        })
    links = []
    for e in edges:
        links.append({
            "source": e["source_id"],
            "target": e["target_id"],
            "relationship": e["relationship"],
            "weight": int(e.get("weight", 1)),
            "notes": e.get("notes", ""),
        })
    graph = {"nodes": nodes, "links": links}
    GRAPH_JSON.write_text(json.dumps(graph, indent=2, ensure_ascii=False), encoding="utf-8")

# --- Main ---
def main():
    data = load_master()
    edges = load_relationships()

    export_map(data)
    export_timeline(data)
    export_graph(data, edges)

    print("✅ Export complete: map.json, timeline.json, graph.json")

if __name__ == "__main__":
    main()
