## Review setup
- **Input scope** Full manuscript text (abstract, introduction, applications, integration with experiments, conclusions) and figures captions
- **Assessment boundary** Scientific content, technical accuracy, completeness of the review, clarity of presentation, and alignment with stated aims
- **Shared manuscript claim summary** The authors present a review of Metropolis Monte Carlo (MMC) and kinetic Monte Carlo (KMC) methods applied to protein–protein interactions, covering methodological foundations, coarse-grained model evolution, applications to aggregation, receptor organization, liquid–liquid phase separation, and integration with experimental techniques including SAXS/SANS, single-molecule tracking, and fluorescence-based methods.
- **Visible evidence base** Full text with figure captions (Figures 1–3), reference list partially visible in text citations, no supplementary materials
- **Missing materials affecting confidence** Full reference list with complete bibliographic details, figure images (only captions visible), any supplementary information, and explicit methodological details for how the literature was selected and synthesized

## Reviewer
- **Overall assessment** This is a well-structured and readable review that covers a relevant and timely topic. The authors successfully articulate the complementary roles of MMC and KMC, provide a logical progression from early receptor models to modern coarse-grained approaches, and highlight the growing importance of integrating simulations with experimental data. The manuscript is generally clear and accessible to a broad biophysical audience. However, several technical inaccuracies, an overstatement of the scope of coverage, and a lack of critical depth in certain sections weaken the overall impact. The review would benefit from a more balanced treatment of limitations, a clearer articulation of the field's open challenges, and a more rigorous handling of some methodological descriptions.

- **Who would be interested in the results, and why** Researchers in computational biophysics, molecular simulation, and soft matter physics would find this review useful as an entry point to Monte Carlo methods for protein systems. Experimentalists using SAXS/SANS, single-molecule tracking, or fluorescence techniques who wish to interpret their data with simulation support would also benefit. The review is particularly relevant for graduate students and early-career researchers seeking a concise overview of MMC and KMC applications in protein science.

- **Major strengths** 
  1. Clear conceptual distinction between MMC and KMC, with a helpful schematic (Figure 1) that outlines inputs, workflows, and outputs.
  2. Logical organization that traces the evolution of coarse-grained models from isotropic particles to patchy and polymer representations.
  3. Good coverage of the integration of simulations with experimental techniques, especially the discussion of SAXS/SANS and fluorescence-based methods.
  4. Accessible writing style that avoids unnecessary jargon, making the material approachable for nonspecialists.

- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors state that in MMC, "unfavorable moves are accepted with a probability given by the Boltzmann factor, P=exp(-ΔE/kBT)" and that this "ensures that sampled configurations follow the Boltzmann distribution."
- **Evidence pointer** Introduction, paragraph 3; location not provided
- **Concern** The description of the Metropolis acceptance criterion is incomplete and potentially misleading. The standard Metropolis criterion accepts a move with probability min(1, exp(-ΔE/kBT)), meaning that energetically favorable moves (ΔE < 0) are always accepted, and unfavorable moves are accepted with probability exp(-ΔE/kBT). The text as written implies that all moves are accepted with probability exp(-ΔE/kBT), which is incorrect. Furthermore, the claim that this procedure "ensures" Boltzmann-distributed sampling is an oversimplification; it holds only under conditions of ergodicity and detailed balance, which are not discussed.
- **Why it matters** The Metropolis criterion is the foundational algorithm of MMC. An inaccurate description of this core method undermines the pedagogical value of the review and could mislead readers who are new to the field. The claim about Boltzmann distribution sampling is also too strong without qualification.
- **Resolution test** Revise the description to state that moves are accepted with probability min(1, exp(-ΔE/kBT)), and add a brief qualification that this ensures Boltzmann sampling under conditions of detailed balance and ergodicity.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Scientific importance / Completeness
- **Claim pointer** The authors state that "this review focuses specifically on two widely used approaches, Metropolis Monte Carlo (MMC) and kinetic Monte Carlo (KMC)" and that these are "complementary approaches for investigating equilibrium properties and dynamic molecular processes."
- **Evidence pointer** Abstract and Introduction; location not provided
- **Concern** The review does not adequately address the relationship between MMC and KMC in terms of their respective limitations and the conditions under which one should be preferred over the other. While the authors note that MMC samples equilibrium distributions and KMC describes time evolution, they do not discuss key practical issues such as: (i) the difficulty of defining physically meaningful transition rates for KMC in complex protein systems, (ii) the challenge of achieving ergodic sampling in MMC for rugged energy landscapes, or (iii) the role of time-scale separation in choosing between methods. The review would be substantially stronger if it included a critical comparison of when each method is most appropriate and what their key failure modes are.
- **Why it matters** A review that presents two methods as complementary without critically examining their respective limitations does not provide sufficient guidance for readers who need to choose an appropriate method for their research. This is a missed opportunity to add genuine scientific value beyond a descriptive summary.
- **Resolution test** Add a dedicated section or subsection that critically compares MMC and KMC, discussing their respective strengths, limitations, and typical application regimes, with concrete examples of systems where one method is clearly preferred over the other.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Technical soundness
- **Claim pointer** The authors state that "the same simulation framework can produce observables such as cluster-size distributions, fluorescence recovery curves, and scattering structure factors" and that these "can be directly compared with SAXS/SANS experiments."
- **Evidence pointer** Section "Combining Monte Carlo simulations and experimental approaches", Figure 3 caption; location not provided
- **Concern** The claim that fluorescence recovery curves can be produced from the same simulation framework that generates cluster-size distributions and structure factors is not adequately explained. Fluorescence recovery after photobleaching (FRAP) involves modeling the diffusion of molecules into a bleached region, which requires a fundamentally different simulation setup (e.g., explicit spatial domain, boundary conditions, and photobleaching kinetics) than what is typically used for equilibrium sampling of cluster distributions. The authors do not explain how these different observables are generated within a unified framework, and the text implies a level of integration that may not be accurate.
- **Why it matters** The integration of simulations with experiments is a central theme of the review. If the description of how different observables are generated is inaccurate or unclear, it undermines the credibility of the integration narrative and could mislead readers about the practical workflow.
- **Resolution test** Clarify the relationship between the different observables and the simulation framework. Specify whether the same simulation trajectory is used to compute all observables, or whether different simulation protocols are needed for different experimental comparisons. Provide a concrete example of how a FRAP recovery curve is computed from a simulation.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Scientific importance / Completeness
- **Claim pointer** The authors state that "the integration of MC simulations with experimental techniques is reviewed through applications involving Small Angle X-ray and Neutron Scattering (SAXS/SANS), single-molecule tracking, and fluorescence-based methods."
- **Evidence pointer** Abstract and Section "Combining Monte Carlo simulations and experimental approaches"; location not provided
- **Concern** The coverage of single-molecule tracking and fluorescence-based methods is relatively thin compared to the scattering section. The discussion of single-molecule tracking (Section "Single-molecule tracking and diffusion measurements") is limited to three cited studies with minimal critical analysis. The fluorescence section (Section "Fluorescence-based techniques") is similarly brief. In contrast, the scattering section is more developed. This imbalance is not acknowledged, and the review would benefit from either a more even treatment of all three experimental areas or an explicit statement about why scattering is given more weight.
- **Why it matters** The abstract promises a review of integration with three experimental techniques. If the coverage is uneven, the review does not fully deliver on its stated scope, which is a significant issue for a review article.
- **Resolution test** Either expand the single-molecule and fluorescence sections to match the depth of the scattering section, or revise the abstract and introduction to indicate that scattering is the primary focus with briefer coverage of other techniques.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Readability for nonspecialists
- **Affected element** Introduction, paragraph 2
- **Evidence pointer** Location not provided
- **Issue** The historical anecdote about the origin of Monte Carlo methods during World War II is interesting but is presented without any citation. While this is a well-known historical fact, the lack of a reference is inconsistent with the scholarly style of the rest of the manuscript.
- **Required correction** Add a citation for the historical claim, or rephrase to indicate that this is a well-known historical account.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Technical soundness
- **Affected element** Section "Scattering techniques (SAXS/SANS)"
- **Evidence pointer** Location not provided
- **Issue** The description of the ATSAS suite and its tools (DAMMIN/DAMMIF, GASBOR) is accurate but is presented as a digression from the main topic of protein–protein interactions. The connection between these structure-determination tools and the study of protein–protein interactions is not made explicit.
- **Required correction** Add a sentence explaining how these structure-determination tools are relevant to the study of protein–protein interactions, or move this content to a more appropriate location.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Section "Combining Monte Carlo simulations and experimental approaches"
- **Evidence pointer** Location not provided
- **Issue** The discussion of parameter uncertainty and model validation (paragraph 1) is brief and does not provide concrete guidance for readers. The authors mention that "combining multiple independent experimental observables and explicit assessment of parameter uncertainty are important aspects of robust model validation," but do not give examples of how this is done in practice.
- **Required correction** Add a brief example or reference illustrating how multiple observables are combined to constrain model parameters in a specific system.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Readability for nonspecialists
- **Affected element** Section "Applications of Monte Carlo methods to protein organization and assembly"
- **Evidence pointer** Location not provided
- **Issue** The term "floating bonds" model is introduced without explanation. Nonspecialist readers may not be familiar with this model, and the text does not clarify what it represents or why it is relevant.
- **Required correction** Add a brief explanation of the "floating bonds" model when it is first mentioned.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Technical soundness
- **Affected element** Section "Scattering techniques (SAXS/SANS)"
- **Evidence pointer** Location not provided
- **Issue** The statement that "the scattering measured in SAXS/SANS is directly related to the ensemble-averaged spatial distribution of scattering density elements" is correct but could be more precise. The relationship between the measured intensity and the structure factor is not explicitly stated, which may confuse readers who are not familiar with scattering theory.
- **Required correction** Add a brief equation or verbal description of the relationship between the measured intensity, the form factor, and the structure factor.

