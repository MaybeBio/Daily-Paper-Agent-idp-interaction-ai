## Review setup
- **Input scope** Full manuscript text (abstract, introduction, methods, results, discussion, conclusions) without figures, tables, or supplementary materials
- **Assessment boundary** Scientific claims, methodological soundness, and interpretive validity based solely on the provided text; no assessment of figures, tables, or supplementary data that were not supplied
- **Shared manuscript claim summary** The author reports molecular dynamics simulations of human FOXO3, both in implicit solvent (full-length FOXO3/DNA complex) and explicit solvent with accelerated MD (FOXO3120–530), revealing that FOXO3 is largely intrinsically disordered, with two linker regions adjacent to the DNA-binding domain adopting extended conformations due to intramolecular electrostatic repulsion rather than amino acid composition. A new visualization tool, the Local Compaction Plot (LCP), is introduced. The author also reports helical propensity in the KIX-binding region and transactivation domain consistent with templated folding.
- **Visible evidence base** Text descriptions of methods (IUPred2 prediction, sliding window analysis, implicit MD with Amber ff14SBonlysc/GB, explicit MD with TIP4P-D and accelerated MD), results (convergence metrics, secondary structure variability, LCP patterns, PBSA electrostatic analysis, end-to-end distance comparisons), and discussion of implications
- **Missing materials affecting confidence** All figures (Figure 1–7), supplementary figures (Figure S1, S2, S4), Video S1, and all quantitative data (numerical values for distances, RMSD, SASA, secondary structure percentages) are not provided; these are essential for verifying the claims

