## Review setup
- **Input scope** Full manuscript text (abstract, introduction, methods, results, discussion, conclusion) as provided
- **Assessment boundary** Scientific content, experimental design, data interpretation, and claims as presented in the provided text; no supplementary figures or tables were available for direct inspection
- **Shared manuscript claim summary** The authors report recombinant production and biophysical characterization of Drosophila melanogaster Polycomb (Pc) protein as an MBP fusion, presenting evidence for intrinsic disorder outside the chromodomain, buffer-dependent stability, concentration-dependent self-oligomerization into high-molecular-weight assemblies, and conditional folding upon oligomerization, supported by SEC-MALS, DLS, nanoDSF, CD, cryo-EM, and AlphaFold3 predictions
- **Visible evidence base** Text descriptions of results from ProtParam analysis, SDS-PAGE, Western blot, SEC-MALS, DLS, nanoDSF, CD spectroscopy, cryo-EM, and AF3 modeling; references to Figures 1-7 and Tables 1-4, and Supplementary Figures S2-S5, none of which were directly viewable
- **Missing materials affecting confidence** All figures, tables, and supplementary information; raw data for SEC-MALS, DLS, nanoDSF, CD, and cryo-EM; experimental details for expression and purification (deferred to Supplementary Information); NMR and crystallization data referenced but not shown

