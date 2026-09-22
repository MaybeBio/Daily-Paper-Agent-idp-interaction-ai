## Review setup
- **Input scope** Full manuscript text, including abstract, introduction, results, discussion, materials and methods, and supplementary information descriptions.
- **Assessment boundary** Scientific content, experimental design, data interpretation, and claims as presented in the provided text. No external data or unpublished materials were consulted.
- **Shared manuscript claim summary** The authors characterize recruitment and diffusion of 18 guest proteins in p53 liquid droplets using single-molecule fluorescence microscopy and coarse-grained molecular dynamics simulations. They report that recruitment correlates moderately with protein length, total charge, and R+Y residue number, independent of structural class, while diffusion depends on structural class, with folded proteins diffusing faster and more heterogeneously than intrinsically disordered proteins.
- **Visible evidence base** Main text figures 1–6, Table 1, and references to Supplementary Figures S1–S3, Supplementary Videos S1–S3, and Supplementary Methods. Quantitative data are presented as mean ± standard error for experimental measurements and mean ± standard deviation for simulations.
- **Missing materials affecting confidence** Supplementary figures and videos were not provided for direct inspection. Raw single-molecule trajectories, statistical test outputs, simulation parameter details, and the full simulation methodology are not available in the reviewed text. The exact number of droplets analyzed per condition and the criteria for droplet selection are not stated.

