## Review setup
- **Input scope** Full manuscript
- **Assessment boundary** The manuscript as provided, including main text, figures, and methods
- **Shared manuscript claim summary** The authors propose a stepwise molecular pathway for the recruitment of the ULK1 autophagy-initiating complex to membranes, mediated by WIPI proteins and direct membrane interactions of the ATG101 WF finger, and a subsequent interaction between the ULK1 intrinsically disordered region and the ATG13 HORMA domain that positions the ULK1 kinase domain near the membrane for substrate phosphorylation.
- **Visible evidence base** Full manuscript text, all main figures (1-6), supplementary figures (S1-S10), and methods
- **Missing materials affecting confidence** None identified from the supplied material

## Reviewer
- **Overall assessment** This manuscript presents a comprehensive and largely convincing biochemical and cellular dissection of the molecular mechanisms governing ULK1 complex recruitment to membranes during autophagy initiation. The authors identify a WIPI3-binding motif in ATG13, demonstrate the membrane-anchoring function of the ATG101 WF finger, and uncover a novel interaction between the ULK1 intrinsically disordered region and the ATG13 HORMA domain that positions the kinase near its membrane-bound substrates. The combination of structural predictions, molecular dynamics simulations, biochemical reconstitution, and cell-based assays provides a multi-layered approach that substantially advances our understanding of a long-standing question in the autophagy field. The work is technically rigorous and the conclusions are generally well-supported by the data. However, several concerns regarding the quantitative rigor of the cellular data, the physiological relevance of the reconstitution conditions, and the interpretation of the MD simulations need to be addressed.
- **Who would be interested in the results, and why** This work will be of high interest to researchers in the autophagy, membrane trafficking, and cell signaling fields. It provides a mechanistic explanation for the long-observed PI3P-dependent stabilization of ULK1C at phagophore initiation sites, resolves the decade-old question of ATG101's essential function, and establishes a new paradigm for how kinase domains are positioned at membranes through intrinsically disordered region interactions. The findings have implications for understanding the molecular basis of autophagy-related diseases, including Parkinson's disease and cancer.
- **Major strengths** 1. The study addresses a fundamental and long-standing question in the autophagy field with a clear and logical experimental approach. 2. The combination of computational predictions (AlphaFold2, MD simulations) with rigorous biochemical reconstitution and cellular validation is powerful and provides multiple lines of evidence. 3. The identification of the ULK1 IDR-ATG13 HORMA interaction as a mechanism to position the kinase domain near the membrane is a novel and important conceptual advance. 4. The use of quantitative assays (GUV binding, dot blot kinase assays, flow cytometry) strengthens the conclusions.
- **Major Concerns**
    - **Concern ID** R1-M1
    - **Severity** Major
    - **Blocking** No
    - **Axis** Data interpretation and quantification
    - **Claim pointer** The authors claim that the ATG13(HF|DD) mutant "significantly impaired mitophagy" in the mito-QC assay (fig. S6, A and B) and that the ULK1 ADA mutant "significantly reduced" autophagic flux (fig. S10, A and B).
    - **Evidence pointer** Figure S6, A and B; Figure S10, A and B
    - **Concern** The quantification of the mito-QC and mCherry-GFP-LC3 assays relies on manual cell counting or flow cytometry gating. The statistical significance is reported, but the effect sizes for the mutants, while statistically significant, appear modest in some cases. For example, in fig. S6B, the percentage of mitophagic cells for the HF|DD mutant is approximately 15-20% compared to ~25-30% for WT, a reduction of ~30-40%. While this is significant, it is not a complete block. The authors should provide a more detailed discussion of the magnitude of the effect and whether this partial reduction is consistent with the model that this interaction is a critical, but not the sole, determinant of ULK1C recruitment. Furthermore, the flow cytometry gating strategy for the mito-QC and LC3 flux assays should be explicitly described, including how the gate for "autophagic" or "mitophagic" cells was defined.
    - **Why it matters** The quantitative interpretation of the cellular phenotypes is central to the claim that the identified interactions are essential for autophagy and mitophagy. Overstating the effect or not fully characterizing the partial phenotype could mislead the field about the relative importance of this pathway versus other recruitment mechanisms.
    - **Resolution test** 1. Provide a clear description of the flow cytometry gating strategy, including representative plots showing the gate boundaries. 2. Quantify the data as both percentage of positive cells and mean fluorescence intensity of the red-only signal (for mito-QC) or the GFP/mCherry ratio (for LC3). 3. Discuss the partial nature of the phenotype and its implications for the model, acknowledging that other recruitment mechanisms (e.g., ATG9 binding, PI3KC3-C1 supercomplex formation) likely contribute.

    - **Concern ID** R1-M2
    - **Severity** Major
    - **Blocking** No
    - **Axis** Experimental design and controls
    - **Claim pointer** The authors claim that the reconstituted kinase assay (Fig. 4, B and C) demonstrates that ULK1 activity against a membrane-associated substrate "strongly depends on the synergistic recruitment of the complex to the membrane by both ATG13:WIPI binding and membrane docking by the ATG101 WF finger."
    - **Evidence pointer** Figure 4, B and C
    - **Concern** The reconstituted kinase assay uses a minimal ATG16L1 fragment (residues 78-300) that contains the phosphorylation site and WIPI binding sites. However, the assay uses a very high concentration of liposomes (200 µM total lipid) and a relatively low concentration of ULK1C (3 nM ULK1, 30 nM FIP200/ATG13/ATG101). The molar ratio of liposomes to ULK1C is extremely high (~10^5:1). Under these conditions, the observed phosphorylation could be driven by a small fraction of ULK1C that is non-specifically associated with the large excess of liposomes, rather than by the specific, synergistic recruitment pathway proposed. The authors should perform control experiments to rule out this possibility. For example, they could titrate the liposome concentration to determine the dependence of the signal on the specific recruitment pathway. They could also use liposomes lacking PI3P to demonstrate that the WIPI-dependent recruitment is specific.
    - **Why it matters** The reconstitution assay is a key piece of evidence for the proposed model. If the observed activity is largely due to non-specific binding to the high surface area of liposomes, the conclusions about the specific roles of WIPI2, WIPI3, and the WF finger would be weakened.
    - **Resolution test** 1. Perform a liposome titration experiment, measuring ULK1 activity at several different liposome concentrations (e.g., 20, 50, 100, 200 µM). 2. Include a control with liposomes lacking PI3P to demonstrate that the WIPI-dependent enhancement is specific to PI3P-containing membranes. 3. Consider using a lower, more physiologically relevant liposome concentration.

    - **Concern ID** R1-M3
    - **Severity** Major
    - **Blocking** No
    - **Axis** Data interpretation and quantification
    - **Claim pointer** The authors claim that the MD simulations show that the ATG13-ATG101-WIPI3 complex "remained stable throughout 1-µs MD simulations" and that the WF finger is "essential for membrane recruitment and thereby stabilizes the entire heterotrimeric assembly."
    - **Evidence pointer** Figure 3, A-E; Figure S5
    - **Concern** The MD simulations are a valuable component of the study, but the interpretation of the results should be more cautious. The simulations are performed on a single, pre-docked complex, and the stability is assessed over a relatively short timescale (1 µs). While the simulations show that the complex does not dissociate, they do not demonstrate that the proposed binding mode is the most stable or that it is kinetically accessible from an unbound state. The claim that the WF finger "stabilizes the entire heterotrimeric assembly" is based on a single simulation of the WF|DD mutant, which shows detachment of the DD segment and subsequent perturbation of the ATG13-WIPI3 interface. This is a single trajectory and may not be representative. The authors should perform multiple independent simulations of the mutant to assess the reproducibility of this observation. Furthermore, the simulations do not include the full ULK1C, so the effect of the ULK1 IDR-ATG13 interaction on the overall complex stability is not addressed.
    - **Why it matters** The MD simulations are used to support the structural model and to provide a mechanistic rationale for the experimental observations. Over-interpreting the results of a limited number of simulations could lead to an overly confident model.
    - **Resolution test** 1. Perform at least three independent 1-µs simulations of the WF|DD mutant to assess the reproducibility of the observed detachment. 2. Acknowledge the limitations of the simulations (single starting structure, short timescale, absence of full complex) in the text. 3. Consider performing free energy calculations (e.g., MM-PBSA) to provide a more quantitative estimate of the binding affinities.

    - **Concern ID** R1-M4
    - **Severity** Major
    - **Blocking** No
    - **Axis** Data interpretation and quantification
    - **Claim pointer** The authors claim that the ULK1 ADA mutation "almost completely lost the ability to phosphorylate ATG16L1 at this site" in the reconstituted assay (Fig. 5, F and G).
    - **Evidence pointer** Figure 5, F and G
    - **Concern** The dot blot data in Fig. 5F show a clear reduction in signal for the ADA mutant, but the quantification in Fig. 5G shows that the signal is not zero. The authors state "almost completely lost," which is a qualitative description. The data should be presented more quantitatively. For example, what is the fold reduction in signal at the 60-minute time point? Is the residual signal significantly above background? The authors should also perform a time course experiment to determine if the ADA mutant has a slower rate of phosphorylation or a lower maximal activity.
    - **Why it matters** The claim that the ADA mutation "almost completely" abolishes activity is a strong statement. A more precise quantitative description of the effect is needed to support the model that this interaction is essential for positioning the kinase.
    - **Resolution test** 1. Quantify the dot blot data as fold-change relative to the no-ATP control. 2. Perform a statistical test to determine if the signal for the ADA mutant at the 60-minute time point is significantly different from the background. 3. If possible, perform a time course experiment with more time points to determine the kinetics of phosphorylation.

