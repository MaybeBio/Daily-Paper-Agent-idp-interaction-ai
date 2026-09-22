## Review setup
- **Input scope** Full manuscript text
- **Assessment boundary** Scientific content, experimental design, data analysis, and interpretation as presented in the manuscript
- **Shared manuscript claim summary** The authors used TurboID proximity labeling proteomics in HEK293T cells to map the interactome of myelin basic protein (MBP), comparing it with a deaminated MBP variant (MBPCit) and p21 as a structural control. They report identification of MBP-proximal proteins involved in vesicle trafficking, cell adhesion, and iron/lipid metabolism, and propose a role for MBP in ferroptosis-related processes.
- **Visible evidence base** Abstract, Introduction, Materials and Methods, Results (including figure descriptions), Discussion, Conclusions
- **Missing materials affecting confidence** Raw proteomics data tables (referenced as Supplementary Tables S1–S4), full figure panels, statistical analysis details, replicate information, validation experiments, and quantitative comparison metrics between conditions

## Reviewer
- **Overall assessment** The manuscript addresses a relevant question regarding the protein interaction network of MBP, a key myelin protein implicated in multiple sclerosis. The use of TurboID proximity labeling is appropriate and potentially powerful for capturing transient or weak interactions that conventional methods may miss. However, the current presentation has substantial gaps in experimental detail, data transparency, and validation that prevent full assessment of the claims. The central conclusion that MBP recruits proteins involved in ferroptosis and vesicle docking is intriguing but not sufficiently supported by the evidence provided.
- **Who would be interested in the results, and why** Researchers studying myelin biology, oligodendrocyte function, multiple sclerosis pathogenesis, and protein-protein interaction mapping. The potential link between MBP and ferroptosis may also interest investigators focused on cell death mechanisms in neurodegeneration.
- **Major strengths** The experimental design includes appropriate controls (p21 as a structural mimic, MBPCit as a charge-reduced variant) to address the challenge of nonspecific interactions common to intrinsically disordered proteins. The combination of TurboID and conventional immunoprecipitation provides complementary approaches. The focus on membrane-associated and vesicle-trafficking proteins is biologically plausible given MBP's known membrane interactions.
- **Major Concerns** See detailed items below.
- **Minor Comments** See detailed items below.
- **Technical failings that need to be addressed before the case is established** R1-M1 (lack of quantitative data), R1-M2 (insufficient validation), R1-M3 (missing methodological details), R1-M4 (overinterpretation of functional significance)
- **Assessment against Nature-style criteria** Originality: Moderate. The application of TurboID to MBP is novel, but the conceptual advance is incremental. Scientific importance: Potentially high if the ferroptosis link is validated, but currently speculative. Interdisciplinary readership: Limited; primarily relevant to neurobiology and proteomics specialists. Technical soundness: Not fully assessable due to missing details and raw data. Readability for nonspecialists: The manuscript is generally readable but includes jargon and lacks clear summaries of key findings for a broad audience.
- **Recommendation posture** Currently not established from the provided evidence. Supportive if technical concerns are resolved and additional validation is provided.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Data transparency and quantitative rigor
- **Claim pointer** The authors claim identification of specific MBP interactors (e.g., occludin, Ephrin-B1, SNAP23, ACSL4) based on differential enrichment compared to controls.
- **Evidence pointer** Section 3.1, Figure 1b, Supplementary Tables S1–S4 (not provided)
- **Concern** The manuscript lacks quantitative proteomics data. No enrichment ratios, statistical significance values, or effect sizes are reported for the identified interactors. The criteria for defining a protein as an interactor (beyond "identified in at least two repeats" and "exceeded control by two or more times") are not accompanied by any statistical framework or false discovery rate control at the protein level.
- **Why it matters** Without quantitative metrics, the reader cannot assess the confidence in the interactor list. The high background inherent to TurboID, acknowledged by the authors, makes this particularly problematic. The distinction between genuine proximity partners and abundant background proteins is not established.
- **Resolution test** Provide the full quantitative dataset with enrichment values, statistical tests (e.g., t-test or ANOVA with multiple testing correction), and clear thresholds for interactor designation. Include volcano plots or similar visualizations.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Experimental validation
- **Claim pointer** The authors state that MBP "colocalizes" with several proteins and "potentially interacts" with proteins involved in ferroptosis and vesicle trafficking.
- **Evidence pointer** Sections 4.3–4.5, Figure 3
- **Concern** No independent validation of any identified interaction is provided. The claims of colocalization are based solely on proximity labeling without confirmatory experiments such as co-immunoprecipitation with endogenous proteins, immunofluorescence colocalization, or functional assays. The discussion of ferroptosis involvement is entirely speculative without any functional data.
- **Why it matters** Proximity labeling identifies spatial proximity, not necessarily stable or functionally relevant interactions. Without validation, the biological significance of the findings remains uncertain. The ferroptosis claim, in particular, requires functional evidence to be meaningful.
- **Resolution test** Validate at least a subset of key interactors (e.g., SNAP23, ACSL4) using independent methods. For the ferroptosis claim, perform functional experiments such as assessing MBP's effect on ferroptosis sensitivity in relevant cell types.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Methodological completeness
- **Claim pointer** The authors describe the TurboID labeling and mass spectrometry workflow.
- **Evidence pointer** Section 2.2, Section 2.5, Section 2.6
- **Concern** Critical methodological details are missing: (1) The concentration and duration of biotin labeling are not specified. (2) The number of biological replicates is not stated. (3) The criteria for selecting the 1 mm gel bands for analysis are unclear. (4) The normalization approach (total spectral count) is described but its appropriateness for this dataset is not justified. (5) The exclusion criteria for contaminants are not detailed.
- **Why it matters** Reproducibility is a core requirement for proteomics studies. The lack of these details prevents others from replicating the experiments and limits the interpretability of the results.
- **Resolution test** Provide complete experimental parameters, including biotin concentration and time, replicate numbers, and detailed data processing steps. Justify the normalization strategy.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Interpretation and overreach
- **Claim pointer** The authors conclude that MBP "may recruit and regulate the activity" of proteins involved in ferroptosis and vesicle docking, implying a functional role.
- **Evidence pointer** Section 4.4, Section 4.5, Conclusions
- **Concern** The discussion extrapolates from proximity to function without direct evidence. The statement that MBP "recruits" proteins implies an active role that is not demonstrated. The connection to ferroptosis in multiple sclerosis is speculative and not supported by the data presented.
- **Why it matters** Overinterpretation can mislead readers and the broader field. The authors should clearly distinguish between hypothesis-generating observations and established findings.
- **Resolution test** Revise the discussion to clearly label functional claims as hypotheses. Provide direct experimental evidence for any recruitment or regulatory role, or temper the language accordingly.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity of figure presentation
- **Affected element** Figure 1
- **Evidence pointer** Section 3.1, Figure 1a–c
- **Issue** The figure description is insufficient to understand the experimental workflow and results. The number of identified interactors is mentioned but not clearly visualized.
- **Required correction** Provide a more detailed figure legend, including the exact numbers of proteins at each filtering step and clear labels for each panel.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Terminology consistency
- **Affected element** Abstract and Section 3.1
- **Evidence pointer** Abstract, Section 3.1
- **Issue** The term "deaminated" is used in the abstract, while "deiminated" is used in Section 3.1. These are distinct post-translational modifications (deamidation vs. citrullination).
- **Required correction** Use consistent terminology throughout. Clarify which modification was actually studied.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Literature context
- **Affected element** Section 4.5
- **Evidence pointer** Section 4.5
- **Issue** The discussion of SNARE proteins and vesicle trafficking is detailed but lacks recent references on MBP's role in vesicle dynamics beyond the cited Lam et al. paper.
- **Required correction** Add relevant recent literature to contextualize the findings and strengthen the discussion.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Statistical reporting
- **Affected element** Section 2.6
- **Evidence pointer** Section 2.6
- **Issue** The FDR threshold is stated, but no information is provided on how peptide-level FDR translates to protein-level confidence.
- **Required correction** Clarify the protein-level FDR estimation and report the number of proteins passing each threshold.

## Risk / unsupported claims
- The claim that MBP "recruits and regulates" proteins involved in ferroptosis is unsupported by functional data.
- The identification of specific interactors (e.g., occludin, Ephrin-B1, SNAP23) is not quantitatively supported without enrichment statistics.
- The statement that TurboID is "more informative, robust, and reproducible" compared to immunoprecipitation is an overgeneralization not directly demonstrated by the data.
- The biological relevance of the findings to multiple sclerosis is speculative and not experimentally addressed.
- The use of HEK293T cells as a model system for myelin biology is acknowledged as a limitation, but the potential impact on the validity of the findings is not discussed in depth.