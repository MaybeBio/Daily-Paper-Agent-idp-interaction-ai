## Review setup
- **Input scope** Full manuscript text including abstract, introduction, results, discussion, methods, and figure legends
- **Assessment boundary** Scientific content, methodological rigor, claims versus evidence, and presentation quality
- **Shared manuscript claim summary** The authors use atomistic molecular dynamics simulations to study six prenylated intrinsically disordered regions (PIDRs) from Ras and Rho family small GTPases in an asymmetric PC/PS bilayer. They report that conformational plasticity of PIDRs is a key determinant of lipid recognition and sorting, that lipid recognition depends on both headgroup and acyl chain structure, that the sequence outside the polybasic domain (PBD) modulates conformational substates and lipid interactions, and that the PBD is necessary but not sufficient for full lipid sorting.
- **Visible evidence base** Main text with six figures, one table, supplementary figure references, and supplementary data files
- **Missing materials affecting confidence** Supplementary figures and data files were not provided for review; no raw simulation trajectories or analysis scripts were available; no experimental validation data were included

## Reviewer
- **Overall assessment** This manuscript presents a systematic computational study of lipid recognition by prenylated intrinsically disordered regions from small GTPases. The work extends previous findings on KRAS to a broader panel of PIDRs and introduces a useful comparative framework. The simulation methodology is appropriate and the aggregate sampling is substantial. However, the central claim that conformational ensemble-dependent lipid recognition is "generalizable" rests on descriptive analyses of a limited set of sequences, and the evidence for functional significance remains indirect. The manuscript would benefit from clearer quantitative metrics linking conformational substates to lipid selectivity, and from a more critical discussion of limitations.
- **Who would be interested in the results, and why** Researchers studying Ras superfamily membrane targeting, lipid-protein interactions, intrinsically disordered regions, and computational membrane biology. The findings may also interest those working on peripheral membrane protein localization and lipid sorting mechanisms.
- **Major strengths** The study addresses an important and under-explored question about how disordered membrane anchors achieve lipid specificity. The comparative design across six PIDRs with controlled sequence variations is thoughtful. The simulation setup with asymmetric bilayers and multiple peptide copies per system is appropriate. The observation that electrostatic headgroup interactions precede acyl chain selectivity provides a plausible mechanistic link.
- **Major Concerns** See detailed items below.
- **Minor Comments** See detailed items below.
- **Technical failings that need to be addressed before the case is established** R1-M1, R1-M2, R1-M3, R1-M4
- **Assessment against Nature-style criteria** Originality: moderate to high. The concept of ensemble-dependent lipid recognition was previously proposed by the same group for KRAS; this work extends it to additional systems, which is incremental but valuable. Scientific importance: moderate. The findings are relevant to understanding membrane targeting of small GTPases, but the direct biological implications remain speculative without experimental validation. Interdisciplinary readership: limited. The work is primarily of interest to computational biophysicists and membrane protein researchers; the presentation assumes substantial familiarity with MD simulation methods. Technical soundness: generally sound, with appropriate force fields and analysis methods, but some quantitative claims lack statistical rigor. Readability for nonspecialists: moderate. The manuscript is clearly written but the significance of conformational substates and their functional consequences could be better contextualized for a broader audience.
- **Recommendation posture** Supportive if technical concerns are resolved, particularly regarding quantitative support for the generalizability claim and clarification of the relationship between conformational substates and lipid sorting.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Claims versus evidence
- **Claim pointer** The authors state that "conformational ensemble-based lipid recognition is generalizable to all polybasic PIDRs" and that "the PBD is required but not sufficient for the full realization of lipid sorting."
- **Evidence pointer** Results sections "PBD-containing PIDRs segregate lipids in a sequence dependent manner" and "Conformational sub-ensembles and lipid recognition"; Figures 5-8
- **Concern** The generalizability claim is based on five PBD-containing PIDRs plus one non-PBD control. While the authors note that these represent diverse sequences, the sample size is small and the sequences are all from the Ras and Rho families. The claim that the findings apply to "all polybasic PIDRs" is not supported by the evidence presented. Additionally, the assertion that the PBD is "not sufficient" is supported primarily by the Cdc42b case, which has an unusual acidic-rich N-terminal region. It is unclear whether the observed differences reflect a general principle or specific features of the sequences chosen.
- **Why it matters** The central thesis of the manuscript rests on the generalizability of the findings. Overstating the scope of the conclusions could mislead readers about the universality of the proposed mechanism.
- **Resolution test** The authors should either temper the language to reflect the specific systems studied, or provide additional analysis demonstrating that the observed relationships between sequence features, conformational substates, and lipid interactions hold across a broader sequence space. Alternatively, a clear mechanistic rationale for why the observed patterns should be expected to generalize could be provided.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Quantitative support
- **Claim pointer** The authors report "4-fold and ~2-fold PS enrichment at the headgroup and acyl chain regions, respectively" for RhoA, and similar enrichment factors for other PIDRs.
- **Evidence pointer** Results section "PBD-containing PIDRs segregate lipids in a sequence dependent manner"; Figure 5
- **Concern** The enrichment factors are derived from comparisons of hydrogen bond and van der Waals contact counts between PS and PC lipids. However, the statistical significance of these differences is not reported. The manuscript states that "averages were taken over three peptides" but does not provide error estimates, confidence intervals, or statistical tests for the enrichment values. Given that the simulations are equilibrium trajectories, the fluctuations in contact counts could be substantial, and it is unclear whether the reported differences are robust.
- **Why it matters** The quantitative claims of lipid enrichment are central to the paper's conclusions about lipid sorting. Without statistical support, the reader cannot assess whether the observed preferences are meaningful or within the noise of the simulations.
- **Resolution test** Provide standard deviations, confidence intervals, or statistical tests (e.g., block averaging, bootstrap) for the reported enrichment values. If the differences are not statistically significant, this should be stated and the conclusions adjusted accordingly.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Methodological transparency
- **Claim pointer** The authors state that "we analyzed the simulated conformers based on a global measure (Rg or RMSD, whichever has a multimodal distribution) and a local measure based on a pseudo dihedral angle involving four consecutive Cα atoms (Φ)."
- **Evidence pointer** Methods section "Molecular dynamics simulation and trajectory analysis"; Results section "Conformational sub-ensembles and lipid recognition"; Figures 6-8
- **Concern** The choice of which global measure (Rg or RMSD) to use for each system is not justified. The manuscript states that the measure with a "multimodal distribution" was selected, but the criteria for determining multimodality are not described. Furthermore, the selection of the specific pseudo dihedral angle (which four consecutive residues) is stated to be the one that "most clearly classified" the conformers, but the metric used to assess classification quality is not defined. This introduces potential researcher degrees of freedom that could affect the reported results.
- **Why it matters** The identification of conformational sub-ensembles is a key analytical step. If the selection criteria are not objective and reproducible, the resulting clusters and their interpretation may not be robust.
- **Resolution test** Provide explicit, quantitative criteria for selecting the global measure and the pseudo dihedral angle. Ideally, the analysis should be shown to be insensitive to these choices, or the authors should demonstrate that the identified clusters are robust across different analysis parameters.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence for mechanism
- **Claim pointer** The authors propose that "electrostatic-driven sorting of PS lipids at the headgroup ultimately leads to selective interactions at the acyl chain level."
- **Evidence pointer** Results section "PBD-containing PIDRs segregate lipids in a sequence dependent manner"; Figure 5 and Supplementary Figure 5
- **Concern** The temporal ordering of headgroup and acyl chain interactions is inferred from the observation that hydrogen bond contacts with PS headgroups increase before van der Waals contacts with PS acyl chains (Supplementary Figure 5). However, the manuscript does not provide a quantitative analysis of the time course of these interactions, nor does it demonstrate a causal relationship between the two events. The correlation between headgroup binding and subsequent acyl chain interactions could be coincidental or driven by other factors, such as the gradual accumulation of PS lipids in the vicinity of the peptide.
- **Why it matters** The proposed two-step mechanism is a novel and important claim. Without direct evidence for the causal link between headgroup recognition and acyl chain selectivity, the mechanism remains speculative.
- **Resolution test** Perform a time-resolved correlation analysis between headgroup hydrogen bond formation and subsequent acyl chain contact establishment for individual PS lipids. Alternatively, perform simulations with modified lipid headgroups to test whether headgroup interactions are necessary for acyl chain selectivity.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Abstract
- **Evidence pointer** Abstract, first sentence
- **Issue** The phrase "conformational plasticity is a key determinant of lipid sorting" is vague. The authors should specify what aspect of conformational plasticity (e.g., backbone flexibility, substate diversity, specific structural motifs) is most important.
- **Required correction** Clarify the specific conformational feature that correlates with lipid sorting, referencing the quantitative measures used in the study.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Statistical reporting
- **Affected element** Figure 5
- **Evidence pointer** Figure 5 legend
- **Issue** The figure legend states that "equilibrium distributions" are shown, but the number of samples used to construct these distributions is not stated. Given that the data are time series, the effective number of independent samples may be much smaller than the number of frames.
- **Required correction** Report the number of independent samples or the autocorrelation time used to determine effective sample sizes.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Discussion
- **Evidence pointer** Discussion, paragraph 3
- **Issue** The authors discuss the potential biological relevance of their findings but do not address the limitation that the simulations use isolated PIDRs rather than full-length proteins. The presence of the catalytic domain could influence the conformational ensemble and lipid interactions of the PIDR.
- **Required correction** Add a sentence acknowledging this limitation and discussing whether the isolated PIDR is a reasonable model for the membrane-bound state of the full-length protein.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Reproducibility
- **Affected element** Methods
- **Evidence pointer** Methods section "Molecular dynamics simulation and trajectory analysis"
- **Issue** The manuscript states that simulations were performed on Anton 2 but does not provide the software version or specific input parameters beyond the force field. This limits reproducibility.
- **Required correction** Provide the NAMD version, Anton 2 software version, and any non-default simulation parameters.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Presentation
- **Affected element** Figure 6
- **Evidence pointer** Figure 6 legend
- **Issue** The color scale for the 2D probability density plots is described as "dark blue through yellow represent 25% through 100% occupancy." This is confusing because probability densities are typically normalized to a maximum of 1, not 100%.
- **Required correction** Clarify the normalization of the probability density and the meaning of the color scale.

## Risk / unsupported claims
- The claim that "conformational ensemble-based lipid recognition is generalizable to all polybasic PIDRs" is not supported by the limited sequence sampling in this study.
- The proposed two-step mechanism of headgroup-driven acyl chain selectivity is inferred from temporal correlations and lacks direct causal evidence.
- The statement that "the PBD is required but not sufficient for the full realization of lipid sorting" is based primarily on the Cdc42b case and may not be generalizable.
- The biological relevance of the findings is discussed without experimental validation, and the relationship between the simulated isolated PIDRs and full-length protein behavior is not addressed.
- The quantitative enrichment factors for PS over PC are reported without statistical significance testing, making their robustness uncertain.