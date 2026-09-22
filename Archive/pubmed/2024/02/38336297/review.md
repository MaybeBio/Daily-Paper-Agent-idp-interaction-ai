## Review setup
- **Input scope** Full manuscript text (review article) provided in the form of a complete draft, including abstract, main text sections, figure legends, and references cited inline.
- **Assessment boundary** Scientific content, conceptual framework, evidence synthesis, and presentation quality of the review. Not assessed: editorial fit for the specific journal, formatting, or reference list completeness beyond what is visible.
- **Shared manuscript claim summary** The authors propose a framework categorizing amino acid substitution outcomes into "toggle," "rheostat," and "neutral" positions. They argue that rheostat positions, where substitutions sample at least half of the functional range, are widespread, biologically important, underpredicted by current algorithms, and mechanistically linked to protein dynamics rather than static structure.
- **Visible evidence base** The manuscript cites primary experimental studies from the authors' own laboratories (LacI/GalR family, pyruvate kinase, NTCP, aldolase, CIITA) and reanalyses of published deep mutational scanning datasets (GB1, TIM barrel, ACE2). Figures 1-9 present schematics, prevalence data, evolutionary analyses, and structural/dynamic correlations.
- **Missing materials affecting confidence** Full reference list with complete citations is not provided. Figure 2 legend is partially truncated. Some primary data underlying prevalence estimates (e.g., exact thresholds for ACE2 classification) are not fully described in the text. The manuscript does not include a formal methods section for the reanalyses described.

## Reviewer

### Overall assessment
This is a timely and thought-provoking review that consolidates a decade of work on a genuinely underappreciated class of amino acid positions. The central thesis, that substitution outcomes fall along a continuum from neutral to toggle with rheostat positions in between, is well-supported by the authors' own extensive experimental work and by reanalysis of published datasets. The manuscript is clearly written, logically organized, and will be of interest to a broad audience in protein science, evolutionary biology, and biomedical research. The conceptual framework proposed has the potential to reframe how the field thinks about sequence-function relationships and to improve prediction algorithms. However, several concerns need to be addressed to strengthen the case, particularly regarding the generalizability of the framework, the mechanistic claims about dynamics, and the practical utility of the classification scheme.

### Who would be interested in the results, and why
Protein engineers and computational biologists developing substitution prediction algorithms will find the framework directly relevant to improving their methods. Experimental biochemists and structural biologists studying allostery and protein dynamics will be interested in the mechanistic hypotheses. Evolutionary biologists studying sequence conservation and functional divergence will benefit from the nuanced view of nonconserved positions. Clinically oriented researchers interpreting missense variants in disease contexts will find the discussion of intermediate functional outcomes and their biological consequences important. The review is written at a level accessible to graduate students and researchers entering the field.

