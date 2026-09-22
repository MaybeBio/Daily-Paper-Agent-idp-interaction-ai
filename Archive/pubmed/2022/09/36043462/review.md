## Review setup
- **Input scope** Abstract only
- **Assessment boundary** Claims and conclusions as presented in the abstract; no access to full text, figures, tables, or supplementary materials
- **Shared manuscript claim summary** The authors use constant pH molecular dynamics (CpHMD) simulations to study the molten globule (MG) state of alpha-lactalbumin (aLA) at low pH upon calcium removal. They apply dihedral principal component analysis, density-based clustering, and machine learning to identify conformational fluctuations. They report metastable states in the MG state, with residues contributing to essential coordinates originating from a stable helix in the crystal structure but predominantly adopting unstructured or bent conformations in the MG state. These residues are proposed to control exposure of putative fatty-acid binding residues. The authors conclude that the MG state behaves as an intrinsically disordered protein (IDP), with disorder induced by external conditions.
- **Visible evidence base** Abstract text only; no methodological details, simulation parameters, validation metrics, or quantitative results are provided
- **Missing materials affecting confidence** Full manuscript, simulation protocols, force field parameters, CpHMD implementation details, clustering and machine learning validation, structural figures, quantitative fluctuation data, comparison datasets for IDPs, and any statistical analyses

