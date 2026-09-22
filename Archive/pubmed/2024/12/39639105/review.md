## Review setup
- **Input scope** Full manuscript text including abstract, introduction, results, discussion, materials and methods, figure legends, and supplementary information descriptions.
- **Assessment boundary** Scientific content, technical soundness, logical coherence, and support of claims by presented evidence. No assessment of editorial fit or publication decision.
- **Shared manuscript claim summary** The authors propose that remorin proteins, prior to membrane association, adopt a pre-structured conformation in the cytosol. This pre-structuration involves dimeric antiparallel coiled-coil domains with a conserved symmetric hydrophobic interface, a positively charged surface "barcode," and a pre-folded C-terminal membrane anchor containing a flexible kink. This architecture is proposed to serve as a selective platform for lipid nanodomain targeting.
- **Visible evidence base** Dual-color TIRF microscopy of full-length and truncated remorins in Nicotiana benthamiana; NMR spectroscopy of ten remorin C-terminal anchor peptides; NMR-based structure calculations for three StREM1.3 constructs; AlphaFold2 multimer predictions; atomistic molecular dynamics simulations using AMBER and AMOEBA force fields; contact map analysis; GUV binding assays.
- **Missing materials affecting confidence** Supplementary Data files 1–4 and Supplementary Videos are referenced but not provided. These include NMR restraint lists, structural homology search results, Coconat prediction outputs, and simulation trajectories. Without these, the depth of validation for several structural claims cannot be fully assessed.

## Reviewer
- **Overall assessment** This manuscript presents a comprehensive and technically ambitious study combining experimental and computational approaches to address a significant question in plant membrane biology: how remorin proteins achieve selective nanodomain targeting. The combination of NMR, MD simulations, and in vivo imaging is commendable and largely appropriate for the questions posed. The central claim of a pre-structured dimeric coiled-coil architecture with a tunable fuzzy coat is interesting and potentially impactful. However, the manuscript has several weaknesses that currently limit the strength of the conclusions. The evidence for the functional relevance of the proposed "charge barcode" is largely correlative and speculative. The statistical treatment of the imaging data is underpowered and lacks methodological detail. The MD simulations, while extensive, are not sufficiently validated against experimental observables beyond qualitative secondary structure comparisons. The manuscript would be substantially strengthened by direct experimental testing of the proposed mechanism, such as mutagenesis of the identified barcode residues coupled with functional assays, and by a more rigorous quantitative analysis of the imaging data.
- **Who would be interested in the results, and why** Researchers in plant membrane biology, specifically those studying nanodomain organization, lipid-protein interactions, and remorin function. The work may also interest a broader audience in structural biology and biophysics, particularly those using integrative approaches combining NMR and MD simulations to study intrinsically disordered proteins and membrane-interacting proteins. The proposed concept of a "pre-structuration" mechanism for membrane targeting could have general relevance beyond the remorin family.
- **Major strengths**
  1. The study addresses a fundamental and timely question in plant biology: the molecular basis for selective nanodomain targeting by remorins.
  2. The methodological approach is highly integrative, combining in vivo imaging, solution NMR, structure calculations, and advanced MD simulations. This multi-pronged strategy is appropriate for the complexity of the problem.
  3. The identification of a conserved symmetric hydrophobic interface in the coiled-coil dimer, centered on a specific residue (L137 in StREM1.3), provides a concrete and testable molecular model.
  4. The use of a polarizable force field (AMOEBA) for MD simulations is a notable strength, as it is more physically realistic for systems with significant polar and charged residues.
  5. The manuscript is generally well-written and logically organized, with a clear narrative from observation to structural model.
- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Experimental support for functional claims
- **Claim pointer** The manuscript claims that the "charge barcode" on the coiled-coil surface and the pre-structuration of the C-terminal anchor provide a "selective platform for phospholipid binding" and guide nanodomain segregation.
- **Evidence pointer** Figure 4e, Discussion section
- **Concern** The central functional claim linking the proposed structural features (charge barcode, pre-structured anchor) to selective lipid binding and nanodomain segregation is not directly tested. The evidence presented is largely correlative: the structures are predicted or determined in solution, and the imaging shows that the C-terminal region is sufficient for exclusion. However, no experiment directly demonstrates that the specific charged residues identified in the barcode are required for lipid selectivity or nanodomain targeting. The GUV experiments (Figure 4c) only show binding versus no binding for wild-type and a triple mutant that disrupts the coiled-coil, not a selective interaction with specific lipids.
- **Why it matters** Without direct experimental testing, the proposed mechanism remains a structural hypothesis. The manuscript's title and abstract imply a functional role for the pre-structuration, but the data do not establish causality. This is a critical gap that prevents the paper from making a definitive contribution to the field.
- **Resolution test** The authors should perform mutagenesis experiments targeting the positively charged residues in the barcode region and test the effects on (1) lipid binding specificity in vitro using GUVs with defined lipid compositions, and (2) nanodomain localization and segregation in vivo. Alternatively, they could use cross-linking or other approaches to demonstrate that the pre-structured dimer is the functional unit that interacts with specific lipids.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Statistical rigor and reproducibility of imaging data
- **Claim pointer** The manuscript states that full-length remorins from the same group co-localize while those from different groups segregate, and that truncation alters clustering behavior.
- **Evidence pointer** Figure 1a, Figure 4a, "Statistics and reproducibility" section
- **Concern** The quantitative analysis of the TIRF microscopy data is insufficiently described. The methods state that "at least 23 cells were analyzed" and that a Kruskal-Wallis test was used, but the exact metric being compared (Pearson's coefficient) is only mentioned in the figure legend. There is no description of how regions of interest were selected, how background was subtracted, or how the Pearson's coefficient was calculated (e.g., Costes automatic thresholding is mentioned but not detailed). The representative images shown are qualitative, and the statistical comparison appears to be only between the co-localization coefficients, not a rigorous test of segregation.
- **Why it matters** The imaging data are a key piece of evidence for the functional relevance of the C-terminal region in nanodomain segregation. If the statistical analysis is not robust and reproducible, the conclusions drawn from these experiments are weakened. The field requires rigorous quantitative imaging analysis to support claims about protein co-localization and segregation.
- **Resolution test** The authors should provide a detailed description of the image analysis pipeline, including specific software, parameters, and thresholds used. They should report the effect sizes and confidence intervals for the Pearson's coefficients, not just p-values. Ideally, they should also provide a complementary analysis method, such as nearest-neighbor distance analysis or pair-correlation functions, to strengthen the claim of segregation.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Validation of computational predictions
- **Claim pointer** The manuscript claims that AlphaFold2 predicts antiparallel coiled-coil dimers with high confidence and that MD simulations confirm the stability of these dimers and the pre-structuration of the C-terminal anchor.
- **Evidence pointer** Figures 4d, 5, 6; Supplementary Figures 2, 4, 8, 9
- **Concern** While the use of AlphaFold2 and MD simulations is appropriate, the validation of these predictions is limited. The AF2 predictions are presented as structural models, but there is no experimental validation of the dimeric arrangement (e.g., via cross-linking mass spectrometry, analytical ultracentrifugation, or mutagenesis combined with biophysical characterization). The MD simulations are compared to NMR-derived secondary structure propensities, but the agreement is qualitative. The manuscript does not report quantitative metrics of simulation convergence or validation against experimental observables such as NMR residual dipolar couplings or paramagnetic relaxation enhancements.
- **Why it matters** The structural model of the dimeric coiled-coil is central to the paper's thesis. If the computational predictions are not rigorously validated, the structural conclusions remain speculative. The field increasingly expects that computational models be supported by experimental evidence, especially when they form the basis for functional hypotheses.
- **Resolution test** The authors should provide additional experimental validation of the dimeric structure, such as site-directed spin labeling EPR, cross-linking, or mutagenesis of the interface residues followed by biophysical characterization (e.g., SEC-MALS, AUC). For the MD simulations, they should report quantitative comparisons to NMR data and demonstrate convergence of the simulations.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Generalizability of the proposed model
- **Claim pointer** The manuscript proposes a "conserved" pre-structuration mechanism across the remorin family, based on the analysis of ten C-terminal anchor peptides and AF2 predictions for selected family members.
- **Evidence pointer** Figures 1, 2, 4, 5
- **Concern** The study focuses on a limited number of remorin representatives, with a strong emphasis on StREM1.3. While the authors show sequence conservation of certain motifs, the functional and structural diversity within the six remorin groups is not systematically explored. The claim of a "conserved" mechanism may be an overgeneralization given the limited sampling. The differences in dynamics and structure between the groups, which the authors acknowledge, may be functionally significant and undermine the idea of a single conserved pre-structuration mechanism.
- **Why it matters** The title and abstract suggest a general principle for remorin function. If the mechanism is not truly conserved across the family, the impact of the work is reduced. A more nuanced interpretation that acknowledges group-specific variations would be more accurate and useful.
- **Resolution test** The authors should either expand their analysis to include a more comprehensive set of remorin representatives, or temper their claims of conservation and explicitly discuss the potential functional implications of the observed group-specific differences.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity of presentation
- **Affected element** Figure 2b
- **Evidence pointer** Figure 2b
- **Issue** The figure compares secondary structure propensities from MD simulations, AF2 predictions, CcpNMR analysis, and CNS calculations, but the color code and layout are complex and difficult to interpret at a glance.
- **Required correction** The authors should simplify the figure, possibly by separating the different data sources into distinct panels or using a clearer schematic representation. A more detailed legend explaining how to read the figure would also be helpful.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Methodological detail
- **Affected element** Materials and Methods, "Molecular dynamics simulation using the polarizable force field AMOEBA and adaptive sampling"
- **Evidence pointer** Materials and Methods section
- **Issue** The description of the adaptive sampling procedure is dense and somewhat difficult to follow. The number of seeds used for each round is given in Table 4, but the criteria for choosing the number of seeds and the convergence criteria for the adaptive sampling are not clearly stated.
- **Required correction** The authors should expand the methods description to clarify the adaptive sampling protocol, including how convergence was assessed and why the specific number of seeds was chosen.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Interpretation of results
- **Affected element** Discussion section
- **Evidence pointer** Discussion section
- **Issue** The discussion of the "fuzzy coat" and its potential role in membrane interactions is somewhat speculative and could be more tightly linked to the data presented.
- **Required correction** The authors should either provide more direct evidence for the fuzzy coat model or clearly frame this as a hypothesis that requires further testing.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Data availability
- **Affected element** Supplementary Data files
- **Evidence pointer** Supplementary Data 1-4
- **Issue** The supplementary data files are referenced but not provided for review. This limits the ability to fully assess the NMR restraints, structural homology results, and simulation details.
- **Required correction** The authors should ensure that all supplementary data files are made available for review and publication.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Nomenclature
- **Affected element** Throughout
- **Evidence pointer** Throughout
- **Issue** The term "pre-structuration" is used throughout, but its precise definition, particularly in the context of intrinsically disordered proteins, could be clarified.
- **Required correction** The authors should provide a clear definition of what they mean by "pre-structuration" and how it differs from other terms such as "pre-formed structural elements" or "conformational pre-sampling."

## Risk / unsupported claims
- The claim that the "charge barcode" provides a "selective platform for phospholipid binding" is not directly supported by experimental data. No experiment demonstrates that the specific charged residues are required for lipid selectivity.
- The claim that the pre-structuration mechanism is "conserved" across the remorin family is an overgeneralization based on a limited number of representatives and may not hold for all six groups.
- The functional significance of the observed differences in dynamics and structure between remorin groups is not explored, and the claim that these differences are functionally relevant is speculative.
- The claim that the C-terminal region alone is "sufficient for REM nanodomain exclusion" is based on imaging data that lack rigorous statistical validation and detailed methodological description.
- The structural model of the dimeric coiled-coil, while supported by AF2 predictions and MD simulations, lacks direct experimental validation. The claim that this dimer is the functional unit for membrane targeting is therefore not fully established.
- The relevance of the in vitro GUV experiments to the in vivo situation is not fully discussed. The lipid composition of the GUVs is simplified, and the physiological relevance of the observed binding is not demonstrated.