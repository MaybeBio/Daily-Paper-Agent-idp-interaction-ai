## Review setup
- **Input scope** Abstract only
- **Assessment boundary** Claims and evidence presented in the abstract; no access to full text, figures, tables, or supplementary materials
- **Shared manuscript claim summary** The authors use a computational pipeline combining transition path generation, extensive molecular dynamics simulation, and Markov state model analysis to characterize the conformational transition of the intrinsically disordered hypervariable region (HVR) of K-Ras4B from a disordered to an ordered alpha-helical state. They report a stepwise transition pathway, identify key conformational substates, and propose specific HVR-catalytic domain interactions relevant to K-Ras4B mild mutations in congenital developmental anomaly syndromes.
- **Visible evidence base** Abstract text only; no quantitative results, methodological details, or validation metrics are provided
- **Missing materials affecting confidence** Full manuscript, all figures and tables, simulation parameters, convergence criteria, Markov state model validation, and any experimental or clinical correlation data

## Reviewer
- **Overall assessment** The abstract presents a potentially interesting computational study addressing a biologically relevant question, namely the conformational behavior of the K-Ras4B HVR and its transition to an ordered state. However, the abstract provides insufficient methodological detail and no quantitative evidence to evaluate the robustness of the Markov state model, the convergence of the simulations, or the biological significance of the proposed interactions. The claim that specific HVR-catalytic domain interactions "highlight the pathogenesis" of mutations in congenital syndromes is not supported by the evidence presented in the abstract, as no mutational analysis or functional correlation is described. The study may be of interest to computational biophysicists and Ras biologists, but the current abstract does not establish the case for the broader conclusions.
- **Who would be interested in the results, and why** Computational biophysicists interested in conformational transitions of intrinsically disordered proteins and Markov state model applications would find the methodological approach relevant. Ras biologists and cancer researchers studying K-Ras4B regulation, membrane anchoring, and isoform-specific signaling would be interested in the proposed HVR dynamics and its potential role in autoinhibition. Clinicians or geneticists studying congenital developmental anomaly syndromes associated with K-Ras4B mutations might also be interested, though the abstract does not provide sufficient evidence to substantiate the clinical relevance.
- **Major strengths** The study addresses a biologically important and understudied question, namely the large-scale conformational transition of an intrinsically disordered region in a key oncogenic protein. The computational approach, combining transition path generation, extensive molecular dynamics, and Markov state models, is appropriate for studying rare conformational events and could provide mechanistic insight not accessible by experimental methods alone. The focus on the HVR-catalytic domain interface is timely given the growing interest in K-Ras4B isoform-specific regulation.
- **Major Concerns**  
  - R1-M1  
  - R1-M2  
  - R1-M3  
  - R1-M4
- **Minor Comments**  
  - R1-m1  
  - R1-m2  
  - R1-m3
- **Technical failings that need to be addressed before the case is established** R1-M1, R1-M2, R1-M3, R1-M4
- **Assessment against Nature-style criteria**  
  - Originality: The application of Markov state models to the K-Ras4B HVR transition is a novel combination, but the abstract does not clearly distinguish it from prior computational studies of Ras dynamics or intrinsically disordered protein folding.  
  - Scientific importance: The topic is important for understanding K-Ras4B regulation, but the abstract does not demonstrate that the findings change current understanding or have predictive power.  
  - Interdisciplinary readership: The work could appeal to both computational and experimental biologists, but the abstract is written in a way that assumes familiarity with Markov state models and molecular dynamics, which may limit accessibility.  
  - Technical soundness: Cannot be assessed from the abstract alone. No convergence criteria, model validation, or error estimates are provided.  
  - Readability for nonspecialists: The abstract is concise but uses jargon without explanation, and the link between simulation results and disease pathogenesis is asserted rather than explained.
- **Recommendation posture** Currently not established from the provided evidence. The abstract suggests a potentially valuable study, but the lack of methodological detail and quantitative results prevents assessment of the core claims. A revised abstract with explicit validation metrics and a clearer link between simulation findings and biological or clinical relevance would be needed to support the conclusions.

### Major Concerns

- **Concern ID** R1-M1  
- **Severity** Major  
- **Blocking** Yes  
- **Axis** Technical soundness  
- **Claim pointer** The authors claim that "extensive molecular dynamics simulation and Markov state model analysis" reveal a stepwise transition pathway and key conformational substates.  
- **Evidence pointer** Abstract only; no simulation details, convergence metrics, or model validation are provided  
- **Concern** The abstract provides no information on the length of the simulations, the number of replicas, the force field used, the criteria for Markov state model construction, or the validation of the model (e.g., Chapman-Kolmogorov tests, implied timescales, or statistical uncertainties). Without these details, the reliability of the reported pathway and substates cannot be evaluated.  
- **Why it matters** Markov state models are only as reliable as the underlying sampling and the validation of the model. If the simulations are not converged or the model is not validated, the reported transition pathway and substates may be artifacts of insufficient sampling or poor model choice.  
- **Resolution test** Provide in the full manuscript or a revised abstract the simulation length, number of independent trajectories, force field parameters, and Markov state model validation metrics, including implied timescale plots and Chapman-Kolmogorov tests, to demonstrate that the model is statistically robust.

