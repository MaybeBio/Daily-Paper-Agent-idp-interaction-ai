## Review setup
- **Input scope** Full manuscript text, including abstract, introduction, results, discussion, materials and methods, and supplementary figure legends as provided.
- **Assessment boundary** Scientific claims, methodological soundness, data interpretation, and alignment with stated conclusions. No assessment of formatting or editorial style beyond readability for a general scientific audience.
- **Shared manuscript claim summary** The authors propose that isoform-specific variations in the C-terminal tail of DCLK family kinases, arising from alternative splicing, confer distinct autoinhibitory mechanisms. They identify an ATP-mimetic segment that completes the catalytic spine, a pseudosubstrate region, and co-evolved residues in the kinase domain that distinguish DCLKs from other CAMKs. They support this with phylogenetic analysis, molecular dynamics simulations, and in vitro biochemical assays.
- **Visible evidence base** Phylogenetic tree (Figure 2), sequence alignments and BPPS analysis (Figure 6), molecular dynamics simulations (Figure 5, Figure 7), thermal shift assays (Figure 3, Figure 5, Figure 8), kinase activity assays (Figure 3, Figure 8), mass spectrometry phosphosite mapping (Figure 8 supplement), and structural models (PDB 6KYQ, AlphaFold2).
- **Missing materials affecting confidence** Raw MD simulation trajectories and analysis scripts are referenced via a Dropbox link but not directly assessable from the manuscript. Source data files are mentioned but not provided in the submitted text. No experimental replicates beyond technical replicates are described for kinase assays. No cell-based or in vivo validation is presented.

