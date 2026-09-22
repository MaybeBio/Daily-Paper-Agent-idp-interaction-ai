## Review setup
- **Input scope** Full manuscript text (abstract, introduction, methods, results and discussion, conclusions) as provided
- **Assessment boundary** Scientific content, methodological soundness, interpretation of results, and alignment with stated conclusions. Editorial and stylistic issues are noted only where they affect scientific clarity.
- **Shared manuscript claim summary** The authors use an AlphaFold-derived model of C. elegans metallothionein I (MTL-1) and all-atom MD simulations to compare the apo form with five metal-bound forms (Zn2+, Cd2+, Cu2+, Pb2+, Hg2+). They report that metal binding generally stabilizes the protein, with Pb2+ being a notable exception, and identify cysteine-dominated coordination with contributions from non-cysteine residues.
- **Visible evidence base** Abstract, full methods section, results and discussion text, tables referenced (Table 1, Table 2), figures referenced (Figures 1-4), supporting information referenced (Figures S1-S9, Table S1)
- **Missing materials affecting confidence** Actual figures and tables are not provided; only references to them in text. Supporting information files are not available. Force field parameter details for metal ions are only partially described. No PDB files, trajectory data, or analysis scripts are provided.

## Reviewer

- **Overall assessment** This manuscript presents a computational study of metal-binding effects on the structural dynamics of C. elegans metallothionein I. The topic is of interest to the metalloprotein and intrinsically disordered protein communities. However, the study has substantial methodological limitations that are not adequately addressed, and several claims go beyond what the evidence can support. The use of nonbonded metal models without explicit coordination restraints is a major concern for a protein whose function depends on specific metal-thiolate cluster formation. The interpretation of "stability" from MD metrics without thermodynamic analysis is also problematic. The manuscript would benefit from more rigorous validation, additional control simulations, and more careful language regarding the limits of the approach.

- **Who would be interested in the results, and why** Researchers studying metallothionein structure and function, particularly those interested in metal selectivity and the role of intrinsic disorder in metal-binding proteins. The comparative analysis across five metals may also be of interest to those studying metal toxicity and detoxification mechanisms in invertebrates. The methodological discussion around using AlphaFold models for disordered proteins in MD simulations could be relevant to computational biologists working on similar systems.

- **Major strengths**
  1. The study addresses a relevant gap by comparing five different metal ions in a systematic manner using the same computational protocol.
  2. The authors acknowledge the limitations of their approach regarding thermodynamic assessment and quantum effects.
  3. The discussion of Pb2+ as an outlier is interesting and potentially biologically relevant.
  4. The use of triplicate simulations is appropriate for assessing reproducibility.

- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors claim that metal coordination "significantly stabilizes" the protein based on reduced RMSD, RMSF, SASA, and Rg values.
- **Evidence pointer** Results and Discussion, "Metal Coordination Enhances Conformational Stability in Flexible MTL-1"; Table 2; Figure 2
- **Concern** The interpretation of reduced RMSD and Rg as "stability" is problematic. These metrics reflect conformational compaction and reduced positional fluctuation relative to the starting structure, not thermodynamic stability. A protein could show low RMSD in a metastable or even non-native state. The authors do acknowledge this in one sentence, but the framing throughout the manuscript consistently equates these metrics with stability. More critically, the use of nonbonded metal models without coordination restraints means the metals are free to diffuse away from the protein. The fact that some metals remain near coordinating residues may reflect the initial placement rather than genuine binding affinity. Without umbrella sampling, free energy calculations, or at minimum distance-restrained simulations to maintain coordination geometry, the observed "stabilization" cannot be attributed to specific metal-protein interactions.
- **Why it matters** The central claim of the paper is that different metals differentially stabilize MTL-1. If the observed effects are artifacts of the nonbonded model or initial conditions, the conclusions are not valid. The distinction between conformational compaction and thermodynamic stability is fundamental to the interpretation.
- **Resolution test** The authors should either (a) perform free energy calculations (e.g., PMF or umbrella sampling) for metal binding at the identified coordination sites, (b) repeat simulations with explicit coordination bonds or restraints based on known metallothionein cluster geometry, or (c) substantially revise the language to clearly state that only conformational metrics are reported and that no claims of thermodynamic stability are made. If option (c) is chosen, the significance of the findings must be reframed accordingly.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors state that "conserved cysteine residues coordinate the metal through strong thiolate interactions" and identify specific residues (Cys12, Cys26, Cys31, Cys40, Cys55) as frequently involved in coordination.
- **Evidence pointer** Results and Discussion, "Variability and Influence of Distinct Metal Ions in MTL-1 Coordination"; Figures S5-S9
- **Concern** The identification of coordination sites is based on distance criteria (<2.0-3.0 Å depending on metal) between the metal ion and amino acid atoms. However, with nonbonded metal models, the metal ions are not constrained to remain near the protein. The observation that some metals maintain proximity to specific cysteines could be due to electrostatic attraction to the negatively charged thiolates, but this does not constitute evidence of a stable coordination bond. Furthermore, the distance thresholds used are quite short for some metals (e.g., <2.0 Å for Cu2+), which may be physically unrealistic for equilibrium distances in metallothionein clusters. The authors do not report the occupancy or persistence of these contacts over time, nor do they analyze the coordination geometry (e.g., tetrahedral vs. linear). Without such analysis, the claim of specific coordination sites is not well supported.
- **Why it matters** The identification of specific coordination residues is a key finding that the authors use to discuss metal selectivity and the role of non-cysteine residues. If the coordination assignments are unreliable, this discussion is built on a weak foundation.
- **Resolution test** The authors should provide time-resolved distance plots for the key metal-cysteine contacts, report the fraction of simulation time each contact is maintained, and analyze the coordination geometry (e.g., number of sulfur ligands within bonding distance, bond angles). If the contacts are transient or the geometry is inconsistent with known metallothionein clusters, the claims should be revised.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Scientific importance
- **Claim pointer** The authors state that their findings "provide new insights into the structural dynamics of metallothionein in response to different metals" and suggest implications for understanding metal selectivity and biological function.
- **Evidence pointer** Abstract; Conclusions
- **Concern** The biological significance of the findings is not well established. The study uses a single AlphaFold-predicted structure as the starting point, which the authors themselves acknowledge has moderate quality (pLDDT ~60, QMEAN -3.43). For an intrinsically disordered protein, the AlphaFold prediction may represent only one of many accessible conformations. The authors do not test whether their conclusions are robust to different starting structures or to the choice of force field. Additionally, the study only examines the fully metalated state (7 ions), whereas the biological function of metallothionein involves progressive metalation and the existence of partially metalated intermediates. The relevance of the fully metalated state to in vivo conditions is not discussed.
- **Why it matters** The claim of providing biological insights requires that the computational model captures biologically relevant states. If the starting structure is not representative and the metalation state is not biologically realistic, the relevance of the findings to actual metallothionein function is unclear.
- **Resolution test** The authors should either (a) perform simulations starting from multiple conformations (e.g., from an ensemble generated by enhanced sampling or from the NMR structure if available) to test robustness, (b) simulate partially metalated states, or (c) clearly state that the study is exploratory and that biological implications are speculative. If option (c) is chosen, the conclusions should be substantially toned down.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Technical soundness
- **Claim pointer** The authors report that "Cu2+ and Cd2+ did not differ significantly (p = 1.0)" in terms of RMSD, and that all metals differed significantly from each other except this pair.
- **Evidence pointer** Results and Discussion, "Metal Coordination Enhances Conformational Stability in Flexible MTL-1"
- **Concern** The statistical analysis is based on a one-way ANOVA with Tukey post hoc tests on RMSD values from the last 50 ns of triplicate simulations. However, RMSD values from MD simulations are highly autocorrelated over time. Treating each frame as an independent observation inflates the effective sample size and can lead to false significance. The reported F-value of 686,602 is extraordinarily high and suggests that the analysis treats each of the 25,000 frames per system as independent. This is statistically invalid. The authors should use block averaging or compare mean values from independent replicates only (n = 3 per system).
- **Why it matters** The statistical claims of significant differences between metals are central to the paper's conclusions. If the analysis is statistically invalid, the conclusions about metal-specific effects are not supported.
- **Resolution test** The authors should redo the statistical analysis using block-averaged RMSD values or by comparing the three replicate means per system using a non-parametric test. The results should be reported with appropriate measures of uncertainty.