## Reviewer
- **Overall assessment** The manuscript addresses a relevant and timely topic, namely the structural characterization of an intrinsically disordered transcription factor, FOXO3, using MD simulations. The central claim that electrostatic repulsion between negatively charged domains drives the extended conformation of linker regions is mechanistically plausible and potentially interesting. However, the evidence presented in the text alone is insufficient to establish this claim robustly. The absence of all figures and quantitative data prevents verification of convergence, the LCP methodology, and the electrostatic analysis. The comparison between implicit and explicit solvent results is described qualitatively, and the statistical treatment of the end-to-end distance comparison (FOXO3 FL#2B vs. poly-G/poly-G/S) is not reported. The manuscript would benefit from clearer presentation of the novelty relative to prior IDP simulation studies and from a more critical discussion of the limitations of implicit solvent models and accelerated MD.
- **Who would be interested in the results, and why** Researchers studying intrinsically disordered proteins, transcription factor structure-function relationships, and the role of electrostatic interactions in protein conformation. The LCP tool may be of interest to the computational biophysics community as a visualization method for IDP trajectories. The proposed electrostatic repulsion mechanism could inform experimental studies of FOXO3 regulation, particularly regarding post-translational modifications.
- **Major strengths** The study addresses a biologically important protein with limited structural data. The use of both implicit and explicit solvent simulations, including accelerated MD, is a reasonable approach given the size and disorder of FOXO3. The introduction of the LCP as a visualization tool is a potentially useful methodological contribution. The hypothesis that electrostatic repulsion, rather than sequence-encoded stiffness, drives linker extension is mechanistically interesting and testable.
- **Major Concerns** See detailed items below.
- **Minor Comments** See detailed items below.
- **Technical failings that need to be addressed before the case is established** R1-M1 (lack of quantitative evidence for convergence and LCP), R1-M2 (insufficient evidence for electrostatic repulsion mechanism), R1-M3 (inadequate statistical comparison for the "not sequence-encoded" claim), R1-M4 (unvalidated LCP methodology)
- **Assessment against Nature-style criteria**  
  *Originality*: Moderate. The application of MD to FOXO3 is new, and the electrostatic repulsion hypothesis is a novel interpretation, but the general phenomenon of electrostatic effects on IDP conformation is established. The LCP is a new tool but its novelty relative to existing methods (e.g., contact maps, radius of gyration plots) is not clearly articulated.  
  *Scientific importance*: Potentially significant for understanding FOXO3 regulation and IDP biophysics, but the current evidence does not yet establish the central claim with sufficient rigor.  
  *Interdisciplinary readership*: The topic bridges structural biology, computational biophysics, and cell signaling, but the presentation is likely too specialized for a broad Nature readership without clearer framing of biological implications.  
  *Technical soundness*: The simulation protocols are described in reasonable detail, but the lack of quantitative results and statistical analysis undermines confidence. The use of implicit solvent and accelerated MD is justified, but limitations are not fully discussed.  
  *Readability for nonspecialists*: The manuscript is written in a technical style that assumes familiarity with MD and IDP concepts. The introduction of the LCP is described conceptually but would benefit from a more accessible explanation.
- **Recommendation posture** Currently not established from the provided evidence. The central claims are plausible but not verifiable without the missing figures and quantitative data. The manuscript could become supportive if the technical concerns are addressed with full data presentation and statistical rigor.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence sufficiency
- **Claim pointer** The author claims that "all simulations take a similar path through conformational space and converge on a series of structures within a relatively narrowly defined phase space" (Section 3.1) and that the LCP identifies distinct folded and extended regions.
- **Evidence pointer** Section 3.1, Figure 2, Figure 5; location not provided for quantitative values
- **Concern** The text describes convergence and LCP patterns but provides no numerical data (e.g., RMSD values, distance distributions, confidence intervals) to support these claims. The figures that would show this evidence are not available for review. Without quantitative metrics, it is impossible to assess whether the simulations have converged or whether the LCP patterns are statistically robust.
- **Why it matters** Convergence is a prerequisite for any MD-based structural claim. If the simulations have not converged, the observed extended conformations and LCP patterns could be artifacts of insufficient sampling. The LCP is a new tool, and its reliability depends on the quality and quantity of trajectory data, which cannot be evaluated here.
- **Resolution test** Provide quantitative convergence metrics (e.g., RMSD vs. time, block averaging) and statistical analysis of LCP distance distributions (e.g., mean, standard deviation, percentiles) for all simulations. Show that the extended linker conformations are consistently observed across independent runs and are not outliers.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Causal inference
- **Claim pointer** The author claims that the extended conformation of the linker regions "is not due to their amino acid composition, but rather is caused by electrostatic repulsion of the domains connected by the linkers" (Abstract and Section 3.1).
- **Evidence pointer** Section 3.1, Figure 2C, Figure 6; location not provided for PBSA data
- **Concern** The evidence for the electrostatic repulsion mechanism is indirect. The author shows that FL#2B alone does not exhibit rigidity (Figure 2C), and that the overall complex has a negative charge (Figure 6). However, no direct test of the electrostatic repulsion hypothesis is presented, such as simulations with neutralized charges, varying ionic strength, or mutations that alter charge distribution. The PBSA calculation is described but no quantitative results are given.
- **Why it matters** The central mechanistic claim of the paper rests on this causal inference. Without a direct test, alternative explanations (e.g., excluded volume effects, transient interactions with the DNA, or the presence of the folded DBD) cannot be ruled out. The claim that the effect is "not due to amino acid composition" is a strong negative statement that requires more than a single comparison to poly-G/poly-G/S.
- **Resolution test** Perform control simulations with charge neutralization (e.g., mutating acidic residues to neutral ones) or with altered ionic strength to demonstrate that the extended conformation is specifically dependent on electrostatic repulsion. Provide quantitative PBSA data (e.g., electrostatic potential maps, energy contributions) and statistical comparison of end-to-end distances across conditions.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Statistical rigor
- **Claim pointer** The author claims that the end-to-end distance distribution of FL#2B is "statistically indistinguishable from highly flexible polypeptides of the same length consisting of poly-glycine (poly-G) or alternating glycine and serine residues (poly-G/S)" (Section 3.1).
- **Evidence pointer** Section 3.1, Figure 2C; location not provided for statistical test details
- **Concern** The text states that the distributions are "statistically indistinguishable" but does not report the statistical test used, the sample size (number of frames), or the p-value or effect size. Without this information, the claim of indistinguishability is not verifiable.
- **Why it matters** This comparison is used to argue that the linker sequence itself does not encode rigidity, which is a key part of the argument for the electrostatic mechanism. If the statistical test is underpowered or inappropriate, the conclusion could be wrong.
- **Resolution test** Report the specific statistical test (e.g., Kolmogorov-Smirnov test, permutation test), the number of independent samples, and the resulting p-value or confidence interval. Consider whether the test is adequately powered to detect biologically meaningful differences.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Methodological validation
- **Claim pointer** The author introduces the Local Compaction Plot (LCP) as "a new graphical tool for studying and visualizing the structural diversity of IDPs" (Abstract and Section 3.1).
- **Evidence pointer** Section 3.1, Figure 5; location not provided for software or code availability
- **Concern** The LCP is described conceptually, but no validation is provided. It is unclear how the LCP compares to existing methods (e.g., contact maps, distance maps, or radius of gyration plots). The choice of window size (75 amino acids) is stated but not justified, and the sensitivity of the LCP to this parameter is not explored.
- **Why it matters** If the LCP is to be a useful contribution, it must be shown to be robust and to provide information not readily available from existing tools. Without validation, its utility is uncertain.
- **Resolution test** Provide a comparison of LCP outputs to established metrics (e.g., contact maps, RMSF) for the same trajectories. Justify the window size choice and show that the qualitative conclusions are insensitive to reasonable variations in this parameter. State whether the LCP software is publicly available.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Section 2.2, creation of starting structure
- **Evidence pointer** Section 2.2; location not provided
- **Issue** The method for modeling the missing N- and C-terminal IDR sequences by Markov Chain Monte Carlo is described in one sentence without details on the algorithm, the energy function, or the number of steps. This makes it difficult to assess the quality of the starting structures.
- **Required correction** Provide additional details on the MCMC protocol, including the force field used for the modeling, the length of the simulation, and any validation of the resulting structures (e.g., Ramachandran plots, clash checks).

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Section 2.4, accelerated MD parameters
- **Evidence pointer** Section 2.4; location not provided
- **Issue** The parameters for the accelerated MD (aMD) simulations are not fully specified. The text mentions an α-value of 0.2 but does not report the boost energies (dihedral and total) or how they were calculated.
- **Required correction** Report the specific aMD parameters used, including the boost energies and the criteria for choosing them, to allow reproducibility.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Interpretation
- **Affected element** Section 3.3, helical propensity
- **Evidence pointer** Section 3.3, Figure 7; location not provided
- **Issue** The claim that the KIX-binding region and TAD are "predisposed to form helical conformations" is based on secondary structure analysis of the simulations, but the text does not report the percentage of time these helices are formed or the structural stability of these elements.
- **Required correction** Provide quantitative data on helix occupancy (e.g., fraction of frames with helical structure) and, if possible, the free energy of helix formation, to support the claim of predisposition.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Context
- **Affected element** Section 4, Discussion
- **Evidence pointer** Section 4; location not provided
- **Issue** The discussion of the electrostatic repulsion mechanism does not reference prior experimental or computational studies on electrostatic effects in IDPs, which would help contextualize the novelty of the finding.
- **Required correction** Add citations to relevant literature on electrostatic-driven expansion in IDPs (e.g., studies on polyelectrolyte behavior of disordered proteins) to position the claim within the existing body of knowledge.

## Risk / unsupported claims
- The claim that the extended linker conformation is "caused by electrostatic repulsion" is not directly supported by the provided evidence; no control simulations or quantitative electrostatic analysis are presented.
- The claim that the linker extension is "not due to amino acid composition" is based on a single comparison to poly-G/poly-G/S without reported statistical details.
- The claim that the simulations "converge on a series of structures within a relatively narrowly defined phase space" is unverifiable without quantitative convergence metrics.
- The claim that the LCP is a useful new tool is not validated against existing methods or tested for parameter sensitivity.
- The claim that the KIX-binding region and TAD are "predisposed" to form helices is not quantitatively supported.
- The generalizability of the implicit solvent results to explicit solvent conditions is asserted but not rigorously demonstrated, as the explicit simulations cover only a subregion of the protein.