## Reviewer
- **Overall assessment** This manuscript addresses a timely and important question in the field of liquid–liquid phase separation: what molecular features govern the recruitment and dynamics of guest proteins in condensates. The experimental design is systematic, using a panel of 18 guest proteins spanning different sizes, structures, and oligomeric states, and the combination of single-molecule tracking with coarse-grained simulations is a strength. The main conclusions, that recruitment depends on the number of interaction-capable residues rather than structural class, and that folded versus disordered guests exhibit distinct diffusion regimes, are plausible and potentially useful. However, several technical and interpretive issues reduce confidence in the strength of the claims. The correlation analysis is based on a small and heterogeneous dataset, the distinction between "moderate" and "high" recruitment is not rigorously defined, and the simulation model, while reasonable, is simplified and may not capture the full complexity of host–guest interactions. The manuscript would benefit from additional statistical rigor, clearer reporting of experimental replication, and a more cautious interpretation of the correlation results.
- **Who would be interested in the results, and why** Researchers studying biomolecular condensates, membraneless organelles, and phase separation, particularly those interested in the molecular grammar of protein recruitment and mobility within droplets. The findings may also be relevant to those designing synthetic condensates or engineering proteins for targeted localization. The methodological approach, combining single-molecule imaging with coarse-grained simulations, will be of interest to biophysicists and computational biologists working on intracellular organization.
- **Major strengths** 1) Systematic experimental design using a diverse panel of guest proteins with varying size, charge, structure, and oligomeric state. 2) Direct measurement of both recruitment (via enrichment index) and dynamics (via single-molecule diffusion) in the same system. 3) Integration of experimental observations with coarse-grained molecular dynamics simulations to provide a mechanistic interpretation. 4) The finding that recruitment is independent of structural class while diffusion is not is a potentially important distinction. 5) The use of DNA fragments with defined affinities as an orthogonal validation of the host–guest interaction hypothesis.
- **Major Concerns**
  - **Concern ID** R1-M1
  - **Severity** Major
  - **Blocking** Yes
  - **Axis** Statistical rigor and data interpretation
  - **Claim pointer** The authors claim "moderate correlations" between enrichment index and protein length, total charge, and R+Y number, with correlation coefficients of 0.69, 0.66, and 0.68, respectively.
  - **Evidence pointer** Figure 3A–C, Table 1
  - **Concern** The correlation analysis is performed on a dataset of only 18 guest proteins, which includes both folded and disordered proteins, mutants of the host p53, and proteins of widely varying sizes. The correlation coefficients are reported without confidence intervals or p-values. With n=18, a correlation coefficient of approximately 0.66–0.69 corresponds to a p-value of roughly 0.002–0.001, which is significant, but the small sample size and the presence of potential outliers (e.g., dCas9 with high R+Y and high EI) could inflate the correlation. More importantly, the authors do not perform a multiple regression or partial correlation analysis to disentangle the effects of length, charge, and R+Y, which are likely correlated with each other. The claim that "electrostatic and cation–π interactions participate in guest protein recruitment" is supported only by univariate correlations, which is insufficient to establish independent contributions.
  - **Why it matters** The central claim of the paper is that specific molecular features predict recruitment. If the correlations are not robust or if the variables are confounded, the proposed "molecular grammar" is not established. The lack of statistical rigor undermines the generalizability of the conclusion.
  - **Resolution test** Provide p-values and confidence intervals for all correlation coefficients. Perform a multiple linear regression with length, total charge, and R+Y as independent variables to assess their independent contributions. Report the results of a sensitivity analysis excluding potential outliers. If the sample size is too small for multiple regression, acknowledge this limitation explicitly and temper the conclusion.
  - **Concern ID** R1-M2
  - **Severity** Major
  - **Blocking** Yes
  - **Axis** Experimental design and controls
  - **Claim pointer** The authors state that "Recruitment did not significantly depend on the structural properties of the guest proteins" and that folded proteins have "a wide range of recruitment capabilities."
  - **Evidence pointer** Figure 2A–D, Table 1
  - **Concern** The comparison between folded and disordered proteins is confounded by the fact that the two groups differ systematically in other properties. The disordered proteins tested include p53 mutants, which are derived from the host and may have specific interactions, and poly-R and poly-D, which are homopolymers. The folded proteins include DNA-binding proteins, fluorescent proteins, and enzymes. The groups are not matched for size, charge, or oligomeric state. For example, the largest folded protein (dCas9, 1371 AA) has the highest EI among folded proteins, while the smallest disordered protein (poly-R, 200 AA) has a moderate EI. It is therefore not possible to conclude that structural class per se does not influence recruitment. A more appropriate comparison would involve a matched set of folded and disordered proteins of similar length and charge.
  - **Why it matters** The conclusion that structural class is not a determinant of recruitment is a key finding of the paper. If this conclusion is based on a confounded comparison, it may be incorrect. The claim has implications for understanding the molecular grammar of condensates and for predicting which proteins will be recruited.
  - **Resolution test** Either provide a matched set of folded and disordered proteins with similar length, charge, and oligomeric state, or explicitly acknowledge the confounding variables and discuss how they might affect the interpretation. Alternatively, perform a statistical analysis that controls for these variables, such as an analysis of covariance.
  - **Concern ID** R1-M3
  - **Severity** Major
  - **Blocking** No
  - **Axis** Simulation model validity
  - **Claim pointer** The authors use coarse-grained simulations to conclude that "folded proteins diffuse within the voids of the liquid droplet while interacting weakly with neighboring host proteins, whereas disordered proteins adapt their structures to form tight interactions with the host proteins."
  - **Evidence pointer** Figure 6A–C, Methods section on simulations
  - **Concern** The simulation model is highly simplified. The host p53 is represented with folded domains as single spheres and disordered regions as flexible chains with one bead per residue. The guest proteins are modeled with varying levels of detail, but the folded guests are represented as rigid bodies. The interaction potentials are limited to electrostatic and hydrophobic terms, with no explicit representation of hydrogen bonding, cation–π interactions, or specific side-chain chemistry. The simulation temperature is set to T=0.4, which is described as below the critical temperature, but the relationship between this reduced temperature and the experimental conditions (25 μM p53, 150 mM NaCl, 100 mg/mL dextran) is not established. The conclusion that folded proteins diffuse in "voids" is an interpretation of the simulation trajectories, but the authors do not provide a quantitative analysis of void sizes or the frequency of void encounters. The claim that disordered proteins "adapt their structures" is also not directly demonstrated; the simulations show that they have stronger intermolecular energies, but this does not necessarily imply structural adaptation.
  - **Why it matters** The simulation results are used to provide a mechanistic explanation for the experimental observations. If the model is too simplified or if the interpretation of the simulation output is not rigorous, the proposed mechanism is speculative. This weakens the overall impact of the paper.
  - **Resolution test** Provide a more detailed validation of the simulation model against experimental data, such as comparing simulated and experimental diffusion coefficients. Quantify the void sizes in the condensate and the frequency with which folded proteins are located in voids. Provide a direct measure of structural adaptation in the disordered proteins, such as changes in radius of gyration or contact maps. Discuss the limitations of the model more explicitly.
  - **Concern ID** R1-M4
  - **Severity** Major
  - **Blocking** No
  - **Axis** Quantitative reporting and reproducibility
  - **Claim pointer** The authors report diffusion coefficients for guest proteins in droplets (Table 1) and state that "the diffusion of disordered guest proteins was comparable to that of host p53, whereas that of folded proteins varied widely."
  - **Evidence pointer** Table 1, Figure 5A–D, Methods section on single-molecule measurements
  - **Concern** The diffusion coefficients are reported as mean ± standard error, but the number of molecules tracked, the number of droplets analyzed, and the number of independent experiments are not stated. The tracking method is described briefly, but the criteria for selecting trajectories (at least six consecutive points) and the method for calculating D from MSD plots are not fully detailed. The authors state that "we selected trajectories with at least six consecutive points," but the total number of trajectories per condition is not given. The heterogeneity of diffusion is shown in Supplementary Figure S3, but this figure was not provided for review. Without this information, it is not possible to assess the reliability of the diffusion measurements or to reproduce the experiments.
  - **Why it matters** Reproducibility is a core requirement for scientific publication. The lack of detailed reporting on the number of replicates, the number of molecules analyzed, and the statistical methods used makes it difficult to evaluate the robustness of the findings. This is particularly important given the wide range of diffusion coefficients reported for folded proteins.
  - **Resolution test** Provide the number of independent experiments, the number of droplets analyzed, and the number of trajectories per condition. Describe the statistical methods used to compare diffusion coefficients between conditions. Provide the full details of the tracking algorithm and the MSD fitting procedure. Make the raw data and analysis code available.
