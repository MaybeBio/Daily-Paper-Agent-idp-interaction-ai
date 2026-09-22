## Review setup
- **Input scope** Full manuscript text (abstract, introduction, results, discussion, methods, data/code availability statements)
- **Assessment boundary** Scientific validity, methodological soundness, evidence quality, and significance of claims as presented in the provided text
- **Shared manuscript claim summary** The authors introduce On-the-fly Probability Enhanced Sampling (OPES) in the multithermal ensemble as an efficient method for generating atomistic conformational ensembles of intrinsically disordered proteins (IDPs). They demonstrate its application to four systems of increasing size (15 to 71 residues), compare results against REST2 and unbiased simulations, and report the discovery of transient tertiary structure in the disordered protein ACTR that is consistent with experimental data and may be relevant for conformational selection and drug design.
- **Visible evidence base** Abstract, Introduction, Results (narrative only, no figures or tables visible), Methods (detailed simulation protocols, analysis procedures, reweighting methodology), Data/Code availability statements
- **Missing materials affecting confidence** All figures, tables, and supplementary materials referenced in the text (Figures 1–5, S1–S18; Tables 1–2, S1–S8) are not provided. This substantially limits the ability to evaluate the quantitative evidence supporting the central claims.

## Reviewer

- **Overall assessment** This manuscript presents a potentially valuable methodological contribution to the IDP simulation community. The application of OPES multithermal sampling to IDPs is timely, and the practical guidance provided in the Methods section is useful. However, the central scientific claim—that OPES reveals transient tertiary structure in ACTR that is not captured by other methods—cannot be adequately evaluated without the figures, tables, and supplementary materials. The text alone provides insufficient quantitative detail to assess convergence, statistical significance, or the robustness of the reported findings. The manuscript is well-written and the methodological framework is sound in principle, but the evidence base as presented is incomplete.
- **Who would be interested in the results, and why** Computational biophysicists and molecular simulators working on IDPs and conformational ensembles will be the primary audience. The methodological comparison between OPES, REST2, and unbiased simulations addresses a practical need for efficient sampling techniques. Researchers studying coupled folding and binding, particularly those interested in ACTR and similar transcriptional coactivators, will also find the reported transient tertiary structures relevant. The work may additionally interest developers of enhanced sampling methods and those building generative AI models for IDP ensembles, as the authors note the utility of atomistic ensembles as training data.
- **Major strengths** The manuscript addresses a well-recognized challenge in IDP simulation: achieving converged ensembles at tractable computational cost. The choice of four systems spanning a range of sizes and complexities is appropriate for benchmarking. The practical guidance on bias convergence, temperature step estimation, and the empirical formula relating system size to temperature steps is valuable. The integration of multiple experimental datasets (NMR chemical shifts, RDCs, PREs, SAXS) for validation is rigorous in design. The authors are appropriately cautious about limitations, including the possibility of incomplete sampling and the need for further validation.
- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence quality
- **Claim pointer** The claim that OPES enables "efficient generation of atomistic ensembles" and achieves "accelerating convergence and enabling broader exploration of low-population conformational states" across all four systems.
- **Evidence pointer** Results sections "Overview of the approach and model systems", "Helix-coil transitions of the (AAQAA)3 peptide", "Efficient sampling of an extended IDP with helical structure", "OPES enables improved conformational space exploration"; Figures 2–4; Tables S1–S8; location not provided for specific data points
- **Concern** The quantitative evidence supporting the efficiency and convergence claims is not visible in the provided text. The narrative describes acceleration factors (2–3× vs REST2, 10–16× vs unbiased for (AAQAA)3; 1.3–8.8× for HTTex1; 4.4–6.5× for ACTR20-60) and convergence improvements, but the underlying data (autocorrelation functions, blocking analyses, cumulative averages, bootstrap estimates) are in figures and tables that are not provided. Without these, it is impossible to assess whether the reported acceleration factors are statistically meaningful, whether the error estimates are reliable, or whether the convergence criteria are appropriate. The authors note that blocking can underestimate uncertainty, which raises questions about the robustness of the reported error bars.
- **Why it matters** The central methodological claim of the paper is that OPES provides efficient and converged sampling. If the evidence for this claim is not verifiable, the primary contribution of the work is undermined.
- **Resolution test** Provide the figures and tables showing autocorrelation functions, blocking analyses, cumulative averages, and bootstrap estimates. Demonstrate that the reported acceleration factors are robust across independent replicates and that the convergence criteria are met in all systems.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence quality
- **Claim pointer** The claim that OPES reveals "transiently structured states in which multiple α-helices involved in partner binding fold cooperatively and form tertiary contacts" in ACTR, and that these states are "consistent with extensive NMR and SAXS data."
- **Evidence pointer** Results section "An integrative structural ensemble of ACTR"; Figures 5, S15–S18; location not provided for specific data points
- **Concern** The discovery of transient tertiary structure in ACTR is the most scientifically significant claim in the manuscript, yet the evidence for it is entirely contained in figures and supplementary materials that are not provided. The text describes free-energy landscapes, contact maps, clustering analyses, and comparisons with experimental data, but none of these are visible. The claim that these states are "consistent with" experimental data is particularly difficult to evaluate without seeing the quantitative comparisons (e.g., Q-factors, reduced chi-squared values, RMSE values). The statement that the states are "not captured by REST2 or unbiased simulations" is a strong claim that requires demonstration of adequate sampling in those methods to rule out the possibility that the states were simply not sampled due to insufficient simulation time.
- **Why it matters** The biological significance of the work rests on this claim. If the evidence is not verifiable, the impact of the manuscript is substantially reduced.
- **Resolution test** Provide the free-energy landscapes, contact maps, clustering results, and experimental comparisons shown in Figures 5 and S15–S18. Demonstrate that the transient tertiary states are statistically significant, reproducible across independent simulations, and genuinely absent from REST2 and unbiased simulations with adequate sampling.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Methodological rigor
- **Claim pointer** The claim that the reweighted OPES ensemble provides "improved agreement with the left-out RDC and PRE data" compared to the REST2-derived ensemble.
- **Evidence pointer** Results section "An integrative structural ensemble of ACTR"; Figure S15; location not provided for specific data points
- **Concern** The reweighting procedure is described in detail, but the comparison between OPES and REST2 ensembles in terms of agreement with left-out experimental data is only described qualitatively in the text. The authors state that the OPES ensemble showed better agreement with RDCs (Q-factor 0.45 vs 0.55) but the REST2 ensemble achieved slightly better agreement with SAXS (reduced chi-squared 1.19 vs 1.40). The interpretation of these differences is not discussed in sufficient detail. Are these differences statistically significant? Do they reflect genuine differences in ensemble quality or simply differences in the prior ensembles used for reweighting? The authors note that the OPES prior has non-uniform weights, which complicates the comparison.
- **Why it matters** The claim that OPES provides a better basis for integrative ensemble modeling is an important secondary claim. If the differences are not statistically meaningful, the claim is weakened.
- **Resolution test** Provide statistical tests comparing the agreement metrics between OPES and REST2 ensembles. Discuss whether the differences are within the uncertainty of the reweighting procedure.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Reproducibility
- **Claim pointer** The claim that the OPES method is "robust and reproducible" and that "independently generated biases yielded reproducible ensembles" for ACTR20-60.
- **Evidence pointer** Results section "OPES enables improved conformational space exploration"; Figure S9; location not provided for specific data points
- **Concern** The reproducibility assessment is described for ACTR20-60, but the text notes "some small, localised differences exceeding the combined uncertainties" between ensembles generated with independent biases. The authors attribute these to finite sampling and potential underestimation of errors from blocking. This is a reasonable interpretation, but the magnitude and location of these differences are not described. For the larger systems (HTTex1, full-length ACTR), no reproducibility assessment is mentioned. Given that the authors recommend using a single converged bias for production, it is important to know how sensitive the results are to the specific bias used.
- **Why it matters** Reproducibility is a core requirement for a methodological contribution. If the results are sensitive to the choice of bias, the practical utility of the method is reduced.
- **Resolution test** Provide a more detailed description of the differences between ensembles generated with independent biases, including their magnitude and location. Consider assessing reproducibility for the larger systems as well.

