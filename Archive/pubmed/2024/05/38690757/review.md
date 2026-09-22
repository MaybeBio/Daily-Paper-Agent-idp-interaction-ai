## Review setup
- **Input scope** Full manuscript text, including abstract, introduction, results, discussion, conclusions, and supplementary figure references
- **Assessment boundary** Scientific content, experimental design, data interpretation, and claims as presented in the provided text. No access to supplementary figures, raw data, or experimental protocols beyond what is described.
- **Shared manuscript claim summary** The authors report that myristoylation of resilin-like polypeptides (RLPs) with UCST-type phase behaviour increases their propensity to phase separate, alters condensate dynamics and fluidity, and that the magnitude of these effects depends on the sequence of the lipidation site. Molecular dynamics simulations and hydropathy analysis suggest the mechanism involves an expanded hydrophobic region rather than changes in peptide rigidity.
- **Visible evidence base** Turbidimetry (Fig. 2a, 2b, S6, S7, S8), dynamic light scattering (Fig. 3a, S11), confocal microscopy (Fig. 3b, 3c, S10), FRAP (Fig. 4), TEM/cryo-TEM (Fig. 5), FT-IR (Fig. S13), molecular dynamics simulations with Ramachandran analysis (Fig. S12), PARCH hydropathy analysis (Fig. 6, S14), and biochemical characterization (Fig. S1–S5)
- **Missing materials affecting confidence** Supplementary figures and experimental details (ESI), raw data for statistical analyses, simulation parameters and convergence criteria, detailed FRAP methodology, and full thermodynamic fitting procedures

## Reviewer
- **Overall assessment** This manuscript addresses a timely and important question: how lipidation, a common post-translational modification, influences the phase behaviour of proteins with UCST-type transitions. The study is well-motivated, and the experimental design comparing two lipidation site sequences is thoughtful. The combination of experimental biophysics and molecular simulation is appropriate. However, several technical concerns limit the strength of the conclusions as currently presented. The claim that lipidation site sequence context modulates phase behaviour is supported, but the mechanistic interpretation regarding hydrophobic expansion relies heavily on computational analysis without direct experimental validation. The FRAP data, while statistically significant, show very large variability that warrants closer examination. The generalizability claims to other UCST proteins and the biomedical applications discussion extend beyond the evidence provided. Overall, this is a solid contribution to the soft matter and biomolecular condensate fields, but the mechanistic claims require additional support.

- **Who would be interested in the results, and why** Researchers studying biomolecular condensates and phase separation, particularly those interested in post-translational modifications as regulatory mechanisms. The work is also relevant to the protein engineering and biomaterials communities, especially those working with resilin-based or other stimulus-responsive polypeptides. The findings on how lipidation site sequence context modulates phase behaviour could inform the design of lipidated proteins for drug delivery or other biomedical applications.

- **Major strengths** 
  1. The study addresses a significant gap in the literature by examining lipidation effects on UCST-type phase behaviour, which is more representative of many biological phase-separating proteins than the LCST systems previously studied.
  2. The experimental design comparing two lipidation site sequences with only three amino acid differences is elegant and allows for clear attribution of observed differences to sequence context.
  3. The combination of multiple complementary techniques (turbidimetry, DLS, confocal microscopy, FRAP, TEM, FT-IR, and MD simulations) provides a comprehensive characterization of the system.
  4. The finding that lipidation does not alter the concentration dependence of cloud points, contrasting with previous ELP studies, is an important observation that challenges existing assumptions.

- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Mechanistic interpretation
- **Claim pointer** "Molecular simulations suggested these effects result from an expanded hydrophobic region created by the interaction between the lipid and lipidation site rather than changes in peptide rigidity."
- **Evidence pointer** Fig. 6, Fig. S12, Fig. S13, Fig. S14
- **Concern** The mechanistic conclusion that an expanded hydrophobic region drives the observed phase behaviour differences is based primarily on PARCH hydropathy analysis and MD simulations. However, the PARCH analysis is presented as a computational prediction without experimental validation. The Ramachandran analysis and FT-IR data rule out rigidity changes, but they do not directly confirm the hydrophobic expansion mechanism. The authors do not provide any experimental evidence (e.g., solvatochromic probes, NMR relaxation measurements, or binding studies with hydrophobic ligands) that would directly test the hydration state of the lipidation site region.
- **Why it matters** The central mechanistic claim of the paper is that lipidation site sequence context modulates phase behaviour through altered hydrophobicity and hydration. Without direct experimental support for this mechanism, the conclusion remains speculative. This distinction is important because alternative mechanisms, such as changes in local conformational preferences or specific inter-chain interactions involving the lipid moiety, could also explain the observed differences.
- **Resolution test** Provide experimental evidence directly probing hydration or hydrophobicity at the lipidation site, such as NMR-based hydration measurements, fluorescence spectroscopy with environment-sensitive probes, or isothermal titration calorimetry with model hydrophobic ligands. Alternatively, perform mutations that specifically alter hydrophobicity at the lipidation site and show corresponding changes in phase behaviour that match PARCH predictions.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** No
- **Axis** Quantitative analysis and statistics
- **Claim pointer** "FRAP recovery half-lives for unmodified constructs were consistently short (τ1/2 = 1.5 ± 0.2 seconds) across different lipidation sites. In contrast, lipidated constructs exhibited slower recovery rates, with τ1/2 for m-AGA-RLP at 87.5 ± 22.9 seconds and m-LSL-RLP showing much slower rates, with τ1/2 = 379.1 ± 93.2 seconds."
- **Evidence pointer** Fig. 4
- **Concern** The FRAP data show extremely large differences in recovery half-times between unmodified and lipidated constructs (1.5 s vs 87.5 s and 379.1 s), yet the reported standard deviations are relatively small. The two-way ANOVA result (F(1, 8) = 18.47, p = 0.003) is reported, but the degrees of freedom suggest a small sample size. The manuscript does not report the number of independent replicates, the number of droplets analyzed per condition, or whether the FRAP measurements were performed on droplets of comparable size. Given the dramatic differences observed, it is critical to rule out artifacts related to droplet size, fluorophore concentration, or bleaching depth.
- **Why it matters** FRAP recovery kinetics are highly sensitive to experimental conditions. If the lipidated constructs form larger or more viscous droplets, the slower recovery could reflect size effects rather than intrinsic differences in molecular mobility. The manuscript does not provide sufficient detail to assess whether the FRAP measurements were properly controlled.
- **Resolution test** Report the number of replicates and droplets analyzed, provide droplet size distributions for all constructs, and show that FRAP recovery times are independent of droplet size within each condition. If possible, perform FRAP on droplets of matched size across conditions.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Generalizability and scope of claims
- **Claim pointer** "We propose that the observed effects of lipidation are likely generalizable to these proteins, including those with complex sequences like FUS, DDX4, and Laf-1."
- **Evidence pointer** Discussion section
- **Concern** The authors extrapolate their findings from a single model RLP system to complex biological proteins such as FUS, DDX4, and Laf-1 without providing any experimental or computational evidence for this generalizability. These proteins have vastly different sequences, domain architectures, and phase separation mechanisms compared to the simple repeat-sequence RLP used here. The claim that lipidation effects observed in this minimal system will translate to these complex proteins is speculative.
- **Why it matters** Overstating the generalizability of findings can mislead readers and future research directions. While the authors appropriately frame this as a proposal for future work, the statement as written implies a level of confidence not supported by the data.
- **Resolution test** Either remove or substantially soften this claim, or provide additional evidence such as sequence analysis showing conserved features between the RLP lipidation sites and potential lipidation sites in FUS, DDX4, or Laf-1 that would support the proposed generalizability.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Thermodynamic interpretation
- **Claim pointer** "The non-lipidated constructs exhibited similar enthalpic (−93 ± 2 kcal mol−1) and entropic (−230 ± 7 cal mol−1 K−1) contributions... m-AGA-RLP exhibited a decrease in both the enthalpic and entropic components of phase separation, while m-LSL-RLP showed a significant increase."
- **Evidence pointer** Fig. S9
- **Concern** The thermodynamic parameters are extracted using a "modified Van 't Hoff model" applied to turbidity data. The manuscript does not provide sufficient detail about this model, its assumptions, or its validation. The reported values are very large in magnitude (tens of kcal/mol), which raises questions about whether the model is appropriate for this system. Additionally, the manuscript does not report confidence intervals for the thermodynamic parameters or discuss potential systematic errors in the fitting procedure.
- **Why it matters** The thermodynamic interpretation is used to support the mechanistic conclusion that lipidation alters the balance of enthalpic and entropic contributions to phase separation. If the model is not properly validated or the parameters are not reliable, this interpretation is weakened.
- **Resolution test** Provide a detailed description of the modified Van 't Hoff model, its assumptions, and validation. Report confidence intervals for all thermodynamic parameters and discuss potential sources of systematic error. If possible, validate the thermodynamic parameters using an independent method such as differential scanning calorimetry.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity and reproducibility
- **Affected element** Experimental methods
- **Evidence pointer** Results section, Fig. 2
- **Issue** The manuscript states that turbidimetry was used to characterize UCST phase behaviour but does not provide details on the heating/cooling rates, equilibration times, or how cloud points were determined from the turbidity curves.
- **Required correction** Provide a detailed description of the turbidimetry protocol, including temperature ramp rates, equilibration times, and the criterion used to define the cloud point.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Data presentation
- **Affected element** Fig. 2b
- **Evidence pointer** Fig. 2b
- **Issue** The phase diagram in Fig. 2b shows linear fits to the dilute branch, but the manuscript does not report the number of concentrations tested or the concentration range. This information is important for assessing the robustness of the observed linear relationship.
- **Required correction** Report the concentration range and number of data points used for the phase diagram, and consider showing individual data points in the figure.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Interpretation of DLS data
- **Affected element** Fig. 3a
- **Evidence pointer** Fig. 3a
- **Issue** The DLS data show that lipidated constructs form assemblies of approximately 45 nm (m-AGA-RLP) and 180 nm (m-LSL-RLP) above the UCST. The manuscript interprets this as enhanced intermolecular interactions but does not discuss whether these assemblies are equilibrium structures or kinetically trapped aggregates.
- **Required correction** Discuss the possibility of kinetically trapped aggregates and, if possible, perform concentration-dependent DLS measurements to assess whether the assembly size is concentration-dependent.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Simulation details
- **Affected element** MD simulations
- **Evidence pointer** Fig. S12, Fig. 6
- **Issue** The manuscript does not provide details on the MD simulation parameters, including the force field, water model, simulation length, system size, or number of replicates. This information is essential for assessing the reliability of the simulation results.
- **Required correction** Provide a detailed description of the MD simulation setup in the methods section or supplementary information.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Terminology
- **Affected element** Abstract and throughout
- **Evidence pointer** Abstract
- **Issue** The term "phase-separation" is used inconsistently, sometimes with a hyphen and sometimes without. This should be standardized throughout the manuscript.
- **Required correction** Standardize the use of "phase separation" (without hyphen) throughout the manuscript.

- **Concern ID** R1-m6
- **Severity** Minor
- **Axis** Literature context
- **Affected element** Introduction
- **Evidence pointer** Introduction
- **Issue** The introduction discusses the importance of PTMs in regulating phase separation but does not cite several recent reviews on this topic that would provide broader context for the readership.
- **Required correction** Consider citing recent reviews on PTM-mediated regulation of phase separation to strengthen the introduction.

## Risk / unsupported claims
- The claim that lipidation effects observed in the RLP model system are "likely generalizable" to complex proteins such as FUS, DDX4, and Laf-1 is unsupported by the data presented.
- The mechanistic conclusion that an "expanded hydrophobic region" drives the observed phase behaviour differences is supported only by computational analysis and lacks direct experimental validation.
- The statement that lipidation "significantly influences RLPs' thermodynamic propensity for phase separation" is supported by the turbidimetry data, but the thermodynamic parameters extracted from the modified Van 't Hoff model are not fully validated.
- The claim that the observed effects are due to "modified hydration levels" is inferred from PARCH analysis but is not directly tested experimentally.
- The suggestion that these findings "open avenues for designing lipidated resilins for biomedical applications like heat-mediated drug elution" is speculative and not supported by any functional demonstration in the manuscript.