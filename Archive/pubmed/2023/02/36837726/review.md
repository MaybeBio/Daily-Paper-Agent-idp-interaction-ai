## Review setup
- **Input scope** Full manuscript text
- **Assessment boundary** Scientific content, technical soundness, and clarity of the review article, as provided in the manuscript
- **Shared manuscript claim summary** The manuscript reviews and synthesizes recent theoretical, experimental, and computational results on the adhesion of condensate droplets to biomembranes and vesicles, proposing a unified framework based on fluid elasticity to describe adhesion morphologies, wetting transitions, nanotube formation, and engulfment/endocytosis.
- **Visible evidence base** Full text including abstract, introduction, sections 2–14, equations, figure references, and acknowledgments
- **Missing materials affecting confidence** Figures and tables referenced but not provided; no supplementary information; no explicit literature citations list beyond in-text references

## Reviewer
- **Overall assessment** This is a well-structured and authoritative review by a leading researcher in the field. The manuscript provides a coherent theoretical framework for understanding condensate droplet–membrane interactions, integrating analytical theory, simulations, and experiments. The writing is clear and logically organized, with a useful top-down structure from macroscopic to molecular scales. The main weakness is the lack of accessible figures and tables in the provided material, which limits full evaluation of the visual evidence. The review is likely to be of significant interest to researchers in biophysics, soft matter, and membrane biology.
- **Who would be interested in the results, and why** Researchers in biophysics, soft matter physics, membrane biology, and cellular biology, particularly those studying phase separation, membrane remodeling, endocytosis, and biomolecular condensates. The framework presented is broadly applicable and will interest both experimentalists and theorists.
- **Major strengths** 1) Provides a unified theoretical framework (fluid elasticity) that connects diverse observations across scales. 2) Integrates experimental, theoretical, and simulation approaches, reflecting a comprehensive understanding. 3) Clearly identifies key physical parameters (e.g., affinity contrast, line tension, spontaneous curvature) and their roles. 4) Well-organized with a logical progression from qualitative morphologies to quantitative theory. 5) Includes an outlook with open questions, which is valuable for guiding future research.
- **Major Concerns** 1) The manuscript relies heavily on figures and tables that are not provided, making it impossible to fully assess the empirical support for several claims. 2) The review is largely based on the author's own work, which may introduce bias in the selection and interpretation of results. 3) Some claims about the universality of the framework may be overstated given the limited range of systems discussed. 4) The treatment of alternative theoretical approaches or conflicting experimental observations is limited.
- **Minor Comments** 1) The abstract is dense and could benefit from a clearer statement of the review's scope and main conclusions. 2) Some terminology (e.g., "affinity contrast") is introduced without immediate intuitive explanation. 3) The section on protein condensates is brief and could be expanded to better connect to the broader condensate literature. 4) The acknowledgments are detailed but could be shortened for a journal format.
- **Technical failings that need to be addressed before the case is established** 1) The manuscript claims that the "no kink" requirement leads to smoothly curved membranes, but the derivation of intrinsic contact angles from this requirement is not fully detailed. 2) The threshold for droplet adhesion (Equation 53) is presented without a full derivation or discussion of its assumptions. 3) The role of line tension in determining neck shape is discussed, but the relationship between line tension sign and molecular interactions is not fully explained.
- **Assessment against Nature-style criteria** Originality: High. The review presents a novel synthesis of existing results into a unified framework, which is a valuable contribution. Scientific importance: High. The topic is of broad relevance to understanding cellular processes involving condensates and membranes. Interdisciplinary readership: Moderate to high. The work bridges physics, chemistry, and biology, but the technical depth may limit accessibility to non-specialists. Technical soundness: Good, but with some gaps in derivations and reliance on unpublished or not-fully-described data. Readability for nonspecialists: Moderate. The writing is clear but assumes familiarity with membrane physics and phase separation concepts.
- **Recommendation posture** Supportive if technical concerns are resolved and figures/tables are made available for full evaluation.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence sufficiency
- **Claim pointer** The manuscript claims that the "no kink" requirement leads to smoothly curved membranes and defines intrinsic contact angles, but the derivation is not fully presented.
- **Evidence pointer** Section 9, Equations (44)–(46)
- **Concern** The transition from apparent to intrinsic contact angles is a key theoretical step, but the manuscript does not provide a complete derivation or justification for why the "no kink" requirement is universally valid. The relationship between the intrinsic contact angles and the underlying molecular interactions is asserted but not derived from a microscopic model.
- **Why it matters** This is a central claim of the review, and if the derivation is incomplete or the assumptions are not clearly stated, the framework's applicability to other systems is uncertain.
- **Resolution test** Provide a more detailed derivation of the intrinsic contact angles from the "no kink" requirement, including the assumptions and limitations. Alternatively, cite a prior publication where the full derivation is given and summarize the key steps.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence sufficiency
- **Claim pointer** The manuscript claims that the threshold for droplet adhesion is given by Equation (53), but the derivation is not shown and the role of spontaneous curvature and line tension is only qualitatively discussed.
- **Evidence pointer** Section 9.6, Equation (53)
- **Concern** The threshold radius for adhesion is a key quantitative prediction, but the manuscript does not show how it is derived from the shape functional. The effects of spontaneous curvature and line tension on this threshold are mentioned but not quantified.
- **Why it matters** This threshold is experimentally testable, and a clear derivation would strengthen the framework and guide experimental design.
- **Resolution test** Provide a step-by-step derivation of Equation (53) from the shape functional, including the assumptions made. Discuss how the threshold changes with spontaneous curvature and line tension, and compare with any available experimental or simulation data.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Scope and generalizability
- **Claim pointer** The manuscript claims that the framework of fluid elasticity applies to condensate droplets irrespective of molecular composition, but the evidence presented is largely based on PEG-dextran and a few other systems.
- **Evidence pointer** Sections 3 and 14
- **Concern** The review focuses heavily on PEG-dextran systems and a limited number of protein condensates. The claim of universality is not fully supported by the range of examples discussed. The role of specific molecular interactions (e.g., electrostatic, hydrophobic) in determining the key parameters is not systematically addressed.
- **Why it matters** If the framework is to be applied broadly to biological condensates, it is important to understand its limitations and the conditions under which it holds.
- **Resolution test** Expand the discussion to include a wider range of condensate systems, or explicitly state the conditions under which the framework is expected to apply. Discuss how molecular interactions map onto the key parameters (e.g., affinity contrast, line tension).

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Abstract
- **Evidence pointer** Abstract
- **Issue** The abstract is dense and lists many concepts without a clear narrative. It could better highlight the main message and the significance of the review.
- **Required correction** Rewrite the abstract to state the main question, the approach, and the key conclusions more explicitly, with a focus on the broader implications.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Terminology
- **Affected element** Section 6.2
- **Evidence pointer** Section 6.2, Equation (15)
- **Issue** The term "affinity contrast" is introduced without an intuitive explanation of its physical meaning. It is defined mathematically but not connected to the underlying physics.
- **Required correction** Add a brief explanation of what the affinity contrast represents physically (e.g., the difference in adhesion energy per area between the two phases) and why it is a useful parameter.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Section 3.3
- **Evidence pointer** Section 3.3
- **Issue** The section on protein condensates is brief and does not provide a detailed comparison with the PEG-dextran systems. The phase diagram in Figure 7 is mentioned but not described in detail.
- **Required correction** Expand this section to include a more detailed description of the phase behavior of protein condensates and how it compares to the synthetic polymer systems. If possible, include a discussion of the molecular features that determine the phase behavior.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Readability
- **Affected element** Section 10
- **Evidence pointer** Section 10
- **Issue** The section on nanotube formation is detailed but could benefit from a summary of the key conditions for nanotube formation and the role of each parameter.
- **Required correction** Add a brief summary at the end of the section that lists the key conditions for nanotube formation and the role of spontaneous curvature, adhesion energy, and other parameters.

## Risk / unsupported claims
- The claim that the framework applies to all condensate droplets irrespective of molecular composition is not fully supported by the evidence presented, which is limited to a few systems.
- The quantitative predictions for the adhesion threshold (Equation 53) and the effects of line tension on neck shape are not fully derived or compared with experimental data.
- The role of spontaneous curvature in nanotube formation is discussed, but the relationship between spontaneous curvature and molecular interactions is not quantified.
- The claim that negative line tension prevents fission and endocytosis is based on simulations but is not directly verified experimentally.
- The discussion of membrane fusion and its relation to condensate fusion is speculative and not supported by specific data.