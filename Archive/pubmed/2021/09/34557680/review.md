## Review setup
- **Input scope** Full manuscript text, including abstract, introduction, results, discussion, conclusions, methods, and figure legends.
- **Assessment boundary** The scientific claims, methodological approach, data analysis, and interpretation as presented in the manuscript. The review does not assess the suitability for a specific journal.
- **Shared manuscript claim summary** The manuscript claims that the surface charge properties of folded domains, specifically the local distribution and accessibility of charged residues, can influence the conformational behavior of adjacent intrinsically disordered tails. This is supported by all-atom implicit solvent simulations of designed superfolder GFP variants with attached polyelectrolytic tails, a bioinformatic analysis of human proteins with disordered tails, and simulations of natural coronavirus nucleocapsid protein constructs.
- **Visible evidence base** The evidence base includes simulation results presented as scaling maps, internal scaling profiles, 3D contour volume plots, and bioinformatic analyses of protein sequences and structures. The methods section describes the simulation and analysis protocols.
- **Missing materials affecting confidence** The supplementary figures and tables, which are referenced extensively in the text, were not provided for review. This limits the ability to fully evaluate the robustness of the bioinformatic analyses and the detailed simulation parameters.

## Reviewer
- **Overall assessment** This manuscript addresses an important and under-explored question in the field of intrinsically disordered proteins: how the charge properties of folded domains influence the conformational behavior of attached disordered tails. The authors combine a systematic simulation study on designed proteins with a bioinformatic analysis of natural proteins and a case study on coronavirus nucleocapsid proteins. The work is conceptually interesting and the conclusions are potentially significant. However, the manuscript has several technical and presentational issues that need to be addressed. The reliance on a single simulation model (ABSINTH) without experimental validation for the designed systems is a concern. The bioinformatic analysis, while interesting, is descriptive and the link to the simulation findings could be strengthened. The case study on nucleocapsid proteins is compelling but would benefit from a more detailed quantitative comparison. Overall, the core message is plausible and important, but the current presentation does not fully establish the case.
- **Who would be interested in the results, and why** Researchers in the fields of intrinsically disordered proteins, protein biophysics, computational biology, and structural biology would be interested. The work is relevant to understanding how disordered regions function in the context of full-length proteins, which is crucial for understanding protein function, regulation, and mechanisms of disease. The findings on the importance of local charge patches over net charge could have implications for protein engineering and design.
- **Major strengths**
    1.  The study addresses a novel and important question that is the inverse of most prior work in the field.
    2.  The use of a systematic, designed set of protein variants allows for a controlled exploration of the parameter space.
    3.  The combination of simulations on designed proteins with a bioinformatic analysis of natural proteins and a specific case study provides a multi-pronged approach.
    4.  The finding that local charge patches, rather than net charge, can dictate IDR behavior is a significant and non-obvious insight.
    5.  The manuscript is generally well-written and the figures are informative.
