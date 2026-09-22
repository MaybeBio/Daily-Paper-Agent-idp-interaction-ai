## Review setup
- **Input scope** Full manuscript text (abstract, introduction, results, discussion, conclusion, methods) without figures, tables, or supplementary material
- **Assessment boundary** Scientific validity, methodological soundness, interpretational consistency, and alignment with stated claims; no assessment of formatting or editorial style beyond readability
- **Shared manuscript claim summary** The authors propose a chemically interpretable descriptor of amyloidogenic propensity for intrinsically disordered proteins, derived from self-docking analyses of T-REMD conformational ensembles using two force fields. They classify Aβ42 conformers as aggregation-prone or non-aggregation-prone, validate the ensembles against experimental observables, and benchmark the classification using DNAJB6 docking.
- **Visible evidence base** Text descriptions of results, methodological details, and references to figures and tables; actual figures, tables, and supplementary material not provided
- **Missing materials affecting confidence** All figures, tables, supplementary information, simulation parameter details, statistical analyses, and raw data; the manuscript references numerous figures (Figures 1–5, S1–S14) and tables that are essential for evaluating the claims

## Reviewer
- **Overall assessment** The manuscript presents a conceptually interesting approach to identifying aggregation-prone states in disordered proteins, with a potentially useful descriptor for classifying conformers. The dual-force-field strategy and the use of DNAJB6 as a biological benchmark are thoughtful elements. However, the evidence base available for this review is incomplete, and several methodological and interpretational issues require clarification before the central claims can be considered established. The descriptor's novelty relative to existing approaches, the statistical robustness of the classification thresholds, and the biological relevance of monomer-level docking as a proxy for aggregation propensity are all areas that need stronger support.
- **Who would be interested in the results, and why** Researchers in computational biophysics and molecular dynamics, particularly those studying intrinsically disordered proteins and amyloid aggregation; drug discovery groups targeting protein misfolding diseases; and experimentalists studying chaperone interactions with amyloidogenic proteins would find the framework potentially useful for identifying targetable conformers.
- **Major strengths** The use of two complementary force fields to reduce parametrization bias is a sound methodological choice. The interaction-based descriptor, framed as an emergent property of conformational self-recognition, is conceptually appealing and potentially more physically grounded than purely structural metrics. The DNAJB6 benchmark provides a biologically motivated test of the classification scheme. The authors are appropriately cautious in framing the approach as a framework rather than a definitive predictive tool.
- **Major Concerns** See detailed items below.
- **Minor Comments** See detailed items below.
- **Technical failings that need to be addressed before the case is established** R1-M1 (threshold justification), R1-M2 (docking as proxy for aggregation), R1-M3 (DNAJB6 benchmark interpretation), R1-M4 (statistical robustness)
- **Assessment against Nature-style criteria**  
  *Originality*: The interaction-based descriptor is a novel contribution, though it builds on existing concepts of ensemble docking and β-hairpin-centric aggregation models. The originality is moderate rather than transformative.  
  *Scientific importance*: The problem of identifying aggregation-prone states in IDPs is significant for understanding and potentially treating protein misfolding diseases. However, the current evidence does not demonstrate that the descriptor provides predictive or mechanistic insight beyond existing approaches.  
  *Interdisciplinary readership*: The work bridges computational chemistry, biophysics, and neurobiology, and would be of interest to a broad readership if the claims are substantiated.  
  *Technical soundness*: The simulation methodology is standard and appropriate, but the analysis pipeline and statistical treatment require more rigorous justification and validation.  
  *Readability for nonspecialists*: The manuscript is generally well-written and accessible, though some methodological details are dense. The conceptual framing is clear.
