# Local Disordered Region Sampling (LDRS) for Ensemble Modeling of Proteins with Experimentally Undetermined or Low Confidence Prediction Segments


## SUMMARY
  The Local Disordered Region Sampling (LDRS, pronounced loaders) tool, developed for the IDPConformerGenerator platform (Teixeira et al. 2022), provides a method for generating all-atom conformations of intrinsically disordered regions (IDRs) at N- and C-termini of and in loops or linkers between folded regions of an existing protein structure. These disordered elements often lead to missing coordinates in experimental structures or low confidence in predicted structures. Requiring only a pre-existing PDB structure of the protein with missing coordinates or with predicted confidence scores and its full-length primary sequence, LDRS will automatically generate physically meaningful conformational ensembles of the missing flexible regions to complete the full-length protein. The capabilities of the LDRS tool of IDPConformerGenerator include modeling phosphorylation sites using enhanced Monte Carlo Side Chain Entropy (MC-SCE) (Bhowmick and Head-Gordon 2015), transmembrane proteins within an all-atom bilayer, and multi-chain complexes. The modeling capacity of LDRS capitalizes on the modularity, ability to be used as a library and via command-line, and computational speed of the IDPConformerGenerator platform.


## Supplementary Material

## ACKNOWLEDGEMENTS
  This work was supported by the National Institutes of Health [5R01GM127627-04 and 2R01GM127627-05] to T.H.-G. and J.D.F.-K.; the Natural Sciences and Engineering Research Council of Canada (NSERC) [2016-06718] to J.D.F.-K.; the Canada Research Chairs Program to J.D.F.-K.; and NSERC [RGPIN-2023-04864] to C.C.G. We acknowledge Philip Rößler for helping identify the α2A adrenergic receptor system as a transmembrane protein case, and Zhi Wei Zeng for assistance with the protocol to model the bilayer seen in the α2A adrenergic receptor system.