- **Concern ID** R1-M2  
- **Severity** Major  
- **Blocking** Yes  
- **Axis** Support for claims  
- **Claim pointer** The authors claim that "key interactions between the HVR and the catalytic domain are unraveled, highlighting the pathogenesis of K-Ras4B mild mutations in several congenital developmental anomaly syndromes."  
- **Evidence pointer** Abstract only; no mutational data, functional assays, or clinical correlation are described  
- **Concern** The abstract asserts a direct link between specific HVR-catalytic domain interactions and the pathogenesis of congenital syndromes, but no evidence is presented to support this connection. No specific mutations are named, no structural or energetic analysis of mutant effects is described, and no comparison to known clinical phenotypes is provided.  
- **Why it matters** The claim of clinical relevance is a major conclusion of the abstract. Without evidence linking the simulated interactions to specific mutations and their known pathogenic effects, this claim is unsupported and could be misleading to readers who may interpret it as a validated finding.  
- **Resolution test** In the full manuscript, provide a detailed analysis of the specific mutations associated with congenital syndromes, show how these mutations alter the HVR-catalytic domain interactions in the simulations, and discuss how these changes correlate with known clinical severity or phenotype. If such data are not available, the abstract should be revised to present the interactions as a hypothesis rather than a demonstrated pathogenic mechanism.

- **Concern ID** R1-M3  
- **Severity** Major  
- **Blocking** Yes  
- **Axis** Reproducibility  
- **Claim pointer** The authors state that they "deploy a computational scheme that integrates a transition path-generation algorithm, extensive molecular dynamics simulation, and Markov state model analysis."  
- **Evidence pointer** Abstract only; the specific transition path-generation algorithm is not named or described  
- **Concern** The abstract does not identify the transition path-generation algorithm used, nor does it describe how the initial paths were generated, how they were refined, or how they were integrated with the molecular dynamics simulations. Without this information, the methodology cannot be reproduced or assessed for appropriateness.  
- **Why it matters** Reproducibility is a core requirement for computational studies. The choice of path-generation algorithm can significantly influence the resulting pathways and substates, and the lack of detail prevents other researchers from replicating or building on the work.  
- **Resolution test** Specify the name and version of the transition path-generation algorithm, describe the protocol for generating and refining initial paths, and explain how these paths were used to seed the molecular dynamics simulations. This information should be included in the full manuscript and summarized in the abstract if space permits.

- **Concern ID** R1-M4  
- **Severity** Major  
- **Blocking** No  
- **Axis** Completeness of evidence  
- **Claim pointer** The authors claim that the HVR transition follows a "stepwise pathway" and that "several key conformational substates" are uncovered.  
- **Evidence pointer** Abstract only; no free energy landscape, transition rates, or population distributions are provided  
- **Concern** The abstract does not provide any quantitative description of the pathway, such as the number of substates, their relative populations, the free energy barriers between them, or the timescales of transitions. Without these data, the "stepwise" nature of the pathway and the significance of the substates cannot be evaluated.  
- **Why it matters** The central claim of the study is the characterization of the transition pathway. Quantitative details are essential to assess whether the pathway is thermodynamically and kinetically meaningful and to compare it with alternative models or experimental observations.  
- **Resolution test** In the full manuscript, present a free energy landscape or a kinetic network with clear substate definitions, populations, and transition rates. In the abstract, include at least one quantitative metric, such as the number of substates or the dominant transition timescale, to support the claim of a stepwise pathway.

### Minor Comments

- **Concern ID** R1-m1  
- **Severity** Minor  
- **Axis** Clarity  
- **Affected element** Abstract wording  
- **Evidence pointer** Abstract, sentence on "ensemble favoring an ordered alpha-helical structure"  
- **Issue** The phrase "ensemble favoring an ordered alpha-helical structure" is ambiguous. It is unclear whether the authors mean that the HVR adopts a single stable alpha-helix or that the ensemble contains a mixture of conformations with a higher population of helical states.  
- **Required correction** Clarify whether the ordered state is a single dominant conformation or a set of helical conformations, and specify the helical content or structural criteria used to define "ordered."

- **Concern ID** R1-m2  
- **Severity** Minor  
- **Axis** Terminology  
- **Affected element** Abstract, "autoinhibited state"  
- **Evidence pointer** Abstract, first paragraph  
- **Issue** The term "autoinhibited state" is used without defining the structural or functional criteria for autoinhibition. It is not clear whether this refers to a specific conformation, a binding interaction, or a functional outcome.  
- **Required correction** Define what is meant by autoinhibition in this context, for example, the specific HVR-catalytic domain contacts that prevent effector binding or signaling.

- **Concern ID** R1-m3  
- **Severity** Minor  
- **Axis** Scope  
- **Affected element** Abstract, final sentence  
- **Evidence pointer** Abstract, "regulation of K-Ras4B activity at an atomic level"  
- **Issue** The claim of providing "an atomic level" understanding is overstated given that the study is based on simulations and the abstract does not report any experimental validation.  
- **Required correction** Soften the claim to "provide a detailed molecular view" or "offer a structural hypothesis" to align with the computational nature of the study.

## Risk / unsupported claims
- The claim that specific HVR-catalytic domain interactions "highlight the pathogenesis" of K-Ras4B mild mutations in congenital syndromes is unsupported by the abstract, as no mutational or clinical data are presented.
- The claim of a "stepwise pathway" and "key conformational substates" is unsupported without quantitative free energy or kinetic data.
- The overall conclusion that the findings provide "a deeper understanding of the HVR transition mechanism and the regulation of K-Ras4B activity at an atomic level" is not assessable from the abstract alone, as no validation or comparison to experimental data is provided.