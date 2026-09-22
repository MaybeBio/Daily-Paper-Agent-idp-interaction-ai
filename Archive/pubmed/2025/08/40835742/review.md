## Review setup
- **Input scope** Full manuscript text (abstract, introduction, results, discussion, materials and methods) for the article "Decoding phospho-regulation and flanking regions in autophagy-associated short linear motifs" by Utichi et al., submitted to Communications Biology (DOI: 10.1038/s42003-025-08399-9).
- **Assessment boundary** Scientific content, methodological rigor, validity of claims relative to presented evidence, and suitability for the journal's scope. Editorial quality and formatting are considered only insofar as they affect scientific clarity.
- **Shared manuscript claim summary** The authors present an integrative computational-experimental study of the OPTN LIR–LC3B interaction, claiming that (i) phosphorylation at S177 and multi-phosphorylation reduce LIR flexibility and increase β-strand propensity, (ii) phosphorylation rewires salt-bridge networks both locally and at long range, (iii) disease-associated mutations in the LIR region have phosphorylation-dependent effects on binding, and (iv) microfluidic diffusional sizing (MDS) and surface plasmon resonance (SPR) provide reliable affinity and kinetic measurements for these interactions.
- **Visible evidence base** Full text including main figures (Figs 1–7), tables (Tables 1–2), and supplementary figure/table references. Methods section describes MD simulations, metadynamics, FoldX saturation mutagenesis, MDS, and SPR. Supplementary materials referenced but not provided in full.
- **Missing materials affecting confidence** Supplementary figures S1–S7 and tables S1–S4 are referenced but not available for review. Raw MD trajectory data, MDS binding curves, and SPR sensorgrams are only partially shown. Statistical analysis details for MDS and SPR comparisons are incomplete. The OSF repository is referenced but not accessible from the provided material.

## Reviewer
- **Overall assessment** This manuscript addresses a timely and important question in the autophagy field: how phosphorylation and flanking regions modulate SLiM-mediated interactions. The integration of MD simulations with two orthogonal biophysical methods (MDS and SPR) is commendable and represents a methodological advance for studying phospho-regulated SLiMs. The authors provide a detailed mechanistic model for how phosphorylation at S177 enhances binding to LC3B through conformational selection and electrostatic rewiring. However, several concerns limit the strength of the conclusions. The computational predictions are not always directly validated by the experimental data, the SPR kinetic analysis is acknowledged as technically limited, and the MDS sensitivity threshold (2 kcal/mol) means that many predicted effects fall below the detection limit. The disease-associated mutation analysis is largely computational with minimal experimental follow-up. The claim of a "versatile toolkit" is somewhat overstated given the demonstrated limitations. Nevertheless, the core finding that phosphorylation enhances kon through conformational selection is novel and mechanistically insightful. The manuscript would benefit from clearer articulation of which claims are experimentally validated versus computationally inferred, and from additional experimental validation of the most impactful predictions.

- **Who would be interested in the results, and why** Researchers studying autophagy receptor biology, particularly the OPTN–LC3 interaction and its regulation by TBK1 phosphorylation. The broader SLiM community will be interested in the methodological framework for studying phospho-regulated motifs. Structural biologists and computational biophysicists studying protein-protein interactions in disordered regions will find the MD-based approach valuable. The MDS methodology for measuring SLiM affinities could be adopted by other groups studying weak transient interactions. Clinicians studying glaucoma and ALS genetics may find the disease-associated mutation analysis relevant, though the clinical implications are not directly addressed.

- **Major strengths**
  1. Integration of multiple computational and experimental methods provides a comprehensive view of the system.
  2. The use of MDS for SLiM binding studies is novel and addresses a real need for measuring weak interactions.
  3. The "reverse approach" for FoldX saturation mutagenesis to assess phosphorylation effects is methodologically clever.
  4. The study provides mechanistic insight into how phosphorylation enhances kon, which is a relatively underexplored aspect of SLiM regulation.
  5. The authors are appropriately cautious about the limitations of their computational predictions in several places.
  6. The comparison between phosphomimetics and true phosphorylation is an important control that many studies omit.

- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Experimental validation
- **Claim pointer** The authors claim that "specific phosphorylation events and flanking residues modulate binding to LC3B at the atomic level" and that disease-associated mutations "alter these interactions in the phosphorylated context."
- **Evidence pointer** Results section "High-throughput mutational scans identify binding hotspots and residues conferring specificity for the binding mode of the phosphorylated variant"; Table 2; Fig 5E–F
- **Concern** The disease-associated mutation analysis relies almost entirely on computational predictions from FoldX and MAVISp. Only a small subset of mutations (F178W, F178A, M183A) was experimentally tested, and these were selected based on their predicted effects rather than their disease relevance. The claim that disease mutations "alter these interactions" is therefore not directly supported by experimental evidence for the specific disease variants listed in Table 2. The authors do not experimentally validate any of the disease-associated mutations (V161M, E163D, L166V, N169S/T, E175Q, D176Y, F178V, V179D, A184D/S) in the phosphorylated context. The MAVISp predictions for these variants are presented as findings, but the accuracy of these predictions is not benchmarked against experimental data for this specific system.
- **Why it matters** The clinical relevance of the disease mutations is a key motivation for the study. Without experimental validation, the claims about disease mutations affecting phosphorylation-dependent binding remain speculative. The authors themselves acknowledge that FoldX has limitations in predicting stabilizing effects, yet they use these predictions to draw conclusions about disease variants. This creates a disconnect between the strength of the claims and the evidence base.
- **Resolution test** The authors should either (a) experimentally validate at least 2-3 disease-associated mutations in the phosphorylated context using MDS or a comparable method, (b) clearly reframe these as computational predictions requiring future validation, or (c) provide benchmarking data showing that MAVISp predictions correlate with experimental measurements for this system.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness of kinetic measurements
- **Claim pointer** The authors claim that SPR provides "quantitative kinetic constants" and that phosphorylation leads to a ~30-fold increase in kon and ~10-fold increase in koff.
- **Evidence pointer** Results section "Surface plasmon resonance reveals phosphorylation-driven dynamics in OPTN LIR–LC3B interactions"; Fig 7
- **Concern** The authors acknowledge that "the koff values exceeded the measurement capabilities of the Biacore X100 instrument" and that "most kon values are on the brink of the instrument's detection limit." This is a critical limitation. The kon values reported (0.55 × 10³ M⁻¹s⁻¹ for WT) are extremely slow for a protein-peptide interaction, and the authors note that the fits are "acknowledged as suboptimal." The koff values are not directly measured but calculated from steady-state Kd and kon. Given these limitations, the quantitative claims about fold-changes in kon and koff are not reliable. The authors state that "our analysis yielded meaningful insights," but the technical limitations undermine the precision of the reported rate constants.
- **Why it matters** The kinetic interpretation is central to the proposed "conformational selection" mechanism. If the rate constants are not reliably measured, the mechanistic conclusions drawn from them are weakened. The authors use the SPR data to support a specific kinetic model, but the data quality may not support such detailed interpretation.
- **Resolution test** The authors should either (a) use a more sensitive SPR instrument or surface chemistry that can reliably measure fast kinetics, (b) use an alternative method such as stopped-flow fluorescence or BLI with faster time resolution, (c) present the SPR data as semi-quantitative and temper the kinetic claims accordingly, or (d) provide a rigorous error analysis that accounts for the instrument limitations in the reported rate constants.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Computational methodology
- **Claim pointer** The authors claim that MD simulations "are in good agreement with NMR chemical shifts" and that the simulations capture the "overall dynamics observed in solution."
- **Evidence pointer** Results section "MD simulations of LC3B in complex with phosphorylated OPTN are in good agreement with NMR chemical shifts"; Fig 2A; Table 1
- **Concern** The validation of MD simulations against NMR data is limited. The χ²red values are reported for one replicate, with results for other replicates relegated to the OSF repository. The isoleucine residues show χ²red > 3 for Cδ, which the authors attribute to side chain rotameric states. However, the authors do not provide a systematic comparison of all residues or a clear threshold for what constitutes "good agreement." The comparison is also only performed for the penta-phosphorylated construct, not for the unphosphorylated or mono-phosphorylated variants used in subsequent analyses. The use of a single NMR structure as a starting point may bias the simulations.
- **Why it matters** The validity of all subsequent computational analyses depends on the quality of the MD simulations. If the simulations do not accurately reproduce the experimental ensemble, the conclusions about flexibility, salt-bridge networks, and mutational effects may be artifacts of the force field or sampling protocol.
- **Resolution test** The authors should provide a more comprehensive validation, including per-residue chemical shift comparisons, analysis of all replicates, and ideally validation against additional experimental observables such as NOE-derived distances or relaxation data. If such data are not available, the limitations should be more explicitly acknowledged.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Statistical rigor
- **Claim pointer** The authors claim that MDS can "accurately estimate changes in Kd" and that differences between variants are statistically significant.
- **Evidence pointer** Results section "Microfluidic diffusional sizing can accurately estimate changes in Kd and hydrodynamic radii upon substitutions in the phosphorylated OPTN LIR"; Fig 5A; Fig 6
- **Concern** The statistical analysis of MDS data is not fully described. The authors state that "differences between peptide variants and reference variants were evaluated using unpaired, parametric t-tests" but do not report the number of biological replicates for each comparison, the variance structure, or whether multiple testing corrections were applied. The Kd values for some variants (e.g., S177D and S177E) show substantial overlap in their confidence intervals, yet the authors claim they are significantly different from WT. The MDS sensitivity threshold of 2 kcal/mol is mentioned, but it is unclear how this was determined and whether it applies uniformly across all variants.
- **Why it matters** The MDS data provide the primary experimental validation for the computational predictions. If the statistical analysis is not rigorous, the conclusions about which mutations affect binding may be unreliable. The authors use these data to support claims about specific residues being "hotspots" for binding.
- **Resolution test** The authors should provide a complete statistical analysis including: (a) exact n values for each comparison, (b) effect sizes with confidence intervals, (c) multiple testing corrections where applicable, and (d) a power analysis to justify the sample sizes used. They should also clarify how the 2 kcal/mol sensitivity threshold was established.

