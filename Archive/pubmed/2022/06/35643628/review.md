## Review setup
- **Input scope** Full manuscript text (abstract, significance, introduction, methods, results, discussion, conclusion) without figures, tables, or supporting material
- **Assessment boundary** Scientific claims, methodology, and interpretation as presented in the text; figure content assessed only through textual descriptions
- **Shared manuscript claim summary** The authors use coarse-grained Langevin dynamics simulations of a model HP1 dimer interacting with a model chromatin polymer to study the interplay between protein-protein and protein-chromatin interactions. They identify distinct regimes including dense droplets, coating, and absorbing droplets for multivalent interactions, and fractal/gel-like clusters for limited-valence interactions. A key claim is a regime where droplet density rather than size varies with overall protein concentration, and that chromatin absorption slows protein dynamics within droplets.
- **Visible evidence base** Main text methods and results sections; figure descriptions (Figs. 1–7); equation (1) for separation depth; equation (2) for radius of gyration; equation (3) for bond-bond correlation
- **Missing materials affecting confidence** All figures and figure panels; supporting material (S1–S18); simulation parameter details; interaction potential functional forms; equilibration protocols; finite-size analysis; parameter mapping details

## Reviewer
- **Overall assessment** This manuscript presents a systematic simulation study of a simplified model system designed to capture the physics of chromatin-binding proteins with multiple interaction domains. The work addresses an important and timely question in the field of biomolecular condensates, specifically the interplay between protein-protein phase separation and chromatin-mediated clustering. The model is appropriately simple for the questions asked, and the parameter space exploration is thorough. The identification of a regime where droplet density rather than size varies with protein concentration is potentially interesting and relevant to recent experimental observations on HP1. However, the assessment is substantially limited by the absence of figures and supporting material, which are essential for evaluating the quantitative claims, the phase diagram construction, and the robustness of the conclusions. The manuscript would benefit from clearer articulation of the novelty relative to prior simulation work on patchy particles and polymer-protein mixtures, and from a more direct connection between the model parameters and experimentally measurable quantities.

- **Who would be interested in the results, and why** Researchers studying biomolecular phase separation, particularly those interested in chromatin-associated condensates and the physical mechanisms underlying their formation. The work is also relevant to the broader community investigating the role of multivalent interactions and polymer-mediated clustering in cellular organization. Experimentalists studying HP1 and heterochromatin may find the predictions regarding droplet density scaling and slowed internal dynamics useful for interpreting their data. The simulation methodology and phase diagram construction may be of interest to computational biophysicists working on coarse-grained models of chromatin and nuclear bodies.

- **Major strengths** The study addresses a biologically important question with a tractable model that captures essential physics. The systematic exploration of the two-dimensional parameter space (εHH and εHC) is commendable and allows for a comprehensive phase diagram. The distinction between multivalent and limited-valence interaction models provides insight into how molecular details affect condensate morphology. The connection to experimental observations on HP1, particularly the density scaling behavior, is valuable. The discussion of the biological implications is thoughtful and appropriately cautious.

- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors claim to obtain a phase diagram for multivalent proteins that includes liquid-like droplets, droplets with absorbed polymer, and coated polymer regimes, with a regime where droplet density rather than size varies with overall protein concentration.
- **Evidence pointer** Fig. 2; Section "Model 1: Multivalent protein-protein interactions"; supporting material sections 6 and 9
- **Concern** The phase diagram and the key claim of density-dependent rather than size-dependent droplet behavior rest entirely on figures and supporting material that are not provided. The separation depth parameter φsep (Eq. 1) is defined, but the threshold values used to delineate regimes, the method for determining phase boundaries, and the finite-size analysis are not described in the main text. The claim that droplet density varies with overall protein concentration in the shaded region of Fig. 2c is a central result, but without seeing the actual density measurements and the phase diagram, this claim cannot be evaluated.
- **Why it matters** The central novelty of the paper appears to be the identification of a regime where the relationship between droplet density and protein concentration deviates from standard phase separation behavior. If this claim is not robustly supported by the data, the paper's main contribution is weakened. The phase diagram is the primary quantitative output of the study, and its construction methodology must be transparent and defensible.
- **Resolution test** Provide the phase diagram with clear axis labels, regime boundaries, and error estimates. Show the density measurements inside and outside droplets as a function of N for the shaded regime, with comparison to standard phase separation scaling. Describe the criteria used to assign regime boundaries and demonstrate that the results are robust to system size and simulation duration.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors claim that for limited-valence interactions, fractal or gel-like condensates are observed, and that these are long-lived metastable, dynamically arrested structures that do not represent true equilibrium.
- **Evidence pointer** Section "Model 2: Limited valence protein-protein interactions"; Fig. 6; supporting material sections 10 and 11
- **Concern** The distinction between equilibrium and metastable states is critical for interpreting the limited-valence results, but the evidence for dynamical arrest is not presented in the main text. The authors state that configurations depend on initial conditions and that different quenching procedures lead to different aggregate distributions, but no quantitative measures of dynamical arrest (e.g., relaxation times, mean-squared displacement, structural correlation functions) are provided. The fractal dimension measurements are only mentioned in passing.
- **Why it matters** The claim that limited-valence interactions produce gel-like states with different physical properties than the multivalent case is a key comparative result. If the observed structures are simply nonequilibrium artifacts of the quenching protocol, the biological relevance is less clear. The distinction between equilibrium gel phases and kinetically trapped states has important implications for how these results should be interpreted in the context of cellular condensates.
- **Resolution test** Provide quantitative evidence for dynamical arrest, such as time-dependent correlation functions showing plateau behavior, or structural measures that distinguish gel-like from fluid-like states. Show that the observed fractal clusters are robust to different preparation protocols or explain how the protocol dependence informs the interpretation.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Scientific importance
- **Claim pointer** The authors claim that their results provide "biologically relevant insights into the general nature of protein-chromatin condensates in living cells" and specifically that the density scaling behavior is consistent with recent in vivo experiments on HP1.
- **Evidence pointer** Abstract; Conclusion; reference to in vivo experiments (ref. 41)
- **Concern** The connection between the simulation results and in vivo observations is made at a qualitative level, but the mapping between model parameters and biological reality is not thoroughly discussed. The model uses a homogeneous polymer with uniform binding affinity, whereas real chromatin has heterogeneous modification patterns. The protein concentration in simulations (39 mM) is noted to be higher than typical in vivo estimates, but the implications of this discrepancy for the validity of the conclusions are not fully addressed.
- **Why it matters** The broader impact of the work depends on its relevance to understanding biological condensates. If the model is too far from biological reality in key aspects, the claimed insights may not transfer. The authors acknowledge some limitations but do not systematically address how their conclusions might change with more realistic chromatin models or lower protein concentrations.
- **Resolution test** Expand the discussion of parameter mapping to biological systems, including estimates of effective concentrations and interaction strengths. Discuss how heterogeneous chromatin binding patterns might alter the phase diagram. Address whether the key qualitative findings are expected to persist under more biologically realistic conditions.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Originality
- **Claim pointer** The authors present their model as inspired by HP1 and note that bridging-induced attraction has been studied previously, but the specific contribution of this work relative to prior simulation studies is not clearly articulated.
- **Evidence pointer** Introduction; references to prior work on patchy particles and BIA (refs. 11–14, 16–21, 28–32)
- **Concern** The introduction reviews relevant prior work but does not clearly state what is new about this study. The combination of protein-protein and protein-chromatin interactions in a single model with explicit domain structure may be novel, but the authors do not explicitly differentiate their contribution from previous simulation studies of BIA or of protein phase separation in the presence of polymers.
- **Why it matters** For a simulation study, the novelty may lie in the specific model design, the parameter regimes explored, or the phenomena identified. Without a clear statement of novelty, it is difficult to assess the contribution to the field.
- **Resolution test** Add a paragraph in the introduction or discussion that explicitly states what is new in this work relative to prior simulation studies, and what specific questions are addressed that have not been previously answered.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Readability for nonspecialists
- **Affected element** Introduction and model description
- **Evidence pointer** Section "HP1 model"; Fig. 1
- **Issue** The description of the model protein assumes familiarity with HP1 domain structure. The hinge and N-terminal tail regions are mentioned, but their physical properties (e.g., disorder, charge) that motivate the interaction model are not described.
- **Required correction** Briefly describe the physical characteristics of the HP1 domains and why the chosen interaction scheme is a reasonable simplification.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Technical soundness
- **Affected element** Simulation methodology
- **Evidence pointer** Section "Simulation scheme"
- **Issue** The simulation time unit τ is used throughout, but its relationship to physical time is not stated. The total simulation duration (5×10^3 τ) and the equilibration protocol are not described in the main text.
- **Required correction** Provide an estimate of the physical time corresponding to τ, and briefly describe the equilibration procedure and how steady state was determined.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Technical soundness
- **Affected element** Parameter mapping
- **Evidence pointer** Section "Simulation scheme"; supporting material section 4
- **Issue** The mapping of interaction energies εHH and εHC to physical quantities is deferred to the supporting material. A brief statement in the main text about the range of interaction strengths explored and their approximate physical meaning would aid interpretation.
- **Required correction** Add a sentence in the methods or results indicating the range of interaction energies studied and what they correspond to in terms of binding affinities or residence times.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Interdisciplinary readership
- **Affected element** Discussion of biological implications
- **Evidence pointer** Conclusion
- **Issue** The discussion of in vivo relevance is somewhat general. The authors mention HP1 and heterochromatin but do not discuss specific predictions that could be tested experimentally beyond the density scaling behavior.
- **Required correction** Consider adding a brief paragraph with more specific, testable predictions arising from the simulations.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Technical soundness
- **Affected element** Hysteresis observation
- **Evidence pointer** Section "Model 1: Multivalent protein-protein interactions"; Fig. 3c
- **Issue** The hysteresis observed in the slow ramping of εHC is mentioned but not discussed in detail. The implications of this hysteresis for the interpretation of the phase diagram are unclear.
- **Required correction** Briefly discuss whether the hysteresis indicates a first-order transition, kinetic trapping, or finite-size effects, and how this affects the interpretation of the phase boundaries.

## Risk / unsupported claims
- The claim of a regime where droplet density rather than size varies with overall protein concentration is not assessable without the phase diagram and density measurements (Fig. 2c, supporting material sections 6 and 9).
- The claim of fractal or gel-like condensates for limited-valence interactions is not quantitatively supported in the main text; fractal dimension measurements are only mentioned in passing.
- The claim that chromatin absorption slows protein dynamics by nearly an order of magnitude is based on Fig. 7 and supporting material section 12, neither of which is available for assessment.
- The statement that the model results are "robust to changes in details, such as polymer stiffness or exact shape of the protein model" is deferred to supporting material section 13 and cannot be verified.
- The comparison to in vivo experiments on HP1 (ref. 41) is qualitative and the degree of correspondence is not quantified.
- The mapping of simulation time units to physical time is not provided, limiting the interpretation of dynamical quantities.
- The claim that the observed hysteresis suggests a first-order transition in the thermodynamic limit is speculative and not supported by finite-size analysis in the main text.