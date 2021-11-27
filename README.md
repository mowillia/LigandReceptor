# Combinatorial model of ligand-receptor binding

The binding of ligands to receptors is the starting point for many import signal pathways within a cell, but in contrast to the specificity of the processes that follow such bindings, the bindings themselves are often non-specific. Namely, a single type of ligand can often bind to multiple receptors beyond the single receptor to which it binds optimally. This property of ligand-receptor binding naturally leads to a simple question: If a collections of ligands can bind non-specifically to a collection of receptors, but each ligand type has a specific receptor to which it binds most strongly, under what thermal conditions will all ligands bind to their optimal sites?  that is the ligands ligands often bind non-specifically to the collection of receptors in their vicinity. 


<p align="center">
<img src = "https://user-images.githubusercontent.com/8810308/143513360-1df13169-f487-49a8-9f4d-db91cefbfe4a.png" width = "70%">
  <br>
  <em align="center">Depiction of various ligand types binding optimally and sub-optimally to receptors</em>
</p>

  
In this repository, we collect all the simulations that helped us explore this question in the [associated paper](https://arxiv.org/pdf/1909.00455.pdf). In particular, to provide a conceptual handle on the features of optimal and sub-optimal bindings of ligands, we considered an analogous model of colors binding to a grid. 


<p align="center">
<img src = "https://user-images.githubusercontent.com/8810308/143513407-606ec764-efaa-4820-baaf-0dbe4cd3aeef.png" width = "70%">
  <br>
  <em align="center">Partially correct and completely correct binding for the image</em>
</p>
  
In the same way ligands could have certain receptors to which they bind optimally (even though such ligands could bind to many others), each colored square has a certain correct location in the image grid but could exist anywhere on the grid. We have the correct locations form a simple image so that when simulating the system, it is clear by eye whether the system has settled into its completely correct configuration. In all of the notebooks in this repository, we use this system of grid assembly as a toy model to outline the properties of our ligand-receptor binding model. 


## Reproducing figures and tables

Each notebook reproduces a figure in the paper.

- [`simple_particle_binding.ipynb`](https://nbviewer.jupyter.org/github/mowillia/LigandReceptor/blob/master/simple_particle_binding.ipynb): Reproduces Figure 6; Runs in < 5 secs
- [`derangement_model.ipynb`](https://nbviewer.jupyter.org/github/mowillia/LigandReceptor/blob/master/derangement_model.ipynb): Reproduces Figure 7; Runs in ~ 30 minutes
- [`general_grid_assembly.ipynb`](https://nbviewer.jupyter.org/github/mowillia/LigandReceptor/blob/master/general_grid_assembly.ipynb): Reproduces Figure 8; Runs in < 5 secs
- [`search_and_combinatorics.ipynb`](https://nbviewer.jupyter.org/github/mowillia/LigandReceptor/blob/master/search_and_combinatorics.ipynb): Reproduces Figure 9; Runs in < 5 secs
- [`hints_non_equilibrium.ipynb`](https://nbviewer.jupyter.org/github/mowillia/LigandReceptor/blob/master/hints_non_equilibrium.ipynb): Reproduces Figure 10; Runs in < 3 mins


## References
[1] Williams, Mobolaji. "Combinatorial model of ligand-receptor binding" *Physical Review E* 99.4 (2019): 042133.

---
```
@article{williams2021large,
  title={Combinatorial model of ligand-receptor binding},
  author={Williams, Mobolaji},
  journal={arXiv preprint arXiv:2107.14080},
  year={2021}
}
```
