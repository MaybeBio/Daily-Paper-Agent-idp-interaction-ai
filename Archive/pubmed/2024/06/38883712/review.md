## Review setup
- **Input scope** Full manuscript text (abstract, introduction, results, discussion, methods) as provided
- **Assessment boundary** Scientific claims, methodology, evidence quality, and internal consistency based solely on the supplied text
- **Shared manuscript claim summary** The authors use coarse-grained molecular dynamics simulations to argue that the intrinsically disordered N-terminal domain (NTD) of coronavirus nucleocapsid proteins contributes to RNA binding through a conserved, positively charged "groove" formed jointly with the folded RNA-binding domain (RBD), and that this binding mode is preserved across orthologs despite lack of sequence conservation.
- **Visible evidence base** Simulation results (KA* values, scaling maps, structural models), sequence composition analyses, disorder predictions, prior experimental references
- **Missing materials affecting confidence** Figures and supplementary tables referenced but not provided; experimental validation data not included; full simulation parameter details partially described; statistical details for some comparisons absent

## Reviewer
- **Overall assessment** The manuscript addresses a timely and important question in the biology of intrinsically disordered regions: how function can be preserved despite sequence divergence. The authors present a plausible mechanistic model supported by extensive coarse-grained simulations. However, the central claim of "conserved molecular recognition" rests heavily on simulation-derived metrics, and the absence of direct experimental validation for the ortholog panel weakens the case. The manuscript is well-written and the conceptual framework is appealing, but several technical and interpretive issues need resolution before the conclusions can be considered fully established.
- **Who would be interested in the results, and why** Researchers studying intrinsically disordered proteins, RNA-protein interactions, viral nucleocapsid biology, and the evolution of molecular recognition. The work offers a concrete example of how disordered regions can encode function through physicochemical properties rather than primary sequence, which is of broad interest to the molecular biophysics and evolutionary biology communities.
- **Major strengths** The study tackles a fundamental question with a well-defined model system. The use of a large scrambled-sequence library is a powerful approach to dissect sequence determinants. The scaling-map analysis provides a visually intuitive and quantitative framework for comparing bound-state ensembles. The authors are appropriately cautious about the limitations of coarse-grained models and clearly state the semi-quantitative nature of their affinity estimates.
- **Major Concerns** See detailed items below.
- **Minor Comments** See detailed items below.
- **Technical failings that need to be addressed before the case is established** R1-M1 (ortholog simulation validation), R1-M2 (scrambled library representativeness), R1-M3 (KA* normalization validity)
- **Assessment against Nature-style criteria** 
  - **Originality** High. The concept of a bipartite, partially disordered binding groove is a novel contribution.
  - **Scientific importance** High. Provides a potential general principle for IDR function and evolution.
  - **Interdisciplinary readership** Moderate. Will appeal to biophysicists, virologists, and evolutionary biologists, but the heavy simulation focus may limit broader appeal.
  - **Technical soundness** Moderate. The simulation methodology is appropriate, but the lack of experimental validation for the central cross-ortholog claim is a significant gap.
  - **Readability for nonspecialists** Good. The writing is clear, and the conceptual framing is accessible, though some simulation-specific jargon is used without full explanation.
