# Nuclear Magnetic Resonance-Guided Structural Analysis of Moderate-Affinity Protein Complexes with Intrinsically Disordered Polypeptides


## Abstract
  Binding affinity of an individual binding site of an intrinsically disordered protein for its folded partner may be moderate. In such cases, a straightforward determination of the structure of the binding interface is difficult. We offer a hybrid protocol combining NMR chemical shift information, NMR spectral data on amino acid residue sequence substitution effects, residual dipolar coupling, and molecular dynamics simulation that allowed us to determine the structure of a complex between the intrinsically disordered tropomyosin-binding site of leiomodin and a coiled-coil peptide modeling the N-terminal fragment of tropomyosin. The protocol can be used for other moderate-affinity complexes composed of an intrinsically disordered peptide bound to a structured protein partner.


## Introduction
  The ability of a comparatively small and flexible intrinsically disordered protein (IDP) to extend and simultaneously bind to more than one distant binding site makes IDPs likely components of protein assemblies [1]. By wrapping around a large protein complex, a single IDP chain may tether several well-folded domains and ensure a high level of binding affinity and specificity. Even when each of the binding sites has only a moderate affinity for its binding partner, the multivalent mode of interaction results in a high cumulative strength of binding, an effect known in the field of antibody/antigen interactions as avidity [2]. Additionally, should regulatory processes lead to the need for assembly reorganization, binding domains of flexible IDPs can be displaced from their binding sites one by one. The kinetics of such multi-step mechanism of dissociation can be significantly faster than that of a dissociation following a two-state mechanism [3].

  While moderate affinity of individual binding sites in a multivalent IDP provides a clear benefit for biological functions and regulation [4], it represents a considerable challenge for research if the goal is to determine the three-dimensional (3D) structure of the assembly. A common deconstruction approach which focuses on determining the structure of complexes between two components of the assembly is often problematic. Attempts to co-crystallize domains with low binding affinities may be unsuccessful [5, 6]. Fusing IDP domains with domains improving the binding helps co-crystallizing protein complexes [7], but may introduce misleading structural artifacts [8]. The usefulness of standard protein NMR is also limited, because kinetic processes of dissociation/association of a moderate-affinity protein complex lead to resonance line broadening [9]. Line broadening interferes with peak assignments and complicates collection of a sufficient number of structural restraints required for a high-definition structure.

  When—due to their inherent limitations—classical methods of protein structure determination fail, hybrid methods of protein structure determination come to the forefront [10]. The general philosophy of hybrid methods is to generate a low-resolution structure from sparse data obtained by a range of structural methods and further refine it using computational techniques. In cases when NMR spectra are broadened non-uniformly, a partial spectral assignment is often possible, which can be used in combination with other methods to determine the structure [11]. The protocol described below uses a combination of NMR chemical shift information, effects of amino acid residue substitution on NMR spectra, residual dipolar coupling data, and molecular dynamics simulation to determine the structure of a complex between the tropomyosin-binding site of leiomodin and a peptide modeling the N-terminal fragment of tropomyosin [11]. Although the structure did not achieve the level of definition typical of an NMR structure of a well-behaved protein of equal size, it resolved a long-standing debate about the role of leiomodin in actin filament length regulation and maintenance.

  Hybrid approaches tend to require case-by-case strategies of data collection and interpretation and therefore they are difficult to standardize. However, although the protocol presented here was developed specifically for the leiomodin/tropomyosin complex, many aspects of it can be generalized for other protein complexes. First, all the expertise required to follow this protocol—from cloning and site-directed mutagenesis to recombinant protein production, isotope labeling, NMR data collection/interpretation, and molecular modeling—is present in a typical protein NMR lab. Second, the expression protocol makes use of MFH, a reliable expression tag designed to produce mg quantities of disordered peptides and IDPs in Escherichia coli [12]. We have used it extensively to successfully produce a wide range of disordered peptides or peptides capable of spontaneous refolding [5, 13–15]. Although the MFH tag is directed to inclusion bodies in cells, it is very soluble upon extraction and does not precipitate in non-denaturing buffers, which makes it very useful [12]. Finally, mutagenesis or chemical modification of amino acid residues exposed on the surface of a well-folded component of the complex will produce a clear-cut localized response of an IDP NMR spectrum which helps map the interaction interface between an IDP and its partner. The sensitivity of chemical shifts of IDP NMR peaks allows one to make these substitutions very similar in chemical nature so as not to destroy the binding.

  The following protocol details preparation and structure determination of the complex formed by two peptides, Lmod2s1 and αTM1a1–14Zip. Lmod2s1 is an intrinsically disordered tropomyosin-binding region of leiomodin-2, a protein involved in regulation of the actin-thin filament length [16]. αTM1a1–14Zip is a folded chimeric coiled-coil peptide modeling the N-terminus of tropomyosin, a protein bound to the actin filament and leiomodin-2 [13]. In this protocol we will report the preparation of Lmod2s1, the intrinsically disordered part of the complex. However, the preparation of the well-folded αTM1a1–14Zip will not be covered, since approaches to express, isotopically label, and purify soluble folded proteins and their mutants at high yields are well known. Interested readers will find the details of recombinant production and purification of αTM1a1–14Zip in our earlier work [11, 13].


## Materials

### Expression and Purification of the Lmod2s1 Peptide

#### BL21(DE3) Transformation

#### Expression of a 15N, 13C-Labeled Fusion Protein

#### Ni-NTA Purification of the Fusion Protein

#### Fusion Protein Cleavage with Cyanogen Bromide (see Note 5)

#### Desalting of Cleaved Fusion Proteins

#### The Removal of the Tag Protein

#### Orthogonal Two-Step Reversed-Phase HPLC Purification of the Recombinant Peptides

### NMR Data Collection and Analysis

#### NMR Sample Preparation

#### NMR Spectra Collection and Analysis

#### Influence of Amino Acid Substitution in the Folded Component of the Complex on the IDP Spectra

### NMR-Guided Molecular Dynamics Simulations (MDS) of the Lmod2s1 and αTM1a1–14Zip Complex

## Methods

### Expression and Purification of Lmod2s1

#### BL21(DE3) Transformation by Heat Shock

#### Expression of a 15N, 13C-Labeled Fusion Protein (see Note 9)

#### Ni-NTA Purification of the Fusion Protein (see Note 12)

#### Fusion Protein Cleavage with Cyanogen Bromide (see Note 5)

#### Desalting of Cleaved Fusion Proteins

#### The Removal of the Tag Protein

#### Orthogonal Two-Step Reversed-Phase HPLC Purification of Lmod2s1

### NMR Data Collection and Analysis

#### NMR Sample Preparation

#### NMR Spectra Collection and Analysis

#### Influence of Amino Acid Substitution in the Folded Component of the Complex on the IDP Spectra (see Note 25)

### NMR-Guided MDS of the Lmod2s1/α TM1a1–14Zip Complex

#### Generation of the Initial Structures of the Lmod2s1 and αTM1a1–14Zip Complexes

#### Running NMR-Guided NVT MDS with Dihedral Angle Restraints to Equilibrate the Initial Structure

#### Running NMR-Guided Simulated Annealing MDS with Dihedral Angle Restraints to Eliminate Potential Metastable States

#### Running NMR-Guided NPT Production MDS with Dihedral Angle Restraints to Sample Many Conformations (see Note 37)

#### Refine the Structure by Running NMR-Guided MDS with Dihedral Angle and Residual Dipolar Coupling Restraints (see Note 38)

## Notes

## Acknowledgement
  This work was supported by the National Institutes of Health grant GM120137 to ASK.