## Reviewer
- **Overall assessment** The manuscript addresses a technically challenging and biologically relevant problem: the structural characterization of a largely disordered protein that is a core component of PRC1. The authors have generated a recombinant Pc-MBP fusion protein and applied a commendable range of biophysical techniques to characterize its behavior in solution. The central claims, however, rest on evidence that is described only in text and referenced to figures that were not available for review. The most significant issue is the apparent discrepancy between the SEC-MALS data (reporting a ~7.5 MDa assembly) and the cryo-EM data (which, by the authors' own account, did not reveal such large particles without cross-linking). The manuscript would be strengthened by a more critical interpretation of this discrepancy and by direct comparison of the AF3 predictions with experimental data. The work is potentially useful as a methodological framework for studying disordered, self-associating proteins, but the biological conclusions regarding Pc function in Polycomb-mediated regulation remain speculative at this stage.

- **Who would be interested in the results, and why** Researchers studying Polycomb group proteins, intrinsically disordered proteins, and phase separation in chromatin regulation would find this work relevant. The methodological approach combining fusion-protein expression, biophysical characterization, and AI-based structure prediction could also be of interest to structural biologists working on challenging protein targets. However, the lack of high-resolution structural data limits the broader appeal to the structural biology community.

- **Major strengths**
  1. The study tackles a genuinely difficult target: a protein with intrinsic disorder and self-association propensity, which has been refractory to structural characterization.
  2. The combination of multiple orthogonal biophysical techniques (nanoDSF, DLS, SEC-MALS, CD, cryo-EM) is appropriate and comprehensive for the questions asked.
  3. The authors are appropriately cautious in several places, acknowledging limitations of AF3 predictions for IDRs and the challenges of sample heterogeneity in cryo-EM.
  4. The use of GraFix to stabilize weak interactions is a thoughtful methodological choice.

- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence sufficiency
- **Claim pointer** The manuscript claims that SEC-MALS demonstrates Pc-MBP forms "high molecular weight oligomers" with an average molar mass of 7.49 x 10^6 g/mol, corresponding to approximately 100 subunits.
- **Evidence pointer** Results section "Oligomeric State Determined by SEC-MALS", Figure 4, Table 2
- **Concern** The SEC-MALS result is presented as the key evidence for self-oligomerization, but the figure and table are not available for inspection. The claim of a ~7.5 MDa species is extraordinary for a protein whose monomer is ~88 kDa (Pc-MBP), and the authors do not discuss whether this species could represent non-specific aggregation rather than a defined oligomer. The reported Mw/Mn of 1.147 suggests relative uniformity, but the Mz/Mn of 1.552 indicates a significant high-mass tail. The authors do not report whether the oligomer dissociates upon dilution, which would be a critical test of specific versus non-specific assembly.
- **Why it matters** The central claim of the paper, that Pc self-oligomerizes into defined higher-order assemblies, rests on this SEC-MALS result. If the 7.5 MDa species is non-specific aggregation, the biological interpretation collapses. The authors must provide evidence that this species is a specific, reversible assembly.
- **Resolution test** Provide the SEC-MALS elution profile and molar mass distribution plot. Include a concentration-dependence study showing that the oligomeric species dissociates upon dilution, and a discussion of the expected stoichiometry. If the species is non-specific, the claim of defined oligomerization must be revised.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Internal consistency
- **Claim pointer** The manuscript states that cryo-EM "reveals pronounced conformational and oligomeric heterogeneity" and that GraFix partially stabilizes larger assemblies, but also states that "cryo-EM analysis of purified Pc in the absence of crosslinking did not reveal the large oligomeric particles (~7 MDa) detected by DLS and SEC-MALS."
- **Evidence pointer** Results section "AF and Cryo-EM Insights into Pc Self-Oligomerization", Figure 7
- **Concern** This is a critical internal inconsistency. The SEC-MALS data indicate a dominant ~7.5 MDa species in solution, yet cryo-EM of the same sample does not show such particles. The authors attribute this to "partial dissociation during grid preparation," but this explanation is not supported by any control experiments. If the 7.5 MDa species is the dominant solution species, one would expect at least some of these particles to survive vitrification. The discrepancy suggests that the SEC-MALS species may be an artifact of the column or light-scattering analysis, or that the cryo-EM grid preparation conditions (e.g., blotting, dilution) disrupt the assembly.
- **Why it matters** The manuscript claims to provide "initial experimental evidence that Pc can form self-associated assemblies," but the two primary techniques used to support this claim are in direct conflict. Without a resolution of this discrepancy, the central conclusion is not established.
- **Resolution test** Provide side-by-side characterization of the same sample by SEC-MALS and cryo-EM under identical buffer conditions. Include negative-stain EM or native mass spectrometry as an orthogonal method to confirm the oligomeric state. If the discrepancy persists, the authors must provide a rigorous explanation supported by data.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Interpretive caution
- **Claim pointer** The manuscript states that "AF3 predictions support a conditional folding mechanism in which Pc gradually undergoes disorder-to-order transitions upon oligomerization."
- **Evidence pointer** Results section "AF and Cryo-EM Insights into Pc Self-Oligomerization", Figure 6, Table 4
- **Concern** The authors acknowledge that AF3 predictions have low confidence for IDRs and that most ipTM scores are below the 0.3 threshold suggested for estimating oligomerization state. Despite this, they use these predictions to support a "conditional folding" model. This is a significant overinterpretation of low-confidence predictions. The ipTM scores reported in Table 4 are not provided in the text, so the reader cannot assess the degree of confidence.
- **Why it matters** The "conditional folding" model is presented as a mechanistic insight, but it is based on predictions that the authors themselves acknowledge are unreliable for IDRs. This weakens the biological conclusions of the paper.
- **Resolution test** Report the ipTM and pLDDT scores for all models. If the scores are below confidence thresholds, the conditional folding claim should be presented as a hypothesis for future testing, not as a supported conclusion. Consider experimental validation using techniques such as hydrogen-deuterium exchange or limited proteolysis.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Relevance of the fusion construct
- **Claim pointer** The manuscript states that "all further analyses were performed with the MBP-Pc fusion protein" because removal of the MBP tag resulted in complete protein precipitation.
- **Evidence pointer** Results section "Recombinant Expression of Pc Protein in the Bacterial System"
- **Concern** All biophysical characterization was performed on the MBP fusion, not on the native Pc protein. MBP is a 42 kDa protein that is known to dimerize under certain conditions, and its presence could substantially influence the oligomerization behavior observed. The authors do not discuss the potential contribution of MBP-MBP interactions to the observed self-association. The claim that the observed oligomerization reflects Pc's intrinsic properties is therefore not fully supported.
- **Why it matters** The biological relevance of the findings depends on whether the observed self-association is a property of Pc itself or an artifact of the fusion construct. If MBP contributes to oligomerization, the conclusions about Pc function are compromised.
- **Resolution test** Perform control experiments with MBP alone under identical conditions to assess its oligomerization behavior. If possible, characterize a tag-free Pc construct using alternative solubilization strategies. At minimum, the authors should discuss the potential contribution of MBP to the observed assembly.

- **Concern ID** R1-M5
- **Severity** Major
- **Blocking** No
- **Axis** Data availability
- **Claim pointer** The manuscript references Figures 1-7, Tables 1-4, and Supplementary Figures S2-S5, but none of these are available for review.
- **Evidence pointer** Throughout the manuscript
- **Concern** The entire evidentiary basis of the paper is contained in figures and tables that were not provided. Key claims regarding CD spectra, DLS size distributions, SEC-MALS molar masses, nanoDSF melting curves, and cryo-EM micrographs cannot be verified. The manuscript text alone is insufficient to assess the validity of the results.
- **Why it matters** Peer review requires access to the primary data. Without the figures and tables, the claims cannot be evaluated.
- **Resolution test** Provide all figures and tables, including raw data where appropriate, for review.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Methods section
- **Evidence pointer** Materials and Methods, "Data Collection"
- **Issue** The cryo-EM data collection parameters are incomplete. The authors state the microscope, detector, and nominal magnification, but do not report the total electron dose per movie (only total dose per area), the exposure time, the number of movies collected, or the defocus range is given as "1.5 to -2.5 µm" which appears to have a sign error.
- **Required correction** Provide complete data collection parameters, including total dose per movie, number of movies, and correct the defocus range.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Results section
- **Evidence pointer** Results section "Secondary and Tertiary Structure Analysis"
- **Issue** The ProtParam analysis is described as predicting molecular weight and pI, but the authors do not report the extinction coefficient or estimated solubility, which are standard ProtParam outputs and relevant for a protein that precipitates upon tag removal.
- **Required correction** Report all relevant ProtParam parameters, or state why they were not used.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Precision
- **Affected element** Results section
- **Evidence pointer** Results section "Oligomeric State Determined by SEC-MALS"
- **Issue** The authors state the oligomer is composed of "approximately 100 subunits" based on a molar mass of 7.49 x 10^6 g/mol. The expected monomer mass of the Pc-MBP fusion is stated as 87.35 kDa by ProtParam, but the SDS-PAGE band is described as 88 kDa. The calculation of subunit number should be stated explicitly, and the error in the estimate should be discussed.
- **Required correction** Show the calculation for the number of subunits and discuss the uncertainty in this estimate.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Referencing
- **Affected element** Introduction
- **Evidence pointer** Introduction, paragraph 2
- **Issue** The statement "The crystal structure of PRC1 bound to the nucleosome shows that one copy of the PRC1 ubiquitylation module (without the Pc protein) forms a crescent shape..." is referenced to [25], but the authors do not specify which study this refers to in the text. The reference list was not provided.
- **Required correction** Ensure all references are complete and correctly cited in the reference list.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Terminology
- **Affected element** Abstract and throughout
- **Evidence pointer** Abstract
- **Issue** The term "self-oligomerization" is used throughout, but the authors also describe "higher-order assemblies" and "aggregation." These terms are not clearly distinguished. The SEC-MALS data suggest a very large assembly (~7.5 MDa), which may be more accurately described as an aggregate or a condensate-like species rather than a defined oligomer.
- **Required correction** Define the terms used and ensure consistent usage throughout the manuscript.

- **Concern ID** R1-m6
- **Severity** Minor
- **Axis** Statistical rigor
- **Affected element** Results section
- **Evidence pointer** Results section "Thermal Stability of Protein"
- **Issue** The nanoDSF and TSA experiments are described as having technical triplicates, but no statistical analysis is presented. The authors report Tm values as single numbers without error estimates.
- **Required correction** Report mean and standard deviation for Tm values, and state the number of independent experiments.

## Risk / unsupported claims
- The claim that Pc forms defined self-oligomers of approximately 100 subunits is not supported without the SEC-MALS data and a demonstration of specific, reversible assembly.
- The "conditional folding" model is based on low-confidence AF3 predictions and is presented with insufficient caveats.
- The biological relevance of the observed oligomerization to Pc function in Polycomb-mediated regulation is speculative, as all experiments were performed with an MBP fusion protein in vitro.
- The claim that cryo-EM "reveals pronounced conformational and oligomeric heterogeneity" cannot be evaluated without the micrographs and 2D class averages, which the authors state could not be calculated.
- The discrepancy between SEC-MALS (7.5 MDa species) and cryo-EM (no large particles without cross-linking) is not adequately explained and undermines the central conclusion.

## Assessment against Nature-style criteria
- **Originality**: Moderate. The application of a multi-technique biophysical pipeline to a disordered Polycomb protein is not entirely novel, but the specific combination of approaches and the focus on Pc self-association is of some interest. The work does not present a fundamentally new concept or methodology.
- **Scientific importance**: Moderate. Understanding Pc self-association could have implications for Polycomb body formation and epigenetic regulation. However, the study is largely descriptive and does not provide mechanistic insight into how oligomerization affects Pc function in vivo. The biological significance remains speculative.
- **Interdisciplinary readership**: Limited. The manuscript is primarily of interest to biophysicists and structural biologists working on disordered proteins and chromatin factors. The biological conclusions are not developed sufficiently to attract a broad cell biology or epigenetics audience.
- **Technical soundness**: The experimental design is generally sound, with appropriate techniques applied. However, the internal inconsistency between SEC-MALS and cryo-EM results is a significant technical concern that must be resolved. The reliance on a fusion protein without adequate controls for the fusion partner's contribution is also a weakness.
- **Readability for nonspecialists**: The manuscript is clearly written and the logic is generally easy to follow. However, the heavy reliance on referenced figures and tables that are not described in sufficient detail in the text makes it difficult for a nonspecialist to assess the evidence.

## Recommendation posture
Currently not established from the provided evidence. The manuscript addresses a relevant problem and applies an appropriate range of techniques, but the central claim of self-oligomerization is not supported by the available evidence due to (1) the internal inconsistency between SEC-MALS and cryo-EM results, (2) the lack of control experiments for the MBP fusion partner, and (3) the reliance on low-confidence computational predictions for the "conditional folding" model. The authors should be encouraged to resubmit after addressing these concerns with additional data and a more critical interpretation of their results.