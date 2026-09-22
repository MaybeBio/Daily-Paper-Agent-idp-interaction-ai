## Review setup
- **Input scope** Full manuscript text including abstract, introduction, results, discussion, methods, and supporting information references.
- **Assessment boundary** Scientific validity, methodological soundness, interpretation of results, and claims made regarding predictive accuracy of MD simulations for IDP ensembles.
- **Shared manuscript claim summary** The authors claim that modern MD force fields with residue-specific backbone potentials (ff99SBnmr2) combined with TIP4P-D water and replica exchange MD can produce highly realistic IDP ensembles that quantitatively reproduce experimental NMR relaxation data and global conformational properties without reweighting or post hoc corrections.
- **Visible evidence base** Figures 1-6 (described in text), supplementary figures S1-S5, supplementary tables S1-S5, equations 1-12, and comparison with published experimental data.
- **Missing materials affecting confidence** Actual figure images, supplementary figure images, supplementary tables, simulation parameter details beyond those summarized, experimental data files, and convergence metrics for REMD simulations.

## Reviewer
- **Overall assessment** This manuscript presents a compelling demonstration that the ff99SBnmr2 force field with TIP4P-D water can produce IDP ensembles that quantitatively match experimental NMR relaxation data and global conformational properties for two model IDPs. The work is technically sound in its core methodology and the comparison with experiment is thorough. However, several concerns regarding the interpretation of outlier trajectories, the statistical robustness of the ensemble comparisons, and the generalizability of the conclusions warrant careful consideration before the broader claims can be fully accepted.

- **Who would be interested in the results, and why** Researchers in the IDP biophysics community, computational chemists developing and validating force fields, NMR spectroscopists studying protein dynamics, and structural biologists interested in ensemble-based descriptions of disordered proteins. The demonstration that unbiased MD can reproduce experimental relaxation data without reweighting is of significant practical importance for the field.

- **Major strengths** The study addresses a critical validation gap for IDP simulations by comparing against NMR relaxation data that are sensitive to both amplitudes and timescales of motion. The use of multiple independent 1-μs trajectories provides a reasonable sampling strategy. The graph-theoretical analysis of contact networks is a novel and insightful approach to characterizing transient interactions. The comparison with polymer theory provides useful context for interpreting the global conformational properties.

