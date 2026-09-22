## Review setup
- **Input scope** Full manuscript text (main text, methods, figure legends not provided, supplementary material referenced but not provided)
- **Assessment boundary** Scientific claims, methodology, data interpretation, and internal consistency based solely on the supplied manuscript text
- **Shared manuscript claim summary** The authors use native mass spectrometry with surface-induced dissociation (nMS-SID) and molecular dynamics (MD) simulations to show that the intrinsically disordered C-terminal domains (CTDs) of the E. coli RNA chaperone Hfq form a dynamic, interconnected network that stabilizes the hexamer. RNA binding disrupts this CTD network, and the balance between RNA-core stabilization and loss of CTD interactions explains RNA binding selectivity.
- **Visible evidence base** Main text figures referenced (Figs. 2, 3, 4, 5), SI figures and tables referenced but not provided, methods section, data availability statement
- **Missing materials affecting confidence** All figures and figure legends, all SI Appendix content (Figs. S1-S13, Tables S1-S5, Eqs. S1-S3), MD simulation trajectories, raw mass spectra, experimental details for nMS-SID calibration and reproducibility

## Reviewer
- **Overall assessment** This manuscript presents a compelling application of native mass spectrometry with surface-induced dissociation to probe the role of intrinsically disordered regions in a bacterial RNA chaperone. The combination of nMS-SID with MD simulations is innovative and well-suited to the question. The central claim, that disordered CTDs form an interconnected stabilizing network that is disrupted by RNA binding, is plausible and mechanistically interesting. However, the provided text alone does not allow full verification of the quantitative analyses, the statistical treatment, or the robustness of the MD sampling. The manuscript would benefit from clearer presentation of control experiments and from explicit discussion of limitations in the MD force field for disordered proteins.
- **Who would be interested in the results, and why** Researchers studying RNA chaperones, Hfq biology, intrinsically disordered proteins, and the application of native mass spectrometry to protein complexes. The work also has relevance for understanding how disordered regions contribute to protein-protein and protein-RNA interactions more broadly, and for the development of nMS-SID as a tool for probing conformational dynamics in heterogeneous complexes.
- **Major strengths** The use of nMS-SID to directly probe the effect of disordered regions on complex stability is technically sophisticated and relatively novel. The comparison of WT and truncated Hfq provides a clear experimental contrast. The integration of MD simulations with experimental data adds mechanistic depth. The stepwise RNA binding model is a useful conceptual framework.
- **Major Concerns** The manuscript text, as provided, does not include the actual figures or SI content, which limits verification of the quantitative claims. The ERMS analysis relies on comparisons at "equal fragmentation" but the criteria for this matching are not fully described. The MD simulations use a range of trajectory lengths (10 ns to 1500 ns) and it is unclear whether the shorter trajectories are sufficient for convergence of the interaction network statistics. The claim that RNA binding "destabilizes" WT Hfq is based on collision energy differences, but the physical interpretation of this in terms of solution-phase stability requires more careful discussion. The relationship between the observed gas-phase dissociation behavior and the solution-phase functional relevance of the CTD network is not fully established.
- **Minor Comments** The manuscript would benefit from a schematic figure summarizing the proposed model. The significance statement is clear but could be more specific about the mechanistic insight. The discussion of other RNA chaperones with disordered regions is brief and could be expanded. The methods section for MD simulations lacks details on the water model, salt concentration, and temperature control.
- **Technical failings that need to be addressed before the case is established** The lack of access to the figures and SI data prevents full assessment of the quantitative claims. The criteria for matching fragmentation levels between WT and truncated proteins need to be explicit. The MD simulation sampling needs justification, particularly for the shorter trajectories. The statistical treatment of the ERMS data (e.g., error bars, replicates) is not described in the text.
- **Assessment against Nature-style criteria** 
  - Originality: High. The application of nMS-SID to probe disordered region networks in a chaperone is novel.
  - Scientific importance: Moderate to high. The findings have implications for understanding Hfq function and disordered protein regions, but the broader impact beyond the Hfq field is not fully articulated.
  - Interdisciplinary readership: Moderate. The work bridges biophysics, structural biology, and RNA biology, but the technical focus on mass spectrometry may limit appeal to a very broad audience.
  - Technical soundness: Not fully assessable from the text alone. The approach is sound in principle, but the details of the analysis and controls are not visible.
  - Readability for nonspecialists: The significance statement is accessible, but the results section assumes familiarity with nMS-SID and MD terminology. A brief introduction to these techniques for a general audience would improve accessibility.
