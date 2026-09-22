## Review setup
- **Input scope** Full manuscript text (preprint, bioRxiv, 2025-06-27)
- **Assessment boundary** Scientific claims, methodology, evidence quality, and internal consistency as presented in the provided text. No external validation or replication attempted.
- **Shared manuscript claim summary** The authors use proteome-wide structural predictions (AlphaFold/AlphaSync) to identify a substantial fraction (17.6%) of post-translational modification (PTM) sites that are buried within folded protein domains. They report evolutionary conservation of these sites across species, reduced human population variability, and enrichment of disease/cancer-associated variants at these sites. Using all-atom molecular dynamics (MD) simulations on 7 proteins (23 phosphorylation sites), they propose multiple mechanisms (fast sidechain fluctuations, local unfolding, proline isomerization, co-translational folding) that transiently expose buried sites for modification, suggesting a role for protein dynamics in regulating PTM accessibility and signalling timescales.
- **Visible evidence base** Main text, Methods, Extended Data Figure Legends, Supplementary Figure Legends, Data/Code availability statements. No actual figures, tables, or supplementary files were provided for inspection.
- **Missing materials affecting confidence** All figures (main and extended), all supplementary tables (including the key candidate site list and enrichment statistics), and the actual MD trajectory data. The absence of these materials severely limits the ability to verify the quantitative claims, the statistical analyses, and the interpretation of the simulation results.

## Reviewer
- **Overall assessment** This manuscript addresses a significant and timely question: how are buried PTM sites accessed for modification? The authors combine large-scale bioinformatics with targeted MD simulations, a powerful and potentially impactful approach. The central claim that a substantial fraction of PTM sites are buried and evolutionarily constrained is interesting and challenges simple views of PTM accessibility. However, the manuscript in its current form is largely a claim based on unseen data. The core quantitative results (the 17.6% figure, the conservation and variant analyses) are presented without the supporting figures or tables, making it impossible to assess their validity, robustness, or biological significance. The MD simulation component, while detailed in the methods, is presented as a series of observations on a small number of systems, and the link between these specific simulations and the broad, genome-scale conclusions remains largely qualitative and speculative. The manuscript is well-written and the conceptual framework is compelling, but the evidence base as provided is insufficient to establish the case.
- **Who would be interested in the results, and why** This work would be of broad interest to cell biologists, biochemists, and computational biologists studying cell signalling, post-translational modification, protein structure, and protein dynamics. The concept of "kinetic shielding" and the role of dynamics in gating PTM access has implications for understanding signalling specificity, temporal control, and disease mechanisms. The bioinformatics resource (the list of candidate buried sites) could be a valuable community tool. The potential link to co-translational modification is also of interest to those studying protein biogenesis and folding.
- **Major strengths**
    1.  The central question is important and the proposed concept of dynamics-gated access to buried sites is a valuable and potentially unifying framework.
    2.  The combination of large-scale structural bioinformatics with detailed MD simulations is a powerful and appropriate methodological approach.
    3.  The study is ambitious in scope, moving from a proteome-wide census to mechanistic hypotheses.
    4.  The manuscript is clearly written and the logical flow from observation to hypothesis is easy to follow.
- **Major Concerns**
    - **R1-M1**
        - **Severity** Major
        - **Blocking** Yes
        - **Axis** Evidence
        - **Claim pointer** The central quantitative claim that 17.6% of PTM sites are buried within proteins, and the subsequent analyses of their conservation, population variability, and disease association.
        - **Evidence pointer** Fig. 1a-e, Fig. 2a-b, Fig. 3a-e, Extended Data Fig. 1-2, Supplementary Fig. 1-6, Supplementary Tables 1-2 (none provided)
        - **Concern** The entire foundation of the paper rests on these bioinformatics results, yet none of the figures or tables that contain this data were provided for review. It is impossible to assess the distributions, effect sizes, statistical significance, or the validity of the control groups. For example, the claim that buried sites are more conserved than buried unmodified residues (Fig. 2b) is critical, but the density plots and statistical test results are not visible. Similarly, the enrichment of cancer mutations at buried sites (Fig. 3c-d) is a key finding, but the underlying data is absent.
        - **Why it matters** Without the primary evidence, the core premise of the paper cannot be evaluated. The conclusions are entirely dependent on the quality and interpretation of these unseen analyses. This is a blocking issue.
    - **R1-M2**
        - **Severity** Major
        - **Blocking** Yes
        - **Axis** Technical Soundness
        - **Claim pointer** The claim that MD simulations reveal a "broad range of exposure mechanisms spanning multiple orders of magnitude in terms of their dynamic timescale," including proline isomerisation-gated phosphorylation.
        - **Evidence pointer** Fig. 4a-j, Extended Data Fig. 3-10, Supplementary Fig. 7 (none provided)
        - **Concern** The manuscript describes results from 23 phosphorylation sites across 7 proteins, but the simulation data (trajectories, convergence, free energy profiles) is not shown. The claim of proline isomerisation gating is based on metadynamics simulations, but the free energy surfaces and the evidence for the predicted cis/trans populations are not presented. The selection of the 7 proteins and 23 sites from the 4,507 candidate sites is not justified in the provided text. The link between the observed dynamics in these specific systems and the general principle proposed is not quantitatively established.
        - **Why it matters** The MD simulations are intended to provide the mechanistic basis for the bioinformatics observations. Without the data, the mechanistic claims are unverifiable. The small number of systems studied raises questions about the generality of the conclusions, and the lack of a clear selection rationale introduces potential bias.
    - **R1-M3**
        - **Severity** Major
        - **Blocking** No
        - **Axis** Scientific Importance / Interpretation
        - **Claim pointer** The proposal that "protein conformational fluctuations may serve as structure-specific regulatory mechanisms by kinetically burying or exposing the unmodified, and in some cases even modified, sidechains, thereby expanding the functional versatility of proteins and enabling signal transduction across diverse timescales."
        - **Evidence point** Discussion section
        - **Concern** While this is an attractive hypothesis, the manuscript does not provide direct experimental evidence to support it. The simulations show that conformational states with exposed sites exist, but do not demonstrate that these states are kinetically relevant for phosphorylation *in vivo* or that they are specifically "regulatory." The argument that buried sites are functional because they are conserved and disease-associated is circumstantial. The possibility that some of these sites are modified only during co-translational folding or upon stress-induced unfolding, as the authors themselves note, is a distinct scenario that is not fully integrated into the "regulatory mechanism" framing.
        - **Why it matters** The paper's significance hinges on the claim that this is a regulatory mechanism, not just a biochemical curiosity. The current evidence, as presented, supports the latter more strongly than the former. The authors need to more carefully delineate what is established by their data and what is a speculative but testable framework.
