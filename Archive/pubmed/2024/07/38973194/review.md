## Review setup
- **Input scope** Full manuscript text including abstract, introduction, results, discussion, experimental section, and figure legends as provided.
- **Assessment boundary** Scientific content, experimental design, data interpretation, and internal consistency of the claims as presented in the provided text. No external validation or replication was performed.
- **Shared manuscript claim summary** The authors report that alpha-synuclein (αSyn) aggregation and liquid-liquid phase separation (LLPS) exhibit different salt dependencies under crowding conditions. Aggregation shows a non-monotonic salt dependence, attributed to intramolecular NTD-CTT electrostatic interactions modulated by screening and salting-out effects. LLPS shows a monotonic salt dependence, attributed to intermolecular interactions governed by the overall net charge. The authors further report that fibril-like structures formed at low salt concentrations convert into droplets after prolonged incubation, suggesting the droplet state is thermodynamically more stable and can dissolve aggregates.
- **Visible evidence base** ThT aggregation kinetics (Figures 1E-J, S1, S7, S8), AFM imaging (Figure S2), CG simulations (Figures 1K-P, 2B-D, 3C-D, S4, S13), SAXS measurements (Figures S5, S6), LLPS imaging (Figures 2A, 3A-B, S11, S12, S14, S15), long-term incubation studies (Figure 4), droplet size and fibril length analysis (Figure 5), and mass spectrometry (Figure S16).
- **Missing materials affecting confidence** Raw data files, full figure panels with all subpanels and annotations, detailed simulation parameters and convergence criteria, statistical analysis details for LLPS and fibril length measurements, and the complete supporting information document. The manuscript text alone does not allow full verification of all quantitative claims.

## Reviewer
- **Overall assessment** This manuscript presents a systematic and comprehensive investigation of the salt-dependent behavior of αSyn aggregation and LLPS, revealing a decoupling between these two assembly pathways. The combination of experimental assays and CG simulations is appropriate and generally well-executed. The finding that fibril-like structures can dissolve into droplets over extended incubation times is potentially significant and challenges common assumptions about fibril stability. However, several technical concerns, particularly regarding the interpretation of the "fibril-like structures" as bona fide amyloid fibrils, the lack of direct evidence for the proposed molecular mechanisms, and the limited discussion of alternative explanations, need to be addressed before the case is fully established.
- **Who would be interested in the results, and why** Researchers in the fields of protein aggregation, phase separation, neurodegeneration, and biophysics of intrinsically disordered proteins. The work is relevant to understanding the molecular determinants of αSyn assembly and the interplay between LLPS and aggregation, which is of broad interest to the protein misfolding and condensate biology communities. The methodological approach combining high-throughput imaging, simulations, and biophysical assays may also be of interest to those studying other IDPs.
- **Major strengths** 1) The study provides a wide parameter sweep (salt, pH, crowding, protein concentration) that is more comprehensive than most previous studies. 2) The combination of experiments and CG simulations to dissect intra- versus intermolecular interactions is a powerful approach. 3) The observation of fibril-to-droplet conversion over long timescales is novel and potentially important. 4) The use of a robotic dispenser for sample preparation and automated imaging is a technical strength.
- **Major Concerns** See detailed items below.
- **Minor Comments** See detailed items below.
- **Technical failings that need to be addressed before the case is established** R1-M1 (fibril identity), R1-M2 (mechanistic evidence), R1-M3 (simulation-experiment correlation), R1-M4 (long-term stability and reversibility).
- **Assessment against Nature-style criteria**  
  *Originality*: The finding of divergent salt dependencies for aggregation and LLPS, and the long-term conversion of fibrils to droplets, is original and adds new insight to a rapidly evolving field. However, the general concept that LLPS and aggregation can be decoupled is not entirely new, and the molecular mechanism proposed is largely inferred from simulations.  
  *Scientific importance*: The work addresses a fundamental question about the relationship between two key protein assembly states relevant to Parkinson's disease. The results could have implications for understanding disease mechanisms and for the design of therapeutic strategies. The importance is moderate to high, but the impact would be strengthened by more direct experimental validation of the proposed mechanisms.  
  *Interdisciplinary readership*: The topic is of interest to biophysicists, biochemists, cell biologists, and neuroscientists. The use of simulations and biophysical assays makes it accessible to a broad readership, though some specialized knowledge is assumed.  
  *Technical soundness*: The experimental design is generally sound, but several technical concerns (see below) need to be addressed. The CG simulation approach is appropriate but the link to experimental observables requires more careful justification.  
  *Readability for nonspecialists*: The manuscript is generally well-written and the logic is clear. However, some sections, particularly the simulation descriptions, may be challenging for nonspecialists. The figures and figure legends are not fully visible in the provided text, which limits assessment of clarity.
