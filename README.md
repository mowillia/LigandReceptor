# Combinatorial model of ligand-receptor binding

The binding of ligands to receptors is the starting point for many import signal pathways within a cell, but in contrast to the specificity of the processes that follow such bindings, the bindings themselves are often non-specific. Namely, a single type of ligand can often bind to multiple receptors beyond the single receptor to which it binds optimally. This property of ligand-receptor binding naturally leads to a simple question:

>If a collection of ligands can bind non-specifically to a collection of receptors, but each ligand type has a specific receptor to which it binds most strongly, under what thermal conditions will all ligands bind to their optimal sites? 


<p align="center">
<img src = "https://user-images.githubusercontent.com/8810308/143513360-1df13169-f487-49a8-9f4d-db91cefbfe4a.png" width = "70%">
  <br>
  <em align="center">Depiction of various ligand types binding optimally and sub-optimally to receptors</em>
</p>

  
In this repository, we collect all the simulations that helped us explore this question in the [associated paper](https://arxiv.org/pdf/XYXY.XXXX.pdf). In particular, to provide a conceptual handle on the features of optimal and sub-optimal bindings of ligands, we considered an analogous model of colors binding to a grid. 


<p align="center">
<img src = "https://user-images.githubusercontent.com/8810308/143513407-606ec764-efaa-4820-baaf-0dbe4cd3aeef.png" width = "70%">
  <br>
  <em align="center">Partially correct and completely correct binding for the image</em>
</p>
  
In the same way ligands could have certain receptors to which they bind optimally (even though such ligands could bind to many others), each colored square has a certain correct location in the image grid but could exist anywhere on the grid. We have the correct locations form a simple image so that, when simulating the system, it is clear by eye whether the system has settled into its completely correct configuration. In all of the notebooks in this repository, we use this system of grid assembly as a toy model to outline the properties of our ligand-receptor binding model. 


## Reproducing figures and tables

Each notebook reproduces a figure in the paper.

- [`simple_particle_binding.ipynb`](https://nbviewer.jupyter.org/github/mowillia/LigandReceptor/blob/main/simple_particle_binding.ipynb): Reproduces Figure 6; Runs in ~ 3 mins
- [`derangement_model.ipynb`](https://nbviewer.jupyter.org/github/mowillia/LigandReceptor/blob/main/derangement_model.ipynb): Reproduces Figure 7; Runs in ~ 10 mins
- [`general_grid_assembly.ipynb`](https://nbviewer.jupyter.org/github/mowillia/LigandReceptor/blob/main/general_grid_assembly.ipynb): Reproduces Figure 8; Runs in ~ 15 mins
- [`search_and_combinatorics.ipynb`](https://nbviewer.jupyter.org/github/mowillia/LigandReceptor/blob/main/search_and_combinatorics.ipynb): Reproduces Figure 9; Runs in ~ 45 min
- [`hints_non_equilibrium.ipynb`](https://nbviewer.jupyter.org/github/mowillia/LigandReceptor/blob/main/hints_non_equilibrium.ipynb): Reproduces Figure 10; Runs ~ 4 mins

## Simulation Scheme

For these simulations, we needed to define a microstate,  the probability of transitions between microstates, and the types of transitions between microstates.

**Microstate Definition**

A microstate of our system was defined by two lists: one representing the collection of unbound particles, and the other representing particles bound to their various binding sites. The particles themselves were denoted by unique strings and came in multiple copies according to the system parameters. For example, a system with R = 3 types of particles with `n1 = 2`, `n2 = 3`, and `n3 = 1` could have a microstate defined by `unbound_particles = [A2, A2, A3]` and `bound_particles = [A1, −, A2, −, A1, −]` where “−” in the bound list stands for an empty binding site.

Since the number of optimally bound particles was an important observable for the system, we also needed to define the optimal binding configuration for the microstates. Such an optimal configuration was chosen at the start of the simulation and was defined as a microstate with no unbound particles and all the bound particles in a particular order. For example, using the previous example, we might define the optimal binding configuration as `optimal_bound_config = [A1, A1, A2, A2, A2, A3]`, in which case the number of optimally bound particles of each type in `bound_particles = [A1,−,A2,−,A1,−]` is `m1 = 1`, `m2 = 1`, and `m3 = 0`. The number of bound particles of each type is `k_1 = 2`, `k_2 = 1`, and `k_3 = 0`. We note that the order of the elements in `unbound_particles` is not physically important, but, since the number of optimally bound particles is an important observable, the order of the elements in `bound_particles` is physically important.

For these simulations, the energy of a microstate with `k[i]` bound particles of type `i` and `m[i]` optimally bound particles of type `i` was defined as

```
E(k, m) = Sum^R_i (m[i] log delta[i] + k[i] log gamma[i])
```

where `k=[k1,k2,...,,kR]` and `m=[m1,m2,...,mR]`, `gamma[i]` is the binding affinity, and `delta[i]` is the optimal binding affinity of particle of type `i`.
For transitioning between microstates, we allowed for three different transition types: Particle binding to a site; particle unbinding from a site; permutation of two particles in two different binding sites. Particle binding and unbinding both occur in real physical systems, but permutation of particle positions is unphysical. This latter transition type was included to ensure an efficient-in-time sampling of the state space. *(Note: For simulations of equilibrium systems it is valid to include physically unrealistic transition types as long as the associated transition probabilities obey detailed balance.)*

**Transition Probability**

At each time step, we randomly selected one of the three transition types with (equal probability for each type), then randomly selected the final proposed microstate given the initial microstate, and finally computed the probability that said proposal was accepted. By the Metropolis Hastings algorithm, the probability that the transition is accepted is given by

```
prob(init → fin) = min{1, exp(- β(Efin −Einit))*π(fin → init)/π(init → fin) }
```

where `Einit` is the energy of the initial microstate state and `Efin` is the energy of the final microstate. The quantity `π(init → fin)` is the probability of randomly proposing the final microstate state given the initial microstate state and `π(fin → init)` is defined similarly. The ratio `π(fin → init)/π(init → fin)` varied for each transition type. Below we give examples of these transitions along with the value of this ratio in each case. In the following, `Nf` and `Nb` represent the number of free particles and the number of bound particles, respectively, before the transition.

**Types of Transitions**

- **Particle Binding to Site:** One particle was randomly chosen from the `unbound_particles` list and placed in a randomly chosen empty site in the `bound_particles` list. `π(fin → init)/π(init → fin) = Nf^2/(Nb +1)`.

Example: `unbound_particles = [A2, A2, A3]` and `bound_particles = [A1, −, A2, −, A1, −]` →
`unbound_particles = [A2, A3]` and `bound_particles = [A1, A2, A2, −, A1, −]`; `π(fin → init)/π(init → fin) = 9/4`
- **Particle Unbinding from Site:** One particle was randomly chosen from the `bound_particles` list and placed in the `unbound_particles` list. `π(fin → init)/π(init → fin) = Nb/(Nf + 1)^2`.

Example: `unbound_particles = [A2, A2, A3]` and `bound_particles = [A1, −, A2, −, A1, −]` →
`unbound_particles = [A2, A2, A3, A2]` and `bound_particles = [A1, −, −, −, A1, −]`;
`π(fin → init)/π(init → fin) = 3/16`
- **Particle Permutation:** Two randomly selected particles in the `bound_particles` list switched positions.  `π(fin → init)/π(init → fin) = 1`.

Example: `unbound_particles = [A2, A2, A3]` and `bound_particles = [A1, −, A2, −, A1, −]` →
`unbound_particles = [A2, A2, A3]` and `bound_particles = [A2, −, A1, −, A1, −]`;
`π(fin → init)/π(init → fin) = 1`

For impossible transitions (e.g., particle binding when there are no free particles) the probability for accepting the transition was set to zero. At each temperature, the simulation was run for anywhere from 10,000 to 30,000 time steps (depending on convergence properties), of which the last 2.5% of steps were used to compute ensemble averages of ⟨k⟩ and ⟨m⟩. These simulations were repeated five times, and each point in Fig. 6b, Fig. 7b, Fig. 8b, and Fig. 9 in the paper represents the average ⟨k⟩ and ⟨m⟩ over these five runs. 


## References

[1] Mobolaji Williams. "Combinatorial model of ligand-receptor binding." *Journal Name.* 2021. [[arxiv]](https://arxiv.org/abs/XYXY.XXXX)

---
```
@article{williams2021large,
  title={Combinatorial model of ligand-receptor binding},
  author={Williams, Mobolaji},
  journal={arXiv preprint arXiv:XYXY.XXXX},
  year={2021}
}
```
