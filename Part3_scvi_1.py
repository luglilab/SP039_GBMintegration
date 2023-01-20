#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import scanpy as sc
import scanpy.external as sce
import scrublet as scr
import celltypist
from celltypist import models
import decoupler as dc
import matplotlib.pyplot as plt
import seaborn as sns
sc.set_figure_params(dpi=150)
import scanpy.external as sce


# In[2]:


import scvi


# # Import file

# In[3]:


adata = sc.read("/home/lugli/spuccio/Projects/SP039/SCVI_model/adata_raw.h5ad")

adata = adata[~adata.obs['PanglaoDB_Classification'].isin(["Smooth muscle cells",
                                                   "Pulmonary alveolar type II cells",
                                                  "Pyramidal cells",
                                                  "Pulmonary alveolar type I cells",
                                                  "Plasmacytoid dendritic cells",
                                                  "Oligodendrocyte progenitor cells",
                                                  "Neutrophils",
                                                  "Müller cells",
                                                  "Kupffer cells",
                                                  "Interneurons"]),:]

sc.pp.highly_variable_genes(
    adata,
    n_top_genes=2000,
    layer="counts",
    flavor="seurat_v3"
)

# In[4]:


# subset to highly variable genes
adata = adata[:, adata.var.highly_variable].copy()


# In[5]:


#adata = adata[adata.obs_names.isin(adata.obs['leiden'].dropna().index),:]


# In[6]:


sc.pp.scale(adata) # z normalize the columns (genes)
sc.tl.pca(adata)


# In[7]:


sc.pp.neighbors(adata)


# In[8]:


# tell scvi where to get the data
scvi.model.SCVI.setup_anndata(adata, layer="counts", batch_key = 'Cohort',categorical_covariate_keys=["Sample"])


# In[16]:


model = scvi.model.SCVI(adata)


# In[17]:


model.view_anndata_setup()


# In[ ]:


model.train(use_gpu=False)


# In[ ]:


model.save("/home/lugli/spuccio/Projects/SP039/SCVI_model/modelscvi_cohort", overwrite=True)
adata.obsm["X_scvi"] = model.get_latent_representation()
adata.layers["scvi_expr"] = model.get_normalized_expression(adata, n_samples=5, return_mean=True)
adata.write("/home/lugli/spuccio/Projects/SP039/SCVI_model/adata_scvi.h5ad")


