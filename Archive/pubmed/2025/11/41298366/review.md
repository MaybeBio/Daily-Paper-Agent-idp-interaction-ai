## Review setup
- **Input scope** Full manuscript text, including abstract, introduction, results, discussion, methods, and figure legends
- **Assessment boundary** Scientific validity, technical soundness, and support of claims by presented evidence
- **Shared manuscript claim summary** The authors propose structural models for the physiological multimerization of the conserved region (CR, residues 319–341) of TDP-43 C-terminal domain, suggesting that the CR forms dynamic, tetrameric helical assemblies stabilized by a methionine-rich core, with W334 and L330 playing key roles, and that these assemblies are relevant for TDP-43 phase separation, nuclear retention, and function
- **Visible evidence base** NMR spectroscopy (chemical shifts, CSPs, NOEs, relaxation), analytical ultracentrifugation (SV-AUC), AlphaFold2-Multimer predictions, all-atom molecular dynamics simulations, phase separation assays, cell-based nuclear retention assays, and yeast toxicity data from published deep mutagenesis
- **Missing materials affecting confidence** Supplementary figures and tables referenced but not provided; source data files not accessible; detailed statistical analysis for AUC modeling not fully described; raw NMR spectra not shown; specific parameters for AF2-Multimer confidence scoring not fully detailed

