## Review setup
- **Input scope** Full manuscript text, including abstract, introduction, results, discussion, conclusions, and supplementary material references.
- **Assessment boundary** Scientific content, experimental design, data interpretation, and claims as presented in the provided text. No access to raw data, supplementary figures/tables, or experimental protocols beyond what is described.
- **Shared manuscript claim summary** The authors report that 12-deoxyfusicoccin (12-dFC), a semisynthetic derivative of fusicoccin A, selectively stabilizes the interaction between 14-3-3 proteins and the intrinsically disordered phosphoprotein GIGYF2 at a mode-1 consensus motif containing phosphorylated S546. This stabilization enhances GIGYF2-mediated translational repression, suppresses protein synthesis, and inhibits cell proliferation. The authors further propose that AMPK mediates S546 phosphorylation, linking energy stress to translational control.
- **Visible evidence base** Abstract, main text figures (referenced as Figures A–E across sections), supplementary tables (S1–S6), and supplementary figures (S1–S15) as cited. Specific numerical data are provided for binding affinity (Kd values) and cell viability.
- **Missing materials affecting confidence** Raw proteomics data, full supplementary figures and tables, experimental protocols, statistical analysis details, and structural data (e.g., crystallography or modeling) are not available for verification. The manuscript text alone does not permit independent assessment of data quality or reproducibility.

