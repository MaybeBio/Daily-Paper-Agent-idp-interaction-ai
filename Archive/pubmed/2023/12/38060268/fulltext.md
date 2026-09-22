# Local Disordered Region Sampling (LDRS) for ensemble modeling of proteins with experimentally undetermined or low confidence prediction segments


## Summary
  The Local Disordered Region Sampling (LDRS, pronounced loaders) tool is a new module developed for IDPConformerGenerator, a previously validated approach to model intrinsically disordered proteins (IDPs). The IDPConformerGenerator LDRS module provides a method for generating all-atom conformations of intrinsically disordered protein regions at N- and C-termini of and in loops or linkers between folded regions of an existing protein structure. These disordered elements often lead to missing coordinates in experimental structures or low confidence in predicted structures. Requiring only a pre-existing PDB or mmCIF formatted structural template of the protein with missing coordinates or with predicted confidence scores and its full-length primary sequence, LDRS will automatically generate physically meaningful conformational ensembles of the missing flexible regions to complete the full-length protein. The capabilities of the LDRS tool of IDPConformerGenerator include modeling phosphorylation sites using enhanced Monte Carlo-Side Chain Entropy, transmembrane proteins within an all-atom bilayer, and multi-chain complexes. The modeling capacity of LDRS capitalizes on the modularity, the ability to be used as a library and via command-line, and the computational speed of the IDPConformerGenerator platform.


## Availability and implementation
  The LDRS module is part of the IDPConformerGenerator modeling suite version 0.7.23, which can be downloaded from GitHub at https://github.com/julie-forman-kay-lab/IDPConformerGenerator. IDPConformerGenerator is written in Python3 and works on Linux, Microsoft Windows, and Mac OS versions that support DSSP. Users can utilize LDRS’s Python API for scripting the same way they can use any part of IDPConformerGenerator’s API, by importing functions from the “idpconfgen.ldrs_helper” library. Otherwise, LDRS can be used as a command line interface application within IDPConformerGenerator. Full documentation is available within the command-line interface as well as on IDPConformerGenerator’s official documentation pages (https://idpconformergenerator.readthedocs.io/en/latest/).


## Supplementary Material

## Supplementary data
  Supplementary data are available at Bioinformatics online, including all the conformational ensembles and analyses described in this paper.


## Conflict of interest
  None declared.


## Funding
  This work was supported by the National Institutes of Health [5R01GM127627-04 and 2R01GM127627-05 to T.H.-G. and J.D.F.-K.]; the Natural Sciences and Engineering Research Council of Canada [2016-06718 to J.D.F.-K., and RGPIN-2023-04864 to C.C.G.]; and the Canada Research Chairs Program [to J.D.F.-K.].


## Acknowledgements
  We acknowledge Philip Rößler for helping identify the α2A adrenergic receptor system as a transmembrane protein case, and Zhi Wei Zeng for assistance with the protocol to model the bilayer seen in the α2A adrenergic receptor system.