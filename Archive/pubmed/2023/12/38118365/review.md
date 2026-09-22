## Review setup
- **Input scope** Full manuscript text
- **Assessment boundary** Scientific content, technical soundness, and alignment with stated scope of the review article
- **Shared manuscript claim summary** The authors argue that recent advances in molecular simulations, when integrated with experimental validation, reveal that unbound intrinsically disordered proteins (IDPs) autonomously form transient local structures and self-interactions that determine their binding behavior, and that this emerging understanding is enabling rational drug design and biosensor engineering.
- **Visible evidence base** Full text of the review article, including abstract, introduction, five thematic sections, and acknowledgements. No figures, tables, or supplementary materials were provided.
- **Missing materials affecting confidence** Figures (including Figure 1 referenced in the Introduction), any tables, reference list, and supplementary information were not provided. This limits verification of specific claims tied to visual data and citation accuracy.

## Reviewer
- **Overall assessment** This is a well-structured and timely review that synthesizes recent progress in simulating intrinsically disordered proteins and integrating those simulations with experimental data. The authors present a coherent narrative around the emerging theme of transient local structures in unbound IDPs as determinants of binding behavior. The manuscript is generally well-written and accessible to a broad readership. However, several claims lack specific citations or detailed methodological context, and the absence of figures and references in the provided material limits full evaluation. The review would benefit from more critical discussion of limitations and alternative interpretations.
- **Who would be interested in the results, and why** Researchers in computational biophysics, molecular dynamics simulation, structural biology, and biophysical chemistry would find this review valuable. Additionally, investigators studying protein-protein interactions, phase separation, drug discovery targeting IDPs, and biosensor design would benefit from the synthesis of recent methodological advances and biological insights. The review is also relevant for those interested in the integration of computation and experiment in molecular biology.
- **Major strengths** The review is timely and addresses a rapidly evolving field. The organization is logical, progressing from simulation methods to conformational biases, binding mechanisms, functional implications, and applications. The authors effectively highlight the importance of transient structures in unbound IDPs, a concept that is gaining traction. The inclusion of recent examples, such as the CytR and NCBD studies, provides concrete illustrations. The final section on biotechnological applications broadens the appeal and demonstrates translational relevance.
- **Major Concerns** 
  - R1-M1
  - R1-M2
  - R1-M3
- **Minor Comments** 
  - R1-m1
  - R1-m2
  - R1-m3
  - R1-m4
- **Technical failings that need to be addressed before the case is established** The manuscript is a review, not a primary research article, so the standard of "case established" applies to the coherence and support of the synthesis. The main technical failing is the lack of specific citations for several key claims, which prevents verification. Additionally, the discussion of simulation methods would benefit from more detail on force-field limitations and validation criteria.
- **Assessment against Nature-style criteria** 
  - Originality: The review synthesizes recent literature but does not present new data. Its originality lies in framing the field around the concept of transient structures in unbound IDPs. This is a useful perspective but not entirely novel.
  - Scientific importance: The topic is of high importance given the prevalence of IDPs in biology and disease. The review addresses key questions about binding mechanisms and specificity.
  - Interdisciplinary readership: The manuscript is likely to appeal to computational and experimental biophysicists, structural biologists, and biochemists. The writing is accessible, though some sections assume familiarity with simulation techniques.
  - Technical soundness: The technical content appears sound based on the text, but the absence of references and figures limits full assessment. Some claims are stated without supporting citations.
  - Readability for nonspecialists: The review is generally readable, but the methods section may be challenging for those without a computational background. The authors could improve accessibility by briefly explaining key simulation techniques.
