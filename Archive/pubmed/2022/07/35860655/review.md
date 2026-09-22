## Review setup
- **Input scope** Full manuscript text including abstract, main text, figures cited, and one table referenced.
- **Assessment boundary** Scientific content, conceptual framework, evidence quality, and internal consistency of the review article as provided. No external literature verification performed.
- **Shared manuscript claim summary** The authors argue that multivalent and allovalent interactions between substrates and E3 ubiquitin ligases, particularly the APC/C, are critical for understanding substrate degradation kinetics and ordering during mitosis, and that these principles can inform the design of targeted protein degradation (TPD) tools.
- **Visible evidence base** Cited primary literature, structural studies (cryo-EM), biophysical binding data, and a bioinformatic analysis of degron predictions summarized in Table 1. Figure 1 schematics are referenced but not visible in the provided text.
- **Missing materials affecting confidence** Figures 1–5 are referenced but not provided. Table 1 is referenced but not provided. No supplementary data or methods for the bioinformatic analysis are included. No primary experimental data are presented by the authors.

## Reviewer
- **Overall assessment** This is a well-written and conceptually useful review that synthesizes known examples of multivalent and allovalent E3-substrate interactions and applies them to the APC/C system. The authors propose a plausible framework for how degron multiplicity and type contribute to substrate ordering during mitosis, and they connect this to TPD tool design. However, the manuscript is largely speculative in its central generalizations about APC/C substrate ordering, and the evidence base for the proposed distinctions between metaphase, anaphase, and G1 substrates is thin. The bioinformatic analysis presented in Table 1 is not visible, and no methods are described, limiting the ability to assess its validity. The review would benefit from clearer articulation of testable hypotheses and a more rigorous treatment of alternative explanations.
- **Who would be interested in the results, and why** Cell cycle biologists studying APC/C substrate specificity and mitotic exit; biochemists and structural biologists interested in E3 ligase-substrate interactions; and researchers in the targeted protein degradation field, particularly those designing PROTACs or molecular glues that aim to harness APC/C or other E3s. The conceptual distinction between multivalency and allovalency is of broad interest to the ubiquitin field.
- **Major strengths** The review provides a clear and accessible synthesis of key concepts (multivalency, allovalency, cooperativity) with well-chosen examples. The focus on APC/C substrate ordering is timely and relevant. The authors make a useful conceptual contribution by framing substrate competition in terms of degron quantity and type, and by connecting this to TPD design. The writing is clear and logically structured.
- **Major Concerns** The central generalizations about APC/C substrate degron distributions (Section 4) are based on a bioinformatic analysis that is not visible and lacks methodological detail. The distinction between metaphase, anaphase, and G1 substrate requirements is presented as a coherent model but is supported by limited direct evidence. The review does not critically evaluate alternative mechanisms for substrate ordering, such as coactivator switching, phosphorylation, or differential processivity, in sufficient depth. The claim that allovalency could be exploited for TPD design is interesting but underdeveloped.
- **Minor Comments** Some terminology is used loosely (e.g., "allovalency" is defined but the distinction from "avidity" could be sharper). The review would benefit from a summary table of key experimental evidence for each example discussed. The authors state that "pseudo-substrates should bind more tightly than the substrates with which they compete" without providing a citation or mechanistic justification. The section on TPD design is brief and could be expanded with more concrete examples or proposals.
- **Technical failings that need to be addressed before the case is established** The bioinformatic analysis underlying Table 1 and the generalizations in Section 4 is not described. No methods, thresholds, or validation are provided. The authors do not state how degron predictions were made, which database or algorithm was used, or how false positives were handled. Without this, the central claims about degron distributions in APC/C substrates cannot be evaluated.
- **Assessment against Nature-style criteria**  
  - Originality: Moderate. The synthesis of multivalency and allovalency concepts in the context of APC/C substrate ordering is somewhat novel, but the individual concepts are well established.  
  - Scientific importance: Moderate to high. The APC/C substrate ordering problem is important, and the connection to TPD is timely.  
  - Interdisciplinary readership: Moderate. The review bridges cell cycle biology and targeted protein degradation, which will appeal to both communities.  
  - Technical soundness: Weak. The central bioinformatic analysis is not described, and the speculative model is not rigorously supported.  
  - Readability for nonspecialists: Good. The writing is clear, and concepts are introduced in an accessible manner, though some prior knowledge of ubiquitin biology is assumed.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence quality and reproducibility
