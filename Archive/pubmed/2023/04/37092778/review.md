## Review setup
- **Input scope** Abstract only
- **Assessment boundary** Claims and evidence as presented in the abstract; no access to full text, figures, tables, or supplementary materials
- **Shared manuscript claim summary** The authors use three deep learning structure prediction programs (AlphaFold2, RoseTTAFold, ESMFold) to compare "Newly Born" orphan proteins with "Never Born" random polypeptides, and to predict structures of orphan proteins with known or unknown experimental structures. They report that predictions align with experimental data for compactness versus disorder, that only a taxonomically restricted protein yields high-quality consensus predictions matching its crystal structure, and that one large orphan protein (HCO_11565) is predicted with high quality and similarity across all three algorithms.
- **Visible evidence base** Abstract text only; no figures, tables, statistical details, or method descriptions provided
- **Missing materials affecting confidence** Full manuscript, all figures and tables, statistical analysis details, sequence and structure identifiers, algorithm version and parameter settings, and any supplementary data

## Reviewer
- **Overall assessment** The abstract presents an interesting and potentially valuable comparative study, but the evidence base is too limited to evaluate the validity of the central claims. The qualitative agreement between predictions and experimental data is plausible, yet the lack of quantitative metrics, statistical details, and structural comparisons prevents a rigorous assessment. The claim regarding HCO_11565 is intriguing but unsupported without structural alignments or confidence scores.
- **Who would be interested in the results, and why** Researchers in protein evolution, structural biology, and computational biology would find this relevant, as it addresses whether deep learning predictors can extract meaningful signals from orphan proteins and random polypeptides. Those studying de novo gene birth and intrinsically disordered proteins may also be interested in the comparative framework.
- **Major strengths** The study addresses a novel question by applying state-of-the-art predictors to an underexplored protein class. The use of experimentally characterized "Never Born" proteins as a benchmark is a thoughtful design. The inclusion of orphan proteins with known crystal structures provides a test of predictive accuracy.
- **Major Concerns** 
  - R1-M1
  - R1-M2
  - R1-M3
- **Minor Comments** 
  - R1-m1
  - R1-m2
  - R1-m3
- **Technical failings that need to be addressed before the case is established** The abstract lacks any quantitative comparison between predicted and experimental structures (e.g., RMSD, TM-score), no confidence score distributions are reported, and the statistical test for accessible surface area differences is not described. Without these, the core claims of agreement and significance cannot be verified.
- **Assessment against Nature-style criteria** Originality is moderate, as the application of existing tools to orphan proteins is novel but not conceptually groundbreaking. Scientific importance is limited by the descriptive nature of the findings, which do not yet offer mechanistic or generalizable insights. Interdisciplinary readership is plausible but narrow, primarily appealing to structural and evolutionary biologists. Technical soundness cannot be assessed from the abstract alone, as no methodological details or error analyses are provided. Readability for nonspecialists is adequate, though the abstract assumes familiarity with orphan proteins and deep learning predictors.
- **Recommendation posture** Currently not established from the provided evidence. The abstract suggests a potentially useful study, but the absence of quantitative results and methodological transparency precludes a supportive recommendation.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors claim that predicted differences in compactness between Group 1 and Group 3 "Never Born" proteins are statistically significant based on accessible surface areas.
- **Evidence pointer** Abstract text, location not provided
- **Concern** The abstract states that statistical significance was established, but no details are given regarding the statistical test used, the sample size, the distribution of accessible surface area values, or the effect size. Without this information, the claim of significance cannot be evaluated or reproduced.
- **Why it matters** Statistical significance is a central pillar of the study's conclusion that the predictors distinguish ordered from disordered proteins. If the test is underpowered or inappropriately applied, the conclusion may be invalid.
- **Resolution test** Provide the specific statistical test, p-values, confidence intervals, and a description of how accessible surface areas were computed and compared across the two groups.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors claim that for the three orphan proteins with known crystal structures, only the taxonomically restricted protein (not a true orphan) yielded high-quality predictions closely resembling the crystal structure, while the two true orphans with novel folds did not.
- **Evidence pointer** Abstract text, location not provided
- **Concern** No quantitative measures of prediction quality or structural similarity are provided, such as RMSD, TM-score, or pLDDT values. The phrase "closely resembling" is subjective and cannot be assessed without numerical comparisons.
- **Why it matters** The distinction between high-quality and low-quality predictions is a key finding, but without objective metrics, the reader cannot determine whether the differences are meaningful or within normal variation for these predictors.
- **Resolution test** Report per-protein RMSD and TM-score relative to the crystal structures, along with per-residue confidence scores from each algorithm, and specify the criteria used to define "high-quality."

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors claim that all three algorithms make "remarkably similar and high-quality predictions" for HCO_11565, and conjecture this is due to many homologs in its taxonomically restricted family and to Dali server hits with nonrelated proteins.
- **Evidence pointer** Abstract text, location not provided
- **Concern** The claim of high-quality predictions is unsupported by any structural alignment metrics or confidence scores. The conjecture about the cause is speculative and not backed by comparative analyses, such as multiple sequence alignment depth or fold similarity scores.
- **Why it matters** This is a prominent positive result, but without evidence, it may mislead readers into overinterpreting the predictive power of the algorithms for orphan proteins.
- **Resolution test** Provide TM-scores or RMSD between the three predicted models, pLDDT or similar confidence metrics, and a quantitative comparison of the predicted structure to the Dali-identified folds.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Terminology
- **Evidence pointer** Abstract text, location not provided
- **Issue** The terms "Newly Born" and "Never Born" are used without formal definitions, which may confuse readers unfamiliar with the field.
- **Required correction** Define both terms explicitly in the abstract or introduction, and clarify the distinction between orphan proteins and taxonomically restricted proteins.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Reproducibility
- **Affected element** Method description
- **Evidence pointer** Abstract text, location not provided
- **Issue** The abstract does not specify which versions of AlphaFold2, RoseTTAFold, and ESMFold were used, nor the input sequence preparation steps.
- **Required correction** State the software versions and any relevant parameters or default settings in the methods section.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Data availability
- **Evidence pointer** Abstract text, location not provided
- **Issue** The abstract mentions an interactive 3D complement in Proteopedia, but no accession codes or direct links are provided for the orphan proteins or the "Never Born" protein sequences.
- **Required correction** Include accession numbers or database identifiers for all sequences and structures in the main text or supplementary materials.

## Risk / unsupported claims
- The claim of statistical significance for accessible surface area differences is unsupported without test details.
- The claim that only the taxonomically restricted protein yields high-quality predictions is unsupported without quantitative structural metrics.
- The claim of "remarkably similar and high-quality predictions" for HCO_11565 is unsupported without alignment scores or confidence values.
- The conjecture regarding the cause of high-quality predictions for HCO_11565 is speculative and not backed by comparative data.
- The general statement that "the models generated were scored as being of low quality" is vague and lacks a definition of the scoring criteria.