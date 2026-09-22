## Review setup
- **Input scope** Full manuscript text
- **Assessment boundary** Scientific content, technical accuracy, and presentation quality of the review article
- **Shared manuscript claim summary** The manuscript provides a comprehensive overview of implicit solvent models, covering classical continuum electrostatics (PB/GB), nonpolar treatments, quantum-continuum models (PCM, COSMO, SMx/SMD), and emerging machine learning-augmented and quantum computing-based approaches, with applications in biophysics.
- **Visible evidence base** Full text including equations, tables, and figure references
- **Missing materials affecting confidence** Figures and tables referenced in the text were not provided; line numbers were not available

## Reviewer
- **Overall assessment** This manuscript offers a broad and timely survey of implicit solvent models, spanning classical to quantum and machine learning approaches. The scope is ambitious and the topic is of high relevance to computational biophysics. However, the depth of treatment is uneven, with some sections reading as a catalog of methods rather than a critical synthesis. The manuscript would benefit from a clearer organizing framework, more rigorous comparative analysis, and improved technical precision in several areas. The discussion of emerging directions, particularly quantum computing and machine learning, is forward-looking but lacks critical evaluation of current limitations.

- **Who would be interested in the results, and why** Computational biophysicists and chemists seeking a broad overview of available implicit solvent methods; researchers entering the field who need a map of the landscape; practitioners looking for guidance on method selection for specific applications such as protein-ligand binding or intrinsically disordered protein simulations. The review could serve as a useful teaching resource for graduate courses in computational chemistry.

- **Major strengths** 
  1. Comprehensive coverage of the field from historical foundations to cutting-edge developments
  2. Clear presentation of mathematical formulations for key models
  3. Timely inclusion of machine learning and quantum computing frontiers
  4. Practical focus on applications in biophysics, particularly intrinsically disordered proteins
  5. Balanced discussion of strengths and limitations of different approaches

- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The manuscript claims to provide a comprehensive and critical overview of implicit solvent models, but several technical descriptions contain inaccuracies or oversimplifications that undermine confidence in the review's reliability.
- **Evidence pointer** Section 2.1, equations (1)-(18); Section 2.2, equations (19)-(35)
- **Concern** The derivation and presentation of several equations contain errors or lack necessary context. For example, equation (1) presents the Debye equation but the notation is inconsistent with standard treatments. The transition from equation (4) to the discussion of cavity formation is abrupt and the physical meaning of the terms is not adequately explained. In Section 2.2, the presentation of the Poisson-Boltzmann equation and its linearization is oversimplified, and the relationship between equations (19) and (20) is not clearly established. The treatment of the Generalized Born model in equation (38) omits important details about the effective Born radii calculation. These technical imprecisions are problematic for a review article that aims to be a reference resource.
- **Why it matters** A review article's primary value lies in its reliability as a reference. Technical errors or unclear derivations can mislead readers, particularly those new to the field. The manuscript's stated goal of providing a "critical resource" is undermined by these inaccuracies.
- **Resolution test** The authors should carefully verify all equations against primary literature sources, provide more complete derivations or clear citations for each equation, and ensure that the physical meaning of all terms is explicitly stated. A technical expert in the field should be consulted to verify the accuracy of the mathematical content.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Scientific importance
- **Claim pointer** The manuscript claims to highlight "where these methods excel and where they falter" and to provide guidance for method selection, but the comparative analysis is insufficient to support this claim.
- **Evidence pointer** Sections 2-5, particularly the transitions between model descriptions
- **Concern** The review describes many methods but provides limited critical comparison between them. For example, the discussion of DelPhi and APBS in Section 2.4 and 2.5 describes their features but does not critically evaluate their relative performance, limitations, or appropriate use cases. Similarly, the comparison between EEF1 and ABSINTH in Section 5 is superficial, noting differences without explaining the practical implications for users. The manuscript would benefit from a systematic comparative framework, such as tables summarizing key features, accuracy benchmarks, computational costs, and recommended applications for each method.
- **Why it matters** The stated goal of the review is to help readers select appropriate methods for their research. Without rigorous comparative analysis, readers cannot make informed decisions. The review risks becoming a descriptive catalog rather than a critical guide.
- **Resolution test** The authors should add comparative tables or structured discussions that systematically evaluate methods across key dimensions (accuracy, speed, applicability, limitations). Where benchmark data exists, it should be presented and discussed. The conclusions should provide clear, actionable guidance for method selection.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Interdisciplinary readership
- **Claim pointer** The manuscript aims to be accessible to a broad audience in biophysics, but the presentation assumes significant prior knowledge and lacks sufficient context for nonspecialists.
- **Evidence pointer** Throughout, particularly Sections 2 and 3
- **Concern** The manuscript moves rapidly through complex topics without adequate introduction or context. For example, the discussion of quantum-continuum models in Section 3 assumes familiarity with quantum chemistry concepts that may not be familiar to all biophysicists. The treatment of machine learning methods in Section 4 introduces concepts like "graph neural networks" and "uncertainty quantification" without sufficient explanation for readers outside these fields. The applications section (Section 5) jumps between different biological systems without providing adequate background for each.
- **Why it matters** The review's stated audience includes biophysicists who may not be experts in all covered areas. If the presentation is not accessible, the review fails to serve its purpose as a bridge between disciplines.
- **Resolution test** The authors should add introductory paragraphs for each major section that provide context for nonspecialists. Technical terms should be defined at first use. The applications section should provide more background on each biological system and why implicit solvent models are particularly relevant.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Technical soundness
- **Claim pointer** The manuscript discusses machine learning-augmented approaches and quantum computing applications, but the treatment of these emerging areas lacks critical depth and overstates current capabilities.
- **Evidence pointer** Section 3.3 and Section 4
- **Concern** The discussion of quantum computing applications (Section 3.3) describes a single proof-of-concept study without critically evaluating its limitations, scalability challenges, or practical relevance. The claim that this "maps a credible scaling path" is optimistic given the current state of quantum hardware. Similarly, the machine learning section (Section 4) presents results from specific studies without adequate discussion of generalization limitations, data requirements, or potential failure modes. The statement that "hybridization" will "dominate the field" is presented as a prediction without sufficient evidence or discussion of challenges.
- **Why it matters** Emerging areas are often overhyped, and a critical review should provide balanced assessment. Overstating current capabilities can mislead readers about the readiness of these methods for practical applications.
- **Resolution test** The authors should provide more balanced discussions of limitations and challenges in these emerging areas. For quantum computing, discuss error rates, qubit counts, and scalability challenges. For machine learning, discuss data requirements, generalization limits, and validation challenges. The conclusions should be more measured and evidence-based.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Readability for nonspecialists
- **Affected element** Abstract
- **Evidence pointer** Abstract, first sentence
- **Issue** The phrase "quiet majority" is informal and unclear in a scientific context. The abstract would benefit from a more precise opening statement.
- **Required correction** Replace with a more precise statement, such as "Solvents constitute the majority of molecules in biomolecular systems, yet their explicit representation remains computationally demanding."

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Technical soundness
- **Affected element** Section 2.1, equation (1)
- **Evidence pointer** Section 2.1, equation (1)
- **Issue** The notation in equation (1) is inconsistent with standard treatments of the Debye equation. The use of ε for both dielectric constant and permittivity is confusing.
- **Required correction** Clarify notation and ensure consistency with standard literature. Define all symbols explicitly.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Readability for nonspecialists
- **Affected element** Section 3.2
- **Evidence pointer** Section 3.2, discussion of COSMO-RS
- **Issue** The distinction between COSMO and COSMO-RS is not clearly explained. The text jumps between the two without adequately describing the relationship and differences.
- **Required correction** Provide a clearer explanation of how COSMO-RS extends COSMO, including the statistical thermodynamics treatment.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Scientific importance
- **Affected element** Section 5
- **Evidence pointer** Section 5, applications
- **Issue** The applications section is brief and does not provide sufficient depth on how implicit solvent models have contributed to specific biological insights.
- **Required correction** Expand the applications section with more detailed case studies showing how implicit solvent models have led to specific biological discoveries or insights.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Readability for nonspecialists
- **Affected element** Section 4
- **Evidence pointer** Section 4, machine learning discussion
- **Issue** The discussion of machine learning methods assumes familiarity with specific architectures and techniques without adequate introduction.
- **Required correction** Add brief explanations of key machine learning concepts (e.g., graph neural networks, uncertainty quantification) for readers outside this field.

- **Concern ID** R1-m6
- **Severity** Minor
- **Axis** Technical soundness
- **Affected element** Section 2.5, APBS
- **Evidence pointer** Section 2.5
- **Issue** The description of the APBS model's numerical methods is brief and does not adequately explain the advantages of the adaptive multilevel finite element approach.
- **Required correction** Expand the discussion of APBS's numerical methods and explain why the adaptive approach is beneficial for biomolecular systems.

## Risk / unsupported claims
- The claim that quantum computing approaches "map a credible scaling path" (Section 3.3) is not supported by the evidence presented, which describes only a single proof-of-concept study on current hardware with significant limitations.
- The prediction that "hybridization will dominate the field" (Section 4) is presented without sufficient evidence or discussion of potential barriers.
- The statement that machine learning models can achieve "PB-level accuracy at GB-like cost" (Section 4) is based on limited benchmark studies and may not generalize across diverse systems.
- The claim that implicit solvent models "enable rapid hypothesis testing, large design sweeps, and long-time sampling" (Abstract and Section 5) is presented without specific examples or quantitative evidence.
- The assertion that "none of these models could provide chemical accuracy" (Section 5, referring to desolvation energy calculations) is based on a single study and may not be universally applicable.