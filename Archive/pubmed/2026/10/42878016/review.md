## Review setup
- **Input scope** Full manuscript text
- **Assessment boundary** Scientific content, technical soundness, and framing of the review article
- **Shared manuscript claim summary** The review surveys recent advances in coarse-grained molecular simulations of nucleic acid condensation, arguing that base-mediated interactions are dominant drivers in homotypic condensation and that simulation resolution determines accessible physical phenomena. It emphasizes complementary insights across model resolutions and identifies gaps in current modeling capabilities.
- **Visible evidence base** Full text including abstract, introduction, sections on atomistic insights, CG models (SIS/TIS, iConRNA), emerging applications (G-quadruplex, nanostars), heterotypic systems, and concluding outlook. References cited but not individually verified.
- **Missing materials affecting confidence** Figures and tables referenced (Figure 1A–G, Figure 2A–D, Figure 3A–D, Table 1) were not provided. Reference list not fully accessible for verification of cited claims.

## Reviewer
- **Overall assessment** This is a well-structured and timely review that provides a useful synthesis of coarse-grained simulation approaches to nucleic acid condensation. The authors successfully organize a complex and rapidly evolving field by model resolution, and they articulate a coherent central thesis regarding the dominance of base-mediated interactions in homotypic systems. The review is generally balanced and appropriately critical of current limitations. However, several claims regarding model capabilities and validation are presented without sufficient supporting detail, and the absence of figures and tables limits full evaluation. The review would benefit from more explicit comparative analysis across models and clearer articulation of validation standards.
- **Who would be interested in the results, and why** Computational biophysicists and physical chemists working on biomolecular phase separation, developers of coarse-grained nucleic acid models, experimentalists studying RNA/DNA condensation who seek theoretical context, and researchers in synthetic biology interested in programmable condensates. The review provides a practical roadmap for model selection and identifies open challenges that would inform future method development.
- **Major strengths** The organization by model resolution is logical and effective. The central thesis regarding base-mediated interactions as dominant drivers is well supported by the SIS and iConRNA examples. The review appropriately distinguishes between what different model resolutions can and cannot capture. The discussion of atomistic insights provides a useful foundation for understanding CG model design constraints. The identification of future directions, particularly regarding protein–nucleic acid interactions and RNA–DNA distinctions, is thoughtful and forward-looking.
- **Major Concerns** Several concerns identified below relate to insufficient evidence for strong claims, lack of comparative benchmarking, and incomplete treatment of certain model categories.
- **Minor Comments** Several minor issues regarding clarity, terminology, and completeness are noted below.
- **Technical failings that need to be addressed before the case is established** R1-M1 (validation claims for iConRNA), R1-M2 (SIS model claims), R1-M3 (heterotypic model coverage)
- **Assessment against Nature-style criteria** **Originality** The review does not present new data but offers a synthesis with a clear central thesis. The framing around base-mediated interactions as dominant drivers is a useful organizing principle, though not entirely novel. **Scientific importance** The topic is of high importance given the growing recognition of nucleic acid condensation in biology and disease. The review addresses a genuine need for systematic comparison of CG approaches. **Interdisciplinary readership** The review bridges computational chemistry, biophysics, and cell biology, and should be accessible to researchers across these fields. **Technical soundness** Generally sound, but several claims require stronger evidentiary support as detailed in Major Concerns. **Readability for nonspecialists** The writing is clear and accessible, with appropriate context provided for key concepts. The organization aids comprehension. Overall, the review has the potential to be a valuable resource, but requires revisions to strengthen evidentiary support and comparative analysis.
- **Recommendation posture** Supportive if technical concerns are resolved. The review addresses an important topic and provides a useful framework, but several claims require additional support or qualification before the central thesis is fully established.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence sufficiency
- **Claim pointer** "iConRNA has been carefully balanced to reproduce local and long-range structures of flexible ssRNAs, including backbone orientation correlation function (OCF), radius of gyration (Rg), and end-to-end distance (Re) under different salt and Mg2+ concentrations (Figure 2B), as well as folding and melting temperature of a set of small RNAs."
- **Evidence pointer** Section "Intermediate resolution model for condensates of RNAs (iConRNA)", Figure 2B (not provided)
- **Concern** The claim that iConRNA reproduces multiple structural observables and thermodynamic properties is central to the review's argument that this model provides a validated framework. However, the specific quantitative agreement with experimental or atomistic reference data is not described. The reader cannot assess the quality of the validation from the text alone. The claim that this is "a major achievement that has not been demonstrated by other CG or atomistic models to date" requires explicit comparative evidence.
- **Why it matters** The review's central thesis depends on the credibility of iConRNA as a validated model. Without quantitative details of validation performance, the claim of superiority over other models is unsupported and potentially misleading.
- **Resolution test** Provide quantitative measures of agreement (e.g., percent error, correlation coefficients) for OCF, Rg, Re, and melting temperatures against reference data. Include a comparison table or explicit discussion of how other models perform on the same observables.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** No
- **Axis** Claim overreach
- **Claim pointer** "Multichain simulations using the calibrated SIS successfully recapitulated the length and concentration dependence of CAG repeat phase separation observed experimentally."
- **Evidence pointer** Section "Single-site and triple-site interaction models (SIS/TIS)"
- **Concern** The claim of successful recapitulation of experimental phase behavior is stated without specifying the quantitative metrics used for comparison. The text does not describe the experimental data against which the simulations were compared, nor the degree of agreement. Additionally, the statement that "base pairing, even when limited to canonical Watson–Crick contacts, is sufficient to drive phase separation" is a strong conclusion that may depend on the specific system and conditions studied.
- **Why it matters** The review uses this result to support the broader claim that base-mediated interactions are dominant drivers. If the agreement with experiment is only qualitative or limited to specific conditions, the conclusion may be overstated.
- **Resolution test** Specify the experimental datasets used for comparison, the quantitative measures of agreement (e.g., phase boundary coordinates, critical concentrations), and any limitations or conditions under which the model fails to reproduce experimental observations.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Completeness
- **Claim pointer** "Below we discuss representative models within increasing resolution, with particular attention to the nucleic acid component."
- **Evidence pointer** Section "CG models for protein–nucleic acid heterotypic phase transitions"
- **Concern** The section on heterotypic systems covers minimal models, one-bead models, and two-bead models, but the treatment of models with three or more beads per nucleotide in heterotypic contexts is limited to a brief mention of Martini. Given that the review emphasizes the importance of protein–nucleic acid interactions, a more detailed discussion of available multi-bead models and their applications to heterotypic phase separation would strengthen the review. The statement that "most have not been used for heterotypic protein–nucleic acid phase separation" is presented without a systematic survey to support it.
- **Why it matters** The review aims to provide a comprehensive survey of CG models for nucleic acid condensation. An incomplete treatment of multi-bead models in heterotypic systems leaves a significant gap in the coverage and weakens the review's utility as a reference.
- **Resolution test** Expand the discussion of multi-bead models in heterotypic contexts, including any available applications to protein–nucleic acid phase separation. If none exist, state this explicitly and discuss the reasons and potential pathways for such applications.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Terminology
- **Evidence pointer** Section "CG models for nucleic acid phase separation"
- **Issue** The term "homotypic nucleic acid condensation" is used throughout but not explicitly defined. The distinction between homotypic and heterotypic systems is introduced in the Introduction but could be clearer.
- **Required correction** Provide a brief definition of homotypic versus heterotypic condensation at first use, for example in the Introduction or at the start of the CG models section.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Model coverage
- **Evidence pointer** Table 1 (not provided)
- **Issue** The text refers to Table 1 as summarizing models, but the table is not available for review. The text mentions "many models" and "representative models" without a clear statement of inclusion criteria.
- **Required correction** State the criteria for model inclusion in the review and in Table 1. Clarify whether the table is intended to be exhaustive or representative.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Precision
- **Affected element** Claim about Martini
- **Evidence pointer** Section "Models with three or more beads per nucleotide"
- **Issue** The statement that Martini "has compatible protein and nucleic acid parameters, providing a ready-made framework" is somewhat vague. The specific version of Martini and the nature of the compatibility are not detailed.
- **Required correction** Specify the Martini version and briefly describe the nature of the protein–nucleic acid compatibility, including any known limitations.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Readability
- **Affected element** Figure references
- **Evidence pointer** Multiple sections
- **Issue** The text references Figures 1, 2, and 3 extensively, but these are not available. The descriptions in the text are generally clear, but some figure panels (e.g., Figure 1D–G) are referenced without sufficient context in the text.
- **Required correction** Ensure that each figure panel reference is accompanied by a brief description of what is shown, so the text remains comprehensible without the figures.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Consistency
- **Affected element** Citation style
- **Evidence pointer** Throughout
- **Issue** Citations are provided as bracketed numbers, which is standard, but the reference list is not available for verification. Some claims cite multiple references without distinguishing their individual contributions.
- **Required correction** Where multiple references are cited for a single claim, consider briefly indicating the nature of each reference's contribution if they address different aspects.

## Risk / unsupported claims
- The claim that iConRNA reproduces "the nontrivial dependence of CAG repeat phase separation on sequence length, ionic strength, temperature, Mg2+, and RNA concentrations" is presented as a major achievement but lacks quantitative validation details (R1-M1).
- The statement that SIS "successfully recapitulated the length and concentration dependence of CAG repeat phase separation observed experimentally" is not supported by specific comparative metrics (R1-M2).
- The assertion that "base pairing, even when limited to canonical Watson–Crick contacts, is sufficient to drive phase separation" is a strong conclusion that may not generalize beyond the specific systems studied.
- The claim that "most" multi-bead models "have not been used for heterotypic protein–nucleic acid phase separation" is presented without a systematic survey to support it (R1-M3).
- The statement that Martini provides a "ready-made framework" for multicomponent condensation studies is vague and not fully substantiated (R1-m3).
- The review's central thesis that "base-mediated interactions emerge as dominant drivers in homotypic nucleic acid condensation" is supported primarily by two model systems (SIS and iConRNA); broader generalization requires additional evidence from other models and systems.