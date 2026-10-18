## Review setup
- **Input scope** Full manuscript text including abstract, introduction, results, discussion, methods, and supplementary figure legends as provided.
- **Assessment boundary** Scientific and technical evaluation of the claims, methodology, and evidence presented. Editorial and stylistic considerations are noted only where they affect scientific clarity.
- **Shared manuscript claim summary** The authors present ExVivo PhaseScan, a droplet microfluidics platform combining mammalian lysate-based reconstitution with high-throughput imaging and machine learning to generate high-resolution, multidimensional phase diagrams of near-physiological protein condensates. They apply this to stress granules and nucleoli, dissect physicochemical drivers of condensation, and show that ALS-linked FUS mutations promote aggregate formation that can be reversed by a GUG RNA aptamer.
- **Visible evidence base** Main text figures 1–4, supplementary figures 1–8 (referenced), methods sections 1–11, dominance analysis derivation, machine learning classifier performance metrics, FRAP data, and compositional analyses (RNA-seq, proteomics, TLC).
- **Missing materials affecting confidence** Supplementary figures and supplementary text are referenced but not provided in full. Raw imaging data, classifier training details, and full proteomics/RNA-seq datasets are not available for independent assessment. Statistical details for some comparisons are only stated as "in figure legends" without full legend text.

## Reviewer
- **Overall assessment** This manuscript describes a technically ambitious platform that addresses a genuine gap in the condensate field: the need for quantitative phase behaviour measurements in compositionally complex, near-native environments. The combination of lysate-based reconstitution with droplet microfluidics is conceptually appealing and the application to disease-relevant FUS mutants is timely. However, the manuscript currently overclaims several aspects, particularly regarding the "near-physiological" nature of the system, the mechanistic interpretation of the dominance analysis, and the generalisability of the machine learning classifier. Several technical details require clarification or additional controls before the central claims can be considered fully established.
- **Who would be interested in the results, and why** Researchers studying biomolecular condensates, phase separation, and membraneless organelles would be the primary audience. The platform will also interest those working on ALS and other neurodegenerative diseases linked to aberrant phase transitions, as well as groups developing high-throughput screening approaches for condensate-modulating therapeutics. The methodological advance may appeal to the microfluidics and assay development community.
- **Major strengths**
  1. The platform addresses a real limitation of current approaches by combining lysate complexity with microfluidic precision and throughput.
  2. The multidimensional phase diagrams represent a significant technical achievement, with large numbers of droplets sampled per condition.
  3. The application to two distinct condensate systems (stress granules and nucleoli) demonstrates versatility.
  4. The machine learning classifier for morphological classification is a useful addition, with reported F1 scores of 97–98%.
  5. The demonstration of aptamer-mediated reversal of mutant FUS aggregation is potentially impactful.