## Reviewer
- **Overall assessment** The abstract presents an interesting hypothesis that the MG state of aLA exhibits IDP-like conformational behavior, supported by a multi-method computational approach. However, the abstract alone provides insufficient detail to evaluate the technical soundness of the simulations, the robustness of the analytical methods, or the strength of the central claim. The conclusion that the MG state "behaves as an intrinsic disorder protein" is plausible but not established from the evidence presented in the abstract. The work may be of interest to the protein folding and disorder communities, but the current evidence base is too limited for a definitive assessment.
- **Who would be interested in the results, and why** Researchers studying protein folding intermediates, molten globule states, intrinsically disordered proteins, and computational biophysics. The work connects MG dynamics to IDP behavior, which could inform understanding of conformational ensembles and functional roles of partially folded states. Methodologists interested in applying dimensionality reduction, clustering, and machine learning to molecular dynamics trajectories may also find the approach relevant.
- **Major strengths** The study addresses a timely question about the dynamic nature of MG states and their potential functional relevance. The use of CpHMD to model low-pH conditions is appropriate for the system. The combination of multiple analytical techniques (dihedral PCA, density-based clustering, machine learning) is a reasonable strategy to characterize conformational heterogeneity. The link between specific residues and putative binding-site exposure provides a mechanistically plausible connection between conformational fluctuations and function.
- **Major Concerns**  
  - **Concern ID** R1-M1  
  - **Severity** Major  
  - **Blocking** Yes  
  - **Axis** Technical soundness  
  - **Claim pointer** The authors claim that CpHMD simulation maintains the protonation state of titratable residues at low pH and that the resulting ensemble represents the MG state of aLA.  
  - **Evidence pointer** Abstract only; location not provided  
  - **Concern** The abstract provides no information on simulation length, number of replicas, force field, water model, temperature, salt concentration, or validation that the simulated ensemble reproduces experimentally known properties of the aLA MG state (e.g., radius of gyration, secondary structure content, or binding affinity). Without such validation, it is unclear whether the observed conformational fluctuations are representative of the true MG state or artifacts of the simulation setup.  
  - **Why it matters** The central conclusion that the MG state behaves as an IDP depends entirely on the fidelity of the simulated ensemble. If the simulation does not accurately capture the MG state, all downstream analyses and interpretations are compromised.  
  - **Resolution test** Provide simulation details and demonstrate that the simulated ensemble matches experimental observables for the aLA MG state, such as hydrodynamic radius, far-UV circular dichroism spectra, or tryptophan fluorescence, within acceptable tolerances.  
  - **Concern ID** R1-M2  
  - **Severity** Major  
  - **Blocking** Yes  
  - **Axis** Technical soundness  
  - **Claim pointer** The authors claim that metastable states are identified in the MG state using dihedral PCA, density-based clustering, and machine learning.  
  - **Evidence pointer** Abstract only; location not provided  
  - **Concern** The abstract does not describe how metastable states were defined, how many were found, how clustering parameters were chosen, or how the machine learning method was validated. There is no information on convergence of the clustering, robustness across parameter choices, or comparison to alternative methods. Without these details, the metastable states could be artifacts of the analytical pipeline rather than genuine physical states.  
  - **Why it matters** The identification of metastable states is a key finding that supports the IDP-like behavior claim. If the states are not robustly defined, the interpretation of residue-specific conformational preferences and their functional implications is weakened.  
  - **Resolution test** Provide a detailed description of the clustering and machine learning protocols, including parameter selection, validation metrics (e.g., silhouette score, Davies-Bouldin index), and evidence that the identified states are reproducible across independent simulations or trajectory subsampling.  
  - **Concern ID** R1-M3  
  - **Severity** Major  
  - **Blocking** Yes  
  - **Axis** Claim support  
  - **Claim pointer** The authors claim that residues containing the essential coordinates responsible for metastability belong to a stable helix in the crystal structure but prefer unstructured or bent conformations in the MG state, and that these residues control exposure of putative fatty-acid binding residues.  
  - **Evidence pointer** Abstract only; location not provided  
  - **Concern** The abstract does not specify which residues are involved, how "essential coordinates" were defined, or how the connection to fatty-acid binding residues was established. No quantitative data are presented to support the claim that these residues control binding-site exposure. The causal link between conformational preferences of specific residues and exposure of binding residues is asserted without supporting evidence.  
  - **Why it matters** This is the mechanistic core of the paper, linking conformational dynamics to potential function. Without clear evidence, the claim remains speculative and does not advance understanding beyond what is already known about MG state dynamics.  
  - **Resolution test** Identify the specific residues, show their conformational distributions in the MG state versus the native state, and provide a quantitative analysis (e.g., solvent-accessible surface area calculations or binding-site opening metrics) demonstrating that the observed conformational changes directly affect exposure of the putative binding residues.  
  - **Concern ID** R1-M4  
  - **Severity** Major  
  - **Blocking** Yes  
  - **Axis** Claim support  
  - **Claim pointer** The authors claim that the MG state of aLA behaves as an intrinsically disordered protein, with disorder induced by external conditions.  
  - **Evidence pointer** Abstract only; location not provided  
  - **Concern** The abstract does not provide a direct comparison between the conformational fluctuations of the MG state and those of known IDPs. No metrics such as ensemble radius of gyration distributions, secondary structure propensities, or conformational entropy are compared. The claim of IDP-like behavior is inferred rather than demonstrated.  
  - **Why it matters** The title and central conclusion rest on this comparison. Without quantitative benchmarking against IDP datasets or established IDP criteria, the claim is not supported by the presented evidence.  
  - **Resolution test** Provide a quantitative comparison of the MG state ensemble properties (e.g., Ramachandran plot distributions, contact maps, or chain dimensions) to those of well-characterized IDPs under similar simulation conditions, and discuss whether the observed fluctuations meet established criteria for IDP behavior.
