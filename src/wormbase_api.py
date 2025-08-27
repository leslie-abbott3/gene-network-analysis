import requests, argparse, os, json

def fetch_interactions(gene, base_url="https://wormbase.org/rest/widget/gene"):
    url = f"{base_url}/{gene}/interactions"
    r = requests.get(url)
    if r.status_code == 200:
        return r.json()
    else:
        print(f"[ERROR] Failed to fetch {gene}")
        return None

def save_interactions(gene, data, outdir="data/raw"):
    os.makedirs(outdir, exist_ok=True)
    path = os.path.join(outdir, f"{gene}_interactions.json")
    with open(path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"[INFO] Saved interactions for {gene} -> {path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--genes", nargs="+", required=True, help="List of WormBase gene IDs/names")
    parser.add_argument("--outdir", type=str, default="data/raw")
    args = parser.parse_args()

    for g in args.genes:
        data = fetch_interactions(g)
        if data:
            save_interactions(g, data, args.outdir)
