## Review setup
- **Input scope** Full manuscript text including abstract, introduction, results, methods, and figure legends
- **Assessment boundary** Scientific validity, methodological rigor, claims versus evidence, and alignment with Nature-style criteria
- **Shared manuscript claim summary** The authors present OpenCGChromatin, a GPU-accelerated coarse-grained chromatin model with near-atomistic resolution, and use it to predict linker-length-dependent chromatin structure and phase separation, histone tail interaction networks, and acetylation effects on fiber dynamics
- **Visible evidence base** Main text figures 1-8, methods section, and references to supplementary figures and tables
- **Missing materials affecting confidence** Supplementary Information, Source Data, and Reporting Summary are referenced but not provided; figure legends for supplementary figures are absent; no code availability statement is visible

## Reviewer
- **Overall assessment** This manuscript describes a significant technical advance in chromatin simulation methodology and applies it to generate mechanistically insightful predictions about chromatin structure and phase separation. The model's ability to reproduce the oscillatory linker-length dependence of chromatin compaction, a long-standing experimental observation, is impressive and lends credibility to the predictive claims. The application to acetylation effects on long fibers is conceptually interesting and generates testable hypotheses. However, the manuscript would benefit from clearer articulation of the model's limitations, more rigorous treatment of the phase separation simulations, and additional validation against experimental data where available. The claims about "molecular principles" are somewhat broad relative to the evidence presented, which is largely simulation-based with limited direct experimental validation.

- **Who would be interested in the results, and why** Chromatin biologists studying higher-order genome organization, computational biophysicists developing coarse-grained models of nucleic acid-protein systems, researchers investigating phase separation mechanisms in the nucleus, and scientists interested in the molecular basis of epigenetic regulation. The methodological advance will be of particular interest to the molecular simulation community, while the biological predictions about linker-length control of phase behavior and acetylation effects will interest experimental chromatin researchers.

- **Major strengths** The model represents a genuine technical advance, achieving order-of-magnitude improvements in simulation throughput while maintaining near-atomistic resolution. The reproduction of the experimentally observed oscillatory compaction pattern across linker lengths is a strong validation. The connection between single-fiber conformational properties and phase behavior is conceptually elegant and mechanistically insightful. The identification of H4K16 and H3K9 as energetically critical acetylation sites provides a physicochemical rationale for their known regulatory importance.

- **Major Concerns** The phase separation simulations use relatively short tetranucleosome arrays, and the connection to physiological chromatin (which has heterogeneous linker lengths and protein interactions) is not fully addressed. The acetylation simulations use a random 50% acetylation scheme that may not reflect biological acetylation patterns. The discrepancy between simulated and cryo-ET observations of conformational changes upon phase separation is acknowledged but not fully resolved. The model's treatment of ions via Debye-Hückel screening is a significant simplification that may affect quantitative predictions.

- **Minor Comments** The manuscript would benefit from a more explicit statement of the model's limitations in the main text. The use of "near-atomistic" throughout is somewhat imprecise given the coarse-grained nature of the model. The discussion of biological implications could be more carefully qualified given the simplified system studied.

- **Technical failings that need to be addressed before the case is established** The phase separation simulations should be validated against additional experimental observables beyond qualitative binodals. The acetylation predictions would be strengthened by comparison with experimental data on acetylation-induced chromatin decompaction. The model's treatment of nucleosome breathing and its potential effects on the reported results should be discussed more thoroughly.

- **Assessment against Nature-style criteria** 
  - Originality: High. The combination of GPU acceleration with near-atomistic resolution for chromatin systems of this size is novel, and the application to phase separation is timely.
  - Scientific importance: Moderate to high. The predictions about linker-length control of phase behavior and acetylation effects have clear biological relevance, though they remain to be experimentally validated.
  - Interdisciplinary readership: Moderate. The work bridges molecular simulation, biophysics, and chromatin biology, but the technical focus may limit broader appeal.
  - Technical soundness: Generally sound, with appropriate methods and analysis, though some claims extend beyond what the evidence directly supports.
  - Readability for nonspecialists: The abstract and introduction are accessible, but the results section assumes substantial background in both chromatin biology and molecular simulation.