- **Claim pointer** The authors state: "we used the bioinformatic resources created by Norman Davey and colleagues (http://slim.icr.ac.uk/apc/) to map the incidence of validated and predicted degrons in a panel of known substrates of the APC/C (Table 1)" and subsequently propose generalizations about degron distributions in metaphase, anaphase, and G1 substrates.
- **Evidence pointer** Section 4, Table 1 (not provided)
- **Concern** The bioinformatic analysis is central to the manuscript's main conceptual contribution, yet no methods are described. The authors do not specify which degron prediction algorithm was used, how thresholds were set, how validated versus predicted degrons were distinguished, or how the substrate panel was selected. Table 1 is not visible, so the data cannot be inspected. The generalizations drawn from this analysis are therefore not verifiable.
- **Why it matters** The proposed model of substrate ordering by degron number and type rests entirely on this analysis. Without methodological transparency and access to the data, the central claims of the review cannot be assessed or reproduced.
- **Resolution test** Provide a detailed methods section for the bioinformatic analysis, including the algorithm, parameters, and validation. Make Table 1 available with clear annotation of validated versus predicted degrons, and include the full list of substrates analyzed.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** No
- **Axis** Conceptual rigor and alternative explanations
- **Claim pointer** The authors propose that "the broadening of substrate specificity at anaphase onset reflects a relaxation of requirements for efficient substrate ubiquitination" and that "multivalency is important for efficient targeting of anaphase substrates by FZR1, allowing them to outcompete other substrates, but that reduced competition in G1 phase renders multi- or allo-valency of degrons dispensable."
- **Evidence pointer** Sections 4.2 and 4.3
- **Concern** The model is presented as a coherent framework, but alternative mechanisms for substrate ordering are not critically evaluated. The authors mention coactivator switching, phosphorylation, and processivity as contributing factors but do not integrate them into their model or discuss how they might interact with degron multiplicity. The claim that reduced competition in G1 makes multivalency dispensable is speculative and not directly supported by experimental evidence.
- **Why it matters** The APC/C substrate ordering problem is complex, and multiple mechanisms are likely at play. A review that proposes a new framework should engage seriously with competing explanations and clarify what evidence would distinguish between them.
- **Resolution test** Expand the discussion of alternative mechanisms and explicitly state what experimental predictions follow from the authors' model versus others. Provide specific examples or citations that support or challenge the claim about G1 substrates.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Support for TPD design claims
- **Claim pointer** The authors state: "Multivalency could thus be viewed as a useful tool for enhancing substrate affinity for an E3 ligase in the design of TPD tools" and suggest that "multimerizing single degrons to create allovalency could be a way of promoting affinity of a neo-substrate for the APC/C without competing with the critical metaphase substrates."
- **Evidence pointer** Section 5
- **Concern** The TPD design proposals are interesting but are not developed beyond a general suggestion. No specific examples of how allovalency could be engineered into a PROTAC or molecular glue are provided, and no consideration is given to potential pitfalls, such as altered substrate specificity, off-target effects, or the challenges of mimicking allovalent kinetics in a synthetic context.
- **Why it matters** The connection to TPD is a major selling point of the review, but the practical implications are not fleshed out. Readers in the TPD field will want more concrete guidance or at least a clearer articulation of the design principles being proposed.
- **Resolution test** Expand the perspective section with specific design proposals, discuss potential challenges, and reference any existing TPD tools that already exploit multivalent or allovalent principles.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Terminology precision
- **Affected element** Section 2.2, definition of allovalency
- **Evidence pointer** Section 2.2
- **Issue** The distinction between allovalency and avidity could be sharper. The authors define allovalency as a single binding site engaging multiple identical epitopes, but the kinetic consequences are described in terms that overlap with avidity effects.
- **Required correction** Clarify the mechanistic distinction between allovalency and avidity, and consider providing a simple kinetic scheme or equation to illustrate the difference.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Citation support
- **Affected element** Section 3.1, statement about pseudo-substrates
- **Evidence pointer** Section 3.1
- **Issue** The statement "pseudo-substrates should bind more tightly than the substrates with which they compete" is made without citation or mechanistic justification.
- **Required correction** Add a citation or provide a brief mechanistic explanation for why pseudo-substrates are expected to bind more tightly.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Figure accessibility
- **Affected element** Figure 1
- **Evidence pointer** Figure 1 (not visible)
- **Issue** Figure 1 is described as illustrating the different modes of multivalent binding, but the figure is not provided. The text refers to panels (A–D) without describing their content in sufficient detail for a reader without access to the figure.
- **Required correction** Ensure the figure legend is self-contained and describes each panel clearly, or add more detailed descriptions in the text.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Data presentation
- **Affected element** Table 1
- **Evidence pointer** Table 1 (not provided)
- **Issue** Table 1 is referenced multiple times and is central to the authors' generalizations, but it is not included in the provided material.
- **Required correction** Ensure Table 1 is included with the manuscript and is accompanied by a clear legend explaining the columns and the distinction between validated and predicted degrons.

## Risk / unsupported claims
- The claim that "the striking enrichment for degrons (and KEN motifs in particular) in known APC/C substrates indicates that they are likely functional motifs" is presented without quantitative data or statistical support.
- The proposal that "multimerizing single degrons to create allovalency could be a way of promoting affinity of a neo-substrate for the APC/C without competing with the critical metaphase substrates" is speculative and not supported by experimental evidence.
- The generalization that "reduced competition in G1 phase renders multi- or allo-valency of degrons dispensable" is not directly supported by the cited literature.
- The statement that "pseudo-substrates should bind more tightly than the substrates with which they compete" is unsupported by citation or mechanistic argument.
- The bioinformatic analysis underlying Table 1 and the generalizations in Section 4 is not described and cannot be evaluated.