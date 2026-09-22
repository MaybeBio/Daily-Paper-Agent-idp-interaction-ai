## Review setup
- **Input scope** Full manuscript text, including main text, figure legends, and tables. Supplementary material was not provided.
- **Assessment boundary** Scientific soundness, technical validity, clarity of claims, and adequacy of evidence presented in the manuscript. The review does not assess editorial or formatting issues beyond those affecting scientific comprehension.
- **Shared manuscript claim summary** The authors present FiveFold, an ensemble-based protein structure prediction method that integrates five existing prediction algorithms (AlphaFold2, RoseTTAFold, OmegaFold, ESMFold, EMBER3D) to generate multiple conformational states. They validate this approach using alpha-synuclein as a model intrinsically disordered protein, reporting superior conformational coverage (87%) compared to single-structure methods (23-34%), enhanced binding site identification (23 vs 3-5 sites), and improved virtual screening hit rates (5-fold increase). The manuscript also discusses potential applications in drug discovery, particularly for challenging targets such as intrinsically disordered proteins.
- **Visible evidence base** Main text, Figure 1 (schematic of FiveFold architecture), Figure 2 (experimental alpha-synuclein structures), Figure 3 (PFVM heatmap), Figure 4 (FiveFold-generated ensemble), Tables 1-9 (comparative attributes, PFVM construction methodology, experimental structures, generated conformations, performance metrics, platform implementation, detailed attribute comparisons).
- **Missing materials affecting confidence** Supplementary material (referenced as Supplementary Material 1) was not provided. The manuscript references a prior publication by Yang et al. (reference 9) for the original FiveFold methodology, but this paper was not available for review. No code, software repository, or executable version of the FiveFold platform was provided. No raw data files, RMSD calculation outputs, or virtual screening results were provided.

## Reviewer
- **Overall assessment** The manuscript presents an interesting conceptual framework for ensemble-based protein structure prediction, addressing a genuine limitation of current single-structure methods. However, the work as presented is primarily a descriptive application of an existing methodology (FiveFold, previously published by Yang et al.) to a single test case (alpha-synuclein). The validation is limited in scope, lacks rigorous quantitative benchmarking against established methods, and contains several technical inconsistencies and unsupported claims. The performance metrics presented in Tables 7 and 9 appear to be asserted rather than derived from clearly described experimental procedures. The manuscript would benefit substantially from a more rigorous validation framework, including comparison against established ensemble generation methods, statistical analysis of the reported improvements, and independent verification of the claimed performance metrics. As presented, the case for FiveFold's superiority over existing methods is not fully established from the provided evidence.

- **Who would be interested in the results, and why** Computational structural biologists interested in conformational ensembles and intrinsically disordered proteins would find the conceptual framework relevant. Drug discovery researchers working on challenging targets such as IDPs, transcription factors, and protein-protein interactions may find the potential applications interesting. Researchers developing or applying machine learning methods for protein structure prediction would be interested in the ensemble-based approach as an alternative to single-structure paradigms. However, the current evidence base is too limited to strongly influence practice in any of these communities.

- **Major strengths**
  1. Addresses a real and important limitation of current protein structure prediction methods: the inability to capture conformational diversity, particularly for intrinsically disordered proteins.
  2. The conceptual framework of integrating multiple prediction algorithms and representing conformational variation through a position-specific matrix (PFVM) is intellectually appealing.
  3. The use of alpha-synuclein as a test case is appropriate, given its well-characterized disorder and biomedical relevance.
  4. The manuscript provides detailed technical specifications (Tables 2, 8, 9) that could support reproducibility if the underlying data were available.

- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness / Validation rigor
- **Claim pointer** The manuscript claims that FiveFold achieves a conformational coverage score of 0.87, compared to 0.23 for AlphaFold2 and 0.34 for RoseTTAFold, representing a 3.8x and 2.6x improvement, respectively.
- **Evidence pointer** Table 7, Section "FiveFold performance validation", Section "Quantitative conformational diversity analysis"
- **Concern** The conformational coverage score is defined as a binary match (δᵢⱼ = 1 if predicted secondary structure at position j matches experimental structure i within ±2 positions) averaged over 12 experimental structures and 140 residues. However, the manuscript does not provide the actual per-structure or per-position data from which these scores were computed. The score definition itself is problematic: a ±2 position tolerance for secondary structure matching is extremely lenient and would likely yield high scores even for mediocre predictions. More critically, the comparison is unfair because AlphaFold2 and RoseTTAFold are designed to predict a single static structure, not to maximize coverage across an ensemble. The appropriate comparison would be against other ensemble generation methods (e.g., molecular dynamics simulations, Markov state models, or other conformational sampling approaches), not against single-structure predictors. The claimed 0.87 coverage score for FiveFold is also not independently verifiable from the data presented.
- **Why it matters** The central quantitative claim of the manuscript, that FiveFold provides superior conformational coverage, rests entirely on this metric. If the metric is flawed or the comparison is inappropriate, the primary evidence for FiveFold's utility is undermined.
- **Resolution test** Provide the full per-residue, per-structure comparison data. Recompute coverage scores using a more rigorous matching criterion (e.g., exact secondary structure match or RMSD-based structural alignment). Include comparison against established ensemble generation methods, not just single-structure predictors. Provide confidence intervals or statistical significance tests for the reported improvements.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness / Reproducibility
- **Claim pointer** The manuscript states that "the confirmation of any protein 3D structure can be described by a single PFSC string" and that structures can be constructed "through high-throughput screening of the PDB-PFSC database with homologous conformation processing."
- **Evidence pointer** Section "Protein folding shape code (PFSC) system", Section "Protein folding variation matrix (PFVM)", Section "FiveFold multi-conformation generation"
- **Concern** The PFSC system is described as encoding secondary structure states (H, E, B, G, I, T, S, C) for each residue. However, the manuscript does not explain how a one-dimensional string of secondary structure assignments can uniquely or even approximately determine a three-dimensional protein structure. Secondary structure content alone is grossly insufficient to define a protein fold. The claim that 3D structures can be reconstructed from PFSC strings via "homologous conformation processing" against a "PDB-PFSC database" is not substantiated. No details are provided about the database, the homology matching algorithm, the success rate of structure reconstruction, or the accuracy of the resulting models. The ten FiveFold-generated conformations shown in Figure 4 are presented without any quantitative assessment of their structural validity (e.g., Ramachandran statistics, clash scores, or comparison to known alpha-synuclein conformations).
- **Why it matters** The entire premise of the FiveFold approach depends on the ability to generate valid 3D structures from PFSC strings. If this reconstruction step is not reliable, the generated conformations may not be physically meaningful, and all downstream applications (binding site identification, virtual screening) would be compromised.
- **Resolution test** Provide a detailed description of the PDB-PFSC database and the structure reconstruction algorithm. Include validation metrics for reconstructed structures (e.g., RMSD to known structures, MolProbity scores). Demonstrate that the ten generated conformations are physically plausible and energetically reasonable.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Scientific importance / Novelty
- **Claim pointer** The manuscript claims that FiveFold represents a "paradigm-shifting advancement" and a "transformative advancement in protein structure prediction."
- **Evidence pointer** Introduction, Section "Comparative analysis with current methods", Conclusions
- **Concern** The FiveFold methodology was previously published by Yang et al. (reference 9). The current manuscript is described as "a comprehensive application" of this existing method. The novelty of the current work appears to be limited to: (1) application to alpha-synuclein as a test case, and (2) discussion of potential drug discovery applications. Neither of these constitutes a methodological advance. The comparative analysis with current methods (Section "Comparative analysis with current methods") is largely qualitative and does not include quantitative benchmarks against state-of-the-art methods such as AlphaFold2's recently developed ensemble prediction capabilities, AlphaFold3, or other established conformational sampling approaches. The claims of "paradigm-shifting" and "transformative" are not supported by the evidence presented.
- **Why it matters** For a manuscript to be of significant interest to the broad readership of a Nature-family journal, it must present either a novel methodology or a substantial advance in application with clear evidence of improved performance. The current manuscript does neither.
- **Resolution test** Clearly articulate the novel contributions of this manuscript relative to the previously published FiveFold methodology. Provide quantitative benchmarks against current state-of-the-art methods for conformational ensemble prediction, including metrics such as ensemble coverage, diversity, and agreement with experimental data.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness / Data integrity
- **Claim pointer** Table 7 reports specific quantitative values for binding site prediction (23 sites), virtual screening hits (1,247 from 10,000 compounds), and membrane interaction accuracy (89%).
- **Evidence pointer** Table 7, Section "Drug discovery applications"
- **Concern** The manuscript reports these quantitative results without providing the underlying data, methodology details, or analysis protocols. For example: (1) Binding site identification: Which tool was used (CASTp is mentioned in the methodology note)? What was the input structure? How were false positives excluded? (2) Virtual screening: What was the compound library composition? What docking software was used? What was the scoring function? How were "hits" defined? What was the hit rate for the control (single-structure) methods? (3) Membrane interaction accuracy: How was this measured? What was the comparison set? The methodology note states "All metrics represent averages across the experimental validation dataset" but the individual data points are not shown. The virtual screening hit count of 1,247 out of 10,000 (12.5% hit rate) seems implausibly high for a typical virtual screening campaign and requires explanation.
- **Why it matters** These quantitative claims are central to the drug discovery applications section, which is a major part of the manuscript's stated purpose. Without access to the underlying data and methodology, these claims cannot be evaluated or reproduced.
- **Resolution test** Provide detailed methodology for each drug discovery application, including software versions, parameters, and analysis protocols. Provide the full results for all methods compared (not just FiveFold). Make the data publicly available.