- **Minor Comments**
  - **Concern ID** R1-m1
  - **Severity** Minor
  - **Axis** Clarity of presentation
  - **Affected element** Figure 1D
  - **Evidence pointer** Figure 1D, Results section
  - **Issue** The statistical comparison between the EI values of p53 tetramer, dimer, and monomer mutants is described only as "significant difference... confirmed using Welch's t test with α=0.05." It is not clear which specific pairs were compared and whether multiple comparison corrections were applied.
  - **Required correction** Specify which pairs were compared and report the p-values. If multiple comparisons were made, state the correction method used.
  - **Concern ID** R1-m2
  - **Severity** Minor
  - **Axis** Terminology
  - **Affected element** "Guest proteins" and "host proteins"
  - **Evidence pointer** Throughout the manuscript
  - **Issue** The terms "host" and "guest" are used throughout, but the definition is not explicitly stated in the introduction. The reader is left to infer that "host" refers to the scaffold protein that forms the droplet and "guest" refers to proteins that partition into it. This is a common usage, but an explicit definition would improve clarity.
  - **Required correction** Add a sentence in the introduction defining "host" and "guest" proteins in the context of liquid–liquid phase separation.
  - **Concern ID** R1-m3
  - **Severity** Minor
  - **Axis** Data presentation
  - **Affected element** Table 1
  - **Evidence pointer** Table 1
  - **Issue** The table lists "Total charge" as a single column, but the text states that this is the number of R, K, D, and E residues. It would be clearer to specify the exact calculation in the table footnote.
  - **Required correction** Add a footnote to Table 1 stating that "Total charge" is calculated as the sum of R, K, D, and E residues.
  - **Concern ID** R1-m4
  - **Severity** Minor
  - **Axis** Completeness of methods
  - **Affected element** Dextran concentration
  - **Evidence pointer** Methods section on recruitment measurements
  - **Issue** The recruitment measurements use 100 mg/mL dextran, but the molecular weight of the dextran is not specified. Dextran of different molecular weights can have different crowding effects.
  - **Required correction** Specify the molecular weight of the dextran used.
  - **Concern ID** R1-m5
  - **Severity** Minor
  - **Axis** Interpretation of DNA recruitment data
  - **Affected element** Figure 3D
  - **Evidence pointer** Figure 3D, Results section
  - **Issue** The DNA recruitment data are used to support the role of host–guest interactions in recruitment, but the DNA fragments are not proteins and may not be directly comparable. The authors should clarify whether the DNA results are intended as a general validation of the interaction hypothesis or as a specific test of p53–DNA interactions.
  - **Required correction** Clarify the purpose of the DNA experiments in the text.
