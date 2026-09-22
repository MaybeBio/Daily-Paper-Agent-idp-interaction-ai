## Review setup
- **Input scope** Full manuscript text (abstract, introduction, results, discussion, experimental methods) as provided
- **Assessment boundary** Scientific claims, experimental evidence, computational methodology, and interpretation as presented in the provided text
- **Shared manuscript claim summary** The authors describe a sequence-generating algorithm (ALGO-CP) that blends evolutionary conservation with physicochemical design to generate de novo acyl carrier protein (ACP) variants. Two soluble variants (ALGO-055, ALGO-059) and two chimeras (chALGO-012, chALGO-024) undergo full post-translational modification (apo to holo to acyl) in vitro. Circular dichroism spectroscopy indicates these variants lack canonical alpha-helical structure yet remain modifiable, with partial helical recovery upon acylation. The authors propose that ACP post-translational modification can be retained independently of canonical structure.
- **Visible evidence base** Abstract, full introduction, results and discussion sections, experimental methods summary, figure references (Figs 1-7, S1-S49), table references (Tables S2-S20)
- **Missing materials affecting confidence** Supplementary figures and tables referenced but not provided; full experimental details for CD spectroscopy and PTM assays not included; raw LC/ESI-MS spectra not shown; AlphaFold3 model coordinates not provided; MD simulation parameters partially described but trajectory analyses not fully detailed

## Reviewer

### Overall assessment
This manuscript presents a novel computational approach to ACP design and reports the surprising finding that de novo ACP variants can undergo post-translational modification without adopting the canonical alpha-helical fold. The work is conceptually interesting and addresses an underexplored area of ACP sequence space. However, several technical concerns must be addressed before the central claims are fully established. The discrepancy between in silico predictions of alpha-helicity and experimental CD data is striking and warrants more rigorous investigation. The manuscript would benefit from additional biophysical characterization and clearer presentation of the relationship between sequence, structure, and function.

### Who would be interested in the results, and why
Researchers in protein engineering, synthetic biology, and metabolic engineering would find this work relevant, as it demonstrates a computational approach to generating functional protein variants with non-canonical structure. The broader protein science community interested in sequence-structure-function relationships, particularly regarding intrinsically disordered proteins and post-translational modification, would also find the results thought-provoking. The open-source availability of ALGO-CP may attract those seeking new tools for protein design.