- **Concern ID** R1-M5
- **Severity** Major
- **Blocking** No
- **Axis** Technical soundness / Statistical rigor
- **Claim pointer** The manuscript claims that FiveFold's performance improvements are consistent across multiple metrics, including "2.6–7.7x improvement across all primary performance metrics."
- **Evidence pointer** Table 7, Section "FiveFold performance validation"
- **Concern** No statistical analysis is provided for any of the reported improvements. The coverage scores, binding site counts, and virtual screening hit rates are presented as single point estimates without confidence intervals, standard deviations, or significance tests. Given that the comparison involves only one test protein (alpha-synuclein), the generalizability of these results is unknown. The manuscript does not report how many independent runs were performed, whether the results are deterministic, or how sensitive the results are to parameter choices.
- **Why it matters** Without statistical rigor, the reported improvements could be due to chance, parameter tuning, or artifacts of the specific test case. The claim of consistent improvement across all metrics is not supported by appropriate statistical evidence.
- **Resolution test** Provide statistical analysis of all reported metrics, including confidence intervals and significance tests. Perform sensitivity analysis to show that results are robust to parameter choices. Ideally, validate on multiple test proteins with diverse structural characteristics.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity / Reproducibility
- **Affected element** Table 1
- **Evidence pointer** Table 1
- **Issue** The table contains several typographical errors and inconsistencies. For example, the row for "Usage in absence of structural homologs" contains "Yes–it- it works on orphan sequences" with a duplicated "it-". The table also uses inconsistent terminology (e.g., "Rosettafold" vs. "RoseTTAFold" in the header). The column for FiveFold lists "Ten alternative conformations (user-defined PFSC shape paths)" but the number ten is not justified anywhere in the text.
- **Required correction** Proofread the table carefully and correct typographical errors. Use consistent terminology throughout. Justify the choice of ten conformations or state that this is an arbitrary user-defined parameter.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Clarity / Technical accuracy
- **Affected element** Section "Functional score definition"
- **Evidence pointer** Section "Functional score definition"
- **Issue** The functional score is defined as a weighted sum of four components (diversity, experimental agreement, binding site accessibility, computational efficiency) with weights 0.3, 0.4, 0.2, and 0.1. However, the manuscript does not explain how these weights were determined, whether they are optimized for specific applications, or how sensitive the conclusions are to the choice of weights. The experimental agreement component is problematic because for many IDPs, there may not be a single "experimental structure" to compare against.
- **Required correction** Provide justification for the chosen weights. Discuss the sensitivity of results to weight selection. Clarify how experimental agreement is computed when multiple experimental structures exist or when no experimental structure is available.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Completeness / Reproducibility
- **Affected element** Section "Computational modeling analysis using alpha-synuclein"
- **Evidence pointer** Section "Computational modeling analysis using alpha-synuclein"
- **Issue** The manuscript states that "Ten of the possible conformations in PFSC strings are listed in Table 5" but does not explain the criteria used to select these ten conformations from the astronomically large number of possible combinations. The selection criteria are critical for reproducibility and for understanding the diversity of the generated ensemble.
- **Required correction** Describe the algorithm or criteria used to select the ten conformations from the PFVM. Discuss how the selection balances diversity and probability.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Clarity / Technical accuracy
- **Affected element** Section "Comparative analysis with current methods"
- **Evidence pointer** Section "Comparative analysis with current methods"
- **Issue** The comparison with current methods is entirely qualitative. The manuscript states that AlphaFold2 and RoseTTAFold "could not provide the multiple structural states necessary for drug discovery applications" but does not acknowledge recent developments in ensemble prediction, such as AlphaFold2's ability to generate multiple models through stochastic sampling or the development of specialized ensemble prediction methods.
- **Required correction** Update the comparative analysis to acknowledge recent developments in ensemble prediction. Provide quantitative comparisons where possible.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Completeness / Reproducibility
- **Affected element** Section "Regulatory and economic implications"
- **Evidence pointer** Section "Regulatory and economic implications"
- **Issue** This section discusses regulatory frameworks, quality control, and economic implications but does not provide specific examples, case studies, or references to support the claims. The discussion is generic and could apply to any computational drug discovery method.
- **Required correction** Provide specific examples of regulatory considerations for AI-based drug discovery methods. Cite relevant regulatory guidance documents or case studies.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Clarity / Technical accuracy
- **Affected element** Table 5
- **Evidence pointer** Table 5
- **Issue** The PFVM matrix in Table 5B shows probability values for H, E, and C states only, but the PFSC system defines eight states (H, E, B, G, I, T, S, C). The probabilities for the five other states are not shown, and it is unclear whether they are zero or simply omitted. Additionally, the probabilities in each column do not appear to sum to 1.0 (e.g., column 1: 0.8 + 0.1 + 0.1 = 1.0, but column 2: 0.7 + 0.2 + 0.1 = 1.0, while column 3: 0.9 + 0.1 + 0.0 = 1.0; however, some columns appear to sum to less than 1.0).
- **Required correction** Clarify whether the omitted states have zero probability or are simply not shown. Ensure that probabilities in each column sum to 1.0 or explain any deviation.

