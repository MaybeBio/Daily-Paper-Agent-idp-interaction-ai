## Review setup
- **Input scope** Full manuscript text including abstract, results, discussion, experimental procedures, and supporting information references.
- **Assessment boundary** Scientific content, experimental design, data interpretation, and claims as presented in the provided manuscript text. No external data or supplementary files were available for direct inspection.
- **Shared manuscript claim summary** The authors propose that N-terminal intrinsic disorder in Gγ subunits is an ancestral, evolutionarily conserved feature. Using a stepwise mutagenesis approach in yeast Ste18, they convert the disordered N-terminus into an α-helix and report that this structural transition reduces Ste18 protein abundance (proteasome-independently), dampens the Fus1/MAPK (Ste5) signaling axis, and enhances the Far1-dependent polarization and cell cycle arrest axes, thereby shifting Gβγ signaling bias.
- **Visible evidence base** Main text figures (Figs. 1–6), supplementary figure/table references (Figs. S1–S8, Tables S1–S4), methods descriptions for CD, MD, ancestral reconstruction, yeast assays, and statistical analyses.
- **Missing materials affecting confidence** Supplementary figures and tables (S1–S8, S1–S4) were not provided. Raw data, uncropped blots, MD simulation details, and the custom MATLAB analysis code were not available for verification. Statistical details for microscopy analyses were referenced to supplementary information but not shown.

## Reviewer
- **Overall assessment** This manuscript addresses an interesting and timely question regarding the functional role of intrinsically disordered regions in G protein signaling, specifically the Gγ subunit. The evolutionary analysis is compelling and suggests ancestral conservation. The genetic titration approach to convert disorder to order is creative. However, the central claims regarding signaling bias are weakened by unresolved confounding factors, particularly the dramatic reduction in Ste18 protein abundance for the more helical mutants (M3/M4). The authors attempt to control for this via overexpression, but the comparison is imperfect and the interpretation of "signaling bias" versus "reduced overall Gβγ output" remains ambiguous. The manuscript is technically sound in many respects but requires substantial revision and additional experimentation to firmly establish the proposed model.
- **Who would be interested in the results, and why** Researchers in G protein-coupled receptor (GPCR) signaling, particularly those studying Gβγ subunit function and signaling specificity. Also, biochemists and structural biologists interested in the functional consequences of intrinsic disorder in signaling proteins. The evolutionary analysis may appeal to a broader audience studying protein evolution.
- **Major strengths**
  1. The evolutionary analysis using ancestral sequence reconstruction to demonstrate the ancestral nature of Gγ N-terminal disorder is novel and well-presented.
  2. The stepwise genetic approach to titrate disorder-to-order transitions is creative and represents a methodological advance for studying IDRs in a native context.
  3. The combination of in vitro (CD), in silico (MD, ancestral reconstruction), and in vivo (yeast signaling assays) methods provides a multi-faceted approach.
  4. The inclusion of isometric control mutations (C1, C2) is a thoughtful experimental design to control for sequence-specific effects.
