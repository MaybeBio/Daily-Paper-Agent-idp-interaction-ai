## Review setup
- **Input scope** Full manuscript text (main text, methods summary, availability statement) without supplementary figures, tables, or appendices
- **Assessment boundary** Scientific claims, methodological soundness, and internal consistency based solely on the provided text; no assessment of supplementary materials, figures, or tables beyond what is described
- **Shared manuscript claim summary** The authors use coarse-grained simulations (SOP-IDP model) to show that in FUS-LC, the kinetics of fibril-core formation are inversely correlated with thermodynamic stability, consistent with Ostwald's rule of stages. Core-3 forms first and drives droplet nucleation via residues 164-176, while the most stable core-1 forms last. Core-3 and core-1 N∗ states are mutually exclusive. Droplet growth follows Ostwald ripening. Predicted core-3 structures from AlphaFold are used as reference states.
- **Visible evidence base** Main text descriptions of Brownian dynamics simulations (200 trajectories, 280 ms each for FUS-LC; 200 trajectories, 60 ms each for FUS-LC-N), Langevin dynamics simulations, free energy differences, contact maps, β-strand propensities, chemical potential calculations, Jensen-Shannon divergence, comparison with published experimental data (solid-state NMR, cryo-EM, SAXS, DEER, smFRET, hydrogel binding assays)
- **Missing materials affecting confidence** All figures, tables, supplementary information, and movies referenced in the text are not provided; the unpublished cryo-EM structure comparison cannot be independently assessed; the specific implementation details of the N∗ theory and the structural overlap parameter are only summarized

## Reviewer

- **Overall assessment** This manuscript presents a coherent computational study addressing a significant open question in the phase separation field: the molecular basis for the hierarchical assembly of fibril cores in FUS-LC. The central claim, that kinetic accessibility and thermodynamic stability are inversely correlated across the three cores, is well-motivated and supported by the simulation data as described. The connection to Ostwald's rule of stages provides a conceptual framework that could have broader relevance. However, the manuscript relies heavily on the N∗ theory and AlphaFold-predicted structures, and the evidence presented in the text alone is insufficient to fully evaluate the robustness of the conclusions. The statistical treatment of the mean first-passage times, the validation of the correction procedure, and the sensitivity of the results to model parameters are not fully described in the provided material. The comparison with experimental data is thoughtful, but the reliance on an unpublished cryo-EM structure for validation is a concern. The manuscript is well-written and the logical flow is clear, but the absence of figures and supplementary details limits a complete assessment.

- **Who would be interested in the results, and why** Researchers studying liquid-liquid phase separation, particularly those focused on FUS and related FET family proteins, will find the mechanistic insights into core hierarchy and nucleation relevant. The application of Ostwald's rule of stages to protein condensates will interest the broader biophysics community studying aggregation and self-assembly. Computational biophysicists developing coarse-grained models for intrinsically disordered proteins will be interested in the SOP-IDP application. Experimentalists studying FUS aggregation and ALS pathology may find the predictions regarding core-3 as the initiating region useful for designing experiments.

- **Major strengths** The manuscript addresses a specific, unresolved question with a clear hypothesis. The connection between monomer-encoded excited states and fibril formation kinetics is conceptually elegant. The authors make quantitative predictions (formation order, mutual exclusivity, rate differences) that are testable. The comparison with multiple experimental datasets strengthens the credibility of the model. The discussion of limitations, particularly regarding AlphaFold reliability, is honest and measured.

- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors claim that the true mean first-passage times can be reliably estimated using the correction in Eq. 1, and that the resulting order of formation (core-3 fastest, core-1 slowest) is unambiguous.
- **Evidence pointer** Methods section "True Mean FPT"; Results section "Ostwald's Rule of Stages"; Figure 1I (not provided)
- **Concern** The correction procedure in Eq. 1 assumes exponentially distributed first-passage times. The authors state that the raw distributions are broad and that only a fraction of trajectories reach the N∗ states (42/200 for core-1, 87/200 for core-2, 116/200 and 124/200 for core-3 conformations). The validity of the exponential assumption for these rare-event transitions is not demonstrated in the provided text. If the true distribution is not exponential, the corrected mean values could be substantially biased. The authors mention that the robustness of Eq. 1 was tested against solvable models, but this does not establish its validity for the specific FUS-LC system. The statistical significance of the differences between core-1 and the other cores (P-values 0.02-0.04) is marginal, and the corrected values have large uncertainties that are not fully propagated.
- **Why it matters** The central conclusion of the paper, that formation kinetics are inversely correlated with stability, rests on the reliability of these corrected mean first-passage times. If the correction is biased, the ordering of formation times could change, undermining the Ostwald's rule interpretation.
- **Resolution test** Provide a sensitivity analysis showing that the conclusions are robust to the choice of distribution for the first-passage times. Show the raw distributions of observed first-passage times and demonstrate that the exponential fit is appropriate. Provide confidence intervals for the corrected means that account for both the observed events and the censored trajectories.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors use AlphaFold2 and AlphaFold3 predicted structures for core-3 as reference states to define N∗ conformations and compute mean first-passage times, and claim these predictions are validated by comparison with an unpublished cryo-EM structure.
- **Evidence pointer** Results section "Structural Model for Core-3"; Figure 5 (not provided); Supplementary Figures S15, S16 (not provided)
- **Concern** The entire kinetic analysis for core-3 depends on the reliability of AlphaFold-predicted structures. The authors acknowledge that AlphaFold performance for amyloid structures is questionable, and they note that the unpublished cryo-EM comparison should not be interpreted as broad validation. However, the text does not provide quantitative metrics for how well the AF3 predictions match the experimental structures for core-1 and core-2, nor does it describe the level of agreement with the unpublished core-3 cryo-EM structure. The choice of which AF3-generated models to use (given that AF3 produces diverse models depending on random seeds) is not fully justified. If the reference structures are incorrect, the N∗ states identified in simulations may not correspond to the biologically relevant fibril conformations.
- **Why it matters** The conclusions about core-3 initiating assembly and the inverse correlation between stability and kinetics depend on the accuracy of the reference structures. Without quantitative validation, the results could be artifacts of incorrect reference states.
- **Resolution test** Provide quantitative comparison metrics (e.g., RMSD, TM-score) between AF3 predictions and experimental structures for core-1 and core-2. Describe the selection criteria for choosing among multiple AF3 models. Provide details of the unpublished cryo-EM comparison, including resolution and the specific metrics used to assess agreement.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Scientific importance
- **Claim pointer** The authors claim that their simulations reveal that core-3 residues 164-176 drive droplet nucleation and that this finding has implications for understanding FUS-LC assembly and related low-complexity sequences.
- **Evidence pointer** Results section "Mechanism of Droplet Formation"; Results section "Core 3 Residues Drive FUS-LC Condensation"; Figure 3 (not provided)
- **Concern** The claim that core-3 drives droplet nucleation is based on contact analysis in multichain simulations. However, the text does not describe how the simulations were initialized, how many independent simulations were performed, or how statistical significance was assessed for the preferential contacts. The comparison with experimental truncation data is suggestive but the connection between hydrogel binding and droplet nucleation is not direct. The authors state that core-2 does not influence phase separation, but the text does not provide a mechanistic explanation for why core-2 is excluded from early interactions.
- **Why it matters** The mechanistic claim about core-3 initiating assembly is a key novel finding. If the contact analysis is not statistically robust or if the simulations are biased by initial conditions, the conclusion could be premature.
- **Resolution test** Provide details on simulation initialization, number of independent runs, and statistical analysis of contact frequencies. Show that the preferential core-3 interactions are robust across different initial conditions and simulation parameters.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Technical soundness
- **Claim pointer** The authors claim that the chemical potentials of the coexisting phases are equal, with a relative difference of 0.003 ± 0.03, and that this establishes equilibrium.
- **Evidence pointer** Results section "Chemical Potentials in the Two Phases Are Similar"; Figure 3B (not provided)
- **Concern** The uncertainty in the chemical potential difference (0.03) is an order of magnitude larger than the reported mean (0.003). The authors acknowledge this but proceed to use the equality of chemical potentials to justify equilibrium and calculate coexistence concentrations. The large uncertainty raises questions about whether the system has truly reached equilibrium and whether the calculated coexistence concentrations are reliable. The method for computing chemical potentials is only described in the supplementary information, which is not provided.
- **Why it matters** The calculation of coexistence concentrations and the comparison with experimental values depend on the system being at equilibrium. If equilibrium is not established, the concentration values and the comparison with experiments could be misleading.
- **Resolution test** Provide a more detailed analysis of the chemical potential distributions, including convergence tests over time. Show that the uncertainty decreases with longer simulation times or larger system sizes. Describe the method for computing chemical potentials in sufficient detail to assess its validity.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Readability for nonspecialists
- **Affected element** Introduction of N∗ theory
- **Evidence pointer** Results section "Ostwald's Rule of Stages"
- **Issue** The N∗ theory is introduced briefly with a reference to the supplementary information, but the key concept is not explained clearly enough for readers unfamiliar with the prior work. The relationship between N∗ states, the structural overlap parameter, and the free energy landscape is not immediately transparent.
- **Required correction** Provide a more accessible explanation of the N∗ theory in the main text, perhaps with a schematic figure or a more detailed verbal description of the physical picture.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Technical soundness
- **Affected element** Simulation time scales
- **Evidence pointer** Methods section "SOP-IDP Model"; Results section "Droplet Formation and Ostwald Ripening"
- **Issue** The manuscript reports simulation times in units of τ (simulation time step) and in milliseconds, but the relationship between simulation time and physical time is not clearly stated. The statement that fibril formation occurs on timescales of days in experiments while simulations cover milliseconds is not reconciled.
- **Required correction** Clarify the mapping between simulation time and physical time, or explicitly state that the simulations are not intended to capture the full fibril formation process but rather the early nucleation events.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Scientific importance
- **Affected element** Generalizability claims
- **Evidence pointer** Discussion section "Implication for FUS-LC Assembly"
- **Issue** The authors note similarities with TDP-43 but do not provide a detailed comparison. The claim that Ostwald's rule should apply to TDP-43 is speculative and not supported by data presented in this manuscript.
- **Required correction** Either provide a more detailed comparison with TDP-43 or soften the claim to indicate that this is a hypothesis to be tested.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Technical soundness
- **Affected element** Statistical analysis
- **Evidence pointer** Results section "Sequence-Dependent Modulation of Fibril Formation Kinetics"; Figure 1J (not provided)
- **Issue** The correlation between reconfiguration times and mean first-passage times is stated to be strong, but no correlation coefficient or statistical test is reported in the text.
- **Required correction** Report the correlation coefficient and its significance level.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Readability for nonspecialists
- **Affected element** Terminology
- **Evidence pointer** Throughout
- **Issue** Terms such as "nonpolymorphic cross-β cores," "fuzzy coats," and "Ostwald's rule of stages" are used without sufficient definition for readers outside the immediate field.
- **Required correction** Provide brief definitions or explanations for these terms at first use.

