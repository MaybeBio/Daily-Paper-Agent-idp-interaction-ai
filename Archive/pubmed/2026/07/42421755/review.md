## Review setup

- **Input scope** Full manuscript text, including abstract, methods, results, discussion, and supplementary file descriptions
- **Assessment boundary** Computational framework design, methodological rigor, structural biology claims, and translational relevance for PVR
- **Shared manuscript claim summary** The authors propose a disorder-aware computational pipeline integrating intrinsic disorder prediction, redox-sensitive disorder-to-order transition analysis, and generative AI-based binder design to prioritize structurally tractable EMT regulators in PVR, nominating SNAIL1 as the top candidate and generating a de novo binder targeting its C-terminal DOT region
- **Visible evidence base** Methods section, Results section with Tables 1-3 and Figures 1-6, Discussion section, Limitations section, supplementary file descriptions
- **Missing materials affecting confidence** Actual disorder prediction output data for all 25 proteins, complete STRING network data, binder sequence information, structural validation metrics beyond RMSD and pLDDT, experimental validation data, code availability, and full supplementary tables

## Reviewer

- **Overall assessment** This manuscript presents a conceptually interesting computational framework that addresses a genuine gap in PVR therapeutic development. The integration of disorder prediction with generative binder design is timely and aligns with emerging trends in targeting intrinsically disordered proteins. However, the study is entirely computational with no experimental validation, and several methodological details are insufficiently described to assess reproducibility. The claim that SNAIL1 is uniquely positioned as a druggable target is not fully supported by the comparative data presented. The manuscript would benefit from clearer articulation of the novelty relative to existing disorder-aware drug discovery pipelines and from a more rigorous treatment of the limitations inherent in computational binder design.

- **Who would be interested in the results, and why** Researchers in ophthalmic fibrosis and PVR pathogenesis would find the framework relevant as a hypothesis-generating tool. The computational protein design community, particularly those working on intrinsically disordered protein targeting, would be interested in the application of RFdiffusion to a disease-relevant transcription factor. Drug discovery scientists focused on fibrotic diseases beyond PVR may also find the pipeline adaptable to their targets. However, the lack of experimental validation limits the immediate utility for translational researchers.

- **Major strengths** The manuscript addresses an important clinical problem with a novel computational lens. The disorder-aware approach is conceptually sound and represents a departure from conventional structure-based drug design that typically excludes disordered proteins. The staged screening pipeline with explicit quantitative thresholds is clearly articulated and potentially reproducible. The authors appropriately acknowledge the preliminary nature of the computational binder design and the need for experimental validation. The discussion of PTM-enriched DOT regions as druggable interfaces is well reasoned and supported by literature.

- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence sufficiency
- **Claim pointer** The manuscript claims that SNAIL1 emerged as the highest-priority candidate because it satisfied the combined disorder, DOT, and network-based druggability criteria, and that other candidates including YAP1 and TWIST did not satisfy the same combination of criteria.
- **Evidence pointer** Results section, Druggability Assessment subsection, Tables 2-3, Table S1
- **Concern** The comparative screening data for all 25 proteins are not presented in sufficient detail. Table S1 is referenced but not provided in the manuscript text, and the specific quantitative values for YAP1, TWIST, and other candidates that were deprioritized are not shown. The claim that SNAIL1 uniquely satisfied all criteria cannot be independently assessed without the full screening results. Additionally, the thresholds for the STRING network assessment are described as "least stringent, limited interactome density" in Table 2, which is vague and does not provide a clear quantitative basis for the network-based prioritization.
- **Why it matters** The central claim of the manuscript rests on the comparative ranking of SNAIL1 against other EMT-associated proteins. Without transparent presentation of the full screening data, the reader cannot verify that the selection was not biased or that the criteria were applied consistently. The reproducibility of the pipeline depends on complete disclosure of all intermediate results.
- **Resolution test** Provide the complete screening results for all 25 proteins in the main text or a fully accessible supplementary table, including percent disorder values, Δ disorder values, STRING network metrics, and the specific criteria that led to exclusion of each candidate. Clarify the quantitative thresholds used for the STRING network assessment.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The manuscript claims that the top-ranked binder exhibited the lowest structural deviation within the generated ensemble (RMSD 18.5 Å) and high per-residue confidence (mean pLDDT 0.84), and that this represents a structure-aware de novo binder targeting the SNAIL1 C-terminal DOT region.
- **Evidence pointer** Results section, RFdiffusion-Based Binder Design subsection, Figures 5-6
- **Concern** An RMSD of 18.5 Å between the designed binder and the RFdiffusion backbone is exceptionally high and indicates substantial structural divergence. This value is not contextualized against typical RMSD thresholds for successful computational binder design, which are usually in the range of 1-3 Å for well-converged designs. The manuscript acknowledges this as a limitation but does not explain why such a high RMSD is acceptable or what it means for the structural validity of the design. Furthermore, the mean pLDDT of 0.84 is reported as "high" but is not benchmarked against known distributions for experimentally validated de novo binders. The interface metrics (iPAE 28.149, iPTM 0.134) are notably poor, with iPTM values below 0.5 generally considered indicative of unreliable interface predictions.
- **Why it matters** The structural validity of the designed binder is the core technical claim of the manuscript. If the binder does not actually adopt the intended conformation or engage the target interface as predicted, the entire computational pipeline loses its translational relevance. The reported metrics suggest that the design may not have converged to a physically plausible structure.
- **Resolution test** Provide a detailed analysis of the structural metrics, including a comparison of the RMSD distribution across the 64 designs, the relationship between RMSD and other quality metrics, and a justification for why 18.5 Å is acceptable. Consider reporting interface-restricted RMSD, which is more informative for binder-target complexes. Benchmark the pLDDT and iPTM values against known distributions from experimentally validated designs.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Claim substantiation
- **Claim pointer** The manuscript claims that the framework identifies structurally tractable targets and that the designed binder could modulate SNAIL1 activity by disrupting CBP/p300-mediated stabilization, potentially restoring epithelial polarity.
- **Evidence pointer** Discussion section, paragraphs 2-4
- **Concern** The manuscript makes mechanistic claims about the potential functional consequences of binder engagement without any experimental evidence. The assertion that disrupting the K187 acetylation site or the DOT region would modulate SNAIL1 activity is speculative and based on literature from cancer models, not PVR. The translational claims about perioperative or postoperative interventions are premature given the entirely computational nature of the study. The authors do acknowledge these limitations, but the framing in the Discussion overstates the immediate therapeutic potential.
- **Why it matters** The clinical relevance of the framework depends on whether the identified target and designed binder have actual biological activity. Without experimental validation, the claims about therapeutic potential are unsupported and could mislead readers about the maturity of the approach.
- **Resolution test** Reframe the Discussion to clearly distinguish between the computational hypothesis and the need for experimental validation. Avoid definitive statements about therapeutic potential. If possible, include preliminary experimental data or clearly state that such validation is the necessary next step.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Methodological completeness
- **Claim pointer** The manuscript describes a multistage pipeline integrating RIDAO, AIUPred, STRING, RFdiffusion, ProteinMPNN, and AlphaFold2, and claims this represents a novel disorder-aware computational framework.
- **Evidence pointer** Methods section, all subsections
- **Concern** Several methodological details are missing or underspecified. The RIDAO platform is described but its specific parameters and version are not provided. The AIUPred analysis uses a "redox-state prediction mode" but the redox conditions are not defined (what oxidizing and reducing conditions were simulated?). The STRING analysis uses version 11.5 in the Results but version 12.0 in the Methods, an inconsistency that needs resolution. The RFdiffusion parameters (beyond iterations and copy number) are not specified, including the number of diffusion steps, the noise schedule, and the target residue selection criteria. The AlphaFold2 validation protocol is described but the number of recycles and the specific model version are not stated.
- **Why it matters** Reproducibility is a fundamental requirement for computational studies. Without complete methodological details, other researchers cannot replicate the pipeline or assess its robustness. The version inconsistency for STRING is particularly concerning as it may affect the network results.
- **Resolution test** Provide complete methodological details for all tools used, including version numbers, specific parameters, and analysis settings. Resolve the STRING version inconsistency. Consider providing the full computational workflow as a code repository or detailed protocol.

