## Review setup
- **Input scope** Full manuscript text including abstract, introduction, results, discussion, methods, and supplementary figure/table references
- **Assessment boundary** Scientific claims, methodological soundness, data interpretation, and internal consistency based solely on the provided manuscript text
- **Shared manuscript claim summary** The authors report that reconfiguration times of 16 intrinsically disordered linker proteins of identical length but diverse sequence are nearly independent of sequence, despite large variations in chain dimensions. They propose a "dynamical buffering" mechanism where compensating effects of chain compaction and reduced intrachain diffusion result in approximately invariant reconfiguration times.
- **Visible evidence base** Experimental nsFCS and FRET data (referenced from prior work), all-atom explicit-solvent simulations of all 16 IDRs with and without FRET dyes, SAXS comparisons for four IDRs, one-dimensional diffusion model analysis, salt-bridge reweighting analysis, Bayesian reweighting analysis
- **Missing materials affecting confidence** Supplementary figures and tables (S1-S8), experimental FRET efficiency values, SAXS experimental curves, simulation trajectory details, specific numerical values for reconfiguration times and uncertainties, viscosity-dependent data for dCh-

## Reviewer

- **Overall assessment** This manuscript presents a systematic and rigorous investigation of sequence-dependent dynamics in intrinsically disordered proteins. The combination of single-molecule FRET, nsFCS, and long all-atom explicit-solvent simulations across a carefully selected set of 16 IDRs of identical length is a significant methodological achievement. The central observation, that reconfiguration times are nearly invariant despite large variations in chain dimensions, is surprising and potentially important. The proposed "dynamical buffering" mechanism, supported by a one-dimensional diffusion model analysis, provides a plausible and testable explanation. However, several technical aspects require clarification and additional analysis before the case is fully established, particularly regarding the quantitative accuracy of the diffusion model, the treatment of dye effects, and the statistical power of the correlation analyses.

- **Who would be interested in the results, and why** Researchers in the fields of intrinsically disordered proteins, protein biophysics, single-molecule spectroscopy, and molecular simulation would find this work of direct interest. The findings have implications for understanding how sequence encodes conformational dynamics in disordered proteins, which is relevant to protein function, signaling, and regulation. The methodological framework combining experiment and simulation could serve as a template for future studies of IDP dynamics. The concept of "dynamical buffering" may also interest evolutionary biologists studying sequence-function relationships in disordered regions.

- **Major strengths** The study addresses a fundamental and under-explored question about the sequence dependence of IDP dynamics. The experimental design, using 16 naturally occurring IDRs of identical length with diverse sequences, is well conceived. The combination of multiple complementary techniques (nsFCS, FRET, SAXS, all-atom simulations) provides a multi-faceted view. The explicit inclusion of FRET dyes in simulations and the careful validation against experimental data strengthen the credibility of the simulation results. The one-dimensional diffusion model provides a clear mechanistic framework for interpreting the observations. The salt-bridge reweighting analysis offers a concrete avenue for future force field improvement.

- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness of diffusion model analysis
- **Claim pointer** The authors claim that the one-dimensional diffusion model accurately reproduces the lack of correlation between reconfiguration times and FRET efficiencies observed experimentally.
- **Evidence pointer** Results section "Simulations Explain Lack of Correlation between Reconfiguration Times and Transfer Efficiencies"; Methods section "Computing Reconfiguration Times"
- **Concern** The diffusion model is fitted to simulation data and then used to compute reconfiguration times. The manuscript does not provide sufficient detail on how the model parameters are optimized, how many parameters are fitted, and whether the model is overparameterized. The statement that the model correlation functions "avoid the statistical noise seen in the long-time tails" of directly computed autocorrelation functions suggests that the model may be smoothing over important dynamical features. The validation of the model against directly computed correlation functions (Figure S6) is mentioned but not described in detail.
- **Why it matters** The central conclusion of the paper, that reconfiguration times are nearly invariant across sequences, depends critically on the accuracy of the diffusion model analysis. If the model is not adequately validated or if it imposes assumptions that bias the results toward similar reconfiguration times, the main claim would be weakened.
- **Resolution test** Provide a more detailed description of the model fitting procedure, including the number of free parameters, the optimization algorithm, and the convergence criteria. Show a quantitative comparison between model-predicted and directly computed correlation functions for at least a few representative IDRs, including error estimates. Demonstrate that the model can reproduce known dynamical features, such as the viscosity dependence for dCh-.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Statistical robustness of correlation analyses
- **Claim pointer** The authors report a weak correlation between reconfiguration times and FRET efficiencies (ρ_MC = 0.35 ± 0.21) and use this to support the claim of near-independence.
- **Evidence pointer** Results section "nsFCS Experiments Yield Very Similar Reconfiguration Times for a Diverse Set of Linker IDRs"; Figure 1C
- **Concern** The correlation coefficient of 0.35 with a standard error of 0.21 is not statistically distinguishable from zero at the 95% confidence level. The authors should report the p-value or confidence interval for this correlation. Additionally, with only 16 data points, the power to detect a moderate correlation is limited. The manuscript does not discuss whether the observed correlation is consistent with the expected relationship given the measurement uncertainties.
- **Why it matters** The claim that reconfiguration times are "almost independent of sequence" is a key finding. If the correlation is not statistically significant, the claim is weakened, and the interpretation of "dynamical buffering" as a precise compensation mechanism may be overstated.
- **Resolution test** Report the p-value or 95% confidence interval for the correlation coefficient. Perform a power analysis to determine the minimum detectable correlation given the sample size and measurement uncertainties. Discuss whether the observed correlation is consistent with the expected relationship given the measurement uncertainties.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Generalizability of the "dynamical buffering" mechanism
- **Claim pointer** The authors propose that "dynamical buffering" is a general mechanism that conserves reconfiguration times across sequences with varying chain dimensions.
- **Evidence pointer** Discussion section; Results section "Simulations Explain Lack of Correlation between Reconfiguration Times and Transfer Efficiencies"
- **Concern** The proposed mechanism is based on a single set of 16 IDRs of identical length (57 residues). The authors do not discuss whether this mechanism would hold for IDRs of different lengths, for IDRs with different amino acid compositions (e.g., more hydrophobic or more charged), or for IDRs that are more compact (approaching the globule limit). The authors briefly mention that the compensation may not extend to extreme compaction, but this is not quantified or tested.
- **Why it matters** The claim of "dynamical buffering" as a general principle for IDP dynamics would be strengthened by evidence that it applies beyond the specific set of sequences studied. Without such evidence, the mechanism may be specific to this particular set of IDRs.
- **Resolution test** Discuss the range of chain dimensions and sequence properties covered by the 16 IDRs and how this relates to the broader IDP sequence space. If possible, perform additional simulations or analyses on IDRs of different lengths or with more extreme compaction to test the generality of the mechanism.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Quantitative accuracy of simulation predictions
- **Claim pointer** The authors claim that the simulations reproduce experimental FRET efficiencies with "near-quantitative accuracy" and that inclusion of FRET dyes improves agreement.
- **Evidence pointer** Results section "All-Atom Molecular Simulations Reproduce Equilibrium FRET and SAXS Data for the Linker IDRs"; Figure 2A
- **Concern** The manuscript states that differences between simulation and experiment are within calculated standard errors for 8 of 16 proteins, which is close to the 68% expected for Gaussian-distributed errors. However, this means that for the other 8 proteins, the differences are outside the standard errors. The authors do not discuss whether these discrepancies are systematic (e.g., all in one direction) or random. The salt-bridge reweighting analysis suggests that some discrepancies may be due to over-stabilized salt bridges, but the quantitative impact of this correction on the reconfiguration times is not reported.
- **Why it matters** The validity of the dynamical conclusions drawn from simulations depends on the accuracy of the simulated ensembles. If the simulations systematically misrepresent the ensembles for a subset of sequences, the conclusions about reconfiguration times for those sequences may be unreliable.
- **Resolution test** Provide a more detailed analysis of the discrepancies between simulation and experiment, including whether they are systematic across sequences. Report the reconfiguration times computed from the salt-bridge reweighted ensembles and compare them to the uncorrected values. Discuss the implications of any systematic discrepancies for the main conclusions.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity of presentation
- **Affected element** Figure 1
- **Evidence pointer** Results section "nsFCS Experiments Yield Very Similar Reconfiguration Times for a Diverse Set of Linker IDRs"
- **Issue** The manuscript refers to "Figure 1A, B" and "Figure 1C" but does not describe the specific content of each panel in the text. The reader is left to infer what is shown in each panel.
- **Required correction** Add explicit descriptions of each panel in the figure legend and refer to them clearly in the text (e.g., "Figure 1A shows the FRET efficiency distributions, Figure 1B shows example distance distributions, and Figure 1C shows the correlation between reconfiguration time and FRET efficiency").

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Completeness of methods
- **Affected element** Force field parameters for dyes
- **Evidence pointer** Methods section "Force Field Parameters for Cy3B and CF660R"
- **Issue** The description of the dye parameter derivation is brief. The manuscript states that new charges were derived for the C2R residue and the chromophores, but does not provide details on the fitting procedure, the number of conformations used, or the level of theory beyond "Hartree-Fock with the 6-31G* basis set."
- **Required correction** Provide additional details on the charge derivation procedure, including the number of conformations sampled, the fitting method (e.g., RESP), and any validation of the derived parameters against experimental data or higher-level calculations.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Interpretation of viscosity-dependent measurements
- **Affected element** Results section "Simulations Explain Lack of Correlation between Reconfiguration Times and Transfer Efficiencies"; Figure S7
- **Issue** The viscosity-dependent measurements for dCh- are mentioned as evidence for negligible internal friction, but the results are not described in the main text. The reader is referred to Figure S7 without any summary of the findings.
- **Required correction** Add a brief description of the viscosity-dependent results in the main text, including the range of viscosities tested and the observed dependence of reconfiguration times on viscosity.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Discussion of limitations
- **Affected element** Discussion section
- **Issue** The discussion does not explicitly address the limitations of the study, such as the relatively small number of sequences (16), the use of a single force field, or the potential influence of the specific dye pair on the measured dynamics.
- **Required correction** Add a paragraph discussing the limitations of the study and how they might affect the generality of the conclusions.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Reproducibility
- **Affected element** Methods section "All-Atom Simulations"
- **Issue** The manuscript states that simulation trajectories are included in a Zenodo repository, but the specific accession number is only mentioned in the acknowledgements section. This information should be in the methods or data availability section.
- **Required correction** Move the Zenodo repository information to a dedicated data availability statement or include it in the methods section.

## Risk / unsupported claims
- The claim that "dynamical buffering" is a general mechanism for conserving reconfiguration times across IDR sequences is not fully supported by the data, as it is based on a single set of 16 IDRs of identical length. The generality of the mechanism is asserted but not tested.
- The statement that internal friction contributes no more than 10-15 ns to the reconfiguration time for the most compact variants is not directly supported by the data presented. This appears to be an inference from the observed buffering effect, but the quantitative bound is not derived or justified in the text.
- The claim that the simulations reproduce experimental FRET efficiencies with "near-quantitative accuracy" is partially supported, but the fact that 8 of 16 proteins show differences outside standard errors suggests that the accuracy is not uniform across the set.
- The assertion that the one-dimensional diffusion model provides a quantitatively accurate description of the chain dynamics is not fully validated, as the comparison between model predictions and directly computed correlation functions is only mentioned in a supplementary figure without detailed description.
- The statement that "including the dyes in the simulations yields closer correspondence to the measured FRET efficiencies" is supported by the data, but the claim that this is "in line with broader assessments of smFRET reliability" is an unsupported generalization.