## Reviewer
- **Overall assessment** This manuscript presents a compelling and integrative analysis of DCLK kinase regulation, combining evolutionary sequence analysis, computational modeling, and biochemical validation. The identification of an ATP-mimetic autoinhibitory segment and the demonstration of isoform-specific differences in tail dynamics and catalytic output are novel and potentially significant. However, several technical concerns, particularly regarding the interpretation of MD simulations, the limited experimental validation of key claims, and the absence of direct evidence for the proposed regulatory mechanism in a cellular context, temper the strength of the conclusions. The work is of interest to the kinase and signaling communities but requires additional experimental support to fully establish the mechanistic model.
- **Who would be interested in the results, and why** Researchers studying protein kinase regulation, particularly those focused on the CAMK family, intrinsically disordered regions in signaling proteins, and the role of alternative splicing in kinase function. The findings may also interest structural biologists and computational biologists studying allosteric regulation and drug discovery efforts targeting DCLK1 in cancer and neurodegeneration.
- **Major strengths** The study integrates multiple methodologies to address a focused question. The evolutionary analysis provides a broad context for the functional studies. The identification of a specific ATP-mimetic motif and its differential behavior between isoforms is a clear and testable hypothesis. The biochemical assays directly compare isoform variants and support the proposed model of differential autoinhibition.
- **Major Concerns** See detailed items below.
- **Minor Comments** See detailed items below.
- **Technical failings that need to be addressed before the case is established** R1-M1 (MD simulation interpretation), R1-M2 (limited experimental validation of ATP-mimic function), R1-M3 (kinase assay conditions and interpretation), R1-M4 (phosphorylation claim unsupported by direct data).
- **Assessment against Nature-style criteria** Originality: High. The concept of an ATP-mimetic autoinhibitory segment in a kinase tail is novel. Scientific importance: Moderate to high. The findings have implications for understanding kinase regulation and DCLK1 biology, but the direct relevance to disease or therapeutic development is speculative. Interdisciplinary readership: The work bridges evolutionary biology, computational biophysics, and enzymology, which could appeal to a broad audience. Technical soundness: Mixed. The evolutionary and biochemical analyses are generally sound, but the MD simulation interpretation and some experimental designs have weaknesses. Readability for nonspecialists: The manuscript is clearly written but assumes familiarity with kinase structure and MD simulation concepts. The abstract and introduction are accessible, but the results section may be challenging for nonspecialists.
- **Recommendation posture** Supportive if technical concerns are resolved. The core hypothesis is interesting and the data are largely consistent, but the current evidence does not fully establish the mechanistic model, particularly regarding the functional role of the ATP-mimic and the proposed phosphorylation-dependent regulation.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness of computational analysis
- **Claim pointer** The authors claim that MD simulations demonstrate stable docking of the C-terminal tail in the ATP-binding pocket for DCLK1.2, and that this docking completes the catalytic spine, while DCLK1.1 shows unstable tail dynamics.
- **Evidence pointer** Figure 5, Figure 7, and associated text in Results section "An autoinhibitory ATP-mimic completes the C-spine and mimics the gamma phosphate of ATP."
- **Concern** The MD simulations are performed on AlphaFold2 models for DCLK1.1 and DCLK1.2, with only DCLK1.2 having a crystal structure (6KYQ) used as a starting point. The use of AlphaFold2 models for comparative dynamics is problematic, as the models may not accurately represent the conformational ensemble accessible to the protein. The authors do not report simulation convergence, force field validation, or comparison of the AlphaFold2 model to the crystal structure for DCLK1.2. The claim that the tail is "stably docked" in DCLK1.2 is based on RMSF analysis, but the authors do not provide a quantitative threshold for "stable" versus "unstable" docking, nor do they report the free energy of binding or other metrics that would support this claim. The observation that the tail completes the catalytic spine is based on visual inspection of a single simulation frame, which is insufficient to establish a dynamic equilibrium.
- **Why it matters** The central mechanistic model of the paper relies on the differential stability of the tail-docked state between isoforms. If the MD simulations are not robust, the entire model is called into question. The claim of an ATP-mimic that completes the catalytic spine is a strong structural statement that requires more rigorous evidence than visual inspection of a trajectory.
- **Resolution test** The authors should provide evidence of simulation convergence (e.g., RMSD over time, block averaging), compare the AlphaFold2 model of DCLK1.2 to the crystal structure, and perform multiple independent simulations to assess reproducibility. They should also quantify the stability of the tail-docked state using metrics such as the number of native contacts, hydrogen bond occupancy, or free energy calculations (e.g., MM-PBSA or umbrella sampling). The claim of catalytic spine completion should be supported by a quantitative analysis of the spine residue contacts over the entire trajectory, not just a single frame.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Experimental validation of key mechanistic claim
- **Claim pointer** The authors claim that the ATP-mimetic segment (residues 682-688) is functionally important for autoinhibition, and that mutations in this region or in the G-loop relieve autoinhibition and activate the kinase.
- **Evidence pointer** Figure 8 and associated text in Results section "Mutational analysis support isoform-specific allosteric control of catalytic activity by the C-terminal tail."
- **Concern** The mutational analysis is limited to a small number of mutations (D398A, N400A, V682T/V684T, D691A) in the DCLK1.2 background. The authors do not perform the analogous mutations in DCLK1.1 to test whether the corresponding residues are important for the weaker autoinhibition observed in that isoform. The kinase activity assays are performed at a single, high ATP concentration (1 mM), which may not be physiologically relevant and could mask differences in ATP affinity. The authors do not measure ATP binding directly (e.g., via isothermal titration calorimetry or surface plasmon resonance) to support the claim that the tail competes with ATP. The thermal shift assays with DCLK1-IN-1 and Mg:ATP are used to infer binding, but the interpretation is indirect.
- **Why it matters** The claim that the tail functions as an ATP-competitive inhibitor is central to the paper. The current evidence is consistent with this model, but alternative explanations (e.g., the mutations affect protein stability or folding rather than specifically disrupting tail docking) are not excluded. Direct measurement of ATP binding and a more comprehensive mutational analysis would strengthen the case.
- **Resolution test** The authors should perform direct ATP binding assays (e.g., ITC or a fluorescent ATP analog) on wild-type and mutant proteins. They should also generate the corresponding mutations in DCLK1.1 to test whether the same residues are important for the weaker autoinhibition. Kinase assays should be performed at multiple ATP concentrations to determine KM and Vmax for all variants. The thermal shift data should be complemented with a more direct binding assay for the inhibitors.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Interpretation of kinase activity data
- **Claim pointer** The authors claim that DCLK1.1 variants have robust catalytic activity, while DCLK1.2 variants are significantly autoinhibited, and that mutations in DCLK1.2 relieve this autoinhibition.
- **Evidence pointer** Figure 8D and Figure 8 supplement 1.
- **Concern** The kinase activity data are presented as rates of substrate phosphorylation, but the authors do not report the stoichiometry of phosphorylation or the specific activity of the enzymes. The comparison between DCLK1.1 and DCLK1.2 is complicated by the fact that the proteins have different tail lengths and sequences, and the authors do not normalize for potential differences in protein folding or stability. The activity of the DCLK1cat (catalytic domain only) is used as a reference, but it is not clear whether this construct is fully active or whether the removal of the tail affects the intrinsic activity of the kinase domain. The authors report that DCLK1.2 mutants are "activated" relative to WT, but the fold-activation is modest (approximately 5-fold for D398A) and the absolute activity remains low compared to DCLK1.1.
- **Why it matters** The quantitative differences in activity between isoforms and mutants are used to support the model of differential autoinhibition. If the activity measurements are not robust or are influenced by factors other than tail docking, the conclusions may be overstated.
- **Resolution test** The authors should report the specific activity of each enzyme (e.g., nmol/min/mg) and the stoichiometry of phosphorylation. They should also assess protein stability (e.g., via circular dichroism or differential scanning fluorimetry) to ensure that differences in activity are not due to differences in protein folding. The activity of the DCLK1cat construct should be validated as a fully active reference.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Support for phosphorylation-dependent regulation
- **Claim pointer** The authors suggest that phosphorylation of Thr 688 in DCLK1.2 may regulate autoinhibition, and that this site is absent in DCLK1.1.
- **Evidence pointer** Discussion section and Figure 8 supplement 2.
- **Concern** The manuscript does not present direct experimental evidence for the role of Thr 688 phosphorylation in regulating kinase activity. The mass spectrometry data show that Thr 688 is phosphorylated in activated DCLK1.2 mutants, but not in WT, which is correlative. The authors do not test the effect of a phosphomimetic (T688E) or phosphoablative (T688A) mutation on kinase activity in vitro. The MD simulations of the phosphomimetic are mentioned but not described in detail, and the functional consequences are not tested experimentally.
- **Why it matters** The proposed regulatory mechanism involving Thr 688 phosphorylation is a key part of the model, but the evidence is currently weak. Without direct experimental support, this aspect of the model remains speculative.
- **Resolution test** The authors should perform kinase assays with T688A and T688E mutants of DCLK1.2 to directly test the effect of phosphorylation on activity. They should also test whether phosphorylation of Thr 688 affects the ability of the tail to dock in the ATP-binding pocket, using a combination of MD simulations and biochemical assays (e.g., limited proteolysis or hydrogen-deuterium exchange).

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity of nomenclature
- **Affected element** Table 1 and Figure 1
- **Evidence pointer** Table 1, Figure 1
- **Issue** The nomenclature for DCLK1 isoforms (DCLK1.1, DCLK1.2, DCLK1.3, DCLK1.4) and the ΔDCLK1.1/ΔDCLK1.2 designations may be confusing, especially for readers not familiar with the field. The relationship between the isoform names and the protein constructs used in the experiments is not always clear.
- **Required correction** Provide a clear schematic or table that maps the isoform names to the protein constructs used in each experiment, including the exact residue ranges and any tags.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Statistical reporting
- **Affected element** Figure 8 and associated text
- **Evidence pointer** Figure 8
- **Issue** The kinase activity data are presented as mean and SD of 4 technical replicates, but no statistical tests are reported to compare the different variants. The authors state that certain mutants are "activated" or "inhibited" without providing p-values or confidence intervals.
- **Required correction** Perform appropriate statistical tests (e.g., one-way ANOVA with post-hoc comparisons) and report the results in the figure legends or text.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Completeness of methods
- **Affected element** Molecular Dynamics section
- **Evidence pointer** Materials and Methods, "Molecular Dynamics"
- **Issue** The methods for MD simulations are described, but key parameters are missing, including the specific version of GROMACS, the thermostat/barostat settings, the equilibration protocol, and the number of replicates. The authors state that three replicates were performed, but it is not clear if these are independent simulations or different starting conditions.
- **Required correction** Provide a complete description of the MD simulation parameters, including software version, force field parameters, water model, ion concentration, temperature/pressure coupling, and the length of the simulations. Clarify the nature of the replicates.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Data availability
- **Affected element** Data Availability section
- **Evidence pointer** Data Availability section
- **Issue** The MD simulation data are deposited in a Dropbox link, which is not a permanent or citable repository. This may not meet the data availability standards of the journal.
- **Required correction** Deposit the MD simulation data and analysis scripts in a permanent repository (e.g., Zenodo, Figshare, or a university repository) and provide a DOI.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Discussion of limitations
- **Affected element** Discussion section
- **Evidence pointer** Discussion section
- **Issue** The authors do not explicitly discuss the limitations of their study, such as the use of AlphaFold2 models for DCLK1.1, the lack of cellular validation, and the correlative nature of the phosphorylation data.
- **Required correction** Add a paragraph in the Discussion acknowledging these limitations and suggesting future experiments to address them.

## Risk / unsupported claims
- The claim that the ATP-mimetic segment "completes the catalytic spine" is based on visual inspection of MD trajectories and is not quantitatively supported.
- The claim that phosphorylation of Thr 688 regulates autoinhibition is correlative and not directly tested.
- The claim that DCLK1.1 and DCLK1.2 have distinct autoinhibitory properties is supported by the data, but the mechanistic explanation (differential tail docking) is not fully established.
- The evolutionary inference that DCLK1/2 tail extensions are vertebrate-specific regulatory adaptations is based on a limited phylogenetic sample and is not tested experimentally.
- The suggestion that isoform-specific differences in DCLK1 regulation may be relevant to cancer and drug resistance is speculative and not supported by data in this manuscript.