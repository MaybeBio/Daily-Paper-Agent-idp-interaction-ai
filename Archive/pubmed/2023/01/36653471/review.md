## Review setup
- **Input scope** Full manuscript text including abstract, introduction, results, discussion, methods, figure legends, and tables
- **Assessment boundary** Scientific content, experimental design, data interpretation, and claims as presented in the provided manuscript
- **Shared manuscript claim summary** The authors propose that evolutionary fine-tuning of residual helix structure in the intrinsically disordered transcription factor DREB2A modulates binding kinetics, complex structure, and lifetime when interacting with the αα-hub RCD1-RST. They use an evolution-guided design of variants with varying helical propensity and show that increased residual helicity correlates with increased complex lifetime via decreased dissociation rate constants, and that helical content in the free state correlates with structure in the bound state.
- **Visible evidence base** Stopped-flow fluorescence kinetics (association and dissociation), NMR chemical shift analysis, CD spectroscopy, ITC thermodynamics, evolutionary sequence analysis, and structural modeling
- **Missing materials affecting confidence** Supplementary Data files 1-5 (raw kinetic, NMR, CD, and ITC data), Supplementary Figures 1-6, and the Reporting Summary were not provided. These are referenced for key quantitative claims and statistical assessments.

## Reviewer
- **Overall assessment** This manuscript addresses a fundamental question in the biology of intrinsically disordered proteins, namely how residual structure in the free state influences binding kinetics and complex properties. The evolution-guided design approach is novel and thoughtful, and the correlation between free-state helicity and bound-state structure is an important observation. However, the strength of the conclusions depends critically on the quality and interpretation of the kinetic and structural data, and several aspects require clarification. The claim that residual structure "manifests in complex structure and lifetime" is supported by the presented data, but the mechanistic interpretation and generalizability need further scrutiny. The manuscript is well-written and the figures are clear, but some statistical details and control experiments are missing from the provided text.

- **Who would be interested in the results, and why** Researchers studying intrinsically disordered proteins, protein-protein interactions, coupled folding and binding mechanisms, transcriptional regulation, and molecular recognition. The evolution-guided design approach will also be of interest to protein engineers and computational biologists. The findings have implications for understanding how natural sequence variation tunes interaction networks, which is relevant to fields ranging from plant stress biology to human disease mechanisms involving disordered transcription factors.

- **Major strengths**
  1. The evolution-guided design approach is a significant methodological advance over traditional alanine scanning, as it maintains biological relevance while systematically varying helical propensity.
  2. The multi-technique approach (kinetics, NMR, CD, ITC) provides complementary views of the system.
  3. The correlation between free-state helicity and bound-state structure is a novel and important finding.
  4. The LFER analysis provides a clear framework for interpreting the kinetic effects of mutations.
  5. The study addresses a long-standing debate about the role of residual structure in IDP binding.

- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness of kinetic analysis
- **Claim pointer** The authors claim that "the primary effect of residual structure manifested in complex lifetime" based on altered dissociation rate constants, with association rate constants remaining largely unchanged across variants.
- **Evidence pointer** Figure 3c-d, Table 1, Results section "DREB2A helix modulating substitutions manifest in altered dissociation rate constants and complex lifetime"
- **Concern** The association rate constants for all variants are reported as being similar (222-246 µM⁻¹s⁻¹), but the dissociation rate constants vary by over 20-fold (0.030 to 0.70 s⁻¹). The authors attribute this to differences in residual helicity, but the kinetic mechanism is not fully established. Specifically, the stopped-flow experiments measure binding of a peptide to a protein, and the interpretation assumes a simple one-step binding mechanism. However, coupled folding and binding is often described by more complex mechanisms (e.g., induced fit with conformational selection components). The authors do not test whether the data are consistent with alternative kinetic models. Additionally, the dissociation experiments use unlabeled DREB2A(244-272) as a competitor, but the labeled peptide is DREB2A(246-272), which is two residues shorter. The authors state that FITC attachment did not affect affinity, but the truncation effect is not addressed. If the two-residue difference affects binding, the competition assay may not accurately report true dissociation rates.
- **Why it matters** The central claim of the paper is that residual structure modulates complex lifetime through dissociation rate constants. If the kinetic model is incorrect or the competition assay is compromised, this conclusion would be weakened. The quantitative correlation between helicity and koff (R² = 0.98) is striking, but it depends on the accuracy of the koff values.
- **Resolution test** The authors should provide evidence that the binding kinetics are consistent with a single-step mechanism, or explicitly test alternative models. They should also address the potential effect of the two-residue truncation in the labeled peptide, either by using the same length for labeled and unlabeled peptides or by showing that the truncation does not affect binding kinetics.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** No
- **Axis** Interpretation of structural correlation
- **Claim pointer** The authors claim "a correlation (R² = 0.70) between helical structure content in the free and the bound DREB2A variants exists" and that this supports the idea that free-state structure carries information to complex structure.
- **Evidence pointer** Figure 2f-h, Results section "SliM-region substitutions affect helical content in both free and bound forms"
- **Concern** The correlation between free-state and bound-state helicity is based on only five data points (five variants). With such a small sample size, the R² value of 0.70 is not particularly robust, and the confidence intervals on this correlation are likely wide. Moreover, the authors report that the N-terminal part of the helix (V261-L264) has similar helicity (91-94%) across variants in the bound state, while the C-terminal part (L265-D267) varies substantially (58-107%). This suggests that the correlation is driven primarily by the C-terminal region, which is also the region where the mutations are located. The authors should discuss whether the correlation reflects a general principle or is a consequence of the specific positions mutated.
- **Why it matters** The claim that free-state helicity predicts bound-state structure is a key finding with potential general implications. If this correlation is weak or driven by a specific region, the generalizability of the conclusion is limited.
- **Resolution test** The authors should provide confidence intervals for the correlation, discuss the region-specific nature of the correlation, and ideally test additional variants at different positions to determine whether the correlation holds more broadly.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Thermodynamic interpretation
- **Claim pointer** The authors state that "the thermodynamics most likely reflected differences in binding optimization (enthalpy) and structural heterogeneity (entropy) in the complex" based on ITC measurements.
- **Evidence pointer** Table 3, Results section "Thermodynamics of DREB2 variants support altered α-helix content and heterogeneity in the complex"
- **Concern** The ITC measurements were performed at 300 mM NaCl, while the kinetic measurements were performed at 100 mM NaCl. The authors do not discuss whether the thermodynamic parameters are comparable to the kinetic parameters under the same conditions. Additionally, the ITC data show that the R266G variant has a less favorable enthalpy (ΔH = -56 kJ/mol) compared to WT (-68 kJ/mol) and D267L (-69 kJ/mol), but the entropy term is also different. The interpretation that the enthalpy differences reflect "binding optimization" is plausible but not directly tested. The authors should discuss the salt concentration difference and its potential impact on the interpretation.
- **Why it matters** The thermodynamic analysis is used to support the mechanistic interpretation that residual structure affects the energy landscape of binding. If the conditions are not comparable, the conclusions may be compromised.
- **Resolution test** The authors should either perform ITC at 100 mM NaCl or explicitly discuss why the salt concentration difference does not affect the interpretation. They should also provide a more detailed analysis of the enthalpy-entropy compensation.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Generalizability of the evolution-guided approach
- **Claim pointer** The authors claim that their "orthogonal evolutionary approach" is a general strategy for designing variants with varying amounts of structure while maintaining biological relevance.
- **Evidence pointer** Results section "Evolution-guided method for selection of substitutions", Discussion
- **Concern** The approach is applied to a single system (DREB2A binding to RCD1-RST) and a single binding region. The authors identify positions R266 and D267 as key regulators of helicity based on sequence alignments, but it is unclear how general this approach would be for other IDP systems. The authors should discuss the limitations of the approach and what conditions are required for it to be applicable elsewhere.
- **Why it matters** The novelty of the approach is a major strength of the paper, but its general utility is not established. If the approach only works in this specific system, its impact is limited.
- **Resolution test** The authors should discuss the general applicability of the approach, perhaps by identifying the criteria that make a system amenable to this strategy, or by citing examples where similar approaches have been used successfully.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity of presentation
- **Affected element** Figure 1
- **Evidence pointer** Figure 1a-d
- **Issue** The figure is information-dense and the grouping of species into three categories (I, II, III) based on predicted helicity is not immediately clear. The color coding in Figure 1b is not explained in the legend.
- **Required correction** The authors should clarify the color coding in Figure 1b and provide a more explicit explanation of how the three groups were defined and what they represent.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Statistical reporting
- **Affected element** Table 1
- **Evidence pointer** Table 1
- **Issue** The kinetic parameters are reported with standard errors from the fit, but the number of independent experiments (n) is not stated in the table. The methods state that "approximately 50 traces were collected and averaged for each independent acquisition," but the number of independent acquisitions is not given.
- **Required correction** The authors should state the number of independent experiments for each kinetic parameter in the table or in the methods.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Completeness of methods
- **Affected element** ITC methods
- **Evidence pointer** Methods section "Isothermal titration calorimetry (ITC)"
- **Issue** The ITC methods do not specify the concentration of the titrant and the cell contents precisely, nor the number of replicates. The statement "The values represent means with n = 3" is in the table legend, but the methods do not describe how the replicates were performed.
- **Required correction** The authors should provide more detail on the ITC experimental design, including concentrations, number of replicates, and how the data were fit.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Interpretation of LFER
- **Affected element** Figure 3f
- **Evidence pointer** Figure 3f
- **Issue** The LFER plot shows a horizontal relationship between log kon and log Kd, but the slope is reported as 0.007 ± 0.02. The authors should clarify whether this slope is significantly different from zero and what the confidence interval is.
- **Required correction** The authors should report the confidence interval for the slope and state whether it is statistically distinguishable from zero.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Discussion of alternative mechanisms
- **Affected element** Discussion
- **Evidence pointer** Discussion section
- **Issue** The authors conclude that the data support an induced fit mechanism, but they do not discuss alternative interpretations, such as conformational selection or a combination of both. The Discussion would benefit from a more nuanced treatment of the mechanism.
- **Required correction** The authors should acknowledge the limitations of their kinetic analysis in distinguishing between binding mechanisms and discuss the possibility of a more complex mechanism.

