## Review setup
- **Input scope** Full manuscript text (abstract, introduction, methods, results, conclusions, supporting information description)
- **Assessment boundary** Scientific content, methodological soundness, interpretation of results, and alignment with stated claims. No line-by-line editorial or stylistic review.
- **Shared manuscript claim summary** The authors use coarse-grained implicit-solvent molecular dynamics simulations with the HPS model to study the single-chain conformation and phase behavior of hnRNPA1 low-complexity domain variants with different aromatic residue content. They report chain compaction and increased critical temperature with more aromatic residues, more collapsed chains in dilute versus condensed states, density inhomogeneities in condensates near criticality driven by electrostatics, and low interfacial tensions relative to simple liquid mixtures.
- **Visible evidence base** Abstract, full introduction, full methods description, results sections A–C, conclusions, acknowledgments, footnotes. Figures referenced but not provided. Supporting information referenced but not provided.
- **Missing materials affecting confidence** Figures 1–9, tables I–II, supporting information (sequences, additional contact maps, phase diagrams, surface tension data), simulation parameter details beyond those in text, and experimental comparison data from Ref. 44.

## Reviewer
- **Overall assessment** The manuscript addresses a timely and important question in the field of biomolecular condensates: whether single-chain properties can predict phase behavior of IDPs, and how sequence composition, particularly aromatic content, modulates condensation. The authors employ a widely used coarse-grained model and compare against experimental data from a well-characterized system. The work is generally well structured and the conclusions are mostly supported by the described analysis. However, several technical aspects require clarification and additional evidence before the case is fully established, particularly regarding the definition and interpretation of theta temperature, the origin and significance of the reported density inhomogeneities, and the quantitative comparison with experiments.
- **Who would be interested in the results, and why** Researchers studying liquid-liquid phase separation of IDPs, developers and users of coarse-grained models for disordered proteins, and experimentalists investigating hnRNPA1 and related proteins in the context of neurodegenerative disease. The work speaks to the broader question of sequence determinants of phase behavior and the transferability of single-chain measurements to condensed-state properties.
- **Major strengths** The study addresses a relevant and debated question with a systematic approach across sequence variants. The use of a transferable coarse-grained model and direct comparison to experimental data is valuable. The analysis of both single-chain and condensed-state behavior, including contact analysis and surface tension, provides a multifaceted view. The discussion of limitations and potential sources of discrepancy with experiments is thoughtful and constructive.
- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors estimate a theta temperature for A1-LCD (WT) of approximately 277 K based on matching the simulated radius of gyration to the ideal chain value, and use this to argue that the chains are collapsed even above theta conditions.
- **Evidence pointer** Section III A, Figure 1(c), equation (7)
- **Concern** The estimation of theta temperature from a single matching of Rg to the ideal chain value is not well justified. The authors themselves note that the condition T_theta > T_c is not fulfilled, which contradicts expectations from Flory-Huggins theory for upper critical solution temperature systems. The definition of theta conditions for heteropolymers with heterogeneous interactions is conceptually problematic, and the use of a single effective bond length to define the ideal chain reference is an oversimplification. The conclusion that chains are collapsed even above theta temperature relies on this questionable theta estimate.
- **Why it matters** The theta temperature is used as a reference point to interpret the conformational state of the chains and to argue that heteropolymer behavior deviates from homopolymer expectations. If the theta estimate is unreliable, the interpretation of the single-chain data and the comparison to homopolymer theory are weakened.
- **Resolution test** Provide a more rigorous determination of theta conditions, for example by computing the second virial coefficient as a function of temperature and identifying where it vanishes, or by explicitly demonstrating that the chain dimensions follow ideal scaling with N at the claimed theta temperature. Alternatively, reframe the discussion to avoid relying on a precise theta temperature and instead discuss the effective solvent quality directly.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors report density inhomogeneities within condensates near criticality, which they attribute to electrostatic interactions, and state that these inhomogeneities are driven by long-range repulsion between like-charged residues.
- **Evidence pointer** Section III B, Figures 4(b), 4(d), 5
- **Concern** The evidence for electrostatic-driven density inhomogeneities is indirect. The authors show that uncharged chains produce flatter density profiles, but this does not conclusively demonstrate that charge-charge repulsion is the mechanism. Other factors, such as the distribution of hydrophobic residues or finite-size effects, could also contribute. The claim that the depletion at the center is due to like-charge repulsion is plausible but not directly tested. Additionally, the authors state that surface tension was only computed in regimes without pronounced density fluctuations, which limits the characterization of the inhomogeneous regime.
- **Why it matters** The observation of density inhomogeneities is presented as a notable finding with potential implications for condensate internal structure. If the mechanism is not clearly established, the significance of this observation is diminished.
- **Resolution test** Perform additional simulations with modified charge distributions (e.g., neutralizing charges while preserving hydrophobicity) or with varying salt concentrations to directly test the electrostatic mechanism. Alternatively, provide a quantitative analysis correlating local charge density with local density fluctuations.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Scientific importance
- **Claim pointer** The authors state that their findings support the hypothesis that aromatic residues play a dominant role for condensation, and that important properties of condensates are captured in coarse-grained simulations.
- **Evidence pointer** Abstract, Sections III B, III C, Figures 6, 8, 9
- **Concern** The comparison with experiments from Ref. 44 is described as "semi-quantitative agreement," but the quantitative details of this comparison are not presented in the visible text. The critical temperatures from simulations are reported to be 30–50 K lower than experiments, and critical densities about 100 mg/mL higher. The authors attribute these differences to model limitations, but do not provide a systematic analysis of how robust the trends are across the different variants. The claim that aromatic residues dominate condensation is supported by the contact analysis, but the relative contribution of electrostatics versus hydrophobicity is not fully disentangled.
- **Why it matters** The central claim of the paper is that aromatic content drives phase behavior. While the trend is clear, the quantitative discrepancy with experiments and the lack of a detailed error analysis limit the strength of the claim.
- **Resolution test** Provide a more detailed comparison with experimental data, including error bars on simulated critical temperatures and densities, and a discussion of how the model parameters could be adjusted to improve agreement. Consider additional variants or sequence perturbations to further test the role of aromatic residues.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Technical soundness
- **Claim pointer** The authors conclude that "sticker-spacer behavior emerges naturally" in their coarse-grained simulations, and identify charged and aromatic residues as stickers based on contact analysis.
- **Evidence pointer** Section III C, Figures 8, 9
- **Concern** The identification of stickers from contact maps is somewhat circular. The contact analysis identifies which residues form the most contacts, but this does not necessarily mean these residues are the ones driving phase separation. The authors do not provide a quantitative threshold for what constitutes a "sticker" versus a "spacer," and the distinction between distance-based and energy-based criteria is not fully reconciled. The claim that sticker-spacer behavior emerges naturally would be strengthened by a more formal analysis, such as computing per-residue contributions to the free energy of phase separation.
- **Why it matters** The sticker-spacer framework is a popular conceptual model for IDP phase behavior. If the authors claim their simulations support this framework, they should provide a more rigorous demonstration that the identified stickers are indeed the key drivers of condensation.
- **Resolution test** Perform a free energy decomposition or perturbation analysis to quantify the contribution of each residue type to the driving force for phase separation. Alternatively, compare the contact maps with predictions from a formal sticker-spacer model.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Readability
- **Affected element** Section III A, theta temperature discussion
- **Evidence pointer** Section III A
- **Issue** The discussion of theta temperature and its estimation is dense and could be confusing to readers not familiar with polymer physics. The authors introduce the concept, estimate it, and then immediately discuss its limitations, which may obscure the main point.
- **Required correction** Consider restructuring this section to first state the main finding (chains are collapsed in dilute solution), then discuss the theta temperature as a secondary reference point, and clearly separate the estimation from the caveats.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Technical soundness
- **Affected element** Methods, electrostatic interactions
- **Evidence pointer** Section II, equation (3)
- **Issue** The truncation of the electrostatic potential is mentioned but the cutoff value is not stated in the visible text. The choice of truncation can affect phase behavior, especially near criticality.
- **Required correction** State the truncation distance for the electrostatic potential explicitly in the methods section.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Interdisciplinary readership
- **Affected element** Introduction, comparison with experiments
- **Evidence pointer** Section I, Ref. 44
- **Issue** The introduction references experimental work on hnRNPA1 but does not provide sufficient context for readers unfamiliar with this specific system. The relevance of hnRNPA1 to disease is mentioned but not elaborated.
- **Required correction** Add a brief description of hnRNPA1 and its biological relevance, including its role in ALS and other neurodegenerative diseases, to make the work accessible to a broader readership.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Technical soundness
- **Affected element** Section III C, contact analysis
- **Evidence pointer** Section III C, Figures 8, 9
- **Issue** The contact analysis uses both distance-based and energy-based criteria, but the results from the two methods are not systematically compared. It is unclear if they lead to the same conclusions.
- **Required correction** Provide a direct comparison of the contact maps obtained from the two methods, or state explicitly that they are consistent and show only one if they are.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Readability
- **Affected element** Section III B, surface tension
- **Evidence pointer** Section III B, Figure 7
- **Issue** The surface tension values are reported in µN/m, which is an unusual unit for readers familiar with interfacial tensions of simple liquids. The comparison with simple liquid mixtures is made, but the significance of the low values is not fully explained.
- **Required correction** Briefly explain why the surface tensions of protein condensates are expected to be much lower than those of simple liquid mixtures, and what the implications are for condensate properties.

- **Concern ID** R1-m6
- **Severity** Minor
- **Axis** Technical soundness
- **Affected element** Section III B, finite-size scaling
- **Evidence pointer** Section III B, footnote
- **Issue** The authors mention a finite-size scaling analysis but do not provide details in the visible text. The robustness of the critical temperature estimate depends on this analysis.
- **Required correction** Provide a brief description of the finite-size scaling analysis in the main text or refer to the supporting information with a clear summary of the findings.

## Risk / unsupported claims
- The claim that chains are collapsed even above the theta temperature relies on a theta temperature estimate that the authors themselves acknowledge is unreliable.
- The attribution of density inhomogeneities to electrostatic repulsion is plausible but not directly demonstrated.
- The claim that "sticker-spacer behavior emerges naturally" is supported by contact analysis but lacks a formal thermodynamic basis.
- The quantitative comparison with experiments is described as "semi-quantitative" but the details are not fully presented in the visible text.
- The statement that "important properties of condensates are captured in coarse-grained simulations" is broad and not fully substantiated by the specific results shown.
- The surface tension values are compared to simple liquid mixtures, but the significance of the difference is not fully contextualized.
- The claim that the model captures "rich behavior" is somewhat vague and not tied to specific observable predictions that could be tested experimentally.