- **Concern ID** R1-M5
- **Severity** Major
- **Blocking** No
- **Axis** Scope of validation
- **Claim pointer** The claim that the findings "establish OPES multithermal sampling as a robust and accessible approach for uncovering rare, functionally relevant conformations in intrinsically disordered proteins."
- **Evidence pointer** Discussion section; location not provided
- **Concern** The validation is limited to four systems, only one of which (full-length ACTR) is a biologically relevant IDP with known functional significance. The other systems are a short peptide and two IDPs chosen for their challenging sampling properties. While this is a reasonable starting point, the claim of general robustness is not fully supported by the evidence presented. The authors acknowledge this limitation in the Discussion, but the framing of the conclusion is somewhat stronger than the evidence warrants.
- **Why it matters** The generalizability of the method is a key claim. If the method only works well for certain types of IDPs or under certain conditions, the practical impact is reduced.
- **Resolution test** Discuss the limitations of the validation more explicitly and temper the conclusion accordingly. Alternatively, provide additional validation on a broader range of IDP systems.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Methods section, OPES multithermal simulations
- **Evidence pointer** Methods section, "OPES multithermal simulations"; location not provided
- **Issue** The description of the empirical formula for estimating the number of temperature steps is incomplete. The text states "we also estimated a simple relationship between (number of atoms) and the number of temperature steps" but the actual formula is not given in the visible text. It may be in a table or supplementary material, but this is not clear.
- **Required correction** Provide the explicit formula in the main text or clearly reference the table or supplementary section where it is given.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Results section, "An integrative structural ensemble of ACTR"
- **Evidence pointer** Results section, "An integrative structural ensemble of ACTR"; location not provided
- **Issue** The description of the reweighting procedure mentions that "frames for which PRE observables could not be evaluated for all sites (due to steric clashes between spin label rotamers and protein atoms) were excluded from the analysis." The fraction of frames excluded is not reported. This could introduce bias if a significant fraction of frames is excluded.
- **Required correction** Report the fraction of frames excluded and discuss the potential impact on the results.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Results section, "OPES enables improved conformational space exploration"
- **Evidence pointer** Results section, "OPES enables improved conformational space exploration"; location not provided
- **Issue** The text mentions that "OPES samples ~40% more area in Rg–helicity space" for ACTR20-60, but the baseline for this comparison is not entirely clear. Is this compared to REST2, unbiased simulations, or both?
- **Required correction** Clarify the baseline for the comparison and ensure consistency with the description of the HTTex1 results.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Reproducibility
- **Affected element** Methods section, "Molecular dynamics simulations"
- **Evidence pointer** Methods section, "Molecular dynamics simulations"; location not provided
- **Issue** The text states that "all simulations were prepared and performed with GROMACS 2023.4 and PLUMED 2.10 using GPUs (except REST2 simulations, vide infra)." The specific GPU hardware and software versions are not reported. This is a minor issue but could affect reproducibility.
- **Required correction** Report the specific GPU hardware and software versions used.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Discussion section
- **Evidence pointer** Discussion section; location not provided
- **Issue** The Discussion mentions that "several conformations observed in MD simulations initiated from the bound state of ACTR were not recovered, or were sampled with reduced structural content" in the OPES simulations. This is an important limitation, but it is not discussed in detail. Which conformations were not recovered, and what are the implications for the completeness of the OPES ensemble?
- **Required correction** Provide more detail on which conformations were not recovered and discuss the implications for the interpretation of the results.