## Risk / unsupported claims
1. The claim that "the primary effect of residual structure manifested in complex lifetime" is supported by the kinetic data, but the mechanistic interpretation depends on the assumption of a simple one-step binding mechanism, which is not explicitly tested.
2. The correlation between free-state and bound-state helicity (R² = 0.70) is based on a small sample size (n = 5) and may not be robust.
3. The claim that the evolution-guided approach is "orthogonal" and maintains "biological relevance" is plausible but not quantitatively demonstrated. The authors do not show that the variants are more biologically relevant than traditional alanine variants.
4. The statement that "the thermodynamics most likely reflected differences in binding optimization (enthalpy) and structural heterogeneity (entropy)" is speculative and not directly tested.
5. The generalizability of the findings to other IDP systems is not established, and the authors do not discuss the limitations of the approach in this regard.
6. The claim that "balancing of residual structure can be a powerful tool for fine-tuning complex IDP-based interaction networks" is an extrapolation that goes beyond the data presented.
7. The ITC measurements at 300 mM NaCl are not directly comparable to the kinetic measurements at 100 mM NaCl, and the authors do not address this discrepancy.
8. The statement that "the higher the content of α-helix in the free state of DREB2A, the longer the lifetime of the complex" is based on a correlation with R² = 0.98, but this is derived from only five data points and should be interpreted with caution.

## Assessment against Nature-style criteria
- **Originality** The evolution-guided design approach is genuinely novel and represents a methodological advance over traditional alanine scanning. The finding that free-state helicity correlates with bound-state structure is an important and original observation. The study addresses a long-standing question in the IDP field with a fresh approach.
- **Scientific importance** The results have implications for understanding how natural sequence variation in disordered regions tunes interaction networks, which is relevant to many biological processes. The finding that residual structure modulates complex lifetime through dissociation rate constants is mechanistically important and could inform future studies of IDP-based interactions.
- **Interdisciplinary readership** The work will appeal to biophysicists, structural biologists, biochemists, and molecular biologists studying protein interactions. The evolutionary perspective adds a dimension that may attract evolutionary biologists and bioinformaticians. The writing is accessible, but some sections assume familiarity with biophysical methods.
- **Technical soundness** The experimental design is generally sound, with appropriate methods for the questions asked. However, the kinetic analysis would benefit from a more rigorous treatment of alternative models, and the ITM conditions are not fully consistent with the kinetic conditions. The small sample size for the correlation analysis is a limitation.
- **Readability for nonspecialists** The manuscript is well-written and the figures are clear. The abstract and introduction are accessible, but the results and discussion sections assume familiarity with biophysical terminology and concepts. The evolutionary analysis is explained clearly.

## Recommendation posture
Supportive if technical concerns are resolved. The core finding, that evolutionarily informed variation in residual helicity correlates with complex lifetime through dissociation rate constants, is interesting and potentially important. However, the strength of this conclusion depends on the kinetic analysis being robust to alternative models and the correlation being statistically meaningful. The authors should address the concerns about the kinetic model, the ITC conditions, and the statistical robustness of the correlations. If these issues are resolved, the manuscript would be suitable for publication in Communications Biology.