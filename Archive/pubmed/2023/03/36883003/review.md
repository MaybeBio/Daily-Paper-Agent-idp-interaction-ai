## Review setup
- **Input scope** Full manuscript text (abstract, significance, introduction, materials and methods, results and discussion, conclusions, author contributions, supporting material statement, acknowledgments)
- **Assessment boundary** Scientific content, methodological soundness, internal consistency, and support of claims by the evidence presented in the provided text. Figures are referenced but not directly viewable; assessment relies on figure captions and textual descriptions.
- **Shared manuscript claim summary** The authors use multiscale simulations (residue/nucleotide-resolution coarse-grained Mpipi model and a minimal patchy-particle model) to show that RNA length and concentration jointly control the thermodynamic stability of RNA-protein condensates. They report that longer RNAs enhance condensate stability more effectively and allow higher RNA concentrations before destabilization, and that in mixed-length systems, short RNAs accumulate at the condensate surface acting as surfactants while long RNAs localize to the core acting as scaffolds.
- **Visible evidence base** Text descriptions of simulation methods, phase diagram data (Fig. 1b-d), density profiles (Fig. 3a-e), surface tension calculations (Fig. 3f), patchy-particle model results (Fig. 4b-c), and references to supporting figures S1 and S2.
- **Missing materials affecting confidence** Actual figure images, simulation parameter tables, force field details, convergence criteria, error bars or uncertainty quantification, system size details, and the full supporting material document. These are referenced but not provided in the submitted text.

