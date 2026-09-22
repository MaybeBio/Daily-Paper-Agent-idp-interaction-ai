## Review setup
- **Input scope** Full manuscript text including abstract, introduction, experimental section, results and discussion, conclusions, and supplementary material references.
- **Assessment boundary** Scientific content, methodological rigor, internal consistency, and support of claims by presented evidence. No assessment of formatting, grammar, or journal fit beyond Nature-style criteria.
- **Shared manuscript claim summary** The authors report that the B-box domain of HMGB1 forms self-associates approximately 30 nm in size, that these associates bind heparin with higher apparent affinity than monomeric B-box, that the secondary and tertiary structure of B-box is preserved upon association, and that AlphaFold modeling suggests charge redistribution in oligomers enhances electrostatic attraction to polyanions.
- **Visible evidence base** DLS data, CD spectra, fluorescence spectra, cw-EPR spectra, native PAGE gel shift assays, heparin-sepharose chromatography, TIM-MS data, AlphaFold models, and supporting figures referenced in the Supplementary Material.
- **Missing materials affecting confidence** Supplementary figures S1–S10 are referenced but not provided in the submitted text. Raw data, error bars, replicate numbers, and statistical analyses are not shown for DLS, CD, fluorescence, or EPR measurements. Experimental details for AlphaFold model validation and charge calculation methodology are incomplete.

## Reviewer
- **Overall assessment** The manuscript addresses a relevant question regarding HMGB1 B-box self-association and its effect on heparin binding. The combination of biophysical techniques is appropriate and the observation that B-box associates bind heparin more strongly than monomers is potentially interesting. However, the evidence presented is insufficient to fully establish the central claims. Key quantitative data are missing, the interpretation of EPR results requires more rigorous analysis, and the AlphaFold-based mechanistic explanation is speculative without experimental validation. The manuscript would benefit from additional experiments and clearer presentation of quantitative results.

- **Who would be interested in the results, and why** Researchers studying HMGB1 biology, particularly its extracellular functions as a damage-associated molecular pattern and its interactions with glycosaminoglycans. The work may also interest biophysicists studying protein-polyelectrolyte interactions and the role of protein self-association in modulating binding affinity. Additionally, those investigating liquid-liquid phase separation of proteins and its functional consequences may find the observations relevant.

- **Major strengths** The study combines multiple orthogonal biophysical techniques to characterize B-box self-association and heparin binding. The use of EPR spectroscopy to probe local dynamics at a specific residue is methodologically sound. The observation that B-box associates bind heparin with higher apparent affinity than monomers is novel and potentially significant. The authors appropriately note the lack of structural perturbation upon association, which strengthens the interpretation that functional differences arise from avidity effects rather than conformational changes.

- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence sufficiency
- **Claim pointer** The authors claim that B-box forms 30 nm large self-associates and that approximately half of the protein is in associated form.
- **Evidence pointer** Results section "Formation of B-Box Associates during the Expression Procedure", Figure 1, Supplementary Figures S6 and S7
- **Concern** The DLS data are presented without quantitative analysis. The hydrodynamic radius distribution is described qualitatively, but no information is provided on the polydispersity index, the relative intensity or mass fraction of each peak, or the reproducibility across multiple preparations. The claim that approximately half of the protein is associated is based on UV-vis intensity at 280 nm of filtered fractions, but the extinction coefficients for monomeric versus associated forms may differ, and no correction for this is described. Additionally, the assignment of the 2.3 nm peak to oligomers of approximately eight monomers is based on a volume estimate that assumes spherical geometry and close packing, which is not justified.
- **Why it matters** The central premise of the study is that B-box self-association modulates heparin binding. Without robust quantitative characterization of the association state, including the size distribution, the fraction of associated protein, and the stability of these associates, the subsequent comparisons between monomeric and associated forms are difficult to interpret.
- **Resolution test** Provide quantitative DLS analysis including polydispersity indices, intensity and mass-weighted size distributions, and replicate measurements. Provide a more rigorous determination of the fraction of associated protein using methods such as size-exclusion chromatography with multi-angle light scattering or analytical ultracentrifugation. Justify the oligomer size estimate with additional data or modeling.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Interpretation of EPR data
- **Claim pointer** The authors claim that EPR spectroscopy shows that the presence of B-box associates significantly enhances interactions with heparin, and that the interaction site is close to Cys19.
- **Evidence pointer** Results section "B-Box Binding Patterns to Heparin in Single and Self-Associated States", Figures 3 and S9
- **Concern** The EPR data are interpreted primarily through changes in the 2Azz value, but the analysis is incomplete. No spectral simulation or fitting is presented to extract quantitative parameters such as rotational correlation times, order parameters, or populations of bound versus free species. The claim that the interaction site is close to Cys19 is based on the appearance of resolved z-components, but this interpretation requires more rigorous analysis. Additionally, the statement that a molar ratio of 3:50 heparin to B-box is sufficient for a majority of protein molecules to be bound is not supported by any quantitative analysis of the spectra. The decrease in 2Azz at high heparin concentrations is interpreted as a reduction in complex size, but alternative explanations such as changes in local dynamics or protein unfolding are not discussed.
- **Why it matters** The EPR data are the primary evidence for enhanced heparin binding in the associated state and for the location of the binding site. Without quantitative spectral analysis, the conclusions drawn from these data are not fully supported.
- **Resolution test** Perform spectral simulations to extract quantitative parameters. Provide titration curves with error bars and fit the data to a binding model. Use power saturation or other methods to verify that the spectral changes are due to binding rather than other effects. Consider site-directed spin labeling at multiple positions to map the binding interface more rigorously.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Mechanistic explanation
- **Claim pointer** The authors claim that AlphaFold modeling reveals that oligomer formation induces charge redistribution, resulting in an extended positively charged region that enhances electrostatic attraction to heparin.
- **Evidence pointer** Results section "B-Box Binding Patterns to Heparin in Single and Self-Associated States", Figure 4
- **Concern** The AlphaFold predictions are presented as a mechanistic explanation for the enhanced heparin binding, but the models are not experimentally validated. The charge distribution calculations are described only qualitatively, and no quantitative comparison between monomeric and oligomeric charge distributions is provided. The relationship between the predicted charge patches and the experimentally observed binding enhancement is correlative, not causal. Furthermore, the AlphaFold models are not validated by any experimental structural data, and the accuracy of the predicted oligomer interfaces is unknown.
- **Why it matters** The proposed mechanism is a key part of the manuscript's conclusion. Without experimental validation or at least a more rigorous computational analysis, the mechanistic claim remains speculative.
- **Resolution test** Provide quantitative analysis of the electrostatic potential surfaces for monomers and oligomers. Validate the predicted oligomer interfaces using cross-linking mass spectrometry, mutagenesis, or other experimental approaches. Alternatively, temper the mechanistic claims and present the AlphaFold results as a hypothesis requiring further testing.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Quantitative comparison
- **Claim pointer** The authors claim that the associated form of B-box exhibits increased binding affinity to heparin compared to the monomeric form.
- **Evidence pointer** Results section "B-Box Binding Patterns to Heparin in Single and Self-Associated States", Figures 3 and S9
- **Concern** The comparison between monomeric and associated forms is made at different effective protein concentrations, since the associated form represents a locally concentrated state. The authors do not account for this difference in their interpretation. The claim of increased binding affinity could be due to avidity effects from the local concentration of binding sites rather than an intrinsic change in affinity per binding site. No binding constants or quantitative affinity measures are provided.
- **Why it matters** The central conclusion of the manuscript is that self-association enhances heparin binding. Without quantitative binding affinities or a clear distinction between avidity and intrinsic affinity effects, the conclusion is not fully supported.
- **Resolution test** Perform quantitative binding assays, such as isothermal titration calorimetry or surface plasmon resonance, to determine binding constants for monomeric and associated forms. Alternatively, use competition assays to compare apparent affinities under controlled conditions.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Methodological detail
- **Affected element** Protein concentration determination
- **Evidence pointer** Experimental section "B-Box HMGB1 Domain Expression and Purification"
- **Issue** The extinction coefficient used for concentration determination is stated as 11,460 M-1 cm-1, which is identical to the molecular weight in Da. This appears to be a coincidence or an error, as extinction coefficients are typically derived from amino acid composition. The authors should verify this value.
- **Required correction** Verify the extinction coefficient calculation and provide the correct value with appropriate justification.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Data presentation
- **Affected element** Native PAGE gel shift assay
- **Evidence pointer** Results section "B-Box Binding Patterns to Heparin in Single and Self-Associated States", Figure 2
- **Issue** The native PAGE experiment is described as showing binding, but no quantification or replicate data are provided. The figure is not available in the submitted text.
- **Required correction** Provide the figure with appropriate labels and quantification of the shift. Include replicate experiments and a control for the effect of the FITC label on binding.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Clarity of writing
- **Affected element** Abstract and Introduction
- **Evidence pointer** Abstract, Introduction
- **Issue** The abstract states that B-box forms 30 nm associates, but the DLS data show a peak at 32 nm. The discrepancy is not explained. Additionally, the introduction could more clearly distinguish between the A-box and B-box contributions to heparin binding.
- **Required correction** Reconcile the size values or explain the discrepancy. Clarify the relative contributions of A-box and B-box to heparin binding in the introduction.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Supplementary material
- **Affected element** Supplementary Figures S1–S10
- **Evidence pointer** Supplementary Material section
- **Issue** The supplementary figures are referenced but not provided. Without these, the reader cannot fully evaluate the data.
- **Required correction** Ensure all supplementary figures are included in the submission and referenced appropriately.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Terminology
- **Affected element** "Protein-Polyelectrolyte Interactions" in title
- **Evidence pointer** Title
- **Issue** The title uses "Protein-Polyelectrolyte Interactions" which is broad. The study specifically addresses heparin binding. A more specific title may better reflect the content.
- **Required correction** Consider revising the title to be more specific, such as "Self-Association of HMGB1 B-Box Domain Enhances Heparin Binding."

## Risk / unsupported claims
- The claim that approximately half of the protein is in associated form is not quantitatively supported by the data presented.
- The claim that the interaction site of heparin is close to Cys19 is based on qualitative EPR line shape analysis and requires more rigorous spectral analysis.
- The AlphaFold-based mechanism of charge redistribution enhancing electrostatic attraction is speculative and not experimentally validated.
- The claim that the final state after adding excess heparin is comparable for monomeric and associated forms is based on visual comparison of spectra without quantitative analysis.
- The statement that oligomers of approximately eight monomers are present is based on an unvalidated volume estimate.
- The claim that the B-box associates are stable over 6 hours is based on a single DLS measurement without replicate data.