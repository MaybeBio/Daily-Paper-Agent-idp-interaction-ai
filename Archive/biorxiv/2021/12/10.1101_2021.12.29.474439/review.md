## Review setup
- **Input scope** Full manuscript text (Abstract, Introduction, Materials and Methods, Results and Discussion, Conclusion)
- **Assessment boundary** Scientific soundness, methodological rigor, validity of claims based on the provided evidence; no assessment of editorial fit or publication policy
- **Shared manuscript claim summary** The authors claim to capture a "disorder-to-order transition" in the SARS-CoV-2 Spike furin-like cleavage site (FLCS) upon binding to furin, driven by persistent, interchangeable salt-bridges involving arginines R682, R683, R685 and anionic furin residues, with implications for coronavirus pathology and evolution.
- **Visible evidence base** Computational docking (ClusPro, ZDOCK), molecular dynamics simulations (GROMACS, OPLS-AA, 300 ns and 100 ns trajectories), Ramachandran plot analyses, FoldX thermodynamic calculations, sequence-based disorder predictions
- **Missing materials affecting confidence** Supplementary figures, tables, and video referenced but not provided; no experimental validation data; no raw simulation trajectories or convergence metrics; no force field validation details; no error estimates for thermodynamic quantities

## Reviewer

- **Overall assessment** This manuscript presents a computational study of the SARS-CoV-2 spike furin cleavage site dynamics upon furin binding. The central claim of a disorder-to-order transition driven by persistent salt-bridges is plausible but the evidence provided is largely qualitative and derived from a single docking pose with limited cross-validation. The study lacks experimental validation, and several methodological details are insufficiently described to assess robustness. The novelty is moderate, building on known observations of furin cleavage site disorder, though the specific salt-bridge network analysis and Ramachandran-based metrics offer some new angles. The manuscript would benefit from substantial revision, additional controls, and clearer presentation of quantitative results.

- **Who would be interested in the results, and why** Structural biologists and computational biophysicists studying protein-protein interactions, intrinsically disordered regions, and protease-substrate recognition. Virologists interested in SARS-CoV-2 entry mechanisms and furin cleavage may also find the salt-bridge network analysis relevant. The methodological demonstration of Ramachandran plot-derived metrics for probing disorder-to-order transitions could interest method developers in the computational structural biology community.

- **Major Strengths**
  1. The study addresses a relevant and timely question regarding the molecular basis of furin cleavage efficiency in SARS-CoV-2, which has implications for understanding viral entry and pathogenesis.
  2. The combination of ensemble docking, MD simulations, and multiple analytical approaches (salt-bridge persistence, Ramachandran metrics, thermodynamic calculations) provides a multi-faceted computational perspective.
  3. The inclusion of a SARS-CoV baseline comparison is appropriate and helps contextualize the SARS-CoV-2-specific features.
  4. The authors demonstrate awareness of the disordered nature of the FLCS and attempt to quantify the transition using multiple complementary metrics.

- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors claim that the "disorder-to-order transition" of the FLCS is "triggered and sustained by highly persistent interchangeable salt-bridge dynamics" at the Spike–Furin interface.
- **Evidence pointer** Section 3.6, Table 1, Figure 3
- **Concern** The central claim rests on salt-bridge persistence values derived from a single 300 ns MD simulation of one docking pose (RR1 CoV-2). The persistence values (e.g., 0.93, 0.85, 0.90) are presented as evidence of stable interactions, but no error estimates, replicate simulations, or convergence analyses are provided. The choice of a single trajectory to support a mechanistic claim of this strength is insufficient. Additionally, the force field (OPLS-AA) is known to have biases in salt-bridge stability, and no comparison with alternative force fields or enhanced sampling methods is presented.
- **Why it matters** The central mechanistic claim of the paper depends entirely on the stability and reproducibility of these salt-bridge interactions. Without replicate simulations, convergence assessment, or force field validation, the persistence values cannot be distinguished from stochastic fluctuations or force field artifacts. This undermines the primary conclusion.
- **Resolution test** Provide at least three independent replicate simulations with different initial velocities, demonstrate convergence of salt-bridge persistence values, and show that the key salt-bridges are robust to force field choice (e.g., AMBER, CHARMM) or enhanced sampling approaches. Alternatively, temper the claim to reflect the preliminary nature of single-trajectory observations.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors claim that the Ramachandran plot-derived parameters demonstrate a statistically significant disorder-to-order transition upon furin binding, with a chi-square value of 3650.32 (df=9).
- **Evidence pointer** Section 3.8, Table 4, Figure 7
- **Concern** The chi-square test compares the distribution of (phi, psi) points between unbound and bound states, but the statistical validity of this test is questionable. The Ramachandran points from MD trajectories are highly autocorrelated (sampled every 10 ps from a continuous trajectory), violating the independence assumption of the chi-square test. The effective sample size is far smaller than the nominal number of snapshots, inflating the chi-square statistic. Additionally, the choice of 10 bins appears arbitrary, and no sensitivity analysis is provided.
- **Why it matters** The statistical significance claim (at the 99.9% level) is a key quantitative support for the disorder-to-order transition. If the test is statistically invalid due to autocorrelation, the significance claim is unsupported, weakening the central conclusion.
- **Resolution test** Account for temporal autocorrelation in the Ramachandran data (e.g., using block averaging, effective sample size estimation, or decorrelation time-based subsampling). Provide a sensitivity analysis for bin number and boundaries. Alternatively, use a more appropriate statistical framework for comparing distributions from correlated trajectories.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Scientific importance
- **Claim pointer** The authors state that their findings "offer novel mechanistic insights into the coronavirus molecular pathology and evolution" and that the disorder-to-order transition "should find its place at the very heart of the coronavirus molecular pathology."
- **Evidence pointer** Abstract, Section 4
- **Concern** The manuscript overstates the significance of purely computational findings without experimental validation. The claim that this transition is at the "heart" of coronavirus pathology is speculative and not supported by the data presented. The study demonstrates a plausible computational model, but no experimental evidence links the proposed salt-bridge networks to actual furin cleavage efficiency, viral entry, or pathogenicity. The connection to "evolution" is also asserted without phylogenetic or functional validation.
- **Why it matters** Overstated claims can mislead readers and the broader scientific community, particularly in a high-stakes area like COVID-19 research. The distinction between computational prediction and experimentally validated mechanism must be clear.
- **Resolution test** Temper the language throughout to reflect the computational and predictive nature of the findings. Add explicit statements about the need for experimental validation. If possible, include any available experimental data (e.g., cleavage assays, mutagenesis) to support the claims.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Technical soundness
- **Claim pointer** The authors claim that the docking approach was "blind" and unbiased, and that the top-ranked pose (RR1 CoV-2) represents the most plausible binding mode.
- **Evidence pointer** Section 2.3, Section 3.4
- **Concern** The description of the docking protocol is incomplete. The authors state that ClusPro was used for "blind docking" but do not provide details on the scoring function parameters, the number of poses generated per model, the clustering parameters, or the criteria for selecting the top pose. The use of 500 different receptor conformations (from the ensemble modeling) with docking performed on each is mentioned, but the aggregation of results across this ensemble is not clearly described. The ZDOCK cross-validation is mentioned but the degree of agreement between the two methods is not quantified.
- **Why it matters** Docking results are highly sensitive to protocol choices. Without detailed methodology, the reproducibility of the docking results is questionable, and the selection of the "top-ranked" pose may be arbitrary or biased.
- **Resolution test** Provide complete docking parameters, including scoring function details, clustering thresholds, and pose selection criteria. Quantify the agreement between ClusPro and ZDOCK results (e.g., RMSD between top poses, rank correlation). Describe how results were aggregated across the 500-member ensemble.

- **Concern ID** R1-M5
- **Severity** Major
- **Blocking** No
- **Axis** Technical soundness
- **Claim pointer** The authors claim that FoldX-derived thermodynamic parameters show enthalpy-entropy compensation accompanying the Spike–Furin binding, with the binding free energy being "mildly disfavored" (positive).
- **Evidence pointer** Section 3.7, Table 2, Figure 6
- **Concern** The FoldX calculations are performed on MD trajectory snapshots, but the methodology for selecting snapshots, the equilibration status of the system, and the treatment of solvent effects are not described. FoldX is a knowledge-based potential with known limitations for absolute free energy calculations, particularly for protein-protein interactions involving disordered regions. The claim of "enthalpy-entropy compensation" is inferred from the opposing signs of enthalpy and entropy terms, but no statistical analysis or error propagation is provided. The positive Delta G binding values are interpreted as "metastability," but this interpretation is speculative.
- **Why it matters** Thermodynamic claims require rigorous methodology and error analysis. If the FoldX calculations are not properly validated or the errors are large, the thermodynamic interpretation is unreliable, and the "metastability" conclusion is unsupported.
- **Resolution test** Provide details on FoldX calculation settings, snapshot selection, and equilibration. Include error estimates (e.g., standard errors from block averaging). Validate the FoldX approach against known binding affinities or alternative methods (e.g., MM-PBSA, TI). Temper the interpretation of positive Delta G values.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Readability
- **Affected element** Introduction, Section 1
- **Evidence pointer** Paragraphs 1-3
- **Issue** The introduction contains extensive discussion of the COVID-19 origin debate and "gain of function" research, which is tangential to the scientific content of the study. This material appears to be included for narrative impact rather than scientific necessity and may distract from the actual research questions.
- **Required correction** Significantly condense the origin debate discussion and focus the introduction on the scientific rationale: why the disorder-to-order transition of the FLCS matters for understanding furin cleavage, and what is currently unknown.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Technical soundness
- **Affected element** Section 2.2, Modeling of disordered loops
- **Evidence pointer** Paragraph on MODELLER ensemble generation
- **Issue** The description of the ensemble modeling states that 500 models were generated but does not specify the criteria for model selection, the scoring function used for ranking, or the diversity of the resulting ensemble. The statement that the "lowest energy model" was retained for SARS-CoV but an ensemble approach was used for SARS-CoV-2 is inconsistent and not justified.
- **Required correction** Clarify the model selection criteria for both systems. Justify the different approaches (single model vs. ensemble) or use a consistent methodology. Provide measures of ensemble diversity (e.g., pairwise RMSD distribution).

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Technical soundness
- **Affected element** Section 2.4, MD simulation parameters
- **Evidence pointer** Paragraph on simulation setup
- **Issue** The simulation protocol is described but key parameters are missing: the thermostat and barostat coupling constants, the integration time step, the treatment of long-range interactions beyond PME, the equilibration criteria, and the criteria for determining that "the system showed convergence." The choice of 300 ns as "sufficiently long" is not justified.
- **Required correction** Provide complete simulation parameters. Include convergence metrics (e.g., RMSD plateau, energy drift, block-averaged property stability). Justify the simulation length based on the system dynamics.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Scientific importance
- **Affected element** Section 3.6, Table 1
- **Evidence point** Salt bridge persistence values
- **Issue** The salt bridge analysis identifies specific residue pairs but does not discuss whether these interactions are conserved across SARS-CoV-2 variants or other coronaviruses beyond the single SARS-CoV comparison. The evolutionary implications claimed in the conclusion are not supported by the data presented.
- **Required correction** Either add a conservation analysis across available coronavirus sequences/structures or temper the evolutionary claims to what the current data can support.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Readability
- **Affected element** Section 3.8, Figure 7
- **Evidence point** Ramachandran plot analysis
- **Issue** The description of the Ramachandran plot analysis is dense and difficult to follow. The distinction between the "scattered points representation" and the "line-drawing" approach is unclear, and the interpretation of the chi-square test results is presented without sufficient context for readers unfamiliar with this type of analysis.
- **Required correction** Clarify the methodology and provide a more accessible explanation of what the Ramachandran plot metrics mean physically. Consider moving some technical details to a methods supplement.

