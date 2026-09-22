## Review setup
- **Input scope** Full manuscript text, including abstract, introduction, results, discussion, methods, and figure legends as provided.
- **Assessment boundary** Evaluation is limited to the content and claims presented in the supplied manuscript text. Supplementary figures and tables are referenced but not independently assessed.
- **Shared manuscript claim summary** The authors characterize the SARS-CoV-2 nucleocapsid (N) protein as a flexible, multivalent RNA-binding protein with three dynamic disordered regions containing transiently-helical motifs. They combine single-molecule FRET, fluorescence correlation spectroscopy, and all-atom simulations to describe conformational behavior of the disordered regions in the context of folded domains. They further demonstrate that N protein undergoes RNA-dependent liquid-liquid phase separation and propose a symmetry-breaking model suggesting that high-affinity binding sites can drive single-genome condensation over multi-polymer phase separation.
- **Visible evidence base** Single-molecule FRET efficiency histograms, ns-FCS correlation data, denaturant titration curves, all-atom Monte Carlo simulation results, turbidity assays, and confocal fluorescence images of droplets, as described in Figures 1-6 and referenced supplementary materials.
- **Missing materials affecting confidence** Supplementary figures (S1-S19), supplementary tables (S1, S2, S7), detailed simulation parameters, full methods for phase separation assays, and raw data files were not provided. These are essential for verifying quantitative claims, simulation convergence, and reproducibility.

