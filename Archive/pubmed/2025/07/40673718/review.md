## Review setup
- **Input scope** Full manuscript text (abstract, introduction, methods, results, discussion, conclusions) as provided
- **Assessment boundary** Scientific content, methodological soundness, evidence quality, and alignment with claims; no assessment of editorial fit or publication policy
- **Shared manuscript claim summary** The authors develop a circuit topology-based analysis framework combined with atomistic molecular dynamics simulations to study how site-specific phosphorylation modulates the conformational ensemble and topological dynamics of the intrinsically disordered glucocorticoid receptor N-terminal domain (GR AF1c). They report that phosphorylation promotes nonlocal contacts and disordered compact topologies, that topological compaction depends on the specific phosphorylation site, and that the framework can be broadly applied to disordered proteins.
- **Visible evidence base** Methods section (simulation protocols, analysis tools), Results section (Rg, SASA, secondary structure, PCA, circuit topology, kinetics), Discussion, Figures referenced but not provided, Supplementary figures referenced but not provided
- **Missing materials affecting confidence** Figures and supplementary figures are referenced but not included in the provided material; experimental NMR data are cited but not shown; simulation convergence and sampling quality metrics are not fully described; force field validation details are incomplete

## Reviewer
- **Overall assessment** The manuscript presents a potentially useful analytical framework for studying topological dynamics of disordered proteins and applies it to a biologically relevant system. The combination of extensive MD simulations with circuit topology analysis is conceptually interesting. However, the evidence provided in the text alone is insufficient to fully evaluate the robustness of the claims. Several key results are described qualitatively without supporting quantitative data, and the relationship between the computational observations and biological function remains speculative. The central methodological contribution, the CT Folding Score, requires clearer validation and benchmarking against existing approaches.
- **Who would be interested in the results, and why** Researchers studying intrinsically disordered proteins, particularly those interested in post-translational modification effects on conformational ensembles; computational biophysicists developing new analysis tools for MD simulations; nuclear receptor biologists interested in GR regulation mechanisms. The proposed CT Folding Score could be of interest to the broader protein folding and polymer physics community.
- **Major strengths** The study addresses an important and understudied question regarding how phosphorylation modulates disordered protein conformations. The use of extensive unbiased MD simulations (over 40 microseconds total) is commendable. The circuit topology framework is conceptually novel and could provide new insights beyond traditional geometric measures. The comparison with experimental NMR data for validation is appropriate. The biological context (GR signaling) gives the work practical relevance.
- **Major Concerns**
  - **Concern ID** R1-M1
  - **Severity** Major
  - **Blocking** Yes
  - **Axis** Technical soundness
  - **Claim pointer** The authors claim that the CT Folding Score can efficiently distinguish topologically compact from solvent-exposed conformations and that this approach is more sensitive than geometric measures.
  - **Evidence pointer** Results section, Circuit Topology subsection; Figures 4, 5, S4, S5, S6 (not provided)
  - **Concern** The definition and validation of the CT Folding Score are not fully described in the text. The threshold for defining "topologically compact" is stated as the average score, but the rationale for this choice is not justified. The claim that this metric is superior to Rg or SASA for detecting compaction events requires quantitative comparison, which is not presented in the text. The sensitivity and specificity of the metric for detecting biologically relevant conformational states are not established.
  - **Why it matters** The CT Folding Score is the central methodological contribution of the paper. If its validity and utility are not rigorously demonstrated, the core claim of the manuscript is undermined. Without proper benchmarking against existing metrics and demonstration of its unique value, the framework may be seen as an incremental addition rather than a significant advance.
  - **Resolution test** Provide a clear mathematical definition of the CT Folding Score, demonstrate its behavior on test systems with known topology, quantitatively compare its performance against Rg, SASA, and contact number in distinguishing known conformational states, and show that it captures information not available from these standard metrics.
  - **Concern ID** R1-M2
  - **Severity** Major
  - **Blocking** Yes
  - **Axis** Evidence quality
  - **Claim pointer** The authors claim that "site-specific phosphorylation facilitates the formation of nonlocal contacts, leading to the emergence of disordered compact topologies with significant entanglement, which are distinct from solvent-exposed topologies."
  - **Evidence pointer** Results section, Circuit Topology subsection; Figures 4, 5, S10 (not provided)
  - **Concern** The quantitative evidence for this central claim is not presented in the text. The authors describe differences in contact maps and topology matrices between phosphovariants, but no statistical measures, effect sizes, or confidence intervals are reported. The claim of "significant entanglement" is not supported by any quantitative metric of entanglement. The distinction between "disordered compact" and "solvent-exposed" states appears to be based on a threshold that is not independently validated.
  - **Why it matters** This is the primary biological finding of the study. Without quantitative support, the claim that phosphorylation induces specific topological states cannot be evaluated. The reader cannot assess whether the observed differences are robust, reproducible, or biologically meaningful.
  - **Resolution test** Provide quantitative comparisons between phosphovariants for contact probabilities, topology metrics, and entanglement measures, with appropriate statistical tests. Show that the observed differences are consistent across independent replicates and are not artifacts of the analysis method.
  - **Concern ID** R1-M3
  - **Severity** Major
  - **Blocking** No
  - **Axis** Sampling adequacy
  - **Claim pointer** The authors claim that their simulations reveal the conformational ensemble and kinetics of AF1c phosphovariants, including slow and fast dynamics groups with half-decay times of 30 ns and 10 ns, respectively.
  - **Evidence pointer** Methods section, Molecular Dynamics Simulations; Results section, Conformational Kinetics; Figure 6 (not provided)
  - **Concern** The manuscript does not provide sufficient evidence that the simulations have converged. For disordered proteins, which have rugged energy landscapes and slow relaxation times, 1 microsecond per replicate may not be sufficient to sample the full conformational ensemble. The authors state that the first 100 ns were removed as equilibration, but no convergence metrics (e.g., block averaging, multiple independent runs reaching similar distributions) are reported. The autocorrelation times of 30 ns suggest that the effective number of independent samples may be limited.
  - **Why it matters** If the simulations are not converged, the reported conformational ensembles and kinetic parameters may not be representative of the true behavior of the system. This would affect all downstream analyses and conclusions.
  - **Resolution test** Provide convergence analysis, such as split-half analysis of the trajectory data, comparison of distributions from different time windows, or assessment of whether the observed properties stabilize over the simulation time. Report the effective number of independent samples for each phosphovariant.
  - **Concern ID** R1-M4
  - **Severity** Major
  - **Blocking** No
  - **Axis** Force field validation
  - **Claim pointer** The authors use the amber99SBdisp force field with phosphoserine parameters taken from a specific source, and validate their simulations against experimental NMR chemical shifts.
  - **Evidence pointer** Methods section, Molecular Dynamics Simulations and Calculation of NMR Spectra; Results section, NMR validation; Figure S2, S3 (not provided)
  - **Concern** The validation against NMR data is only performed for the nonphosphorylated variant. The phosphoserine parameters are not independently validated. The authors note deviations in nitrogen shifts for residues 215-226 and at the C-terminus, but the implications of these deviations for the reliability of the simulations are not discussed. The correlation coefficients (R > 0.76) are reported, but the significance of these values for validating disordered protein simulations is not established.
  - **Why it matters** The reliability of all conclusions depends on the accuracy of the force field and simulation parameters. If the phosphoserine parameters are not validated, the results for phosphorylated variants may be unreliable. The observed deviations could indicate systematic errors that affect the conformational ensemble.
  - **Resolution test** Validate the phosphoserine parameters against experimental data where available, or at minimum discuss the known limitations and their potential impact on the results. Provide a more detailed analysis of the NMR deviations and their structural implications.
  - **Concern ID** R1-M5
  - **Severity** Major
  - **Blocking** No
  - **Axis** Biological relevance
  - **Claim pointer** The authors state that "the ability of AF1c phosphovariants to adopt multiple structural changes likely creates distinct binding surfaces within the NTD, enabling the GR to selectively interact with different regulatory complexes along its signal transduction pathway."
  - **Evidence pointer** Discussion section
  - **Concern** The connection between the computational observations and biological function is speculative. The authors do not provide experimental evidence linking specific conformational states to functional outcomes. The claim that different phosphovariants create distinct binding surfaces is not tested, and no binding partners or functional assays are discussed. The extrapolation from in silico observations to in vivo signaling consequences is not justified by the data presented.
  - **Why it matters** The biological significance of the findings is a key motivation for the work. If the functional implications are not supported by evidence, the impact of the study is diminished. Overinterpretation of computational results can mislead readers and future research directions.
  - **Resolution test** Either temper the biological claims to match the evidence, or provide additional experimental or literature-based support for the proposed functional consequences. Clearly distinguish between observations and hypotheses.
