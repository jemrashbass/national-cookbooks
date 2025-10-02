# README_TAGS.md
**Influence Tagging for National Cookbooks Dataset**

This file documents the logic used to populate the `influence_tags` field in  
`national_cookbooks_master_with_tags.csv`. Tags are aligned with the map colour  
legend so they can be visualised meaningfully.  

---

## 🎨 Legend: Tags → Colour
- **household** → 🔵 Blue (domestic, everyday adoption)  
- **compendium** → 🟣 Purple (encyclopedic, national anthologies)  
- **professional** → 🔴 Red (chef-driven, culinary schools, haute cuisine)  
- **codification** → 🟢 Green (works that set or codify national standards)  
- **translation / adaptation** → 🟠 Orange (cross-cultural or hybridising works)  
- **renaissance / historical** → 🟤 Brown (foundational or early works)  

---

## 🗂 Assignment Rules

**Renaissance / Historical**  
- Authors: Bartolomeo Scappi, Hannah Glasse, Eliza Acton, Katharina Prato, Elena Molokhovets  
- Tags: `renaissance;historical`  

**Professional / Codification**  
- Authors: Auguste Escoffier, Fernand Point, Dr. Oetker, Shizuo Tsuji  
- Tags: `professional;codification`  

**Codification only**  
- Authors: Pellegrino Artusi, C. J. Wannée  
- Titles: *The Book of Tasty and Healthy Food* (USSR)  
- Tags: `codification`  

**Household / Compendium**  
- Authors: Isabella Beeton, Ada Boni, Bertha Rosa-Limpo, Irma Rombauer, Delia Smith, General Mills (Betty Crocker), KVLV (*Ons Kookboek*), KF Provkök (*Vår kokbok*), Companhia Editora Nacional (*Dona Benta*)  
- Tags: `household;compendium`  

**Translation / Adaptation**  
- Authors: Elizabeth David, Julia Child/Simone Beck/Louisette Bertholle, Marcella Hazan, Madhur Jaffrey, Claudia Roden, Margaret Fulton, Ken Hom, Julee Rosso & Sheila Lukins (*The Silver Palate*)  
- Tags: `translation;adaptation`  

**Default (catch-all)**  
- If no rule matched, fallback = `household`  

---

## ⚙️ Notes
- Tags are semicolon-separated to allow multi-category assignment (e.g. `professional;codification`).  
- Tags are used to colour pins in the map visualisation via `config/influence_colors.json`.  
- Categories are intentionally broad, designed to show contrasts in cookbook adoption type rather than bibliographic detail.  
