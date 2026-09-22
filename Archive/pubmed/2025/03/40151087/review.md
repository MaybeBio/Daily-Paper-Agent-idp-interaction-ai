## Review setup
- **Input scope** Full manuscript text (abstract, introduction, results and discussion, conclusions) without supplementary information or figures
- **Assessment boundary** Scientific claims, experimental design logic, interpretation of results, and internal consistency based on the provided text only
- **Shared manuscript claim summary** The authors report that the helix-hairpin-helix (HhH) motif and its duplicated (HhH)2-Fold exhibit functional ambidexterity, defined as the ability to interact with both natural and mirror-image nucleic acids, across the putative evolutionary trajectory from phase-separating peptides to folded dsDNA-binding domains
- **Visible evidence base** CD spectroscopy, phase separation microscopy, SPR binding and dissociation kinetics, mutational analysis, and MD simulations, all described in text but with figures and supplementary data not directly visible
- **Missing materials affecting confidence** All figures, tables, supplementary information, experimental protocols, and raw data are not provided; only the narrative text is available for assessment

## Reviewer
- **Overall assessment** This manuscript presents a conceptually interesting and potentially significant observation regarding the tolerance of an ancient nucleic acid-binding domain to total chiral inversion. The central claim of functional ambidexterity is supported by a multi-pronged experimental approach, but the absence of the actual data figures and supplementary materials prevents full verification of the quantitative claims. The evolutionary interpretation, while thought-provoking, extends beyond what the presented evidence can directly establish. The work is likely to interest the origins-of-life and protein evolution communities, but the strength of the conclusions depends heavily on the quality of the unseen data.
- **Who would be interested in the results, and why** Researchers in origins of life, prebiotic chemistry, protein evolution, and chirality studies would find this work relevant. The demonstration that a primordial nucleic acid-binding motif retains function under chiral inversion has implications for the plausibility of mirror-image biology and for understanding the evolutionary constraints on biomolecular chirality. The biophysical community studying protein-nucleic acid interactions may also be interested in the multi-modal binding behavior described.
- **Major strengths** The conceptual framing of using chiral inversion as a probe for binding mode specificity is elegant and novel. The study spans a plausible evolutionary trajectory from simple peptides to folded domains, which is a valuable approach. The combination of experimental techniques (CD, phase separation, SPR, mutations, MD) provides complementary lines of evidence. The inclusion of a designed negative control (5G mutant) strengthens the argument that binding is not merely electrostatic.
- **Major Concerns**
  - **Concern ID** R1-M1
  - **Severity** Major
  - **Blocking** Yes
  - **Axis** Evidence sufficiency
  - **Claim pointer** The claim that functional ambidexterity is observed for both phase separation of HhH peptides with RNA and binding of the (HhH)2-Fold to dsDNA
  - **Evidence pointer** Figures 2b, 3c-d, described in text; figures not visible
  - **Concern** The central experimental evidence for ambidexterity is presented in figures that are not available for review. The text describes binding curves and coacervation observations, but without seeing the actual data, the magnitude of the effects, the signal-to-noise ratios, and the reproducibility cannot be assessed. The claim that the D-protein binds D-dsDNA with "weaker" affinity than the natural pair is qualitative in the text, and the supporting quantitative data are not visible.
  - **Why it matters** The entire thesis of the paper rests on the demonstration that cross-chiral binding occurs and is not a minor or artifactual effect. Without visual confirmation of the binding curves, coacervation images, and statistical treatment, the core claim cannot be verified.
  - **Resolution test** Provide the actual SPR sensorgrams, coacervation micrographs, and quantitative binding parameters with error bars and replicates. The figures must clearly show that cross-chiral binding is robust and reproducible.
  - **Concern ID** R1-M2
  - **Severity** Major
  - **Blocking** No
  - **Axis** Interpretive overreach
  - **Claim pointer** The statement that "the similarity of several dissociation phases upon chiral inversion may reflect the history of (HhH)2-Fold binding, with the ultimate emergence of a high-affinity binding mode, supported by a bridging metal ion, depopulating but not displacing more primitive (potentially ambidextrous) modes"
  - **Evidence pointer** Dissociation kinetics section, Figures S21-S22
  - **Concern** The evolutionary narrative proposed in this claim is highly speculative. The observation that multiple dissociation phases exist and that some are shared between chiral pairs does not directly establish a temporal sequence of binding mode evolution. The interpretation that low-affinity modes are "primitive" and the high-affinity mode is "derived" is an inference that goes beyond the kinetic data.
  - **Why it matters** The paper's broader significance is tied to this evolutionary interpretation. If the claim is presented as a conclusion rather than a hypothesis, it overstates what kinetic data can reveal about evolutionary history.
  - **Resolution test** Reframe this interpretation as a hypothesis or speculation, clearly separated from the direct experimental findings. Alternatively, provide additional evidence, such as phylogenetic analysis of binding mode conservation or ancestral reconstruction experiments, to support the evolutionary narrative.
  - **Concern ID** R1-M3
  - **Severity** Major
  - **Blocking** No
  - **Axis** Technical validation
  - **Claim pointer** The claim that MD simulations reveal "an overlap between the binding modes adopted by the natural and mirror-image proteins to natural dsDNA"
  - **Evidence pointer** Figure 4, described in text
  - **Concern** The MD simulations are described as showing that the D-protein adopts multiple binding modes with the PGIGP motifs shifting approximately 90 degrees along the DNA axis. However, the text does not specify the force field validation, the simulation convergence criteria, or whether the simulations were performed with sufficient sampling to draw robust conclusions about binding mode distributions. The claim of "overlap" between binding modes is not quantitatively defined.
  - **Why it matters** MD simulations are only as reliable as their sampling and validation. If the simulations are not converged or the force field is not appropriate for mirror-image systems, the conclusions about binding mode overlap could be artifacts.
  - **Resolution test** Provide convergence metrics, replicate simulations, and a quantitative definition of binding mode overlap. Clarify whether the force field parameters for D-amino acids were validated.
