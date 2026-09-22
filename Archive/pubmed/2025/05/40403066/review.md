## Review setup
- **Input scope** Full manuscript text including abstract, main text, methods, and supplementary figure/table references
- **Assessment boundary** Scientific validity, methodological soundness, claims versus evidence, and alignment with Nature-style criteria. No line-by-line copyediting or formatting review.
- **Shared manuscript claim summary** The authors present FINCHES, a sequence-based method that repurposes coarse-grained molecular force fields (Mpipi-GG and CALVADOS2) to predict intermolecular interactions involving intrinsically disordered regions (IDRs). The method computes a mean-field interaction parameter (ε) from force field-derived inter-residue potentials, enabling prediction of phase diagrams, identification of interaction hotspots, decomposition of chemically distinct IDR subdomains, and interpretation of experimental binding data. The authors validate against experimental second virial coefficients, phase diagrams, and specific protein systems, and apply the method to proteome-wide analyses of homotypic interactions, phosphorylation effects, and chemical space clustering.
- **Visible evidence base** Main text figures referenced (Figs. 1-5), supplementary figures (figs. S1-S18), supplementary tables (tables S1-S8), methods section, and software availability statements. No raw data, code, or full supplementary material were provided for direct inspection.
- **Missing materials affecting confidence** Supplementary figures and tables referenced in the text were not provided. The full software documentation and code were not inspected. Experimental datasets used for validation (e.g., smFRET data for ProTα-H1, phase diagrams for hnRNPA1 and DDX4) were cited but not included. The Zenodo snapshot and GitHub repositories were not accessed.

## Reviewer

- **Overall assessment** This manuscript presents a conceptually appealing and computationally efficient approach to predicting IDR-mediated intermolecular interactions from sequence alone. The core idea of repurposing force field parameters into a mean-field interaction score is elegant and well-motivated. The validation against experimental data, while qualitative in places, spans multiple systems and environmental conditions, lending credibility to the approach. The proteome-wide applications are thought-provoking and generate testable hypotheses. However, several technical concerns regarding the derivation of the interaction parameter, the treatment of sequence context, and the interpretation of proteome-wide results need to be addressed before the case is fully established. The manuscript is well-written and accessible, with clear figures and a logical flow.

- **Who would be interested in the results, and why** Researchers studying intrinsically disordered proteins, phase separation, and biomolecular condensates will find this directly relevant. The method offers a fast, interpretable alternative to simulation-based approaches for generating hypotheses about IDR interactions. The proteome-wide analyses will interest those working on IDR function, phosphorylation signaling, and protein interaction networks. The software availability and webserver lower the barrier for adoption, making this useful for experimentalists seeking to design mutagenesis experiments or interpret interaction data.

- **Major strengths**
  1. The conceptual advance of repurposing force field physics for high-throughput sequence-based prediction is novel and timely.
  2. The method is fast (>1000 sequences per second) and fully interpretable, addressing a key limitation of machine learning approaches.
  3. Validation spans multiple experimental observables (virial coefficients, phase diagrams, binding affinities) and multiple systems, providing reasonable confidence in the approach.
  4. The proteome-wide applications (chemical space clustering, phosphorylation rewiring) demonstrate the scalability and potential impact of the method.
  5. The software is open source with a webserver, facilitating adoption and reproducibility.

- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness of the interaction parameter derivation
- **Claim pointer** The authors claim that taking the integral under the pairwise potential yields a mean-field interaction parameter analogous to a Mayer-f function, and that this parameter correlates with experimentally measurable second virial coefficients.
- **Evidence pointer** Fig. 1D, Fig. 2A-C, Supplementary Methods (location not provided)
- **Concern** The derivation of ε from the integral of the potential is not fully detailed. The Mayer-f function analogy is invoked but the omission of the volume correction component is not justified. The relationship between ε and the second virial coefficient is asserted to be proportional, but the mathematical connection is not shown. The calibration of the charge prefactor (0.2 for Mpipi-GG, 0.7 for CALVADOS2) is described as "empirical and qualitative," which raises questions about the robustness of the absolute ε values. The authors state that ε values are not expected to offer high-resolution quantitative predictions, but the validation against B2 and A2 values suggests a quantitative relationship that is not fully characterized.
- **Why it matters** The entire method rests on the validity of ε as a meaningful interaction parameter. If the derivation is not rigorous or the calibration is too system-specific, the generalizability of the approach is compromised. The claim of a 1:1 correspondence between predicted and measured salt-dependent B2 values for LAF-1 RGG (Fig. 2C) is strong and needs a clear theoretical basis.
- **Resolution test** Provide a detailed derivation of ε from the force field potentials, including the mathematical relationship to the second virial coefficient. Show explicitly how the volume correction is handled and justify its omission. Perform a sensitivity analysis across a wider range of sequences and conditions to demonstrate that the calibration is not overfit to the validation set.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Validation strength for phase diagram predictions
- **Claim pointer** The authors claim that their approach yields phase diagrams that show "good agreement" with experimental data for hnRNPA1 variants and DDX4 as a function of salt.
- **Evidence pointer** Fig. 3C, 3F-H, fig. S4-S5 (location not provided)
- **Concern** The comparison between predicted and experimental phase diagrams appears qualitative. The authors state that the goal is not to "quantitatively reproduce co-existence curves to match 1:1 with experiments," but the criteria for "good agreement" are not defined. For hnRNPA1, the relative impact of aromatic mutations is captured, but the absolute positions of the coexistence curves are not compared. For DDX4, the salt-dependent shift is reproduced, but the magnitude of the shift is not quantified. The use of T/TC normalization may obscure quantitative discrepancies.
- **Why it matters** Phase diagram prediction is a central claim of the manuscript. If the agreement is only qualitative, the utility of the method for predicting absolute phase behavior is limited. The authors should provide a more rigorous quantitative comparison, such as computing the critical temperature or binodal curves and comparing them to experimental values.
- **Resolution test** Provide a quantitative comparison metric (e.g., root mean square deviation between predicted and experimental binodal curves, or comparison of critical temperatures and concentrations) for at least the hnRNPA1 and DDX4 systems. If quantitative agreement is not expected, state this clearly and justify the qualitative approach.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Interpretation of proteome-wide analyses
- **Claim pointer** The authors claim that hierarchical clustering of IDRs based on ε values reveals "chemically distinct" clusters and that phosphorylation rewires interaction propensities for a substantial fraction of IDRs.
- **Evidence pointer** Fig. 4A-B, Fig. 3K, tables S3-S4 (location not provided)
- **Concern** The biological interpretation of the clustering results is underdeveloped. The authors identify 24 clusters but do not provide a detailed characterization of what distinguishes these clusters in terms of sequence features or biological function. The claim that "some chemistries appear much more promiscuous than others" is interesting but not quantified beyond a ranking. The phosphorylation analysis is based on phosphomimetic mutations (S/T/Y to E), which is a rough approximation, and the authors acknowledge this. The finding that ~57% of IDRs show reduced attraction upon phosphorylation is intriguing, but the functional significance is not explored.
- **Why it matters** The proteome-wide analyses are presented as major applications of the method. Without deeper biological interpretation, these analyses risk being descriptive rather than mechanistic. The clustering results could be validated by comparing to known functional annotations or by experimental testing of a few predictions.
- **Resolution test** Provide a more detailed characterization of the clusters (e.g., enriched sequence features, GO terms, or known functional annotations). For the phosphorylation analysis, discuss the potential biological implications of the rewiring and validate a few predictions experimentally or against published data.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Generalizability to IDR-folded domain interactions
- **Claim pointer** The authors claim that FINCHES can be extended to predict interactions between IDRs and folded domains by averaging over surface residue patches.
- **Evidence pointer** Fig. 5I-J, fig. S15 (location not provided)
- **Concern** The extension to IDR-folded domain interactions is conceptually interesting but the validation is limited. The analysis of GCN4-Gal11 shows overlap with experimentally determined activation domains, but the correlation between predicted interaction strength and AD score (Fig. 5J) is described as "excellent" without a reported correlation coefficient. The authors also note an "apparent paradox" where some IDRs are strongly attractive for Gal11 yet show poor AD scores, which they interpret as off-target interactions. This interpretation is speculative and not directly tested.
- **Why it matters** The ability to predict IDR-folded domain interactions would significantly broaden the applicability of the method. However, the current validation is thin, and the interpretation of the paradox needs experimental support.
- **Resolution test** Report the correlation coefficient and statistical significance for the AD score comparison. Provide experimental evidence (e.g., mutagenesis or binding assays) to support the off-target interaction interpretation.

