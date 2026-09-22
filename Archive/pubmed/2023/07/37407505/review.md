## Review setup
- **Input scope** Full manuscript text, including abstract, introduction, materials and methods, results and discussion, conclusions, and supplementary material description.
- **Assessment boundary** Scientific content, methodological rigor, validity of claims, and presentation quality. Not assessed: editorial fit, ethical compliance, or data availability beyond what is stated.
- **Shared manuscript claim summary** The authors combine single-molecule FRET (smFRET) experiments on 14 doubly labeled α-synuclein constructs with coarse-grained molecular dynamics (CG-MD) simulations to characterize intra- and inter-regional interactions in this intrinsically disordered protein. They report a global Flory scaling exponent of ν = 0.57 under physiological salt conditions, local compaction in the NAC region (residues 56–90) driven by hydrophobic aliphatic contacts and cation–π interactions, and expansion of the C-terminal region (residues 90–140) due to electrostatic repulsion and proline-induced chain stiffness. The authors claim excellent agreement between experiments and simulations, and propose that the combined approach can identify regions with secondary structure propensity.
- **Visible evidence base** Abstract, full methods section for smFRET and CG-MD, results and discussion with reference to Figures 1–3 and Supplementary Figures S1–S4, and conclusions. No raw data, no supplementary figures or tables, no simulation parameter files, no analysis code, and no statistical details are provided in the supplied material.
- **Missing materials affecting confidence** Supplementary figures (S1–S4) referenced in the text are not provided. Raw smFRET burst data, per-construct distance values, uncertainty estimates, simulation trajectories, force field parameter files, and convergence criteria are absent. The exact fitting procedures and error analysis for the Flory scaling exponent and persistence length are not fully described. No information on replicate measurements or reproducibility is given.

