## Review setup
- **Input scope** Full manuscript text (abstract, introduction, main body, perspectives, acknowledgments)
- **Assessment boundary** Scientific content, technical soundness, and completeness of the review article as provided; no external literature verification performed
- **Shared manuscript claim summary** The authors review recent (2021 onward) computational methods for modeling biomolecular crowding and condensation in cellular environments, covering physics-based and data-driven approaches across scales from single molecules to whole cells, and summarize mechanistic insights on diffusion, binding, stability, and material properties of condensates
- **Visible evidence base** Full text including sections on cellular/crowded environments, phase separation, mechanistic insights, and perspectives; figures and tables referenced but not provided
- **Missing materials affecting confidence** Figures 1 and 2, Table 1, and all figure/table captions are referenced but not included; reference list not provided; no supplementary information

## Reviewer
- **Overall assessment** This is a well-structured and timely review covering an important and rapidly evolving area at the interface of computational biophysics and cell biology. The authors have organized a large body of recent work into coherent thematic sections, and the writing is generally clear and accessible. The review successfully highlights both established methods and emerging directions, including machine learning approaches. However, the absence of figures and tables in the provided material limits the ability to fully assess the pedagogical value and completeness of the presentation. The review is largely descriptive rather than critical; it would benefit from a more explicit comparative assessment of method strengths, limitations, and validation status. The mechanistic insights section is useful but could be strengthened by more systematic synthesis across studies. Overall, the manuscript is likely to be of interest to practitioners and newcomers in the field, but its impact would be enhanced by more critical evaluation and clearer guidance on method selection.
- **Who would be interested in the results, and why** Computational biophysicists and chemists working on macromolecular crowding, intrinsically disordered proteins, and phase separation; experimental cell biologists seeking to interpret their observations in the context of in silico models; method developers in molecular simulation and machine learning applied to biological systems; researchers in drug design interested in intracellular binding kinetics. The review provides a convenient entry point to a dispersed literature and highlights open challenges that could guide future research.
- **Major strengths** 1) Comprehensive and up-to-date coverage of a fast-moving field, with a clear focus on the 2021 onward period. 2) Logical organization that separates crowding effects from condensation phenomena while also connecting them. 3) Inclusion of both physics-based and data-driven approaches, reflecting the current methodological landscape. 4) Discussion of mechanistic insights, including counterintuitive findings such as increased diffusion in crowded environments, which adds value beyond a mere method catalog. 5) Clear articulation of outstanding challenges and future directions in the perspectives section.
- **Major Concerns** 1) The review is largely descriptive and lacks a critical comparative framework for assessing method performance, accuracy, and applicability. 2) The mechanistic insights section synthesizes findings across studies but does not critically evaluate the robustness or generalizability of these insights. 3) The treatment of machine learning approaches is relatively brief given their growing importance. 4) The absence of figures and tables in the provided material prevents assessment of whether the visual presentation adequately supports the text. 5) The scope boundary between "crowding" and "condensation" is sometimes blurred, and the authors do not always clarify whether effects attributed to crowding are distinct from those arising from specific interactions.
- **Minor Comments** 1) The introduction could benefit from a more explicit statement of the review's selection criteria for included studies. 2) Some technical terms (e.g., "soft interactions," "quinary interactions") are introduced without definitions for nonspecialist readers. 3) The discussion of water models in all-atom simulations is somewhat tangential to the main theme of crowding. 4) The perspectives section raises important questions but could be more specific about which methodological advances are most needed. 5) The acknowledgment of limitations in comparing simulation results across different force fields and models could be more prominent.
- **Technical failings that need to be addressed before the case is established** None identified that would invalidate the review's core content. However, the following should be addressed: 1) Clarify the criteria for study inclusion and the temporal scope. 2) Provide a more critical assessment of method validation against experimental data. 3) Ensure that claims about specific simulation results are accurately attributed to the cited studies (verification of citations needed against the reference list, which was not provided).
- **Assessment against Nature-style criteria** Originality: The review covers a topic of high current interest, but similar reviews exist in the broader literature; its originality lies in the specific focus on recent computational methods and the integration of crowding and condensation. Scientific importance: High, as the field is rapidly advancing and a consolidated overview is valuable. Interdisciplinary readership: The topic bridges biophysics, computational chemistry, cell biology, and increasingly machine learning, making it potentially attractive to a broad audience. Technical soundness: The manuscript is technically sound in its descriptions of methods and findings, though the lack of critical comparison limits its depth. Readability for nonspecialists: The writing is generally clear, but some terms and concepts assume familiarity with molecular simulation and biophysics; a glossary or more careful introduction of key concepts would improve accessibility.
- **Recommendation posture** Supportive if technical concerns are resolved. The review is informative and well-organized, but it would be strengthened by a more critical and comparative treatment of the methods discussed, clearer inclusion criteria, and verification of citation accuracy. The absence of figures and tables in the provided material should be rectified in the final submission.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** No
- **Axis** Critical assessment
- **Claim pointer** The review claims to compile computational methods developed in the past few years for simulating biomolecular crowding and condensation, but it does not provide a critical comparison of method performance, accuracy, or limitations.
- **Evidence pointer** Sections "Cellular and Crowded Environments", "Phase Separation and Biomolecular Condensates", "Mechanistic Insights Obtained from Simulations"; location not provided
- **Concern** The manuscript reads largely as a descriptive catalog of methods and findings. While this is acceptable for a review, the value to the community would be substantially enhanced by a more explicit comparative framework. For example, the authors could discuss the trade-offs between different coarse-grained models (e.g., Martini vs. residue-based models like CALVADOS or COCOMO) in terms of accuracy, computational cost, and transferability. Similarly, the choice between all-atom and coarse-grained approaches for specific questions could be more explicitly addressed. The absence of such critical assessment makes it difficult for readers to select appropriate methods for their own research.
- **Why it matters** A review that merely summarizes without critically evaluating does not provide sufficient guidance to practitioners, particularly those new to the field. The stated goal of encouraging progress toward simulating cellular environments requires an honest assessment of what works, what does not, and where the gaps are.
- **Resolution test** The authors should add a comparative discussion, possibly in the form of a table or dedicated section, that evaluates the strengths and limitations of different methodological approaches, including validation status against experimental data.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** No
- **Axis** Scope and inclusion criteria
- **Claim pointer** The review states it focuses on works published from 2021 onward, but the criteria for study inclusion are not explicitly defined.
- **Evidence pointer** Introduction; location not provided
- **Concern** The temporal scope is stated, but the authors do not specify how studies were selected for inclusion. Was a systematic literature search performed? Were certain types of studies (e.g., those using specific methods or model systems) excluded? The lack of explicit inclusion criteria makes it difficult to assess whether the review is comprehensive or representative of the field.
- **Why it matters** Without clear inclusion criteria, readers cannot judge whether the review provides a balanced and complete picture of recent developments or whether it reflects the authors' particular interests. This is particularly important in a field as broad as computational modeling of cellular environments.
- **Resolution test** The authors should state their literature search strategy and inclusion/exclusion criteria in the introduction or methods section.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Validation and benchmarking
- **Claim pointer** The review presents mechanistic insights from simulations (e.g., effects of crowding on diffusion, binding, stability) but does not systematically discuss how these simulation results compare with experimental data.
- **Evidence point** Section "Mechanistic Insights Obtained from Simulations"; location not provided
- **Concern** The review reports findings from simulations, some of which are described as counterintuitive (e.g., increased diffusion in crowded environments). However, the authors do not consistently address whether these findings have been experimentally validated or whether they remain predictions. A more systematic discussion of the experimental evidence supporting or contradicting simulation results would greatly strengthen the review.
- **Why it matters** The credibility of computational approaches depends on their ability to reproduce and predict experimental observations. Without explicit discussion of validation, readers cannot assess the reliability of the reported insights.
- **Resolution test** The authors should add a subsection or table that summarizes the experimental validation status of key simulation findings.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Machine learning coverage
- **Claim pointer** The review includes a section on data-driven approaches to predict protein phase separation, but this section is relatively brief given the rapid growth and importance of machine learning in this area.
- **Evidence point** Section "Data Driven Approaches to Predict Protein Phase Separation"; location not provided
- **Concern** The machine learning section covers a few specific tools (e.g., DeePhase, PSPredictor) but does not provide a broader overview of the landscape of data-driven methods, including their training data, feature representations, and limitations. Given the stated goal of covering "physics-based and data-driven computational methods," the treatment of the latter feels imbalanced.
- **Why it matters** Machine learning is increasingly central to the field, and a review that aims to be comprehensive should provide a more thorough treatment of these approaches, including their potential and limitations relative to physics-based methods.
- **Resolution test** The authors should expand the machine learning section to include a broader survey of available tools, their underlying methodologies, and a critical assessment of their predictive power and generalizability.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Accessibility
- **Affected element** Introduction
- **Evidence pointer** Introduction; location not provided
- **Issue** Terms such as "soft interactions" and "quinary interactions" are used without definition, which may confuse nonspecialist readers.
- **Required correction** Provide brief definitions or a glossary for these and other specialized terms upon first use.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Section "Cellular and Crowded Environments"
- **Evidence pointer** Section "Cellular and Crowded Environments"; location not provided
- **Issue** The distinction between "crowding" and "condensation" is not always clear, and the authors sometimes discuss them together without clarifying whether the effects are distinct or overlapping.
- **Required correction** Add a brief paragraph or table clarifying the conceptual and mechanistic relationship between crowding and condensation, and how the methods discussed address each.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Section "Mechanistic Insights Obtained from Simulations"
- **Evidence pointer** Section "Mechanistic Insights Obtained from Simulations"; location not provided
- **Issue** The section on mechanistic insights is useful but could benefit from a more systematic synthesis, such as a summary table of key findings across studies.
- **Required correction** Consider adding a table that summarizes the main mechanistic insights, the methods used, and the systems studied.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Future directions
- **Affected element** Section "Perspectives and Conclusion"
- **Evidence pointer** Section "Perspectives and Conclusion"; location not provided
- **Issue** The perspectives section raises important challenges but could be more specific about which methodological advances are most needed and how they might be achieved.
- **Required correction** Expand the perspectives section with more concrete suggestions for future research directions, such as improved force fields, enhanced sampling techniques, or integration of experimental data.

## Risk / unsupported claims
- The claim that "the first minimal synthetic bacterial cell, JCVI-syn3.0, a derivation from Mycoplasma, is also being used for 3D cell modeling studies" is presented without specific citation details; verification against the reference list is needed.
- The statement that "the rise of machine learning models offers tremendous potential for predicting the components of biomolecular condensates in cells and uncovering previously unknown components" is forward-looking and not supported by specific examples in the review; it should be framed as a perspective rather than an established finding.
- The claim that "the effects of macromolecular crowding and cellular environments over protein-target binding, diffusion rates of macromolecules and small drug-like molecules, and protein stability" are well-understood from simulations is not uniformly supported by the evidence presented; some findings are from single studies and may not be generalizable.
- The assertion that "experimental methods such as FRAP, to measure diffusion rates, and NMR, to detect protein conformational changes, can be used to investigate proteins inside cells, providing useful benchmarks" is reasonable but not elaborated; the authors should specify which types of experimental data are most suitable for benchmarking which simulation approaches.