- **Recommendation posture** Supportive if technical concerns are resolved, particularly regarding validation of phase separation predictions and clearer articulation of model limitations.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Claim-evidence alignment
- **Claim pointer** "OpenCGChromatin simulations independently predict, from physicochemical principles, the linker-DNA-dependent chromatin structures observed by cryo-ET and the relative thermodynamic stability of condensates inferred from biochemical assays."
- **Evidence pointer** Figure 2, Supplementary Figures 3, 4, 7
- **Concern** The claim of "independently predict" is weakened by the fact that the model was parameterized to reproduce experimental compaction trends for linker lengths 25, 30, and 58 bp (Supplementary Figure 4). While the authors state that other linker lengths are predictions, the model's ability to reproduce the oscillatory pattern is partly a consequence of the fitting procedure. The distinction between parameters used for fitting and genuinely predicted observables should be made more explicit.
- **Why it matters** The central claim of the manuscript rests on the model's predictive power. If the oscillatory compaction pattern is largely a consequence of parameter fitting rather than emergent behavior, the strength of the validation is substantially reduced.
- **Resolution test** Provide a clear statement of which parameters were fit to which experimental data, and demonstrate that the oscillatory pattern emerges for linker lengths not included in the fitting procedure. Ideally, show that the model predicts compaction for intermediate linker lengths (e.g., 35, 40, 45 bp) that were not used in parameterization.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Methodological rigor
- **Claim pointer** "Extending simulations to 108-nucleosome fibers shows that acetylation disrupts chromatin compaction in a pattern-specific manner by weakening key tail-mediated interactions, with H4K16 and H3K9 emerging as the most energetically disruptive modifications."
- **Evidence pointer** Figures 7, 8, Supplementary Figure 17
- **Concern** The acetylation simulations use a random 50% acetylation of lysine residues, which is acknowledged as an upper bound of plausible acetylation density. However, the biological relevance of this scheme is unclear. In vivo, acetylation is targeted to specific residues by histone acetyltransferases and occurs at varying stoichiometries. The claim that H4K16 and H3K9 are "the most energetically disruptive" may be an artifact of the random acetylation scheme rather than a reflection of biological specificity. Additionally, the simulations do not account for the charge neutralization effects of acetylation on histone-DNA interactions within the same nucleosome.
- **Why it matters** The biological interpretation of the acetylation results depends critically on the acetylation scheme used. If the results are sensitive to the pattern of acetylation, the conclusions about specific residues may not be robust.
- **Resolution test** Perform additional simulations with different acetylation patterns (e.g., targeted acetylation of specific residues, varying stoichiometries) to test whether the identified residues are robustly the most disruptive. Alternatively, compare with experimental data on acetylation-induced decompaction to validate the predictions.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Scope of claims
- **Claim pointer** "The model recapitulates key experimental observations, such as the oscillatory dependence of chromatin compaction on linker DNA length, the structural motifs resolved by cryo-EM, X-ray crystallography and cryo-ET, and the modulation of chromatin condensate stability with linker DNA length."
- **Evidence pointer** Figure 2, Supplementary Figures 3, 7
- **Concern** The comparison with cryo-EM and X-ray crystallography structures is described but the quantitative nature of this comparison is not fully clear. The authors state that "all cryo-ET values fall within the simulated distributions" for radius of gyration, but the comparison with cryo-EM and crystallography appears more qualitative. A more rigorous quantitative comparison with available structural data would strengthen the validation.
- **Why it matters** The claim of recapitulating experimental structures is central to establishing the model's credibility. A qualitative comparison is insufficient to support the strength of the claim.
- **Resolution test** Provide quantitative metrics for the comparison with cryo-EM and crystallographic structures, such as root-mean-square deviations of nucleosome positions or contact map similarities, rather than qualitative statements of agreement.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Generalizability
- **Claim pointer** "The model recapitulates key experimental observations... and the modulation of chromatin condensate stability with linker DNA length."
- **Evidence pointer** Figure 4, Supplementary Figures 14-16
- **Concern** The phase separation simulations are performed with tetranucleosome arrays at a single concentration and salt condition. The authors acknowledge that the direct coexistence approach probes equilibrium behavior, but the relevance to cellular chromatin, which contains heterogeneous linker lengths, nucleosome-free regions, and associated proteins, is not addressed. The claim that the model reveals "molecular principles that control chromatin structure and phase separation" may overstate the generalizability of results obtained with simplified model systems.
- **Why it matters** The biological significance of the findings depends on their relevance to physiological chromatin. If the results are specific to the simplified systems studied, the broader claims are not supported.
- **Resolution test** Discuss more explicitly how the simplified model systems relate to physiological chromatin, and identify which predictions are expected to be robust in more complex systems. If possible, perform simulations with heterogeneous linker lengths or include additional chromatin components to test the robustness of the conclusions.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Terminology
- **Evidence pointer** Throughout
- **Issue** The term "near-atomistic" is used throughout but is not precisely defined. The model represents each amino acid and nucleotide as a single bead, which is a coarse-grained representation, not truly "near-atomistic" in the sense of retaining atomic detail.
- **Required correction** Define the term clearly in the introduction or methods, and consider using a more precise descriptor such as "residue-level coarse-grained" or "quasi-atomistic."

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Reproducibility
- **Affected element** Code availability
- **Evidence pointer** Methods section
- **Concern** No code availability statement is provided. Given the methodological focus of the manuscript, making the OpenCGChromatin code and simulation parameters publicly available would substantially enhance reproducibility and utility to the community.
- **Required correction** Add a code availability statement with a link to a public repository containing the model implementation, parameter files, and example simulation inputs.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Statistical rigor
- **Affected element** Figure 1b
- **Evidence pointer** Figure 1b
- **Issue** The benchmark data in Figure 1b are described as single descriptive measurements (n=1) with no uncertainty or inferential comparison claimed. While this is transparent, it limits the strength of the performance claims.
- **Required correction** Consider providing at least a small number of replicate benchmark measurements to demonstrate the stability of the performance results, or clearly state that these are representative single measurements.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Biological relevance
- **Affected element** Discussion of acetylation
- **Evidence pointer** Discussion section
- **Issue** The discussion of acetylation focuses on the energetic disruption of tail-mediated interactions but does not address the role of acetylation in recruiting reader proteins (e.g., bromodomain-containing proteins) that can further modulate chromatin structure. This is a missed opportunity to connect the simulation results to broader biological mechanisms.
- **Required correction** Add a brief discussion of how the simulation results relate to the broader acetylation signaling network, including reader protein recruitment.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Experimental validation
- **Affected element** Phase separation predictions
- **Evidence pointer** Figure 4
- **Concern** The phase separation predictions are compared with "closely related chromatin-array experiments using similar assembly and buffer conditions from the same research program." This is a somewhat circular validation, as the experiments come from the same group. Independent experimental validation would strengthen the claims.
- **Required correction** Acknowledge the source of the experimental comparisons and discuss any independent experimental data that support or contradict the predictions.

## Risk / unsupported claims
- The claim that H4K16 and H3K9 are "the most energetically disruptive" acetylation sites is based on a random 50% acetylation scheme and may not reflect biological specificity; this claim is not fully supported by the evidence presented.
- The claim of "independently predict" is weakened by the parameterization procedure, which used some of the same experimental data for fitting.
- The comparison with cryo-EM and X-ray crystallography structures is described qualitatively; the quantitative basis for this comparison is not provided in the visible text.
- The phase separation simulations use simplified model systems (tetranucleosome arrays with uniform linker lengths), and the generalizability of the conclusions to physiological chromatin is not fully established.
- The statement that "the same behavior emerges independently" in the restrained and unrestrained simulations is presented as validation, but both simulations use the same underlying model, so this is not truly independent validation.
- The biological interpretation of the results as revealing "molecular principles that control chromatin structure and phase separation" extends beyond what the evidence directly supports, given the simplified systems studied.