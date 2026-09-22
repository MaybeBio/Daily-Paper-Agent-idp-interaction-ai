## Review setup
- **Input scope** Full manuscript text (review article) as provided by the user, including abstract, main text, and standard sections (author contributions, conflict of interest, etc.). No figures, tables, or supplementary material were provided.
- **Assessment boundary** The review assesses the manuscript's scientific content, structure, and claims as presented in the provided text. It does not assess the accuracy of the cited literature or the validity of the underlying data in the original studies discussed, as these are not available for verification.
- **Shared manuscript claim summary** The manuscript argues that AI-based methods, particularly deep learning models, offer a transformative and often superior alternative to traditional MD simulations for sampling conformational ensembles of intrinsically disordered proteins (IDPs). It claims these methods are faster, can access rare states, and can achieve comparable or better experimental agreement, while acknowledging limitations such as data dependence and interpretability.
- **Visible evidence base** The manuscript's arguments are supported by descriptions of specific AI models (e.g., idpGAN, idpSAM, IDPFold, Phanto-IDP, ICoN, AF-MI) and their reported performance metrics, as cited from the primary literature. The text also includes general statements about the limitations of MD simulations and the potential of AI, supported by citations.
- **Missing materials affecting confidence** The review is based solely on the manuscript text. The absence of figures, tables (including the referenced Table 1 and Table 2), and supplementary material limits the ability to fully evaluate the comparative data and visual summaries that are central to the manuscript's arguments. The specific quantitative claims made in the text (e.g., RMSD values, generation times) cannot be independently verified without access to the cited primary sources.

## Reviewer
- **Overall assessment** This manuscript provides a timely and broad overview of the rapidly evolving field of AI-based conformational sampling for IDPs. It successfully identifies a key challenge in the field (the computational cost and sampling limitations of MD) and presents a compelling narrative for the potential of deep learning methods to address it. The review is well-structured, covering generative models, hybrid approaches, and the critical role of experimental validation. However, the manuscript's strength lies more in its breadth than its depth. The descriptions of individual methods are often brief and lack critical comparative analysis. The central claim that AI methods "outperform" MD is presented somewhat one-sidedly, with the acknowledged disadvantages of AI (Section 8) appearing as a somewhat disconnected list rather than a balanced counterpoint integrated into the main argument. The manuscript would be significantly strengthened by a more critical and nuanced discussion of the conditions under which AI methods are genuinely superior, and by a clearer synthesis of the field's current capabilities and limitations. The writing is generally clear but could benefit from more precise language in places.
- **Who would be interested in the results, and why** This review would be of primary interest to researchers in the computational biophysics and structural biology communities, particularly those working on IDPs. It serves as a useful entry point for experimentalists who are considering using AI tools to complement or replace MD simulations in their studies. The review's focus on the practical advantages (speed, cost) and limitations (data dependence, interpretability) of AI methods would also be valuable for researchers deciding on the most appropriate computational strategy for their specific IDP system. The discussion of experimental validation techniques (NMR, SAXS, smFRET) makes it relevant to a broader interdisciplinary audience interested in the integration of computational and experimental approaches.
- **Major strengths**
    1.  The manuscript addresses a highly relevant and timely topic, capturing the current excitement and rapid progress in applying AI to a long-standing problem in the field.
    2.  The scope is comprehensive, covering a wide range of AI architectures (GANs, VAEs, diffusion models, transformers) and their applications, from direct generation to hybrid AI-MD approaches.
    3.  The inclusion of specific case studies (e.g., Aβ42, α-synuclein) and quantitative performance metrics from the literature provides concrete examples that ground the discussion.
    4.  The review explicitly discusses the critical role of experimental data for validation and integration, which is a crucial and often underappreciated point.
    5.  The structure is logical, moving from the limitations of MD to the promise of AI, and then to the challenges and future directions.
