## Review setup
- **Input scope** Full manuscript text (abstract, main text, figure legends not provided)
- **Assessment boundary** Scientific content, conceptual framework, evidence integration, and internal consistency of the proposed model
- **Shared manuscript claim summary** The authors propose that SASH1 functions as a context-dependent multi-docking scaffold that organizes signaling architecture by linking receptor signaling to cytoskeletal dynamics. They synthesize structural, biochemical, genetic, and functional evidence across cell types and disease contexts, grouping SASH1 interactions into three functional modules (receptor regulation, intracellular signaling, cytoskeletal organization) and propose a hierarchical "scaffold-of-scaffolds" model.
- **Visible evidence base** Text descriptions of published experimental results (co-crystallography, NMR, microscale thermophoresis, yeast two-hybrid, co-immunoprecipitation, mutagenesis, mouse genetics, human genetic variants); Table references (Tables 1-5); Figure references (Figures 1-4, 6-8); AlphaFold2 model predictions
- **Missing materials affecting confidence** Figures and tables not provided; reference list not provided; figure legends not provided; specific experimental details and quantitative data not available for independent verification

## Reviewer
- **Overall assessment** This is a well-structured and thoughtfully argued review that proposes a unifying mechanistic framework for SASH1 function. The authors synthesize a broad and heterogeneous literature into a coherent model centered on SASH1 as a context-dependent multi-docking scaffold. The manuscript is clearly written and the conceptual organization into three functional modules is useful. However, the central claim of a "scaffold-of-scaffolds" architecture remains largely speculative, as the authors themselves acknowledge that simultaneous engagement of multiple partners by full-length SASH1 has not been demonstrated. The review would benefit from a more critical treatment of the evidence base, particularly regarding the strength of interaction data for several key partners, and from a clearer articulation of how the proposed model generates testable predictions that distinguish it from alternative explanations.
- **Who would be interested in the results, and why** Cell biologists studying scaffold proteins and signal integration; researchers in pigmentation biology and melanocyte stem cell biology; cancer biologists interested in tumor suppressors and metastasis; vascular biologists studying endothelial signaling and angiogenesis; structural biologists interested in multidomain proteins and intrinsically disordered regions. The review provides a framework that could inform studies of other scaffold proteins and offers a potential bridge between molecular architecture and disease phenotypes.
- **Major strengths** 
  1. The manuscript addresses a genuine gap in the field: the absence of a unifying mechanistic framework for SASH1 function despite extensive genetic and biochemical data.
  2. The proposed model is conceptually elegant and provides a plausible explanation for the pleiotropic functions of SASH1 across diverse biological contexts.
  3. The authors are appropriately cautious in several places, explicitly acknowledging when evidence is limited or when conclusions remain speculative.
  4. The organization of interactions into functional modules (receptor regulation, intracellular signaling, cytoskeletal organization) is a useful heuristic that helps organize a complex literature.
  5. The inclusion of an evidence-tier system (Table 5) for different interactions is commendable and adds transparency.
  6. The discussion of intrinsically disordered regions and their potential role in multivalent interactions and phase separation is timely and thought-provoking.
