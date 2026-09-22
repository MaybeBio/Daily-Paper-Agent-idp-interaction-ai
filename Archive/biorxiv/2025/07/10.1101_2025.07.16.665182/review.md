## Review setup
- **Input scope** Full manuscript text including abstract, introduction, results, discussion, methods, and supplementary figure legends
- **Assessment boundary** Scientific claims, experimental design, data interpretation, and technical soundness as presented in the provided text
- **Shared manuscript claim summary** The authors propose that the intrinsically disordered L2 linker of KANK1 binds the hub protein LC8 through multiple weak, noncanonical motifs, and that cooperative multivalency converts this disordered region into an elongated, rod-like assembly capable of bridging the 35–50 nm membrane–microtubule gap at focal adhesions
- **Visible evidence base** In-cell colocalization, pulldown assays, ITC, SEC-MALS, SV-AUC, AlphaFold predictions, negative stain electron microscopy, and worm-like chain calculations
- **Missing materials affecting confidence** Figures S1–S13, all main text figures, raw ITC thermograms, SEC-MALS elution profiles, AUC sedimentation data, NSEM micrographs, AlphaFold confidence metrics, and detailed statistical analyses

## Reviewer
- **Overall assessment** This manuscript addresses a compelling question in cellular architecture: how a long intrinsically disordered region can span a defined subcellular gap. The central hypothesis, that cooperative multivalency among weak LC8 binding motifs drives formation of an elongated rod, is conceptually interesting and potentially generalizable. However, the evidence presented in the text is insufficient to fully establish the claims. Key quantitative data are described but not shown, the relationship between in vitro assemblies and in-cell function remains correlative, and the structural model relies heavily on AlphaFold predictions without adequate experimental validation. The work is potentially significant but requires substantial additional evidence and clarification before the central conclusions can be accepted.
- **Who would be interested in the results, and why** Cell biologists studying cytoskeletal organization, focal adhesion dynamics, and microtubule regulation would find the KANK1–LC8 interaction relevant. Structural biologists interested in intrinsically disordered proteins and multivalent assemblies would value the proposed design principles. Researchers studying LC8 biology and its expanding client repertoire would also be interested. The broader concept of using weak multivalent interactions to rigidify disordered regions could appeal to those working on protein architecture and biomolecular condensates.
- **Major strengths** The study tackles a genuine paradox in cellular architecture with a plausible mechanistic solution. The combination of in-cell, biochemical, biophysical, and computational approaches is ambitious and appropriate for the question. The observation that isolated peptides fail to bind while the multivalent construct binds tightly is a clean demonstration of cooperativity. The comparison with KANK2, which lacks LC8 binding, provides a useful negative control. The potential generalizability of the design principles is thought-provoking.
- **Major Concerns** The manuscript does not provide sufficient quantitative evidence to support several central claims. The worm-like chain calculation is described but the parameters and results are not fully justified. The ITC data for KANK1 595-720 and KANK1 500-805 are reported with stoichiometries of approximately 6 and 18 LC8 dimers, respectively, but the raw data and fitting details are not shown. The SEC-MALS and AUC data are described qualitatively without presenting the actual profiles or derived masses. The AlphaFold predictions are central to the structural model, but the confidence metrics and validation against experimental data are not adequately described. The NSEM images are mentioned but not shown, and the particle counts for angle measurements are not provided. The claim that the rod spans the 35–50 nm gap is based on extrapolation from in vitro assemblies and AlphaFold models, not direct in-cell measurements. The functional significance of LC8 binding for KANK1's role in microtubule organization is not directly tested.
- **Assessment against Nature-style criteria** Originality: The concept of using cooperative multivalency among weak motifs to rigidify a disordered region is novel and potentially impactful. Scientific importance: If fully established, this mechanism could explain how other long disordered linkers achieve defined lengths and rigidity, with implications for cellular architecture. Interdisciplinary readership: The work bridges cell biology, biophysics, and structural biology, which could attract a broad audience. Technical soundness: The experimental approaches are appropriate, but the presented evidence is incomplete and does not yet meet the standard required for a high-impact journal. Readability for nonspecialists: The writing is generally clear, but the significance of the findings would be more accessible with better contextualization of the paradox and its resolution.