### Major Strengths
- Novel computational approach (ALGO-CP) that combines evolutionary and physicochemical design principles
- Surprising experimental finding that non-helical ACP variants retain post-translational modification capability
- Integration of computational predictions with experimental validation
- Open-source code availability under permissive license
- Clear writing and logical flow of the narrative

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors claim that ALGO-055 and ALGO-059 "lack the canonical alpha-helical fold of an ACP, whilst remaining soluble and readily modifiable" based on CD spectroscopy.
- **Evidence pointer** Figure 6A-C, Table S15
- **Concern** The CD spectroscopy data are presented as the primary experimental evidence for the absence of canonical alpha-helical structure. However, the manuscript does not provide sufficient detail on the CD data analysis, including how secondary structure content was estimated, what reference spectra were used, and whether the proteins were confirmed to be monomeric and properly folded under the measurement conditions. The binary order-disorder classification (Table S15) is mentioned but the methodology for this classification is not described in the main text.
- **Why it matters** The central claim of the manuscript rests on the demonstration that these variants lack canonical structure yet remain functional. If the CD analysis is not rigorously performed and interpreted, the main conclusion is undermined. Additionally, CD spectroscopy provides only a global measure of secondary structure and cannot exclude the presence of locally structured regions that may be functionally important.
- **Resolution test** Provide full CD spectra with appropriate controls, describe the deconvolution method and reference set used, include sedimentation equilibrium or size-exclusion chromatography data to confirm the oligomeric state, and consider complementary structural probes such as limited proteolysis, chemical crosslinking, or NMR spectroscopy to corroborate the absence of stable tertiary structure.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors state that "both ALGO-055 and ALGO-059 could be readily converted to their respective holo forms in vitro using purified Ec AcpS" and that acylation proceeded to "greater than 99%".
- **Evidence pointer** Figure 3C-D, Table S14, Figures S21, S23, S30-31
- **Concern** The quantitative claim of greater than 99% acylation is based on LC/ESI-MS analysis, but the manuscript does not describe how this percentage was calculated, whether the analysis accounted for potential co-eluting species, or whether the mass spectrometry data were processed with appropriate controls. Additionally, the observation that these variants were "partly purified in holo form" from E. coli suggests in vivo modification, but the efficiency of this process relative to natural AcpS is not quantified.
- **Why it matters** The efficiency and completeness of post-translational modification is central to the claim that these variants are functionally competent ACPs. If the quantification is not rigorous, the strength of the functional claim is uncertain.
- **Resolution test** Provide representative raw mass spectra, describe the integration and quantification method, include replicates with standard deviations, and report the limits of detection for the unmodified species. Consider kinetic measurements of PTM to compare efficiency with natural AcpP.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Scientific importance
- **Claim pointer** The authors propose that "some key aspects of ACP behaviour (specifically post-translational modification) can be retained independently of the canonical structure" and suggest evolutionary implications for the emergence of the alpha-helical fold.
- **Evidence pointer** Discussion section, Conclusion
- **Concern** The evolutionary speculation, while interesting, extends beyond the data presented. The authors have demonstrated that two specific variants can be modified in vitro, but this does not establish a general principle about ACP evolution or the dispensability of structure. The comparison to intrinsically disordered proteins is suggestive but not rigorously developed.
- **Why it matters** The broader significance of the work depends on whether the findings can be generalized or whether they represent idiosyncratic properties of the specific sequences generated. Overinterpretation may mislead readers about the implications for ACP biology and evolution.
- **Resolution test** Either temper the evolutionary claims to match the data more closely, or provide additional evidence such as testing additional ALGO variants, measuring modification efficiency quantitatively, or demonstrating that the variants can participate in downstream fatty acid biosynthesis reactions.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Technical soundness
- **Claim pointer** The authors state that "we further reveal by circular dichroism spectroscopy that ALGO-055 and ALGO-059 lack the canonical alpha-helical fold of an ACP, whilst remaining soluble and readily modifiable. Upon acylation of ALGO-055 and ALGO-059, we observe a marked increase in helicity indicative of partial restructuring."
- **Evidence pointer** Figure 6A-C, Figure S48
- **Concern** The MD simulations were initiated from AlphaFold3-predicted structures that are predominantly alpha-helical, yet the CD data indicate the proteins are largely unstructured in solution. This discrepancy is acknowledged in the conclusion but not adequately addressed. The MD simulations may be probing the stability of an imposed fold rather than the intrinsic conformational preferences of these sequences, as the authors partially acknowledge. However, the manuscript does not present any simulations initiated from unfolded or partially folded states to test whether the helical conformation is accessible.
- **Why it matters** The interpretation of the MD data as evidence for "structural plasticity" is weakened if the simulations are biased by the starting structures. The relationship between the computational predictions and experimental observations needs to be clarified to support the claim that these variants are conformationally dynamic.
- **Resolution test** Perform additional MD simulations initiated from extended or unfolded conformations, or use enhanced sampling methods to explore the conformational landscape. Compare the free energy of the helical state relative to disordered states. Alternatively, present the MD data more cautiously as probing the stability of the AlphaFold3-predicted fold rather than the intrinsic folding propensity.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Readability
- **Affected element** Figure 1
- **Evidence pointer** Figure 1A-C
- **Issue** The schematic of ALGO-CP is referenced but not described in sufficient detail in the main text. The relationship between the two routes (AC and AP) and the weighting parameter r is not immediately clear from the text alone.
- **Required correction** Expand the figure legend and add a brief description in the main text explaining the workflow and how the weighting parameter affects sequence generation.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Technical soundness
- **Affected element** MD simulation methodology
- **Evidence pointer** Experimental section, "Predictive structural modelling and molecular dynamics simulation"
- **Issue** The manuscript states that "three NPT equilibration phases were performed" for holo simulations of ALGO-059 and ALGO-055, but the reason for this special treatment is not explained. The force constants for the gradual reduction are given, but the rationale is unclear.
- **Required correction** Provide a brief explanation for why these specific systems required modified equilibration protocols and whether this affects the comparability of results across systems.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Readability
- **Affected element** Discussion of sequence analysis
- **Evidence pointer** Figure 7, Tables S17-20
- **Concern** The sequence analysis section is dense and the significance of the "rare amino acid variations" is not immediately clear. The connection between specific variations and the observed structural or functional properties is not established.
- **Required correction** Consider adding a more accessible summary of the key sequence features that distinguish the functional ALGO variants from the non-functional ones, and clarify what insights the sequence analysis provides beyond descriptive statistics.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Technical soundness
- **Affected element** PTM assay conditions
- **Evidence pointer** Experimental section, "Purification of Bs Sfp"
- **Issue** The PTM assay conditions are described briefly, but the stoichiometry of enzyme to substrate, the time course, and the buffer conditions for the acylation reaction are not fully specified in the main text.
- **Required correction** Provide additional experimental details either in the main text or by referring more explicitly to the Supplementary Information.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Readability
- **Affected element** Conclusion
- **Evidence pointer** Conclusion section
- **Issue** The conclusion contains speculative language about "evolutionary implications" and "precursor-like states" that goes beyond the data. This may be appropriate for a perspective but is somewhat out of place in a research article conclusion.
- **Required correction** Consider moving the more speculative evolutionary discussion to a dedicated section or framing it more explicitly as hypothesis-generating rather than data-supported.