## Reviewer
- **Overall assessment** This manuscript presents a comprehensive, multi-technique investigation into the structural basis of TDP-43 CTD conserved region multimerization. The integration of NMR, AUC, AF2-Multimer, and MD simulations is ambitious and appropriate for the challenging nature of the system. The correlation between in vitro phase separation data, NMR-derived contacts, and simulation-based structural models is compelling. However, several technical concerns regarding the interpretation of AUC data, the use of AF2-Multimer for dynamic assemblies, and the indirect nature of some cellular assays need to be addressed before the central claims can be fully established. The manuscript is well-written and will be of interest to the structural biology and neurodegeneration communities.
- **Who would be interested in the results, and why** Structural biologists studying intrinsically disordered proteins and their assemblies; researchers in the TDP-43 field, including those focused on ALS, FTD, and LATE; scientists interested in the application of integrative structural biology approaches combining AI-based prediction with experimental validation; pharmaceutical researchers interested in targeting TDP-43 assemblies for therapeutic intervention
- **Major strengths** 1) The study addresses a significant gap in understanding TDP-43 CR structure and function, which has been elusive due to technical challenges. 2) The multi-technique approach is well-designed and complementary, with each method providing distinct constraints. 3) The correlation between biophysical measurements and cellular functional assays strengthens the biological relevance of the findings. 4) The use of modern force fields validated against NMR data for IDP simulations is methodologically sound. 5) The manuscript is clearly written and the figures are informative.
- **Major Concerns** See detailed items below.
- **Minor Comments** See detailed items below.
- **Technical failings that need to be addressed before the case is established** R1-M1 (AUC interpretation), R1-M2 (AF2-Multimer reliability), R1-M3 (correlation analysis), R1-M4 (cellular assay specificity)
- **Assessment against Nature-style criteria** **Originality**: High. The study provides novel structural models for TDP-43 CR multimerization, which has been a missing piece in understanding TDP-43 function and dysfunction. The integrative approach combining AF2-Multimer with extensive experimental validation is innovative. **Scientific importance**: High. TDP-43 pathology is central to multiple neurodegenerative diseases, and understanding the native structure of the CR is critical for understanding both normal function and disease mechanisms. The findings have potential therapeutic implications. **Interdisciplinary readership**: Moderate to high. The work bridges structural biology, biophysics, cell biology, and neurodegeneration research. The methods will be of interest to computational biologists and experimentalists alike. **Technical soundness**: Moderate. While the overall approach is sound, several technical concerns need to be addressed, particularly regarding AUC data interpretation and the use of AF2-Multimer for dynamic assemblies. **Readability for nonspecialists**: Good. The manuscript is well-structured and explains concepts clearly, though some sections assume familiarity with NMR and simulation techniques.
- **Recommendation posture** Supportive if technical concerns are resolved. The core findings are potentially important, but the current evidence does not fully establish the tetrameric model as the definitive native state of TDP-43 CR. The manuscript would benefit from additional experimental validation and more cautious interpretation of some results.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors claim that SV-AUC data support the presence of tetrameric assemblies, with a monomer-dimer-tetramer model providing the best fit to the sedimentation data.
- **Evidence pointer** Figure 3, Supplementary Table 1, Methods section "Analytical ultracentrifugation"
- **Concern** The interpretation of the SV-AUC data is not fully convincing. The authors state that a "two state" monomer-dimer or monomer-trimer model and "three state" monomer-dimer-trimer models resulted in poorer fits, but the details of these fits are not provided. The distinction between a monomer-dimer-tetramer model and a monomer-tetramer model, or a model with continuous self-association, is not clearly demonstrated. Additionally, the authors note that the s-value for the faster-sedimenting species is approximately 2x that of the monomer, which they interpret as suggestive of a tetramer, but this scaling argument is not rigorous for non-spherical or hydrated species. The confidence intervals for the fitted dissociation constants are wide, and the authors acknowledge that the multimeric form could not be saturated, which limits the reliability of the derived equilibrium constants.
- **Why it matters** The tetrameric stoichiometry is a central claim of the manuscript. If the AUC data do not unambiguously support a tetramer, the structural models and subsequent interpretations are weakened. The distinction between a tetramer and other higher-order assemblies, or a continuum of oligomeric states, is critical for the proposed structural model.
- **Resolution test** Provide a more detailed comparison of alternative models, including statistical measures of fit quality (e.g., Akaike or Bayesian information criteria). Show residual plots for each model. Consider performing sedimentation equilibrium experiments to obtain molecular weights more directly. If possible, use a combination of techniques (e.g., mass photometry or native mass spectrometry) to independently verify the stoichiometry.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors use AF2-Multimer predictions as starting configurations for MD simulations and claim that the resulting tetrameric model is stable and consistent with experimental data.
- **Evidence pointer** Figure 5, Methods section "AlphaFold-multimer predictions" and "All-atom MD simulations"
- **Concern** The use of AF2-Multimer for predicting structures of dynamic, weakly-associated IDP assemblies is questionable. AF2-Multimer is trained on stable, well-folded complexes and its reliability for transient, low-affinity interactions is not well-established. The authors acknowledge low confidence scores for the predicted multimers, which raises concerns about the validity of using these as starting points. The selection of specific models for MD simulations is not clearly justified. Furthermore, the MD simulations are relatively short (microsecond timescale) for assessing the stability of a tetrameric assembly, and the authors do not demonstrate convergence of the simulations.
- **Why it matters** The structural models presented in the manuscript are derived from AF2-Multimer predictions refined by MD. If the initial predictions are unreliable, the resulting models may not represent the true native state. The stability of the tetramer in MD simulations is used as evidence for its biological relevance, but this is only meaningful if the simulations are sufficiently long and the starting structures are plausible.
- **Resolution test** Provide a more rigorous justification for the selection of AF2-Multimer models, including analysis of the confidence metrics and comparison with alternative prediction methods. Perform longer MD simulations (e.g., >10 μs) and demonstrate convergence of key structural properties. Consider using enhanced sampling techniques to explore the free energy landscape of tetramerization. Validate the models against additional experimental data, such as mutagenesis data beyond those already used.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Evidence strength
- **Claim pointer** The authors report a strong correlation (Pearson r = 0.7) between per-residue intermolecular contacts from dimer simulations and experimental phase separation data (csat) from alanine mutagenesis.
- **Evidence pointer** Figure 2G
- **Concern** The correlation analysis between simulation-derived contacts and experimental csat values is presented as supporting evidence for the relevance of the simulated contacts. However, the analysis includes only a limited number of data points (the alanine variants tested), and the correlation is driven by a few key residues. The statistical significance of the correlation is not reported, and the possibility of confounding factors (e.g., effects of mutations on monomer stability or solubility) is not fully addressed. Additionally, the use of dimer simulations to predict contacts relevant for higher-order assemblies (tetramers) is an approximation that needs justification.
- **Why it matters** The correlation is used to link the computational models to the experimental phase separation data. If the correlation is weak or driven by artifacts, the connection between the structural models and the functional data is weakened.
- **Resolution test** Report the statistical significance of the correlation (p-value). Perform a more comprehensive analysis including all available mutagenesis data. Consider using partial correlations to control for potential confounding factors. Justify the use of dimer simulations for predicting contacts in higher-order assemblies, or perform the analysis using tetramer simulations.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Evidence strength
- **Claim pointer** The authors claim that mutations that disrupt phase separation (W334A, L330A) reduce TDP-43 nuclear retention, while mutations that enhance phase separation promote nuclear retention, linking the structural findings to cellular function.
- **Evidence pointer** Figure 2H, Supplementary Figure 4
- **Concern** The nuclear retention experiments are performed in a heterologous overexpression system (HEK293 cells with inducible HA-tagged TDP-43). While the authors argue that this system minimizes overexpression artifacts, the relevance to endogenous TDP-43 in neurons is not directly demonstrated. The correlation between phase separation propensity and nuclear retention is based on a small number of mutants, and the effects are modest for some variants. The authors note that some differences do not reach statistical significance, which limits the strength of the conclusions. Additionally, the mechanism by which altered phase separation affects nuclear retention is not directly tested.
- **Why it matters** The cellular data are used to argue for the functional relevance of the structural findings. If the cellular assays are not robust or specific, the link between the in vitro biophysics and in vivo function is weakened.
- **Resolution test** Provide additional validation in a more physiologically relevant system, such as primary neurons or iPSC-derived neurons. Test additional mutants to strengthen the correlation. Directly measure the size of TDP-43 complexes in cells (e.g., using FCS or single-molecule tracking) to link phase separation to nuclear retention. Address the mechanism by which phase separation affects nuclear retention.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Figure 1
- **Evidence pointer** Figure 1B-D
- **Issue** The comparison of NMR spectra at pH 6.1 and pH 7.0 with 150 mM NaCl is shown, but the authors do not provide a quantitative analysis of the chemical shift differences. The statement that the spectra are "very similar" is subjective.
- **Required correction** Provide a quantitative measure of chemical shift differences (e.g., weighted average chemical shift perturbation) for all residues, and state a threshold for significance.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Methods
- **Evidence pointer** Methods section "Analytical ultracentrifugation"
- **Concern** The details of the AUC data analysis are incomplete. The authors mention "direct Lamm equation modeling" but do not provide sufficient information about the fitting procedure, such as the software settings, the number of iterations, and the criteria for assessing fit quality.
- **Required Correction** Provide a more detailed description of the AUC data analysis, including the fitting model, the parameters that were floated or fixed, and the statistical measures used to compare models.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Interpretation
- **Affected element** Discussion
- **Evidence pointer** Discussion section
- **Issue** The authors suggest that pharmacological stabilization of the helical tetramer could be a therapeutic avenue. This is speculative and not directly supported by the data presented.
- **Required Correction** Soften this claim or provide additional discussion of the potential challenges and uncertainties associated with this approach.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Technical detail
- **Affected element** Methods
- **Evidence pointer** Methods section "All-atom MD simulations"
- **Concern** The authors state that the AMBER03ws force field was selected based on its ability to reproduce NMR-derived helical propensities. However, the validation is only briefly mentioned and the specific comparison is not shown.
- **Required Correction** Provide a more detailed description of the force field validation, including a comparison of simulated and experimental observables (e.g., chemical shifts, J-couplings) for the monomeric TDP-43310-350.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Figure 5
- **Evidence pointer** Figure 5E
- **Issue** The representative structure of the tetramer is shown, but the orientation and labeling of the chains are not clear. It is difficult to discern the specific contacts described in the text.
- **Required Correction** Provide a clearer representation of the tetramer structure, with each chain labeled and key contact residues highlighted.

## Risk / unsupported claims
- The claim that the tetramer is the "most likely native form" of the CR is not fully supported by the data, as the AUC analysis could not distinguish between a monomer-dimer-tetramer model and a monomer-tetramer model with high confidence.
- The claim that the structural models "provide critical information required to understand the early steps in functional TDP-43 CTD assembly" is somewhat overstated, as the functional relevance is inferred from indirect assays.
- The claim that the CR must convert to β-sheet aggregates to form pathogenic fibrils is based on prior literature and is not directly tested in this manuscript.
- The suggestion that stabilizing the helical tetramer could be a therapeutic strategy is speculative and not supported by direct experimental evidence.
- The correlation between per-residue contacts from dimer simulations and csat values is presented as strong evidence, but the statistical significance and robustness of this correlation are not fully established.