- **Recommendation posture** Supportive if technical concerns are resolved and the full data (figures, SI) are made available for review. The core idea is interesting and the approach is appropriate, but the current submission cannot be fully evaluated without the missing materials.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence quality
- **Claim pointer** The claim that WT Hfq is more stable than HfqΔCTD, based on the energy required to reach 20% fragmentation (~390 eV vs ~220 eV).
- **Evidence pointer** Fig. 2 B and C; SI Appendix Fig. S2; location not provided
- **Concern** The comparison of fragmentation energies between WT and truncated proteins is central to the paper's conclusions. However, the text does not describe how the "20% fragmentation" point is determined, whether this is a linear interpolation between data points, and what the uncertainty in this value is. The energy scale is corrected for mass (as stated in Methods), but the correction factor and its application are not shown. Without error bars or replicate measurements, it is unclear whether the ~170 eV difference is statistically significant.
- **Why it matters** The entire argument that CTDs stabilize the hexamer rests on this quantitative comparison. If the difference is within experimental noise, the central claim is weakened.
- **Resolution test** Provide the full ERMS curves with error bars from at least three independent replicates, describe the method for determining the 20% fragmentation threshold, and show the mass correction calculation explicitly.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Methodology
- **Claim pointer** The claim that RNA binding "destabilizes" WT Hfq but "stabilizes" HfqΔCTD, based on differences in ERMS profiles.
- **Evidence pointer** Fig. 4 B-G; SI Appendix Figs. S11-S13; location not provided
- **Concern** The interpretation of the ERMS data for RNA-bound complexes is complex. The text states that RNA binding destabilizes WT Hfq relative to free Hfq, but the physical basis for this in the gas phase is not explained. In nMS-SID, the measured dissociation energy reflects the gas-phase stability of the complex, which may not directly correspond to solution-phase stability. The authors do not discuss how the presence of RNA might affect the charge state, the conformation, or the dissociation pathway in ways that could confound the stability comparison. Additionally, the claim that "even short RNAs destabilized the complexes substantially" (Fig. 4E) is surprising and requires a mechanistic explanation that is not provided.
- **Why it matters** The conclusion that RNA binding disrupts the CTD network is a key finding. If the destabilization is an artifact of gas-phase effects rather than a reflection of solution-phase behavior, the biological interpretation is compromised.
- **Resolution test** Provide control experiments with a non-binding RNA or with RNA mutants that do not interact with Hfq. Discuss the potential gas-phase effects of RNA on charge state and conformation. Consider complementary solution-phase methods (e.g., thermal stability assays) to support the gas-phase findings.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Methodology
- **Claim pointer** The claim that MD simulations reveal a "network of CTD interactions" that is "disrupted" by RNA binding.
- **Evidence pointer** Fig. 3; SI Appendix Figs. S3-S9, Table S2; location not provided
- **Concern** The MD simulations are used to support the interpretation of the experimental data. However, the text does not provide sufficient detail on the simulation protocol, the force field validation for disordered proteins, or the convergence of the simulations. The trajectory lengths vary from 10 ns to 1500 ns, and it is unclear whether the shorter trajectories are long enough to sample the conformational space of the disordered CTDs. The analysis of "contacts" is described but the definition of a contact (distance cutoff, residue pairs) is not given. The text states that "no two CTDs adopted the same conformation," which is expected for disordered regions, but the statistical significance of the interaction network is not assessed.
- **Why it matters** The MD simulations are a key piece of evidence for the proposed mechanism. If the simulations are not converged or the analysis is not robust, the conclusions drawn from them are not reliable.
- **Resolution test** Provide details on the simulation setup (water model, salt concentration, temperature, pressure coupling), the force field parameters, and the convergence criteria. Show the time evolution of the contact counts and the variability between replicate simulations. Define the contact criteria explicitly.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Interpretation
- **Claim pointer** The claim that the CTD network "helps Hfq discriminate among different RNAs" and that "weakly bound RNAs are removed" when the CTDs regain their interactions.
- **Evidence pointer** Fig. 5; Discussion; location not provided
- **Concern** The proposed model of RNA discrimination is speculative and goes beyond the direct experimental evidence. The experiments show that RNA binding affects the stability of the complex, but they do not directly measure RNA binding affinity or selectivity. The claim that the CTD network contributes to "discrimination" is an inference that is not directly tested. The discussion of "removal of weakly bound RNAs" is presented as a conclusion but is not supported by the data shown.
- **Why it matters** The broader biological significance of the work depends on this interpretation. If the model is not well-supported, the impact of the study is reduced.
- **Resolution test** Perform direct binding assays (e.g., ITC, fluorescence anisotropy) with WT and HfqΔCTD for different RNA ligands to test whether the CTDs affect binding selectivity. Alternatively, temper the language in the discussion to clearly distinguish speculation from evidence.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Significance statement
- **Evidence pointer** Significance section; location not provided
- **Issue** The significance statement is somewhat general and does not clearly state the specific mechanistic insight gained from this study.
- **Required correction** Revise the significance statement to explicitly mention the finding that CTDs form a dynamic network that is disrupted by RNA binding, and that this may contribute to RNA selectivity.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Methodology
- **Affected element** nMS-SID experimental details
- **Evidence pointer** Materials and Methods, MS section; location not provided
- **Issue** The text states that "typical voltage settings and instrument parameters" are in the SI, but the key parameters for the SID experiment (e.g., surface material, collision energy range, ion activation time) are not described in the main text.
- **Required correction** Provide the key SID parameters in the main text or ensure they are clearly described in the SI.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Data presentation
- **Affected element** Fig. 4
- **Evidence pointer** Fig. 4; location not provided
- **Issue** The figure is described as showing "mass-corrected ERMS plots" but the correction method is only briefly mentioned in the Methods. The figure legend (not provided) would presumably clarify this, but the main text should also explain the correction.
- **Required correction** Add a sentence in the Results section explaining the mass correction and why it is necessary.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Interpretation
- **Affected element** Discussion of other systems
- **Evidence pointer** Discussion, final paragraph; location not provided
- **Issue** The comparison to SSB protein and histone tails is interesting but brief. The parallels are drawn without sufficient detail to be fully convincing.
- **Required correction** Either expand the comparison with specific references to the relevant literature or shorten it to a brief mention.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Reproducibility
- **Affected element** MD simulation data availability
- **Evidence pointer** Data, Materials, and Software Availability; location not provided
- **Issue** The MD simulation trajectories are deposited in a data repository, but the analysis scripts and the specific parameters used for the contact analysis are not mentioned.
- **Required correction** Provide the analysis scripts or a detailed description of the analysis pipeline to ensure reproducibility.

## Risk / unsupported claims
- The claim that the CTD network "helps Hfq discriminate among different RNAs" is not directly supported by the experimental data presented.
- The claim that "weakly bound RNAs are removed" by the CTD network is speculative and not tested.
- The quantitative difference in fragmentation energy between WT and HfqΔCTD cannot be assessed for statistical significance without the full ERMS data and error analysis.
- The MD simulation results are presented as supportive evidence, but the convergence and statistical robustness of the simulations cannot be evaluated from the text alone.
- The physical interpretation of gas-phase dissociation energies in terms of solution-phase stability is not fully justified.