import networkx as nx
import argparse, os
import pandas as pd

def find_shared_partners(network_file, genes, output_file):
    G = nx.read_gml(network_file)
    partner_sets = {g: set(G.neighbors(g)) for g in genes if g in G}
    shared = set.intersection(*partner_sets.values()) if partner_sets else set()
    
    df = pd.DataFrame({
        "shared_partners": list(shared)
    })
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    df.to_csv(output_file, index=False)
    print(f"[INFO] Shared partners saved -> {output_file}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--genes", nargs="+", required=True)
    parser.add_argument("--network", type=str, default="data/processed/network.gml")
    parser.add_argument("--output", type=str, default="results/shared_partners.csv")
    args = parser.parse_args()
    find_shared_partners(args.network, args.genes, args.output)