- **Major Concerns**
    - **R1-M1**
        - **Severity** Major
        - **Blocking** Yes
        - **Axis** Technical soundness
        - **Claim pointer** The claim that the observed conformational behavior of the designed (GSE)n and (GSK)n tails attached to GFP variants is a general principle governing IDR-FD interactions.
        - **Evidence pointer** Results section, Figures 3-6, Methods section "All-atom implicit solvent simulations".
        - **Concern** The central conclusions are drawn from all-atom simulations using a single force field (ABSINTH) and a single implicit solvent model. While ABSINTH is a well-established model for IDPs, the findings are entirely computational. There is no experimental validation, such as single-molecule FRET or NMR, to confirm the predicted conformational changes or interaction preferences for the designed GFP variants. The authors do not discuss the potential limitations or force-field dependence of their results.
        - **Why it matters** The conclusions are presented as general principles. If the observed behavior is an artifact of the specific simulation model, the conclusions would be significantly weakened. The lack of experimental validation makes it difficult to assess the biological relevance of the predicted effects.
        - **Resolution test** The authors should either provide experimental validation for at least a subset of the designed systems or significantly temper their claims and explicitly discuss the potential limitations of relying on a single simulation model. A discussion of the robustness of the results to force-field choice would also be helpful.
    - **R1-M2**
        - **Severity** Major
        - **Blocking** No
        - **Axis** Scientific importance / Evidence quality
        - **Claim pointer** The claim that the bioinformatic analysis of natural proteins supports the simulation findings, specifically that "naturally occurring proteins possess multiple charge patches that are physically accessible to local IDRs."
        - **Evidence pointer** Results section "Surface charge distribution characteristics of natural proteins", Figures 8-9, Supplementary Figures 21-23.
        - **Concern** The bioinformatic analysis is largely descriptive. It characterizes the surface charge patches of folded domains but does not directly test the hypothesis that these patches influence IDR conformation in natural proteins. The correlation between IDR properties (e.g., FCR) and FD patch properties is weak (only FCR vs. FCR and FCR vs. total patch size are mentioned). The analysis does not connect the presence of specific patches to the predicted conformational behavior of the attached tail. The link between this analysis and the simulation results is therefore not strongly established.
        - **Why it matters** The bioinformatic analysis is a key part of the paper's narrative, suggesting that the simulation findings are relevant to real proteins. Without a stronger, more direct link, this section feels disconnected from the main simulation results and does not fully support the paper's conclusions.
        - **Resolution test** The authors should strengthen this analysis. For example, they could use their simulation-derived framework to predict the conformational behavior of the natural IDRs based on the patch properties of their adjacent folded domains and then test these predictions against available experimental data or additional simulations. At minimum, they should more explicitly discuss how the descriptive statistics support the simulation-derived principles.
    - **R1-M3**
        - **Severity** Major
        - **Blocking** No
        - **Axis** Technical soundness / Readability
        - **Claim pointer** The claim that the case study on coronavirus nucleocapsid proteins demonstrates that "even modest changes in surface charge distribution can significantly influence IDR conformational behavior and IDR-FD interactions."
        - **Evidence pointer** Results section "Effect of surface charge distribution characteristics in real protein systems", Figure 10.
        - **Concern** The presentation of the nucleocapsid protein results is somewhat qualitative. The authors state that the RBD surface charge distribution is "quite different" and that this leads to different conformational behavior, but the quantitative analysis is not fully described in the main text. The specific features of the charge distribution that are responsible for the observed differences are not clearly identified. The comparison between the two systems is based on a limited set of analyses (internal scaling profiles and scaling maps).
        - **Why it matters** This case study is intended to be the most biologically relevant demonstration of the paper's core principle. A more detailed and quantitative analysis would make the argument more compelling and provide a clearer template for how to apply this framework to other protein systems.
        - **Resolution test** The authors should provide a more detailed quantitative comparison of the two RBD surfaces, identifying the specific patches that are different and how these differences correlate with the observed changes in IDR conformation. They could also perform additional analyses, such as calculating the contact probabilities between specific IDR residues and specific RBD surface residues.
