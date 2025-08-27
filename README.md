🔹 Project Structure
gene-network-analysis/
│
├── config/
│   └── config.yaml                # Configurable parameters
│
├── data/
│   ├── raw/                       # Downloaded WormBase datasets
│   └── processed/                 # Processed graphs & results
│
├── notebooks/
│   └── exploratory_network.ipynb  # Jupyter notebook for visualization
│
├── src/
│   ├── wormbase_api.py            # API wrapper for WormBase
│   ├── network_analysis.py        # Build & analyze gene interaction networks
│   ├── workflows.py               # Automated workflows
│   ├── visualize.py               # Graph visualization & export
│   └── utils.py                   # Shared helper functions
│
├── results/
│   ├── shared_partners.csv        # Example workflow output
│   └── network_plot.png           # Example visualization
│
├── requirements.txt
├── README.md
├── Dockerfile
├── .dockerignore
└── LICENSE

🔹 README.md
# Gene Interaction Network Analysis (C. elegans)

This repository contains Python pipelines for **gene interaction network analysis** in *C. elegans*.  
Developed during my work as a **Research Associate at Fairfield University School of Arts and Sciences**.  

The project integrates **WormBase API data**, builds **gene interaction networks**, and automates workflows for identifying **shared interaction partners**, helping genomics research teams interpret complex biological findings.

---

## 🚀 Features
- 🔗 Fetches interaction data via **WormBase API**  
- 🧬 Builds **gene interaction networks** using NetworkX  
- ⚡ Automated workflows for **shared partner discovery**  
- 📊 Visualizations & statistical summaries of gene networks  
- 🔄 Config-driven, reproducible pipelines  

---

## 📂 Example Workflow
1. **Query WormBase for interactions**
   ```bash
   python src/wormbase_api.py --genes egl-30 daf-2 let-60


Build & analyze network

python src/network_analysis.py --input data/raw/interactions.json --output data/processed/network.gml


Identify shared partners

python src/workflows.py --genes egl-30 daf-2 --output results/shared_partners.csv


Visualize

python src/visualize.py --input data/processed/network.gml --output results/network_plot.png

📊 Example Outputs

results/shared_partners.csv: genes that interact with multiple query genes

results/network_plot.png: network visualization (nodes=genes, edges=interactions)

🛠️ Tech Stack

Python 3.9+

NetworkX

Pandas / NumPy

Matplotlib / Seaborn

Requests (WormBase API)

PyYAML

📜 License

MIT License


---

## 🔹 `requirements.txt`
```txt
networkx
pandas
numpy
matplotlib
seaborn
requests
pyyaml
