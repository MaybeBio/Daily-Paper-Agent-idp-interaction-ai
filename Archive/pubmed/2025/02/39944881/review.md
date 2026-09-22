## Review setup
- **Input scope** Full manuscript text (Perspective article, QRB Discovery, DOI 10.1017/qrd.2024.15)
- **Assessment boundary** Scientific content, structure, and claims as presented in the provided text; no external verification of cited literature or data
- **Shared manuscript claim summary** The authors argue that integrative structural modeling is essential for determining structures of large macromolecular assemblies, that recent advances in AI-based prediction and cryo-electron tomography have renewed interest in this field, and that two areas require immediate method development: modeling intrinsically disordered regions and leveraging in situ cryo-ET data. They support this with a review of existing software, recent case studies, and a discussion of open challenges.
- **Visible evidence base** Abstract, Introduction, sections on integrative modeling methods, recent examples (nuclear pore complex, NuRD, desmosomes), IDP modeling, in situ data analysis, Outlook, Tables 1 and 2, Figure 1
- **Missing materials affecting confidence** Figure 1 image not visible; Table 1 and Table 2 content partially embedded in text but formatting unclear; no supplementary materials; no line numbers; no access to cited references for verification

## Reviewer
- **Overall assessment** This is a well-written and timely Perspective that identifies two genuine frontiers in integrative structural modeling: intrinsically disordered regions and in situ cryo-ET data. The authors draw on their own experience with the desmosomal outer plaque and the NuRD complex to ground their arguments. The manuscript is readable and logically organized. However, the Perspective is largely descriptive rather than critical, and the "frontiers" identified are presented as a list of challenges without a clear prioritization or a concrete roadmap for how the field should address them. The treatment of IDP modeling and cryo-ET analysis is competent but does not go substantially beyond what has been stated in other recent reviews. The claim that these two areas are the most pressing is asserted rather than argued against alternative candidates. The manuscript would benefit from a sharper thesis and a more critical comparison of existing methods and their limitations.

- **Who would be interested in the results, and why** Structural biologists, computational biologists, and method developers working on macromolecular complexes, particularly those using cryo-ET or dealing with disordered proteins. The Perspective is also relevant for researchers entering the field who seek an overview of available software and recent case studies. The discussion of AI-based structure prediction and its integration with experimental data will appeal to the broader AlphaFold-adjacent community.

- **Major strengths** 
  1. Clear and accessible writing style, suitable for a broad readership.
  2. Good selection of recent case studies (NPC, NuRD, desmosomes) that illustrate the power and challenges of integrative modeling.
  3. The identification of IDPs and in situ data as key areas is timely and well-justified by the examples.
  4. The Outlook section raises several important open problems beyond the two main foci, showing awareness of the wider landscape.
  5. The inclusion of a software table and a case-study table provides useful reference material.

- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** No
- **Axis** Originality / conceptual advance
- **Claim pointer** The authors state that "two areas warranting immediate method development in the context of integrative modeling" are IDP modeling and in situ data utilization.
- **Evidence pointer** Introduction, final paragraph; also repeated in Outlook
- **Concern** The manuscript identifies two frontiers but does not provide a critical argument for why these two are the most urgent relative to other challenges, such as model validation, sampling efficiency, or handling conformational heterogeneity in ordered complexes. The selection appears to be driven by the authors' own research interests rather than a systematic assessment of the field's needs. The treatment of each area is a summary of known challenges and existing methods, with limited new insight or a concrete research agenda.
- **Why it matters** A Perspective should offer a point of view that helps shape the field. If the prioritization is not argued, the manuscript reads more as a review than a perspective, reducing its impact and distinctiveness.
- **Resolution test** The authors should either (a) provide explicit criteria for why these two areas are the most pressing, with evidence from the literature or their own work, or (b) reframe the manuscript as a review of current challenges without claiming prioritization.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** No
- **Axis** Technical soundness / depth of analysis
- **Claim pointer** The section on IDP modeling discusses representation learning, ensemble generation, and experimental data integration, but does not critically evaluate the performance or limitations of the cited methods.
- **Evidence pointer** Section "Integrative modeling of intrinsically disordered proteins"
- **Concern** The discussion of pLMs for IDPs lists challenges but does not provide a comparative assessment of existing approaches. For example, the claim that "state-of-the-art pLMs do not account for the environmental context and interacting partners" is plausible but is not supported by specific examples or benchmarks. Similarly, the section on ensemble generation mentions MD, coarse-grained models, and generative models, but does not discuss their relative accuracy, computational cost, or applicability to different IDP types. The section on experimental data integration lists methods but does not explain when one approach is preferred over another.
- **Why it matters** For a Perspective aimed at method developers, a more critical and comparative analysis would be more useful than a descriptive list. Without this, the reader cannot assess the state of the art or identify the most promising directions.
- **Resolution test** Add a comparative discussion of at least two methods per topic, with explicit criteria for when each is appropriate, or cite benchmark studies that provide such comparisons.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Interdisciplinary readership / accessibility
- **Claim pointer** The section on cryo-ET analysis introduces concepts such as template matching, DeepFinder, DeePiCt, MemBrain, TomoTwin, MPP, and DISCA, but does not explain the underlying principles or the differences between them in sufficient depth for a non-specialist.
- **Evidence pointer** Section "Integrative structure determination using in situ data"
- **Concern** The manuscript is aimed at a broad readership, but the cryo-ET section assumes familiarity with the methods. For example, the difference between supervised and unsupervised approaches is mentioned but not explained in terms of what data and annotations are required. The concept of "missing wedge" is mentioned but not defined. A reader from a different subfield may struggle to follow the argument.
- **Why it matters** The stated goal of the Perspective is to highlight frontiers for method development. If the readership cannot fully understand the challenges, the message is weakened.
- **Resolution test** Add brief explanations of key concepts (e.g., missing wedge, template matching, supervised vs. unsupervised learning) or provide a glossary. Alternatively, explicitly state the target audience and adjust the level of detail accordingly.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Scientific importance / impact
- **Claim pointer** The Outlook section states that "the grand challenge in the field is to construct spatiotemporal models of entire cells" and that integrative models can contribute via metamodeling.
- **Evidence pointer** Outlook section
- **Concern** This is a bold claim, but it is not developed. The authors do not explain what "spatiotemporal models of entire cells" would look like, what data would be required, or how integrative modeling would concretely contribute. The term "metamodeling" is introduced without definition or examples. This weakens the impact of the final message.
- **Why it matters** The Outlook is the place to inspire the reader and set a research agenda. An underdeveloped grand challenge reduces the manuscript's ability to motivate future work.
- **Resolution test** Expand the Outlook with a concrete example of how integrative modeling could contribute to a cell-scale model, or define metamodeling and give an example from the literature.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Table 1
- **Evidence pointer** Table 1
- **Issue** The table lists software with references and URLs, but the "N/A" entry for ISD's URL is inconsistent with the other entries. Also, the table caption states that each software "combines information from three or more experimental and/or computational sources," but this is not evident from the table itself.
- **Required correction** Either add the URL for ISD or state that it is not available. Clarify the caption or add a column indicating the types of data each software integrates.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Accuracy
- **Affected element** Table 2
- **Evidence pointer** Table 2
- **Issue** The entry "Khanppnavar, B (2024)" is incomplete; the author list appears truncated. Also, the entry for "Baldwin et al. (2024)" lists "Data from cryo-EM and XLMS" but does not mention AlphaFold predictions, which are likely relevant.
- **Required correction** Complete the author list for the Khanppnavar entry. Verify the data types listed for each study and ensure completeness.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Readability
- **Affected element** Figure 1
- **Evidence pointer** Figure 1
- **Issue** The figure is described in the text but the image is not visible in the provided material. The caption mentions "Input low-resolution cryo-EM and cryo-ET maps and intrinsically disordered regions in both complexes are highlighted in yellow," but without seeing the figure, it is difficult to assess its clarity and usefulness.
- **Required correction** Ensure the figure is legible and that the highlighted elements are clearly visible. Consider adding a version with labels for readers unfamiliar with the complexes.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Section "Integrative structure determination using in situ data"
- **Evidence pointer** Section text
- **Issue** The section mentions "recent studies used integrative approaches to combine data from cryo-ET, SPA with cryo-EM, mass spectrometry, and predictions from AlphaFold" for IFT-A/IFT-B and microtubule doublets, but does not provide details on how the integration was performed or what software was used.
- **Required correction** Add a sentence or two describing the integration workflow for these examples, or refer the reader to the original papers for details.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Consistency
- **Affected element** Abstract and Introduction
- **Evidence pointer** Abstract, Introduction
- **Issue** The abstract states that "recent advancements in AI-based structure prediction and cryo electron-microscopy have sparked renewed enthusiasm for integrative modeling," but the Introduction does not explicitly discuss why this enthusiasm is justified or what has changed compared to earlier periods.
- **Required correction** Add a brief historical context in the Introduction to explain what is new about the current situation.

- **Technical failings that need to be addressed before the case is established** 
  None identified that would invalidate the manuscript's core claims. The manuscript is a Perspective, not a primary research article, so the absence of new data is expected. However, the lack of a critical comparison of methods and the underdeveloped prioritization argument weaken the case for the two frontiers being the most important.

- **Assessment against Nature-style criteria** 
  - Originality: Moderate. The manuscript identifies two important areas but does not offer a novel framework or a new synthesis. Similar points have been made in other recent reviews and perspectives.
  - Scientific importance: High. The topics are relevant and timely, and the case studies are well chosen. However, the manuscript does not go beyond what is already known.
  - Interdisciplinary readership: Moderate. The manuscript is accessible to structural biologists and computational scientists, but the cryo-ET section may be challenging for non-specialists.
  - Technical soundness: Adequate. The descriptions of methods are accurate, but the lack of critical evaluation limits the depth.
  - Readability for nonspecialists: Good. The writing is clear, but some concepts (e.g., missing wedge, pLMs) are not explained for a general audience.

- **Recommendation posture** Supportive if the authors address the major concerns, particularly by sharpening the prioritization argument, adding critical comparisons of methods, and improving accessibility of the cryo-ET section. The manuscript is a solid Perspective but currently does not fully distinguish itself from existing reviews.

## Risk / unsupported claims
- The claim that the two identified areas are the most pressing for method development is not supported by a systematic argument or evidence.
- The statement that "state-of-the-art pLMs do not account for the environmental context and interacting partners" is plausible but not supported by specific examples or benchmarks.
- The claim that "integrative models of assemblies can contribute directly to this effort via metamodeling efforts" is not explained or exemplified.
- The assertion that "the grand challenge in the field is to construct spatiotemporal models of entire cells" is presented without justification or a concrete path forward.
- The completeness and accuracy of Table 2 entries cannot be fully verified from the provided text.