- **Concern ID** R1-M5
- **Severity** Major
- **Blocking** No
- **Axis** Comparative novelty
- **Claim pointer** The manuscript claims to introduce a novel disorder-aware computational framework and to be the first systematic assessment of structural plasticity as a determinant of therapeutic tractability in PVR.
- **Evidence pointer** Abstract, Introduction, Discussion
- **Concern** The novelty claim is not fully contextualized against existing computational approaches for target identification in fibrosis or against disorder-aware drug discovery pipelines in other disease areas. The use of RFdiffusion for binder design is not new, and the integration of disorder prediction with generative design has been explored in other contexts. The specific application to PVR is novel, but the framework itself may not represent a fundamental methodological advance. The authors should more carefully position their work relative to existing literature.
- **Why it matters** The significance of the contribution depends on its novelty relative to prior work. If the framework is largely an application of existing tools to a new disease context, the claims of novelty should be tempered accordingly.
- **Resolution test** Expand the Introduction and Discussion to more thoroughly review existing disorder-aware computational frameworks and generative binder design approaches, clearly articulating what is genuinely new in this work versus what is an application of established methods.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Abstract, Results
- **Evidence pointer** Abstract, Results section, Druggability Assessment subsection
- **Issue** The abstract states that SNAIL1 demonstrated "a pronounced redox-sensitive DOT region" but does not provide the quantitative Δ disorder value. The Results section reports Δ disorder = 0.25, which is above the stated threshold of 0.20 but not dramatically so. The term "pronounced" may overstate the magnitude.
- **Required correction** Consider using more measured language in the abstract, such as "a redox-sensitive DOT region exceeding the predefined threshold," and include the quantitative value where space permits.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Consistency
- **Affected element** Methods, Results
- **Evidence pointer** Methods section, Druggability Assessment subsection; Results section, Druggability Assessment subsection
- **Issue** The Methods section states that STRING v12.0 was used, while the Results section and Table 3 reference STRING v11.5. This inconsistency is confusing and may indicate an error in one of the sections.
- **Required correction** Verify which version of STRING was actually used and correct the inconsistency throughout the manuscript.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Presentation
- **Affected element** Figure 5
- **Evidence pointer** Figure 5 and its legend
- **Issue** Figure 5A shows an overlay of 64 RFdiffusion-generated binder backbones, but the figure is described as showing "conformational diversity" without providing a quantitative measure of this diversity. The visual overlay may be difficult to interpret without additional metrics.
- **Required correction** Consider adding quantitative measures of structural diversity, such as pairwise RMSD distributions or clustering analysis, to support the visual presentation.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Discussion, Limitations
- **Evidence pointer** Discussion section, Limitations subsection
- **Issue** The limitations section is thorough but does not address the potential for off-target effects of the designed binder, the specificity of the SNAIL1 DOT region as a therapeutic target, or the possibility that other EMT regulators not included in the initial 25-protein panel could be equally or more tractable.
- **Required correction** Consider adding these points to the limitations discussion to provide a more complete assessment of the framework's scope and potential weaknesses.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Referencing
- **Affected element** Introduction, Discussion
- **Evidence pointer** Introduction, Discussion
- **Issue** The manuscript references recent work on de novo binder design targeting intrinsically disordered regions but does not provide a comprehensive review of this emerging field. The citation to Wu et al. is mentioned but not fully contextualized.
- **Required correction** Expand the discussion of prior work on targeting intrinsically disordered proteins with designed binders to better position the current study within the broader literature.

- **Concern ID** R1-m6
- **Severity** Minor
- **Axis** Accessibility
- **Affected element** Methods, Results
- **Evidence pointer** Methods section, RFdiffusion-Based Binder Design subsection; Results section, RFdiffusion-Based Binder Design subsection
- **Issue** The manuscript uses specialized terminology (e.g., "protein message passing neural network," "interface predicted alignment error") without defining these terms for readers who may not be computational biologists. Given the target audience of ophthalmology researchers, some of this terminology may be inaccessible.
- **Required correction** Consider adding brief definitions or explanations for key computational terms, or include a glossary for non-specialist readers.

- **Technical failings that need to be addressed before the case is established** R1-M1 (incomplete comparative screening data), R1-M2 (inadequate structural validation metrics), R1-M3 (unsupported mechanistic and translational claims), R1-M4 (incomplete methodological details)

- **Assessment against Nature-style criteria** 
  - Originality: Moderate. The application of disorder-aware computational screening to PVR is novel, but the individual components (disorder prediction, RFdiffusion, AlphaFold2) are established methods. The integration is creative but does not represent a fundamental methodological breakthrough.
  - Scientific importance: Moderate. PVR is an important clinical problem with no effective pharmacologic therapy, and the framework could inform future target identification. However, the entirely computational nature limits immediate impact.
  - Interdisciplinary readership: Limited. The manuscript bridges computational biology and ophthalmology, but the technical depth may limit accessibility for clinical readers, and the clinical relevance may be insufficiently compelling for computational biology readers.
  - Technical soundness: Weak to moderate. The pipeline is logically structured, but the structural validation metrics are concerning (RMSD 18.5 Å), and the comparative screening data are not fully presented.
  - Readability for nonspecialists: Moderate. The manuscript is generally well-written, but the methods section assumes familiarity with computational biology tools and terminology.

- **Recommendation posture** Currently not established from the provided evidence. The manuscript presents an interesting computational framework with potential utility, but the central claims regarding SNAIL1 as a uniquely tractable target and the validity of the designed binder are not sufficiently supported by the data presented. The high RMSD and poor interface metrics raise questions about the structural validity of the binder design, and the incomplete presentation of comparative screening data prevents independent verification of the target prioritization. The manuscript would require substantial revision, including complete data disclosure, more rigorous structural validation, and tempering of translational claims, before the case for the framework's utility is established.