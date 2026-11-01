## Review setup
- **Input scope** Full manuscript text (abstract, main text, references cited within text)
- **Assessment boundary** Scientific content, technical accuracy, structural coherence, and evidentiary support of the review's central thesis; no assessment of formatting or journal fit beyond general scope
- **Shared manuscript claim summary** The manuscript argues that the convergence of structural computation, machine learning, and generative AI has made historically "undruggable" oncology targets (KRAS, p53, MYC, SHP2) systematically approachable, while acknowledging that clinical translation remains limited by biological factors.
- **Visible evidence base** Full text of the manuscript, including abstract, introduction, methods (literature search strategy), mathematical foundations, target-specific analyses, modality discussions, translational assessment, and conclusions; no figures or tables were provided
- **Missing materials affecting confidence** Figures (including Figure 1, the integrated pipeline diagram), all tables (Tables 1–6), and the complete reference list; these are referenced extensively in the text and are essential for verifying specific claims about target selection, computational methods, and clinical outcomes

## Reviewer
- **Overall assessment** This is a well-structured, ambitious narrative review that attempts to synthesize a complex, rapidly evolving interdisciplinary field. The manuscript's central thesis—that druggability is a function of method, not a fixed property of a target—is compelling and well-argued. The authors demonstrate strong command of both the computational and biological literatures, and the explicit separation of "what has been achieved" from "what is promised" is commendable. However, the manuscript suffers from several significant issues that must be addressed before it can be considered for publication. The mathematical sections, while thorough, are not well-integrated with the biological narrative and may alienate the target readership. The treatment of clinical evidence is uneven, with some claims exceeding what the cited evidence supports. Most critically, the absence of the figures and tables in the provided material makes it impossible to fully evaluate the manuscript's coherence and evidentiary support. The authors' candor about the field's limitations is a genuine strength, but the review would benefit from a more critical examination of the methodological gaps between computational prediction and clinical reality.

- **Who would be interested in the results, and why** Computational chemists and AI researchers working on drug discovery would find the mathematical foundations and the assessment of generative methods valuable. Medicinal chemists and chemical biologists targeting traditionally difficult proteins would benefit from the structured analysis of how different modalities (covalent, allosteric, glue, degrader) map onto specific biophysical obstacles. Oncology researchers and clinicians would be interested in the translational assessment and the candid discussion of clinical attrition. The review could serve as a useful teaching resource for graduate students entering this interdisciplinary space, provided the mathematical sections are made more accessible.

- **Major strengths**
  1. The central thesis is clearly articulated and consistently developed throughout: druggability is a function of the methods brought to bear, not a fixed property of the target.
  2. The explicit three-category framework (classical structural/computational work vs. demonstrated ML contributions vs. prospective generative AI) is a valuable analytical tool that brings clarity to a literature that often conflates these categories.
  3. The selection of targets (KRAS, p53, MYC, SHP2) is well-justified by the stated criteria of mechanistic non-redundancy and evidentiary depth, and the treatment of each target is thorough.
  4. The manuscript is admirably candid about the field's limitations, including the lack of prospective generative design success against undruggable oncology targets, the physical-validity gaps in deep learning methods, and the clinical attrition problem.
  5. The discussion of molecular glues (Section 6.3) is particularly strong, with a clear articulation of the six distinct obstacles to rational glue design and the computational responses to each.
  6. The treatment of resistance (Section 7.3) is sophisticated, correctly identifying it as a biological problem that computational design alone cannot solve.

- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness and integration
- **Claim pointer** The manuscript claims that the mathematical foundations in Section 2 are necessary for assessing the capabilities and limitations of generative models, and that the formalism is "a means rather than the point."
- **Evidence pointer** Section 2, Sections 2.1–2.4; location not provided
- **Concern** The mathematical sections are presented in a way that is disconnected from the biological and chemical narrative. The derivations of equivariant graph neural networks, diffusion models, and flow networks are technically correct but are not used to derive any specific insight about the undruggable targets discussed later. For example, the discussion of EGNNs (Section 2.2) does not explain how equivariance specifically enables or constrains the design of ligands for the switch-II pocket or the Y220C crevice. The authors state that the formalism is a means, but it functions more as an appendix that interrupts the flow of the argument. A reader coming from medicinal chemistry (an explicitly anticipated audience) would struggle to see why the mathematical detail is necessary for the review's conclusions.
- **Why it matters** The review's stated purpose is integrative, but the mathematical sections are not integrated. If the mathematics is not used to generate specific insights about the targets, it should be substantially condensed or moved to an appendix. As written, it risks losing the target readership without adding analytical power.
- **Resolution test** The authors should either (a) demonstrate how specific mathematical properties (e.g., equivariance, score-based sampling) directly inform the design strategies or limitations discussed in Section 5, or (b) condense Section 2 to a summary of capabilities and limitations, with full derivations in an appendix.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidentiary support for clinical claims
- **Claim pointer** The manuscript states that vepdegestrant was "licenced by the FDA in May 2026" and that daraxonrasib "met its dual primary endpoint" in a randomized phase 3 trial, with a median overall survival of 13.2 vs 6.6 months and a hazard ratio of 0.40.
- **Evidence pointer** Section 1.2, Section 5.1.4, Section 7.1; location not provided
- **Concern** These are specific, quantitative clinical claims that are presented without any citation to primary sources or trial registries. The manuscript's literature search is stated to have been updated through May 2026, with clinical status refreshed through August 2026, but no references are provided in the text for these claims. Given that the manuscript itself emphasizes the importance of distinguishing "demonstrations of principle from clinical outcomes," it is inconsistent to present these specific clinical results without verifiable citations. The claim about daraxonrasib's hazard ratio is particularly consequential and must be traceable to a primary source.
- **Why it matters** The review's credibility depends on the accuracy of its clinical claims. Uncited quantitative results, especially for recently approved drugs or recent trial readouts, cannot be verified by the reader. This is a fundamental evidentiary failure for a review that positions itself as candid about the field's realities.
- **Resolution test** Provide full citations to the primary clinical trial publications, regulatory announcements, or trial registries for all specific clinical claims, including vepdegestrant's approval and daraxonrasib's phase 3 results.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Reproducibility and transparency of literature search
- **Claim pointer** The manuscript states that a structured literature search was conducted across specified databases with defined inclusion criteria, and that the search was "last updated in May 2026" with clinical status "refreshed through 31 August 2026."
- **Evidence pointer** Section 1.4, Table 2; location not provided
- **Concern** The text describes the search strategy in general terms but does not provide the actual search strings, the number of records retrieved, the screening process, or the number of records included. The authors explicitly acknowledge that "a fully reproducible electronic search would require database-specific strings, exact search dates, retrieval counts and a description of deduplication, none of which we recorded prospectively." This is a significant transparency gap for a review that makes claims about the state of a field. The absence of this information makes it impossible to assess whether the review's selection of literature is biased or incomplete.
- **Why it matters** The review's conclusions about what has been "proven" versus "promised" depend on the completeness and impartiality of the literature search. Without reproducible search details, the reader cannot distinguish a comprehensive synthesis from a selective narrative.
- **Resolution test** Provide the full search strings for each database, the date of each search, the number of records retrieved and screened, and the number of records included in the final synthesis. If this is not possible retrospectively, the authors should state this limitation explicitly and temper their claims accordingly.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Balance and critical assessment
- **Claim pointer** The manuscript argues that the convergence of structural computation, ML, and generative AI has made the undruggable "systematically approachable," while acknowledging that "the prospective generative design of a small molecule against a genuinely novel undruggable oncology target, carried through to the clinic, has not yet been demonstrated."
- **Evidence pointer** Section 1.2, Section 9, Section 10; location not provided
- **Concern** There is a tension between the review's framing ("the verdict has been overturned," "the category has contracted") and its own admission that no generative AI-designed drug has succeeded against an undruggable oncology target. The review does not engage critically with the possibility that the "undruggable" label may reflect not just technical limitations but fundamental biological constraints (e.g., the lack of a suitable binding site, the difficulty of achieving sustained target engagement in vivo). The discussion of resistance (Section 7.3) touches on this but does not fully explore the implication that computational advances may have reached the limit of what they can contribute to certain targets.
- **Why it matters** A review that aims to be candid about the field's limits should more directly confront the possibility that some targets may remain undruggable regardless of computational advances. The current framing risks overstating the degree to which the problem has been "changed in kind."
- **Resolution test** Add a section or subsection that explicitly addresses the biological and physicochemical limits of druggability that computational methods cannot overcome, and discuss whether any of the four targets may remain intractable despite the advances described.