- **Concern ID** R1-M5
- **Severity** Major
- **Blocking** No
- **Axis** Treatment of sequence context and local environment
- **Claim pointer** The authors state that they account for local charge and hydrophobic context by adjusting interaction parameters based on neighboring residues.
- **Evidence pointer** Methods section, fig. S1 (location not provided)
- **Concern** The local context corrections are described briefly and appear to be heuristic. The charge correction down-weights like-charged regions based on local charge density, and the hydrophobic correction scales up aliphatic interactions based on contiguous runs. The justification for these specific functional forms is not provided, and the sensitivity analysis (fig. S16) only examines the effect of varying the underlying force field parameters, not the context correction parameters.
- **Why it matters** The context corrections are essential for capturing sequence-specific effects beyond simple composition. If these corrections are not well-justified or are too coarse, the method may miss important determinants of IDR interactions.
- **Resolution test** Provide a more detailed derivation and justification of the context corrections. Perform a sensitivity analysis on the context correction parameters and compare predictions with and without these corrections to demonstrate their necessity.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity of figure presentation
- **Affected element** Fig. 1E, Fig. 3D
- **Evidence pointer** Fig. 1E, Fig. 3D
- **Issue** The intermap representations in Fig. 1E and Fig. 3D are visually dense and may be difficult for non-specialists to interpret. The color scale and the meaning of the axes are not immediately clear.
- **Required correction** Add a clear legend explaining the color scale and axis labels for intermaps. Consider providing a simplified schematic of how to read an intermap in the main text or supplementary material.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Statistical reporting
- **Affected element** Fig. 2A-C, Fig. 5J
- **Evidence pointer** Fig. 2A-C, Fig. 5J
- **Issue** Correlation coefficients and p-values are not reported for the comparisons between predicted ε and experimental B2/A2 values, or between predicted interaction strength and AD scores.
- **Required correction** Report correlation coefficients (e.g., Pearson or Spearman) and p-values for all quantitative comparisons.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Terminology consistency
- **Affected element** Throughout
- **Evidence pointer** Throughout
- **Issue** The terms "chemical specificity," "intermolecular interaction," and "interaction fingerprint" are used somewhat interchangeably. The distinction between "chemical specificity" and "sequence-specific" interactions is introduced but could be clarified earlier.
- **Required correction** Define these terms explicitly in the introduction and use them consistently throughout.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Discussion of limitations
- **Affected element** Discussion section
- **Evidence pointer** Discussion section
- **Issue** The limitations of the approach are discussed, but the discussion could be more specific about the types of interactions that are likely to be poorly captured (e.g., interactions involving secondary structure elements, or interactions where precise geometry matters).
- **Required correction** Expand the limitations paragraph to include specific examples of systems or interaction types where FINCHES is likely to fail.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Software availability
- **Affected element** Data and materials availability
- **Evidence pointer** Data and materials availability
- **Issue** The manuscript states that all data and code are deposited on Zenodo and GitHub, but the specific version numbers or commit hashes are not provided.
- **Required correction** Provide specific version identifiers (e.g., Zenodo DOI, GitHub release tag) to ensure reproducibility.

- **Concern ID** R1-m6
- **Severity** Minor
- **Axis** Comparison to existing methods
- **Affected element** Discussion section
- **Evidence pointer** Discussion section
- **Issue** The manuscript mentions machine learning approaches but does not provide a direct comparison of FINCHES to existing predictors of IDR interactions or phase behavior.
- **Required correction** Add a brief comparison to one or two existing methods, highlighting the advantages and disadvantages of each.

## Risk / unsupported claims
- The claim of "1:1 correspondence" between predicted and measured salt-dependent B2 values for LAF-1 RGG (Fig. 2C) is strong and not fully supported by the described analysis.
- The interpretation of the "apparent paradox" in the GCN4-Gal11 analysis (Fig. 5J-K) as off-target interactions is speculative and not directly tested.
- The claim that FINCHES can identify "chemically distinct domains" in IDRs is based on clustering analysis that is not deeply characterized or validated.
- The statement that "~57% of IDRs that undergo phosphorylation showed a reduction in homotypic attractive interaction" is based on phosphomimetic mutations, which are acknowledged as approximations, and the biological significance is not explored.
- The generalizability of the method to IDR-folded domain interactions is not fully established given the limited validation.
- The sensitivity analysis (fig. S16) does not examine the sensitivity to the local context correction parameters, which are a key component of the method.