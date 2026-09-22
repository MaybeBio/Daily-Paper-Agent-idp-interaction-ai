## Review setup
- **Input scope** Full manuscript text (main text, figure legends, methods summary) as provided by the user
- **Assessment boundary** Scientific content, experimental design, data interpretation, and claims as presented in the provided text. No access to supplementary figures, tables, or raw data beyond what is described in the text.
- **Shared manuscript claim summary** The authors propose that Arg–Tyr cation–π interactions drive liquid–liquid phase separation (LLPS) in native black widow spider major ampullate (MA) silk and persist into the final fiber state, where they contribute to β-sheet assembly. The study integrates solution NMR, DNP-enhanced solid-state NMR, molecular dynamics simulations, and AlphaFold3 structural modeling to support this model.
- **Visible evidence base** Main text figures (Figs. 1–6) as described in the text, NMR chemical shift and relaxation data summarized in text, MD simulation results, AlphaFold3 model predictions, and SHIFTX2 chemical shift comparisons. Supplementary tables and figures are referenced but not available for review.
- **Missing materials affecting confidence** Supplementary figures (S1–S18) and tables (S1–S21) are referenced extensively but not provided. Raw NMR spectra, simulation trajectories, and AlphaFold3 model coordinates are not available. Experimental details for NMR acquisition and analysis are only summarized in the main text.

## Reviewer

- **Overall assessment** This manuscript presents a compelling and technically sophisticated investigation into the molecular mechanisms underlying LLPS and fiber assembly in native spider silk. The combination of solution NMR, DNP-enhanced solid-state NMR, MD simulations, and AI-based structural modeling is ambitious and largely appropriate for the questions addressed. The central claim that Arg–Tyr cation–π interactions serve as molecular "stickers" linking phase separation to structural ordering is plausible and supported by multiple lines of evidence. However, several concerns regarding the strength of the NMR evidence for cation–π interactions in the fiber state, the interpretation of relaxation data, and the reliance on low-confidence AlphaFold3 models warrant careful consideration. The manuscript would benefit from additional quantitative analysis and clearer presentation of key data.

- **Who would be interested in the results, and why** Researchers in the fields of biomaterials, protein phase separation, structural biology, and biophysics would find this work of significant interest. The study addresses a long-standing question in spider silk biology—how soluble proteins transition to solid fibers—and offers a molecular-level framework that could inform biomimetic fiber design. The methodological integration of NMR, simulations, and AI-based modeling will also appeal to methodologists and those studying other intrinsically disordered proteins and phase-separating systems.

- **Major Strengths**  
  1. The use of native silk dope rather than recombinant constructs is a significant advance, as prior LLPS studies have largely relied on simplified recombinant systems.  
  2. The combination of multiple complementary techniques (solution NMR, DNP-enhanced SSNMR, MD, AlphaFold3) provides a multi-scale view from molecular interactions to macroscopic assembly.  
  3. The observation that phosphate selectively enhances Arg–Tyr interactions while disrupting Arg–Ala contacts is a specific and mechanistically informative finding.  
  4. The DNP-enhanced SSNMR approach to detect Arg–Tyr contacts in the solid fiber is technically innovative and addresses a challenging problem.  
  5. The authors are appropriately cautious in acknowledging limitations, particularly regarding the low confidence of AlphaFold3 models and the complexity of heterogeneous systems.

- **Major Concerns**