- **Minor Comments**
  - **Concern ID** R1-m1
  - **Severity** Minor
  - **Axis** Clarity
  - **Affected element** Definition of ambidexterity
  - **Evidence pointer** Abstract and Introduction
  - **Issue** The term "functional ambidexterity" is used throughout but is only implicitly defined. The distinction between ambidexterity (binding both chiral forms) and simple non-specificity (binding anything) is not crisply articulated.
  - **Required correction** Provide an explicit operational definition of functional ambidexterity early in the manuscript, distinguishing it from general non-specific binding.
  - **Concern ID** R1-m2
  - **Severity** Minor
  - **Axis** Quantitative reporting
  - **Affected element** Binding affinity comparisons
  - **Evidence pointer** Figure 3d, described in text
  - **Issue** The text states that the D-protein binds D-dsDNA with "weaker" affinity and that the Ancestor variant shows an "even smaller difference in affinity," but no numerical values are given in the text.
  - **Required correction** Report quantitative affinity values or relative binding levels in the text, not only in figures, so the magnitude of the chiral preference is clear.
  - **Concern ID** R1-m3
  - **Severity** Minor
  - **Axis** Reproducibility
  - **Affected element** MST experiments
  - **Evidence pointer** Figure S24, described in text
  - **Issue** The text notes that MST experiments were "concentration-limited due to significant changes in initial fluorescence at high concentrations of DNA," which suggests technical difficulties that may limit the reliability of those measurements.
  - **Required correction** Clarify whether the MST data are considered confirmatory or exploratory, and describe how the fluorescence artifacts were addressed.
  - **Concern ID** R1-m4
  - **Severity** Minor
  - **Axis** Completeness
  - **Affected element** Negative control
  - **Evidence pointer** Figure 3e, described in text
  - **Issue** The 5G mutant is described as binding with "drastically lower affinity," but the text does not specify whether this mutant was tested for both chiral pairs or only the natural pair.
  - **Required correction** State explicitly whether the 5G mutant was tested against both D- and L-dsDNA, and report the results for both.
- **Technical failings that need to be addressed before the case is established** The primary technical failing is the inaccessibility of the actual data figures and supplementary materials, which prevents verification of the central claims. Additionally, the MD simulation validation is not described in sufficient detail, and the evolutionary interpretation is presented with more certainty than the data can support.

## Risk / unsupported claims
- The claim that ambidextrous binding modes "may reflect the history of (HhH)2-Fold binding" is an unsupported evolutionary inference from kinetic data.
- The claim that "the veil between worlds with alternative chiral preferences may not be as impenetrable as is often assumed" is a broad generalization that extends beyond the specific system studied.
- The assertion that low-affinity binding modes are "potentially ambidextrous" and represent "a more primitive or ancestral mode of binding" is speculative and not directly testable from the presented data.
- The quantitative comparison of binding affinities between chiral pairs is not verifiable without the actual figure data.
- The MD simulation claim of binding mode overlap is not quantitatively defined and cannot be assessed without convergence and validation details.

## Assessment against Nature-style criteria
- **Originality** High. The use of total chiral inversion as a systematic probe of binding mode evolution in an ancient nucleic acid-binding domain is a novel approach that has not been previously reported for this system.
- **Scientific importance** Moderate to high. The findings bear on questions of homochirality, the plausibility of mirror-image biology, and the evolutionary constraints on protein-nucleic acid interactions. However, the broader significance depends on whether the ambidexterity observed here is generalizable to other domain families, which is not established.
- **Interdisciplinary readership** Moderate. The work bridges protein evolution, nucleic acid biochemistry, and origins-of-life research, but the technical nature of the biophysical methods may limit accessibility to a broader readership.
- **Technical soundness** Cannot be fully assessed from the text alone. The experimental design is logical and includes appropriate controls, but the actual data quality, statistical treatment, and simulation validation cannot be verified without the figures and supplementary materials.
- **Readability for nonspecialists** Adequate. The manuscript is clearly written and the conceptual framing is accessible, though some sections assume familiarity with biophysical terminology and methods.

## Recommendation posture
Supportive if technical concerns are resolved. The conceptual framework and experimental approach are promising, and the findings, if the data are as described, would constitute a significant contribution. However, the current manuscript cannot be fully evaluated without access to the figures and supplementary materials, and the evolutionary interpretation should be tempered to match the direct evidence.