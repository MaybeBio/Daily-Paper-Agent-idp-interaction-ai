## Review setup
- **Input scope** Full manuscript text including abstract, results, methods, and supplementary figure/table references
- **Assessment boundary** Scientific validity of claims, experimental support, technical soundness, and significance of findings as presented in the provided manuscript
- **Shared manuscript claim summary** The authors propose that TSWV nucleocapsid protein (N) recruits host phosphoglycerate kinase (NbPGK) to form phase-separated condensates, which reprogrammes host glycolysis to generate ATP that promotes N protein phase separation and viral proliferation. They further identify a small-molecule compound F10 that binds to N protein residues Arg94, Lys192 and Gly228, disrupts the N-NbPGK interaction, and exhibits antiviral activity superior to Ningnanmycin.
- **Visible evidence base** Results sections covering protein interaction assays (LCA, BiFC), gene silencing experiments, transcriptomics, inhibitor studies, binding affinity measurements (MST, BLI), molecular docking, molecular dynamics simulations, and in planta antiviral assays. Supplementary figures and tables are referenced but not provided.
- **Missing materials affecting confidence** Supplementary figures S1-S11, tables S1-S5, movies S1-S7, and scheme S1 are referenced but not available for review. Raw data, statistical analysis details, and full experimental protocols for several key assays are not provided.