## Reviewer
- **Overall assessment** This manuscript presents a comprehensive biophysical characterization of the SARS-CoV-2 N protein, combining experimental and computational approaches to describe the conformational dynamics of its disordered regions and its phase separation behavior with RNA. The work is timely and relevant given the urgent need to understand SARS-CoV-2 biology. The integration of single-molecule spectroscopy with all-atom simulations is methodologically sound and provides a detailed residue-level view of the protein. However, several claims, particularly regarding the physiological relevance of phase separation and the symmetry-breaking model, are speculative and not directly supported by the experimental data presented. The phase separation experiments are limited to homopolymeric RNA and in vitro conditions, and the connection to viral genome packaging remains hypothetical. The symmetry-breaking model is illustrative but lacks quantitative validation against experimental observations. The manuscript would benefit from clearer distinctions between established findings and proposed models, and from additional experimental evidence linking the in vitro observations to functional relevance.
- **Who would be interested in the results, and why** Researchers in virology, particularly those studying coronavirus replication and assembly, will find the structural and biophysical characterization of the N protein valuable. The work also appeals to the biomolecular condensate and phase separation community, as it adds a viral protein to the growing list of RNA-binding proteins that undergo liquid-liquid phase separation. Additionally, biophysicists interested in disordered proteins and single-molecule methods will appreciate the methodological integration. The proposed symmetry-breaking model may interest theorists working on polymer physics and genome organization.
- **Major strengths** The combination of multiple orthogonal techniques (smFRET, ns-FCS, simulations) provides a robust and internally consistent picture of the disordered regions. The identification of transient helical motifs with potential functional significance offers testable hypotheses. The phase separation experiments are carefully executed with appropriate controls, including salt dependence and re-entrant behavior. The symmetry-breaking model is conceptually elegant and provides a framework for understanding how single-genome condensation might be achieved. The writing is clear and accessible, with appropriate caveats about model limitations.
- **Major Concerns** The major concerns are detailed below.
- **Minor Comments** The minor comments are detailed below.
- **Technical failings that need to be addressed before the case is established** R1-M1 (physiological relevance of phase separation), R1-M2 (model validation), R1-M3 (quantitative comparison of simulations and experiments), R1-M4 (interpretation of ns-FCS data for CTD).
- **Assessment against Nature-style criteria** **Originality**: The work is original in its comprehensive integration of single-molecule and simulation approaches applied to a viral protein of urgent interest. The symmetry-breaking model, while building on existing polymer physics concepts, is applied here in a novel context. **Scientific importance**: The characterization of the N protein is important for understanding SARS-CoV-2 biology and may inform therapeutic strategies. The phase separation findings contribute to the broader understanding of viral assembly mechanisms. **Interdisciplinary readership**: The work bridges virology, biophysics, and polymer physics, and should appeal to readers across these fields. **Technical soundness**: The experimental and computational methods are generally appropriate and well-executed, but several quantitative claims require additional validation as noted in the concerns. **Readability for nonspecialists**: The manuscript is well-written with clear figures and logical flow, though some sections on polymer physics may be challenging for nonspecialist readers. The abstract and introduction effectively frame the significance for a broad audience.
- **Recommendation posture** Supportive if technical concerns are resolved. The core biophysical characterization is solid and valuable, but the broader claims about physiological relevance and the symmetry-breaking model require either additional experimental support or more careful framing as hypotheses.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Claim-Data Gap
- **Claim pointer** The authors state that phase separation "may in fact be an unavoidable epiphenomenon that reflects physical properties necessary to drive the compaction of long genomic RNA molecules" and propose that their model "provides a plausible route through which single-genome condensation preferentially occurs over phase separation."
- **Evidence pointer** Figure 5, Figure 6, Discussion section
- **Concern** The physiological relevance of the observed phase separation is speculative. The experiments use homopolymeric RNA (poly(rU)) in dilute buffer conditions, which is far from the complex cellular environment. The claim that phase separation relates to genome packaging is not directly tested. The symmetry-breaking model is presented as a "plausible route" but no experimental evidence is provided to connect the model predictions to actual viral genome packaging. The authors acknowledge this limitation in the Discussion, but the framing in the abstract and introduction overstates the connection.
- **Why it matters** The title and abstract emphasize phase separation as a key finding, and the Discussion builds a narrative around its relevance to viral biology. If the physiological connection is not established, the significance of the phase separation observations is substantially diminished. The manuscript would be strengthened by either providing direct evidence for single-genome condensation (e.g., single-molecule imaging of full-length genomic RNA with N protein) or by clearly reframing the phase separation and model as purely biophysical observations with potential, but unproven, biological relevance.
- **Resolution test** The authors should either (1) provide experimental evidence linking the in vitro phase separation to genome packaging, such as demonstrating that N protein compacts full-length viral RNA into single-molecule condensates, or (2) revise the abstract, introduction, and Discussion to clearly state that the physiological relevance is unknown and that the phase separation is presented as a biophysical phenomenon with potential implications that require further investigation.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Model Validation
- **Claim pointer** The symmetry-breaking model is used to argue that "the same multivalent interactions that drive phase separation also engender RNA compaction" and that a "small number of high-affinity-binding sites" can shift the balance from multi-polymer phase separation to single-polymer condensation.
- **Evidence pointer** Figure 6, Discussion section
- **Concern** The coarse-grained model is highly simplified, using generic polymer and binder beads with isotropic interactions. The model parameters are not systematically varied or compared to experimental data. The claim that the model "establishes" that symmetry-breaking promotes single-genome condensation is not supported by quantitative analysis. The model is illustrative but does not provide predictive power for the real N protein-RNA system. The authors do not test whether the model predictions are robust to parameter choices or whether they match any quantitative experimental observables.
- **Why it matters** The model is a central component of the paper's conceptual framework, linking the biophysical observations to a proposed mechanism for genome packaging. Without validation, the model remains a hypothesis-generating exercise rather than a supported conclusion. The manuscript's impact is reduced if the model is not rigorously tested.
- **Resolution test** The authors should either (1) perform a systematic parameter sweep to demonstrate the robustness of the symmetry-breaking effect, (2) compare model predictions to quantitative experimental data (e.g., measured saturation concentrations, condensate sizes), or (3) clearly label the model as a conceptual illustration and remove claims that it "establishes" or "demonstrates" the mechanism.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Quantitative Agreement
- **Claim pointer** The authors state "We observed good agreement between simulation and experiment for the equivalent inter-residue distance" for the NTD-RBD construct, and similar claims are made for the linker and CTD.
- **Evidence pointer** Figures 2D, 3D, 4D
- **Concern** The "good agreement" is assessed qualitatively by visual comparison of histograms. No quantitative metrics (e.g., root-mean-square deviation, overlap coefficients, statistical tests) are provided. The simulation histograms appear broader and shifted relative to the experimental distributions in some cases. The authors do not report uncertainties in the simulation ensembles or account for potential force field inaccuracies. The claim of "good agreement" is therefore not rigorously supported.
- **Why it matters** The agreement between simulations and experiments is a cornerstone of the paper's claim that the simulations provide atomistic insight into the experimental observations. Without quantitative validation, the reader cannot assess the reliability of the simulation-derived conclusions about transient helices and inter-domain interactions.
- **Resolution test** The authors should provide quantitative measures of agreement (e.g., chi-squared statistics, Kolmogorov-Smirnov tests, or Bayesian evidence) for each comparison between simulated and experimental distance distributions. If the agreement is not statistically robust, the claims should be softened accordingly.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Data Interpretation
- **Claim pointer** The authors interpret the flat ns-FCS cross-correlation for the CTD as evidence for "two populations in equilibrium whose correlations compensate each other."
- **Evidence pointer** Figure 4B, Results section
- **Concern** This interpretation is presented as one of several possibilities, but the alternative explanation that the CTD is simply static on the ns timescale is not fully excluded. The authors do not provide a quantitative model of the two-population scenario or test whether it uniquely fits the data. The increase in anticorrelated amplitude with denaturant is consistent with their interpretation, but could also be explained by other mechanisms (e.g., changes in quenching efficiency).
- **Why it matters** The interpretation of the CTD dynamics is important for the overall picture of the protein as dynamic and disordered. If the CTD is actually static in the context of the full-length protein, this would affect the interpretation of its functional role.
- **Resolution test** The authors should either (1) provide additional evidence for the two-population model, such as fluorescence lifetime data or temperature-dependent measurements, or (2) present the interpretation more cautiously and discuss alternative explanations in the text.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Figure 1
- **Evidence pointer** Figure 1A
- **Issue** The domain architecture diagram does not clearly indicate the boundaries of the disordered regions relative to the folded domains. The positions of the dye labels are shown, but the scale and exact residue numbers are not provided in the figure.
- **Required correction** Add residue numbers and domain boundaries to the schematic in Figure 1A, or provide this information in the figure legend.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Reproducibility
- **Affected element** Methods section
- **Evidence pointer** Methods, "Protein expression, purification, and labeling"
- **Issue** The methods for phase separation assays (turbidity, confocal imaging) are not described in the main text. The reader is referred to the supplementary information, which was not provided for this review.
- **Required correction** Include a brief description of the phase separation assay conditions (e.g., protein and RNA concentrations, buffer composition, incubation time) in the main text Methods, or ensure the supplementary information is accessible.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Statistical Reporting
- **Affected element** Figure 2A, 3A, 4A
- **Evidence pointer** Figure legends
- **Issue** The reported uncertainties (e.g., 0.65 ± 0.03) are described as systematic errors in the text, but the number of independent measurements and the statistical treatment are not specified.
- **Required correction** Clarify the source of the uncertainties (e.g., standard deviation across replicate measurements, fitting uncertainty) and report the number of independent experiments or molecules analyzed.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Terminology
- **Affected element** Discussion section
- **Evidence pointer** Discussion, "The physics of single-polymer condensates"
- **Issue** The term "single-polymer condensates" is used to describe collapsed single chains, which may be confused with condensates formed by multiple chains. The distinction between a collapsed chain and a condensate should be clarified.
- **Required correction** Define the term clearly when first used, and consider using "single-chain collapsed states" or similar terminology to avoid ambiguity.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Literature Context
- **Affected element** Introduction
- **Evidence pointer** Introduction, paragraph 1
- **Issue** The introduction cites several recent preprints on SARS-CoV-2 N protein phase separation (references 20-27) but does not clearly distinguish the present work's contributions from these prior studies.
- **Required correction** Add a sentence in the Introduction or Discussion explicitly stating what new information this study provides beyond the existing literature on N protein phase separation.

## Risk / unsupported claims
- The claim that phase separation is an "unavoidable epiphenomenon" reflecting interactions relevant to genome packaging is not directly supported by experimental evidence and is presented as speculation.
- The symmetry-breaking model's prediction that "the same multivalent interactions that drive phase separation also engender RNA compaction" is not validated against experimental data.
- The assertion that the identified transient helices (H2, H3, H4, H5, H6) have specific functional roles (e.g., RNA binding, nuclear export, membrane interaction) is based on sequence homology and prior literature, not on direct functional experiments in this study.
- The statement that "phase separation offers a convenient readout for molecular interactions that might otherwise be challenging to measure" is a reasonable suggestion but is not demonstrated as a general principle.
- The claim that the model "establishes that if weak multivalent interactions underlie the formation of large multi-polymer droplets, those same interactions cannot also drive polymer compaction inside the droplet" is a model-derived conclusion that requires experimental verification.
- The physiological relevance of the observed phase separation to SARS-CoV-2 replication and assembly is not established and should be treated as a hypothesis.