### Major Strengths
1. The manuscript fills a genuine gap in the literature by systematically defining and characterizing rheostat positions, which have been largely overlooked due to historical bias toward conserved positions.
2. The authors bring together an impressive body of evidence from diverse protein types (soluble globular, membrane, intrinsically disordered) to support the generality of their claims.
3. The quantitative framework (RheoScale) provides an objective, reproducible method for classifying positions, which is a significant methodological contribution.
4. The discussion of limitations of current prediction algorithms and the specific assumptions that fail for rheostat positions is insightful and actionable.
5. The figures are well-designed and effectively illustrate the key concepts, particularly the schematic in Figure 1 and the prevalence data in Figure 3.
6. The authors are appropriately cautious in acknowledging gaps in knowledge, such as the lack of rheostat positions in some proteins and the unknown effects on stability.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Generalizability of the framework
- **Claim pointer** The manuscript claims that rheostat positions are "widespread" and can be "prevalent within individual proteins" (up to 40% in LacI, >30% in hLPYK), and that they have been observed in "globular soluble, integral membrane, and intrinsically disordered proteins."
- **Evidence pointer** Section "Rheostat positions are present in many protein types"; Table 1; Figure 3
- **Concern** The evidence for prevalence comes from a small number of proteins, many studied by the authors' own laboratories. The claim of "widespread" occurrence is based on: (1) LacI and engineered LacI/GalR paralogs (same protein family), (2) hLPYK and ZmPYK (same enzyme class), (3) NTCP (4 positions), (4) CIITA (7 positions), and (5) retrospective analysis of ACE2. While the diversity of protein types is commendable, the total number of independent protein systems is limited. The authors acknowledge that some proteins (ZmPYK, PafA) show few or no rheostat positions, which raises questions about what fraction of proteins might harbor them. The 40% prevalence in LacI is based on low-resolution in vivo assays, which the authors themselves note may overestimate rheostat positions. The manuscript would be strengthened by a more systematic survey of available deep mutational scanning datasets to estimate the frequency of rheostat positions across a larger, more diverse set of proteins.
- **Why it matters** The central claim of the review is that rheostat positions are a general phenomenon important for understanding protein function. If they are rare or confined to certain protein classes, the framework's utility for improving prediction algorithms would be substantially diminished. The current evidence, while suggestive, does not yet establish the claimed generality.
- **Resolution test** The authors should either (a) conduct a systematic reanalysis of publicly available deep mutational scanning datasets (e.g., from MaveDB) to estimate the prevalence of rheostat positions across a diverse set of proteins, or (b) temper the claims of "widespread" and "prevalent" to reflect the current evidence base, explicitly stating the number of independent protein systems examined and the potential for selection bias in the proteins studied to date.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Mechanistic claim regarding protein dynamics
- **Claim pointer** The manuscript states that "measured functional changes show promising correlations with predicted changes in protein dynamics" and that "the emergent properties of predicted, dynamically coupled amino acid networks might explain some of the complex functional outcomes observed when substituting rheostat positions."
- **Evidence pointer** Section "Substitutions at functional rheostat positions might cause functionally important changes in dynamics"; Figure 7
- **Concern** The evidence for the dynamics mechanism is based on a single study of one LacI position using anisotropic network models. The correlation between predicted dynamic changes and measured functional changes is described as "promising" but the manuscript does not provide quantitative details (e.g., correlation coefficients, number of variants tested, statistical significance). The claim that dynamically coupled networks "might explain" complex outcomes is highly speculative and presented without sufficient caveats. The authors do not discuss alternative mechanisms (e.g., changes in electrostatic interactions, hydrophobic packing, or hydrogen bonding patterns) that could equally explain long-range effects. The distinction between "dynamics" as a causal mechanism versus a correlated readout of structural changes is not adequately addressed.
- **Why it matters** The dynamics hypothesis is presented as a potential unifying mechanism for rheostat positions and is used to justify future research directions. If this claim is overstated, it could mislead the field toward a narrow mechanistic focus. The review would be more balanced and scientifically rigorous if the speculative nature of the dynamics mechanism were more explicitly acknowledged and alternative hypotheses discussed.
- **Resolution test** The authors should either (a) provide quantitative evidence from the LacI study (correlation coefficients, significance levels) and discuss any validation in other systems, or (b) reframe the dynamics discussion as one of several possible mechanisms, explicitly stating that direct experimental evidence for dynamics changes is currently limited to computational predictions and indirect inferences.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Practical utility of the framework for prediction
- **Claim pointer** The manuscript states that "separate algorithms correctly predict toggle positions but not rheostat positions" and implies that the framework provides a path toward improving predictions.
- **Evidence pointer** Section "Historical limitations of prediction algorithms and the existence of rheostat positions were identified by a 'semiSM' experimental design"; reference to (1)
- **Concern** The manuscript does not provide a clear, actionable path for how the rheostat framework could be incorporated into existing prediction algorithms. The authors note that current algorithms fail for rheostat positions but do not specify what new features or approaches might improve predictions. The discussion of evolutionary signatures (ConSurf, least-patterned scores) shows that these features can partially discriminate position classes, but the overlap is substantial (AUC ~0.84-0.87), and the manuscript does not address whether this level of discrimination would be practically useful. The review would benefit from a more concrete discussion of how the framework could be operationalized, e.g., by identifying features that distinguish rheostat from toggle and neutral positions that could be incorporated into machine learning models.
- **Why it matters** A key motivation for studying rheostat positions is to improve prediction of substitution outcomes. Without a clear path to implementation, the framework risks being seen as descriptive rather than actionable, limiting its impact on the field.
- **Resolution test** The authors should add a section or paragraph discussing specific strategies for incorporating rheostat position identification into prediction algorithms, such as combining evolutionary features with structural or dynamic predictions, or using Rheostat scores as training labels for machine learning approaches.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Definition and boundary of "neutral" positions
- **Claim pointer** The manuscript defines neutral positions as those where "all substitutions exhibit wild-type function" and distinguishes them from rheostat positions.
- **Evidence pointer** Section "Rheostat, toggle, and neutral positions can be objectively assigned"; Figure 2
- **Concern** The definition of neutral positions as "all substitutions exhibit wild-type function" is problematic. In practice, most positions will have at least some substitutions that affect function, and the classification depends heavily on the sensitivity and dynamic range of the functional assay used. The manuscript acknowledges this issue in the context of Rheostat scores but does not fully address the implications. A position classified as neutral in one assay might be rheostat in a more sensitive assay or for a different functional parameter. The authors note that "a truly neutral position must be neutral for all parameters that can be measured," but this is an extremely stringent criterion that may rarely be met in practice. The manuscript would benefit from a more nuanced discussion of how assay sensitivity and the choice of functional parameter affect position classification.
- **Why it matters** The distinction between neutral and rheostat positions is central to the framework. If the boundary is highly dependent on experimental context, the framework's utility for comparing across studies and proteins is limited.
- **Resolution test** The authors should discuss the dependence of position classification on assay sensitivity and parameter choice, and consider whether the framework should incorporate a "context-dependent" classification or a more graded measure of rheostat behavior.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Terminology
- **Affected element** The term "rheostat" and the analogy to electrical components
- **Evidence pointer** Title; throughout
- **Issue** The electrical analogy (rheostat vs. toggle vs. neutral) is engaging but may be confusing for readers unfamiliar with older electrical terminology. A rheostat is a variable resistor, while a toggle switch has discrete states. The analogy is apt for the described behaviors, but the manuscript does not explicitly define the analogy for readers who may not be familiar with these terms.
- **Required correction** Add a brief explanation of the electrical analogy when the terms are first introduced, perhaps in the abstract or early in the introduction.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Figure clarity
- **Affected element** Figure 2
- **Evidence pointer** Figure 2 legend
- **Issue** The legend for Figure 2 is partially truncated in the provided manuscript, and the description of the weighting scheme for bins is unclear. The relationship between the histogram analysis and the calculation of Rheostat, Toggle, and Neutral scores is not fully explained.
- **Required correction** Complete the legend and provide a more detailed explanation of the scoring algorithm, possibly with a step-by-step description or a supplementary methods box.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Completeness of evidence
- **Affected element** Table 1
- **Evidence pointer** Table 1
- **Issue** The table lists "Rheostat positions identified to date" for each protein, but the criteria for inclusion and the completeness of the literature search are not described. For example, the table does not include any deep mutational scanning studies beyond those specifically mentioned in the text.
- **Required correction** Add a footnote describing the literature search strategy and inclusion criteria, or explicitly state that the table is not intended to be exhaustive.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Discussion of limitations
- **Affected element** Section "Substitutions at functional rheostat positions have unknown effects on stability"
- **Evidence pointer** Section "Substitutions at functional rheostat positions have unknown effects on stability"
- **Issue** The discussion of stability is brief and does not address the potential interplay between stability and function in the context of rheostat positions. The authors mention the "stability/activity tradeoff" but do not discuss how this might specifically apply to rheostat positions.
- **Required correction** Expand this section to discuss how stability changes might contribute to or confound the functional effects observed at rheostat positions, and how future studies might disentangle these contributions.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Readability
- **Affected element** Section "Assumption 1"
- **Evidence pointer** Section "Assumption 1"
- **Issue** The three assumptions listed are important but are presented in a somewhat dense and abstract manner. The connection between each assumption and its practical consequences for prediction algorithms could be made more explicit.
- **Required correction** Consider adding a brief example or concrete illustration for each assumption to make the concepts more accessible to non-specialist readers.

