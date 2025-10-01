# 🍲 National Cookbooks Visualisations

This project collects and visualises **core national cookbooks** of the last century – books that defined how countries cook, eat, and imagine their cuisine.  
It brings the data to life in three ways:

- 🗺️ **Map** – where these cookbooks belong geographically  
- ⏳ **Timeline** – when they emerged and how they cluster across eras  
- 🔗 **Graph** – how they influence and connect with each other  

👉 **Live site:** [National Cookbooks on GitHub Pages](https://<your-username>.github.io/national-cookbooks/)  
![GitHub Pages](https://img.shields.io/badge/view-online-green?logo=github)

---

## 📂 Repo Structure

```
national-cookbooks/
│
├── data/  
│   ├── national_cookbooks_master.csv    # Master dataset (cookbooks as nodes)
│   └── cookbook_relationships.csv       # Relationships (edges for graph)
│
├── visualisations/  
│   ├── map/                             # Google Maps view
│   ├── timeline/                        # TimelineJS / D3 view
│   └── graph/                           # D3 force-directed graph
│
├── scripts/                             # Export tools (CSV → JSON)
│
├── index.html                           # Landing page (links to all views)
└── README.md
```

---

## 📊 Data

The project’s backbone is a single CSV: **`national_cookbooks_master.csv`**, which contains:  

- `id` – unique code for each book  
- `title`, `author`, `year`, `country`  
- `latitude`, `longitude` – to map it  
- `language`, `notes`, `sources`, `cover_image_url`  
- `influence_tags`, `timeline_display`, `graph_node_type`  

Connections between books (influence, translation, adaptation) live in **`cookbook_relationships.csv`**.

---

## 🚀 Usage

Clone and explore locally:

```bash
git clone https://github.com/<your-username>/national-cookbooks.git
cd national-cookbooks
open index.html   # Mac
# or
xdg-open index.html   # Linux
```

To contribute new books:
1. Add to `data/national_cookbooks_master.csv`.
2. If relevant, add links in `data/cookbook_relationships.csv`.
3. Commit + push.  
4. GitHub Pages will auto-update the live visualisations.

---

## 🌍 Visualisations

- [🗺️ Map](visualisations/map/) – geographic view of cookbook origins  
- [⏳ Timeline](visualisations/timeline/) – chronological milestones  
- [🔗 Graph](visualisations/graph/) – network of influence  

---

## 📝 Roadmap

- [ ] Export scripts to generate JSON (GeoJSON, Timeline, Graph) from CSV  
- [ ] Populate dataset with full century of cookbooks  
- [ ] Enhance visualisations with filters (by country, language, influence type)  
- [ ] Add cookbook cover images and references  

---

## 📖 Inspiration

Cookbooks are more than recipes — they’re cultural artefacts, stitching together **national identity, history, and taste**. This project aims to show those threads across countries and time.

---

## 🧾 License

MIT License – open to share, adapt, remix.  