### Major Concerns
- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence sufficiency
- **Claim pointer** The authors claim that KANK1 595-720 binds LC8 with a stoichiometry of approximately 6 LC8 dimers and a Kd of 893 ± 49 nM, and that KANK1 500-805 binds approximately 18 LC8 dimers with a Kd of 579 ± 65 nM
- **Evidence pointer** Results section, ITC experiments, Figure 3d and 6d (figures not provided)
- **Concern** The ITC data are reported as fitted values, but the raw thermograms, integrated heats, and fitting residuals are not shown. The stoichiometry of 5.78 ± 0.02 for KANK1 595-720 is unusually precise and may not be reliable given the authors' own caveat about the independent-sites model. For KANK1 500-805, the stoichiometry of 17.98 ± 0.07 is reported with a precision that seems inconsistent with the complexity of the system. The fitting procedure for KANK1 500-805, which required doubling the cell concentration to accommodate the software's maximum stoichiometry of 10, is a significant methodological concern that could introduce systematic errors.
- **Why it matters** The stoichiometry and affinity are central to the claim of multivalent, cooperative binding. If the stoichiometry is incorrect, the model of seven LC8 dimers per KANK1 strand in the 595-720 region and fifteen in the full L2 region would be unsupported. The reported precision of the fits suggests a level of confidence that may not be justified.
- **Resolution test** Provide raw ITC thermograms, integrated heat plots, and fitting residuals for all titrations. Justify the choice of the independent-sites model and address potential systematic errors in the KANK1 500-805 fitting procedure. Report confidence intervals for stoichiometry and Kd values.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence sufficiency
- **Claim pointer** The authors claim that SEC-MALS and SV-AUC experiments support the formation of a 14:2 LC8:KANK1 595-720 complex and a 15:2 LC8:KANK1 500-805 complex
- **Evidence pointer** Results section, SEC-MALS and SV-AUC experiments, Figures 3e-f and 6e-f (figures not provided)
- **Concern** The SEC-MALS and AUC data are described only qualitatively. The elution profiles, MALS-derived masses across the peaks, and sedimentation coefficient distributions are not shown. The claim that the mass along the SEC-MALS peak is not uniform due to partial dissociation is not supported by any quantitative analysis. The AUC data are described as showing three species at low ratios, but the sedimentation coefficients and their assignments are not provided. Without these data, it is impossible to assess whether the proposed stoichiometries are correct or whether the observed species are consistent with the proposed model.
- **Why it matters** The stoichiometry of the complex is a key claim. If the SEC-MALS and AUC data do not clearly support the proposed 14:2 and 15:2 complexes, the model of cooperative multivalency would be weakened. The presence of higher-order aggregates in the KANK1 500-805 samples further complicates interpretation.
- **Resolution test** Provide SEC-MALS elution profiles with MALS-derived molar masses across each peak, and AUC c(s) distributions with sedimentation coefficients for all titration points. Quantitatively analyze the mass distributions and discuss how they support the proposed stoichiometries.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence sufficiency
- **Claim pointer** The authors claim that AlphaFold predictions identify 15+ LC8 binding sites in KANK1-L2 and that AlphaFold Multimer titrations predict a rod-like structure with seven LC8 dimers packed on two parallel KANK1 strands
- **Evidence pointer** Results section, AlphaFold predictions, Figures 5a-f and 6a-c (figures not provided)
- **Concern** The AlphaFold methodology is described briefly, but the results are not presented in sufficient detail. The predicted binding sites are listed in the text, but the confidence scores, the specific residues involved, and the comparison between the exclusive and inclusive thresholds are not shown. The AlphaFold Multimer titrations are described as predicting a rod-like structure, but the structural models, the confidence metrics (pLDDT, PAE), and the validation of these predictions against experimental data are not provided. The claim that the rod is "highly confident" is not supported by any quantitative metrics.
- **Why it matters** AlphaFold predictions are used to identify the binding sites and to model the overall structure. If the predictions are not reliable, the identification of the specific motifs and the structural model would be called into question. The authors acknowledge that AlphaFold predictions can be unreliable for weak or noncanonical motifs, which is exactly the case here.
- **Resolution test** Provide the AlphaFold confidence metrics for all predicted binding sites, including pLDDT and PAE values. Show the predicted structural models with confidence coloring. Validate the predictions against the experimental binding data, such as the pulldown and ITC results.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence sufficiency
- **Claim pointer** The authors claim that negative stain electron microscopy reveals rod-like structures for KANK1 595-720 and KANK1 500-805 in complex with LC8, with the KANK1 500-805 complex forming a closed hairpin configuration
- **Evidence pointer** Results section, NSEM experiments, Figures 6g-j (figures not provided)
- **Concern** The NSEM data are described qualitatively, but the micrographs, class averages, and particle counts are not shown. The claim that the KANK1 595-720 complex forms straight rods with seven segments is based on a small number of manually picked particles (24 for the straight conformation, 43 for the 6+1 L-shape, and 10 for the 5+2 L-shape). The KANK1 500-805 complex is described as forming a closed hairpin, but the number of particles analyzed and the resolution of the class averages are not provided. The angle measurements are mentioned, but the distribution and the number of particles (239) are not shown graphically.
- **Why it matters** The NSEM data are the primary experimental evidence for the rod-like structure. If the particle counts are low and the class averages are not shown, it is difficult to assess whether the proposed structures are reliable. The manual picking of particles introduces potential selection bias.
- **Resolution test** Provide representative micrographs, class averages, and the number of particles in each class. Show the distribution of angle measurements. Discuss the resolution limits and potential artifacts of negative staining.