### Technical failings that need to be addressed before the case is established
- R1-M1: CD spectroscopy analysis requires more rigorous methodology and complementary structural validation
- R1-M2: Quantification of PTM efficiency requires more detailed mass spectrometry analysis
- R1-M4: MD simulation methodology needs to address the discrepancy between predicted and experimentally observed structure

### Assessment against Nature-style criteria
- **Originality** The work is original in its computational approach to ACP design and in the surprising finding that non-helical variants retain modification capability. The concept of exploring ACP sequence space beyond natural constraints is novel.
- **Scientific importance** The findings have potential importance for understanding sequence-structure-function relationships in ACPs and for protein engineering more broadly. However, the current evidence base is limited to in vitro modification assays, and the broader functional implications (e.g., participation in fatty acid synthesis) are not demonstrated.
- **Interdisciplinary readership** The work bridges computational protein design, biochemistry, and structural biology, which would appeal to a broad readership. The open-source availability of the algorithm enhances its potential impact.
- **Technical soundness** The computational methodology is described in reasonable detail, but the experimental validation is incomplete. The CD spectroscopy data require more rigorous analysis, and the discrepancy with MD predictions needs to be addressed. The PTM assays are straightforward but require more quantitative rigor.
- **Readability for nonspecialists** The manuscript is generally well-written and accessible, though some sections (particularly the sequence analysis) are dense. The figures are referenced appropriately, but the main text could benefit from clearer explanations of the computational workflow.

### Recommendation posture
Supportive if technical concerns are resolved. The central finding, that de novo ACP variants can undergo post-translational modification without canonical alpha-helical structure, is potentially significant. However, the evidence base requires strengthening through more rigorous CD analysis, complementary structural characterization, and clearer quantification of PTM efficiency. The evolutionary speculation should be tempered or supported with additional data.

## Risk / unsupported claims
- The claim that ALGO-055 and ALGO-059 "lack the canonical alpha-helical fold" is based solely on CD spectroscopy and requires complementary validation
- The claim of "greater than 99% acylation" requires more detailed mass spectrometry quantification
- The evolutionary speculation about "precursor-like states" and the emergence of the alpha-helical fold is not supported by the data presented
- The statement that these are "the first examples of expressible, soluble and modifiable ACPs designed entirely de novo by a computer algorithm" is difficult to verify without a comprehensive literature search
- The functional significance of the observed structural plasticity for in vivo ACP function is not demonstrated
- The relationship between specific "rare amino acid variations" and the observed properties is correlative, not causal