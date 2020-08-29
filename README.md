[![DOI](https://zenodo.org/badge/289968174.svg)](https://zenodo.org/badge/latestdoi/289968174)

# FAIR sharing of molecular visualization experiences

This is a data and code collection (`fair_covid_molvisexp`) for our publication available as preprint on [biorxiv](http://dx.doi.org/10.1101/2020.08.27.270140) experimenting with FAIR sharing of molecular visualization experiences. We initially provide four example scripts for the [UnityMol](http://unitymol.sourceforge.net) software as well as derived media such as images, movies and 3D models.

## Contents

- `overview`: a MarkDown readme file with a table that references all items that were created for this work, including data, software, images, movies, 3D models, web entries in diverse platforms, etc. This should be the starting point to have a global picture on what was implemented. Just ["open" this github subdirectory](overview) in the bowser and github will render the readme file along with all links
- `ex1_spike`: The first example aims at setting up a simple structural view of the SARS spike glycoprotein  complex with human angiotensin-converting enzyme 2 (ACE2). The trimeric complex accessible from PDB-id 6CS2 was used as starting point for many early SARS-CoV-2 studies. The directory contains [UnityMol](http://unitymol.sourceforge.net) scripts, structure and derived media files
- `ex2_binding_sites`: a comparative look at where drug molecules bind to the main protease of Covid-19. The visualization is inspired by the [animation of small molecules in 92 protein databank structures](https://www.rbvi.ucsf.edu/chimerax/data/sars-protease-may2020/) prepared by the [ChimeraX](https://www.cgl.ucsf.edu/chimerax/) team. We created a 3D print of the protease monomer as well. The directory contains [UnityMol](http://unitymol.sourceforge.net) scripts to render the scene or render a movie of it, structure and derived media files
- `ex3_mdtraj`: molecular dynamics simulations provide another inestimable resource for insight into molecular mechanisms. Example 3 is based on a trajectory depicting a binding event of the receptor- binding domain (RBD) of the SARS-CoV-2 spike and the human ACE2 receptor (DESRES-ANTON- [10857295,10895671]) available from [DE Shaw research](https://www.deshawresearch.com/downloads/download_trajectory_sarscov2.cgi/).
- `ex4_bioinfo`:  illustrates a visual experience related to representing the results of bioinformatics analyses. Our example is built upon the freely available data from a recent study on cross-species transmission of SARS-CoV-2, highlighting the species variability of viral-host protein interactions [by Rodrigues et al](https://doi.org/10.1101/2020.06.05.136861). We visually map this data onto the ACE2-RBD complex.

## License

The whole data collection is under the CC-BY International license, see the `LICENSE` file for details.

## Contact

For questions, bugs, suggestions, and further inquiries, please leave an issue here or send the corresponding author an email at baaden [at] smplinux [dot] de