- **Minor Comments**
  - **Concern ID** R1-m1
  - **Severity** Minor
  - **Axis** Clarity
  - **Affected element** Methods section, Circuit Topology
  - **Evidence pointer** Methods section, Circuit Topology subsection
  - **Issue** The description of the CT Folding Score formula is incomplete. The text states it is defined as Paverage(P)+Saverage(S)+Xaverage(X) but does not explain how the averages are calculated, what the expected range of values is, or how the score behaves for known reference states.
  - **Required correction** Provide a complete mathematical definition, including how averages are computed, and describe the expected behavior of the score for idealized cases (e.g., fully extended, fully compact, random coil).
  - **Concern ID** R1-m2
  - **Severity** Minor
  - **Axis** Reproducibility
  - **Affected element** Methods section, Molecular Dynamics Simulations
  - **Evidence pointer** Methods section, Molecular Dynamics Simulations subsection
  - **Issue** The manuscript states that three different initial structures were selected for each phosphovariant, but does not describe how these structures were generated or selected. The criteria for choosing initial structures and the diversity among them are not specified.
  - **Required correction** Describe the procedure for generating and selecting initial structures, including any quality scores used and the structural diversity among the chosen starting points.
  - **Concern ID** R1-m3
  - **Severity** Minor
  - **Axis** Statistical reporting
  - **Affected element** Results section, Sequential Phosphorylation Opens Up the Protein Structure
  - **Evidence pointer** Results section, Sequential Phosphorylation subsection; Figures 2, S2 (not provided)
  - **Concern** The authors report Rg values as 2.2 ± 0.4 nm and 2.5 ± 0.4 nm for different variants, but do not specify what the uncertainty represents (standard deviation, standard error, or confidence interval). The number of independent samples contributing to these estimates is not stated.
  - **Required correction** Specify the type of uncertainty reported and the number of independent samples. Consider reporting confidence intervals or bootstrap estimates.
  - **Concern ID** R1-m4
  - **Severity** Minor
  - **Axis** Literature context
  - **Affected element** Discussion section
  - **Evidence pointer** Discussion section, paragraph on biological implications
  - **Issue** The discussion of phosphorylation effects on GR function cites several studies but does not critically evaluate how the present computational findings align with or challenge existing experimental observations beyond a general statement of consistency.
  - **Required correction** Provide a more nuanced comparison with experimental findings, including any discrepancies and how they might be resolved.
  - **Concern ID** R1-m5
  - **Severity** Minor
  - **Axis** Accessibility
  - **Affected element** Introduction section
  - **Evidence pointer** Introduction section, first paragraph
  - **Issue** The introduction assumes familiarity with circuit topology concepts without providing sufficient background for readers outside the immediate field. The relevance of topological descriptions to protein function is not clearly motivated.
  - **Required correction** Provide a brief, accessible introduction to circuit topology and explain why topological analysis may offer advantages over traditional structural descriptors for disordered proteins.