## Reviewer
- **Overall assessment** This manuscript presents a compelling and potentially significant finding: the identification of GIGYF2 as a target of 12-dFC, a molecular glue that stabilizes 14-3-3 interactions with a disordered phosphoprotein. The work is well-motivated, and the experimental approach is logical, progressing from unbiased proteomics to biochemical validation and functional assays. The claim that 12-dFC enhances translational repression via GIGYF2 is supported by multiple lines of evidence, including BONCAT and knockdown experiments. However, several technical concerns, particularly regarding the directness of AMPK involvement, the specificity of the molecular glue mechanism, and the quantitative rigor of some assays, need to be addressed before the case is fully established.
- **Who would be interested in the results, and why** Chemical biologists studying molecular glues and PPI stabilizers; researchers investigating 14-3-3 signaling and its role in disease; cancer biologists interested in translational control and metabolic stress responses; and drug discovery scientists seeking new therapeutic strategies targeting protein-protein interactions involving intrinsically disordered proteins.
- **Major strengths** 1) The identification of a novel 14-3-3 client (GIGYF2) selectively stabilized by 12-dFC, with clear differential activity versus 12-hFC, provides a strong structure-activity relationship foundation. 2) The functional link between 12-dFC-mediated stabilization and translational repression is convincingly demonstrated through BONCAT and knockdown experiments. 3) The proposed connection to AMPK and energy stress offers a physiologically relevant context that broadens the significance of the work. 4) The study addresses an underexplored area: stabilizing PPIs involving intrinsically disordered proteins, which is technically challenging and conceptually important.
- **Major Concerns** R1-M1, R1-M2, R1-M3, R1-M4, R1-M5
- **Minor Comments** R1-m1, R1-m2, R1-m3, R1-m4
- **Technical failings that need to be addressed before the case is established** R1-M1 (direct AMPK phosphorylation), R1-M2 (specificity of 12-dFC for GIGYF2), R1-M3 (quantitative rigor of FP assay), R1-M4 (proteomics validation)
- **Assessment against Nature-style criteria** Originality: High. The work introduces a new target for molecular glue stabilization and a novel mechanism linking energy stress to translational control via a disordered phosphoprotein. Scientific importance: High. The findings have implications for understanding 14-3-3 biology, translational regulation, and potential therapeutic development. Interdisciplinary readership: Moderate to high. The work bridges chemical biology, cell signaling, and cancer biology, though the technical detail may limit accessibility to a broader audience. Technical soundness: Moderate. The experimental design is generally sound, but several concerns (see Major Concerns) require clarification or additional data. Readability for nonspecialists: Moderate. The manuscript is clearly written but assumes familiarity with molecular glue concepts and 14-3-3 biology.
- **Recommendation posture** Supportive if technical concerns are resolved. The core finding is novel and potentially impactful, but the current evidence does not fully establish the direct role of AMPK or the specificity of 12-dFC for GIGYF2 over other 14-3-3 clients.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Claim support
- **Claim pointer** The authors state that "AMPK mediates S546 phosphorylation" and that this is "critical" for the proposed mechanism linking energy stress to translational control.
- **Evidence pointer** Results section "AMPK Mediates Phosphorylation-Dependent GIGYF2–14-3-3 Interaction", Figures A–B, Table S6
- **Concern** The evidence for AMPK-mediated phosphorylation of S546 is indirect. The authors show that AICAR treatment enhances 14-3-3 binding to wild-type GIGYF2 but not the S546A mutant, and that kinase prediction software ranks AMPK as the top candidate. However, no direct evidence is provided that AMPK phosphorylates S546, such as an in vitro kinase assay with purified AMPK and GIGYF2 peptide, or phospho-specific antibodies. The authors themselves acknowledge that "further investigation is required to determine whether AMPK directly phosphorylates S546 or acts through downstream effectors," which undermines the strength of this claim.
- **Why it matters** The proposed link between AMPK and GIGYF2 phosphorylation is a central part of the manuscript's significance, as it connects energy stress to translational control. If this link is not directly established, the physiological relevance of the findings is weakened, and the mechanistic model presented in the Discussion becomes speculative.
- **Resolution test** Provide direct biochemical evidence, such as an in vitro kinase assay showing AMPK phosphorylates a GIGYF2 peptide containing S546, or use of a phospho-S546-specific antibody to demonstrate increased phosphorylation upon AMPK activation. Alternatively, use AMPK inhibitors or knockdown to show loss of S546 phosphorylation.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Specificity
- **Claim pointer** The authors claim that 12-dFC selectively stabilizes the 14-3-3–GIGYF2 interaction, implying specificity for this client over other 14-3-3 binding partners.
- **Evidence pointer** Results section "Tandem-Affinity Purification", Figures A–C, Table S1
- **Concern** The proteomics experiment identified GIGYF2 as a prominent hit, but the manuscript does not report whether other known 14-3-3 clients were also enriched in the presence of 12-dFC. The claim of selectivity is based on the comparison with 12-hFC, but the full list of proteins affected by 12-dFC is not discussed. Without this information, it is unclear whether 12-dFC is truly selective for GIGYF2 or whether it stabilizes multiple 14-3-3 interactions, with GIGYF2 being the most abundant or most easily detected.
- **Why it matters** The therapeutic potential of 12-dFC as a molecular glue depends on its selectivity. If it broadly stabilizes 14-3-3 interactions, the observed effects on translational repression and cell proliferation may be due to off-target effects rather than specific GIGYF2 engagement.
- **Resolution test** Provide a comprehensive list of proteins enriched in the 12-dFC condition compared to controls, and discuss whether other known 14-3-3 clients are affected. If selectivity is claimed, demonstrate that 12-dFC does not stabilize interactions with a panel of other 14-3-3 clients, either by proteomics or targeted biochemical assays.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Quantitative rigor
- **Claim pointer** The authors report a "approximately 50-fold" enhancement in binding affinity of the KGVpS546IP peptide for 14-3-3 in the presence of 12-dFC, based on fluorescence polarization (FP) assays.
- **Evidence pointer** Results section "12-dFC and 14-3-3 Bind to the GIGYF2 Consensus Motif", Figure E, Figure S7
- **Concern** The FP assay is described, but the manuscript does not provide details on the number of replicates, error analysis, or the fitting model used to determine Kd values. The reported Kd values (68.7 ± 20.2 μM without 12-dFC, 1.41 ± 0.09 μM with 12-dFC) show a large relative error for the weaker binding, which could affect the reliability of the calculated fold enhancement. Additionally, the assay uses a short phosphopeptide, which may not fully recapitulate the binding of the full-length disordered protein.
- **Why it matters** The quantitative claim of a 50-fold enhancement is a key piece of evidence for the molecular glue mechanism. If the assay is not rigorously performed or the error is underestimated, the strength of this claim is diminished.
- **Resolution test** Provide full experimental details for the FP assay, including replicates, error propagation, and the fitting model. Consider validating the fold enhancement with an orthogonal method, such as isothermal titration calorimetry (ITC) or surface plasmon resonance (SPR), using a longer GIGYF2 peptide or the full-length protein.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Validation
- **Claim pointer** The authors state that 12-dFC downregulates glycolysis-related proteins, based on 2D-DIGE proteomic analysis.
- **Evidence pointer** Results section "12-dFC Downregulates the Expression of Glycolysis-Related Proteins", Figure , Tables S2–S4
- **Concern** The 2D-DIGE experiment is described, but the manuscript does not provide validation of the proteomic findings, such as Western blot confirmation of specific downregulated proteins. Additionally, the statistical criteria for identifying differentially expressed proteins are not stated, and the number of biological replicates is not mentioned. The comparison with 150 bioactive compounds is interesting but lacks a clear quantitative framework for assessing the significance of the observed downregulation.
- **Why it matters** The downregulation of glycolysis-related proteins is presented as a functional consequence of 12-dFC treatment, linking the molecular mechanism to a metabolic phenotype. Without validation, this finding remains preliminary and could be an artifact of the 2D-DIGE methodology.
- **Resolution test** Validate at least two downregulated glycolysis-related proteins by Western blot or qPCR. Provide details on the statistical analysis, including the number of replicates and the criteria for significance. If possible, perform a targeted proteomics experiment to confirm the 2D-DIGE results.

