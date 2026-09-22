## Review setup
- **Input scope** Full manuscript text (abstract, introduction, methods, results, discussion, supporting material references)
- **Assessment boundary** Scientific content and technical soundness as presented in the provided text; no external validation of data or code
- **Shared manuscript claim summary** The authors present an integrative approach combining metadynamics MD simulations, NMR spectroscopy, and SAXS to characterise the cis and trans proline conformers of the ORF6 C-terminal region from SARS-CoV-2. They report convergence of proline isomerisation sampling in two force fields, identify AMBER03ws as most accurate against experimental data, and use Bayesian/maximum entropy reweighting to refine ensembles. They conclude the approach is broadly applicable to disordered proteins with slow conformational transitions.
- **Visible evidence base** Abstract, introduction, materials and methods, results, discussion, figure legends referenced in text (Figs 1-5, S1-S17), tables referenced (Tables S1-S2)
- **Missing materials affecting confidence** Full figures and figure legends, supporting information document, experimental NMR parameters, SAXS data processing details, convergence analysis plots, code repository contents

## Reviewer
- **Overall assessment** This manuscript presents a technically ambitious integration of enhanced-sampling MD simulations with NMR and SAXS experiments to characterise proline cis/trans isomerisation in a disordered peptide. The work addresses a genuinely challenging problem in IDP biophysics, and the combination of techniques is appropriate and timely. However, the manuscript as presented has several significant gaps in methodological detail and validation that prevent full assessment of the claims. The central conclusion that AMBER03ws most accurately predicts cis-proline populations rests on a single experimental comparison, and the statistical treatment of uncertainties in both simulation and experiment requires clarification. The work is potentially important but currently not fully established from the provided evidence.

- **Who would be interested in the results, and why** Researchers in the IDP biophysics community, particularly those working on proline isomerisation and its role in disordered protein function. The methodological comparison of force fields for disordered proteins will interest computational biophysicists. The specific application to SARS-CoV-2 ORF6 may attract virologists studying host-pathogen interactions, though this is a secondary aspect. The integrative approach combining enhanced sampling with NMR and SAXS will interest method developers in structural biology.

- **Major strengths**  
  1. The combination of multiple complementary techniques (metadynamics, NMR, SAXS) to address a single question is well conceived and represents a rigorous approach to a difficult problem.
  2. The use of multiple force fields optimised for disordered proteins, with explicit assessment of their performance against experimental data, is a valuable contribution.
  3. The application of BME reweighting to refine ensembles against SAXS data is appropriate and well executed.
  4. The experimental work includes careful controls, such as the comparison of labelled and unlabelled peptides and the use of multiple NMR observables.
  5. The authors are appropriately cautious in their interpretation, acknowledging limitations of force fields and the need for further validation.

- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** "A good agreement between the cis-P57 populations predicted from metadynamics simulations in AMBER03ws was observed with populations obtained from experimental NMR data."
- **Evidence pointer** Results section, Fig. 1D, Fig. 2D
- **Concern** The central claim that AMBER03ws accurately predicts cis-proline populations is based on a comparison between simulation-derived populations and NMR-derived populations, but the manuscript does not provide a clear description of how uncertainties are propagated in either measurement. The NMR population is reported as 8.8 ± 2.5% at 37°C, while the AMBER03ws population is reported as 13 ± 2% after BME reweighting. These values differ by approximately 1.5 standard deviations, which may or may not be statistically significant depending on the correlation between measurements. The manuscript does not report the raw simulation populations before reweighting, nor does it provide confidence intervals for the simulation-derived populations that account for the finite sampling and the BME reweighting procedure.
- **Why it matters** The identification of AMBER03ws as the most accurate force field is a central conclusion of the paper. If the statistical comparison is not robust, this conclusion is not supported. Furthermore, the manuscript does not report the cis-proline populations from the other force fields after reweighting, making it impossible to assess whether the superiority of AMBER03ws is maintained after refinement.
- **Resolution test** Provide a clear statistical comparison between simulation and experiment, including confidence intervals for both. Report the cis-proline populations for all force fields before and after BME reweighting. Perform a formal statistical test (e.g., a Bayesian model comparison or a bootstrap analysis) to assess whether AMBER03ws is significantly better than the alternatives.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** "We employed metadynamics to enhance sampling, using various local and global CVs, including those on the P57 ζ and ψ angles."
- **Evidence pointer** Materials and Methods, Results section, Fig. S3A-C
- **Concern** The manuscript states that convergence was assessed by blocking analysis for every CV, and that convergence was observed for all CVs except the P57 ζ dihedral angle in the AMBER99SB-disp force field. However, the manuscript does not provide the blocking analysis results, nor does it describe the criteria used to determine convergence. The statement that "convergence was reached" for the ζ dihedral in AMBER03ws and CHARMM36m is not supported by any quantitative measure. Furthermore, the manuscript does not report the free energy surface for the ζ dihedral angle, which would be essential to verify that the cis and trans states are properly sampled and that the barrier between them is adequately explored.
- **Why it matters** The reliability of the entire simulation-based analysis depends on the convergence of the metadynamics simulations. If the ζ dihedral angle is not fully converged, the cis-proline populations derived from the simulations are unreliable, and the comparison with experiment is meaningless. The manuscript's claim that convergence was achieved is not verifiable from the provided evidence.
- **Resolution test** Provide the blocking analysis plots for all CVs in all force fields, with clear criteria for convergence. Show the free energy surface as a function of the ζ dihedral angle for each force field, demonstrating that the cis and trans minima are well-sampled and that the barrier is adequately explored. If convergence is not fully achieved, discuss the implications for the reported populations.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Reproducibility
- **Claim pointer** "We used the BME software to update the metadynamics weights to better match experimental SAXS data."
- **Evidence pointer** Materials and Methods, Results section, Fig. 3A
- **Concern** The BME reweighting procedure is described only briefly, and the manuscript does not provide sufficient detail to reproduce the analysis. Specifically, the manuscript does not report the uncertainty in the SAXS data used for reweighting, the choice of prior (i.e., the metadynamics weights), the regularisation parameter, or the convergence criteria for the BME optimisation. The manuscript also does not report the effective number of samples after reweighting, which is critical to assess whether the reweighted ensemble is statistically meaningful.
- **Why it matters** BME reweighting can produce overfit ensembles if the uncertainty in the experimental data is underestimated or if the regularisation is not appropriate. Without these details, the reweighted ensembles cannot be evaluated, and the reported cis-proline populations after reweighting are not reproducible.
- **Resolution test** Provide a detailed description of the BME reweighting procedure, including the uncertainty in the SAXS data, the prior, the regularisation parameter, and the convergence criteria. Report the effective sample size after reweighting and assess the sensitivity of the results to the choice of regularisation.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Scientific importance
- **Claim pointer** "Our findings suggest that both the cis-P57 and trans-P57 conformations of ORF6 CTR are extremely dynamic and that interdisciplinary approaches combining both multi-scale computations and experiments offer avenues to explore highly dynamic states that cannot be reliably characterised by either approach in isolation."
- **Evidence pointer** Abstract, Discussion
- **Concern** The claim that the approach is broadly applicable to disordered proteins with slow conformational transitions is not fully supported by the data. The manuscript demonstrates the approach on a single 21-residue peptide with a single proline residue. While the results are encouraging, the generalisability of the approach to larger systems, multiple proline residues, or systems with more complex energy landscapes is not established. The authors acknowledge this limitation in the Discussion, but the claim in the abstract is stronger than the evidence supports.
- **Why it matters** The significance of the work depends on its generalisability. If the approach only works for small, simple systems, its impact is limited. The manuscript should either provide evidence of generalisability or temper the claim.
- **Resolution test** Either provide additional examples demonstrating the applicability of the approach to other systems, or revise the claim to be more modest and clearly state the limitations of the approach.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Abstract
- **Evidence pointer** Abstract
- **Issue** The abstract states "ORF6 CTR" without defining the abbreviation. While the introduction defines it, the abstract should be self-contained.
- **Required correction** Define "ORF6 CTR" in the abstract, e.g., "the C-terminal region of ORF6 (ORF6 CTR)".

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Technical soundness
- **Affected element** Materials and Methods, NMR spectroscopy
- **Evidence pointer** Materials and Methods
- **Issue** The manuscript states that NMR experiments were recorded at 15°C and 37°C, but does not provide details on the NMR spectrometer, pulse sequences, or data processing parameters. This information is essential for reproducibility.
- **Required correction** Provide details on the NMR spectrometer, pulse sequences, and data processing parameters, or refer to a previous publication where these details are described.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Results, Fig. 2D
- **Evidence pointer** Fig. 2D
- **Issue** The manuscript reports cis-proline populations from NMR at 15°C and 37°C, but does not specify which residues were used for the population analysis. The text mentions residues E55, Q56, M58, and E59, but it is unclear whether all four residues were used or only a subset.
- **Required correction** Specify which residues were used for the population analysis and whether the populations were averaged over these residues or reported individually.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Reproducibility
- **Affected element** Data availability
- **Evidence pointer** Data availability
- **Issue** The manuscript states that code is available on GitHub, but the repository is not described in detail. It is unclear what code is included (e.g., simulation input files, analysis scripts, BME reweighting code).
- **Required correction** Provide a brief description of the contents of the GitHub repository, including the types of files and any dependencies.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Discussion
- **Evidence pointer** Discussion
- **Issue** The Discussion mentions "the ongoing accumulation of data will further enhance the accuracy of force fields" but does not provide specific examples or references to support this statement.
- **Required correction** Either provide specific examples of recent force field improvements or remove the statement.

## Risk / unsupported claims
- The claim that AMBER03ws most accurately predicts cis-proline populations is not fully supported due to insufficient statistical comparison (R1-M1).
- The claim that convergence was achieved for the proline isomerisation sampling is not verifiable from the provided evidence (R1-M2).
- The claim that the approach is broadly applicable to disordered proteins with slow conformational transitions is not fully supported by the single example presented (R1-M4).
- The statement that "the cis-P57 conformation is enthalpically disfavoured but entropically favoured" is based on a Van't Hoff analysis, but the manuscript does not provide the raw data or the goodness-of-fit for the linear regression, making it difficult to assess the reliability of the reported ΔH and ΔS values.
- The manuscript states that "all experimentally-determined chemical shifts were within the CamShift error" but does not provide the actual comparison data or the CamShift error estimates, making this claim unverifiable.