- **Major Concerns**
  - **Concern ID** R1-M1
  - **Severity** Major
  - **Blocking** Yes
  - **Axis** Claim vs evidence
  - **Claim pointer** The authors state that ExVivo PhaseScan enables study of condensates "under near-physiological conditions" and that lysate-based condensates "closely resemble their endogenous counterparts."
  - **Evidence pointer** Abstract; Introduction; Results section "Generation of high-resolution phase diagrams"; Supplementary Fig. 1
  - **Concern** The "near-physiological" claim is not quantitatively supported. The system uses diluted lysate (0.1–8 mg/mL total protein), which is substantially below intracellular protein concentrations (typically 100–300 mg/mL). The authors acknowledge that lysate concentration is a dilution series of total retained components, but the implications for physiological relevance are not discussed. The comparison to endogenous condensates relies on prior work from the Taylor lab, but no direct compositional or biophysical comparison is made here between lysate-reconstituted condensates and cellular condensates under the specific conditions used.
  - **Why it matters** The central selling point of the platform is its physiological relevance relative to recombinant systems. If the lysate dilution fundamentally alters condensate composition or properties, the conclusions drawn about disease-relevant behaviour may not translate to cells. The claim as stated is broader than the evidence provided.
  - **Resolution test** Provide quantitative comparison of condensate composition (e.g., proteomics of isolated condensates) between lysate-reconstituted and cellular condensates. Alternatively, temper the claim to "lysate-based" rather than "near-physiological" and discuss the limitations of dilution explicitly.
  - **Concern ID** R1-M2
  - **Severity** Major
  - **Blocking** Yes
  - **Axis** Technical soundness
  - **Claim pointer** The dominance analysis is used to "partition the relative energetic contributions of different components to condensation" and to conclude that RNA dissolution is "mediated through a reduction in the energetic contributions from non-scaffold interactions."
  - **Evidence pointer** Results section "Poly(A) RNA tunes stress granule condensation in a biphasic manner"; Methods section "Dominance analysis"; Supplementary Fig. 3
  - **Concern** The dominance analysis derivation contains a potential unit inconsistency. The authors define α as the ratio of recombinant to tagged protein in both dilute and dense phases, but the derivation leading to Equation 7 assumes α ≫ 1 and a specific relationship between dilute phase concentrations that is not fully justified. The claim that the slope of a scatter plot of recombinant protein concentration (µM) versus lysate concentration (mg/mL) yields a "dominance" value requires more careful explanation of how the unit mismatch is resolved. The derivation appears to conflate total protein concentration in lysate with tagged scaffold concentration.
  - **Why it matters** The mechanistic conclusions about which interactions dominate condensation rest entirely on this analysis. If the derivation is flawed or the assumptions not met, the conclusions about RNA acting via non-scaffold interactions are unsupported.
  - **Resolution test** Provide a clearer derivation with all assumptions stated, validate the approach on a system with known interaction stoichiometry, or present independent biochemical evidence (e.g., competition experiments, mutant scaffolds) supporting the mechanistic interpretation.
  - **Concern ID** R1-M3
  - **Severity** Major
  - **Blocking** Yes
  - **Axis** Technical soundness
  - **Claim pointer** The machine learning classifier is described as distinguishing "homogeneous, condensate-, and aggregate-containing" droplets with high accuracy, and this classification is used to define phase boundaries including aggregate regions.
  - **Evidence pointer** Results section "ALS-linked FUS mutations remodel condensate phase behaviour"; Methods section "Machine Learning-assisted droplet classification"; Supplementary Figs. 7–8
  - **Concern** The classifier was trained on manually assigned categories from the same experimental platform. The authors report F1 scores of 97–98% on held-out test sets, but the critical question is whether the classifier distinguishes aggregates from condensates based on morphology or based on intensity or size artefacts. The authors state they validated against "class-specific information leakage" (Supplementary Fig. 8a), but the details of this validation are not provided in the main text. Additionally, the classifier was trained on data from specific lysate and scaffold combinations; its generalisability to new conditions is asserted but not demonstrated.
  - **Why it matters** The identification of aggregate regions in the phase diagrams is a key finding, particularly for the FUS mutant analysis. If the classifier confounds intensity with morphology, the phase boundaries and the conclusion that mutants promote aggregation could be artefacts of labelling or imaging conditions.
  - **Resolution test** Show representative images from each class with corresponding intensity distributions, demonstrate that classification is invariant to overall intensity scaling, and test the classifier on an independent dataset with different lysate preparations or imaging settings.
  - **Concern ID** R1-M4
  - **Severity** Major
  - **Blocking** No
  - **Axis** Scientific importance
  - **Claim pointer** The authors state that the GUG RNA aptamer "collapsed the aggregated region for R522G and restored a condensate-only landscape" and suggest this as a potential therapeutic strategy.
  - **Evidence pointer** Results section "ALS-linked FUS mutations remodel condensate phase behaviour"; Fig. 4e, h
  - **Concern** The aptamer experiments are performed only in the lysate-based system. No cellular validation is provided. The authors acknowledge that cellular validation is needed, but the claim of "restoring healthy condensate behaviour" is premature. Additionally, the mechanism by which the aptamer acts is not directly tested; the authors infer it biases interactions toward reversible states, but no binding or competition data are shown.
  - **Why it matters** The therapeutic implication is a significant part of the paper's broader impact. Without cellular or in vivo validation, the translational relevance is speculative.
  - **Resolution test** Add cellular experiments showing aptamer effects on stress granule or nucleolar phenotypes in FUS mutant cell lines. Alternatively, temper the claim to "in vitro reversal" and discuss the limitations.
