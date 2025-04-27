# User Instructions
1. In this naming system, if there is no suffix, it represents operations based on the **outflow** of each node. If the suffix is **in**, it represents operations based on the **inflow** of each node. This code processes outflow and inflow separately.
2. In this naming system, the suffix **noweighted** indicates that the edge weights of the graph are **not enhanced** using the method proposed in this paper. The suffix **weighted** indicates that edge weights **are enhanced** using this method.
3. There are two main tasks:  
   - **Task 1**: Hierarchical clustering operation of HDPC-L (corresponding to the `Datasets_haikou` and `Datasets_Shenzhen` folders).  
   - **Task 2**: Running seven baseline models using the obtained adjacency matrices and datasets to produce experimental results (corresponding to the `PyG_Haikou`, `PyG_Haikou_in`, `PyG_Shenzhen`, `PyG_Shenzhen_in`, `ST-SSL-main-300epoch`, and `STPGCN-2pre` folders).

---

# Datasets_haikou and Datasets_Shenzhen

## Datasets_haikou
1. Run `Datasets_haikou/pre-process/get-diff-granularity-dens.py` to obtain block-wise processing results of the Haikou dataset at different granularities.
2. Run the following scripts in sequence under `Datasets_haikou/hierarchical-cluster/`:  
   `layer1_get_clusters.py` → `layer1_clusters_combine.py` → `layer2_get_layer1's_every_cluster.py` → `layer2_get_clusters.py` → `layer2_clusters_combine.py` → `layer3_get_layer2's_every_cluster.py` → `layer3_get_clusters.py` → `layer3_clusters_combine.py` → `layer4_get_layer3's_every_cluster.py` → `layer4_get_clusters.py` → `layer4_clusters_combine.py`.  
   This generates four-layer hierarchical density clustering results for Haikou, saved in `Datasets_haikou/cluster_layers`.
3. Run `Datasets_haikou/after-cluster-process/store-every-layer-final-order.py` to store all Haikou dataset-related data into MongoDB.
4. Run `Datasets_haikou/after-cluster-process/get-adj-matrices-in.py` and `get-adj-matrices-out.py` to generate inflow and outflow adjacency matrices for Haikou.
5. Run `Datasets_haikou/after-cluster-process/get-final-dataset-in.py` and `get-final-dataset-out.py` to obtain inflow/outflow traffic datasets per node. Normalize using `normalize-sml-dataset.py` (following the method in the TGCN paper).
6. Files like `get-layer{x}-final-order.py`, `adj-heatmap.py`, `before-after-compare.py`, and `draw_adj.py` under `Datasets_haikou/after-cluster-process/` are for visualization purposes in the paper.

## Datasets_Shenzhen
1. Run `Datasets_Shenzhen/pre-process/get-final-dataset-42days.py` to filter the Shenzhen dataset to 42 days (data volume is normal only during this period due to COVID-19 impacts).
2. Run `Datasets_Shenzhen/pre-process/get-diff-granularity-dens.py` to obtain block-wise results at different granularities.
3. Follow the same hierarchical clustering steps as Haikou (scripts under `Datasets_Shenzhen/hierarchical-cluster/`), resulting in four-layer clustering saved in `Datasets_Shenzhen/cluster_layers`.
4. Run `Datasets_Shenzhen/after-cluster-process/store-every-layer-final-order.py` to store Shenzhen data into MongoDB.
5. Run `get-adj-matrices-in.py` and `get-adj-matrices-out.py` under `Datasets_Shenzhen/after-cluster-process/` to generate adjacency matrices.
6. Run `get-final-dataset-in.py`, `get-final-dataset-out.py`, and `normalize-sml-dataset.py` to process Shenzhen’s node-level traffic data.
7. Visualization scripts (e.g., `get-layer{x}-final-order.py`, `adj-heatmap.py`) are used similarly to Haikou for paper figures.

---

# Folders: PyG_Haikou, PyG_Haikou_in, PyG_Shenzhen, PyG_Shenzhen_in, ST-SSL-main-300epoch, STPGCN-2pre

## PyG_Haikou
1. Place the processed Haikou data (from `Datasets_haikou`) into `PyG_Haikou/self_models/recurrent/data/`, including the folders `in`, `in_weighted`, `out`, and `out_weighted`.
2. All files except `run.py` are model-related. Execute `run.py` to obtain experimental results.

## PyG_Haikou_in
1. Follow the same data placement as `PyG_Haikou`, but under `PyG_Haikou_in/self_models/recurrent/data/`.
2. Run `run.py` to execute the models.

## PyG_Shenzhen
1. Place Shenzhen data (from `Datasets_Shenzhen`) into `PyG_Shenzhen/self_models/recurrent/data/`.
2. Run `run.py` for results.

## PyG_Shenzhen_in
1. Same as `PyG_Shenzhen`, but under `PyG_Shenzhen_in/self_models/recurrent/data/`.
2. Execute `run.py`.

## ST-SSL-main-300epoch
1. Place data from both Haikou and Shenzhen into `ST-SSL-main-300epoch/ST-SSL-main/data/`.
2. Run `ST-SSL-main-300epoch/ST-SSL-main/settle_our_datasets.py` to reformat the data for ST-SSL.
3. Execute `run.py` to generate results.

## STPGCN-2pre
1. Place the datasets into `STPGCN-2pre/STPGCN-main/Pytorch/data/dataset/`.
2. Run `STPGCN-2pre/STPGCN-main/Pytorch/run.py` for experimental results.