- **Major Concerns**
  - **Concern ID** R1-M1
  - **Severity** Major
  - **Blocking** Yes
  - **Axis** Conceptual framework / model validity
  - **Claim pointer** The central claim that SASH1 functions as a "context-dependent multi-docking scaffold" that "links receptor signaling to cytoskeletal dynamics" through a hierarchical "scaffold-of-scaffolds" architecture.
  - **Evidence pointer** Sections 4, 4.5, 4.6; Table 5
  - **Concern** The central model is presented as a unifying framework, but the evidence that SASH1 simultaneously assembles multiple partners into a higher-order signaling complex is not established. The authors acknowledge that "simultaneous recruitment of multiple partners by full-length SASH1 has not yet been demonstrated" (Section 4.1), yet the model is repeatedly presented as if this were the case. The "scaffold-of-scaffolds" concept is introduced with limited direct evidence that SASH1 engages pre-existing scaffold complexes rather than simply binding individual partners in a sequential or mutually exclusive manner.
  - **Why it matters** The scientific value of the proposed model depends on its ability to explain phenomena that alternative explanations (e.g., SASH1 as a simple adaptor with multiple independent binding partners) cannot. Without evidence for simultaneous engagement or hierarchical organization, the "scaffold-of-scaffolds" model risks being a restatement of the observation that SASH1 has multiple binding partners, rather than a genuinely new mechanistic insight.
  - **Resolution test** The authors should either (a) provide a more explicit articulation of what distinguishes the "scaffold-of-scaffolds" model from a conventional multi-adaptor model, including specific testable predictions, or (b) reframe the model as a hypothesis with clearly stated criteria that would falsify it. Alternatively, they could present the model more modestly as a conceptual organizing framework rather than a mechanistically established architecture.
  - **Concern ID** R1-M2
  - **Severity** Major
  - **Blocking** No
  - **Axis** Evidence quality / critical appraisal
  - **Claim pointer** The claim that SASH1 interacts with cortactin, IQGAP1, and PKM2, and that these interactions support the proposed model.
  - **Evidence pointer** Sections 4.1, 6.1, 6.2; Table 5
  - **Concern** The authors note that the cortactin, IQGAP1, and PKM2 interactions are "supported mainly by co-immunoprecipitation, with their SASH1-binding interfaces still unmapped" (Section 4.1). Yet these interactions are subsequently used as evidence for the model's claims about cytoskeletal regulation and scaffold-of-scaffolds organization. Co-immunoprecipitation alone is notoriously prone to false positives and does not establish direct physical interaction. The review would benefit from a more critical discussion of the limitations of these data and from a clearer separation between well-validated interactions (e.g., EphA8, TNFR6) and those requiring further validation.
  - **Why it matters** The strength of the proposed model depends on the reliability of the interaction data on which it is built. If key interactions are not robustly validated, the model's foundation is weakened. Readers need to understand which parts of the model rest on solid evidence and which are provisional.
  - **Resolution test** The authors should explicitly flag which interactions meet a higher evidence threshold (structural or quantitative biophysical data) and which are supported only by immunoprecipitation, and should adjust the strength of their claims accordingly. They should also discuss whether any of these interactions have been independently replicated.
  - **Concern ID** R1-M3
  - **Severity** Major
  - **Blocking** No
  - **Axis** Conceptual clarity / model specificity
  - **Claim pointer** The claim that SASH1's "context-dependent" function arises from selective partner recruitment in different cellular environments.
  - **Evidence pointer** Sections 1, 2, 4.6
  - **Concern** The concept of "context-dependence" is invoked repeatedly but never precisely defined. What constitutes "context"? Cell type? Signaling state? Subcellular localization? Post-translational modifications? The authors mention several possibilities but do not articulate a coherent framework for how context is encoded and decoded by SASH1. Without a clearer specification of what determines partner selection, the "context-dependent" aspect of the model remains vague and difficult to test.
  - **Why it matters** The claim that SASH1 generates "cell-type-specific outputs" is central to the model's explanatory power. If the mechanisms of context-dependence are not specified, the model cannot be distinguished from a simpler explanation in which SASH1 simply binds whatever partners happen to be expressed in a given cell type.
  - **Resolution test** The authors should provide a more explicit account of the molecular mechanisms that could confer context-dependence (e.g., competitive binding, post-translational modification-dependent switching, subcellular compartmentalization, expression-level thresholds) and should discuss which of these are supported by existing data.
  - **Concern ID** R1-M4
  - **Severity** Major
  - **Blocking** No
  - **Axis** Scope / depth of coverage
  - **Claim pointer** The claim that the review provides a comprehensive synthesis of SASH1 biology across "pigmentation, innate immunity, receptor signaling, cytoskeletal dynamics, vascular biology, and tumor suppression."
  - **Evidence pointer** Sections 2, 5, 6, 7, 8, 9
  - **Concern** The coverage of some areas is uneven. The pigmentation and vascular biology sections are relatively detailed, while the innate immunity section is comparatively brief. The cancer section appropriately notes the correlative nature of much of the evidence, but the discussion of specific cancer types is somewhat cursory. Given the breadth of the claims, a more systematic and balanced treatment of each area would strengthen the review.
  - **Why it matters** A review that claims to synthesize a broad literature should provide reasonably balanced coverage. If some areas are treated superficially, readers in those fields may not find the synthesis useful, and the overall credibility of the review is diminished.
  - **Resolution test** The authors should either expand the coverage of underdeveloped areas or explicitly state that some areas are covered in less depth due to space constraints or limitations in the available literature.
