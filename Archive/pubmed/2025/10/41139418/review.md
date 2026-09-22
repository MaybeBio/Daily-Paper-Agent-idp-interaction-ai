## Review setup
- **Input scope** Full manuscript text (abstract, introduction, results and discussion, conclusion) as provided
- **Assessment boundary** Scientific claims, methodology, data interpretation, and internal consistency based solely on the supplied text; no supplementary figures, tables, or experimental protocols were available for inspection
- **Shared manuscript claim summary** The authors use AlphaFold-Multimer to predict a binding interface between MYC and Miz-1 MID2 that overlaps with the MYC/MAX dimerization domain. They design stapled peptidomimetics based on this prediction, validate binding via biolayer interferometry, perform alanine scanning to identify hotspots, and demonstrate that optimized variants disrupt MYC/MAX/DNA complex formation in electrophoretic mobility shift assays with submicromolar potency, while noting some off-target effects on MAX/MAX/DNA complexes.
- **Visible evidence base** Text descriptions of AlphaFold confidence metrics (ipTM, pTM), BLI-derived observed Kd values, CD spectroscopy helicity estimates, EMSA results, and alanine scanning outcomes; all referenced figures and tables are in the Supporting Information and were not provided
- **Missing materials affecting confidence** All figures (Figure 1-4), all Supporting Information figures (S1-S18), all tables (S1-S4), experimental methods, peptide synthesis details, protein expression and purification protocols, BLI raw data, CD spectra, EMSA gel images, and AlphaFold prediction details

