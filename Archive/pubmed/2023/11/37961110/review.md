## Review setup
- **Input scope** Full manuscript text (abstract, introduction, results, methods, discussion sections as provided)
- **Assessment boundary** Scientific validity, methodological soundness, claims versus evidence, and suitability for a high-impact general journal
- **Shared manuscript claim summary** The authors present a computational algorithm based on MCMC sampling and CALVADOS coarse-grained simulations to design intrinsically disordered protein variants with specified conformational properties, particularly chain compaction, while keeping amino acid composition fixed. They validate predictions experimentally for five variants of the hnRNPA1 low-complexity domain, measuring both chain dimensions and phase separation propensity, and report good agreement between computation and experiment.
- **Visible evidence base** Computational design results for four IDPs (αSyn, A1-LCD, FUS-PLD, LAF-1-RGG); sequence feature analyses (charge patterning, k parameter, z(δ+−) scores); multi-chain slab simulations for phase separation; experimental characterization of five A1-LCD variants including DIC microscopy, SAXS, and DOSY NMR; comparison with human IDRome predictions
- **Missing materials affecting confidence** Figures and supplementary figures referenced but not provided; detailed experimental protocols for protein expression and purification not included; raw SAXS curves and fitting details referenced but not shown; specific sequence identities of designed variants not listed; statistical details of experimental replicates partially provided but incomplete

