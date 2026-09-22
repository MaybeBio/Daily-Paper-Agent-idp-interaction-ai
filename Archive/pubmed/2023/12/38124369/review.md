## Review setup
- **Input scope** Abstract only
- **Assessment boundary** Claims and conclusions as presented in the abstract; no access to full text, figures, tables, or supplementary materials
- **Shared manuscript claim summary** The authors present a Perspective on the use of AlphaFold2 and RoseTTaFold in protein structure prediction, discussing their integration into experimental pipelines, performance across protein classes (membrane proteins, intrinsically disordered proteins, oligomers), complementarity with molecular dynamics simulations, and a proposed "wish list" for future model improvements.
- **Visible evidence base** Abstract text only; no experimental data, case studies, or methodological details are available for verification
- **Missing materials affecting confidence** Full manuscript, all figures and tables, specific case study descriptions, methodological details for the proposed meta-tool, and any quantitative performance comparisons

## Reviewer
- **Overall assessment** This Perspective addresses a timely and important topic in structural biology, summarizing the current state and limitations of deep-learning-based protein structure prediction tools. The abstract provides a coherent overview of key application areas and challenges. However, the claims are presented at a high level without quantitative support or detailed evidence, which is typical for a Perspective but limits the ability to critically evaluate the scientific rigor of the arguments. The proposed "wish list" is forward-looking but lacks specificity regarding implementation or feasibility. The manuscript would benefit from clearer articulation of novel insights beyond existing literature and more concrete examples to substantiate the claims.
- **Who would be interested in the results, and why** Structural biologists, computational biologists, and researchers in protein science would find this Perspective useful as a concise summary of current capabilities and limitations of AF2 and RF. Those integrating prediction tools into experimental workflows, particularly in X-ray crystallography, NMR, and mass spectrometry, would benefit from the discussion of complementarity. Researchers working on membrane proteins, IDPs, or oligomers would gain context on specific challenges in these areas. The "wish list" may interest developers of deep-learning models in structural bioinformatics.
- **Major strengths** The abstract addresses a highly relevant and rapidly evolving topic. It covers multiple protein classes and experimental integration scenarios, providing a broad perspective. The emphasis on complementarity with molecular dynamics simulations and experimental data is practical and useful. The forward-looking "wish list" frames future directions constructively.
- **Major Concerns** The abstract lacks specific evidence or examples to support claims about performance across protein classes. The discussion of limitations for membrane proteins and IDPs is qualitative without quantitative context. The proposed "wish list" items are not detailed enough to assess feasibility or novelty. The abstract does not clearly distinguish this Perspective from prior reviews on similar topics.
- **Minor Comments** The abstract could benefit from a clearer statement of the intended audience and scope. The term "wish list" is informal for a scientific journal; a more precise term such as "recommendations" or "priorities" may be appropriate. The abstract does not mention any limitations of the Perspective itself, such as potential biases in selected examples.
- **Technical failings that need to be addressed before the case is established** None identified from the supplied material, as the abstract does not present quantitative technical claims that can be verified or falsified.
- **Assessment against Nature-style criteria** Originality: The topic is current but the abstract does not clearly demonstrate novel insights beyond existing literature. Scientific importance: High, given the transformative impact of AF2 and RF on structural biology. Interdisciplinary readership: Moderate, as the content is primarily relevant to structural biology and computational chemistry. Technical soundness: Cannot be fully assessed from the abstract; claims are qualitative and lack supporting data. Readability for nonspecialists: The abstract is accessible but assumes familiarity with protein structure prediction concepts.
- **Recommendation posture** Supportive if technical concerns are resolved, provided the full manuscript offers concrete examples, quantitative context, and a clearer articulation of novel contributions relative to existing Perspectives.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** No
- **Axis** Evidence sufficiency
- **Claim pointer** The abstract claims that AF2 and RF show "promising results for oligomeric models, outperforming traditional docking methods" and that "AlphaFold-Multimer shows improved performance."
- **Evidence pointer** Abstract only; location not provided
- **Concern** The claim of outperforming traditional docking methods is presented without specific benchmarks, datasets, or comparison metrics. The abstract does not indicate which docking methods were compared, under what conditions, or with what performance measures.
- **Why it matters** Without quantitative context, readers cannot assess the magnitude or generalizability of the claimed advantage. This is a central claim for the utility of these tools in oligomer prediction.
- **Resolution test** The full manuscript should provide specific performance comparisons, including datasets used, metrics (e.g., DockQ, TM-score), and statistical significance, to substantiate this claim.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** No
- **Axis** Evidence sufficiency
- **Claim pointer** The abstract states that "AF2's confidence score (pLDDT) serves as a competitive disorder predictor" for intrinsically disordered proteins.
- **Evidence pointer** Abstract only; location not provided
- **Concern** The term "competitive" implies a comparison against established disorder predictors, but no benchmarks or comparative data are mentioned. The abstract does not specify which predictors were compared or the evaluation criteria.
- **Why it matters** This claim positions pLDDT as a useful tool for disorder prediction, which has practical implications. Without comparative evidence, the claim is unsubstantiated.
- **Resolution test** The full manuscript should include a comparison of pLDDT against established disorder predictors (e.g., IUPred, DisoPred) using standard benchmarks such as the DisProt database, with appropriate metrics.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Novelty and contribution
- **Claim pointer** The abstract proposes a "wish list" for improving deep-learning-based protein folding prediction models, including using experimental data as constraints and modifying models with binding partners or post-translational modifications, and suggests a meta-tool for ranking and suggesting composite models.
- **Evidence pointer** Abstract only; location not provided
- **Concern** The proposed items are presented at a conceptual level without details on how they would be implemented, what challenges exist, or how they differ from ongoing efforts in the field. The meta-tool suggestion lacks specification of inputs, outputs, or evaluation criteria.
- **Why it matters** For a Perspective, the value lies in offering actionable and novel directions. Without specificity, the "wish list" reads as generic and may not provide new guidance to the community.
- **Resolution test** The full manuscript should elaborate on each wish list item with concrete implementation strategies, potential pitfalls, and how they build on or diverge from existing approaches. The meta-tool should be described with a clear framework for ranking and integration.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity and precision
- **Affected element** Abstract wording
- **Evidence pointer** Abstract, first sentence
- **Issue** The phrase "revolutionized structural biology" is a strong claim that, while likely true, is presented without qualification or citation context in the abstract.
- **Required correction** Consider softening to "have had a major impact on structural biology" or provide a brief qualifier to avoid overstatement.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Scope definition
- **Affected element** Abstract scope
- **Evidence pointer** Abstract, overall
- **Issue** The abstract does not explicitly state the scope of the Perspective, such as the time frame of literature covered or the criteria for selecting the discussed examples.
- **Required correction** Add a sentence clarifying the scope, such as "This Perspective focuses on developments up to [year] and highlights representative examples from recent literature."

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Terminology
- **Affected element** "wish list"
- **Evidence pointer** Abstract, final paragraph
- **Issue** The term "wish list" is informal and may not align with the tone expected in a scientific journal.
- **Required correction** Replace with a more formal term such as "recommendations" or "priorities for future development."

## Risk / unsupported claims
- The claim that AF2 and RF "outperform traditional docking methods" for oligomers is unsupported in the abstract without specific benchmarks.
- The claim that pLDDT is a "competitive disorder predictor" is unsupported without comparative data.
- The general statement that AF2 models "help X-ray crystallography in resolving the phase problem" is presented without specific examples or success rates.
- The assertion that "integrative approaches including molecular dynamics simulations or hydrophobic cluster analyses are advocated" for IDPs is presented as a recommendation without evidence of efficacy.
- The feasibility and novelty of the proposed meta-tool cannot be assessed from the abstract.