## Review setup
- **Input scope** Full manuscript text including abstract, introduction, results, discussion, methods, and supplementary figure references
- **Assessment boundary** Scientific validity of claims, experimental design, data interpretation, and technical soundness based solely on the provided manuscript text
- **Shared manuscript claim summary** The authors propose that the SARS-CoV-2 Envelope (E) protein acts as an "exoregulin" that disrupts calcium homeostasis by interacting with SERCA2b and endogenous regulins (PLN, ALN, ELN), thereby inhibiting SERCA-mediated ER calcium refill and destabilizing ER calcium dynamics.
- **Visible evidence base** FRET-based interaction assays (AP-FRET), calcium imaging experiments (ER-GCaMP6-150), co-localization microscopy, structural docking (PIPER/ClusPro), and molecular dynamics simulations (3 x 500 ns per complex)
- **Missing materials affecting confidence** Supplementary figures S1-S6 are referenced but not provided; raw FRET efficiency values with statistical distributions are not shown; representative microscopy images are not included; MD simulation convergence metrics and force field parameters are only partially described; no information on biological replicates or statistical test details for calcium experiments

## Reviewer
- **Overall assessment** The manuscript addresses a timely and potentially important question regarding the molecular mechanism by which the SARS-CoV-2 E protein perturbs host calcium signaling. The hypothesis that E protein functions as an exoregulin is novel and mechanistically plausible given the structural similarity to regulins. However, the evidence presented is incomplete in several critical respects. The FRET data supporting direct E protein-SERCA2b interaction are not fully quantified or controlled for expression level effects. The calcium imaging experiments lack detailed statistical analysis and do not fully exclude alternative explanations such as indirect effects on IP3 receptor sensitivity or store-operated calcium entry. The computational modeling, while useful for generating hypotheses, is not validated experimentally. The manuscript would benefit from additional experiments including mutagenesis of the proposed interaction interface, dose-response analysis, and verification in a more physiologically relevant cell system.
- **Who would be interested in the results, and why** Virologists studying SARS-CoV-2 pathogenesis, cell biologists investigating calcium signaling regulation, and researchers focused on SERCA regulation and its role in disease. The potential therapeutic implications for severe COVID-19 would also attract interest from translational researchers.
- **Major strengths** The hypothesis is well-formulated and mechanistically grounded in the structural similarity between E protein and regulins. The combination of FRET, functional calcium imaging, and computational modeling provides a multi-pronged approach. The study addresses a clinically relevant question with potential therapeutic implications.
- **Major Concerns** See detailed items below.
- **Minor Comments** See detailed items below.
- **Technical failings that need to be addressed before the case is established** R1-M1 (FRET quantification and controls), R1-M2 (calcium data analysis), R1-M3 (MD simulation validation)
- **Assessment against Nature-style criteria** Originality: The exoregulin concept applied to a viral protein is novel and represents a conceptual advance. Scientific importance: The question of how SARS-CoV-2 E protein perturbs calcium homeostasis is significant for understanding pathogenesis, but the current evidence does not fully establish the proposed mechanism. Interdisciplinary readership: The topic bridges virology, cell biology, and biophysics, which would appeal to a broad audience if the evidence were more complete. Technical soundness: The experimental approaches are appropriate but the execution and analysis have gaps that undermine confidence. Readability for nonspecialists: The manuscript is generally well-written and accessible, though some sections on MD simulations may be challenging for non-computational readers.
- **Recommendation posture** Supportive if technical concerns are resolved. The core hypothesis is interesting and worth pursuing, but the current evidence does not fully establish the proposed mechanism.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence quality
- **Claim pointer** "Using FRET experiments we demonstrate that E protein can form oligomers with regulins, and thus can alter the monomer/multimer regulin ratio and consequently influence their interactions with SERCAs. We also confirmed that a direct interaction between E protein and SERCA2b results in a decrease in SERCA-mediated ER Ca2+ reload."
- **Evidence pointer** Results section, Figures 3 and 4
- **Concern** The FRET data are presented as mean values with significance tests against a soluble control, but the manuscript does not provide the full distribution of FRET efficiencies, the number of cells measured per condition, or the range of expression levels. The authors note that "only E protein tagged at its N-terminal (luminal) end resulted in a stable fluorescent protein," which means the FRET pair is positioned on opposite sides of the membrane. While the authors argue this supports strong interaction, it also complicates interpretation because the orientation may affect FRET efficiency in ways that are not controlled for. Additionally, the comparison between E protein/SERCA and regulin/SERCA FRET values is made without accounting for differences in expression levels or protein stability, which could confound the results.
- **Why it matters** The claim of direct physical interaction between E protein and SERCA2b is central to the manuscript's thesis. Without robust quantification and appropriate controls, the FRET data cannot be considered conclusive evidence of a specific interaction. The lack of expression level normalization is particularly concerning because differences in protein concentration can produce artifactual FRET signals.
- **Resolution test** Provide full FRET efficiency distributions for all conditions, including the number of cells and biological replicates. Include expression level measurements (e.g., western blot or fluorescence intensity) and demonstrate that FRET efficiency is not correlated with expression level. Perform a positive control with a known interacting pair and a negative control with a membrane protein that does not interact with SERCA. Consider using a different FRET approach (e.g., FLIM-FRET) to confirm the interaction.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Data interpretation
- **Claim pointer** "Following ATP administration, significantly lower Ca2+ levels were detected in the presence of E protein than in its absence. In addition, strong switch-like responses corresponding to a sudden depletion of the ER store were observed more frequently in cells expressing E protein than in control cells. These results demonstrated that E protein made ER Ca2+ homeostasis metastable, sensitive to stimuli and depleting easily."
- **Evidence pointer** Results section, Figures 6 and 8
- **Concern** The calcium imaging experiments show differences in ER calcium dynamics between E protein-expressing and control cells, but the analysis is incomplete. The manuscript does not specify the number of cells or independent experiments, the statistical test used, or whether the data were normally distributed. The "switch-like response" is described qualitatively but no quantitative criteria are provided for classifying this response. The re-addition experiment (Figure 8) shows slower ER refill in E protein-expressing cells, but the authors do not exclude the possibility that E protein affects IP3 receptor sensitivity or downstream calcium signaling pathways rather than directly inhibiting SERCA. The statement that "the plasma membrane was intact and the endoplasmic reticulum was emptied under identical conditions" is not supported by data showing membrane integrity or equal loading of the ER calcium sensor.
- **Why it matters** The functional claim that E protein inhibits SERCA-mediated calcium refill is the key physiological conclusion of the study. If the observed effects are due to indirect mechanisms or experimental artifacts, the central thesis would be weakened. The lack of detailed statistical analysis and controls makes it difficult to assess the robustness of the findings.
- **Resolution test** Provide detailed statistical analysis including the number of cells, biological replicates, and the specific test used. Define quantitative criteria for classifying "switch-like" responses. Include controls for IP3 receptor function (e.g., using a membrane-permeant IP3 ester or direct IP3 receptor agonist). Verify plasma membrane integrity using a membrane-impermeant dye. Normalize ER calcium measurements to sensor expression levels.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** "The E protein complex exhibited similar stability as the PLN/SERCA dimer and low fluctuations. The PLN and E protein exhibited overlapping binding sites on SERCA. Both PLN and E protein interacted with SERCA TM2, TM6, and TM9, albeit in a slightly different manner."
- **Evidence pointer** Results section, Figure 5, Supplementary Figures S3 and S4
- **Concern** The MD simulations are used to support the structural model of E protein binding to SERCA, but the manuscript does not provide sufficient details to evaluate the quality of the simulations. The force field parameters, water model, and simulation temperature are mentioned, but no information is given on system size, equilibration criteria, or convergence. The authors state that the E protein pentamer was unstable in simulations, which is consistent with previous reports for regulins, but this raises questions about the physiological relevance of the pentameric form. The docking results from PIPER/ClusPro are not validated experimentally, and the authors do not test whether mutations in the proposed interaction interface disrupt the E protein-SERCA interaction.
- **Why it matters** The structural model is used to support the mechanistic interpretation of the FRET and calcium data. If the simulations are not converged or the docking results are not robust, the structural claims are not reliable. The lack of experimental validation of the proposed interaction interface weakens the overall case.
- **Resolution test** Provide detailed simulation parameters including system size, equilibration protocol, and convergence metrics (e.g., RMSD over time). Validate the docking results with mutagenesis experiments targeting the proposed interaction interface and test the effect on FRET and calcium dynamics. Consider using additional structural prediction methods (e.g., AlphaFold-Multimer) to cross-validate the E protein-SERCA interaction.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Abstract
- **Evidence pointer** Abstract
- **Issue** The abstract states that E protein "can form oligomers with regulins" and "can alter the monomer/multimer regulin ratio," but the functional significance of this hetero-oligomerization is not clearly explained. The abstract also claims "novel links in the host-virus interaction network" without specifying what these links are.
- **Required correction** Clarify the mechanistic significance of E protein-regulin hetero-oligomerization and specify the proposed novel links in the host-virus interaction network.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Data presentation
- **Affected element** Figure 6
- **Evidence pointer** Results section, Figure 6
- **Issue** The three types of cellular responses to ATP are described qualitatively but no representative traces or quantitative criteria are provided. The figure legend does not specify the number of cells or experiments.
- **Required correction** Provide representative calcium traces for each response type and define quantitative criteria for classification. Include the number of cells and independent experiments in the figure legend.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Methodology
- **Affected element** Methods section, calcium measurements
- **Evidence pointer** Methods section
- **Issue** The calcium measurement methods state that "the maximum and minimum values were obtained with 250 μM ionomycin and 2 mM EGTA, respectively, then the signals were normalized between 0 and 1." However, it is not clear whether ionomycin was applied at the end of each experiment or in separate control experiments.
- **Required correction** Clarify the calibration procedure and whether ionomycin was applied to each sample or only to control samples.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Interpretation
- **Affected element** Discussion
- **Evidence pointer** Discussion section
- **Issue** The discussion states that "the delayed viroporin formation is possibly crucial for the virus to avoid early cell death before viral replication," but this is speculative and not supported by data presented in the manuscript.
- **Required correction** Either provide supporting evidence or clearly label this as speculation.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Data availability
- **Evidence pointer** Data availability section
- **Issue** The data availability statement says "Some of our data are available at http://www.hegelab.org/resources.html or upon request." This is vague and does not specify which data are available.
- **Required correction** Specify which data are available at the website and which are available upon request.

## Risk / unsupported claims
- The claim that E protein "can alter the monomer/multimer regulin ratio" is inferred from FRET data but not directly demonstrated. The manuscript does not show that E protein binding to regulins changes the oligomeric state of the regulins.
- The claim that E protein inhibits SERCA-mediated ER calcium refill is supported by the re-addition experiment, but alternative explanations (e.g., effects on IP3 receptor or store-operated calcium entry) are not excluded.
- The structural model of the E protein-SERCA complex is based on docking and MD simulations that are not experimentally validated. The claim of overlapping binding sites with regulins is plausible but not confirmed.
- The statement that "the E protein pore becomes stable only when other viral proteins are also expressed at a sufficient level" is speculative and not supported by data in this manuscript.
- The claim that "the virally reprogrammed Ca2+ signaling can lead to different cell fates" is a general statement not directly tested in this study.