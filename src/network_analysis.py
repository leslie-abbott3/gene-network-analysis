import networkx as nx
import json, argparse, os

def build_network(input_dir, output_file):
    G = nx.Graph()
    for f in os.listdir(input_dir):
        if f.endswith(".json"):
            with open(os.path.join(input_dir, f)) as infile:
                data = json.load(infile)
                if "data" in data:
                    interactions = data["data"]["interactions"]["data"]
                    for i in interactions:
                        partner = i["interactor"]["label"]
                        gene = i["object"]["label"]
                        G.add_edge(gene, partner)
    nx.write_gml(G, output_file)
    print(f"[INFO] Network saved to {output_file} ({len(G.nodes)} nodes, {len(G.edges)} edges)")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=str, default="data/raw")
    parser.add_argument("--output", type=str, default="data/processed/network.gml")
    args = parser.parse_args()
    os.makedirs(os.path.dirname(args.output), exist_ok=True)
    build_network(args.input, args.output)