- **Concern ID** R1-M5
- **Severity** Major
- **Blocking** No
- **Axis** Mechanistic model
- **Claim pointer** The authors propose a model in which 12-dFC stabilizes the 14-3-3–GIGYF2 interaction, enhancing TTP recruitment and translational repression, and that this is linked to AMPK-mediated phosphorylation under energy stress.
- **Evidence pointer** Discussion section, Figures A–B
- **Concern** The proposed model is plausible but relies on several assumptions that are not directly tested. For example, the manuscript does not demonstrate that 12-dFC enhances the formation of a ternary complex containing 14-3-3, GIGYF2, and TTP in cells. The interaction between GIGYF2 and TTP is shown to be enhanced by 12-dFC, but the stoichiometry and dynamics of the proposed complex are not characterized. Additionally, the link between AMPK activation and translational repression is inferred from AICAR experiments but not directly shown to be dependent on GIGYF2.
- **Why it matters** The model is a central part of the manuscript's significance, as it proposes a new mechanism for regulating translation in response to energy stress. If the model is not fully supported by the data, the broader implications of the work are weakened.
- **Resolution test** Perform co-immunoprecipitation experiments to demonstrate the formation of a ternary complex containing 14-3-3, GIGYF2, and TTP in the presence of 12-dFC. Use a GIGYF2 knockout or knockdown cell line to show that the effects of 12-dFC on translational repression and cell proliferation are dependent on GIGYF2. Additionally, test whether AMPK activation leads to increased S546 phosphorylation in a GIGYF2-dependent manner.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Abstract
- **Evidence pointer** Abstract, first sentence
- **Issue** The phrase "Chemical stabilization of protein–protein interactions involving intrinsically disordered phosphoproteins is an emerging yet challenging problem" is somewhat vague. It would be clearer to specify what makes this challenging (e.g., the lack of defined binding pockets, the transient nature of the interactions).
- **Required correction** Revise the sentence to briefly indicate the specific challenges, such as "due to the lack of stable binding interfaces and the dynamic nature of disordered regions."

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Data presentation
- **Affected element** Results section "Tandem-Affinity Purification"
- **Evidence pointer** Figure B, Table S1
- **Issue** The manuscript states that "elevated levels in several proteins upon 12-dFC treatment" were observed, but the criteria for "elevated" are not defined. It is unclear whether this is based on fold-change, statistical significance, or both.
- **Required correction** Define the threshold for elevated levels (e.g., >2-fold change with p < 0.05) and state the number of proteins meeting this criterion.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Results section "12-dFC and 14-3-3 Bind to the GIGYF2 Consensus Motif"
- **Evidence pointer** Figure D
- **Issue** The single-mutation experiments show that S546A has a greater impact than S438A, but the manuscript does not report whether the double mutant (S438A/S546A) has an additive or synergistic effect. This information would help clarify the relative contributions of the two sites.
- **Required correction** Include data for the double mutant in Figure D or discuss why it was not included.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Interpretation
- **Affected element** Discussion section
- **Evidence pointer** Discussion, paragraph on AMPK
- **Issue** The manuscript states that "AMPK mediates S546 phosphorylation" but later acknowledges that "further investigation is required to determine whether AMPK directly phosphorylates S546 or acts through downstream effectors." This inconsistency could confuse readers.
- **Required correction** Revise the earlier statement to be more cautious, such as "AMPK activation is associated with S546 phosphorylation" and reserve the direct mediation claim for the Discussion where it is appropriately qualified.

## Risk / unsupported claims
- The claim that AMPK directly mediates S546 phosphorylation is not supported by direct biochemical evidence; the data only show correlation with AICAR treatment and kinase prediction.
- The claim that 12-dFC selectively stabilizes the 14-3-3–GIGYF2 interaction is not fully supported, as the full proteomics dataset is not presented and other potential 14-3-3 clients are not discussed.
- The proposed model of a ternary complex involving 14-3-3, GIGYF2, and TTP is speculative and not directly tested.
- The statement that 12-dFC is "the first antiproliferative agent that suppresses translation by selectively stabilizing PPIs within mRNA translational repression complexes" is a strong claim that would require a comprehensive literature review to substantiate.
- The functional significance of S546 phosphorylation under starvation conditions is inferred from a single experiment (Figure C) and requires further validation, including quantification and statistical analysis.