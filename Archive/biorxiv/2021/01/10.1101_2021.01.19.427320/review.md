## Review setup
- **Input scope** Full manuscript text (abstract, introduction, methods, results, discussion, conclusions) as provided
- **Assessment boundary** Scientific content, methodological soundness, validity of claims, and alignment with stated evidence; no assessment of formatting or editorial style beyond readability
- **Shared manuscript claim summary** The authors use coevolutionary analysis, coarse-grained molecular simulations, and perturbation-based network modeling to propose that binding of four antibodies (H014, S309, S2M11, S2E12) to SARS-CoV-2 spike protein modulates allosteric interactions and signaling, stabilizes specific conformational states, and may explain neutralization mechanisms and resistance to mutations
- **Visible evidence base** Sequence conservation scores, coevolutionary coupling scores (MfDCA, plmDCA, gaussianDCA), CABS-flex coarse-grained simulations, protein contact network analysis, betweenness centrality, perturbation response scanning; figures referenced but not provided
- **Missing materials affecting confidence** Figures 1-13, Tables S1-S10, and all Supporting Information are referenced but not included in the provided material; no quantitative data (e.g., RMSF values, binding energies, centrality scores) are presented in the text; no statistical analysis or error estimates are described

## Reviewer
- **Overall assessment** The manuscript presents a computational study aimed at linking antibody binding to allosteric regulation in the SARS-CoV-2 spike protein. The conceptual framework is interesting and the combination of coevolutionary analysis with network-based perturbation methods is potentially valuable. However, the manuscript as provided is largely descriptive and qualitative. The central claims, particularly regarding the existence of specific allosteric pathways and the proposed switch between population-shift and induced-fit mechanisms, are not supported by quantitative evidence presented in the text. The absence of all figures and supporting tables makes it impossible to evaluate the robustness of the results. The manuscript reads more as a hypothesis-generating report than a definitive mechanistic study.
- **Who would be interested in the results, and why** Structural biologists and computational biophysicists studying viral entry mechanisms, allosteric regulation in large protein complexes, and antibody neutralization. Researchers focused on SARS-CoV-2 spike dynamics and therapeutic antibody design may find the proposed framework useful for generating testable hypotheses, though the lack of experimental validation limits broader appeal.
- **Major strengths** The study addresses a timely and important question regarding the mechanistic basis of antibody neutralization beyond direct receptor blockade. The integration of coevolutionary analysis with perturbation-based network modeling is a creative approach that could reveal functionally relevant residues. The authors connect their computational findings to existing experimental structures and functional data, which helps contextualize the results.
- **Major Concerns** The central claims are not quantitatively supported in the provided text. The manuscript relies heavily on qualitative descriptions of "increased effector potential" and "strengthened couplings" without presenting numerical data or statistical significance. The absence of all figures and tables is a critical limitation. The methods section is incomplete, lacking details on simulation parameters, convergence criteria, and validation of the coarse-grained approach. The link between computational predictions and experimental neutralization mechanisms is speculative and not rigorously established.
- **Minor Comments** The manuscript contains several typographical errors and inconsistent terminology (e.g., "communcating," "meditig," "attentuating"). The introduction is overly long and could be streamlined. The conclusions overstate the novelty and certainty of the findings given the qualitative nature of the analysis.
- **Technical failings that need to be addressed before the case is established** Absence of quantitative results (numerical values for scores, RMSF, energies, centrality); lack of statistical analysis or error estimates; incomplete methods description; no validation of the coarse-grained model against experimental data or all-atom simulations; no demonstration that the proposed allosteric pathways are robust to methodological choices.
- **Assessment against Nature-style criteria** Originality: Moderate. The combination of methods is somewhat novel, but the conceptual framework of allosteric regulation in spike proteins has been explored previously. Scientific importance: Moderate. The question is important, but the study does not provide definitive mechanistic insights. Interdisciplinary readership: Limited. The manuscript is highly specialized and would primarily appeal to computational biophysicists. Technical soundness: Weak. The methods are not described in sufficient detail to assess rigor, and the absence of quantitative results undermines confidence. Readability for nonspecialists: Poor. The manuscript assumes deep familiarity with network theory and coarse-grained simulation methods without adequate explanation.
- **Recommendation posture** Currently not established from the provided evidence. The manuscript requires substantial revision, including presentation of quantitative results, complete methods, and all figures, before the claims can be evaluated.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence sufficiency
- **Claim pointer** The authors claim that antibody binding "can allow for efficient modulation of allosteric interactions and signal propagation between remote functional regions" and that this "protects the spike apparatus from membrane fusion."
- **Evidence pointer** Results sections on coevolutionary analysis, network modeling, and PRS; Figures 5-13 and Tables S1-S10 referenced but not provided
- **Concern** The central mechanistic claims are presented without any quantitative data in the text. Terms such as "increased effector potential," "strengthened couplings," and "restored allosteric potential" are used repeatedly, but no numerical values, confidence intervals, or statistical tests are reported. The reader cannot assess the magnitude or significance of the reported effects.
- **Why it matters** Without quantitative evidence, the claims are unfalsifiable and cannot be distinguished from subjective interpretation. The proposed allosteric mechanisms, which form the core of the manuscript, require robust numerical support to be credible.
- **Resolution test** Provide numerical values for all key metrics (e.g., effector scores, centrality values, RMSF changes) with appropriate statistical analysis, and show that the reported differences between bound and unbound states are significant and reproducible across simulation replicates.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Methodological completeness
- **Claim pointer** The authors state they used "coarse-grained (CG) CABS model" and "CABS-flex approach" for simulations, and "perturbation response scanning" for allosteric analysis.
- **Evidence pointer** Materials and Methods section, subsections on Coarse-Grained Molecular Simulations and Perturbation Response Scanning
- **Concern** The methods section is critically incomplete. No simulation parameters are given (e.g., temperature, number of Monte Carlo steps, replica exchange settings, force field parameters). The PRS methodology is described only by reference to previous work, with no details on how forces were applied, how responses were quantified, or how the 3N x 3N Hessian was constructed from coarse-grained trajectories. No convergence criteria or validation of the simulations are described.
- **Why it matters** Reproducibility is a fundamental requirement for computational studies. Without complete methodological details, the results cannot be replicated or independently verified, and the validity of the conclusions cannot be assessed.
- **Resolution test** Provide a complete description of all simulation and analysis parameters, including convergence checks, validation against experimental data or all-atom simulations, and a clear explanation of the PRS implementation specific to this study.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Claim-evidence alignment
- **Claim pointer** The authors conclude that "antibody binding can induce a switch from a moderately cooperative population-shift mechanism... to antibody-induced highly cooperative mechanism that can better withstand mutations."
- **Evidence pointer** Results section on Perturbation Response Scanning; Figures 12-13 referenced but not provided
- **Concern** The proposed switch between allosteric mechanisms is a strong claim that requires direct comparative analysis of the unbound and bound states. The text describes differences in effector profiles but does not provide a quantitative framework for distinguishing between "population-shift" and "induced-fit" mechanisms. No metrics are defined to operationalize these concepts, and no statistical comparison is made.
- **Why it matters** This claim is presented as a key finding, but it is not supported by the evidence described. The distinction between allosteric mechanisms has specific theoretical implications, and asserting a switch requires rigorous demonstration, not qualitative inference.
- **Resolution test** Define quantitative metrics that distinguish between population-shift and induced-fit mechanisms (e.g., changes in conformational ensembles, correlation patterns, or energy landscapes), and show statistically significant differences between unbound and bound states using these metrics.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** External validity
- **Claim pointer** The authors suggest that their findings "provide a plausible strategy for therapeutic intervention by targeting specific hotspots of allosteric interactions."
- **Evidence pointer** Conclusions section
- **Concern** The therapeutic implications are speculative and not supported by any experimental validation. The study is purely computational, and no evidence is provided that the identified hotspots are druggable, that modulation of these sites would have the predicted effects in vivo, or that the proposed strategy would be superior to existing approaches.
- **Why it matters** Overstating therapeutic relevance without experimental support can mislead readers and detract from the legitimate scientific contributions of the study.
- **Resolution test** Either remove or substantially temper the therapeutic claims, or provide experimental evidence (e.g., mutagenesis, binding assays, neutralization assays) that supports the proposed strategy.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Abstract and Conclusions
- **Evidence pointer** Abstract, Conclusions
- **Issue** The abstract and conclusions use vague and grandiose language (e.g., "novel insight," "plausible strategy") that overstates the certainty of the findings.
- **Required correction** Use more measured language that accurately reflects the hypothesis-generating nature of the study.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Terminology consistency
- **Affected element** Throughout the manuscript
- **Evidence pointer** Multiple sections
- **Issue** Inconsistent and sometimes incorrect terminology is used (e.g., "communcating," "meditig," "attentuating," "timer" instead of "trimer").
- **Required correction** Thorough proofreading and consistent use of technical terms.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Contextualization
- **Affected element** Introduction
- **Evidence pointer** Introduction
- **Issue** The introduction is excessively long and includes extensive background that is not directly relevant to the study's specific contributions.
- **Required correction** Condense the introduction to focus on the specific gap the study addresses and the rationale for the chosen methods.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Reproducibility
- **Affected element** Methods
- **Evidence pointer** Materials and Methods, Sequence Conservation and Coevolutionary Analyses
- **Issue** The description of the coevolutionary analysis lacks details on sequence filtering, alignment trimming, and the specific thresholds used for defining "significant" coevolutionary couplings.
- **Required correction** Provide complete parameters for the coevolutionary analysis, including the number of sequences used, alignment quality metrics, and criteria for identifying significant couplings.

## Risk / unsupported claims
- The claim that antibody binding "restores and enhances couplings between spatially separated functional regions" is unsupported by quantitative data.
- The proposed switch from population-shift to induced-fit mechanisms is not operationalized or tested.
- The therapeutic implications are speculative and not supported by experimental evidence.
- The assertion that the studied antibodies "protect the spike apparatus from membrane fusion" through allosteric mechanisms is not directly demonstrated.
- All claims based on figures and tables that were not provided in the manuscript are unverifiable from the supplied material.