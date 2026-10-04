## Review setup
- **Input scope** Full manuscript text (Abstract, Introduction, all thematic sections, Practical guide, Outlook, Closing perspective, author statements)
- **Assessment boundary** Scientific content, conceptual framing, internal consistency, and support for claims as presented in the provided text. No assessment of figures, tables, or supplementary materials, which were not provided.
- **Shared manuscript claim summary** The manuscript argues that solution NMR spectroscopy is uniquely positioned within integrated structural biology to provide quantitative, site-specific information on conformational heterogeneity, dynamics, exchange kinetics, weak interactions, allostery, disorder, and phase behavior. It advocates a question-centered rather than method-centered organization of NMR approaches and emphasizes integration with complementary techniques such as cryo-EM, crystallography, simulations, and AI-based prediction.
- **Visible evidence base** The manuscript is a narrative review. Evidence is presented through cited literature (e.g., Eisenmesser et al., 2005; Tzeng and Kalodimos, 2012; Fawzi et al., 2011; Murthy et al., 2019) and illustrative examples. No original experimental data, figures, or tables were available for assessment.
- **Missing materials affecting confidence** Figures 1-4 and Tables 1-2 are referenced but not provided. The reference list is not provided. The Generative AI statement indicates figures were created with ChatGPT, but the figures themselves could not be evaluated for accuracy or appropriateness.

## Reviewer
- **Overall assessment** This is a well-written, conceptually coherent review that makes a persuasive case for repositioning solution NMR as a quantitative, integrative tool rather than a standalone structure-determination method. The question-centered organization is a genuine strength and will be useful to both specialists and non-specialists. The manuscript is clear, logically structured, and generally avoids overclaiming. However, the absence of the figures and tables limits full evaluation, and some claims about the uniqueness of NMR capabilities would benefit from more careful qualification. The review is likely to be of interest to the structural biology community, but its impact will depend on how well the visual materials support the textual arguments.
- **Who would be interested in the results, and why** Structural biologists, biophysicists, and biochemists who use or consider using NMR in integrative studies. The manuscript will also be relevant to researchers working on intrinsically disordered proteins, biomolecular condensates, allostery, and weak protein interactions, as it provides a framework for selecting NMR approaches based on mechanistic questions. Computational biologists who use NMR data for ensemble refinement or simulation validation will also find the integration sections useful.
- **Major strengths**
  1. The question-centered organization is a clear improvement over traditional method-centered NMR reviews and will help non-specialists navigate the field.
  2. The manuscript consistently emphasizes integration with other methods, avoiding the common pitfall of presenting NMR in isolation.
  3. The treatment of condensates and phase separation is current and well integrated with the broader argument.
  4. The practical guide (Section 10) and the explicit mapping of questions to methods (Table 2, not seen) are valuable pedagogical contributions.
  5. The writing is accessible and avoids unnecessary jargon, making it suitable for a broad readership.
- **Major Concerns**
  - **Concern ID** R1-M1
  - **Severity** Major
  - **Blocking** No
  - **Axis** Support for claims
  - **Claim pointer** The manuscript repeatedly asserts that solution NMR provides information that is "difficult to infer" or "invisible" to other methods, and that it occupies a "distinctive position" in integrated structural biology.
  - **Evidence pointer** Abstract; Introduction; Section 3; Section 4
  - **Concern** While the claim is plausible and likely true, the manuscript does not provide a systematic comparison of NMR against other solution techniques (e.g., smFRET, HDX-MS, SAXS) in terms of what each can uniquely deliver. The assertion of uniqueness is repeated but not rigorously demonstrated. For a review aimed at non-specialists, a more balanced discussion of where NMR is not the best tool would strengthen credibility.
  - **Why it matters** The central thesis of the manuscript depends on the claim that NMR has a distinctive, indispensable role. If this claim is not critically examined, the review risks reading as advocacy rather than balanced assessment, which may reduce its persuasiveness for skeptical readers.
  - **Resolution test** Add a section or subsection that explicitly compares NMR with other solution-state methods for each class of question (structure, dynamics, interactions, allostery, disorder, condensates), noting where NMR is superior, where it is complementary, and where other methods are preferable.
  - **Concern ID** R1-M2
  - **Severity** Major
  - **Blocking** No
  - **Axis** Reproducibility and transparency
  - **Claim pointer** The manuscript states that figures were generated using ChatGPT and that the authors reviewed and edited the output.
  - **Evidence pointer** Generative AI statement
  - **Concern** The use of AI for figure generation is disclosed, but the nature of the figures is not described in the text. Without seeing the figures, it is impossible to assess whether they are accurate, informative, and appropriately attributed. If the figures contain conceptual diagrams, AI-generated artwork may introduce inaccuracies or stylistic inconsistencies that could mislead readers.
  - **Why it matters** Figures are central to a review's communicative function. If they are inaccurate or misleading, the manuscript's scientific message is compromised. The disclosure is transparent, but the lack of detail about what was generated and how it was verified is a concern.
  - **Resolution test** Provide a description of each figure in the text or figure legends, including what content was AI-generated and what was author-created. If possible, include a statement on how the figures were validated for scientific accuracy.
  - **Concern ID** R1-M3
  - **Severity** Major
  - **Blocking** No
  - **Axis** Completeness of evidence
  - **Claim pointer** The manuscript references specific studies (e.g., Eisenmesser et al., 2005; Tzeng and Kalodimos, 2012; Fawzi et al., 2011; Murthy et al., 2019) as illustrative examples of NMR applications.
  - **Evidence pointer** Sections 4, 5, 6, 8
  - **Concern** The examples are cited but not described in sufficient detail for a non-specialist to understand what was measured, what was found, and why it matters. For instance, the cyclophilin A example is mentioned in one sentence, but the reader is not told what the relaxation dispersion data revealed about the catalytic cycle. Similarly, the FUS condensate example is referenced but not explained.
  - **Why it matters** A review that aims to be accessible to non-specialists must provide enough context for each example to be meaningful. Without this, the examples function as name-dropping rather than illustration, and the reader cannot evaluate the strength of the evidence.
  - **Resolution test** Expand the discussion of at least 3-5 key examples, providing a brief description of the system, the NMR observables measured, the result, and the mechanistic insight gained.