- **Concern ID** R1-m6
- **Severity** Minor
- **Axis** Completeness / Reproducibility
- **Affected element** Section "Platform implementation"
- **Evidence pointer** Table 8
- **Issue** The platform implementation details in Table 8 list specific software components (Java JDK 1.8.0, PostgreSQL 12.0, React 18.0) but do not provide information about the operating system, hardware requirements, or whether the platform is publicly available. The manuscript does not mention a software repository, license, or availability statement.
- **Required correction** Provide information about software availability, including a repository URL or contact for obtaining the platform. Specify the operating system and hardware requirements.

- **Concern ID** R1-m7
- **Severity** Minor
- **Axis** Clarity / Technical accuracy
- **Affected element** Section "Conclusions"
- **Evidence pointer** Section "Conclusions"
- **Issue** The conclusion states that "the methodology's ability to generate multiple plausible conformations provides drug discovery researchers with detailed conformational landscapes that identify cryptic binding sites, optimize selectivity across various states, and develop allosteric modulators that leverage conformational communication networks." This is a strong claim that goes beyond the evidence presented. The manuscript demonstrates the generation of ten conformations for alpha-synuclein but does not demonstrate the identification of cryptic binding sites, optimization of selectivity, or development of allosteric modulators.
- **Required correction** Moderate the conclusions to reflect the actual evidence presented. Distinguish between demonstrated capabilities and potential applications.

