## Review setup
- **Input scope** Full manuscript text (abstract, introduction, results, methods, supplementary figure legends, and references as provided)
- **Assessment boundary** Scientific content, methodological rigor, and claims as presented in the provided text; no external data or unpublished materials were accessed
- **Shared manuscript claim summary** The authors report that the C-terminal intrinsically disordered region (CIDR) of the transcription factor RUNX2 is required for chromatin binding and osteogenic differentiation. They show that linear sequence motifs are dispensable, and instead, features of the conformational ensemble predict function. They develop a generative design algorithm (GOOSE with FINCHES) to create de novo functional IDRs that rescue RUNX2 activity.
- **Visible evidence base** Abstract, introduction, results sections (Figures 1–5 referenced), supplementary figure legends (S1–S14), and methods sections for cell culture, differentiation, CRISPR knockout, immunoblotting, single molecule tracking, ChIP-seq, RNA-seq, molecular dynamics simulations, and generative design
- **Missing materials affecting confidence** Full figure panels and data values (e.g., exact ChIP-seq peak numbers, RNA-seq effect sizes, SMT binding fractions with error bars), supplementary tables, and code/analysis scripts were not provided; statistical details for several comparisons are incomplete

## Reviewer
- **Overall assessment** This manuscript presents a compelling and well-executed study that addresses a significant gap in protein engineering: the design of functional intrinsically disordered regions. The authors combine careful cell biology, quantitative imaging, genomics, and biophysical simulations to demonstrate that RUNX2's CIDR functions through ensemble-level properties rather than linear motifs. The generative design approach is innovative and the results are potentially transformative. However, several technical concerns regarding data completeness, statistical rigor, and the generalizability of the design algorithm need to be addressed before the conclusions are fully established.
- **Who would be interested in the results, and why** This work will be of high interest to researchers in protein biophysics, intrinsically disordered proteins, transcription factor biology, developmental biology, and protein engineering. The demonstration that de novo IDR design can recapitulate complex biological functions opens new avenues for synthetic biology and therapeutic design. The methodological framework (GOOSE + FINCHES) will be valuable to the IDR community.
- **Major strengths** 1) The study addresses a fundamental and timely question in IDR biology with a rigorous multi-disciplinary approach. 2) The use of a physiologically relevant differentiation assay provides strong functional validation. 3) The systematic mutagenesis and scrambling experiments are well-designed to distinguish between motif-based and ensemble-based mechanisms. 4) The generative design approach is novel and represents a significant methodological advance. 5) The integration of simulations, imaging, and genomics provides a comprehensive view of mechanism.
- **Major Concerns** See detailed items below.
- **Minor Comments** See detailed items below.
- **Technical failings that need to be addressed before the case is established** R1-M1 (statistical rigor of SMT), R1-M2 (ChIP-seq peak calling and differential analysis), R1-M3 (generative design validation), R1-M4 (generalizability of design algorithm)
- **Assessment against Nature-style criteria**  
  *Originality*: High. The concept of designing functional IDRs based on ensemble properties is novel and extends the field beyond structure-based design.  
  *Scientific importance*: High. The findings challenge the prevailing motif-centric view of IDR function and provide a new framework for understanding and engineering IDRs.  
  *Interdisciplinary readership*: Broad. The work bridges biophysics, cell biology, genomics, and computational design, making it relevant to multiple communities.  
  *Technical soundness*: Generally strong, but several methodological details and statistical analyses need clarification and strengthening (see Major Concerns).  
  *Readability for nonspecialists*: The manuscript is well-written and accessible, with clear figures and logical flow. Some methods sections are dense but appropriate for the target audience.