## Reviewer
- **Overall assessment** This manuscript presents a well-motivated and technically ambitious study that combines two complementary approaches to probe the conformational properties of α-synuclein at residue-level resolution. The experimental design using 14 FRET constructs spanning the full protein is thoughtful, and the global analysis framework based on Flory theory is appropriate. The agreement between smFRET and CG-MD simulations is encouraging and, if robust, would constitute a useful methodological contribution. However, the current manuscript has several significant gaps that prevent full evaluation of the central claims. The most critical issues are the lack of quantitative uncertainty analysis on the derived scaling exponent and persistence length, the absence of the referenced supplementary figures, and insufficient detail on how the CG-MD model was validated for this specific system. The claim that the NAC region compaction results specifically from valine/alanine hydrophobic contacts and lysine–tyrosine cation–π interactions is based on simulation contact maps, but the statistical significance and specificity of these contacts are not demonstrated. The solvent-dependent experiments are presented briefly and would benefit from more thorough analysis. Overall, the study is potentially valuable, but the evidence as presented is not sufficient to fully establish all conclusions.
- **Who would be interested in the results, and why** Researchers studying intrinsically disordered proteins, particularly those interested in α-synuclein structure and aggregation, would find this work relevant. The methodological combination of smFRET with CG-MD simulations will appeal to biophysicists and computational chemists working on IDP conformational ensembles. The findings on regional compaction and expansion may inform studies on α-synuclein function and pathology. The proposed approach for identifying secondary structure propensity regions could be of interest to the broader IDP community.
- **Major strengths** The study addresses an important question about the molecular determinants of IDP conformation using a combination of experimental and computational methods. The use of 14 FRET constructs spanning the entire protein is a comprehensive approach. The global analysis framework that simultaneously uses intensity and lifetime data to determine the scaling exponent is methodologically sound. The agreement between experiments and simulations, if confirmed, would strengthen confidence in both approaches. The identification of specific interaction types (hydrophobic, cation–π) contributing to regional compaction is mechanistically informative.
- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors claim a global Flory scaling exponent of ν = 0.57 and a persistence length of lp = 0.49 nm for α-synuclein under physiological salt conditions.
- **Evidence pointer** Results and Discussion, Figure 2b and 2c; location not provided for specific data points
- **Concern** The determination of ν relies on minimizing the difference between Rint and Rτ across all constructs. However, the manuscript does not provide any uncertainty estimates for these derived quantities. No confidence intervals, standard errors, or bootstrap analyses are reported. The fitting procedure for lp is described, but the quality of the fit, residuals, or parameter uncertainties are not shown. Without this information, it is impossible to assess whether ν = 0.57 is statistically distinguishable from, for example, ν = 0.5 (theta solvent) or ν = 0.588 (self-avoiding walk in three dimensions).
- **Why it matters** The central conclusion that physiological salt is a good solvent for α-synuclein rests on the precision of ν. If the uncertainty in ν is large, the claim of "good solvent" conditions is not established. Similarly, the persistence length is used to interpret regional deviations, and its uncertainty propagates into the interpretation of ΔR values.
- **Resolution test** Provide confidence intervals or standard errors for ν and lp, obtained through bootstrapping or Monte Carlo error propagation. Show the fit residuals and the distribution of per-construct distances. State the number of independent measurements per construct and the reproducibility across replicate experiments.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors claim "excellent agreement" between smFRET measurements and CG-MD simulations for the mean distances between labeling positions across all constructs.
- **Evidence pointer** Results and Discussion, Figure 2c; location not provided for quantitative comparison
- **Concern** The agreement between experiments and simulations is stated qualitatively, but no quantitative comparison metric is provided. The figure shows data points and a fit, but the level of agreement is not quantified (e.g., root-mean-square deviation, correlation coefficient, or per-construct percent difference). Moreover, the CG-MD simulations were performed on sequences with cysteine mutations, and the authors state that no parameters were adjusted, but the sensitivity of the results to the specific choice of CG model parameters is not discussed. The implicit-solvent model may not capture all relevant interactions, and the agreement could be fortuitous or model-dependent.
- **Why it matters** The claim of excellent agreement is a cornerstone of the paper, as it justifies using the simulations to interpret the experimental data at the molecular level. Without a quantitative measure, the strength of this agreement cannot be evaluated. If the agreement is only moderate for some constructs, the molecular interpretation may be unreliable.
- **Resolution test** Provide a quantitative comparison metric (e.g., RMSD between experimental and simulated distances, with per-construct breakdown). Show the distribution of simulated distances and compare to experimental uncertainties. Discuss the sensitivity of the simulated distances to CG model parameters, and ideally perform a parameter scan or use an ensemble of model parameters.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence sufficiency
- **Claim pointer** The authors attribute NAC region compaction to "hydrophobic aliphatic contacts, mostly between valine and alanine residues, and cation–π interactions between lysine and tyrosine."
- **Evidence pointer** Results and Discussion, Figure 3b and Supplementary Figure S4; location not provided for contact maps
- **Concern** The contact map analysis is presented as the basis for identifying the specific interactions responsible for compaction. However, the supplementary figures that would show these contact maps are not provided in the supplied material. The text states that valine and alanine contacts are most abundant and that cation–π interactions between lysine and tyrosine are increased, but no quantitative data (e.g., contact frequencies, enrichment relative to random expectation, or statistical significance) are given. It is unclear whether these contacts are specific to the NAC region or simply reflect the amino acid composition of that region.
- **Why it matters** The molecular mechanism proposed for NAC compaction is a key finding of the paper. Without the actual contact maps and quantitative analysis, the claim is not verifiable. The distinction between contacts that are merely frequent due to abundance versus those that are specifically enriched and functionally relevant is critical.
- **Resolution test** Provide the contact maps (as in Supplementary Figure S4) with quantitative contact frequencies. Show enrichment of specific contact types relative to a composition-matched random coil model. Report statistical significance (e.g., z-scores or p-values) for the identified contacts. If possible, perform control simulations with modified interaction parameters to test causality.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Technical soundness
- **Claim pointer** The authors state that "the protein remains flexible in these solvents (τDA/τD – EFRET > 0)" for low salt, urea, and methanol conditions.
- **Evidence pointer** Results and Discussion, Figure 3c; location not provided for the data
- **Concern** The solvent-dependent experiments are presented as a test of how different regions respond to changes in solvent quality. However, the analysis is limited to reporting ΔEFRET values, and the interpretation is qualitative. For the methanol condition, the authors note the appearance of a large population of slowly diffusing particles, indicating aggregation, but the analysis of the remaining monomeric fraction is based on a small number of events. The statistical power of these measurements is not discussed, and no error bars are shown in the figure.
- **Why it matters** The solvent-dependent results are used to support the claim that different regions have different sensitivities to solvent conditions. If the measurements are underpowered or the analysis is biased by the selection of the monomeric fraction, the conclusions may not be robust.
- **Resolution test** Report the number of bursts analyzed per condition, the fraction of events excluded due to aggregation, and the statistical uncertainty in ΔEFRET. Show the full distribution of τDA/τD versus EFRET for each solvent condition. Consider whether the observed changes are consistent with the proposed mechanisms (e.g., charge screening in low salt, denaturation in urea).