- **Concern ID** R1-M5
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence sufficiency
- **Claim pointer** The authors claim that the worm-like chain model predicts a rms end-to-end distance of approximately 17 nm for L2, with only 0.41% of the ensemble extending beyond 35 nm, and that this is insufficient to span the membrane–microtubule gap
- **Evidence pointer** Results section, worm-like chain calculations, Figure 1d (figure not provided)
- **Concern** The worm-like chain calculation is described in the methods, but the specific parameters used (persistence length, contour length, number of residues) are not fully justified. The authors state that they varied the persistence length between 0.64 and 1 nm and the residue length between 0.34 and 0.38 nm, but the resulting range of predicted distances is not reported. The claim that the rod-like assembly extends to approximately 53 nm is based on the AlphaFold model, not on direct measurement. The relationship between the in vitro rod length and the in-cell gap distance is not established.
- **Why it matters** The paradox that the manuscript aims to resolve depends on the claim that the disordered L2 cannot span the gap on its own. If the worm-like chain calculation is not robust to parameter choices, the paradox may not be as severe as claimed. The proposed resolution, that LC8 binding extends L2 to 53 nm, needs to be validated experimentally.
- **Resolution test** Provide a sensitivity analysis of the worm-like chain calculation to parameter choices. Report the full range of predicted distances. Validate the rod length using an experimental method such as size exclusion chromatography with a calibrated column or dynamic light scattering.

- **Concern ID** R1-M6
- **Severity** Major
- **Blocking** No
- **Axis** Functional significance
- **Claim pointer** The authors claim that LC8 binding to KANK1 is functionally significant for KANK1's role in organizing microtubules at focal adhesions
- **Evidence pointer** Results section, in-cell experiments, Figure 2a (figure not provided)
- **Concern** The in-cell experiments demonstrate colocalization of KANK1 and LC8 at focal adhesion edges and show that KANK1 depletion eliminates LC8 localization. However, the functional consequence of disrupting the KANK1–LC8 interaction is not tested. The authors do not show whether LC8 binding is required for KANK1's ability to recruit KIF21A, regulate microtubule growth, or maintain focal adhesion dynamics. The claim that LC8 acts as a molecular switch to rigidify and extend L2 is not directly tested in cells.
- **Why it matters** The title and abstract emphasize the resolution of a paradox in cellular architecture. Without functional experiments showing that LC8 binding is necessary for KANK1's role in bridging the membrane–microtubule gap, the significance of the structural findings remains correlative.
- **Resolution test** Perform experiments where the LC8 binding sites in KANK1 are mutated or deleted, and assess the effects on KANK1 localization, KIF21A recruitment, microtubule dynamics, and focal adhesion turnover. Alternatively, use a KANK1 construct with a constitutively rigid linker to test whether LC8 binding is required for function.

- **Concern ID** R1-M7
- **Severity** Major
- **Blocking** No
- **Axis** Generalizability
- **Claim pointer** The authors claim that the design principles revealed by this work, namely cooperative multivalency among weak motifs with short linkers, are generalizable to other large protein architectures
- **Evidence pointer** Discussion section
- **Concern** The generalizability claim is speculative and not supported by data from other systems. While the comparison to ASCIZ and Nup159 is informative, the authors do not provide evidence that the principles identified in KANK1 apply more broadly. The claim that this represents a "generalizable strategy" is not tested.
- **Why it matters** The broader significance of the work depends on the generalizability of the design principles. If the mechanism is unique to KANK1, the impact would be more limited.
- **Resolution test** Provide examples of other proteins with similar weak multivalent LC8 binding sites and short linkers, and show that they exhibit similar cooperative behavior. Alternatively, temper the generalizability claims in the discussion.