- **Concern ID** R1-m6
- **Severity** Minor
- **Axis** Technical soundness
- **Affected element** Model validation
- **Evidence pointer** Methods section "SOP-IDP Model"
- **Issue** The manuscript states that the SOP-IDP model was used without alterations, but does not describe how the model parameters were validated for FUS-LC specifically. The transferability of the model to this system is asserted but not demonstrated.
- **Required correction** Provide a brief description of previous validation studies or cite specific references that establish the model's applicability to FUS-LC.

- **Technical failings that need to be addressed before the case is established** R1-M1 (statistical reliability of corrected MFPTs), R1-M2 (validation of AlphaFold-predicted structures for core-3)

- **Assessment against Nature-style criteria** 
  - Originality: The application of Ostwald's rule of stages to explain the hierarchical assembly of FUS-LC cores is a novel conceptual contribution. The idea that monomer-encoded excited states determine the order of fibril formation is creative and extends prior work on N∗ states.
  - Scientific importance: The manuscript addresses a significant question in the phase separation field, namely how specific sequence regions drive nucleation and assembly. The findings have potential implications for understanding FUS pathology and related neurodegenerative diseases. However, the importance is somewhat limited by the reliance on computational predictions that require experimental validation.
  - Interdisciplinary readership: The topic bridges biophysics, computational biology, and neurobiology. The conceptual framework of Ostwald's rule could appeal to a broad readership, but the technical details of the simulations may limit accessibility.
  - Technical soundness: The simulation methodology is appropriate for the questions asked, but the statistical treatment of rare events and the reliance on predicted structures raise concerns that need to be addressed. The comparison with experimental data is a strength, but the unpublished cryo-EM validation is a weakness.
  - Readability for nonspecialists: The manuscript is generally well-written, but the introduction of specialized concepts (N∗ theory, structural overlap parameter) could be more accessible. The significance statement is clear and effectively summarizes the key findings.

- **Recommendation posture** Supportive if technical concerns are resolved. The conceptual framework is interesting and the conclusions are potentially important, but the statistical reliability of the key quantitative results and the validation of the AlphaFold-predicted structures must be addressed before the case is fully established.

## Risk / unsupported claims
- The claim that core-3 and core-1 N∗ states are mutually exclusive is based on the observation that the joint probability vanishes in simulations, but the text does not provide a mechanistic explanation for this mutual exclusivity.
- The claim that the predicted core-3 structure shows "reasonable agreement" with an unpublished cryo-EM structure cannot be assessed without quantitative data.
- The statement that deviations from Lifshitz-Slyozov scaling indicate additional physical mechanisms is not supported by a detailed analysis in the provided text.
- The claim that the findings have implications for "related low-complexity sequences" is speculative and not supported by data presented in this manuscript.
- The assertion that the simulations capture the early events of fibril formation despite the timescale gap between simulation (milliseconds) and experiment (days) is not fully justified.