- **Recommendation posture** Supportive if technical concerns are resolved; currently not established from the provided evidence

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Methodological justification
- **Claim pointer** The authors state that HS ≤ −60 classifies conformers as aggregation-prone and HS ≥ −20 as non-aggregation-prone, with thresholds selected using a statistically based criterion assuming a Gaussian distribution and retaining conformers beyond ±1 standard deviation from the mean.
- **Evidence pointer** Results section, "Interaction-Based Descriptor versus Structural Metrics"; Methods, "Clustering and Aggregation-Prone Score Function"; location not provided
- **Concern** The threshold selection is described as based on ±1 standard deviation from the mean, but the rationale for this specific statistical criterion is not explained. The choice of a Gaussian assumption for HS distributions is not justified, and the relationship between the thresholds and the underlying biophysical meaning of aggregation propensity is unclear. The authors do not demonstrate that the classification is robust to the choice of threshold or that the ±1 SD criterion is appropriate for this descriptor.
- **Why it matters** The entire classification scheme, and all subsequent analyses including the DNAJB6 benchmark, depends on these thresholds. If the thresholds are arbitrary or not robust, the classification of conformers as aggregation-prone or non-aggregation-prone is not reliable, and the central claims of the paper are undermined.
- **Resolution test** The authors should provide a sensitivity analysis showing how the classification and downstream results change with different threshold values. They should also justify the Gaussian assumption or provide an alternative statistical basis for threshold selection, ideally with reference to experimental or biophysical benchmarks.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Interpretational validity
- **Claim pointer** The authors claim that the HADDOCK homodimer docking score serves as a proxy for self-association propensity and thus for amyloidogenic propensity, framing this as an "emergent property of conformational self-recognition."
- **Evidence pointer** Results, "Aggregation-Prone Morphologies: An Ensemble-Docking Descriptor"; Methods, "Ensemble-Based Docking"; location not provided
- **Concern** The use of monomer–monomer docking to assess aggregation propensity is a significant simplification. Aggregation in Aβ involves multi-molecular processes, and the relevance of pairwise monomer interactions to the nucleation of oligomers is not established. The authors do not discuss the limitations of this approach, such as the absence of concentration effects, the lack of multi-body interactions, or the potential for docking artifacts. The claim that the descriptor captures "emergent" properties is not supported by the evidence presented.
- **Why it matters** If the docking score does not reliably reflect the actual aggregation propensity of conformers in solution, the classification scheme and the DNAJB6 benchmark results are not meaningful. The central premise of the paper rests on this proxy relationship.
- **Resolution test** The authors should provide validation of the docking-based descriptor against experimental or more rigorous computational measures of aggregation propensity, such as comparison with known aggregation-prone regions, experimental mutation data, or coarse-grained simulations of oligomerization. They should also discuss the limitations of the pairwise docking approximation.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Interpretational validity
- **Claim pointer** The authors state that the positive correlation between Aβ–Aβ and Aβ–DNAJB6 HADDOCK scores indicates that DNAJB6 preferentially binds aggregation-prone Aβ conformers, supporting the classification scheme.
- **Evidence pointer** Results, "DNAJB6 Supports Conformer-Selective Recognition"; location not provided
- **Concern** The interpretation of the correlation between Aβ–Aβ and Aβ–DNAJB6 docking scores is not straightforward. A positive correlation could arise from trivial factors, such as overall conformational properties (e.g., size, surface area) that affect docking scores generally, rather than from specific recognition of aggregation-prone features. The authors do not control for such confounding factors. Additionally, the use of a single DNAJB6 construct and a fixed active site definition limits the generality of the finding. The claim that this supports the classification scheme is therefore not well established.
- **Why it matters** The DNAJB6 benchmark is presented as a key validation of the classification scheme. If the correlation is driven by confounding factors, the validation is not meaningful, and the biological relevance of the classification is not supported.
- **Resolution test** The authors should perform control docking experiments with a non-chaperone protein or with a DNAJB6 mutant lacking the active site, to demonstrate specificity. They should also analyze whether the correlation persists after controlling for global conformational properties such as Rg or SASA.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** Yes
- **Axis** Statistical robustness
- **Claim pointer** The authors report Pearson correlation coefficients between HS and structural descriptors, and state that the results are consistent across time blocks and force fields.
- **Evidence pointer** Results, "Interaction-Based Descriptor versus Structural Metrics"; Figures 5 and S13–S14; location not provided
- **Concern** The statistical analysis appears limited to Pearson correlations without reported confidence intervals, significance tests, or effect sizes. The number of representative conformers used in the correlation analysis is not stated, and the potential for non-linear relationships is not addressed. The claim of consistency across time blocks is based on visual inspection of figures rather than quantitative comparison.
- **Why it matters** Without proper statistical treatment, the strength and reliability of the reported correlations cannot be assessed. The conclusions drawn from these correlations, including the claimed superiority of the interaction-based descriptor over structural metrics, are not quantitatively supported.
- **Resolution test** The authors should report sample sizes, confidence intervals, and p-values for all correlations. They should also test for non-linear relationships and provide a quantitative comparison of correlations across time blocks and force fields.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Abstract
- **Evidence pointer** Abstract; location not provided
- **Issue** The abstract states that the descriptor "classifies individual conformers within the generated ensembles according to their intrinsic aggregation tendency," but the term "intrinsic" is potentially misleading given that the descriptor is derived from docking calculations that depend on the specific force field and docking protocol used.
- **Required correction** Consider rephrasing to "classifies individual conformers according to their computed self-association propensity within the present computational framework" to avoid overstating the generality of the descriptor.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Methods
- **Evidence pointer** Methods, "Ensemble Generation via T-REMD with Multiple FFs"; location not provided
- **Issue** The description of the T-REMD setup is incomplete. The number of replicas, the temperature spacing, the total simulation time per replica, and the exchange acceptance rates are not reported. The statement "a cumulative simulation time of ∼150 μs" is ambiguous without specifying the per-replica time.
- **Required correction** Provide a complete description of the simulation parameters, including the number of replicas, temperature range and spacing, simulation length per replica, and exchange rates.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Interpretational caution
- **Affected element** Results, "Intrinsically Disordered Nature of Aβ42"
- **Evidence pointer** Results, "Intrinsically Disordered Nature of Aβ42"; location not provided
- **Issue** The authors state that the two force fields "consistently reproduce the intrinsically disordered nature of Aβ42," but the reported average Rg values (1.03 nm and 1.05 nm) are below the experimental value of 1.2 ± 0.2 nm. While the authors note this is within the experimental uncertainty, the systematic underestimation is not discussed in detail.
- **Required correction** Add a brief discussion of the systematic underestimation of Rg and its potential implications for the conformational ensemble and the subsequent classification.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Results, "Aggregation-Prone Morphologies"
- **Evidence pointer** Results, "Aggregation-Prone Morphologies: An Ensemble-Docking Descriptor"; location not provided
- **Issue** The description of the clustering procedure is unclear regarding the number of clusters obtained, the size distribution of clusters, and how representative structures were selected from clusters with at least 100 members. The relationship between cluster size and the final number of conformers used for docking is not stated.
- **Required correction** Provide details on the number of clusters, the criteria for selecting representative structures, and the total number of conformers used in the docking analysis.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Methods, "Ensemble-Based Docking with DNAJB6"
- **Evidence pointer** Methods, "Ensemble-Based Docking of Aggregation- and Non-Aggregation-Prone Conformations with DNAJB6"; location not provided
- **Issue** The definition of the active site residues (132–221) is described as spanning the linker and part of the C-terminal domain, but the rationale for this specific choice is not fully explained. The authors state that this region "mediates client-protein recognition," but do not provide supporting evidence or references for this claim.
- **Required correction** Provide a more detailed justification for the choice of active site residues, with reference to experimental or structural data on DNAJB6–client interactions.

## Risk / unsupported claims
- The claim that the descriptor captures "emergent" properties of conformational self-recognition is not supported by the evidence presented; the descriptor is a pairwise docking score, and its relationship to multi-molecular aggregation processes is not established.
- The claim that DNAJB6 "preferentially interacts with aggregation-prone conformers" is based on a correlation between docking scores that may be confounded by global conformational properties; specificity controls are not reported.
- The claim that the classification scheme provides a "physically grounded descriptor" is not fully supported, as the physical basis of the HADDOCK score as a proxy for aggregation propensity is not validated against experimental or more rigorous computational benchmarks.
- The claim that the approach is "potentially generalizable to other amyloidogenic proteins" is speculative and not tested in this work.
- The statistical significance and robustness of the reported correlations between HS and structural descriptors cannot be assessed from the provided information.