- **Minor Comments**
    - **R1-m1**
        - **Severity** Minor
        - **Axis** Clarity
        - **Affected element** Figure 1e
        - **Evidence pointer** Fig. 1e (not provided)
        - **Issue** The text mentions that buried sites are "significantly, though marginally, closer to the nearest surface residue along the primary structure than buried control residues." The biological relevance of a "marginal" difference is unclear.
        - **Required correction** Please clarify the magnitude of this effect and discuss its potential biological significance, or temper the claim if it is not likely to be meaningful.
    - **R1-m2**
        - **Severity** Minor
        - **Axis** Methodology
        - **Affected element** Candidate site selection
        - **Evidence pointer** Methods, Supplementary Table 2 (not provided)
        - **Issue** The criteria for selecting the 7 proteins and 23 sites for MD simulation are listed, but the rationale for the final choice is not clear.
        - **Required correction** Please provide a more detailed justification for the specific systems chosen, perhaps including a table of the candidate sites considered and why the selected ones were prioritized.
    - **R1-m3**
        - **Severity** Minor
        - **Axis** Readability
        - **Affected element** Discussion of disease relevance
        - **Evidence pointer** Fig. 3c-e, Discussion
        - **Issue** The link between the enrichment of disease/cancer variants at buried sites and the proposed dynamic gating mechanism is not fully articulated.
        - **Required correction** Please expand on how the disruption of dynamics or the introduction of phosphomimetic mutations at these specific sites could contribute to disease pathogenesis.
- **Technical failings that need to be addressed before the case is established**
    - R1-M1: The primary bioinformatics evidence (all main and extended figures) is missing.
    - R1-M2: The primary MD simulation evidence (all simulation figures and analyses) is missing.
- **Assessment against Nature-style criteria**
    - **Originality** High. The concept of "kinetic shielding" and the systematic analysis of buried PTM sites is a novel and potentially important contribution.
    - **Scientific importance** Potentially high. If the claims are substantiated, this work could change the understanding of how PTMs are regulated and how signalling specificity is achieved. The resource of candidate sites is also valuable.
    - **Interdisciplinary readership** High. The topic bridges structural biology, cell signalling, and computational biology, and would be of interest to a broad audience.
    - **Technical soundness** Unassessable. The technical methods are described in detail, but the results of these methods are not available for review. The lack of evidence is a critical failing.
    - **Readability for nonspecialists** Good. The manuscript is well-structured and the concepts are explained clearly, making it accessible to a broad scientific audience.
- **Recommendation posture** Currently not established from the provided evidence. The central claims are interesting and the approach is sound, but the manuscript cannot be evaluated without the primary data. A resubmission with the full set of figures, tables, and simulation analyses is required for a proper assessment.

## Risk / unsupported claims
- The claim that 17.6% of PTM sites are buried is unsupported without Figure 1.
- The claim that buried sites are evolutionarily conserved is unsupported without Figure 2.
- The claim that buried sites are enriched in disease/cancer variants is unsupported without Figure 3.
- The claim that MD simulations reveal a range of exposure mechanisms is unsupported without Figures 4 and Extended Data Figures 3-10.
- The claim that proline isomerisation gates phosphorylation at specific sites is unsupported without the metadynamics data.
- The claim that these dynamics constitute a "regulatory mechanism" is a reasonable hypothesis but is not directly supported by the data presented in the text.