## Reviewer
- **Overall assessment** This manuscript describes a potentially valuable computational approach for designing intrinsically disordered proteins with tunable conformational properties. The core idea, using MCMC sampling coupled to efficient coarse-grained simulations with alchemical free energy calculations, is sensible and the demonstration of composition-preserving sequence redesign is technically interesting. The experimental validation, while limited to five variants of one protein, provides encouraging support for the computational predictions. However, several concerns limit the strength of the claims as currently presented. The experimental validation set is small, the discrepancy for one variant (V5) is not fully explained, and the generality of the approach beyond chain compaction remains to be demonstrated. The manuscript would benefit from clearer presentation of the algorithm's performance characteristics and a more critical discussion of its limitations.
- **Who would be interested in the results, and why** Researchers in the fields of intrinsically disordered proteins, protein design, and biomolecular condensates would find this work of interest. The demonstration that sequence patterning, particularly charge segregation, can be exploited to modulate both single-chain dimensions and phase separation propensity has implications for understanding sequence-ensemble-function relationships in IDPs. The computational approach may also appeal to those developing protein design tools, as it extends design capabilities to disordered proteins, which are typically excluded from structure-based design pipelines. The potential applications in designing linkers, signaling molecules, or biomaterials could attract a broader biotechnology audience.
- **Major strengths** 1) The computational algorithm is well conceived, combining MCMC sequence sampling with efficient coarse-grained simulations and alchemical free energy calculations to make the design process tractable. 2) The restriction to fixed amino acid composition is a clever experimental design choice that isolates the effects of sequence patterning from composition effects. 3) The experimental validation, while limited, uses complementary techniques (DIC microscopy, SAXS, DOSY NMR) to assess both phase separation and chain dimensions. 4) The analysis of sequence determinants, particularly the role of charge patterning, connects the design results to established biophysical principles. 5) The placement of designed variants in the context of the human IDRome provides useful perspective on how designed sequences relate to natural sequence space.
- **Major Concerns**
- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Experimental validation scope
- **Claim pointer** The authors claim "good agreement between the experiments and predictions" for the designed A1-LCD variants, and use this to support the broader claim that their algorithm can design IDPs with specified conformational properties.
- **Evidence pointer** Results section "Experimental characterization of A1-LCD variants"; Figures 5c and 5d (referenced but not shown)
- **Concern** The experimental validation is limited to five variants of a single protein (A1-LCD). While the correlation between predicted and measured csat values is reported as high, the sample size is small. More importantly, one of the five variants (V5) is described as an outlier whose experimental csat is lower than predicted, and the authors state the origin of this discrepancy is unclear. This is concerning because V5 is the only variant predicted to be more expanded than wild type, meaning the validation is effectively strongest for the compaction direction. The authors do not provide sufficient analysis of why V5 fails, nor do they test whether the discrepancy reflects a systematic limitation of the model for expanded sequences.
- **Why it matters** The claim of experimental validation underpins the broader assertion that the algorithm can reliably design IDPs with specified properties. If the model systematically fails for expanded sequences, this would substantially limit the generality of the approach. The small number of validated variants also means that the observed correlation could be influenced by a few data points.
- **Resolution test** The authors should either expand the experimental validation to include more variants, particularly those predicted to be more expanded, or provide a convincing mechanistic explanation for the V5 discrepancy. Alternatively, they should temper the claim of general validation and explicitly acknowledge the limited experimental evidence for the expansion direction.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** No
- **Axis** Algorithm performance and efficiency
- **Claim pointer** The authors state their algorithm is "efficient" and enables "large-scale exploration of the sequence-structure space," implying it is practically useful for designing many variants.
- **Evidence pointer** Results section "Algorithm to design novel IDPs"; Methods section "Markov chain Monte Carlo sampling for IDP design"
- **Concern** The manuscript does not provide quantitative information about the computational cost of the design process. How many MCMC steps are typically required to converge? How many MD simulations or alchemical calculations are needed per design? What is the wall-clock time for designing one variant? Without this information, it is difficult to assess whether the approach is genuinely scalable to large-scale design efforts. The authors mention that the algorithm uses reweighting to reduce the number of simulations, but the actual efficiency gain is not quantified.
- **Why it matters** The practical utility of a design algorithm depends critically on its computational cost. If designing a single variant requires days of simulation time, the approach may not be practical for generating large libraries of variants. The claim of "large-scale exploration" needs quantitative support.
- **Resolution test** The authors should provide benchmark data on computational cost, including the number of MCMC steps, number of simulations required, and total computational time for a typical design run. They should also discuss how the cost scales with protein length and sequence diversity.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Generality of design capability
- **Claim pointer** The authors state their algorithm is "general" and "can be used to design sequences with varying amino acid composition and for other target properties than chain expansion."
- **Evidence pointer** Introduction and Conclusions sections
- **Concern** The manuscript only demonstrates the algorithm for one target property (chain compaction) with fixed amino acid composition. While the authors state the algorithm is general, no evidence is provided that it works for other target properties or with variable composition. The MCMC framework may need substantial modification to handle other design objectives, and the efficiency of the approach for other targets is unknown. The claim of generality appears to be an extrapolation rather than a demonstrated capability.
- **Why it matters** The broader impact of this work depends on whether the approach can be extended beyond the specific demonstration. If the algorithm is only effective for chain compaction with fixed composition, its utility is more limited than claimed.
- **Resolution test** The authors should either provide proof-of-principle demonstrations for other target properties or variable composition, or explicitly frame the generality claim as a future direction rather than a current capability.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Phase separation prediction accuracy
- **Claim pointer** The authors report a "high correlation between predicted and observed values of csat" for the designed A1-LCD variants.
- **Evidence pointer** Results section "Experimental characterization of A1-LCD variants"; Figure 5c (referenced but not shown)
- **Concern** The correlation between predicted and experimental csat values is presented as evidence of predictive accuracy. However, the range of csat values spanned by the five variants is not stated, and the absolute errors are not reported. A high correlation can be achieved even with systematic offsets or large absolute errors if the range is wide. The authors note a "small, but systematic, offset between the predicted and experimentally determined values" for both Rg and Rh, which suggests the model has a consistent bias. The magnitude of this offset and its implications for predictive accuracy are not discussed in detail.
- **Why it matters** For practical design applications, absolute accuracy matters more than correlation. If the model systematically over- or under-predicts csat, users would need to apply corrections, and the reliability of the predictions for novel sequences would be uncertain.
- **Resolution test** The authors should report the absolute errors in csat predictions, the range of csat values tested, and a more detailed analysis of the systematic offset. They should also discuss whether the offset is consistent across different sequence types and whether it can be corrected.