## Reviewer
- **Overall assessment** This manuscript presents a systematic computational study of how RNA length and concentration jointly modulate the thermodynamic stability of protein-RNA condensates. The work combines a sequence-resolved coarse-grained model (Mpipi) with a minimal patchy-particle model to argue that the observed behaviors are general physical phenomena. The central claims, that longer RNAs enhance stability more effectively and that length-dependent spatial segregation (short at surface, long in core) occurs in mixed systems, are interesting and potentially significant. However, the manuscript as presented has several issues that need to be addressed. The distinction between "surfactant" and "scaffold" roles is used somewhat loosely, and the mechanistic explanation for why short RNAs act as better surfactants is not fully developed. The comparison between the two models is qualitative, and the quantitative relationship between the patchy-particle parameters and the real molecular system is not established. The claim that RNA diversity should be considered in assessing condensate regulation is reasonable but somewhat beyond what the simulations directly demonstrate. The writing is generally clear, though some sections could be tightened. Overall, the work is potentially valuable, but the case would be strengthened by more rigorous treatment of uncertainties and a clearer articulation of what is novel relative to prior work.
- **Who would be interested in the results, and why** Researchers studying biomolecular condensates, particularly those interested in the role of RNA in phase separation. This includes experimentalists working on FUS, TDP-43, and related RNA-binding proteins, as well as computational biologists developing coarse-grained models of LLPS. The findings on length-dependent surfactant/scaffold behavior could inform interpretations of experiments with heterogeneous RNA populations. The patchy-particle model results may interest soft-matter physicists working on colloidal systems with polymer additives.
- **Major strengths** 1) The study addresses an important and timely question: how RNA length, not just concentration, modulates condensate stability. 2) The use of two complementary models (sequence-resolved and minimal) is a good strategy for arguing generality. 3) The finding of length-dependent spatial segregation (short at surface, long in core) is novel and mechanistically interesting. 4) The connection to the Henninger et al. transcriptional condensate model provides biological context. 5) The writing is generally accessible and the figures appear well-designed based on captions.
- **Major Concerns** See detailed items below.
- **Minor Comments** See detailed items below.
- **Technical failings that need to be addressed before the case is established** R1-M1 (quantitative comparison between models), R1-M2 (mechanistic basis for surfactant behavior), R1-M3 (uncertainty quantification), R1-M4 (novelty relative to prior work).
- **Assessment against Nature-style criteria** Originality: The finding of length-dependent spatial segregation of RNAs in condensates is novel, though the general reentrant behavior is known. Scientific importance: Potentially high for the condensate field, as it provides a mechanistic framework for understanding RNA length effects. Interdisciplinary readership: The work bridges biophysics, soft matter, and cell biology, and should be accessible to a broad audience. Technical soundness: The simulation methods are appropriate, but the lack of uncertainty quantification and the qualitative nature of the model comparison weaken the technical case. Readability for nonspecialists: The manuscript is generally well-written, but the distinction between surfactant and scaffold roles could be explained more clearly for readers outside the field.
- **Recommendation posture** Supportive if technical concerns are resolved. The core findings are interesting and potentially significant, but the manuscript needs to address the issues around quantitative rigor, mechanistic explanation, and novelty before the case is fully established.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors claim that the patchy-particle model "captures" the behavior observed in the Mpipi simulations, and that the combined results demonstrate that the effects are governed by "general physical parameters like the molecular valency, binding affinity, and polymer length."
- **Evidence pointer** Fig. 4b-c and accompanying text in "Self-organizing polymers trigger concentration-dependent reentrant phase behavior of colloidal patchy-particle condensates modulated by polymer length"
- **Concern** The comparison between the Mpipi and patchy-particle models is purely qualitative. The authors state that the patchy model reproduces the trends (longer polymers enhance stability more, shift reentrant peak to higher ratios), but no quantitative comparison is made. For example, the magnitude of the enhancement (50% for cognate, 8% for scaffold in the patchy model) is not compared to the corresponding values from the Mpipi simulations. Without a quantitative mapping between the two models, the claim that the patchy model "captures" the behavior is not fully supported. The authors should either provide a quantitative comparison (e.g., scaling collapse, mapping of parameters) or temper the claim to "qualitative agreement."
- **Why it matters** The central argument of the paper is that the observed effects are general physical phenomena. This claim rests on the agreement between the two models. If the agreement is only qualitative, the strength of the generality claim is weakened.
- **Resolution test** Provide a quantitative comparison between the Mpipi and patchy-particle results, such as a scaling collapse of the critical temperature versus polymer length/ratio data, or a clear statement of the limitations of qualitative agreement.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Scientific importance
- **Claim pointer** The authors claim that short RNAs act as "natural biomolecular surfactants" that stabilize condensates by reducing interfacial free energy, while long RNAs act as scaffolds that enhance internal connectivity.
- **Evidence pointer** Fig. 3a-f and accompanying text in "RNA length and concentration determine the internal organization of molecules in RNA-protein condensates and the properties of their interfaces"
- **Concern** The surfactant/scaffold dichotomy is presented as a clear mechanistic distinction, but the evidence for the surfactant mechanism is indirect. The authors show that short RNAs accumulate at the interface and that the interfacial free energy is lower when short RNAs are present. However, they do not directly demonstrate that the reduction in interfacial free energy is the cause of the enhanced stability. An alternative explanation is that the short RNAs simply reduce the electrostatic repulsion at the interface by being less charged per molecule, or that the effect is entropic. The authors should either provide a more direct mechanistic test (e.g., decomposing the free energy into enthalpic and entropic contributions) or soften the claim.
- **Why it matters** The surfactant/scaffold framework is a key conceptual contribution of the paper. If the mechanistic basis is not firmly established, the framework may be seen as descriptive rather than explanatory.
- **Resolution test** Perform a free energy decomposition (e.g., enthalpic vs. entropic contributions to the interfacial free energy) or provide additional simulations that directly test the proposed mechanism.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors report critical temperatures and density profiles from simulations, and compare conditions across different RNA lengths and concentrations.
- **Evidence pointer** Figs. 1b-d, 3a-f, and associated text
- **Concern** No uncertainty quantification is provided for any of the reported quantities. Critical temperatures are estimated from phase diagrams, but no error bars or confidence intervals are given. Density profiles are shown as single curves without indication of run-to-run variability. The comparison between NpT and direct coexistence methods (Fig. 1b) is presented as validation, but the agreement is only described qualitatively. Given that the conclusions rely on differences in critical temperatures (e.g., 20% enhancement for PR25 with longer RNA), it is essential to know whether these differences are significant relative to statistical uncertainty.
- **Why it matters** Without uncertainty quantification, the reader cannot assess the robustness of the reported trends. This is particularly important for the claims about the magnitude of the RNA length effect and the shift in the reentrant peak.
- **Resolution test** Provide error bars or confidence intervals for all reported quantities, and state the number of independent simulations or blocks used for averaging.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Originality
- **Claim pointer** The authors state that "RNA length has been shown to mediate condensate reentrant phase behavior" and cite reference 53, but the novelty of their contribution is not clearly positioned relative to this prior work.
- **Evidence pointer** Introduction and Discussion sections
- **Concern** The manuscript would benefit from a clearer statement of what is new relative to prior computational and experimental studies. The authors mention that previous work has shown reentrant behavior and that longer RNAs stabilize condensates, but the specific new contributions (e.g., the spatial segregation mechanism, the systematic length-concentration phase diagram) are not explicitly highlighted. A more explicit statement of novelty would help the reader understand the advance.
- **Why it matters** For a broad-audience journal, it is important to clearly articulate the advance over prior work.
- **Resolution test** Add a paragraph in the introduction or discussion that explicitly states what is new in this study relative to prior work, and how the findings extend or challenge existing understanding.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Readability
- **Affected element** Abstract
- **Evidence pointer** Abstract, first sentence
- **Issue** The title and abstract use the "Surfactants or scaffolds?" framing, but the distinction is not defined in the abstract. A reader unfamiliar with the surfactant/scaffold concept in the condensate field may be confused.
- **Required correction** Briefly define what is meant by surfactant and scaffold in the abstract, or rephrase to avoid the jargon.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Technical soundness
- **Affected element** Methods, NpT simulations
- **Evidence pointer** Materials and methods, "To determine the stability of RNA-protein condensates, we evaluate the phase diagrams..."
- **Issue** The description of how critical temperatures are estimated from NpT simulations is vague. The text states that an interval is estimated, but the procedure for defining this interval is not described.
- **Required correction** Provide a more detailed description of the procedure for estimating critical temperatures from NpT simulations, including the criteria for determining stability versus instability.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Readability
- **Affected element** Results, Fig. 3
- **Evidence pointer** Fig. 3 caption and associated text
- **Issue** The density profiles in Fig. 3 are described as showing "considerable differences" in distribution, but the quantitative scale of these differences is not discussed. It is unclear whether the segregation is strong or subtle.
- **Required correction** Provide quantitative measures of the segregation (e.g., enrichment ratios, interfacial widths) in the text.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Technical soundness
- **Affected element** Results, patchy-particle model
- **Evidence pointer** Fig. 4 and associated text
- **Issue** The patchy-particle model uses polymer chains of 10, 20, 50, and 100 beads, but the mapping to real RNA lengths (in nucleotides) is not stated. The authors mention that each bead accounts for ~5 nt, but this is only in the figure caption.
- **Required correction** State the bead-to-nucleotide mapping in the main text, and discuss whether the range of polymer lengths explored is representative of biologically relevant RNA lengths.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Readability
- **Affected element** Discussion
- **Evidence pointer** Conclusions section
- **Issue** The discussion of implications for transcriptional condensates (Henninger et al.) is brief and somewhat speculative. The connection between the simulation results and the biological context could be developed further.
- **Required correction** Expand the discussion of biological implications, or clearly label this as speculation.

## Risk / unsupported claims
- The claim that short RNAs act as "natural biomolecular surfactants" is not fully supported by direct mechanistic evidence; the reduction in interfacial free energy is demonstrated, but the causal link to stability enhancement is inferred.
- The claim that the patchy-particle model "captures" the behavior of the Mpipi model is only supported qualitatively; no quantitative comparison is provided.
- The claim that "RNA diversity should be considered when assessing the impact of RNA on biomolecular condensates regulation" is a reasonable extrapolation but goes beyond what the simulations directly demonstrate.
- The statement that "longer RNAs increase both the maximum concentration of RNA that condensates can incorporate before dissolving, and their range of stability" is supported for the specific systems studied, but the generality across different protein-RNA combinations is not established.
- The biological implications for neurodegenerative disorders are speculative and not directly tested in this work.