## Reviewer
- **Overall assessment** This manuscript presents a conceptually interesting application of AlphaFold-Multimer to a challenging intrinsically disordered protein target, with a logical workflow from prediction to peptide design to functional validation. The core idea, that an AI-predicted interface on MYC overlapping with the MAX-binding site could be targeted by Miz-1-derived peptidomimetics, is timely and potentially impactful. However, the evidence as presented in the text is insufficient to fully establish the central claims. Key quantitative data, raw experimental traces, and methodological details are all relegated to Supporting Information that was not available for review. The observed BLI binding behavior is acknowledged by the authors to be non-ideal, and the specificity concerns raised by the MAX/MAX/DNA inhibition are not adequately resolved. The manuscript reads as a proof-of-concept study with promising but preliminary results, and the strength of the conclusions currently exceeds what the visible evidence can support.
- **Who would be interested in the results, and why** Researchers working on MYC as a therapeutic target, particularly those interested in peptide-based inhibition of transcription factor PPIs; investigators studying intrinsically disordered proteins and their druggability; computational biologists using AlphaFold for PPI prediction and drug discovery; and medicinal chemists developing stapled peptide therapeutics. The demonstration that AlphaFold can identify targetable interfaces on disordered proteins could have broader methodological appeal.
- **Major strengths** The study addresses a genuinely difficult and clinically relevant target, MYC, which has long been considered undruggable. The use of AlphaFold-Multimer to predict a specific interface on an IDP is a creative and timely application of AI-based structure prediction. The workflow is logical and integrates computational prediction with experimental validation, including binding assays, alanine scanning, and functional competition assays. The identification of specific hotspot residues that align with the AlphaFold prediction provides some internal consistency. The authors are appropriately cautious about the limitations of their BLI data and acknowledge the specificity issues observed in EMSA.
- **Major Concerns**
  - **Concern ID** R1-M1
  - **Severity** Major
  - **Blocking** Yes
  - **Axis** Evidence sufficiency
  - **Claim pointer** The manuscript claims that AlphaFold-Multimer predicts Miz-1 MID2 binds at a site overlapping with the MYC/MAX dimerization domain, and that this prediction is validated by experimental binding and functional assays.
  - **Evidence pointer** Figure 1, Figure 2, Figure 3, Figure 4, Supporting Information Figures S1-S18, Tables S1-S4; location not provided
  - **Concern** All primary experimental data, including AlphaFold prediction details, BLI sensorgrams, CD spectra, EMSA gel images, and alanine scanning results, are contained exclusively in the Supporting Information, which was not provided for review. The text descriptions alone are insufficient to evaluate the quality of the data, the rigor of the analysis, or the validity of the stated quantitative values. For example, the observed Kd values are presented with error margins, but no information is given about the number of replicates, the fitting model, or the quality of the fits. The EMSA results are described qualitatively, and the claimed submicromolar potency is not supported by any visible dose-response data.
  - **Why it matters** The central claims of the paper, including the validity of the AlphaFold prediction, the binding affinity improvements from stapling, the identification of hotspots, and the functional inhibition of MYC/MAX/DNA, all rest on data that cannot be assessed from the supplied material. Without access to the primary data, the scientific case cannot be independently evaluated.
  - **Resolution test** Provide the full Supporting Information, including all figures, tables, raw data traces, and detailed methods, for review. The claims can then be assessed against the actual experimental evidence.
  - **Concern ID** R1-M2
  - **Severity** Major
  - **Blocking** Yes
  - **Axis** Specificity and mechanism
  - **Claim pointer** The manuscript claims that select Mizmetic variants disrupt MYC/MAX complex formation and prevent MYC from binding E-box DNA, while also noting that MAX/MAX DNA complex formation is reduced, "likely indicating some degree of unspecific binding."
  - **Evidence pointer** Figure 4, Supporting Information Figures S14-S18; location not provided
  - **Concern** The observed inhibition of MAX/MAX/DNA complexes by Mizmetic 16 and 20 is a significant specificity concern that is not adequately resolved. The authors state that no direct binding to MAX was observed by BLI, but this does not explain the EMSA results. The possibility that the compounds act through a non-specific mechanism, such as aggregation, DNA intercalation, or disruption of the MAX dimer, is not experimentally excluded. The claim that the compounds specifically target the MYC/MAX interface is weakened by this off-target activity.
  - **Why it matters** For a therapeutic development program, specificity is paramount. If the compounds non-specifically disrupt protein-DNA complexes, their utility as MYC/MAX inhibitors is questionable. The manuscript's own data suggest that the mechanism of action may not be as clean as proposed, and this needs to be resolved before the central claim of targeted MYC/MAX disruption can be accepted.
  - **Resolution test** Perform additional experiments to determine the mechanism of MAX/MAX/DNA inhibition, such as testing the compounds against unrelated protein-DNA complexes, assessing compound aggregation under assay conditions, or using a more direct binding assay (e.g., ITC, MST) with MAX alone. If the off-target effect cannot be eliminated, the claims should be revised to reflect a less specific mechanism.
  - **Concern ID** R1-M3
  - **Severity** Major
  - **Blocking** No
  - **Axis** Quantitative rigor
  - **Claim pointer** The manuscript reports observed Kd values of 4.6 ± 1.3 µM for Mizmetic WT, ≈176 ± 1 nM for Mizmetic 1, ≈118.6 nM for Mizmetic 2, and ≈76 ± 1 nM for Mizmetic 2 in a full concentration curve, and IC50 values of ≈3 and ≈2 µM for Mizmetic 16 against MYC/MAX and MAX/MAX, respectively, and 560 nM for Mizmetic 20 against MYC/MAX.
  - **Evidence pointer** Figure 2, Figure 4, Supporting Information Tables S2-S4, Figures S11, S15-S17; location not provided
  - **Concern** The authors acknowledge that the BLI binding curves were non-ideal and that "finding the true affinity value toward MYC" was not possible. Despite this, they report specific Kd values with small error margins. The inconsistency between the stated limitation and the precision of the reported values is concerning. Additionally, the IC50 values are presented without error estimates or information on the number of independent experiments. The use of "observed" Kd is appropriate, but the precision implied by the error values may be misleading given the acknowledged data quality issues.
  - **Why it matters** Quantitative binding and inhibition parameters are central to the claim that the stapled peptides are potent and improved over the unmodified sequence. If the data quality does not support precise values, the conclusions about relative improvements (e.g., 26-fold improvement for Mizmetic 1) may not be robust.
  - **Resolution test** Provide the raw BLI and EMSA data with details on replicates, fitting procedures, and statistical analysis. If the data quality is indeed poor, the authors should present the values as estimates with appropriate caveats and avoid over-interpreting small differences.
  - **Concern ID** R1-M4
  - **Severity** Major
  - **Blocking** No
  - **Axis** Validation of computational prediction
  - **Claim pointer** The manuscript claims that AlphaFold-Multimer predicts a 28-amino acid region of Miz-1 that binds to the MYC HLH domain, and that alanine scanning validates the predicted hotspots.
  - **Evidence pointer** Figure 1, Figure 3; location not provided
  - **Concern** The AlphaFold prediction is presented as the foundation of the study, but no details are provided about the confidence of the prediction beyond ipTM and pTM values. The ipTM of 0.33 for the initial MID2 prediction is relatively low, and the improvement to 0.5 for the truncated construct is modest. The alanine scanning results are described as validating the prediction, but only three hotspot residues are identified, and the correlation between the predicted interface and the experimental results is not quantified. The possibility that the peptide binds to a different site than predicted is not excluded.
  - **Why it matters** The entire study is predicated on the accuracy of the AlphaFold prediction. If the prediction is not reliable, the design rationale for the peptides is weakened. The validation of the prediction is therefore critical, and the current evidence is suggestive but not conclusive.
  - **Resolution test** Provide a more detailed analysis of the AlphaFold prediction, including per-residue confidence scores, a comparison of the predicted interface with the experimental alanine scanning data, and ideally a mutagenesis study on the MYC side to confirm the binding site. If the prediction is not fully validated, the claims should be tempered accordingly.