- **Minor Comments**
  - **Concern ID** R1-m1
  - **Severity** Minor
  - **Axis** Clarity
  - **Affected element** Section 3, paragraph 1
  - **Evidence pointer** Location not provided
  - **Issue** The sentence "The central principle is that the biological uncertainty should determine the NMR observables, not the other way around" is slightly tautological and could be sharpened.
  - **Required correction** Rephrase to something like "The choice of NMR observables should be driven by the specific biological question, rather than by the availability of a particular experiment."
  - **Concern ID** R1-m2
  - **Severity** Minor
  - **Axis** Terminology
  - **Affected element** Section 8, paragraph 2
  - **Evidence pointer** Location not provided
  - **Issue** The term "dark states" is used without definition. Non-specialist readers may not know that this refers to NMR-invisible or broadened states.
  - **Required correction** Add a brief parenthetical definition on first use, e.g., "dark states (states that are too broadened or too sparsely populated to be directly observed)".
  - **Concern ID** R1-m3
  - **Severity** Minor
  - **Axis** Consistency
  - **Affected element** Section 10, Table 2 (referenced)
  - **Evidence pointer** Table 2 (not provided)
  - **Issue** The text states that Table 2 matches questions to methods, but the table itself is not available for review. It is unclear whether the table is consistent with the text.
  - **Required correction** Ensure the table is provided in the final submission and that it aligns with the text descriptions.
  - **Concern ID** R1-m4
  - **Severity** Minor
  - **Axis** Completeness
  - **Affected element** Section 11, paragraph 2
  - **Evidence pointer** Location not provided
  - **Issue** The discussion of in-cell and in situ NMR is brief and does not mention specific challenges such as sensitivity, spectral overlap, or sample preparation.
  - **Required correction** Add one or two sentences acknowledging these challenges and referencing recent reviews or methodological advances.
- **Technical failings that need to be addressed before the case is established** None identified from the supplied material. The manuscript is a review, and the technical content is presented at an appropriate level. The main technical limitation is the absence of figures and tables, which prevents full evaluation of the visual aids.
- **Assessment against Nature-style criteria**
  - **Originality** The question-centered framing is not entirely new, but the manuscript applies it more consistently and comprehensively than most existing NMR reviews. The emphasis on integration with AI-based prediction and condensate biology is timely. However, the core ideas are not novel enough to constitute a major conceptual advance.
  - **Scientific importance** The manuscript addresses a real need: helping the structural biology community understand where NMR fits in the modern integrative landscape. The importance is moderate to high, depending on how well the figures and examples support the argument.
  - **Interdisciplinary readership** The manuscript is written for a broad audience and avoids excessive jargon. It should be accessible to structural biologists, biochemists, and computational scientists. The question-centered organization enhances interdisciplinary appeal.
  - **Technical soundness** The technical content is accurate and well referenced, based on the text. No factual errors were identified. The main limitation is the lack of detail in the examples, which prevents full assessment of the evidence base.
  - **Readability for nonspecialists** The writing is clear and well structured. The use of questions as section headings is effective. However, some terms (e.g., "dark states," "methyl-TROSY") are used without definition, which may hinder non-specialist readers.
- **Recommendation posture** Supportive if technical concerns are resolved. The manuscript is well conceived and clearly written, but the absence of figures and tables, the lack of detail in key examples, and the uncritical assertion of NMR uniqueness should be addressed before publication.

## Risk / unsupported claims
- The claim that NMR provides information "invisible" to other methods is asserted but not systematically demonstrated.
- The statement that "the future of solution NMR will not be defined by a return to the era" of competing structure-determination methods is an opinion, not a supported claim.
- The manuscript implies that AI-generated figures were reviewed and edited, but the nature and accuracy of these figures cannot be assessed from the provided text.
- The claim that "signal loss is potentially informative" in condensate studies is presented without discussion of the alternative explanations (e.g., aggregation, viscosity) that the authors themselves acknowledge later in the same paragraph. This is internally consistent but could be more clearly framed.