- **Concern ID** R1-M5
- **Severity** Major
- **Blocking** No
- **Axis** Generalizability of findings
- **Claim pointer** The authors claim that their findings on OPTN LIR provide "a versatile toolkit to characterize phospho-regulated SLiMs" and that their approach "can be extended to other LIRs or SLiMs regulated by phosphorylation."
- **Evidence pointer** Abstract; Discussion
- **Concern** The study focuses exclusively on a single LIR (OPTN) and a single binding partner (LC3B). While the authors discuss previous work on other LIRs, they do not demonstrate that their approach works for other systems. The MDS method, in particular, may not be generalizable to all SLiM interactions due to differences in binding affinities, molecular weights, and the need for fluorescent labeling. The computational pipeline (MD + FoldX + MAISM) requires significant expertise and computational resources that may not be accessible to all researchers.
- **Why it matters** The claim of a "versatile toolkit" is a significant part of the paper's broader impact. If the approach is not demonstrated to work beyond this one system, the claim is overstated. The authors should either demonstrate applicability to at least one additional LIR system or temper the generalizability claims.
- **Resolution test** The authors should either (a) apply their approach to at least one additional LIR-containing protein with known phosphorylation-dependent regulation, (b) provide a clear protocol that others can follow, including potential pitfalls and limitations, or (c) revise the claims to be more specific to the OPTN-LC3B system.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Figure 1B
- **Evidence pointer** Fig 1B
- **Issue** The schematic of constructs used for MD simulations is difficult to interpret. The differences between the constructs (e.g., which residues are included, where phosphorylation sites are located) are not clearly labeled.
- **Required correction** Provide a clearer schematic with residue numbers, phosphorylation site positions, and a legend explaining the color coding and symbols used.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Methods section
- **Evidence pointer** Materials and methods, "Microfluidic diffusional sizing (MDS)"
- **Issue** The equation for fitting MDS data is presented in a format that is difficult to read. The variables are not all defined in the text.
- **Required correction** Define all variables in the equation and provide a brief explanation of the fitting procedure, including initial parameter estimates and constraints.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Interpretation
- **Affected element** Fig 2F
- **Evidence pointer** Fig 2F
- **Issue** The free energy surface (FES) profiles from metadynamics are shown for only two variants (WT and penta-phosphorylated). The mono-phosphorylated variant is not shown, making it difficult to assess whether the effect is graded with phosphorylation level.
- **Required correction** Either include the mono-phosphorylated variant in the FES plot or provide a clear explanation for its omission.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Consistency
- **Affected element** Table 2
- **Evidence pointer** Table 2
- **Issue** The ΔΔG values for binding are reported for p5 and p1 variants, but the units are not specified. The threshold for "damaging" effects is not clearly defined.
- **Required correction** Specify the units (kcal/mol) and provide a clear explanation of the thresholds used to classify variants as damaging, neutral, or uncertain.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Literature context
- **Affected element** Discussion
- **Evidence pointer** Discussion
- **Issue** The discussion of the "conformational selection" mechanism would benefit from more explicit comparison to alternative models (e.g., induced fit) and to experimental studies that have directly tested these models for other LIR-ATG8 interactions.
- **Required correction** Add a brief paragraph discussing alternative kinetic models and how the current data distinguish between them, or acknowledge that the data cannot definitively distinguish between models.

- **Concern ID** R1-m6
- **Severity** Minor
- **Axis** Reproducibility
- **Affected element** Materials and methods
- **Evidence pointer** Materials and methods, "Molecular dynamics (MD) simulations"
- **Issue** The methods for MD simulations are described but key parameters such as the number of ions added, the specific NaCl concentration, and the equilibration protocol are not fully specified.
- **Required correction** Provide complete details of the simulation setup, including ion concentration, equilibration steps, and any restraints applied during equilibration.

## Risk / unsupported claims
- The claim that disease-associated mutations "alter these interactions in the phosphorylated context" is not experimentally supported for the specific disease variants listed in Table 2. Only F178W, F178A, and M183A were experimentally tested, and these are not the disease variants.
- The claim that SPR provides "quantitative kinetic constants" is weakened by the acknowledged technical limitations of the measurements.
- The claim of a "versatile toolkit" for characterizing phospho-regulated SLiMs is not demonstrated beyond the OPTN-LC3B system.
- The claim that "specific phosphorylation events and flanking residues modulate binding to LC3B at the atomic level" is partially supported by MD simulations but the atomic-level details are not experimentally validated.
- The MDS sensitivity threshold of 2 kcal/mol is stated but not justified or demonstrated.
- The correlation analysis of salt-bridge distances (Fig 4H) is described but the statistical significance of the correlations is not reported.
- The claim that "the effect cannot be recapitulated by the single phosphorylation" (regarding N-terminal hotspot activation) is based on computational predictions that are not experimentally validated for the mono-phosphorylated variant.