- **Concern ID** R1-m6
- **Severity** Minor
- **Axis** Technical soundness
- **Affected element** Section 2.6, FoldX calculations
- **Evidence point** Thermodynamic parameter calculations
- **Issue** The manuscript states that FoldX was used to calculate thermodynamic parameters but does not specify which FoldX energy terms were included, how the "unbound" states were defined (separated monomers vs. ensemble averages), or whether the calculations were performed on the full complex or on specific interface regions.
- **Required correction** Provide complete details of the FoldX protocol, including the specific energy terms, the definition of bound and unbound states, and the treatment of the glycan modifications present in the spike protein.

- **Concern ID** R1-m7
- **Severity** Minor
- **Axis** Readability
- **Affected element** Throughout
- **Evidence point** Writing style
- **Issue** The manuscript contains numerous typographical errors, grammatical issues, and awkward phrasings (e.g., "entrap" used repeatedly, inconsistent use of tense, missing articles). Some sentences are overly long and difficult to parse. The writing would benefit from professional editing.
- **Required correction** Thorough proofreading and editing for grammar, clarity, and conciseness. Consider restructuring long sentences and ensuring consistent terminology throughout.

- **Concern ID** R1-m8
- **Severity** Minor
- **Axis** Scientific importance
- **Affected element** Section 3.7, Figure 6
- **Evidence point** Enthalpy-entropy compensation analysis
- **Issue** The comparison between SARS-CoV and SARS-CoV-2 thermodynamic parameters is presented as evidence of evolutionary optimization, but the differences could also arise from methodological artifacts (different simulation lengths, different starting structures, different numbers of salt bridges). The authors do not address alternative explanations for the observed differences.
- **Required correction** Discuss alternative interpretations of the observed thermodynamic differences. If possible, perform additional control calculations to rule out methodological artifacts.

## Risk / unsupported claims
- The claim that the disorder-to-order transition is "at the very heart of the coronavirus molecular pathology" is unsupported by the computational evidence presented; no experimental validation links the observed salt-bridge dynamics to actual furin cleavage efficiency or pathogenicity.
- The claim of "highly persistent" salt bridges is based on a single MD trajectory without replicate simulations or convergence analysis; persistence values cannot be distinguished from stochastic fluctuations.
- The chi-square test for the significance of the disorder-to-order transition is statistically invalid due to autocorrelation in the trajectory data, making the reported significance level (99.9%) unreliable.
- The claim that the findings "add substantially to the existing theories of proteolytic cleavages" is overstated; the study provides a computational model but no new general theory of proteolysis.
- The evolutionary implications drawn from the SARS-CoV vs SARS-CoV-2 comparison are speculative; no phylogenetic or functional data support the claim of "gain of function" optimization.
- The thermodynamic parameters (Delta G, Delta H, Delta S) are presented without error estimates, making quantitative comparisons between systems unreliable.
- The statement that the furin cleavage site is "absent in other related respiratory viruses" is presented as established fact but is not systematically verified across the relevant viral families in this manuscript.
- The claim that the study is "the first" to report this disorder-to-order transition is not verifiable from the provided reference list and should be tempered.