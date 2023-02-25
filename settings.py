### Edge and Hyper-edge calculation ###
# Connectivity radius is specified in data/metadat.json!
# construct initial hypergraph using: "Dynamic Hypergraph Neural Networks" https://www.ijcai.org/proceedings/2019/0366.pdf #Algo 1 + smol extension.
settings_hyperedges         = False # if true, returns hyper-edges as opposed to normal edges.
# Settings for Normal Edges:
settings_radius_clustering  = False # Radius
settings_knn_clustering     = False # K nearest neighbours
settings_kmeans_clustering  = False # Split nodes into k clusters
# Settings for hyper-edges


# Shared Settings
k_nn_nr = 4     #number of k nearest neighbours to use

### End Hyper-edge Calculation ###