- **Major Concerns**
  - **Concern ID** R1-M1
  - **Severity** Major
  umber **Blocking** Yes
  - **Axis** Data interpretation / Confounding variables
  - **Claim pointer** The claim that helix-stabilizing mutations "shift the signaling bias of Gβγ subunits" by dampening the Ste5 axis and promoting the Far1 axis.
  - **Evidence pointer** Figures 5 and 6, specifically the comparison of pTEF1-M3/M4 to pRS313-WT.
  - **Concern** The central conclusion of signaling bias is confounded by the significant reduction in Ste18 protein levels for M3/M4 mutants. While the authors attempt to control for this by overexpressing M3/M4 to levels comparable to wild-type, the comparison is between a wild-type expressed from a centromeric plasmid (pRS313) and mutants overexpressed from a strong constitutive promoter (pTEF1). This does not fully recapitulate the native expression context. Furthermore, the authors show that M1/M2, which are expressed at ~25% of wild-type levels, exhibit slightly elevated Fus1 activation, whereas M3/M4 at ~10% show reduced activation. This suggests a dose-dependent effect on the Ste5 axis, not necessarily a specific structural effect. The enhanced Far1 axis (polarization, arrest) could also be a consequence of reduced Ste5 competition for Gβγ, rather than a direct structural effect of the helical N-terminus on Far1 binding.
  - **Why it matters** The paper's main novelty and title hinge on the concept of "signaling bias" being influenced by the N-terminal structure. If the observed phenotypes are primarily due to reduced protein abundance, the conclusion is not supported. The distinction between a structural effect on signaling specificity and a quantitative effect on Gβγ levels is fundamental to the paper's thesis.
  - **Resolution test** To resolve this, the authors should perform a direct comparison of M3/M4 and wild-type Ste18 at matched protein expression levels using the same promoter and plasmid system. Ideally, they could use a titratable promoter to express wild-type at levels equivalent to the overexpressed M3/M4 and vice versa. Alternatively, they could introduce the helix-stabilizing mutations into a system where protein abundance is normalized, e.g., by using a degradation-resistant mutant or by expressing the proteins from an inducible promoter at identical levels. If the signaling bias phenotype persists under matched expression, the claim would be significantly strengthened.
  - **Concern ID** R1-M2
  - **Severity** Major
  - **Blocking** No
  - **Axis** Technical soundness / Methodology
  - **Claim pointer** The claim that the M1–M4 mutations produce a "stepwise disorder-to-order transition" in the N-terminus, validated by CD and MD.
  - **Evidence pointer** Figures 2 and 3, and supplementary Figures S1 and S2.
  - **Concern** The CD and MD data are presented as "relative helix percentage" but the correlation between the two methods, while stated, is not shown in the main text. The CD spectra for M1 and M2 show only "slight deviation" from wild-type, and the quantitative helix percentages for these mutants are not explicitly stated in the main text. The MD simulations were performed on isolated peptides, which may not fully recapitulate the behavior of the N-terminus in the context of the full Gβγ complex. The authors acknowledge this in the discussion but do not address it experimentally.
  - **Why it matters** The validity of the "gradient" of structural states is crucial for interpreting the phenotypic gradient observed in vivo. If M1 and M2 do not significantly differ in structure from wild-type, then their phenotypes (elevated Fus1) may be due to other factors, such as the specific mutations affecting protein-protein interactions rather than structure per se.
  - **Resolution test** The authors should provide a clear figure showing the correlation between CD-derived and MD-derived helix percentages for all mutants. They should also consider performing CD or MD on the N-terminus in the context of a Gβγ complex, or at least discuss the limitations more explicitly. If possible, they could use a more direct structural probe, such as NMR, to confirm the structural states in a more native context.
  - **Concern ID** R1-M3
  - **Severity** Major
  - **Blocking** No
  - **Axis** Data interpretation / Evolutionary claims
  - **Claim pointer** The claim that N-terminal intrinsic disorder is an "ancestral feature" of Gγ subunits based on ancestral sequence reconstruction.
  - **Evidence pointer** Figure 1 and Table S1.
  - **Concern** The ancestral sequence reconstruction is based on a set of 92 sequences, but the selection criteria for these sequences are not fully detailed. The prediction of disorder in ancestral sequences relies on the accuracy of the reconstruction and the disorder prediction algorithm (IUPred2A). The authors state that the ancestral sequence has an 8-amino acid disordered N-terminus, but the confidence intervals or statistical support for this specific length are not provided. Furthermore, the analysis is limited to the length of the disordered region and does not consider the sequence composition or conservation of specific residues within the disordered region, which could be functionally important.
  - **Why it matters** The evolutionary claim is a key part of the paper's significance. If the reconstruction is not robust or the disorder prediction is uncertain, the claim of ancestry is weakened. The functional importance of the disordered region may not be solely dependent on its length but also on its specific sequence features.
  - **Resolution test** The authors should provide a more detailed description of the sequence selection and the statistical support for the ancestral disorder prediction. They could also perform a sensitivity analysis by using different disorder prediction algorithms or by examining the conservation of specific residues within the disordered region across the phylogeny. A more robust evolutionary analysis would strengthen this claim.