## Technical failings that need to be addressed before the case is established
- R1-M1: CT Folding Score definition and validation are incomplete
- R1-M2: Quantitative evidence for phosphorylation-induced topological changes is not presented
- R1-M3: Simulation convergence and sampling adequacy are not demonstrated
- R1-M4: Force field validation for phosphoserine is lacking

## Risk / unsupported claims
- The claim that the CT Folding Score is "more sensitive" than geometric measures is not supported by quantitative comparison
- The claim of "significant entanglement" in disordered compact states is not backed by any entanglement metric
- The biological implications regarding distinct binding surfaces and selective interactions with regulatory complexes are speculative and not supported by experimental evidence
- The statement that "topologically compact states are stabilized by interactions with phosphoserines" is presented as a conclusion but is based on indirect evidence
- The claim that the framework "can be broadly applied to studying the topological dynamics of disordered proteins" is plausible but not demonstrated beyond the single system studied
- The assertion that the simulations are "not dependent on the choice of our initial conformation" is not adequately supported by the evidence presented

## Assessment against Nature-style criteria
- **Originality** Moderate. The application of circuit topology to disordered protein dynamics is novel, but the underlying concept of phosphorylation modulating disordered protein conformations is well established. The specific combination of approaches is new, but the conceptual advance is incremental.
- **Scientific importance** Moderate. The GR system is biologically relevant, and understanding phosphorylation effects on disordered protein conformations is important. However, the study is primarily computational and the biological implications are not experimentally validated, limiting immediate impact.
- **Interdisciplinary readership** Limited. The work will primarily interest computational biophysicists and IDP researchers. The biological relevance is discussed but not demonstrated, which may limit appeal to a broader biological audience. The methodological aspects may interest polymer physicists but the presentation is not sufficiently accessible.
- **Technical soundness** Not fully established from the provided material. The simulation methodology is standard, but the novel analysis framework (CT Folding Score) lacks rigorous validation. Sampling and convergence are not adequately demonstrated. The NMR validation is partial and deviations are not fully addressed.
- **Readability for nonspecialists** The manuscript is written for a specialized audience. The introduction does not provide sufficient background on circuit topology for readers unfamiliar with the approach. The biological context is presented but the significance of the computational findings for GR function is not made accessible.

## Recommendation posture
Currently not established from the provided evidence. The manuscript presents an interesting conceptual framework and addresses a relevant biological question, but the central methodological contribution requires more rigorous validation and the key biological claims need quantitative support. The authors should be encouraged to resubmit after addressing the major concerns, particularly the validation of the CT Folding Score, demonstration of simulation convergence, and provision of quantitative comparisons between phosphovariants. The biological interpretation should be tempered or supported with additional evidence.