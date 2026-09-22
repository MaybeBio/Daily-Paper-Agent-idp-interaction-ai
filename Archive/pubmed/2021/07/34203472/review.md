## Review setup
- **Input scope** Full manuscript text
- **Assessment boundary** Scientific content, technical soundness, and clarity of the review article as provided
- **Shared manuscript claim summary** The authors review computational approaches, specifically all-atom molecular dynamics, coarse-grained, and mesoscopic models, for studying bacterial toxin entry into host cells. They highlight the GL-Lect mechanism for Shiga and cholera toxins, discuss the applicability of these methods to nanoparticle design and membrane protein phase separation, and outline future directions.
- **Visible evidence base** Abstract, Introduction, sections on computational methods (all-atom, coarse-grained, mesoscopic), Summary and Outlook, and references cited within the text
- **Missing materials affecting confidence** Figures and their captions are referenced but not provided; full reference list is not included; no supplementary information or detailed methodological protocols are available

## Reviewer
- **Overall assessment** This is a well-structured and readable review that provides a useful overview of computational methods applied to bacterial toxin entry, with a particular focus on the GL-Lect mechanism. The authors are clearly knowledgeable in the field, and the manuscript is likely to be of interest to researchers in biophysics, computational biology, and toxin research. However, the review is largely descriptive and does not critically evaluate the strengths and limitations of the methods discussed in sufficient depth. Several claims are made without adequate supporting evidence or references, and the lack of figures limits the ability to fully assess the presented results. The manuscript would benefit from a more critical and comparative analysis of the methods, as well as clearer articulation of open questions and challenges.
- **Who would be interested in the results, and why** Researchers in computational biophysics, molecular dynamics simulation, membrane biology, and bacterial pathogenesis would find this review useful. It provides a concise entry point for those interested in applying simulation techniques to toxin-membrane interactions and could inform the design of drug delivery vehicles. The discussion of the GL-Lect mechanism may also appeal to cell biologists studying endocytosis.
- **Major strengths** The manuscript is clearly written and logically organized. The authors successfully cover a range of computational methods and connect them to a specific biological problem. The emphasis on multiscale approaches and the link to experimental observations is a positive feature. The discussion of the GL-Lect mechanism is timely and relevant.
- **Major Concerns** The review lacks critical depth in comparing the methods discussed. Claims about the capabilities and limitations of each method are often stated without sufficient justification or comparison to alternative approaches. The section on mesoscopic models, in particular, relies heavily on the authors' own work without adequate context from other studies. The manuscript also does not clearly identify unresolved questions or challenges in the field, which would strengthen its value as a review.
- **Technical failings that need to be addressed before the case is established** The manuscript does not provide a clear framework for how the different methods should be integrated in practice. The claim that multiscale approaches are "among the first successful applications" is not substantiated with specific examples or comparisons. The lack of figures makes it difficult to evaluate the presented simulation results.
- **Assessment against Nature-style criteria** Originality: The review covers a topic that has been reviewed before, but the focus on the GL-Lect mechanism and the integration of multiple simulation scales provides some fresh perspective. Scientific importance: The topic is of significant importance to understanding bacterial pathogenesis and for biomedical applications. Interdisciplinary readership: The manuscript is likely to appeal to a broad audience, but the technical detail may be challenging for nonspecialists. Technical soundness: The methods described are generally sound, but the review lacks critical evaluation and comparative analysis. Readability for nonspecialists: The manuscript is generally readable, but some sections assume prior knowledge of simulation techniques.
- **Recommendation posture** Supportive if technical concerns are resolved. The manuscript has potential but requires significant revision to improve critical depth, provide clearer comparisons, and address the lack of supporting evidence for several claims.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors claim that multiscale simulation approaches are "among the first successful application of multiscale simulation methods" for studying bacterial toxin entry.
- **Evidence pointer** Section 2, location not provided
- **Concern** This claim is made without specific examples or references to support it. It is unclear which studies are being referred to and how they demonstrate success.
- **Why it matters** The claim is central to the review's premise that multiscale methods are uniquely suited for this problem. Without supporting evidence, the reader cannot assess the validity of this assertion.
- **Resolution test** Provide specific examples of multiscale studies that have successfully addressed toxin entry, with references and a brief description of their findings.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors state that the GL-Lect mechanism is "well established" for Shiga and cholera toxins and that simulations have "significantly advanced" understanding of this process.
- **Evidence pointer** Sections 1 and 3, location not provided
- **Concern** The review does not critically evaluate the evidence for the GL-Lect mechanism or the specific contributions of simulations. It is not clear what aspects of the mechanism are well established and what remains uncertain.
- **Why it matters** A review should provide a balanced assessment of the current state of knowledge. Without critical evaluation, the reader cannot distinguish between established findings and speculative interpretations.
- **Resolution test** Provide a more detailed discussion of the experimental and computational evidence for the GL-Lect mechanism, including any controversies or unresolved questions.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Readability for nonspecialists
- **Claim pointer** The manuscript claims to be a review accessible to a broad audience, but the technical descriptions of simulation methods may be difficult for nonspecialists to follow.
- **Evidence pointer** Sections 3-5, location not provided
- **Concern** The descriptions of all-atom, coarse-grained, and mesoscopic models assume familiarity with simulation techniques. Terms such as "curvature imprint" and "thermal Casimir-like force" are introduced without sufficient explanation.
- **Why it matters** The review aims to reach a broad audience, including experimentalists and cell biologists. If the methods are not explained clearly, these readers may not benefit from the review.
- **Resolution test** Add a brief introductory explanation of each method, including its basic principles, strengths, and limitations, in terms accessible to nonspecialists.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Scientific importance
- **Claim pointer** The authors suggest that the methods discussed are applicable to the design of membrane-penetrating nanoparticles and the study of protein phase separation at membrane surfaces.
- **Evidence pointer** Sections 1 and 6, location not provided
- **Concern** These applications are mentioned but not developed. The review does not explain how the methods discussed for toxin entry would be adapted for these other problems.
- **Why it matters** The claim of broader applicability is a key selling point of the review. Without elaboration, it remains an unsupported assertion.
- **Resolution test** Provide specific examples or a brief discussion of how the methods have been or could be applied to nanoparticle design and protein phase separation.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Abstract
- **Evidence pointer** Abstract, location not provided
- **Issue** The abstract is somewhat vague, particularly in the final sentence about "other likely routes for future development."
- **Required correction** Specify at least one or two concrete future directions to give readers a clearer sense of the field's trajectory.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Section 3
- **Evidence pointer** Section 3, location not provided
- **Issue** The discussion of all-atom simulations focuses heavily on the authors' own work on Shiga and cholera toxins. Other relevant studies are not mentioned.
- **Required correction** Include a broader survey of all-atom simulation studies on toxin-membrane interactions to provide a more balanced perspective.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Section 5
- **Evidence pointer** Section 5, location not provided
- **Issue** The description of the mesoscopic model based on dynamically triangulated surfaces is brief and may be difficult to follow without prior knowledge.
- **Required correction** Provide a more detailed explanation of the model and its key features, or refer the reader to the original publications for more information.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Section 6
- **Evidence pointer** Section 6, location not provided
- **Issue** The discussion of future challenges is limited to increasing membrane complexity and environmental factors. Other challenges, such as the need for better force fields or improved sampling methods, are not mentioned.
- **Required correction** Expand the discussion of future challenges to include methodological developments as well as biological complexity.

## Risk / unsupported claims
- The claim that multiscale simulation approaches are "among the first successful application" for studying toxin entry is not supported by specific examples or references.
- The assertion that the GL-Lect mechanism is "well established" is not critically evaluated, and the specific contributions of simulations to this understanding are not clearly articulated.
- The applicability of the discussed methods to nanoparticle design and protein phase separation is mentioned but not developed or supported with examples.
- The statement that simulations can provide "tuning parameters" for drug delivery vehicle design is presented without concrete examples of how this has been achieved.