- **Concern ID** R1-M1  
- **Severity** Major  
- **Blocking** Yes  
- **Axis** Evidence strength for central claim  
- **Claim pointer** "DNP-enhanced MAS SSNMR experiments provide direct evidence for Arg–Tyr cation–π interactions in the final spun fiber" and "cross-peaks between Tyr Cγ,δ and Cε sites and Arg Nη groups, consistent with cation–π contacts"  
- **Evidence pointer** Figure 5A, SI Appendix Figs. S9–S11, S18  
- **Concern** The central claim that Arg–Tyr cation–π interactions persist in the fiber state rests on a single 2D hNHHC spectrum (Fig. 5A). The authors report cross-peaks between Tyr ring carbons and Arg Nη groups, but the text acknowledges that one potential correlation (Tyr Cζ–Arg Nη) overlaps with an Arg Cζ–Nη signal. This overlap raises the possibility that the observed correlations are not uniquely attributable to cation–π interactions. Furthermore, the assignment of the two distinct Arg Nη resonances (72.5 and 75.8 ppm) to a single asymmetric T-shaped geometry is an interpretation that requires more rigorous justification. Alternative explanations, such as two distinct binding sites or conformational heterogeneity, are not fully excluded. The authors should provide more detailed spectral analysis, including control experiments or additional correlation experiments, to strengthen this assignment.  
- **Why it matters** The persistence of Arg–Tyr cation–π interactions in the fiber state is a key pillar of the proposed model. If this evidence is ambiguous, the claim that these interactions "drive" β-sheet assembly is weakened.  
- **Resolution test** Provide additional 2D correlation spectra with higher resolution or selective labeling strategies to unambiguously assign the observed cross-peaks. Include control experiments with mutant or modified peptides that disrupt cation–π interactions. Quantify the signal-to-noise ratio and provide evidence that the observed correlations are statistically significant.

- **Concern ID** R1-M2  
- **Severity** Major  
- **Blocking** No  
- **Axis** Interpretation of relaxation data  
- **Claim pointer** "T2 relaxation measurements... revealed phase-dependent differences in backbone dynamics" and "enhanced T2 relaxation in Gly-rich regions suggestive of modulated μs–ms dynamics"  
- **Evidence pointer** Figure 3, SI Appendix Figs. S5, Tables S5–S7  
- **Concern** The interpretation of T2 shortening in the condensed phase as evidence for "modulated μs–ms dynamics" is plausible but not uniquely determined. T2 can be affected by multiple factors, including chemical exchange, dipolar interactions, and sample heterogeneity. The authors note that T2 values could not be reliably measured for Gly-rich regions in 1 M urea due to low signal, which limits the comparison. Additionally, the claim that "Arg and Tyr residues exhibited higher NOEs (~0.3 to 0.4) than most Gly residues" is presented without statistical analysis. The authors should provide error estimates and statistical tests to support claims of significant differences between samples and residue types.  
- **Why it matters** The relaxation data are used to support the model that LLPS induces selective dynamic changes in Gly-rich regions. If the interpretation is not robust, the mechanistic conclusions are weakened.  
- **Resolution test** Provide uncertainty estimates for T1, T2, and NOE values. Perform statistical comparisons (e.g., t-tests or ANOVA) between conditions. Consider additional relaxation dispersion experiments to directly probe μs–ms timescale dynamics.

- **Concern ID** R1-M3  
- **Severity** Major  
- **Blocking** No  
- **Axis** Model validation  
- **Claim pointer** "AlphaFold3 models more closely resemble the nanocrystalline β-sheet architecture characteristic of the silk fiber" and "SHIFTX2-predicted 13C and 15N chemical shifts for Ala, Gly, and Arg residues in β-sheet regions also show strong concordance with experimental values"  
- **Evidence pointer** Figure 6, SI Appendix Tables S16–S19  
- **Concern** The use of AlphaFold3 models to represent the fiber state is concerning given the low overall confidence scores (pTM = 0.33 for the hexamer). The authors acknowledge this limitation but proceed to use these models to draw structural conclusions. The claim of "strong concordance" between SHIFTX2-predicted and experimental chemical shifts is not quantified. What is the magnitude of the deviations? How does this concordance compare to what would be expected for a random or incorrect structure? The authors should provide quantitative metrics (e.g., RMSD between predicted and experimental shifts) and compare against appropriate null models.  
- **Why it matters** The structural models are used to support the proposed arrangement of Arg–Tyr interactions at β-sheet interfaces. If the models are unreliable, the structural conclusions are speculative.  
- **Resolution test** Provide quantitative comparison metrics between predicted and experimental chemical shifts. Include error analysis and discuss the significance of the agreement. Consider alternative modeling approaches or experimental validation (e.g., mutagenesis coupled with NMR) to test the predicted interactions.