- **Technical failings that need to be addressed before the case is established** The primary technical failing is the absence of all figures, tables, and supplementary materials from the provided text. The central claims of the manuscript—efficiency gains, convergence, discovery of transient tertiary structure, and consistency with experimental data—are all supported by data in these missing materials. Without them, the case is not established. Additionally, the reproducibility assessment is incomplete for the larger systems, and the potential for bias from excluding frames in the PRE analysis is not quantified.

- **Assessment against Nature-style criteria** 
  - Originality: The application of OPES multithermal sampling to IDPs is a novel contribution, though the method itself is established. The discovery of transient tertiary structure in ACTR is potentially original and significant, but this cannot be fully assessed without the evidence.
  - Scientific importance: The work addresses a significant challenge in the field and has potential implications for understanding IDP function and drug design. The importance is moderate to high, depending on the robustness of the evidence.
  - Interdisciplinary readership: The work is primarily of interest to computational biophysicists and molecular simulators. The potential biological implications for ACTR function may broaden the audience, but the technical focus limits interdisciplinary appeal.
  - Technical soundness: The methodological framework is sound in principle, and the authors demonstrate awareness of potential pitfalls (e.g., blocking underestimating errors). However, the technical soundness of the specific claims cannot be fully evaluated without the missing data.
  - Readability for nonspecialists: The manuscript is well-written and the concepts are explained clearly. The Methods section is detailed and accessible. However, the Results section relies heavily on figures and tables that are not provided, making it difficult to follow the narrative.

- **Recommendation posture** Currently not established from the provided evidence. The manuscript has the potential to be a valuable contribution, but the evidence base is incomplete. I would recommend requesting the full manuscript with all figures, tables, and supplementary materials before making a final decision. If the evidence supports the claims as described, the manuscript could be suitable for publication in a high-impact journal, though the scope may be more appropriate for a specialized computational biology or biophysics journal rather than a general audience journal.

## Risk / unsupported claims
- The claim that OPES "enables efficient generation of atomistic ensembles" and achieves "accelerating convergence" is not supported by visible evidence.
- The claim that OPES reveals "transiently structured states" in ACTR with "tertiary structure not captured by REST2 or unbiased simulations" is not supported by visible evidence.
- The claim that these states are "consistent with extensive NMR and SAXS data" is not supported by visible evidence.
- The claim that the OPES ensemble shows "improved agreement with the left-out RDC and PRE data" compared to REST2 is not supported by visible evidence.
- The claim that the method is "robust and reproducible" is only partially supported by the text, and the reproducibility assessment is incomplete for the larger systems.
- The claim that the findings "establish OPES multithermal sampling as a robust and accessible approach" is not fully supported by the limited validation presented.