- **Recommendation posture** Supportive if technical concerns are resolved. The core findings are novel and important, but the current evidence base has gaps in statistical rigor and validation that must be addressed.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Statistical rigor
- **Claim pointer** "For both functional RUNX2 variants, WT and LocScr1, the slow-diffusing fraction was near the H2B control, indicating most molecules were chromatin-bound."
- **Evidence pointer** Figure 4C, S10
- **Concern** The SMT data are presented as a single comparison of slow-diffusing fractions, but no statistical analysis is reported. The number of cells, number of independent experiments, and variability (e.g., standard error or confidence intervals) are not provided. The claim that WT and LocScr1 are "near the H2B control" is qualitative and lacks a formal statistical test. Additionally, the diffusion coefficient of free molecules is mentioned but not quantified or compared across variants.
- **Why it matters** The SMT data are central to the claim that the CIDR mediates chromatin binding. Without proper statistical analysis, it is unclear whether the observed differences between functional and non-functional variants are significant and reproducible.
- **Resolution test** Provide a detailed statistical analysis of SMT data, including the number of cells and experiments, mean and variance of bound fractions, and appropriate statistical tests (e.g., ANOVA or mixed-effects models) comparing all variants. Report effect sizes and confidence intervals.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Data analysis and interpretation
- **Claim pointer** "The ΔCIDR variant lost the majority of ChIP-seq peaks, L2mut and P3mut showed a partial loss, and LocScr1 bound a similar number of sites relative to WT."
- **Evidence pointer** Figure 4E–J, S11–S13
- **Concern** The ChIP-seq analysis is described but key details are missing: the number of peaks called for each variant, the criteria for differential binding, and the statistical thresholds used. The PCA on differentially bound peaks is mentioned, but the variance explained by PC1 and the loadings are not reported. The linear model for predicting differential binding from motif count and accessibility is described, but the model coefficients, significance, and goodness-of-fit are not provided. The claim that ΔCIDR binds "only in the most open chromatin regions" is not quantitatively supported.
- **Why it matters** The ChIP-seq data are essential for linking CIDR function to chromatin binding at specific genomic loci. Without rigorous analysis and reporting, the conclusions about differential binding and chromatin accessibility are not fully supported.
- **Resolution test** Provide a complete ChIP-seq analysis pipeline, including peak counts, differential binding statistics, PCA results with variance explained, and the full linear model output. Include genome browser tracks or heatmaps to visually support the claims about binding at accessible vs. inaccessible regions.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Validation of generative design
- **Claim pointer** "Two synthetic variants – one of fixed and one of free composition – were fully functional, matching the success rates reported for state-of-the-art structured binder design."
- **Evidence pointer** Figure 5E
- **Concern** The success rate of the generative design is based on only six tested variants (three per category). The claim that this "matches" state-of-the-art structured binder design is not statistically justified given the small sample size. Additionally, the criteria for "fully functional" are not clearly defined beyond the mineralization assay. It is unclear whether the functional synthetic variants were tested for all aspects of RUNX2 function (e.g., gene expression, chromatin binding) or only mineralization.
- **Why it matters** The generative design is a key innovation of the study. The small number of tested variants and lack of detailed functional characterization limit the strength of the claim that the algorithm can reliably produce functional IDRs.
- **Resolution test** Increase the number of designed variants tested (e.g., 20–30 per category) and provide a clear definition of "functional" with multiple assays. Report the success rate with confidence intervals and compare to a suitable null model.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Generalizability
- **Claim pointer** "These findings demonstrate the central role for TF IDRs in chromatin binding and extend generative protein design beyond the folded proteome."
- **Evidence pointer** Abstract, Discussion
- **Concern** The study focuses on a single TF (RUNX2) and a single differentiation system. The claim that the findings "extend generative protein design beyond the folded proteome" is broad and may overstate the generalizability of the approach. The authors do not test whether the design algorithm works for other IDRs or in other cellular contexts.
- **Why it matters** The broader significance of the work depends on whether the design principles are transferable. Without additional examples, the claim of generalizability is not fully supported.
- **Resolution test** Provide evidence that the design algorithm can generate functional IDRs for at least one additional TF or IDR, or clearly state the limitations of the current study in the Discussion.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Figure 1F
- **Evidence pointer** Figure 1F, S4
- **Issue** The mineralization data for the VP16, ZIM3, and ARGFX fusions are described qualitatively. It would be helpful to show the full time course or dose-response curves.
- **Required correction** Include representative images or quantitative time-course data for mineralization in the supplementary figures.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Methodology
- **Affected element** Molecular dynamics simulations
- **Evidence pointer** Methods, Figure 3
- **Issue** The simulation parameters (e.g., temperature, salt concentration, number of replicates) are described, but the convergence of the simulations is not discussed. It is unclear whether the contact maps and inter-residue distances are well-converged.
- **Required correction** Add a convergence analysis (e.g., block averaging or split-half analysis) to demonstrate that the simulation results are stable.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Data availability
- **Affected element** Code and data availability
- **Evidence pointer** Data, code, and materials availability
- **Issue** The statement that code is available on GitHub is good, but the specific repository structure and dependencies are not described. It would be helpful to provide a versioned release or DOI.
- **Required correction** Provide a stable link with a versioned release and a brief description of the repository structure.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Interpretation
- **Affected element** Discussion
- **Evidence pointer** Discussion
- **Issue** The discussion of "fuzzy complexes" and "molecular grammars" is interesting but somewhat speculative. The authors could more clearly distinguish between what is directly supported by their data and what is hypothesis.
- **Required correction** Add a sentence or two clarifying which aspects of the model are directly tested and which are speculative.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Statistical reporting
- **Affected element** RNA-seq analysis
- **Evidence pointer** Methods, Figure 4G
- **Issue** The RNA-seq analysis is described, but the number of differentially expressed genes and the effect sizes are not reported in the main text.
- **Required correction** Include a summary of the RNA-seq results (e.g., number of DEGs, top pathways) in the main text or supplementary.

## Risk / unsupported claims
- The claim that "linear IDR motifs are dispensable" is supported by the scrambling experiments, but the possibility of redundant motifs is acknowledged. The statement is somewhat strong given that only a limited set of scrambling variants was tested.
- The claim that "features of the conformational ensemble predict function" is based on correlations between simulation-derived metrics and mineralization. The causal relationship is not directly tested.
- The claim that the generative design "matches the success rates reported for state-of-the-art structured binder design" is not statistically justified given the small sample size.
- The generalizability of the design approach to other IDRs and TFs is not demonstrated and should be stated as a limitation.