- **Concern ID** R1-M4  
- **Severity** Major  
- **Blocking** No  
- **Axis** Generalizability of findings  
- **Claim pointer** "These findings establish a framework for understanding how proteins harness phase separation to form functional materials"  
- **Evidence pointer** Discussion section  
- **Concern** The study focuses on a single spider species (L. hesperus) and a single protein system (MaSp1). The claim that the findings establish a general framework for phase separation in functional materials is ambitious. The authors do not discuss how their findings might apply to other silk types (e.g., flagelliform silk) or other structural proteins. The specificity of the Arg–Tyr interaction mechanism to this system is not addressed.  
- **Why it matters** The broader significance of the work depends on its generalizability. If the mechanism is unique to this system, the impact is more limited.  
- **Resolution test** Discuss the conservation of Arg–Tyr motifs across spider species and silk types. If possible, provide preliminary data on other systems or clearly articulate the testable predictions that would extend the framework.

- **Minor Comments**

- **Concern ID** R1-m1  
- **Severity** Minor  
- **Axis** Clarity of methods  
- **Affected element** Materials and Methods section  
- **Evidence pointer** Materials and Methods  
- **Issue** The methods section is extremely brief and refers readers to the SI Appendix for "full experimental details." Given the technical complexity of the experiments (DNP-enhanced NMR, selective isotope labeling), more detail in the main text would help readers assess the feasibility and robustness of the approach.  
- **Required correction** Provide additional methodological details in the main text, particularly for the DNP experiments and the isotope labeling strategy, or clearly state which specific SI sections contain the relevant information.

- **Concern ID** R1-m2  
- **Severity** Minor  
- **Axis** Statistical reporting  
- **Affected element** Figure 3 and associated text  
- **Evidence pointer** Figure 3, SI Appendix Tables S5–S7  
- **Issue** Relaxation parameters are reported as averages with standard deviations, but no statistical comparisons are provided. The claim that "Gly residues—particularly in RG, GG, GAG, GAG, AG motifs—showed enhanced T2 relaxation in the condensed phase" is not supported by statistical analysis.  
- **Required correction** Add statistical tests (e.g., t-tests with multiple comparison correction) to support claims of significant differences between samples and residue types.

- **Concern ID** R1-m3  
- **Severity** Minor  
- **Axis** Figure quality  
- **Affected element** Figure 5A  
- **Evidence pointer** Figure 5A  
- **Issue** The key hNHHC spectrum showing Arg–Tyr correlations is described in the text but the figure itself is not available for review. The authors should ensure that the figure clearly shows the cross-peaks and that the assignments are unambiguous.  
- **Required correction** Ensure the figure includes clear labels for the cross-peaks and provides sufficient resolution to distinguish the reported correlations from noise or overlap.

- **Concern ID** R1-m4  
- **Severity** Minor  
- **Axis** Discussion of limitations  
- **Affected element** Discussion section  
- **Evidence pointer** Discussion section  
- **Issue** The authors acknowledge limitations but do not discuss the potential impact of the low AlphaFold3 confidence scores on their conclusions in sufficient depth.  
- **Required correction** Expand the discussion of model limitations and how they might affect the interpretation of the structural data.

- **Concern ID** R1-m5  
- **Severity** Minor  
- **Axis** Terminology  
- **Affected element** Throughout  
- **Evidence pointer** Throughout  
- **Issue** The term "native" is used to describe the silk system, but the silk is obtained from spiders that have been fed isotope-labeled amino acids. This is a form of metabolic labeling that could potentially affect protein behavior.  
- **Required correction** Clarify whether the isotope labeling has any known effects on silk protein properties and discuss this in the context of the "native" designation.

## Risk / unsupported claims
- The claim that Arg–Tyr cation–π interactions "drive" β-sheet assembly in the fiber state is not fully supported by the evidence presented. The hNHHC spectrum provides evidence for spatial proximity, but causality is not established.
- The assertion that AlphaFold3 models "more closely resemble the nanocrystalline β-sheet architecture" of the fiber is based on low-confidence predictions (pTM = 0.33) and requires more rigorous validation.
- The claim that the findings "establish a framework for understanding how proteins harness phase separation to form functional materials" is overly broad given the focus on a single system.
- The statement that "phosphate promotes LLPS by displacing hydration water and shifting the sidechain interaction network toward Arg–Tyr contacts" is supported by MD simulations but lacks direct experimental validation of the water displacement mechanism.
- The interpretation of the two distinct Arg Nη resonances as evidence for a single asymmetric T-shaped geometry is not uniquely determined and requires additional experimental support.