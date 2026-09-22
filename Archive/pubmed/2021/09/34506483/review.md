## Review setup
- **Input scope** Full manuscript text including abstract, introduction, results, discussion, methods, and supporting information references.
- **Assessment boundary** Scientific validity, logical coherence, methodological soundness, and support of claims by presented evidence. No assessment of formatting or editorial style beyond readability for a general scientific audience.
- **Shared manuscript claim summary** The authors propose that stochastic pulsing of the transcription factor Crz1 is conserved across distantly related fungi, that this conservation is maintained by stabilizing selection on the signaling phenotype, and that functionally divergent intrinsically disordered regions (IDRs) can support this conserved phenotype. They further claim that increased calcineurin docking site (PxIxIT) strength in a specific region of the IDR is sufficient to rescue pulsing and fitness in a heterologous context.
- **Visible evidence base** Figures 1-5, supplementary figures S1-S11, methods descriptions, statistical analyses, sequence analyses, and competition assays.
- **Missing materials affecting confidence** Raw data files, full strain lists, complete statistical outputs, code for analyses, and some methodological details (e.g., exact parameters for Gaussian process fitting, details of the mutual information estimation pipeline in S1 Text) are not provided in the manuscript text.

## Reviewer
- **Overall assessment** This manuscript addresses an important and underexplored question in evolutionary cell biology: how stochastic signaling dynamics are conserved despite rapid sequence divergence in the regulatory regions that control them. The authors combine comparative genomics, quantitative imaging, information theory, and fitness assays to build a compelling case that Crz1 pulsing is conserved across fungi, that IDR function has diverged, and that a specific molecular feature (PxIxIT strength) can be modified to rescue function. The study is creative and the experimental design is generally rigorous. However, several concerns regarding the strength of the causal claims, the interpretation of the fitness data, and the robustness of the information-theoretic analyses need to be addressed before the case is fully established.
- **Who would be interested in the results, and why** Researchers studying stochastic gene expression and signaling dynamics, evolutionary biologists interested in the evolution of regulatory networks and intrinsically disordered proteins, and systems biologists working on calcium signaling. The work provides a rare example of linking molecular-level changes in IDRs to organismal fitness, which will be of broad interest.
- **Major strengths** 1. The study addresses a fundamental and timely question about the evolution of dynamic signaling phenotypes. 2. The combination of cross-species comparisons, quantitative single-cell imaging, and functional assays is powerful and appropriate. 3. The use of information theory to quantify signaling capacity is a sophisticated and appropriate approach. 4. The identification of a specific, testable molecular feature (PxIxIT strength) and the demonstration that its modification can rescue function is a strong and convincing result. 5. The writing is clear and the logic is generally easy to follow.
- **Major Concerns** 
  - **R1-M1** (Blocking: Yes)
  - **R1-M2** (Blocking: Yes)
  - **R1-M3** (Blocking: No)
  - **R1-M4** (Blocking: No)
- **Minor Comments** 
  - **R1-m1**
  - **R1-m2**
  - **R1-m3**
  - **R1-m4**
- **Technical failings that need to be addressed before the case is established** R1-M1 and R1-M2 are blocking concerns. R1-M3 and R1-M4 are non-blocking but should be addressed to strengthen the manuscript.
- **Assessment against Nature-style criteria** 
  - **Originality** High. The question of how stochastic signaling dynamics evolve is novel, and the specific focus on IDRs and stabilizing selection is a fresh perspective.
  - **Scientific importance** High. The findings have implications for understanding the evolution of signaling systems, the functional significance of IDRs, and the relationship between molecular features and organismal fitness.
  - **Interdisciplinary readership** Moderate to high. The work bridges evolutionary biology, cell biology, and biophysics, and should appeal to researchers in all three fields.
  - **Technical soundness** Generally strong, but with some concerns (see Major Concerns). The imaging, image analysis, and statistical methods are appropriate and well-described. The information-theoretic analysis is a strength, but its robustness needs further validation.
  - **Readability for nonspecialists** Good. The manuscript is well-written and the concepts are explained clearly, although some of the methodological details may be challenging for a general audience.