- **Major Concerns**
  - **Concern ID** R1-M1
  - **Severity** Major
  - **Blocking** Yes
  - **Axis** Statistical robustness of ensemble comparisons
  - **Claim pointer** The authors claim that the MD ensembles "closely reproduce experimental data at the global conformational ensemble level" and that R1/R2 relaxation rates are in "close agreement with experiment."
  - **Evidence pointer** Figures 3A-3D, S2 Fig, S4 Table
  - **Concern** The comparison between simulated and experimental R1/R2 values is presented primarily through correlation coefficients and RMSE values. However, the statistical significance of these comparisons is not established. With only 10 independent trajectories, the uncertainty in the ensemble-averaged relaxation rates may be substantial, particularly for residues with slower dynamics. The authors note that 1-2 trajectories are outliers with more compact structures, but the impact of these outliers on the reported correlation coefficients and RMSE values is not quantified. Furthermore, the experimental uncertainties in the R1/R2 measurements are not reported, making it impossible to assess whether the observed discrepancies are within experimental error.
  - **Why it matters** The central claim of the paper is that the simulations quantitatively reproduce experimental data without reweighting. Without proper error analysis on both the simulation and experimental sides, this claim cannot be rigorously evaluated. If the agreement is within combined uncertainties, the claim is supported; if not, the discrepancies may indicate systematic force field inaccuracies that are being masked by averaging.
  - **Resolution test** Provide per-residue error bars for both simulated and experimental R1/R2 values, and perform a statistical test (e.g., chi-squared or reduced chi-squared) to assess whether the differences between simulation and experiment are within combined uncertainties. Report the impact of removing outlier trajectories on the correlation coefficients and RMSE values.

  - **Concern ID** R1-M2
  - **Severity** Major
  - **Blocking** Yes
  - **Axis** Interpretation of outlier trajectories
  - **Claim pointer** The authors state that "10-20% of the individual MD trajectories display the formation of secondary structures not observed in the experimental NMR data" and that these trajectories are "not representative of the other trajectories."
  - **Evidence pointer** Fig 4C and 4D, S2 Fig, S4 Table
  - **Concern** The identification of outlier trajectories is based on their disagreement with experimental data, and these trajectories are then excluded from the contact cluster analysis. This creates a circular argument: trajectories that disagree with experiment are deemed outliers and removed, and then the remaining trajectories are used to validate the force field. The authors acknowledge this concern partially in the discussion, but the criteria for identifying outliers are not clearly defined. Is the classification based on a quantitative threshold (e.g., R2 values exceeding a certain number of standard deviations from the mean) or a qualitative assessment? The potential for selection bias in this procedure needs to be addressed more rigorously.
  - **Why it matters** If outlier trajectories are removed based on their disagreement with experiment, the remaining ensemble is no longer a purely unbiased sample from the force field. This undermines the claim that the simulations produce realistic ensembles "without the need for reweighting." The distinction between identifying simulation artifacts and cherry-picking trajectories that agree with experiment is subtle but critical for the validity of the conclusions.
  - **Resolution test** Define explicit, pre-established criteria for identifying outlier trajectories (e.g., based on secondary structure propensity exceeding a threshold or Rg falling outside a defined range). Show that the conclusions are robust to the inclusion or exclusion of these trajectories, or alternatively, demonstrate that the outlier trajectories are identifiable by internal criteria (e.g., lack of convergence) rather than by comparison with experiment.

  - **Concern ID** R1-M3
  - **Severity** Major
  - **Blocking** No
  - **Axis** Generalizability of conclusions
  - **Claim pointer** The authors conclude that "modern MD force fields with residue-specific backbone potentials can produce highly realistic IDP ensembles sampling a hierarchy of nano- and picosecond time scales."
  - **Evidence pointer** Discussion section, Abstract
  - **Concern** The study is limited to two IDPs, p53TAD and Pup, both of which are negatively charged and fold upon binding. While these are appropriate test cases, the claim of generalizability to all IDPs is not supported by the data. IDPs vary widely in sequence composition, charge distribution, and propensity for transient structure. The performance of ff99SBnmr2 may be sequence-dependent, and the favorable results obtained here may not extend to IDPs with different characteristics (e.g., positively charged, proline-rich, or containing aromatic-rich low-complexity regions).
  - **Why it matters** The broader significance of the work depends on its applicability beyond the two test cases. If the force field performs well only for a subset of IDPs, the conclusions need to be appropriately qualified. The authors do acknowledge this in the discussion, but the abstract and title make broader claims that are not fully supported.
  - **Resolution test** Qualify the conclusions in the abstract and title to reflect the specific systems studied, or provide additional validation on a more diverse set of IDPs with different sequence properties.

  - **Concern ID** R1-M4
  - **Severity** Major
  - **Blocking** No
  - **Axis** Validation of graph-theoretical analysis
  - **Claim pointer** The authors use graph theory to identify "dominant inter-residue contact clusters and characteristic amino-acid contact propensities" and relate these to R2 profiles.
  - **Evidence pointer** Fig 5, Fig 6, Methods section
  - **Concern** The graph-theoretical analysis is presented as a novel contribution, but the validation of this approach is limited. The authors do not compare their contact cluster analysis with alternative methods for characterizing transient interactions in IDPs (e.g., principal component analysis of contact maps, community detection algorithms). The choice of the 4 Å cutoff for defining contacts is not justified, and the sensitivity of the results to this parameter is not explored. Additionally, the relationship between contact clusters and R2 profiles is largely qualitative; no quantitative correlation is established.
  - **Why it matters** The graph-theoretical analysis is presented as providing new insights into IDP behavior, but without proper validation and sensitivity analysis, the robustness of these insights is unclear. The field would benefit from a more rigorous demonstration that the identified clusters are meaningful and not artifacts of the analysis parameters.
  - **Resolution test** Perform a sensitivity analysis of the contact definition (e.g., varying the distance cutoff from 3.5 to 5.0 Å) and show that the identified clusters and propensities are robust. Compare the graph-theoretical results with an alternative method for characterizing contact networks and demonstrate agreement.