### Technical failings that need to be addressed before the case is established
1. The quantitative evidence for the dynamics mechanism (R1-M2) is not presented in sufficient detail to evaluate the strength of the correlation.
2. The manuscript does not provide a systematic analysis of available deep mutational scanning datasets to support the claim of "widespread" rheostat positions (R1-M1).
3. The definition of neutral positions and the dependence of classification on assay sensitivity are not adequately addressed (R1-M4).

### Assessment against Nature-style criteria
- **Originality**: The framework of rheostat, toggle, and neutral positions is a novel synthesis that challenges the traditional binary view of substitution effects. While individual observations of intermediate functional effects are not new, the systematic classification and the proposal of a unifying framework represent an original contribution.
- **Scientific importance**: The framework has significant implications for protein engineering, personalized medicine, and evolutionary biology. If validated and adopted, it could improve prediction algorithms and guide experimental design. The importance is high, though the evidence base for generalizability is currently limited.
- **Interdisciplinary readership**: The topic is relevant to structural biology, biochemistry, computational biology, evolutionary biology, and clinical genetics. The manuscript is written in a style that is largely accessible across these disciplines, though some sections (e.g., the dynamics discussion) may be challenging for non-specialists.
- **Technical soundness**: The experimental evidence cited is generally of high quality, and the Rheostat scoring system is a reasonable quantitative approach. However, the reliance on a limited number of protein systems and the speculative nature of the dynamics mechanism reduce the technical soundness of the broader claims.
- **Readability for nonspecialists**: The manuscript is well-written and the figures are effective. The electrical analogy is helpful, though it may require explanation for some readers. The abstract provides a clear summary of the key concepts.

### Recommendation posture
Supportive if technical concerns are resolved. The manuscript presents a valuable conceptual framework that deserves publication, but the claims of generalizability and the mechanistic hypothesis regarding dynamics need to be either strengthened with additional evidence or appropriately tempered. The authors should address the concerns regarding the prevalence of rheostat positions across diverse proteins, provide more quantitative detail on the dynamics correlation, and discuss the practical path toward improving prediction algorithms. With these revisions, the review would make a significant contribution to the field.

## Risk / unsupported claims
- The claim that rheostat positions are "widespread" and can constitute up to 40% of positions in a protein is based on a small number of protein systems, many studied by the authors' own laboratories. The generalizability of this claim is not established.
- The statement that "the emergent properties of predicted, dynamically coupled amino acid networks might explain some of the complex functional outcomes" is speculative and not directly supported by the evidence presented.
- The claim that "∼10% of substitutions gain function" at rheostat positions is presented as a general finding but is based on a limited number of studies and may not be representative.
- The assertion that "no structural pattern has been observed for the locations of functional rheostat positions" is based on visual inspection of a few proteins and does not constitute a systematic analysis.
- The statement that "the two classes [rheostat and neutral] have different evolutionary signatures" is based on analysis of a limited number of proteins and may not be generalizable.