- **Minor Comments**
    - **Concern ID** R1-m1
    - **Severity** Minor
    - **Axis** Clarity and presentation
    - **Affected element** Figure 1
    - **Evidence pointer** Figure 1, A and B
    - **Issue** The sequence logo in Fig. 1A is difficult to read. The font size for the residue numbers and the species names is very small.
    - **Required correction** Increase the font size of the labels in the sequence logo. Consider presenting the alignment in a more readable format, such as a table.

    - **Concern ID** R1-m2
    - **Severity** Minor
    - **Axis** Clarity and presentation
    - **Affected element** Methods
    - **Evidence pointer** "Microscopy-based bead protein-protein interaction assay"
    - **Issue** The description of the bead binding assay quantification is somewhat brief. The authors state that a "semiautomated pipeline" was used, but the details of the algorithm (e.g., the parameters for Canny edge detection and Hough circle transform) are not provided in the main text.
    - **Required correction** Provide a more detailed description of the quantification pipeline in the Methods section, or include a reference to the deposited code.

    - **Concern ID** R1-m3
    - **Severity** Minor
    - **Axis** Data interpretation
    - **Affected element** Figure 2
    - **Evidence pointer** Figure 2, D and E
    - **Issue** The GUV binding data in Fig. 2D show that the ATG101(WF|DD) mutant still shows some membrane recruitment, especially at higher protein concentrations. The authors state that "residual membrane binding is primarily driven by the WIPI3-PI3P interaction." This is a reasonable interpretation, but it should be explicitly stated that the WF finger is not absolutely required for membrane binding, but rather enhances the efficiency of recruitment.
    - **Required correction** Add a sentence to the text clarifying that the WF finger is important for efficient recruitment at physiological concentrations, but that other interactions (WIPI3-PI3P, CTH) can provide some residual binding.

    - **Concern ID** R1-m4
    - **Severity** Minor
    - **Axis** Clarity and presentation
    - **Affected element** Figure 6
    - **Evidence pointer** Figure 6, G and H
    - **Issue** The co-IP data in Fig. 6G show a reduction in ATG13 co-precipitation with the ULK1 ADA mutant, but the quantification in Fig. 6H shows a relatively modest effect (~30% reduction). The authors should comment on whether this partial reduction is consistent with the model that this interaction is critical for ULK1C stability at initiation sites.
    - **Required correction** Add a sentence to the discussion of Fig. 6 addressing the magnitude of the co-IP effect and its implications.

    - **Concern ID** R1-m5
    - **Severity** Minor
    - **Axis** Data interpretation
    - **Affected element** Discussion
    - **Evidence pointer** "The observation of a membrane-anchoring role for the ATG13:ATG101 HORMA dimer (HD) leads naturally to the question of positioning of the catalytic KD of ULK1 itself."
    - **Issue** The discussion of the volume available to the ULK1 KD (6 x 10^4 nm^3) and the reduction upon HD-ULK1 IDR interaction is interesting but speculative. The authors should clearly state that this is a theoretical estimate based on a simplified model.
    - **Required correction** Add a qualifier such as "based on our simplified model" or "this theoretical estimate suggests" to the relevant sentences.

- **Technical failings that need to be addressed before the case is established** None of the concerns are considered blocking, as the core claims are supported by multiple lines of evidence. However, the concerns regarding the quantification of cellular phenotypes (R1-M1), the controls in the reconstitution assay (R1-M2), and the interpretation of the MD simulations (R1-M3) should be addressed to strengthen the manuscript.

## Risk / unsupported claims
- None identified from the supplied material. All claims are supported by the presented data, although the strength of support varies as noted in the concerns above.