- **Recommendation posture** Supportive if technical concerns are resolved. The core observations are potentially interesting, but the current evidence does not fully establish the mechanistic claims. The authors should address the concerns raised, particularly regarding the identity of the "fibril-like structures" and the direct evidence for the proposed molecular mechanisms.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness / Data interpretation
- **Claim pointer** The manuscript repeatedly refers to "fibril-like structures" and "amyloid fibrils" formed at low salt concentrations, and claims these convert into droplets over time.
- **Evidence pointer** Figures 3A, 4A-D, S2, S11, S14, S15; text in Results sections "Decoupling Aggregation and Phase Separation of αSyn" and "Dissolution of αSyn Aggregates into Droplets"
- **Concern** The manuscript does not provide definitive evidence that the "fibril-like structures" observed by optical microscopy are indeed amyloid fibrils. The only structural characterization mentioned is AFM (Figure S2), which is described in the text but not shown in the provided material. ThT fluorescence is used for aggregation kinetics, but the correlation between ThT-positive species and the "fibril-like structures" seen in the LLPS experiments is not established. The authors should provide direct evidence (e.g., AFM images, electron microscopy, or ThT staining of the specific structures) that the structures observed in the LLPS experiments are amyloid fibrils and not amorphous aggregates or other species.
- **Why it matters** The central claim of the paper is that fibrils can dissolve into droplets. If the "fibril-like structures" are not bona fide amyloid fibrils, the interpretation of the results changes fundamentally. The distinction between amyloid fibrils and other aggregated states is critical for the conclusions drawn.
- **Resolution test** Provide high-resolution images (AFM or EM) of the "fibril-like structures" at the conditions where they are observed, and demonstrate that they bind ThT or show characteristic amyloid structure (e.g., X-ray diffraction, FTIR). Additionally, show that the conversion to droplets involves the disappearance of these amyloid-specific features.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Mechanistic understanding
- **Claim pointer** The manuscript claims that the non-monotonic salt dependence of aggregation is due to the interplay between electrostatic screening and salting-out effects on intramolecular NTD-CTT interactions, while the monotonic salt dependence of LLPS is due to intermolecular interactions governed by the overall net charge.
- **Evidence pointer** Figures 1K-P, 2B-D, 3C-D, S4, S13; text in Results sections "Regulation of αSyn Aggregation by Intramolecular Electrostatic Interactions Between NTD and CTT" and "Multivariate Effect of Crowding and Salt on αSyn Phase Separation"
- **Concern** The proposed mechanism is largely inferred from CG simulations. While the simulations are consistent with the experimental observations, the manuscript lacks direct experimental evidence that the proposed intramolecular NTD-CTT interactions are the primary determinant of the aggregation salt dependence. For example, mutations that specifically disrupt NTD-CTT interactions (beyond the ΔCTT variant) or experimental probes of intramolecular distances (e.g., FRET) under the relevant conditions would strengthen the claim. Additionally, the simulations use an implicit treatment of salt and crowding, and the authors should discuss the limitations of this approach.
- **Why it matters** The mechanistic explanation is a key part of the paper's contribution. Without direct experimental support, the mechanism remains speculative, and alternative explanations (e.g., salt effects on water activity, specific ion binding, or changes in protein conformation) are not fully excluded.
- **Resolution test** Provide experimental evidence (e.g., FRET measurements, mutagenesis of specific charged residues in NTD and CTT) that directly tests the role of NTD-CTT interactions in the salt-dependent aggregation. Alternatively, discuss and rule out alternative mechanisms.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Technical soundness / Data interpretation
- **Claim pointer** The manuscript claims a correlation between the simulated single-chain size (Rg) and aggregation behavior, and between simulated intermolecular interactions and LLPS behavior.
- **Evidence pointer** Figures 1K-P, 2B-D, 3C-D; text in Results sections as above
- **Concern** The quantitative correlation between simulation and experiment is not clearly established. For example, the simulated Rg values are reported to be larger than experimental values (the text notes "larger Rg values compared to CG simulations for all cases"), and the authors attribute this to high protein concentrations and the presence of other assembly states. However, it is unclear how the simulations were adjusted for these effects, and whether the qualitative agreement is sufficient to support the mechanistic claims. The authors should provide a more rigorous comparison, including error estimates and a discussion of the sensitivity of the results to simulation parameters.
- **Why it matters** The simulations are used to provide molecular-level insight into the experimental observations. If the correlation is not robust, the mechanistic conclusions are weakened.
- **Resolution test** Provide a quantitative comparison of simulation and experimental results, including a discussion of the limitations of the CG model and the sensitivity of the conclusions to the choice of interaction parameters.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Data interpretation / Significance
- **Claim pointer** The manuscript claims that the droplet state is more stable than the fibril state at the conditions tested, based on the observation that fibrils convert to droplets after prolonged incubation.
- **Evidence pointer** Figure 4A-D; text in Results section "Dissolution of αSyn Aggregates into Droplets" and Discussion
- **Concern** The conclusion that the droplet state is thermodynamically more stable is based on a single set of observations at specific conditions. The manuscript does not demonstrate that the conversion is reversible, nor does it explore whether the conversion is kinetically limited or thermodynamically driven. Additionally, the possibility that the "fibril-like structures" are kinetically trapped intermediates that dissolve without forming a thermodynamically stable droplet state is not discussed. The authors should provide a more detailed thermodynamic and kinetic analysis, or temper their conclusions.
- **Why it matters** The claim that droplets can dissolve fibrils is a significant and potentially impactful finding. If the interpretation is not robust, the significance of the work is diminished.
- **Resolution test** Perform experiments to test the reversibility of the fibril-to-droplet conversion (e.g., by changing salt concentration after droplet formation). Provide a more detailed analysis of the kinetics and thermodynamics of the process, or revise the conclusions to be more cautious.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity / Reproducibility
- **Affected element** Experimental section, "Measurement of Droplet Formation"
- **Evidence pointer** Methods section
- **Issue** The description of the LLPS experiments is brief. The authors state that "at least four replicates per condition were investigated," but do not specify how droplet formation was quantified (e.g., number of droplets, size distribution, turbidity). The criteria for classifying a condition as "droplet-forming" versus "non-forming" are not defined.
- **Required correction** Provide a more detailed description of the LLPS assay, including quantification methods and criteria for droplet formation.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Data presentation
- **Affected element** Figures 3A and 4A-D
- **Evidence pointer** Figures 3A, 4A-D
- **Issue** The representative images in Figures 3A and 4A-D are described in the text but not visible in the provided material. The authors should ensure that the images are of high quality and clearly show the features described (e.g., fibril-like structures, droplets, coexistence).
- **Required correction** Ensure that the figures are clear and that scale bars are included. Consider providing higher-magnification images to show the details of the structures.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Interpretation
- **Affected element** Discussion section
- **Evidence pointer** Discussion
- **Issue** The authors propose an energy landscape picture to explain their observations. While this is a useful conceptual framework, the discussion is somewhat speculative and could be more quantitative. For example, the authors could discuss the relative depths of the free energy minima for the droplet and fibril states based on their observations.
- **Required correction** Consider providing a more quantitative discussion of the proposed energy landscape, or clearly state that the picture is qualitative.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Reproducibility
- **Affected element** Methods, "Molecular Dynamics Simulations"
- **Evidence pointer** Methods section
- **Issue** The description of the CG simulations is brief. The authors state that the HPS model was used with an interaction strength of 0.13 kcal/mol, but do not provide details on how this was optimized, the system size, simulation length, or the number of replicates.
- **Required correction** Provide more details on the simulation setup, including system size, simulation time, and how the interaction strength was determined.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Abstract and Introduction
- **Evidence pointer** Abstract, Introduction
- **Issue** The abstract and introduction state that "factors promoting or inhibiting aggregation have similar effects on LLPS" based on previous work. This is presented as a general statement, but the authors should clarify that this is not always the case and that their study reveals exceptions.
- **Required correction** Rephrase to acknowledge the complexity of the relationship between LLPS and aggregation.

## Risk / unsupported claims
- The claim that "the droplet state is therefore capable of inhibiting aggregation or even dissolving aggregates through heterotypic interactions" is not fully supported by the data presented. The observation of fibril-to-droplet conversion is suggestive, but the mechanism of dissolution and the generality of this phenomenon are not established.
- The claim that the "sequence determinants of phase separation and aggregation have not co-evolved" is speculative and not directly tested in this study.
- The quantitative correlation between simulated Rg and experimental aggregation behavior is not rigorously established, as the authors note discrepancies between simulated and experimental values.
- The claim that the "unique sequence arrangement of αSyn and its specific heteropolymeric interactions between NTD and CTT contribute to the decoupling" is inferred from simulations and not directly tested experimentally.
- The long-term stability of the droplet state and the reversibility of the fibril-to-droplet conversion are not demonstrated.