- **Minor Comments**
  - **Concern ID** R1-m1
  - **Severity** Minor
  - **Axis** Clarity / Presentation
  - **Affected element** Figure 1
  - **Evidence pointer** Figure 1A and 1B
  - **Issue** The figure legend is sparse. It is unclear what the box plot in Figure 1A represents (e.g., median, quartiles, outliers). The color coding in Figure 1B is not explained in the legend.
  - **Required correction** Expand the figure legend to fully explain the data representation, including the definition of boxes, whiskers, and any outliers. Clearly state what the color coding in the phylogenetic tree represents.
  - **Concern ID** R1-m2
  - **Severity** Minor
  - **Axis** Technical soundness / Methodology
  - **Affected element** Molecular Dynamics simulation
  - **Evidence pointer** Experimental procedures, Molecular dynamics simulation section
  - **Issue** The methods state that simulations were performed with both NAMD and Amber, but it is unclear which software was used for which part of the simulation (e.g., equilibration vs. production). The equilibration at 400 K is unusual and not standard for peptide simulations.
  - **Required correction** Clarify the exact role of each software package. Provide a justification for the high-temperature equilibration step or remove it if it is not essential.
  - **Concern ID** R1-m3
  - **Severity** Minor
  - **Axis** Data interpretation / Statistics
  - **Affected element** Figure 6J
  - **Evidence pointer** Figure 6J and Statistical analysis section
  - **Issue** The halo assay results are stated to be statistically significant, but the effect size and the number of biological replicates are not explicitly stated in the main text. The statistical test used (two-way ANOVA with Tukey's correction) is appropriate, but the presentation of the data could be clearer.
  - **Required correction** State the number of biological replicates for the halo assay in the figure legend. Consider showing individual data points on the bar graph to better illustrate the variability.
  - **Concern ID** R1-m4
  - **Severity** Minor
  - **Axis** Clarity / Presentation
  - **Affected element** Discussion
  - **Evidence pointer** Discussion, "Effects of Gγ helix-stabilizing mutations..." section
  - **Issue** The discussion of the potential mechanism by which the helical N-terminus affects signaling is speculative. The authors suggest a possible effect on Gβγ/effector interactions but do not provide direct evidence.
  - **Required correction** Clearly distinguish between data-supported conclusions and speculation. Consider adding a short paragraph on future directions to test the proposed mechanism directly.
- **Technical failings that need to be addressed before the case is established**
  1. The confounding effect of reduced protein abundance on the signaling bias claim (R1-M1) is a critical technical issue that must be resolved with matched-expression experiments.
  2. The lack of a clear demonstration that the M1/M2 mutants are structurally distinct from wild-type, given their modest CD changes, needs to be addressed (R1-M2).
  3. The robustness of the ancestral disorder prediction needs to be demonstrated with statistical support and sensitivity analysis (R1-M3).
- **Assessment against Nature-style criteria**
  - **Originality** The work is original in its approach to studying IDR function via a genetic titration strategy and in its evolutionary analysis of Gγ N-terminal disorder. The concept of Gγ N-terminal structure influencing signaling bias is novel.
  - **Scientific importance** The findings are of interest to the GPCR signaling field and contribute to the broader understanding of IDR function. However, the importance is somewhat diminished by the unresolved confounding factors. The claim of ancestral conservation is important but requires stronger validation.
  - **Interdisciplinary readership** The topic is primarily of interest to cell biologists, biochemists, and molecular biologists. The evolutionary aspect may attract a wider audience, but the overall scope is likely too specialized for a general journal.
  - **Technical soundness** The experimental design is generally sound, with appropriate controls (C1, C2). However, the key issue of protein abundance confounding the signaling bias conclusion is a significant technical weakness. The CD and MD methods are appropriate but their correlation and limitations need to be more clearly presented.
  - **Readability for nonspecialists** The manuscript is well-written and logically structured. The abstract is clear. However, the complexity of the genetic approach and the signaling assays may be challenging for a completely nonspecialist reader. The figures are generally clear, but some legends need expansion.
- **Recommendation posture** Supportive if technical concerns are resolved. The core idea is interesting and the evolutionary analysis is a strength. However, the central claim of signaling bias is not currently established from the provided evidence due to the confounding effect of protein abundance. The authors must provide additional experiments with matched protein expression levels to support their model. The robustness of the evolutionary and structural analyses also needs to be strengthened.

## Risk / unsupported claims
- The claim that the observed changes in signaling are due to a "shift in signaling bias" rather than a reduction in overall Gβγ signaling output is not fully supported by the data presented, due to the confounding effect of reduced Ste18 protein levels.
- The claim that the M1–M4 mutations create a "stepwise" gradient of structural states is not fully supported by the data shown, as the structural differences between wild-type, M1, and M2 appear minimal.
- The claim that N-terminal disorder is an "ancestral feature" is plausible but not robustly supported without statistical confidence intervals for the ancestral state prediction and a sensitivity analysis of the methods used.
- The speculation that the effects might be due to altered Gβγ/effector interactions is not directly tested and remains unsupported.