- **Concern ID** R1-M5
- **Severity** Major
- **Blocking** No
- **Axis** Interdisciplinary accessibility
- **Claim pointer** The manuscript states that a reader coming from medicinal chemistry or cancer biology "should not have to absorb equivariance and stochastic differential equations before learning why either matters."
- **Evidence pointer** Section 2, Section 2.1–2.4; location not provided
- **Concern** Despite this stated intention, the mathematical sections are dense and assume significant prior familiarity with the material. The notation is introduced rapidly, and the connections to practical drug design are not made explicit. For example, the discussion of the probability-flow ODE (Section 2.3) is unlikely to be meaningful to a medicinal chemist, and the text does not explain why this mathematical object matters for drug design. The authors' promise that the formalism is "a means rather than the point" is not fulfilled.
- **Why it matters** The review explicitly targets an interdisciplinary audience. If the mathematical sections are not accessible to that audience, they will be skipped, and the review's argument will be weakened. The authors should either rewrite these sections for a non-specialist audience or move the full derivations to an appendix and provide a plain-language summary in the main text.
- **Resolution test** Have a reader with a medicinal chemistry background (but no ML specialization) read Section 2 and report whether they can articulate why each method matters for drug design. Revise accordingly.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity of terminology
- **Affected element** Section 1.1, Section 5.1.2
- **Evidence pointer** Location not provided
- **Issue** The term "undruggable" is used throughout without a precise operational definition. The authors distinguish "druggable" from "undruggable" targets but do not specify the criteria (e.g., presence of a binding pocket, ligand efficiency, clinical validation). This is particularly important because the review argues that druggability is method-dependent.
- **Required correction** Provide an explicit definition of "undruggable" as used in this review, and note that the term is historically contingent.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Consistency of claims
- **Affected element** Section 1.2 vs. Section 9
- **Evidence pointer** Location not provided
- **Issue** The introduction states that "the last decade has overturned that verdict," while the discussion section states that "the prospective generative design of a small molecule against a genuinely novel undruggable oncology target, carried through to the clinic, has not yet been demonstrated." These statements are not contradictory, but the introduction's framing is more triumphalist than the discussion's, and the reader is not prepared for the more cautious tone later.
- **Required correction** Adjust the introduction's framing to be more consistent with the review's overall assessment, or add a forward reference to the discussion's more nuanced conclusion.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Completeness of target selection
- **Affected element** Section 1.5
- **Evidence pointer** Location not provided
- **Issue** The four targets are justified by mechanistic non-redundancy, but the review does not discuss whether other "undruggable" targets (e.g., KRAS G12V, NRAS, transcription factors beyond MYC) would have led to different conclusions. The selection criteria are stated, but the sensitivity of the review's conclusions to this selection is not addressed.
- **Required correction** Add a brief discussion of how the conclusions might differ if other targets had been selected, or state explicitly that the four targets are representative of the broader class.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Figure and table integration
- **Affected element** Figure 1, Tables 1–6
- **Evidence pointer** Referenced in text; not provided
- **Issue** The text references Figure 1 and Tables 1–6 extensively, but these are not provided in the manuscript. It is impossible to assess whether the figure and tables accurately represent the claims made in the text.
- **Required correction** Ensure that all figures and tables are included in the manuscript and that they are consistent with the text.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Citation practice
- **Affected element** Section 7.1, Section 7.2
- **Evidence pointer** Location not provided
- **Issue** The manuscript cites "a systematic assessment" and "an evaluation" without providing specific references in the text. While the reference list is not provided, the text should include citation markers at the point of claim.
- **Required correction** Add citation markers for all claims that reference specific studies, including the systematic assessment of co-folding accuracy and the evaluation of PROTAC ternary complexes.

- **Concern ID** R1-m6
- **Severity** Minor
- **Axis** Scope of literature coverage
- **Affected element** Section 7.2
- **Evidence pointer** Location not provided
- **Issue** The discussion of clinical attrition rates for AI-discovered drugs relies on a single analysis. Given the review's emphasis on candor, it would be strengthened by acknowledging the limitations of this single source and, if possible, citing additional or contrasting analyses.
- **Required correction** Acknowledge the limitations of the cited analysis and, if available, cite additional studies that corroborate or challenge its findings.

## Risk / unsupported claims
- The specific clinical claims about vepdegestrant's FDA approval (May 2026) and daraxonrasib's phase 3 results (median OS 13.2 vs 6.6 months, HR 0.40) are presented without citations and cannot be verified from the provided material.
- The claim that "more than half of proteins lacking an obvious ground-state pocket may nonetheless harbour a cryptic one" is attributed to PocketMiner's analysis but the specific statistic is not verifiable without the reference.
- The claim that "the first targeted protein degrader to show a phase 3 benefit has since become an approved medicine" is presented as fact but the specific drug and trial are not identified in the text.
- The statement that "the best of them recovered only about a third of the glue–protein interactions and roughly half of the protein–protein interfaces" for co-folding models is presented without a specific citation.
- The claim that "a parallel assessment on PROTAC ternary complexes reported that apparent accuracy is substantially inflated by accessory subunits" is presented without a specific citation.
- The overall assessment that generative AI has made the undruggable "systematically approachable" is an interpretive claim that goes beyond the evidence presented, which shows no generative AI-designed drug has succeeded against an undruggable oncology target.