- **Minor Comments**
  - **Concern ID** R1-m1
  - **Severity** Minor
  - **Axis** Clarity
  - **Affected element** Methods section "Dominance analysis"
  - **Evidence pointer** Methods section "Dominance analysis"
  - **Issue** The derivation of the dominance parameter is difficult to follow. The notation switches between D_app and D without clear definition, and the physical meaning of "dominance" is not intuitively explained.
  - **Required correction** Provide a plain-language explanation of what dominance measures and why the slope of the scatter plot relates to it. Consider adding a schematic figure.
  - **Concern ID** R1-m2
  - **Severity** Minor
  - **Axis** Reproducibility
  - **Affected element** Methods section "Machine Learning-assisted droplet classification"
  - **Evidence pointer** Methods section "Machine Learning-assisted droplet classification"
  - **Issue** The number of training images per class, the distribution of classes in the training set, and the criteria for manual annotation are not specified.
  - **Required correction** Report the dataset size, class balance, and annotation criteria. Provide the code and trained model weights for reproducibility.
  - **Concern ID** R1-m3
  - **Severity** Minor
  - **Axis** Statistical rigour
  - **Affected element** Fig. 3c
  - **Evidence pointer** Fig. 3c
  - **Issue** The quantification of client fluorescence intensity per condensate area is presented with p-values, but the number of condensates analysed, the number of independent experiments, and the statistical test used are only stated as "in figure legends" without the full legend text.
  - **Required correction** Include the full statistical details in the main text or ensure the figure legends are complete.
  - **Concern ID** R1-m4
  - **Severity** Minor
  - **Axis** Completeness
  - **Affected element** Methods section "Lysate generation"
  - **Evidence pointer** Methods section "Lysate generation"
  - **Issue** The lysis buffer contains NP-40, a non-ionic detergent. The authors state that detergent did not influence phase behaviour (Supplementary Fig. 2j), but the concentration of NP-40 in the final droplet is not reported.
  - **Required correction** Report the final NP-40 concentration in droplets and discuss any potential effects on weak hydrophobic interactions, given that 1,6-hexanediol is used to probe hydrophobic interactions.
  - **Concern ID** R1-m5
  - **Severity** Minor
  - **Axis** Interpretation
  - **Affected element** Results section "Poly(A) RNA tunes stress granule condensation in a biphasic manner"
  - **Evidence pointer** Fig. 2b–d
  - **Concern** The biphasic response to RNA is described as "likely" due to multivalent crosslinking at low concentrations and charge repulsion at high concentrations. This interpretation is plausible but not directly tested.
  - **Required correction** Consider adding experiments with RNA of different lengths or valency to support the mechanistic interpretation, or explicitly state that the mechanism is inferred.
- **Technical failings that need to be addressed before the case is established**
  1. The dominance analysis derivation requires clarification and validation (R1-M2).
  2. The "near-physiological" claim needs quantitative support or tempering (R1-M1).
  3. The machine learning classifier requires more rigorous validation of morphology-based classification (R1-M3).
  4. The aptamer reversal claim needs cellular validation or tempering (R1-M4).
- **Assessment against Nature-style criteria**
  - **Originality** The combination of lysate-based reconstitution with droplet microfluidics for multidimensional phase diagram generation is novel. Previous work has used microfluidics for recombinant condensate systems, and lysate-based condensate reconstitution has been demonstrated, but the integration into a high-throughput platform with machine learning analysis is a new contribution.
  - **Scientific importance** The platform addresses a real need in the condensate field. The ability to map phase behaviour in compositionally complex environments with high resolution could accelerate both fundamental understanding and therapeutic screening. The FUS mutant findings are potentially important but require additional validation.
  - **Interdisciplinary readership** The work bridges biophysics, cell biology, microfluidics, and machine learning. The findings on condensate phase behaviour and FUS mutations will interest a broad readership, though the technical complexity may limit accessibility.
  - **Technical soundness** The microfluidics and imaging appear technically sound, but the dominance analysis and machine learning validation have gaps as noted above. The compositional analyses are described but not fully presented.
  - **Readability for nonspecialists** The manuscript is generally well-written but the dominance analysis section is dense and would benefit from clearer explanation. The figures are informative but some panels are complex.
- **Recommendation posture** Supportive if technical concerns are resolved. The platform is a genuine advance and the findings are potentially significant, but the current evidence does not fully support all claims. The dominance analysis needs clarification or validation, the "near-physiological" claim needs tempering or additional evidence, and the machine learning classifier requires more rigorous validation. The aptamer reversal finding is intriguing but needs cellular confirmation.

## Risk / unsupported claims
- The claim that condensates are studied "under near-physiological conditions" is not quantitatively supported given the substantial dilution of lysate.
- The mechanistic conclusion that RNA dissolution acts via non-scaffold interactions rests on a dominance analysis whose derivation is not fully transparent.
- The claim that the GUG aptamer "restores healthy condensate behaviour" is not supported by cellular or in vivo data.
- The assertion that the machine learning classifier is generalisable beyond the specific training conditions is not demonstrated.
- The statement that lysate-reconstituted condensates "closely resemble their endogenous counterparts" relies on prior work and is not directly tested here.