- **Major Concerns**
    - **R1-M1**
        - **Severity** Major
        - **Blocking** No
        - **Axis** Argumentative balance and rigor
        - **Claim pointer** The manuscript's overarching thesis, as stated in the title and abstract, is that AI methods are a superior choice for sampling IDP conformational ensembles, with the abstract stating they "outperform MD in generating diverse ensembles with comparable accuracy."
        - **Evidence pointer** Abstract; Sections 4, 7, and 8
        - **Concern** The manuscript presents a largely one-sided argument in favor of AI methods. While Section 8 lists disadvantages, this section is not well-integrated into the main narrative. The text does not critically evaluate the conditions under which AI methods are genuinely superior to MD. For example, the discussion of Phanto-IDP (Section 7) highlights its successes but only briefly mentions that MD outperformed it for some systems (J-coupling values). This nuance is not reflected in the overall conclusion. The review would be more persuasive if it presented a more balanced and critical comparison, discussing the specific strengths and weaknesses of each approach in different contexts (e.g., system size, available data, property of interest).
        - **Why it matters** A review that is perceived as biased or lacking critical analysis will have less impact and credibility. The field is still nascent, and a balanced assessment is crucial for guiding future research and helping users choose the right tool for their specific problem. Overstating the capabilities of AI methods could lead to their misuse and disillusionment.
        - **Resolution test** The authors should revise the discussion to explicitly compare the performance of AI and MD across different scenarios, highlighting where each method excels and fails. The conclusion should be tempered to state that AI methods are a powerful and rapidly improving complement to MD, with the potential to outperform it in specific tasks, rather than a general replacement.
    - **R1-M2**
        - **Severity** Major
        - **Blocking** No
        - **Axis** Technical depth and critical evaluation
        - **Claim pointer** The manuscript claims that AI methods can "circumvent the kinetic barriers that constrain MD simulations" (Section 4.1) and that models like IDPFold "capture a broader Boltzmann-distributed ensemble" (Section 7).
        - **Evidence pointer** Sections 4.1, 4.4, and 7
        - **Concern** The manuscript describes the mechanisms of various AI models but does not provide a deep or critical evaluation of their underlying assumptions and limitations. For instance, the claim that generative models can circumvent kinetic barriers is presented as a fact, but the text does not discuss the physical basis for this or the potential for these models to generate physically unrealistic states. The discussion of "Boltzmann-distributed" ensembles is used loosely without a clear explanation of how this is assessed or what it means in the context of a generative model trained on a potentially biased dataset. A more rigorous review would critically examine the physical validity of AI-generated ensembles and the metrics used to assess their quality.
        - **Why it matters** The scientific value of a review depends on its ability to critically synthesize and evaluate the primary literature. Simply describing methods without a deep analysis of their strengths, weaknesses, and underlying assumptions provides limited insight for the expert reader and could be misleading for the non-expert.
        - **Resolution test** The authors should add a more critical discussion of the physical and statistical foundations of the AI methods. For example, they could discuss the concept of "Boltzmann generators" more rigorously, the challenges of validating AI-generated ensembles against experimental data, and the potential for AI models to suffer from mode collapse or generate non-physical conformations.
    - **R1-M3**
        - **Severity** Major
        - **Blocking** No
        - **Axis** Readability and clarity for a general audience
        - **Claim pointer** The manuscript aims to summarize recent advancements for a broad audience, as implied by the introductory sections and the journal's scope.
        - **Evidence pointer** Sections 3, 4, and 7
        - **Concern** The manuscript assumes a high level of prior knowledge in both machine learning and molecular dynamics. Terms like "variational autoencoders," "diffusion probabilistic models," "Boltzmann generators," and "metainference" are introduced without sufficient explanation for a non-specialist. The descriptions of model architectures are often dense and technical. While some background is provided, the text would benefit from clearer, more intuitive explanations of the core concepts, perhaps with the use of simple analogies or a dedicated "key concepts" box. This would make the review more accessible to a wider audience, including experimentalists and students.
        - **Why it matters** A key goal of a review in a broad journal is to inform and educate a wide readership. If the technical details are impenetrable to a significant portion of the target audience, the review's impact will be limited. The current text risks being accessible only to a narrow group of specialists.
        - **Resolution test** The authors should revise the manuscript to include more accessible explanations of the key AI and MD concepts. This could involve adding a glossary, simplifying the language in the methods descriptions, and providing more intuitive explanations of how the models work and why they are advantageous.