- **Recommendation posture** Supportive if the technical concerns are resolved. The core findings are potentially important, but the current evidence does not fully establish the causal link between PxIxIT strength, pulsing, and fitness, nor does it rule out alternative explanations for the observed conservation of pulsing.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Causal inference
- **Claim pointer** The authors claim that "increasing PxIxIT strength in the homologous region of S. cerevisiae IDR is sufficient to rescue pulsing phenotype and fitness" (Results, section "Increasing PxIxIT strength in the homologous region of S. cerevisiae IDR is sufficient to rescue pulsing phenotype and fitness").
- **Evidence pointer** Figure 5, specifically panels B, C, and D.
- **Concern** The rescue experiment (CaHigh) involves three point mutations (Q445T, I446P, N451Q) that increase predicted PxIxIT strength. While the authors show that this construct supports pulsing and improves fitness, the experiment does not isolate the effect of PxIxIT strength from other potential effects of these specific mutations. The mutations could alter other properties of the IDR, such as overall charge, phosphorylation status, or interactions with other proteins. The claim that PxIxIT strength is "sufficient" is therefore too strong. A more rigorous test would involve mutating the PxIxIT site in the S. cerevisiae IDR to reduce its strength and showing that this abolishes pulsing, or using a more systematic mutagenesis approach to show that the effect is specifically due to PxIxIT strength.
- **Why it matters** The central thesis of the paper is that a specific molecular feature (PxIxIT strength) is a key determinant of pulsing and fitness. If the rescue is due to other effects of the mutations, the conclusion is weakened.
- **Resolution test** The authors should either (1) perform a complementary experiment where the S. cerevisiae PxIxIT is weakened and show that this reduces or abolishes pulsing and fitness, or (2) use a series of mutations that systematically vary PxIxIT strength (e.g., using the PSSM to design mutations with graded predicted strengths) and show a dose-response relationship with pulsing and fitness.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Statistical robustness
- **Claim pointer** The authors claim that "the dynamics of both constructs with the S. cerevisiae docking site (CaHigh and Ca:PxIxIT:Sc) encoded more mutual information than that of the outgroup IDRs" (Results, section "Increasing PxIxIT strength in the homologous region of S. cerevisiae IDR is sufficient to rescue pulsing phenotype and fitness").
- **Evidence pointer** Figure 5B and 5C, and Methods section "Estimation of mutual information and pulse-triggered averaging".
- **Concern** The mutual information (MI) estimates are based on a kNN estimator with k=4, applied to Gaussian process parameters. The authors report mean MI values and p-values from t-tests, but the sample sizes are very small (n=3 for CaHigh and Ca:PxIxIT:Sc, n=1 for Ca:Sc). The MI estimates are likely to be noisy, and the t-test may not be appropriate for such small sample sizes. Furthermore, the authors do not report confidence intervals or effect sizes. The robustness of the MI estimates to the choice of k, the Gaussian process kernel, and the parameterization of the trajectories is not assessed.
- **Why it matters** The information-theoretic analysis is a key piece of evidence for the claim that pulsing encodes information. If the MI estimates are not robust, the claim is not well-supported.
- **Resolution test** The authors should (1) report the full distribution of MI estimates, including confidence intervals, (2) perform a sensitivity analysis varying k and the Gaussian process parameters, and (3) consider using a permutation test or other non-parametric test that does not rely on the t-test assumption.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Alternative explanations
- **Claim pointer** The authors state that "the lack of pulsing of more distantly related IDRs (and failure to rescue fitness under calcium stress) when expressed in S. cerevisiae implies that protein-protein interactions between the IDRs and the calcium signaling pathway have changed in some way, while the output of the regulatory network has remained the same" (Results, section "Pulsing is conserved, but the underlying mechanisms have changed").
- **Evidence pointer** Figures 2 and 3.
- **Concern** The authors interpret the lack of pulsing of the C. albicans and S. pombe IDRs in S. cerevisiae as evidence for changes in protein-protein interactions. However, this could also be due to differences in protein stability, expression levels, or post-translational modification machinery between the species. The authors do not directly measure protein levels or stability of the chimeric constructs. The observation that the outgroup IDRs show similar average nuclear localization (Figure 2A) is suggestive but does not rule out differences in the dynamics of nuclear import/export or in the interactions with other S. cerevisiae proteins.
- **Why it matters** The conclusion that the mechanism has changed is important for the stabilizing selection model. If the lack of pulsing is due to a trivial reason like poor expression, the conclusion is weakened.
- **Resolution test** The authors should measure the expression levels and stability of the chimeric proteins (e.g., by Western blot) and, if possible, test whether the outgroup IDRs interact with S. cerevisiae calcineurin and other relevant proteins (e.g., by co-immunoprecipitation).

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Generalizability
- **Claim pointer** The authors propose a general model where "evolutionary flexibility of functionally divergent IDRs underlies the conservation of stochastic signaling by stabilizing selection" (Abstract and Discussion).
- **Evidence pointer** Entire manuscript.
- **Concern** The study is limited to a single transcription factor (Crz1) and a single signaling pathway (calcium/calcineurin). While the authors discuss the potential generalizability of their findings, they do not provide evidence from other systems. The claim of a general principle is therefore speculative.
- **Why it matters** The title and abstract suggest a broad conclusion, but the evidence is from a single case study. Overstating the generality could mislead readers.
- **Resolution test** The authors should temper their language in the abstract and discussion, or provide additional evidence from other pulsatile transcription factors or signaling pathways to support the general model.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Methods, "Estimation of mutual information and pulse-triggered averaging"
- **Evidence pointer** Methods section.
- **Issue** The description of the MI estimation pipeline is somewhat terse, and the details are relegated to S1 Text. A brief summary of the key steps in the main text would improve readability.
- **Required correction** Add a sentence or two summarizing the pipeline in the main text, and ensure S1 Text is complete and self-contained.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Statistical reporting
- **Affected element** Figure 2C and 2E
- **Evidence pointer** Figure 2.
- **Issue** The authors report p-values from t-tests but do not report effect sizes or confidence intervals. For a reader, it is difficult to assess the magnitude of the differences.
- **Required correction** Report effect sizes (e.g., Cohen's d) and confidence intervals for the key comparisons.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Data availability
- **Affected element** Methods, "Yeast strains"
- **Evidence pointer** Methods section.
- **Issue** The authors do not state whether the strains and plasmids are available upon request or deposited in a public repository.
- **Required correction** Add a data availability statement.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Interpretation
- **Affected element** Discussion, paragraph on compensatory changes
- **Evidence pointer** Discussion section.
- **Issue** The authors speculate about compensatory changes in the calcineurin regulatory domain (Cna1) but do not provide direct evidence. This is presented as a "possible mechanism" which is fine, but it could be more clearly labeled as speculation.
- **Required correction** Clearly distinguish between conclusions supported by data and speculative hypotheses.

## Risk / unsupported claims
- The claim that PxIxIT strength is "sufficient" to rescue pulsing and fitness is not fully supported, as the rescue experiment does not isolate the effect of PxIxIT strength from other potential effects of the mutations (R1-M1).
- The claim that the lack of pulsing of outgroup IDRs in S. cerevisiae is due to changes in protein-protein interactions is not directly tested and could be due to other factors (R1-M3).
- The general model of "evolutionary flexibility of functionally divergent IDRs underlies the conservation of stochastic signaling" is based on a single case study and is presented too strongly (R1-M4).
- The mutual information estimates are based on small sample sizes and their robustness is not assessed (R1-M2).