### Minor Comments
- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Abstract
- **Evidence pointer** Abstract, first sentence
- **Issue** The phrase "Cooperative multivalency converts disorder into rods" is catchy but may be unclear to readers unfamiliar with the system. The abstract would benefit from a brief explanation of what "rods" means in this context.
- **Required correction** Consider rephrasing to "Cooperative multivalency converts a disordered linker into an elongated, rod-like assembly" for clarity.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Results section, KANK1 colocalization
- **Evidence pointer** Results, Figure 2a
- **Concern** The colocalization experiments are described, but the quantification of colocalization is not provided. The statement that LC8 signal "strongly overlaps" with KANK1 is subjective.
- **Required correction** Provide quantitative colocalization analysis, such as Pearson's correlation coefficient or Manders' overlap coefficient, with appropriate controls.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Methodology
- **Affected element** Methods, worm-like chain calculation
- **Evidence pointer** Methods, Worm-like Chain Assessment
- **Issue** The methods state that the proportion of the ensemble above 35 and 50 nm was calculated using Wolfram Alpha, but the specific equation and the integration limits are not fully described.
- **Required correction** Provide the full equation and the integration limits used for the calculation.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Data presentation
- **Affected element** Results, AlphaFold predictions
- **Evidence pointer** Results, Figure 5
- **Concern** The AlphaFold predictions are described as identifying five binding sites with the exclusive threshold and additional sites with the inclusive threshold, but the specific sequences and their locations are not listed in the text.
- **Required correction** Provide a table listing the predicted binding sites, their sequences, and the confidence scores.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Interpretation
- **Affected element** Discussion, comparison to ASCIZ and Nup159
- **Evidence pointer** Discussion, "Conformational and compositional heterogeneity" section
- **Issue** The comparison to ASCIZ and Nup159 is informative, but the authors do not discuss potential differences in the structural context of these proteins. ASCIZ and Nup159 are not membrane-associated adaptors like KANK1, and the functional requirements for rod formation may differ.
- **Required correction** Briefly discuss how the structural context of KANK1, particularly its membrane anchoring, might influence the requirements for rod formation compared to soluble proteins.

- **Concern ID** R1-m6
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Discussion, molecular switch model
- **Evidence pointer** Discussion, "LC8 binding as a molecular switch" section
- **Issue** The term "molecular switch" is used, but the mechanism by which LC8 binding switches KANK1 from a disordered to a rod-like state is not fully explained. The authors mention cooperativity but do not describe the structural basis for the switch.
- **Required correction** Provide a more detailed model for how LC8 binding induces the conformational change, including the role of the short linkers in promoting cooperativity.

- **Concern ID** R1-m7
- **Severity** Minor
- **Axis** Data availability
- **Affected element** Methods, NSEM
- **Evidence pointer** Methods, Negative stain electron microscopy
- **Issue** The methods describe the NSEM procedure, but the number of micrographs collected and the total number of particles picked are not stated.
- **Required correction** Provide the total number of micrographs and particles analyzed for each construct.

## Risk / unsupported claims
- The claim that the KANK1-LC2 rod extends to approximately 53 nm and is sufficient to bridge the 35–50 nm membrane–microtubule gap is based on AlphaFold predictions and in vitro assemblies, not direct in-cell measurements. This claim is not fully supported by the presented evidence.
- The claim that LC8 binding acts as a "molecular switch" that converts KANK1 L2 from a disordered to a rod-like state is inferred from in vitro and computational data, but the in-cell relevance is not directly tested.
- The claim that the design principles revealed by this work are "generalizable" to other large protein architectures is speculative and not supported by data from other systems.
- The claim that KANK1 595-720 binds seven LC8 dimers and KANK1 500-805 binds fifteen LC8 dimers is based on ITC, SEC-MALS, and AUC data that are not fully presented. The stoichiometries should be considered provisional until the raw data are shown.
- The claim that the KANK1-LC8 interaction is unique among the KANK family is based on a single experiment comparing KANK1 and KANK2. The authors do not test KANK3 or KANK4.