- **Recommendation posture** Supportive if technical concerns are resolved, particularly the need for experimental validation of the conserved binding mode across orthologs and clarification of the normalization procedure.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence sufficiency
- **Claim pointer** "the same specific subregions within the NTD come closer to the RBD across coronavirus orthologs" and "the bound-state ensemble (and hence RNA binding mode) appears to be largely conserved across the six coronavirus NTD-RBD constructs examined"
- **Evidence pointer** Results section "NTD-RBD:RNA Behavior in the Bound State is Conserved Across Orthologs", Figure 4
- **Concern** The central claim of conserved binding mode across orthologs is based entirely on simulations of five additional orthologs, with no experimental validation. The authors previously established simulation-experiment agreement for SARS-CoV-2, but it is not demonstrated that the force field accurately captures the behavior of the other orthologs, which have different sequences and surface chemistries. The scaling-map analysis is qualitative, and no statistical test is provided to demonstrate that the observed similarities across orthologs are significant relative to the variation seen among the scrambled sequences.
- **Why it matters** The title and abstract make a strong claim about conservation of molecular recognition. Without experimental support (e.g., binding assays or structural data) for at least one non-SARS-CoV-2 ortholog, the claim remains a simulation-based prediction rather than an established finding.
- **Resolution test** Provide experimental binding data (e.g., fluorescence anisotropy, ITC, or smFRET) for at least two additional orthologs, or provide a quantitative statistical comparison showing that the scaling maps of natural orthologs are significantly more similar to each other than to those of the scrambled library.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** No
- **Axis** Methodology
- **Claim pointer** "we generated 172 scrambled NTDSCO2 sequences" and "for the majority of the scrambled sequences, the binding affinity is fairly similar, and, importantly, this 'average' binding affinity is almost an order of magnitude weaker than the wild-type NTD-RBD"
- **Evidence pointer** Results section "Sequence Composition Alone Does Not Determine NTD Contribution to Binding Affinity", Figure 3D, Supplementary Table 7
- **Concern** The scrambled library is generated from a single NTD sequence (SARS-CoV-2). It is unclear whether the conclusions drawn from this library, particularly the importance of residue positioning, would hold for scrambles of other ortholog NTDs, which have different lengths and compositions. The four scrambling strategies are described, but the rationale for these specific strategies and the criteria for ensuring adequate sampling of sequence space are not fully explained.
- **Why it matters** The conclusion that "the ordering of the residues in the NTDSCO2 is specific" is based on a single parental sequence. If the positional effects are idiosyncratic to the SARS-CoV-2 NTD, the generalizability of the model is limited.
- **Resolution test** Generate scrambled libraries for at least one additional ortholog NTD and show that the relationship between residue positioning and binding affinity is qualitatively similar, or explicitly discuss the limitations of using a single parental sequence.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Methodology
- **Claim pointer** "we normalize this apparent binding affinity by the binding affinity associated with wildtype NTD-RBD binding (rU)25, reporting this normalized binding affinity as KA*"
- **Evidence pointer** Methods section "Calculating Apparent Association Constants From Simulations", Results section "Inert Intrinsically Disordered Regions Diminish RNA Binding"
- **Concern** The normalization of KA values to the wild-type SARS-CoV-2 NTD-RBD is used throughout, but the validity of this normalization for cross-ortholog comparisons is not established. If the absolute KA values for the different orthologs differ substantially in magnitude, the normalized values may not be directly comparable. Additionally, the error propagation for the ratio assumes independent errors, which may not hold if the reference value is itself uncertain.
- **Why it matters** The KA* metric is the primary quantitative output of the study. If the normalization introduces systematic biases, the conclusions about relative binding affinities across orthologs and mutants could be affected.
- **Resolution test** Report absolute KA values for all constructs and demonstrate that the conclusions are robust to the choice of normalization reference (e.g., by also normalizing to the RBD-only construct or to a different ortholog).

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Figure 2D
- **Evidence pointer** Results section "Inert Intrinsically Disordered Regions Diminish RNA Binding"
- **Issue** The text states that the (GS)25-RBD construct "bound half as tightly as the RBD alone" but the KA* values are given as 0.020 ± 0.003 and 0.037 ± 0.004, respectively. The ratio is approximately 0.54, which is "about half," but the error bars overlap substantially. It would be helpful to state whether this difference is statistically significant.
- **Required correction** Add a statistical test (e.g., a t-test or bootstrap confidence interval) to support the claim of a significant difference, or soften the language to reflect the uncertainty.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Methods section "Calculating Apparent Association Constants From Simulations"
- **Evidence pointer** Methods section
- **Issue** The equation for KD is given as KD=(1−fbound)2NAVfbound. The derivation of this equation is not provided, and it is unclear how the factor of 2 in the numerator arises. This is important for readers who wish to reproduce the analysis.
- **Required correction** Provide a brief derivation or citation for this equation, and define all variables explicitly.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Interpretation
- **Affected element** Discussion section
- **Evidence pointer** Discussion and Conclusion
- **Issue** The authors speculate that the second binding hotspot around residue 12 in SARS-CoV-2 may play an "auxiliary regulatory role," but no functional data are presented to support this speculation. The claim is presented as a possibility, which is appropriate, but it would be strengthened by a more explicit statement of what kind of experiment could test this hypothesis.
- **Required correction** Add a sentence suggesting a specific experimental approach (e.g., mutagenesis of residues 5–15 followed by binding assays) to test the proposed auxiliary role.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Presentation
- **Affected element** Figure 4C
- **Evidence pointer** Results section "NTD-RBD:RNA Behavior in the Bound State is Conserved Across Orthologs"
- **Issue** The text states that "structural models of the bound-state ensemble with six conformers each" are shown, but it is not clear how these conformers were selected from the simulation trajectories. If they are representative, the selection criteria should be stated.
- **Required correction** Clarify the selection criteria for the displayed conformers (e.g., clustering of the ensemble, lowest energy, etc.).

## Risk / unsupported claims
- The claim that the bound-state ensemble is "conserved across orthologs" is unsupported by experimental validation and relies on qualitative visual comparison of scaling maps.
- The claim that the NTD and RBD form a "positively charged groove" is inferred from simulations and has not been directly observed experimentally.
- The speculation that the second binding hotspot (residue 12 in SARS-CoV-2) has an "auxiliary regulatory role" is unsupported by functional data.
- The statement that "the ordering of the residues in the NTDSCO2 is specific" is based on a single parental sequence and may not generalize.
- The claim that the (GS)25-RBD construct binds "half as tightly" as the RBD alone is not supported by a statistical test.