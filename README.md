# National Cookbooks Visualisations

This repo houses:
- **/data/**: master dataset and relationships
- **/visualisations/**: standalone HTMLs for Map, Timeline, Graph
- **/scripts/**: helper scripts for exporting CSV → JSON (to be added)

## Hosting on GitHub Pages
1. Commit + push this repo to GitHub.
2. In the repo settings, enable **GitHub Pages** → Source: `main` branch 
→ Root (`/`).
3. Pages will be served at 
`https://<your-username>.github.io/national-cookbooks/`.

## Updating Data
- Update `data/national_cookbooks_master.csv` or 
`data/cookbook_relationships.csv`.
- Run export scripts (to be written) to generate JSON for each 
visualisation.
- Push changes → GitHub Pages auto-updates.