## Reviewer
- **Overall assessment** The manuscript addresses an important and timely question in plant virology, namely how viruses hijack host metabolic enzymes to support phase separation-driven replication. The central hypothesis that TSWV N recruits NbPGK to remodel glycolysis and generate ATP for condensate formation is conceptually novel and potentially significant. However, the evidence presented has several critical gaps. The causal link between NbPGK recruitment, ATP generation, and condensate formation is not rigorously established. The claim that ATP acts as a non-enzymatic regulator of N phase separation is supported only by in silico simulations and correlative in vitro data. The mechanism of action of compound F10, while interesting, lacks direct evidence that its antiviral activity is specifically due to disruption of the N-NbPGK interaction rather than off-target effects. The manuscript would benefit from additional loss-of-function and gain-of-function experiments, quantitative imaging analyses, and a more rigorous statistical framework.
- **Who would be interested in the results, and why** Plant virologists studying tospoviruses and other negative-strand RNA viruses would find the N-NbPGK interaction mechanism of direct relevance. Researchers investigating phase separation in plant-pathogen interactions would be interested in the demonstration that a viral protein recruits a host metabolic enzyme into condensates. The agrochemical community, particularly those developing antiviral compounds against plant viruses, would be interested in F10 as a potential lead compound. The broader cell biology community studying the intersection of metabolism and biomolecular condensates may also find the ATP-dependent regulation of phase separation conceptually interesting.
- **Major strengths** The study addresses a significant gap in understanding how plant viruses exploit host metabolism for replication. The identification of NbPGK as a host factor recruited by TSWV N is novel and provides a mechanistic link between glycolysis and viral condensate formation. The development of F10 as a small-molecule modulator of this process represents a potentially valuable translational outcome. The combination of in vivo interaction assays, transcriptomics, biophysical binding measurements, and computational simulations provides a multi-pronged approach.
- **Major Concerns** See detailed items below.
- **Minor Comments** See detailed items below.
- **Technical failings that need to be addressed before the case is established** R1-M1, R1-M2, R1-M3, R1-M4, R1-M5
- **Assessment against Nature-style criteria** Originality: The concept of a plant virus recruiting a glycolytic enzyme into phase-separated condensates to fuel replication is original and extends beyond prior work on viral protein phase separation. Scientific importance: The findings have potential implications for understanding tospovirus pathogenesis and for developing antiviral strategies, but the importance is currently tempered by incomplete mechanistic evidence. Interdisciplinary readership: The topic bridges virology, plant biology, and biophysics, and would appeal to a broad audience if the claims are fully substantiated. Technical soundness: Several key experiments lack appropriate controls, quantitative rigor, or direct causal evidence. The reliance on correlative data and in silico predictions weakens the technical foundation. Readability for nonspecialists: The manuscript is generally well-written and accessible, though some sections assume familiarity with phase separation concepts and biophysical methods.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Causal link between NbPGK recruitment and condensate formation
- **Claim pointer** The authors claim that NbPGK recruitment by N protein drives condensate formation and that this is essential for viral proliferation.
- **Evidence pointer** Results sections "TSWV N Interacts With the Host Protein Phosphoglycerate Kinase" and "NbPGK-N Interaction Remodels the Host Glycolytic Pathway"; Figures 1 and 2
- **Concern** The manuscript demonstrates that NbPGK interacts with N and that co-expression increases condensate size and number, but does not provide loss-of-function evidence that NbPGK is required for condensate formation. Silencing NbPGK reduces viral accumulation, but the authors do not directly show that this is due to impaired condensate formation rather than a general reduction in host fitness or glycolytic flux. The claim that NbPGK recruitment is a driver of condensate formation requires experiments where NbPGK is depleted or its interaction with N is disrupted, followed by assessment of condensate formation.
- **Why it matters** The central mechanistic claim of the paper is that N hijacks NbPGK to promote condensate formation. Without direct evidence that NbPGK is necessary for this process, the causal relationship remains correlative.
- **Resolution test** Perform NbPGK silencing or knockout in N. benthamiana and assess N condensate formation by confocal microscopy. Alternatively, express N mutants that cannot bind NbPGK and test whether condensate formation is impaired. Quantify condensate number, size, and dynamics under these conditions.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** ATP as a direct regulator of N phase separation
- **Claim pointer** The authors claim that glycolysis-derived ATP promotes N protein phase separation through a non-enzymatic mechanism, based on exogenous ATP application and CGMD simulations.
- **Evidence pointer** Results section "Glycolysis-Derived ATP Promotes N Protein PS"; Figure 4 and Figure S7
- **Concern** The evidence that ATP directly regulates N phase separation is indirect. Exogenous ATP application in planta could have pleiotropic effects on cellular metabolism, stress responses, or other ATP-dependent processes. The in vitro experiments show that ATP enhances condensate formation, but the concentrations used (1-2 mM) are supraphysiological. The CGMD simulations are informative but do not constitute experimental evidence. The authors do not rule out that ATP acts indirectly, for example by affecting protein phosphorylation or other ATP-dependent enzymes.
- **Why it matters** The claim that ATP is a direct, non-enzymatic regulator of N phase separation is a key mechanistic finding. If ATP acts indirectly, the proposed model of glycolytic reprogramming driving condensate formation would need revision.
- **Resolution test** Perform in vitro phase separation assays with purified N protein and ATP at physiologically relevant concentrations, using non-hydrolyzable ATP analogs to distinguish enzymatic from non-enzymatic effects. Test whether ATP depletion in vivo (e.g., by treatment with glycolysis inhibitors) reduces condensate formation in a manner that is rescued by exogenous ATP.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Specificity of F10 mechanism of action
- **Claim pointer** The authors claim that F10 binds to N protein residues Arg94, Lys192 and Gly228, disrupts the N-NbPGK interaction, and thereby inhibits condensate formation and viral replication.
- **Evidence pointer** Results sections "Small-Molecule F10 Significantly Reduces N Protein Condensates and Proper Replication of RNPs by Targeting the N Protein" and "The Absence of Key Binding Sites for F10 to N Protein Significantly Impairs Viral Proliferation In Vivo"; Figures 5 and 6
- **Concern** The evidence that F10 specifically disrupts the N-NbPGK interaction is indirect. The DARTS assay identifies N as a binding target, and molecular docking predicts binding sites, but the authors do not directly demonstrate that F10 disrupts the N-NbPGK complex. The mutant studies show that mutations at the predicted binding sites reduce viral proliferation, but this could be due to effects on N protein stability, folding, or other functions rather than specifically on F10 binding. The claim that F10 liberates NbPGK is not directly tested.
- **Why it matters** The proposed mechanism of F10 action is central to the translational claims of the paper. If F10 acts through a different mechanism, the conclusions about targeting the N-NbPGK interaction would be unsupported.
- **Resolution test** Perform co-immunoprecipitation or pull-down assays to directly test whether F10 disrupts the N-NbPGK interaction in vitro and in planta. Use surface plasmon resonance or isothermal titration calorimetry to measure the effect of F10 on N-NbPGK binding affinity. Test whether F10 affects condensate formation in cells expressing N mutants that cannot bind NbPGK.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** Yes
- **Axis** Statistical rigor and quantification
- **Claim pointer** The authors make quantitative claims about condensate size, number, viral accumulation, and gene expression changes throughout the manuscript.
- **Evidence pointer** Figures 1-7 and associated text
- **Concern** The manuscript lacks clear statistical information for most quantitative comparisons. No effect sizes, confidence intervals, or statistical test details are provided in the main text. The number of biological replicates, technical replicates, and independent experiments is not stated for most assays. The quantification methods for condensate size and number are not described in sufficient detail. The transcriptomics analysis lacks details on differential expression thresholds beyond the stated cutoff.
- **Why it matters** Without proper statistical reporting, the reliability and reproducibility of the quantitative claims cannot be assessed. This is particularly important for the condensate quantification, which is central to the paper's conclusions.
- **Resolution test** Provide full statistical details for all quantitative experiments, including the number of replicates, statistical tests used, and effect sizes. Describe the image analysis pipeline for condensate quantification in detail. Provide access to raw data or a data availability statement that allows independent verification.

