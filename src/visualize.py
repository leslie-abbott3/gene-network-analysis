import networkx as nx
import matplotlib.pyplot as plt
import argparse, os

def visualize_network(network_file, output_file):
    G = nx.read_gml(network_file)
    plt.figure(figsize=(8,6))
    pos = nx.spring_layout(G, seed=42)
    nx.draw(G, pos, node_color="skyblue", with_labels=True, node_size=500, font_size=8)
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    plt.savefig(output_file, dpi=300)
    print(f"[INFO] Network visualization saved -> {output_file}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=str, default="data/processed/network.gml")
    parser.add_argument("--output", type=str, default="results/network_plot.png")
    args = parser.parse_args()
    visualize_network(args.input, args.output)