- **Concern ID** R1-m8
- **Severity** Minor
- **Axis** Completeness / Reproducibility
- **Affected element** Section "Structural database analysis"
- **Evidence pointer** Section "Structural database analysis", Table 3
- **Issue** The manuscript states that twelve experimental structures were used for validation, but Table 3 lists only ten structures with PDB IDs. Two structures appear to be missing from the table. Additionally, the table lists "1XQ8-A" with a resolution of 2.1 Å, but the original publication for 1XQ8 reports a different resolution. The chain identifiers and resolution values should be verified against the PDB.
- **Required correction** Ensure that all twelve structures are listed in Table 3. Verify all PDB IDs, chain identifiers, and resolution values against the Protein Data Bank.

- **Concern ID** R1-m9
- **Severity** Minor
- **Axis** Clarity / Technical accuracy
- **Affected element** Section "Quantitative conformational diversity analysis"
- **Evidence pointer** Section "Quantitative conformational diversity analysis"
- **Issue** The manuscript states that "approximately 4.85 × 10¹³⁹ conformations in PFSC shapes can be formed" from the PFVM. This calculation assumes independent selection from each of the 28 five-residue segments with an average of 4-8 possible states per segment. However, the PFVM in Table 5B shows only three states (H, E, C) with non-zero probabilities, which would give 3²⁸ ≈ 2.3 × 10¹³ possible combinations, not 4.85 × 10¹³⁹. The calculation appears to be inconsistent with the data presented.
- **Required correction** Reconcile the calculation with the data in Table 5B. Provide the full probability distribution for all eight PFSC states and show the calculation steps.

- **Concern ID** R1-m10
- **Severity** Minor
- **Axis** Completeness / Reproducibility
- **Affected element** Section "Computational modeling analysis using alpha-synuclein"
- **Evidence pointer** Section "Computational modeling analysis using alpha-synuclein"
- **Issue** The manuscript states that "the default FiveFold sampling did not produce beta-strand fragments in the N-terminal region" despite experimental evidence for such structures. This is acknowledged as a limitation, but the manuscript does not provide a quantitative assessment of how significant this limitation is. For example, what fraction of the N-terminal region is affected? How does this impact the utility of the generated ensemble for drug discovery applications?
- **Required correction** Provide a quantitative assessment of the N-terminal sampling limitation and its potential impact on downstream applications.

## Risk / unsupported claims
1. The claim that FiveFold achieves "87% conformational coverage" compared to "23-34% for traditional methods" is not supported by the data presented. The coverage score calculation is not fully described, the comparison is against inappropriate baselines (single-structure predictors rather than ensemble methods), and no statistical analysis is provided.
2. The claim that FiveFold identified "23 potential binding sites" compared to "3-5 sites" for traditional methods is not supported. The binding site identification methodology is not described in sufficient detail, and the comparison is not apples-to-apples.
3. The claim of "5x improvement in virtual screening hits" is not supported. The virtual screening methodology is not described, and the hit rate of 12.5% (1,247/10,000) is implausibly high without additional context.
4. The claim that "the confirmation of any protein 3D structure can be described by a single PFSC string" is not supported. Secondary structure strings are insufficient to define 3D structure.
5. The claim that FiveFold can identify "cryptic binding sites" and "cryptic pockets" is not supported by any experimental validation.
6. The claim that FiveFold provides "superior performance across multiple evaluation criteria" (Figure 1 legend) is not supported by the data presented.
7. The claim that "applications like FiveFold can help reduce the diversity of probable structures, allowing for a better focus on drug discovery efforts" is speculative and not supported by the evidence.
8. The manuscript's assertion that approximately 80% of human proteins are "undruggable" is presented without citation and is an oversimplification of a complex topic.
9. The claim that "considering protein flexibility can increase fragment hit rates by 2-4 fold" is presented without specific citations or context.
10. The manuscript's statement that "the online version contains supplementary material" suggests that additional data may be available, but this material was not provided for review, making several claims unverifiable.