- **Concern ID** R1-M5
- **Severity** Major
- **Blocking** No
- **Axis** Technical soundness
- **Claim pointer** The authors state that "Glu residues were particularly important for coordinating Cd and Hg ions along with Cys" and that "Lys, Tyr, and Pro also emerged as bond-stabilizing residues."
- **Evidence pointer** Results and Discussion, "Metal Interactions in MTL-1: Cysteines and Beyond"; Figures S6, S8
- **Concern** The involvement of non-cysteine residues in metal coordination is presented as a notable finding. However, with nonbonded metal models, the metal ions can interact electrostatically with any negatively charged or polar residue. The observation that Glu residues are near the metal does not establish that they participate in coordination in a chemically meaningful way. The authors do not analyze whether these interactions are specific (e.g., whether the carboxylate oxygen is within bonding distance and oriented appropriately) or whether they are merely transient electrostatic contacts. Additionally, the claim that these residues "stabilize" the metal-protein complex is not supported by any energetic analysis.
- **Why it matters** The claim that non-cysteine residues contribute to metal coordination is presented as a novel insight. If these interactions are not genuine coordination bonds, the claim is misleading.
- **Resolution test** The authors should analyze the geometry of the proposed non-cysteine coordination (e.g., metal-oxygen distances and angles for Glu), report the occupancy of these contacts, and compare the interaction energies (e.g., using MM/GBSA or interaction energy decomposition) between cysteine-only and cysteine-plus-non-cysteine coordination scenarios.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Readability
- **Affected element** Abstract
- **Evidence pointer** Abstract
- **Issue** The abstract states that "Metal binding significantly enhanced the protein's stability" without specifying that this refers to conformational stability in MD simulations, not thermodynamic stability. This could mislead readers.
- **Required correction** Add a qualifier such as "conformational stability in MD simulations" or "structural compaction" to the abstract.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Technical soundness
- **Affected element** Methods
- **Evidence pointer** Materials and Methods, "System Preparations for Molecular Dynamic Simulations"
- **Issue** The authors state that all cysteines were modeled as deprotonated thiolates. This is a strong assumption, as the pKa of cysteine in metallothionein can vary depending on the local environment. The authors do not justify this choice or discuss its potential impact on the results.
- **Required correction** Provide a brief justification for the uniform deprotonation, or acknowledge that this is a simplifying assumption and discuss its potential limitations.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Technical soundness
- **Affected element** Methods
- **Evidence pointer** Materials and Methods, "System Preparations for Molecular Dynamic Simulations"
- **Issue** The metal ions were modeled using nonbonded parameters from frcmod.ionslm_126_opc. This is a reasonable choice for a comparative study, but the authors should acknowledge that this approach does not capture charge transfer, polarization, or covalent character in metal-thiolate bonds, which are known to be important in metallothioneins.
- **Required correction** Add a sentence acknowledging this limitation and its potential impact on the interpretation of coordination details.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Scientific importance
- **Affected element** Discussion
- **Evidence pointer** Results and Discussion, "Metal Coordination Enhances Conformational Stability in Flexible MTL-1"
- **Issue** The authors compare their results to experimental studies of metallothionein from other species but do not discuss the sequence differences between C. elegans MTL-1 and the mammalian proteins used in those studies. This limits the strength of the comparison.
- **Required correction** Briefly note the sequence conservation or divergence of the key coordination residues between C. elegans and mammalian metallothioneins.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Readability
- **Affected element** Results and Discussion
- **Evidence pointer** Results and Discussion, "Metal Interactions in MTL-1: Cysteines and Beyond"
- **Issue** The sentence "Confirming, Pb2+ coordinates strongly with some cysteine residues" is awkwardly phrased and the word "Confirming" is unclear.
- **Required correction** Rephrase, e.g., "Consistent with experimental studies, Pb2+ coordinates strongly with some cysteine residues in our simulations."

- **Concern ID** R1-m6
- **Severity** Minor
- **Axis** Technical soundness
- **Affected element** Results and Discussion
- **Evidence pointer** Results and Discussion, "Metal Interactions in MTL-1: Cysteines and Beyond"
- **Issue** The authors mention "the absence of bridging cysteine sulfur" for Pb2+ but do not explain the significance of this observation or how it was determined.
- **Required correction** Provide a brief explanation of what bridging thiolates are, why their absence matters, and how the authors identified this feature in their simulations.

- **Concern ID** R1-m7
- **Severity** Minor
- **Axis** Readability
- **Affected element** Conclusions
- **Evidence pointer** Conclusions
- **Issue** The conclusion states that "Zn2+ (Rg) and Cu2+ (RMSD) inducing the highest levels of compaction and stability" but the text earlier indicates that Cu2+ and Cd2+ had similar RMSD values. The conclusion should be consistent with the results.
- **Required correction** Clarify which metric supports each claim and ensure consistency with the results section.

## Risk / unsupported claims
- The claim that metal binding "significantly enhances stability" is not supported by thermodynamic analysis; only conformational metrics are reported.
- The identification of specific coordination residues (Cys12, Cys26, Cys31, Cys40, Cys55) is based on distance criteria with nonbonded metal models and may not reflect genuine coordination bonds.
- The claim that non-cysteine residues (Glu, Lys, Tyr, Pro) participate in metal coordination is not supported by geometric or energetic analysis.
- The statistical significance of differences between metals is based on an invalid statistical approach that treats autocorrelated MD frames as independent observations.
- The biological relevance of the findings is asserted without testing robustness to starting structure or considering partially metalated states.
- The statement that "the results reveal consistent conformation trends across different metal coordination states" is not supported by a quantitative comparison of the trends across replicates.
- The claim that the AlphaFold model is suitable for MD simulations of this intrinsically disordered protein is not validated by comparison to experimental data or enhanced sampling methods.