- **Minor Comments**
    - **R1-m1**
        - **Severity** Minor
        - **Axis** Clarity
        - **Affected element** Abstract
        - **Evidence pointer** Abstract, "Our results reveal three key takeaways."
        - **Issue** The three key takeaways are listed in the abstract but are not explicitly numbered or clearly delineated, making them slightly difficult to parse.
        - **Required correction** Consider numbering the three key takeaways or using clearer signposting language to improve readability.
    - **R1-m2**
        - **Severity** Minor
        - **Axis** Technical soundness
        - **Affected element** Methods, "GFP mutant construction"
        - **Evidence pointer** Methods section "GFP mutant construction".
        - **Issue** The description of the GFP variant construction is somewhat brief. The criteria for choosing the specific mutations (e.g., "within x percent of the nearest surface residues") could be more clearly defined. It is unclear how "surface residues" are defined and how the distance from the FD:IDR junction is measured.
        - **Required correction** Provide a more detailed and precise description of the mutation strategy, including the definition of surface residues and the distance metric used.
    - **R1-m3**
        - **Severity** Minor
        - **Axis** Readability
        - **Affected element** Results, "Effect of surface charge distribution characteristics in real protein systems"
        - **Evidence pointer** Results section, Figure 10.
        - **Issue** The text describing the nucleocapsid protein results is somewhat dense and could be structured more clearly. The logic of the argument, from the structural comparison to the simulation results, could be made more explicit.
        - **Required correction** Consider restructuring this section to first describe the structural and electrostatic differences between the two RBDs, then present the simulation results, and finally discuss the implications.
    - **R1-m4**
        - **Severity** Minor
        - **Axis** Clarity
        - **Affected element** Discussion
        - **Evidence pointer** Discussion section.
        - **Issue** The discussion of the "polyelectrostatic effect" is interesting but could be expanded to more thoroughly connect the findings to the broader literature on IDP-mediated interactions and phase separation.
        - **Required correction** Consider adding a more detailed discussion of the implications of the findings for understanding IDP function in processes like liquid-liquid phase separation, where multivalent interactions are critical.
- **Technical failings that need to be addressed before the case is established**
    - The lack of experimental validation for the designed systems (R1-M1).
    - The weak and descriptive link between the bioinformatic analysis and the simulation findings (R1-M2).
    - The qualitative nature of the nucleocapsid protein case study (R1-M3).
- **Assessment against Nature-style criteria**
    - **Originality** The question posed is original and addresses a gap in the field. Most prior work has focused on how IDR sequence dictates behavior, while this work systematically investigates the role of the folded domain's surface. This is a fresh perspective.
    - **Scientific importance** The findings have the potential to be important, as they suggest that the local electrostatic environment of a folded domain is a key determinant of IDR behavior. This has implications for understanding protein function, regulation, and design. However, the importance is currently tempered by the lack of experimental validation.
    - **Interdisciplinary readership** The topic is of interest to a broad readership in biophysics, structural biology, computational biology, and cell biology. The conceptual framework of "patchy colloids" could appeal to a wider audience.
    - **Technical soundness** The simulation methodology is state-of-the-art, and the bioinformatic analysis is reasonable. However, the reliance on a single simulation model and the lack of experimental validation are significant technical weaknesses. The analysis of the natural proteins is not fully convincing.
    - **Readability for nonspecialists** The manuscript is generally well-written and the main concepts are explained clearly. The figures are helpful. However, some sections, particularly the nucleocapsid protein case study, are dense and may be challenging for a nonspecialist to follow.
- **Recommendation posture** Supportive if technical concerns are resolved. The core question is important and the simulation results are intriguing. However, the case is not fully established from the provided evidence. The lack of experimental validation and the weak link between the bioinformatic analysis and the simulations are major issues that need to be addressed. The authors should either provide experimental data or significantly temper their claims and provide a more robust computational analysis.

## Risk / unsupported claims
- The claim that the observed behavior in designed GFP variants represents a general principle is not fully supported without experimental validation or a discussion of force-field dependence.
- The claim that the bioinformatic analysis of natural proteins supports the simulation findings is not strongly supported, as the analysis is largely descriptive and does not directly test the hypothesis.
- The claim that "even modest changes in surface charge distribution can significantly influence IDR conformational behavior" in the nucleocapsid proteins is based on a qualitative comparison and would be strengthened by a more detailed quantitative analysis.
- The statement in the Discussion that "the balance of intra-IDR and IDR-FD charge interactions will - at a first approximation - determine if and how an IDR will be influenced by the presence of a folded domain" is a reasonable hypothesis but is presented as a conclusion without direct experimental evidence.