- **Minor Comments**
    - **R1-m1**
        - **Severity** Minor
        - **Axis** Clarity and precision
        - **Affected element** Section 2, paragraph 2
        - **Evidence pointer** Section 2, paragraph 2
        - **Issue** The sentence "Also, MD simulations struggle to effectively integrate experimental data... to bias the conformational sampling towards experimental profiles" is a strong claim that is not fully elaborated. The text mentions this as a limitation but does not discuss the various methods that have been developed to address this (e.g., metainference, replica-averaged modeling), which are mentioned later in the review.
        - **Required correction** The authors should either provide a brief overview of these existing methods in this section or soften the claim to avoid appearing to ignore a significant body of work.
    - **R1-m2**
        - **Severity** Minor
        - **Axis** Consistency
        - **Affected element** Section 4.3
        - **Evidence pointer** Section 4.3
        - **Issue** The text states "His suggests that AlphaFold2’s architecture inherently encodes information about sequence-driven conformational landscapes, albeit indirectly." The word "His" appears to be a typo and should be "This".
        - **Required correction** Correct the typo.
    - **R1-m3**
        - **Severity** Minor
        - **Axis** Completeness
        - **Affected element** Section 7
        - **Evidence pointer** Section 7, paragraph 2
        - **Issue** The text mentions "Table 1" and "Table 2" and "Supplementary Table S1" as comparative summaries. However, these tables were not provided in the manuscript text. It is impossible to assess their content or whether they adequately support the claims made in the text.
        - **Required correction** The authors should ensure that the tables are complete, self-explanatory, and directly support the key comparisons made in the text. The text should also refer to the tables more explicitly, guiding the reader on what to look for.
    - **R1-m4**
        - **Severity** Minor
        - **Axis** Clarity
        - **Affected element** Section 9, paragraph 3
        - **Evidence pointer** Section 9, paragraph 3
        - **Issue** The sentence "This AI-generated ensemble provided structural models that could not be derived solely from MD, offering novel mechanistic insights into Aβ42 aggregation dynamics" is a strong claim. While the preceding text supports this, it would be strengthened by a more explicit statement of what these novel insights are and why they are mechanistically important.
        - **Required correction** The authors should briefly elaborate on the specific mechanistic insights gained from the AI-generated conformations to make the claim more concrete and impactful.
- **Technical failings that need to be addressed before the case is established**
    - The central comparative claim (AI outperforms MD) is not rigorously established due to a lack of critical analysis and a one-sided presentation of evidence. The manuscript needs a more balanced and nuanced discussion that acknowledges the context-dependency of performance.
    - The technical descriptions of AI models are insufficient for a non-specialist to understand their key innovations and limitations. The manuscript needs to be made more accessible.
    - The manuscript relies heavily on quantitative claims from primary sources that cannot be verified from the provided text. The authors should ensure that the presentation of these metrics is accurate and fairly represents the findings of the original studies.
- **Assessment against Nature-style criteria**
    - **Originality:** The topic is current, but the review's perspective is not particularly novel. It synthesizes existing literature without offering a new conceptual framework or a unique critical viewpoint. The originality is moderate.
    - **Scientific importance:** The topic is of high importance to the structural biology and biophysics communities. The potential of AI to address the challenges of IDP conformational sampling is a significant and timely question. The manuscript addresses a question of clear scientific importance.
    - **Interdisciplinary readership:** The topic is inherently interdisciplinary, bridging computer science, physics, chemistry, and biology. However, the current presentation is likely too technical for a broad interdisciplinary audience. The manuscript's readability for non-specialists is a major weakness.
    - **Technical soundness:** The manuscript is a review and does not present new technical work. Its soundness depends on the accuracy of its representation of the primary literature. While the descriptions appear plausible, the lack of critical evaluation and the one-sided argumentation raise concerns about the overall soundness of its conclusions.
    - **Readability for nonspecialists:** This is a significant weakness. The manuscript is written for experts and would be difficult for a non-specialist to follow. The core concepts and methods are not explained in an accessible way.
- **Recommendation posture** Supportive if technical concerns are resolved. The manuscript addresses an important and timely topic and provides a useful overview of the field. However, it requires major revisions to improve its critical balance, technical depth, and accessibility before it can be considered a high-impact review. The authors must address the major concerns regarding the one-sided argument, the lack of critical evaluation, and the poor readability for a general audience.

## Risk / unsupported claims
- The claim that AI methods "outperform MD" is a broad generalization that is not fully supported by the nuanced evidence presented in the text, which shows context-dependent performance.
- The claim that AI models can "circumvent kinetic barriers" is presented as a fact without a critical discussion of the physical basis for this claim or its potential limitations.
- The claim that AI-generated ensembles are "Boltzmann-distributed" is used loosely and is not rigorously defined or supported.
- The specific quantitative performance metrics (e.g., RMSD values, generation times) cited from primary sources cannot be verified from the provided manuscript text and are presented without critical context.
- The statement that "Most of the models today are capable of accurately sampling only relatively smaller IDP sequences" is presented as a general limitation but is not supported by a systematic analysis of the field.