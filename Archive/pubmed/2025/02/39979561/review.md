## Review setup
- **Input scope** Full manuscript text (abstract, introduction, methods, results, discussion, limitations, conclusion)
- **Assessment boundary** Scientific content, methodological soundness, statistical validity, and interpretation of results as presented in the provided manuscript
- **Shared manuscript claim summary** The authors compare intrinsic protein disorder and liquid-liquid phase separation (LLPS) propensity between antimicrobial peptides (AMPs) from the APD3 database and the human proteome from UniProt, reporting that AMPs exhibit higher predicted disorder, lower overall LLPS propensity, distinct amino acid composition, and differential redox-dependent disorder responses.
- **Visible evidence base** Methods sections describing bioinformatics tools (PONDR, IUPred, FuzDrop, FuzPred, AIUPred, Composition Profiler, CH-CDF plots); Results sections with statistical comparisons (ANOVA, chi-square, Mann-Whitney U); Tables 1-2; Figures 1-3 (described in text)
- **Missing materials affecting confidence** Raw data files, complete figure content (only captions visible), exact sequence counts per analysis stage, effect sizes for significant comparisons, software version details, and code/scripts for reproducibility

## Reviewer
- **Overall assessment** The manuscript addresses a potentially interesting question regarding the intrinsic disorder properties of antimicrobial peptides relative to the human proteome. The computational approach is reasonable in principle, and the authors employ multiple established predictors. However, the analysis suffers from several significant methodological weaknesses that undermine confidence in the conclusions. The most critical issue is the substantial reduction in sample size for AMPs (from 3,172 to 1,373 for RIDAO analysis, and further to 410 for FuzDrop/FuzPred), which is not adequately addressed. The length-adjusted comparison is a positive step but is incompletely described. The interpretation of redox-dependent disorder differences is speculative and not well-supported by the data presented. The manuscript would benefit from more rigorous statistical reporting, including effect sizes and confidence intervals, and a clearer discussion of the biological significance of the observed differences.

- **Who would be interested in the results, and why** Researchers in the fields of antimicrobial peptide biology, protein biophysics, and intrinsically disordered proteins would find this work of interest. The study provides a large-scale computational comparison that could inform future experimental studies on AMP mechanisms of action. Clinicians and pharmaceutical researchers interested in developing AMP-based therapeutics might also find the characterization of AMP structural properties useful for design considerations.

- **Major strengths** The study addresses a relevant and timely question given the global antibiotic resistance crisis. The use of multiple complementary disorder predictors (PONDR variants, IUPred) strengthens the robustness of the disorder assessment. The inclusion of a length-adjusted comparison is a thoughtful approach to control for a potential confounding variable. The statistical methods employed (ANOVA, chi-square, Mann-Whitney U) are appropriate for the data types analyzed. The authors acknowledge limitations of computational predictions and appropriately call for experimental validation.

- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors claim that AMPs exhibit higher levels of predicted disorder than human proteins based on RIDAO analysis of 1,373 AMPs versus 20,435 human proteins.
- **Evidence pointer** Results section "Prediction of Disorder Using Commonly Used Predictors", Table 1
- **Concern** The analysis is based on only 1,373 of the 3,172 AMPs initially retrieved, with the remaining 1,799 excluded due to sequence length. This represents a 43% reduction in the AMP dataset. The authors do not provide a comparison of the excluded versus included AMPs in terms of sequence properties, source organisms, or antimicrobial class. If shorter AMPs are systematically excluded, the remaining set may be biased toward longer sequences, which could affect disorder predictions. The comparison with the human proteome, which has a very different sequence length distribution, may therefore be confounded by length effects despite the length-adjusted analysis described later.
- **Why it matters** The central claim of the paper depends on the comparability of the two datasets. If the AMP sample is not representative of the full AMP population, the conclusions about higher disorder in AMPs may not generalize. The lack of transparency about the excluded sequences prevents readers from assessing this potential bias.
- **Resolution test** The authors should provide a detailed comparison of excluded versus included AMPs, including sequence length distributions, amino acid composition, and predicted disorder scores where available. They should also report results using all AMPs where possible, or justify why the excluded sequences cannot be analyzed. Sensitivity analyses using different length thresholds would strengthen the conclusions.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors report that AMPs have a lower overall propensity for LLPS compared to human proteins, based on FuzDrop analysis of 410 AMPs versus 20,274 human proteins.
- **Evidence pointer** Results section "Analysis of Protein LLPS Probability (FuzDrop)", Table 2
- **Concern** The FuzDrop analysis was performed on only 410 AMPs, which is 12.9% of the original 3,172 sequences. This dramatic reduction is attributed to sequence length requirements, but the specific criteria are not stated. The authors do not discuss whether the 410 AMPs are representative of the broader AMP population. Furthermore, the biological interpretation that lower LLPS propensity in AMPs reflects "more controlled and directed" phase separation is speculative and not directly supported by the computational predictions. The FuzDrop tool provides probabilities, not direct evidence of phase separation behavior in biological contexts.
- **Why it matters** The LLPS findings are a major component of the paper's conclusions. If the 410 AMPs analyzed are not representative, the reported differences may be artifacts of the filtering process rather than genuine biological differences. The speculative interpretation of LLPS differences without experimental validation is concerning.
- **Resolution test** The authors should report the exact length criteria used by FuzDrop, compare the characteristics of the 410 analyzed AMPs to the full set, and temper their interpretation of LLPS differences. Ideally, they would also analyze a random sample of human proteins matched for length to the AMPs to ensure the comparison is fair.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Scientific importance
- **Claim pointer** The authors state that their findings "reshape our understanding" of AMPs as "dynamic, multifunctional proteins" and suggest that intrinsic disorder contributes to antimicrobial function.
- **Evidence pointer** Discussion section
- **Concern** The claim that intrinsic disorder contributes to antimicrobial function is not directly tested in this study. The authors show correlations between AMP status and disorder predictions, but they do not establish a causal or mechanistic link between disorder and antimicrobial activity. The discussion cites previous studies on caseins, NK-lysins, and skin peptides, but these are presented as supporting evidence without critical evaluation. The leap from computational predictions to functional claims is not adequately justified.
- **Why it matters** The broader significance of the work depends on the functional relevance of the observed disorder differences. Without experimental evidence linking disorder to antimicrobial activity, the conclusions remain speculative and the practical implications for therapeutic development are unclear.
- **Resolution test** The authors should either (a) clearly frame their findings as computational predictions that require experimental validation, or (b) incorporate additional analyses that link disorder predictions to known antimicrobial potency or mechanism data where available. They should also discuss alternative explanations for the observed differences, such as evolutionary constraints unrelated to antimicrobial function.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Technical soundness
- **Claim pointer** The authors report significant differences in redox-dependent disorder predictions between AMPs and human proteins, interpreting these as indicating "distinct oxidative potential profiles" and suggesting functional implications for antimicrobial activity.
- **Evidence pointer** Results section "Analysis of Redox Reactions with AIUPred", Table 2
- **Concern** The redox-dependent disorder predictions from AIUPred are presented with limited methodological detail. The authors do not explain what the redox-minus and redox-plus scores represent biologically, how the predictions were generated, or what the magnitude of the differences means in practical terms. The effect sizes appear small (e.g., redox-minus 0.328 vs. 0.396), and with large sample sizes, statistical significance may be achieved for differences that are not biologically meaningful. The interpretation that these differences reflect adaptive responses specific to AMPs is not well-supported.
- **Why it matters** The redox findings are presented as a novel contribution, but without clear biological context and effect size information, readers cannot assess their significance. Overinterpretation of small statistical differences could mislead the field.
- **Resolution test** The authors should provide effect sizes (e.g., Cohen's d) and confidence intervals for all significant comparisons, explain the biological meaning of the redox scores, and moderate their interpretation. They should also discuss whether the observed differences are likely to be functionally relevant given the small magnitudes.

- **Concern ID** R1-M5
- **Severity** Major
- **Blocking** No
- **Axis** Technical soundness
- **Claim pointer** The authors describe the CH-CDF plot analysis as revealing that AMPs and human proteins "occupy distinct structural categories," with AMPs showing a greater proportion of highly disordered proteins.
- **Evidence pointer** Results section "CH-CDF Plot Analysis", Figure 3B
- **Concern** The CH-CDF analysis is presented with limited quantitative detail. The authors report chi-square results but do not provide the full contingency table or the proportion of proteins in each quadrant for both groups. The interpretation of quadrant assignments is not clearly linked to functional consequences. Additionally, the length-adjusted CH-CDF analysis is mentioned but not fully described in the results, making it difficult to assess whether the differences persist after controlling for length.
- **Why it matters** The CH-CDF analysis is used to support the conclusion that AMPs are structurally distinct from human proteins. Without complete reporting of the quadrant distributions and their statistical comparison, readers cannot evaluate the strength of this evidence.
- **Resolution test** The authors should provide the full contingency table for the CH-CDF quadrant assignments, including counts and percentages for both AMPs and human proteins, and clearly report the results of the length-adjusted analysis.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Readability
- **Affected element** Abstract
- **Evidence pointer** Abstract
- **Issue** The abstract is dense and includes many technical terms without sufficient context for a general scientific audience. The phrase "liquid-liquid phase separation (LLPS) propensity" is used without explanation of why this property is relevant to antimicrobial function.
- **Required correction** Briefly explain the relevance of LLPS to antimicrobial peptide function in the abstract, or consider whether this detail is necessary for the summary.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Technical soundness
- **Affected element** Methods section "Amino Acid Composition Analysis"
- **Evidence pointer** Methods section
- **Issue** The description of the Composition Profiler analysis is incomplete. The authors state that AMPs and human proteomes were compared against the PDB Select 25 reference set, but do not specify how the statistical significance of composition differences was assessed or whether multiple testing corrections were applied.
- **Required correction** Provide details on the statistical methods used for composition comparison, including any corrections for multiple comparisons.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Technical soundness
- **Affected element** Methods section "Prediction of Disorder Using Commonly Used Predictors"
- **Evidence pointer** Methods section
- **Issue** The authors do not specify the version numbers or specific parameters used for the disorder predictors (PONDR VSL2, VL3, VLXT, FIT, IUPred Short/Long). This limits reproducibility.
- **Required correction** Provide software versions and default or custom parameters for all predictors used.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Readability
- **Affected element** Results section "Analysis of Redox Reactions with AIUPred"
- **Evidence pointer** Results section
- **Issue** The terms "redox-minus" and "redox-plus" are used without clear definition in the results. The reader must infer their meaning from the methods section.
- **Required correction** Briefly define these terms when first used in the results, or refer the reader to the methods section more explicitly.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Technical soundness
- **Affected element** Results section "Length-Adjusted Comparison of Human and AMP Proteomes"
- **Evidence pointer** Results section
- **Issue** The length-adjusted comparison is described in a single paragraph with limited detail. The authors state that significant differences were found but do not report the specific values or effect sizes for the length-matched comparison.
- **Required correction** Provide the key statistics for the length-adjusted comparison, including the number of proteins in each group and the specific metrics compared.

- **Concern ID** R1-m6
- **Severity** Minor
- **Axis** Readability
- **Affected element** Discussion section
- **Evidence pointer** Discussion section
- **Issue** The discussion contains several speculative statements that are not clearly distinguished from findings. For example, the claim that AMPs "may leverage their structural adaptability to interact with diverse microbial targets" is presented as a conclusion rather than a hypothesis.
- **Required correction** Clearly distinguish between findings and hypotheses, and use conditional language for speculative interpretations.

- **Concern ID** R1-m7
- **Severity** Minor
- **Axis** Technical soundness
- **Affected element** Limitations section
- **Evidence pointer** Limitations section
- **Issue** The limitations section does not address the substantial sample size reduction for AMPs in the FuzDrop/FuzPred analyses, which is a significant methodological concern.
- **Required correction** Add a discussion of the sample size reduction and its potential impact on the generalizability of the LLPS findings.

- **Concern ID** R1-m8
- **Severity** Minor
- **Axis** Readability
- **Affected element** Figure 3
- **Evidence pointer** Figure 3 caption
- **Issue** The figure caption is very long and includes extensive methodological detail that would be better placed in the methods section. This makes the caption difficult to read.
- **Required correction** Shorten the figure caption and move methodological details to the methods section.

## Risk / unsupported claims
- The claim that intrinsic disorder "likely contribute[s] to their antimicrobial function" is not directly supported by the computational analysis presented and requires experimental validation.
- The interpretation that lower LLPS propensity in AMPs reflects "more controlled and directed" phase separation is speculative and not supported by the data.
- The claim that redox-dependent disorder differences indicate "distinct oxidative potential profiles" with functional implications is not well-supported given the small effect sizes and lack of biological context.
- The assertion that AMPs and human proteins "occupy distinct structural categories" based on CH-CDF analysis is not fully supported by the quantitative data presented.
- The statement that the study provides "a novel conceptual framework for comparing the disorder profiles" is overstated, as similar comparative approaches have been used in previous studies of disorder in specific protein classes.