- **Minor Comments**
  - **Concern ID** R1-m1
  - **Severity** Minor
  - **Axis** Clarity
  - **Affected element** Abstract
  - **Evidence pointer** Abstract; location not provided
  - **Issue** The abstract states that Mizmetic 2 "binds MYC" and that optimized variants "disrupt MYC/MAX complex formation," but the specificity concerns regarding MAX/MAX inhibition are only mentioned in the Results section. The abstract may overstate the selectivity of the compounds.
  - **Required correction** Consider adding a brief caveat in the abstract about the observed off-target effects on MAX/MAX complexes to accurately represent the findings.
  - **Concern ID** R1-m2
  - **Severity** Minor
  - **Axis** Internal consistency
  - **Affected element** Results section, subsection on alanine scanning
  - **Evidence pointer** Figure 3, Table S4; location not provided
  - **Issue** The text states that five alanine mutants displayed "slightly increased binding" but does not specify the magnitude of the increase or whether these differences are statistically significant. The term "slightly" is vague.
  - **Required correction** Provide quantitative values for the binding changes and indicate statistical significance, or revise the language to avoid implying quantitative differences without supporting data.
  - **Concern ID** R1-m3
  - **Severity** Minor
  - **Axis** Methodology
  - **Affected element** BLI assay description
  - **Evidence pointer** Results section, subsection on stapling; location not provided
  - **Issue** The authors mention optimizing BLI assay conditions but do not describe the final optimized conditions in the text. The reader is referred to the Supporting Information, but the key parameters (e.g., buffer composition, blocking agents, peptide loading density) are not summarized.
  - **Required correction** Briefly summarize the optimized BLI conditions in the main text to allow readers to assess the assay quality without accessing the Supporting Information.
  - **Concern ID** R1-m4
  - **Severity** Minor
  - **Axis** Interpretation
  - **Affected element** Discussion of MAX/MAX inhibition
  - **Evidence pointer** Figure 4, Supporting Information Figure S18; location not provided
  - **Issue** The authors state that no direct binding to MAX was observed by BLI, but this is inconsistent with the EMSA results showing inhibition of MAX/MAX/DNA. The explanation that MAX exists as a dimer in solution and blocks the binding site is speculative.
  - **Required correction** Acknowledge the inconsistency more explicitly and consider alternative explanations, such as the compounds interfering with DNA binding rather than protein-protein interactions, or suggest experiments to resolve the discrepancy.

## Risk / unsupported claims
- The claim that AlphaFold-Multimer accurately predicts the MYC/Miz-1 binding interface is not fully supported without access to the prediction details and confidence metrics beyond the reported ipTM/pTM values.
- The reported Kd values, particularly for Mizmetic WT, are presented with a precision that is inconsistent with the acknowledged non-ideal BLI binding behavior.
- The claim that optimized variants "disrupt MYC/MAX complex formation" with submicromolar potency is not verifiable without the EMSA dose-response data and quantification methods.
- The statement that the compounds prevent MYC from binding E-box DNA is inferred from EMSA but the mechanism (direct competition vs. allosteric vs. non-specific) is not established.
- The explanation for the observed MAX/MAX/DNA inhibition is speculative and not supported by direct experimental evidence.
- The overall conclusion that this work "establishes a strategy for targeting transient but structurally precise IDP interfaces" is premature given the unresolved specificity issues and the preliminary nature of the data.

## Assessment against Nature-style criteria
- **Originality** The application of AlphaFold-Multimer to identify a targetable interface on an IDP like MYC is a creative and relatively novel approach. The specific focus on the MYC/Miz-1 interface as a therapeutic target is underexplored, and the idea of using Miz-1-derived peptides to disrupt MYC/MAX adds a new angle. However, the concept of stapled peptides targeting MYC is not entirely new, and the originality lies mainly in the computational-guided discovery aspect.
- **Scientific importance** MYC is a high-value oncology target, and any credible new approach to inhibit it would be of significant interest. The potential to target the MYC/Miz-1 interaction, which is less studied than MYC/MAX, could open new therapeutic avenues. However, the importance of the findings is currently limited by the unresolved specificity issues and the lack of cellular or in vivo data.
- **Interdisciplinary readership** The work bridges computational biology, structural biology, peptide chemistry, and cancer biology, which could appeal to a broad audience. The use of AlphaFold is timely and would attract attention from the computational community, while the therapeutic angle would interest medicinal chemists and cancer researchers.
- **Technical soundness** The experimental design is logical, but the technical execution cannot be fully assessed without the Supporting Information. The acknowledged issues with BLI data quality and the unexplained off-target effects on MAX/MAX complexes are significant technical concerns that need to be addressed.
- **Readability for nonspecialists** The manuscript is generally well-written and accessible. The concepts are explained clearly, and the flow from prediction to design to validation is easy to follow. However, some sections, particularly the discussion of BLI and EMSA, assume familiarity with these techniques.

## Recommendation posture
Supportive if technical concerns are resolved. The core concept is interesting and the workflow is logical, but the current evidence base is insufficient to fully establish the claims. The authors must provide the Supporting Information for review, address the specificity concerns regarding MAX/MAX inhibition, and reconcile the reported quantitative values with the acknowledged data quality limitations. If these issues are resolved, the manuscript could make a valuable contribution to the field of IDP targeting and MYC inhibition.