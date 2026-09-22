## Review setup
- **Input scope** Abstract only
- **Assessment boundary** Claims and conclusions presented in the abstract; no methods, results, figures, or tables were provided for evaluation
- **Shared manuscript claim summary** The abstract states that computational prediction of DNA-binding residues (DBRs) and RNA-binding residues (RBRs) in protein sequences is an active field with approximately 90 predictors, about 20 published in the last two years. It claims that new predictors use deep neural networks and protein language models, produce accurate predictions, and are available as code or web servers. It further identifies a shortage of tools for intrinsically disordered regions and for residues interacting with specific RNA and DNA types, and recommends that cross-predictions between RBRs and DBRs be quantified and minimized.
- **Visible evidence base** Abstract text only; no supporting data, literature survey details, benchmark results, or methodological descriptions were supplied
- **Missing materials affecting confidence** Full manuscript, including the literature survey methodology, criteria for predictor inclusion, performance comparison data, definitions of "accurate predictions," and any quantitative evidence for the identified gaps

## Reviewer
- **Overall assessment** The abstract presents a concise and plausible overview of the current state of nucleic acid binding residue prediction, with a clear identification of research gaps and a forward-looking recommendation. However, the claims are largely qualitative and cannot be verified from the abstract alone. The absence of methodological detail, quantitative evidence, and a defined scope for the survey limits the ability to assess the rigor and completeness of the review. The recommendation regarding cross-predictions is sensible but lacks supporting data.
- **Who would be interested in the results, and why** Computational biologists, bioinformaticians, and researchers developing or using protein function prediction tools would find this review useful. It provides a snapshot of the field, highlights practical limitations, and suggests directions for future tool development, which is relevant for both tool builders and experimentalists seeking reliable prediction methods.
- **Major strengths** The abstract is clearly written and identifies specific, actionable gaps in the field, particularly the lack of tools for intrinsically disordered regions and for nucleic acid type-specific interactions. The emphasis on quantifying cross-predictions is a practical and important point that could improve the specificity of future predictors. The stated count of predictors and recent publications suggests a systematic survey, which is valuable for readers.
- **Major Concerns** 
  - R1-M1
  - R1-M2
  - R1-M3
- **Minor Comments** 
  - R1-m1
  - R1-m2
- **Technical failings that need to be addressed before the case is established** The abstract does not provide any evidence for the claimed number of predictors, the accuracy of new methods, or the identified gaps. Without a description of the survey methodology, inclusion criteria, or performance benchmarks, the central claims are unverifiable. The recommendation to minimize cross-predictions is not supported by any quantitative analysis of current predictor behavior.
- **Assessment against Nature-style criteria** Originality: The abstract does not present novel findings but rather a synthesis of existing work, which is appropriate for a review but not original in a research sense. Scientific importance: The topic is relevant and the identified gaps are meaningful, but the importance is not demonstrated with data. Interdisciplinary readership: The abstract is accessible to a broad computational biology audience, but the lack of quantitative detail may limit appeal to experimentalists. Technical soundness: Cannot be assessed from the abstract alone; the claims are plausible but unsupported. Readability for nonspecialists: The abstract is clear and jargon is minimal, making it readable for a general scientific audience.
- **Recommendation posture** Currently not established from the provided evidence. The abstract is promising but the claims require full manuscript evidence to be evaluated. Supportive if the full manuscript provides a systematic survey methodology, quantitative performance data, and a clear analysis of the identified gaps.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence sufficiency
- **Claim pointer** The abstract claims there are about 90 predictors and 20 published in the last two years, and that new predictors produce accurate predictions.
- **Evidence pointer** Abstract text; location not provided
- **Concern** The abstract provides no methodology for how predictors were identified, counted, or classified as recent. The claim of "accurate predictions" is not supported by any benchmark data or comparison metrics.
- **Why it matters** These quantitative claims are central to the review's value. Without a transparent survey method and performance evidence, readers cannot trust the counts or the accuracy assertion, which undermines the credibility of the entire review.
- **Resolution test** The full manuscript must include a detailed description of the literature search strategy, inclusion and exclusion criteria, and a table or figure summarizing predictor performance with defined metrics and datasets.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Claim support
- **Claim pointer** The abstract states there is a shortage of tools for intrinsically disordered regions and for specific RNA and DNA types.
- **Evidence pointer** Abstract text; location not provided
- **Concern** The identified gaps are presented as facts, but no evidence is given to demonstrate the shortage, such as a systematic analysis of existing tools' capabilities or a comparison of coverage across different prediction targets.
- **Why it matters** The gaps are the main contribution of the review, as they motivate future work. If the shortage is not rigorously demonstrated, the review's recommendations lack a solid foundation.
- **Resolution test** The full manuscript should include a systematic assessment of available predictors, categorizing them by their ability to handle disordered regions and nucleic acid type specificity, with a clear table or figure showing the distribution.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence sufficiency
- **Claim pointer** The abstract recommends that cross-predictions between RBRs and DBRs be quantified and minimized.
- **Evidence pointer** Abstract text; location not provided
- **Concern** The recommendation is reasonable, but the abstract does not provide any data showing that cross-predictions are currently a problem, such as error rates or confusion matrices from existing predictors.
- **Why it matters** Without evidence of the issue, the recommendation appears speculative. Quantifying the problem is necessary to justify the proposed direction and to give readers a sense of its severity.
- **Resolution test** The full manuscript should include an analysis of existing predictors' cross-prediction behavior, with quantitative results showing the extent of the issue and its impact on prediction specificity.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Definition of "accurate predictions"
- **Evidence pointer** Abstract text; location not provided
- **Issue** The term "accurate predictions" is vague and could mean different things depending on the dataset, metric, or threshold used.
- **Required correction** In the full manuscript, define accuracy with specific metrics (e.g., Matthews correlation coefficient, area under the receiver operating characteristic curve) and describe the benchmark datasets used.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Scope clarity
- **Affected element** Survey scope
- **Evidence pointer** Abstract text; location not provided
- **Issue** The abstract does not specify the time frame for the survey beyond "last two years" for recent predictors, nor does it clarify whether the 90 predictors include all published tools or only those with available implementations.
- **Required Correction** Clarify the search period, inclusion criteria, and whether predictors without code or web servers were excluded, to allow readers to interpret the counts accurately.

## Risk / unsupported claims
- The claim of approximately 90 predictors and 20 recent publications is unsupported without a described survey methodology.
- The assertion that new predictors produce accurate predictions is unsupported without performance data.
- The identified shortage of tools for intrinsically disordered regions and specific nucleic acid types is unsupported without a systematic gap analysis.
- The recommendation to quantify and minimize cross-predictions is unsupported without evidence of the problem's existence or magnitude.