- **Minor Comments**  
  - **Concern ID** R1-m1  
  - **Severity** Minor  
  - **Axis** Clarity  
  - **Affected element** Abstract wording  
  - **Evidence pointer** Abstract; location not provided  
  - **Issue** The phrase "the MG state of a protein behaves as an intrinsic disorder protein" is grammatically awkward and conceptually imprecise. The MG state is a state, not a protein, and the comparison to IDPs should be framed as a similarity in conformational behavior rather than an equivalence.  
  - **Required correction** Rephrase to "the conformational fluctuations of the MG state resemble those of intrinsically disordered proteins" or similar.  
  - **Concern ID** R1-m2  
  - **Severity** Minor  
  - **Axis** Completeness  
  - **Affected element** Abstract content  
  - **Evidence pointer** Abstract; location not provided  
  - **Issue** The abstract does not state the simulation time scale or the number of independent trajectories, which is essential context for evaluating whether the observed fluctuations are statistically meaningful.  
  - **Required correction** Add a sentence specifying the total simulation time and number of replicas or independent runs.  
  - **Concern ID** R1-m3  
  - **Severity** Minor  
  - **Axis** Reproducibility  
  - **Affected element** Methods description  
  - **Evidence pointer** Abstract; location not provided  
  - **Issue** The machine learning technique is mentioned but not specified. Different methods (e.g., hidden Markov models, variational autoencoders, or Markov state models) have different assumptions and outputs, and the choice affects interpretation.  
  - **Required correction** Name the specific machine learning method used and briefly state its purpose in the analysis.  
  - **Concern ID** R1-m4  
  - **Severity** Minor  
  - **Axis** Context  
  - **Affected element** Introduction of IDP comparison  
  - **Evidence pointer** Abstract; location not provided  
  - **Issue** The abstract states that earlier studies show MG states are dynamic, but does not cite specific examples or explain how the current work advances beyond those studies.  
  - **Required correction** Add one or two references and a sentence clarifying the novel contribution relative to prior MG dynamics studies.

## Technical failings that need to be addressed before the case is established
- R1-M1: Lack of simulation validation against experimental MG state properties
- R1-M2: Insufficient detail on metastable state identification and validation
- R1-M3: Unsupported causal link between residue conformations and binding-site exposure
- R1-M4: No quantitative comparison to IDP behavior

## Risk / unsupported claims
- The claim that the MG state "behaves as an intrinsic disorder protein" is unsupported without direct comparative analysis against IDP datasets.
- The claim that specific residues "control" exposure of fatty-acid binding residues is unsupported without quantitative exposure or accessibility data.
- The existence and number of metastable states are unverifiable from the abstract alone.
- The assertion that CpHMD accurately represents the low-pH MG state is unverifiable without validation details.

## Assessment against Nature-style criteria
- **Originality** The idea of comparing MG state dynamics to IDP behavior is not entirely new, but the specific application to aLA with a multi-method computational approach may offer a fresh perspective. The originality is moderate and depends on whether the full paper provides novel mechanistic insights beyond prior MG studies.
- **Scientific importance** The work addresses a fundamental question about the nature of protein folding intermediates and their potential functional relevance. If the claims are robustly supported, the findings could inform understanding of how partially folded states contribute to biological function. However, the importance is currently tempered by the lack of demonstrated novelty over existing MG dynamics studies.
- **Interdisciplinary readership** The topic bridges protein biophysics, computational chemistry, and structural biology. The use of machine learning may attract computational scientists, but the abstract does not clearly articulate the broader significance for experimentalists or non-specialists.
- **Technical soundness** Not assessable from the abstract. The methods are named but not described in sufficient detail to evaluate their appropriateness or correctness. Validation is entirely absent.
- **Readability for nonspecialists** The abstract is generally readable but uses jargon (e.g., "dihedral principal component analysis," "density based clustering") without explanation. The central claim about IDP-like behavior is stated clearly, but the mechanistic details are opaque.

## Recommendation posture
Currently not established from the provided evidence. The abstract presents an interesting hypothesis and a plausible methodological approach, but the absence of simulation details, validation, and quantitative comparisons prevents assessment of whether the central claims are supported. The manuscript may become publishable if the full paper addresses the technical concerns, particularly simulation validation, metastable state robustness, and direct IDP comparison. A supportive recommendation would require evidence that the simulated ensemble faithfully represents the aLA MG state and that the IDP-like behavior claim is quantitatively demonstrated.