- **Concern ID** R1-M5
- **Severity** Major
- **Blocking** Yes
- **Axis** In vivo relevance of the proposed mechanism
- **Claim pointer** The authors claim that the N-NbPGK interaction and glycolytic reprogramming are relevant for natural TSWV infection and that F10 is effective in a natural host.
- **Evidence pointer** Results sections "NbPGK Silencing Weakens TSWV Infection" and "Small-Molecule F10 Significantly Reduces N Protein Condensates and Proper Replication of RNPs by Targeting the N Protein"; Figures 2 and 5
- **Concern** The experiments are performed using transient expression systems and a recombinant TSWV based on a lettuce isolate. The relevance to natural TSWV infection in agronomically important hosts is not fully established. The F10 efficacy is tested in N. glutinosa local lesion assays and in tomato, but the experimental conditions (e.g., timing of application, concentrations) may not reflect field conditions. The manuscript does not address whether NbPGK is differentially expressed or regulated during natural TSWV infection.
- **Why it matters** The translational claims of the paper depend on the relevance of the proposed mechanism to natural infections. If the mechanism only operates under the artificial conditions used here, the significance for disease management would be limited.
- **Resolution test** Validate the N-NbPGK interaction and condensate formation in naturally infected plants. Test F10 efficacy under conditions that more closely mimic field application (e.g., foliar spray, different growth stages). Examine NbPGK expression and glycolytic flux in naturally infected susceptible and resistant hosts.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Figure quality and presentation
- **Affected element** Figures 1-7
- **Evidence pointer** Figures 1-7
- **Issue** Several figures appear to lack scale bars, and the resolution of some confocal images is insufficient to clearly visualise condensate morphology. The figure legends do not consistently state the number of replicates or the statistical tests used.
- **Required correction** Add scale bars to all microscopy images. Provide higher-resolution images where necessary. Ensure all figure legends include information on replicates and statistical analysis.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Terminology consistency
- **Affected element** Throughout the manuscript
- **Evidence pointer** Abstract and Results sections
- **Issue** The terms "condensates," "granules," "inclusions," and "IBs" are used interchangeably throughout the manuscript. This creates confusion about whether the authors are referring to the same structures.
- **Required correction** Use consistent terminology throughout, preferably defining the term "condensate" at first use and using it consistently thereafter.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Control experiments
- **Affected element** Figure 1 and Figure 2
- **Evidence pointer** Figure 1 and Figure 2
- **Issue** The negative controls for LCA and BiFC are described but not shown in the main figures. The specificity of the N-NbPGK interaction would be strengthened by showing these controls.
- **Required correction** Include representative negative control images in the main figures or supplementary material.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Dose-response data
- **Affected element** Figure 3
- **Evidence pointer** Figure 3
- **Issue** The dose-response experiments with 2-DG show effects on condensate formation, but the concentrations used are not justified. It is unclear whether the observed effects are due to specific inhibition of glycolysis or general cellular toxicity.
- **Required correction** Provide cell viability data for the 2-DG concentrations used. Include a discussion of the specificity of 2-DG as a glycolysis inhibitor in plants.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Molecular dynamics simulation details
- **Affected element** Methods section "Molecular Dynamics"
- **Evidence pointer** Methods section
- **Issue** The methods section for molecular dynamics simulations is very brief and lacks critical details such as force field parameters, simulation time, temperature/pressure coupling, and analysis methods.
- **Required correction** Provide a complete description of the simulation parameters and analysis methods, or cite the relevant protocols.

- **Concern ID** R1-m6
- **Severity** Minor
- **Axis** Compound specificity
- **Affected element** Figure 5 and Tables S1-S2
- **Evidence pointer** Figure 5 and Tables S1-S2
- **Issue** The manuscript does not discuss whether F10 has activity against other plant viruses or whether it affects plant growth and development beyond the tested conditions.
- **Required correction** Include a brief discussion of the specificity of F10 and any potential off-target effects.

## Risk / unsupported claims
- The claim that ATP acts as a direct, non-enzymatic regulator of N protein phase separation is not fully supported by the experimental evidence, as the in vivo experiments do not distinguish direct from indirect effects.
- The claim that F10 specifically disrupts the N-NbPGK interaction is not directly demonstrated; the evidence is based on DARTS, docking, and mutant phenotypes, which are correlative.
- The claim that glycolytic reprogramming is a general mechanism for TSWV proliferation is based on experiments with a single viral isolate and transient expression systems, limiting generalizability.
- The claim that F10 outperforms Ningnanmycin is based on a single assay type (local lesion half-leaf assay) and may not reflect efficacy under field conditions.
- The transcriptomics data are presented as supporting glycolytic pathway remodelling, but the full analysis, including validation by qRT-PCR for all key genes and pathway-level statistics, is not shown.
- The in vitro condensate formation experiments lack quantitative analysis of condensate properties (e.g., viscosity, dynamics) that would strengthen the phase separation claim.