- **Minor Comments**
  - **Concern ID** R1-m1
  - **Severity** Minor
  - **Axis** Clarity / terminology
  - **Affected element** Section 3.2, domain organization
  - **Evidence pointer** Section 3.2
  - **Issue** The term "SPIDER" is used throughout, but the rationale for this acronym is not explained in the text. Readers unfamiliar with the SLy protein literature may find this confusing.
  - **Required correction** Provide the full expansion of the acronym at first use, or at least a brief explanation of its origin.
  - **Concern ID** R1-m2
  - **Severity** Minor
  - **Axis** Internal consistency
  - **Affected element** Section 4.2, phase separation discussion
  - **Evidence pointer** Section 4.2
  - **Issue** The discussion of liquid-liquid phase separation (LLPS) is interesting but somewhat disconnected from the rest of the review. The authors note that "whether SASH1 undergoes LLPS is currently unknown" and that "no condensate behavior has been directly demonstrated," yet the topic is given substantial space. This is acceptable as a speculative discussion, but it should be more clearly framed as such.
  - **Required correction** Add an explicit statement that this is a speculative hypothesis and clarify how it relates to the central model being proposed.
  - **Concern ID** R1-m3
  - **Severity** Minor
  - **Axis** Completeness / future directions
  - **Affected element** Section 11, knowledge gaps
  - **Evidence pointer** Section 11
  - **Issue** The list of knowledge gaps is useful but somewhat generic. Several of the gaps identified (e.g., lack of full-length structure, need for systematic PTM mapping) are common to many proteins and could be stated more specifically in the context of SASH1.
  - **Required correction** Where possible, make the knowledge gaps more specific to SASH1 and its proposed scaffold function, and prioritize them in terms of which are most critical for testing the model.
  - **Concern ID** R1-m4
  - **Severity** Minor
  - **Axis** Presentation / accessibility
  - **Affected element** Abstract
  - **Evidence pointer** Abstract
  - **Issue** The abstract is dense and uses specialized terminology (e.g., "scaffold-of-scaffolds") without sufficient context. For a broad readership, a brief explanation of what a multi-docking scaffold is and why this matters would improve accessibility.
  - **Required correction** Add one or two sentences in the abstract that explain the concept of a scaffold protein and why the proposed model is significant beyond the SASH1 field.
  - **Concern ID** R1-m5
  - **Severity** Minor
  - **Axis** Evidence presentation
  - **Affected element** Section 5.2, variant distribution
  - **Evidence pointer** Section 5.2; Figure 4
  - **Issue** The claim that "more than 70% of reported pigmentation-associated variants localize to the SPIDER" is presented without a clear denominator. How many variants total? How many are in each domain? A simple table or more detailed breakdown would strengthen this claim.
  - **Required correction** Provide the total number of variants and the distribution across domains, either in the text or in a supplementary table.
  - **Concern ID** R1-m6
  - **Severity** Minor
  - **Axis** Interpretation / overreach
  - **Affected element** Section 8.4, cancer context-dependence
  - **Evidence pointer** Section 8.4
  - **Issue** The discussion of context-dependent cancer functions is thoughtful, but the claim that the scaffold model "readily explains" the observed variability in SASH1's prognostic associations may be overstated. The model provides a plausible framework, but it does not yet explain the specific mechanisms by which context determines whether SASH1 acts as a tumor suppressor or promoter.
  - **Required correction** Soften the language from "readily explains" to "provides a plausible framework for understanding" or similar.

## Risk / unsupported claims
- The "scaffold-of-scaffolds" hierarchical model is presented as a central concept but lacks direct experimental support for simultaneous engagement of multiple scaffold partners by full-length SASH1.
- The claim that SASH1 "links receptor signaling to cytoskeletal dynamics" implies a mechanistic connection that is inferred from separate interaction datasets rather than demonstrated in a single experimental system.
- The interactions with cortactin, IQGAP1, and PKM2 are described as supporting the model, but the evidence for these interactions is limited to co-immunoprecipitation and the binding interfaces are unmapped.
- The proposal that SASH1 may undergo liquid-liquid phase separation is explicitly speculative and should not be presented as a likely mechanism without direct evidence.
- The claim that disease-associated variants "likely perturb the strength, composition, or regulation of specific SASH1 interactions" is reasonable but remains a hypothesis; for most variants, the functional consequences have not been characterized.
- The statement that SASH1's "principal function" is the organization of signaling architecture is an interpretive claim that goes beyond the available data, which support a role in signaling but do not establish this as the principal function.
- The assertion that SASH1 is "distinguished" from its SLy-family paralogs by the presence of a second C-terminal SAM domain and broader tissue expression is presented as established fact, but the functional significance of these differences has not been directly tested.
- The evolutionary conservation argument (Section 3.3) implies functional importance, but conservation alone does not establish the specific functions proposed in the model.