- **Minor Comments**
  - **Concern ID** R1-m1
  - **Severity** Minor
  - **Axis** Clarity of methods
  - **Affected element** Methods section, "Molecular dynamics simulations"
  - **Evidence pointer** Methods section, S1 Table
  - **Issue** The description of the REMD protocol is brief. Details such as the number of replicas, temperature spacing, exchange attempt frequency, and total simulation time per replica are mentioned but not fully contextualized. The criteria for determining convergence of the REMD simulations are not stated.
  - **Required correction** Provide additional details on the REMD convergence criteria (e.g., replica exchange acceptance rates, convergence of ensemble averages over time) and justify the choice of temperature range and number of replicas.

  - **Concern ID** R1-m2
  - **Severity** Minor
  - **Axis** Presentation of results
  - **Affected element** Fig 3
  - **Evidence pointer** Fig 3A-3D
  - **Issue** The correlation coefficients and RMSE values are reported in the text, but the figure itself does not show the experimental error bars. This makes it difficult to visually assess the quality of agreement.
  - **Required correction** Add experimental error bars to Fig 3A-3D, or provide a supplementary figure with error bars included.

  - **Concern ID** R1-m3
  - **Severity** Minor
  - **Axis** Interpretation of Flory exponent
  - **Affected element** Results section, "Ensemble properties of radius of gyration tensor"
  - **Evidence pointer** Fig 1C and 1D, Eq 6
  - **Issue** The Flory exponent for p53TAD (ν = 0.624) is stated to "clearly exceed" the theoretical value for a self-avoiding random coil (ν = 0.588). The authors attribute this to the higher negative charge of p53TAD, but no quantitative analysis is provided to support this interpretation.
  - **Required correction** Provide a more detailed discussion of the factors contributing to the increased Flory exponent, or acknowledge alternative explanations (e.g., residual secondary structure propensity).

  - **Concern ID** R1-m4
  - **Severity** Minor
  - **Axis** Completeness of references
  - **Affected element** Introduction, Discussion
  - **Evidence pointer** References [41-47]
  - **Issue** The discussion of residue-specific force fields cites several references, but the comparison with other recent force field developments for IDPs (e.g., CHARMM36m, a99SB-disp) is limited.
  - **Required correction** Add a brief comparison with other state-of-the-art force fields for IDPs to contextualize the choice of ff99SBnmr2.

- **Technical failings that need to be addressed before the case is established** R1-M1 (statistical robustness) and R1-M2 (outlier trajectory interpretation) are the primary technical issues that need to be resolved. The circularity in the outlier identification procedure and the lack of rigorous error analysis undermine the central claim of quantitative agreement without reweighting.

- **Assessment against Nature-style criteria**
  - **Originality** The work is original in its combination of residue-specific force fields with comprehensive validation against NMR relaxation data and graph-theoretical analysis of contact networks. However, the individual components (force field development, REMD simulations, NMR validation) are established techniques.
  - **Scientific importance** The demonstration that unbiased MD can reproduce experimental relaxation data for IDPs is important for the field, as it addresses a long-standing concern about force field accuracy for disordered proteins. The graph-theoretical approach to characterizing transient contacts is potentially valuable.
  - **Interdisciplinary readership** The work will appeal to computational biophysicists, NMR spectroscopists, and structural biologists. The methods and results are presented in a way that is accessible to these communities, though some familiarity with MD simulation techniques is assumed.
  - **Technical soundness** The core simulation methodology is sound, but the statistical analysis of the comparison with experiment and the handling of outlier trajectories need improvement. The graph-theoretical analysis requires sensitivity testing.
  - **Readability for nonspecialists** The manuscript is generally well-written and the logic is clear. However, the methods section assumes significant background knowledge in MD simulations and NMR relaxation theory. The abstract is accessible to a broad scientific audience.

- **Recommendation posture** Supportive if technical concerns are resolved. The core finding, that ff99SBnmr2 with TIP4P-D can produce IDP ensembles in good agreement with experimental NMR relaxation data, is potentially important. However, the statistical rigor of the comparison and the handling of outlier trajectories must be addressed before the broader claims can be fully accepted.

## Risk / unsupported claims
- The claim that the MD protocol produces ensembles that "closely reproduce experimental data" is not fully supported without proper error analysis on both simulated and experimental values.
- The claim that outlier trajectories are "not representative" is potentially circular, as they are identified by their disagreement with experiment.
- The generalizability of the conclusions to all IDPs is not supported by the two test cases studied.
- The relationship between contact clusters and R2 profiles is presented qualitatively and requires quantitative validation.
- The statement that the protocol "realistically captures" the dominant free energy minima and transition states is an interpretation that goes beyond the direct evidence presented.