- **Technical failings that need to be addressed before the case is established** 
  R1-M1 (inaccurate description of the Metropolis criterion) and R1-M3 (unclear relationship between simulation framework and different observables) are the most significant technical issues. R1-M1 is a factual error in the description of a core algorithm and must be corrected. R1-M3 requires clarification of the methodological workflow to avoid misleading readers.

- **Assessment against Nature-style criteria** 
  - **Originality**: The review does not present new research findings but offers a synthesis of existing work. Its originality lies in the specific framing of MMC and KMC as complementary tools for protein interaction studies. This is a reasonable but not highly novel framing.
  - **Scientific importance**: The topic is important and timely, given the growing interest in biomolecular condensation and phase separation. However, the review does not fully capitalize on this importance by providing a critical perspective on open challenges.
  - **Interdisciplinary readership**: The review has the potential to appeal to a broad audience spanning biophysics, computational biology, and experimental biochemistry. The writing is generally accessible, though some sections assume familiarity with simulation terminology.
  - **Technical soundness**: The description of the Metropolis criterion is inaccurate (R1-M1), and the relationship between simulation frameworks and experimental observables is unclear (R1-M3). These issues must be addressed.
  - **Readability for nonspecialists**: The review is generally well-written and accessible, but some terms and concepts are introduced without sufficient explanation (R1-m4, R1-m5).

- **Recommendation posture** Supportive if technical concerns are resolved. The review addresses a relevant topic and has a clear structure, but the inaccurate description of the Metropolis criterion and the unclear treatment of simulation-observable relationships must be corrected. The uneven coverage of experimental techniques should also be addressed to fully deliver on the stated scope.

## Risk / unsupported claims
- The claim that MMC "ensures" Boltzmann-distributed sampling is an overstatement without qualification regarding detailed balance and ergodicity (R1-M1).
- The claim that the same simulation framework can produce fluorescence recovery curves, cluster-size distributions, and structure factors is not adequately supported by the text (R1-M3).
- The historical account of Monte Carlo method origins is presented without citation (R1-m1).
- The statement that "increasing model complexity does not necessarily translate into greater predictive accuracy" is presented as a general conclusion without specific supporting examples or references.
- The claim that "Reverse Monte Carlo approaches... may aid in bringing more ideas to the table" is vague and not substantiated with concrete examples.