- **Concern ID** R1-M5
- **Severity** Major
- **Blocking** No
- **Axis** Sequence diversity of designed variants
- **Claim pointer** The authors state that 113 of 119 swap variants have "less than 30% sequence identity to the wild-type protein," implying substantial sequence diversity.
- **Evidence pointer** Results section "Relating sequence, compaction and propensity to phase separate for the designs"; Figure S6 (referenced but not shown)
- **Concern** Sequence identity is a crude measure of diversity. Two sequences with 30% identity could still be very similar in terms of the properties that matter for IDP behavior, such as the distribution of charged residues, aromatic content, or hydropathy patterns. The authors do not provide a more nuanced analysis of the sequence space explored by their algorithm. Additionally, the clustering procedure used to select representative sequences is not described in sufficient detail to assess whether the selected variants truly sample diverse sequence features.
- **Why it matters** The claim that the algorithm explores diverse sequence space is important for establishing its utility. If the generated variants are all similar in terms of the biophysically relevant features, the approach may be less powerful than claimed.
- **Resolution test** The authors should provide a more detailed characterization of the sequence diversity of their designed variants, including analysis of the distribution of key biophysical features (charge patterning, hydropathy, aromatic content) and a clearer description of the clustering methodology.

- **Minor Comments**
- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Presentation clarity
- **Affected element** Algorithm description
- **Evidence pointer** Methods section "Markov chain Monte Carlo sampling for IDP design"
- **Issue** The description of the MCMC algorithm is somewhat terse. The acceptance criterion in Equation 1 is presented without a clear derivation or intuitive explanation. The role of the control parameter c is mentioned but its selection and sensitivity are not discussed.
- **Required correction** Expand the methods description to provide a clearer explanation of the algorithm's logic, the rationale for the acceptance criterion, and the choice of c. A brief discussion of how the algorithm's performance depends on c would be helpful.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Statistical reporting
- **Affected element** Experimental measurements
- **Evidence pointer** Results section "Experimental characterization of A1-LCD variants"
- **Issue** The number of experimental replicates for csat and Rg measurements is not clearly stated. The authors mention three independent simulations for csat but do not specify how many independent experimental measurements were performed.
- **Required correction** Clearly state the number of independent experimental replicates for each measurement and report the variability (e.g., standard deviation or confidence intervals) for the reported values.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Figure accessibility
- **Affected element** All figures
- **Evidence pointer** Throughout manuscript
- **Issue** The manuscript references many figures and supplementary figures, but the actual figures are not provided in the text. This makes it difficult to assess the quality of the data presentation and the strength of the visual evidence.
- **Required correction** Ensure that all figures are included in the final submission and that they are of sufficient quality to support the claims. Consider whether any additional figures would help clarify the algorithm's performance or the experimental results.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Terminology consistency
- **Affected element** "Intrinsically disordered proteins" definition
- **Evidence pointer** Introduction
- **Issue** The authors define IDPs as including both fully disordered proteins and disordered regions, but the term is used somewhat loosely throughout. The distinction between "IDP variants" and "variants of IDP regions" could be clarified.
- **Required correction** Use consistent terminology throughout, and clarify whether the designed variants are full-length proteins or regions within larger proteins.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Literature context
- **Affected element** Discussion of previous design efforts
- **Evidence pointer** Introduction
- **Issue** The introduction mentions previous work using genetic algorithms for IDP design but does not provide a detailed comparison with the current approach. The novelty of the MCMC-based method relative to prior work is not fully articulated.
- **Required correction** Expand the discussion of prior IDP design efforts and clearly articulate what is new about the current approach.

- **Concern ID** R1-m6
- **Severity** Minor
- **Axis** Data availability
- **Affected element** Code and data deposition
- **Evidence pointer** Data and code availability section
- **Issue** The authors state that data and code are available on GitHub and the Electronic Research Data Archive, but specific repository identifiers or accession numbers are not provided.
- **Required correction** Provide specific repository URLs and accession numbers to ensure that the data and code are accessible to readers.

## Risk / unsupported claims
- The claim that the algorithm is "general" and can be used for other target properties and variable composition is not supported by evidence presented in this manuscript.
- The claim of "good agreement" between predicted and experimental csat values is weakened by the unexplained discrepancy for V5 and the lack of absolute error reporting.
- The statement that the algorithm enables "large-scale exploration of the sequence-structure space" is not quantitatively supported by computational cost data.
- The assertion that charge patterning is the main determinant of compaction in the designed sequences is supported by correlation analysis but causal claims should be tempered.
- The claim that the designed variants have "diverse structural properties" is based on computational predictions and limited experimental validation; the full extent of structural diversity is not experimentally characterized.
- The comparison of designed variants to the human IDRome is based on computational predictions and assumes the simulation model is accurate for these extreme sequence properties, which is not fully validated.