- **Technical failings that need to be addressed before the case is established** R1-M1 (statistical rigor of correlation analysis), R1-M2 (confounded comparison of folded and disordered proteins), R1-M3 (simulation model validation and interpretation), R1-M4 (incomplete reporting of experimental replication and methods).
- **Assessment against Nature-style criteria**  
  *Originality*: The question of what determines guest protein recruitment and dynamics in condensates is timely, and the systematic experimental approach is valuable. However, the finding that cation–π and electrostatic interactions are important is not entirely novel, as similar conclusions have been drawn in other systems. The distinction between recruitment and dynamics, and the observation that these are governed by different factors, is a potentially original contribution.  
  *Scientific importance*: Understanding the molecular grammar of condensates is of high importance for the field of phase separation and for understanding cellular organization. The results could inform predictions about which proteins are recruited to condensates and how they move within them. However, the limitations in statistical rigor and experimental design reduce the strength of the conclusions.  
  *Interdisciplinary readership*: The topic is of interest to biophysicists, cell biologists, and computational biologists. The combination of experimental and computational approaches broadens the appeal. However, the manuscript assumes familiarity with phase separation concepts and single-molecule techniques, which may limit accessibility to a general audience.  
  *Technical soundness*: The experimental methods are generally appropriate, but the lack of detailed reporting on replication and statistical analysis is a concern. The simulation model is simplified, and the interpretation of simulation results is not fully rigorous.  
  *Readability for nonspecialists*: The manuscript is generally well-written, but the results section is dense and would benefit from clearer explanations of the key findings. The figures are informative, but the text could be more accessible.
- **Recommendation posture** Supportive if technical concerns are resolved. The manuscript addresses an important question and presents a systematic dataset that could be valuable to the field. However, the statistical rigor of the correlation analysis, the confounding of structural class with other variables, and the lack of detailed reporting on experimental replication must be addressed. The simulation results, while suggestive, require more careful validation and interpretation. If these issues are resolved, the manuscript could make a solid contribution.

## Risk / unsupported claims
- The claim that "recruitment did not significantly depend on the structural properties of the guest proteins" is not fully supported due to confounding variables between the folded and disordered protein groups.
- The claim that "electrostatic and cation–π interactions participate in guest protein recruitment" is based on univariate correlations without controlling for confounding variables or providing statistical significance levels.
- The mechanistic interpretation that "folded proteins diffuse within the voids of the liquid droplet while interacting weakly with neighboring host proteins, whereas disordered proteins adapt their structures to form tight interactions" is based on simplified simulations and is not directly validated by experimental data.
- The statement that "the diffusion of disordered guest proteins was comparable to that of host p53" is based on a small number of disordered proteins, some of which are p53 mutants, and may not be generalizable.
- The claim that "strong host–guest interactions slow diffusion" is inferred from a limited dataset and requires additional experimental support.