- **Concern ID** R1-M5
- **Severity** Major
- **Blocking** No
- **Axis** Scientific importance
- **Claim pointer** The authors propose that "fast CG-MD simulations alongside future smFRET experiments on IDPs can be used to identify regions in these proteins with higher propensities for secondary structure transitions."
- **Evidence pointer** Conclusions; location not provided
- **Concern** This is a forward-looking claim about the general applicability of the approach. While plausible, the manuscript does not provide a demonstration of this capability. The only example of a discrepancy between experiment and simulation is the αS56–90 construct, which the authors attribute to hydrogen bonding and secondary structure propensity. However, this is a single case, and the authors do not show how the method would be used prospectively to identify such regions in other IDPs.
- **Why it matters** The broader significance of the work depends in part on this methodological claim. If the approach is to be adopted by others, a clearer demonstration of its predictive power is needed.
- **Resolution test** Provide a more detailed analysis of the αS56–90 discrepancy, including a comparison with all-atom simulations or experimental secondary structure propensity data. Discuss how the discrepancy between CG-MD and smFRET could be used as a diagnostic for secondary structure propensity, and outline criteria for when this would be reliable.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Methods, FRET labeling
- **Evidence pointer** Methods section, "FRET Labeling of αS Synuclein"; location not provided
- **Issue** The manuscript states that "two amino acids were replaced with cysteines" but does not specify which amino acids were replaced in each of the 14 constructs. The construct names (e.g., αS9–18) indicate the positions of the labels, but the original residues are not listed.
- **Required correction** Provide a table listing the specific amino acid substitutions for each construct, including the wild-type residue, position, and cysteine replacement.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Technical detail
- **Affected element** Methods, smFRET analysis
- **Evidence pointer** Methods section, "smFRET Instrumentation, Data Collection, and Analysis"; location not provided
- **Issue** The correction procedure for the FRET efficiency and donor lifetime is referenced to Hellenkamp (ref 31), but the specific correction factors used (e.g., leakage, direct excitation, detection efficiency) are not reported. The manuscript states that cross-excitation of Alexa Fluor 568 by 485 nm excitation was neglected, but the justification for this assumption is not given.
- **Required correction** Report the numerical values of the correction factors used, or state that they are provided in the supplementary material. Justify the neglect of cross-excitation, or provide an estimate of its magnitude.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Reproducibility
- **Affected element** Methods, MD simulations
- **Evidence pointer** Methods section, "MD Simulations"; location not provided
- **Issue** The manuscript states that "an updated 1-bead-per-amino-acid (1BPA) model" was used, with updates to nonbonded parameters developed by Driver and Onck. However, the specific parameter values or the nature of the updates are not described. The reference to previous work (refs 35–37) is helpful, but the reader cannot assess what is new in this work.
- **Required correction** Provide a description of the updated parameters, or state that they are available in a repository or supplementary file. If the updates are described in a separate publication, clarify the relationship to that work.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Presentation
- **Affected element** Results and Discussion, Figure 2d
- **Evidence pointer** Results and Discussion, Figure 2d; location not provided
- **Issue** The ΔR plot in Figure 2d is used to identify regional deviations from global scaling. However, the statistical significance of these deviations is not assessed. It is unclear whether the deviations for specific constructs are within experimental uncertainty or represent genuine regional effects.
- **Required correction** Add error bars to the ΔR values, derived from the uncertainty in Rint and Rτ. Indicate which deviations are statistically significant.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Results and Discussion, solvent experiments
- **Evidence pointer** Results and Discussion, Figure 3c; location not provided
- **Issue** The solvent-dependent experiments are described for three constructs (αS9–42, αS42–90, αS90–140), but the rationale for choosing these specific constructs is not stated. The authors mention that the protein remains flexible in all solvents, but the quantitative changes in EFRET are not discussed in detail.
- **Required correction** State the rationale for the construct selection. Provide a more detailed interpretation of the ΔEFRET values, including whether the changes are consistent with the expected effects of each solvent on the specific region.

- **Concern ID** R1-m6
- **Severity** Minor
- **Axis** Language
- **Affected element** Conclusions
- **Evidence pointer** Conclusions; location not provided
- **Issue** The phrase "the soltuion is globally a good solvent" contains a typographical error ("soltuion" instead of "solution").
- **Required correction** Correct the typographical error.

## Risk / unsupported claims
- The claim of "excellent agreement" between smFRET and CG-MD simulations is not quantitatively supported; no comparison metric or uncertainty analysis is provided.
- The specific molecular interactions (hydrophobic valine/alanine contacts, lysine–tyrosine cation–π interactions) proposed to drive NAC compaction are not supported by the provided evidence, as the relevant contact maps (Supplementary Figure S4) are not included in the supplied material.
- The global Flory scaling exponent ν = 0.57 and persistence length lp = 0.49 nm are reported without uncertainty estimates, making it impossible to assess the precision of these values or the robustness of the "good solvent" conclusion.
- The statement that "the protein remains flexible in these solvents" is based on qualitative inspection of τDA/τD versus EFRET plots, without statistical testing or quantitative criteria for flexibility.
- The claim that the approach can identify regions with secondary structure propensity is speculative and not demonstrated beyond a single construct (αS56–90).
- The solvent-dependent results for methanol are based on a small fraction of monomeric particles after aggregation, and the statistical power of these measurements is not discussed.
- The neglect of cross-excitation of the acceptor dye is stated without justification or quantitative estimate of its potential impact on the measured FRET efficiencies.