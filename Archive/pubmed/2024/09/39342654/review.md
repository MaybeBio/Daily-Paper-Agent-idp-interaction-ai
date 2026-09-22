## Review setup
- **Input scope** Full manuscript text (abstract, introduction, methods, results, discussion, conclusions) without figures or supplementary material
- **Assessment boundary** Scientific claims, methodological soundness, and interpretive validity based solely on the provided text; figures, tables, and supplementary data referenced but not directly examined
- **Shared manuscript claim summary** The authors use all-atom discrete molecular dynamics (DMD) simulations of the TDP-43 low-complexity domain (LCD) and four disease-associated mutants to infer that dimerization propensity correlates with liquid-liquid phase separation (LLPS) propensity, that the dimerization process is dynamic and heterogeneous with multiple bound states, and that specific hydrophobic and aromatic residue clusters act as "stickers" driving self-association.
- **Visible evidence base** Text descriptions of simulation protocols, secondary structure analyses, contact probability calculations, free energy surfaces, and comparisons to published experimental data; figures and supplementary items are referenced but not visible
- **Missing materials affecting confidence** All figures (Figures 1-7), supplementary figures (S1-S13), and supplementary tables; simulation parameter files; force field validation details; raw trajectory analyses; convergence metrics beyond those described in text

## Reviewer
- **Overall assessment** The manuscript addresses an important and timely question regarding the molecular drivers of TDP-43 LCD phase separation. The use of all-atom DMD to probe dimerization as a proxy for LLPS is a reasonable and computationally tractable strategy. The reported agreement with experimental mutation effects is encouraging. However, several methodological and interpretive issues require clarification. The central assumption that dimerization propensity directly reflects LLPS propensity is plausible but not rigorously established. The identification of "hot spots" relies on contact frequency analyses whose statistical significance is not fully demonstrated. The distinction between low- and high-contact states, while interesting, needs stronger quantitative support. The manuscript would benefit from clearer articulation of what is novel relative to prior simulation studies of TDP-43.
- **Who would be interested in the results, and why** Researchers studying phase separation of intrinsically disordered proteins, particularly those focused on TDP-43 biology and neurodegeneration. Computational biophysicists interested in all-atom simulation approaches for IDPs. Experimental groups working on LLPS mechanisms who could use the identified interaction hotspots as targets for mutagenesis or drug design.
- **Major strengths** The study addresses a significant gap in understanding the molecular-level interactions driving TDP-43 LLPS. The use of all-atom DMD with microsecond timescales represents a methodological advance over coarse-grained approaches. The validation against multiple experimental datasets (NMR secondary structure, mutation effects on LLPS) strengthens confidence in the simulations. The identification of multiple interaction regions beyond the previously characterized helical domain provides a more comprehensive picture. The dynamic view of dimerization with elastic and inelastic collisions is physically insightful.
- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Claim-evidence alignment
- **Claim pointer** The manuscript claims that dimerization propensity, as measured by contact probability in simulations, reflects LLPS propensity, and that this correlation "fully" agrees with experimental reports.
- **Evidence pointer** Results section "The dimerization propensity of TDP-43 LCD wild type and four mutants correlated with corresponding LLPS propensities"; Figure 3
- **Concern** The central assumption that dimerization propensity is a valid proxy for LLPS propensity is asserted but not rigorously justified. The authors cite Flory-Huggins theory, but the connection between a two-molecule dimerization simulation and macroscopic phase separation involves significant extrapolation. The reported contact probabilities (25.12% for WT, ranging from 20.22% to 33.21% for mutants) show modest differences, and the statistical significance of these differences is not reported. No error bars, confidence intervals, or replicate analyses are described for the contact probability measurements.
- **Why it matters** If the dimerization-to-LLPS extrapolation is not valid, the central conclusion of the paper is undermined. The quantitative differences between mutants are small, and without statistical rigor, the claimed "full" agreement with experiments cannot be properly evaluated.
- **Resolution test** Provide statistical analysis of contact probabilities across independent simulations (e.g., standard errors, confidence intervals). Justify the dimerization-to-LLPS connection more rigorously, perhaps by comparing dimerization free energies with experimentally measured LLPS critical concentrations or by showing that the identified interaction hotspots are also enriched in higher-order oligomer simulations.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Methodological soundness
- **Claim pointer** The manuscript claims that the DMD simulations with the Medusa force field accurately capture the structural and interaction properties of TDP-43 LCD, validated by agreement with NMR secondary structure data.
- **Evidence pointer** Methods section "Discrete molecular dynamics simulations"; Results section "Structural dynamics of the TDP-43 low-complexity domain monomer"; Figure 1
- **Concern** The validation of the force field and simulation protocol is incomplete. The authors state agreement with NMR secondary chemical shifts and δ2D predictions, but the quantitative comparison is not shown in the text. The choice of the Medusa force field, which is not among the most commonly used force fields for IDP simulations, requires stronger justification. The implicit solvation model (EEF1) and Debye-Huckel electrostatics are approximations that may affect IDP conformational ensembles. The simulation length (750 ns per run) may be insufficient for full convergence of IDP dimerization dynamics, and no convergence tests are described for the dimer systems.
- **Why it matters** The reliability of all conclusions depends on the accuracy of the simulation methodology. If the force field or sampling is inadequate, the identified interaction hotspots and the dynamic picture of dimerization may be artifacts.
- **Resolution test** Provide quantitative comparison between simulated and experimental secondary structure propensities (e.g., RMSD values). Show convergence tests for dimer simulations (e.g., block averaging, multiple independent runs reaching similar distributions). Justify the choice of Medusa force field for IDP simulations, possibly with benchmark comparisons against other force fields on similar systems.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Interpretive validity
- **Claim pointer** The manuscript claims that the dimerization process involves distinct "low-contact" and "high-contact" states, with the high-contact state potentially initiating amyloid fibrillization.
- **Evidence pointer** Results section "TDP-43 LCD peptides involved in elastic collision and also inelastic collisions with both low- and high-contact bound states"; Figures 6 and 7
- **Concern** The identification of two distinct bound states is based on a piecewise linear fit to the probability distribution of contact numbers, with a crossover at approximately 160 contacts. The statistical support for this bimodal interpretation is not provided. The authors do not show whether alternative models (e.g., a single continuous distribution) fit the data comparably. The claim that the high-contact state facilitates amyloid fibrillization is speculative, as no direct evidence linking the simulated high-contact state to fibril formation is presented.
- **Why it matters** The two-state interpretation is used to support a mechanistic model of LLPS and fibrillization. If the distinction between low- and high-contact states is not robust, the mechanistic conclusions are weakened.
- **Resolution test** Provide statistical model comparison (e.g., AIC or BIC) for one versus two-state fits. Show that the high-contact state is enriched in inter-peptide contacts involving known amyloidogenic regions. If possible, compare the simulated high-contact state with experimentally derived fibril structures.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Novelty and contextualization
- **Claim pointer** The manuscript claims to provide "for the first time, a comprehensive picture of the intermolecular interactions driving the phase separation of TDP-43 LCD."
- **Evidence pointer** Introduction; Conclusions
- **Concern** The claim of providing a "comprehensive picture for the first time" is overstated. Previous simulation studies, including the cited work by Conie et al., have examined TDP-43 dimerization and identified interaction hotspots. The present study extends this work to the full LCD and includes additional mutants, but the conceptual framework (stickers-and-spacers, hydrophobic and aromatic interactions) is well established in the LLPS field. The authors should more carefully position their work relative to prior computational studies of TDP-43 and other IDPs.
- **Why it matters** Overstated novelty claims can undermine the credibility of the work and may not accurately represent the field's state.
- **Resolution test** Revise the novelty claim to be more specific about what is new (e.g., full-length LCD coverage, systematic mutant comparison, identification of specific interaction networks) rather than claiming a "first comprehensive picture."

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity and presentation
- **Affected element** Abstract and Introduction
- **Evidence pointer** Abstract; Introduction, first paragraph
- **Issue** The abstract and introduction use the term "elastic collision" without defining it in the context of protein interactions. The distinction between "elastic" and "inelastic" collisions is not standard terminology in the LLPS field and may confuse readers.
- **Required correction** Define these terms clearly when first used, or use more standard terminology such as "transient encounters" and "stable associations."

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Technical completeness
- **Affected element** Methods section
- **Evidence pointer** Methods section "Simulation setups"
- **Issue** The methods state that "fifty independent simulations" were performed for each system, but the criteria for determining that this number is sufficient for convergence are not described. The text also does not specify how the initial conformations were selected from the equilibrated monomeric ensembles.
- **Required correction** Add a brief description of convergence assessment and the rationale for the number of independent simulations. Specify the selection criteria for initial dimer conformations.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Interpretive caution
- **Affected element** Results section
- **Evidence pointer** Results section "Self-association of TDP-43 LCD was driven by multiple hot-spots featuring hydrophobic clusters and aromatic residues"
- **Issue** The authors state that identified residues "act as stickers" in the stickers-and-spacers model, but the simulations only probe dimerization, not the network formation that occurs in macroscopic phase separation. The extrapolation from dimer contacts to sticker behavior in a phase-separated network is reasonable but should be explicitly acknowledged as an inference.
- **Required correction** Add a sentence acknowledging that the sticker assignment is inferred from dimerization data and would benefit from validation in higher-order oligomer or condensed-phase simulations.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Data presentation
- **Affected element** Results section
- **Evidence pointer** Results section "The dimerization propensity of TDP-43 LCD wild type and four mutants correlated with corresponding LLPS propensities"
- **Issue** The text reports contact probabilities as single values (e.g., 25.12% for WT) without any measure of variability. Given the stochastic nature of simulations, reporting only point estimates is insufficient.
- **Required correction** Report mean values with standard deviations or standard errors across the 50 independent simulations.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Referencing
- **Affected element** Introduction
- **Evidence pointer** Introduction, paragraph 2
- **Issue** The introduction cites "Conie et al." in the context of prior simulation work, but the reference list is not provided in the submitted text. The citation style is inconsistent with the rest of the manuscript.
- **Required correction** Ensure all citations are complete and consistently formatted.

## Risk / unsupported claims
- The claim that dimerization propensity "fully" correlates with LLPS propensity across all five simulated variants is not quantitatively supported in the provided text; no statistical measures are given.
- The identification of four "crucial regions" as stickers for LLPS is based on dimerization contact frequencies; the extension to macroscopic phase separation is an inference not directly tested.
- The claim that the high-contact state "facilitates amyloid fibrillization" is speculative; no direct evidence linking the simulated state to fibril formation is presented.
- The statement that the study provides "a comprehensive picture of the intermolecular interactions driving the phase separation" is not fully supported given that only dimerization, not higher-order assembly or condensed-phase behavior, was simulated.
- The agreement between simulated secondary structure propensities and NMR data is stated but not quantitatively demonstrated in the text.
- The statistical significance of differences in contact probabilities between WT and mutants is not reported, making the claimed correlations with experimental LLPS data difficult to evaluate.