- **Recommendation posture** Supportive if technical concerns are resolved, specifically the addition of citations for key claims and clarification of methodological details.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence quality
- **Claim pointer** The authors state that "recent results strongly indicate that IDP ensembles... contain networks of fleeting local structures and tertiary interactions that render specific conformational biases" and that these "could certainly drive the specific responses of IDPs to binding partners."
- **Evidence pointer** Section "Conformational Biases and Dynamics", location not provided
- **Concern** The claim that IDP ensembles universally contain transient structures that determine binding behavior is presented as a general conclusion, but the supporting evidence is drawn from a limited number of examples. The authors cite references [10-12, 26-29] but do not discuss potential counterexamples or the possibility that some IDPs may lack such structures. The generalization may overstate the current evidence.
- **Why it matters** If the central thesis of the review is overstated, it could mislead readers about the universality of the proposed mechanism. A more balanced discussion acknowledging variability among IDPs would strengthen the scientific credibility.
- **Resolution test** The authors should either provide a more comprehensive survey of evidence, including cases where transient structures are absent, or temper the claim to reflect the current state of knowledge.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors state that "new hybrid tempering protocols have been developed that accelerate water dynamics in replica exchange simulations of IDPs without ensemble reweighting, and seem to scale well for large IDPs [19]."
- **Evidence pointer** Section "Simulation Methods for IDP Dynamics", location not provided
- **Concern** The description of the hybrid tempering protocol is brief and lacks technical detail. It is unclear how the method accelerates water dynamics, what "without ensemble reweighting" means in practice, and what evidence supports the claim of scalability. Without more detail, readers cannot assess the validity or utility of the method.
- **Why it matters** The review aims to inform readers about methodological advances. If a method is described too vaguely, readers cannot evaluate its potential applicability to their own research.
- **Resolution test** The authors should expand the description of the hybrid tempering protocol, including the underlying principle, validation results, and any limitations.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence quality
- **Claim pointer** The authors state that "a recent NMR study of an IDP that folds into a 3-helix bundle upon binding to DNA discovered that the globular structure forms transiently in the unbound IDP as an excited state [35]" and that this supports a "strict conformational selection mechanism."
- **Evidence pointer** Section "Interactions, Ordering Transitions, and Binding Mechanisms", location not provided
- **Concern** The interpretation of the NMR study as evidence for "strict conformational selection" is presented without critical evaluation. The authors do not discuss alternative interpretations, such as the possibility of induced-fit contributions that were not detected due to experimental limitations. The term "strict" may be too strong given the inherent uncertainties in detecting transient states.
- **Why it matters** The distinction between conformational selection and induced-fit has important mechanistic implications. Overinterpreting a single study could bias the reader's understanding of IDP binding mechanisms.
- **Resolution test** The authors should either provide a more nuanced discussion of the NMR study's limitations or soften the claim to acknowledge potential alternative mechanisms.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Abstract
- **Evidence pointer** Abstract, location not provided
- **Issue** The phrase "exploit their plasticity to deploy a rich panoply of soft interactions" is somewhat vague and could be more precise.
- **Required correction** Consider rephrasing to more concretely describe the types of interactions and their functional consequences.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Section "Simulation Methods for IDP Dynamics"
- **Evidence pointer** Section "Simulation Methods for IDP Dynamics", location not provided
- **Issue** The discussion of machine learning for generating IDP ensembles is brief and does not mention potential limitations, such as the need for training data or the risk of overfitting.
- **Required correction** Add a sentence acknowledging the limitations of machine learning approaches in this context.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Section "IDP Function and Disease"
- **Evidence pointer** Section "IDP Function and Disease", location not provided
- **Issue** The concept of "molecular logic gates" is introduced but not fully explained. Readers unfamiliar with this terminology may struggle to understand the analogy.
- **Required correction** Briefly define what is meant by a molecular logic gate in this context.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Section "Biotechnological Applications"
- **Evidence pointer** Section "Biotechnological Applications", location not provided
- **Issue** The section on drug discovery mentions "new computational protocols designed for multi-conformer targets" but does not describe these protocols or their validation.
- **Required correction** Provide a brief description of the computational protocols and cite specific examples.

## Risk / unsupported claims
- The claim that "unbound IDPs autonomously form transient local structures and self-interactions that determine their binding behavior" is presented as a general principle but is supported by a limited set of examples. This may be an overgeneralization.
- The statement that "new hybrid tempering protocols... seem to scale well for large IDPs" is not substantiated with specific performance data or comparisons to other methods.
- The interpretation of the NMR study [35] as evidence for "strict conformational selection" is not critically evaluated and may overstate the findings.
- The claim that "IDP-based drug discovery has proven difficult because IDP disorder hampers the conventional structure-based computational drug design approaches" is stated without citation or discussion of alternative approaches.
- The assertion that "an uncooperative ordering transition... facilitates the optimization of the transducer's response" is presented as a general design principle but is based on a single example.