import scanpy as sc
import argparse

# scanpy v1.10.2

parser = argparse.ArgumentParser(description="Run Scrublet on a specified region, add predicted_doublet and doublet_score to adata.obs. Using default # PCs for now.")
parser.add_argument("-r", "--region", type=str, required=True,
                    help="Region identifier (e.g., R2)")
args = parser.parse_args()

region = args.region
infile = f'pilot_data/region_{region}/region_{region}_adata_filt.h5ad'
outfile = f'pilot_data/region_{region}/region_{region}_adata_filt_scrublet.h5ad'

adata = sc.read_h5ad(infile)
sc.pp.scrublet(adata, n_prin_comps=30)
adata.obs["predicted_doublet"] = adata.obs["predicted_doublet"].astype(str)

# Save 
adata.write_h5ad(outfile)
