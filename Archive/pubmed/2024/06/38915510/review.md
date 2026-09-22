## Review setup
- **Input scope** Full manuscript text (preprint, bioRxiv)
- **Assessment boundary** Technical soundness of the parameterization, validation against published experimental/simulation data, and interpretation of results as presented in the provided text
- **Shared manuscript claim summary** The authors implement new parameters for phosphoserine (pSer) and phosphothreonine (pThr) in the ABSINTH implicit solvent model with the OPLS-AA force field, and demonstrate through all-atom Monte Carlo simulations that these parameters recapitulate published phosphorylation-induced changes in local and global conformational properties of four intrinsically disordered protein systems (NHE1 TH4, Tau peptides, Ash1, PAGE4). They further explore multi-site phosphorylation effects and discuss limitations of phosphomimetic mutations.
- **Visible evidence base** Abstract, Introduction, Methods, Results, Discussion, figure captions (referenced but not shown), supplementary figure references (not shown)
- **Missing materials affecting confidence** Figures and tables (Table 1, Figures 1–5, Supplementary Figures S1–S5, Tables S1–S4) are referenced but not provided; simulation parameter files and analysis code are only available via external repository; no raw simulation trajectories or convergence metrics are shown

## Reviewer
- **Overall assessment** This manuscript addresses a timely and important need in the disordered protein simulation community: the development and validation of force field parameters for phosphorylated residues within the widely used ABSINTH implicit solvent framework. The choice of four test systems with diverse experimental characterization is thoughtful and provides a reasonable basis for parameter assessment. The qualitative and, in several cases, near-quantitative agreement with published data is encouraging. However, the manuscript as presented has several significant gaps that prevent full evaluation of the claims. The absence of all figures and tables makes it impossible to assess the actual data quality, the degree of agreement claimed, or the robustness of the sampling. The parameterization methodology is described at a high level but lacks critical details on how partial charges were derived and validated. The decision to use a z = −1 charge state with a z = −2 solvation free energy is a pragmatic but theoretically questionable choice that requires more thorough justification and sensitivity analysis. The discussion of phosphomimetic limitations is valuable and well-contextualized. Overall, the work has clear potential to be a useful community resource, but the current evidence base is insufficient to fully establish the claims.

- **Who would be interested in the results, and why** Researchers in the intrinsically disordered protein (IDP) simulation community, particularly those using CAMPARI/ABSINTH, will be the primary audience. The parameter set addresses a clear gap in the available tools for simulating phosphorylated IDPs. Beyond this, experimentalists studying phosphorylation-dependent conformational changes in IDPs (e.g., via NMR, SAXS, FRET) may find the work useful for interpreting their data. The discussion on phosphomimetic limitations is broadly relevant to cell biologists and biochemists who use phosphomimetic mutations as a common experimental strategy.

- **Major strengths**
  1. Addresses a genuine and practical need: pSer/pThr parameters for ABSINTH-OPLS were previously unavailable, limiting the study of phosphorylated IDPs in this widely used framework.
  2. The choice of validation systems is well-considered, spanning short peptides with local effects (NHE1 TH4, Tau) and longer IDPs with global effects (Ash1, PAGE4), and covering different types of experimental data (NMR, SAXS, FRET).
  3. The manuscript includes a thoughtful and balanced discussion of phosphomimetic mutations, correctly noting that their utility is system-dependent and providing multiple examples where they fail to recapitulate true phosphorylation effects.
  4. The authors are transparent about limitations, including the absence of charge regulation, the potential artifacts from Na+ chelation, and the decision not to parameterize pTyr.
  5. The work is presented as an open resource with parameter files and analysis code made available, which will facilitate adoption and further testing by the community.

- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness of parameterization
- **Claim pointer** "We implemented parameters for phosphoserine (pSer) and phosphothreonine (pThr) into the OPLS version of the continuum solvent model, ABSINTH, and assessed their performance in all-atom simulations compared to published findings."
- **Evidence pointer** Methods section, "Phospho-serine and -threonine parameter implementation in CAMPARI"; Table S1 (not provided)
- **Concern** The parameterization methodology is described at a high level but lacks critical details. The partial charges were calculated using LigParGen and normalized to the appropriate net charge, but no information is provided on how the charges were assigned to specific atoms, whether the charges were validated against quantum mechanical calculations or experimental data, or how sensitive the simulation results are to the charge assignment scheme. The FOS values were calculated using the TCPD method, but the manuscript does not report the actual values obtained or compare them to existing parameters for similar functional groups. The choice to use a z = −1 charge state with a z = −2 FOS is a significant approximation that is mentioned but not thoroughly justified. The authors state that using z = −2 led to "trapped" salt bridges and poor sampling, but no systematic analysis of this failure mode is presented. Without a more detailed description of the parameterization and a sensitivity analysis, it is difficult to assess whether the reported agreement with experiment is robust or fortuitous.
- **Why it matters** The central claim of the manuscript is that the new parameters are valid for simulating phosphorylated IDPs. If the parameterization is not rigorously described and tested, the community cannot evaluate the reliability of the parameters or understand the conditions under which they are applicable. This is particularly important given the known sensitivity of IDP simulations to force field parameters and the documented challenges with phosphate-containing residues.
- **Resolution test** Provide a detailed description of the charge derivation and normalization procedure, including the specific atoms and charge values. Report the calculated FOS values and compare them to existing data. Perform and present a sensitivity analysis showing how simulation results (e.g., Rg, helicity) vary with reasonable perturbations to the charge assignment or FOS values. Justify the z = −1/z = −2 approximation with a more thorough analysis of the failure modes of the z = −2 state.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence quality and completeness
- **Claim pointer** "Our simulations of four well-studied phospho-IDRs show near-quantitative agreement with published findings for these systems via metrics including changes to radius of gyration, transient helicity, and persistence length."
- **Evidence pointer** Results section, Figures 1–5, Tables S2–S4 (none provided)
- **Concern** The manuscript makes strong quantitative claims about agreement with published experimental and simulation data, but none of the figures or tables that would support these claims are provided in the submitted material. It is impossible to verify the degree of agreement, assess the statistical significance of the comparisons, or evaluate the quality of the simulation sampling. The text describes trends (e.g., "compaction in the phosphorylated peptide," "increase in persistence length") but does not provide the actual numbers, error bars, or statistical tests. The supplementary figures referenced for sampling quality (Figure S1) and additional analyses (Figures S3–S5) are also not available.
- **Why it matters** The validity of the parameter set rests entirely on the demonstrated agreement with experimental data. Without access to the actual data, the claims cannot be evaluated. This is a fundamental issue that affects the core contribution of the manuscript.
- **Resolution test** Provide all figures and tables with clear axis labels, error bars, and statistical comparisons to the published data. Include convergence metrics (e.g., block averaging, autocorrelation times) to demonstrate that the simulations are well-equilibrated and that the reported ensemble averages are reliable. Show the actual numerical values for Rg, helicity, and persistence length for all systems and conditions.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Interpretation and generalizability
- **Claim pointer** "Herein, we describe phosphorylation as a means to alter sequence chemistry, net charge and charge patterning, and intramolecular interactions, which can collectively modulate the local and global IDP ensemble features."
- **Evidence pointer** Discussion section
- **Concern** The manuscript presents a general framework for understanding phosphorylation effects on IDP conformations, but the evidence is based on only four systems. The authors do not provide a systematic analysis of how sequence context modulates the balance between local (e.g., helix stabilization) and global (e.g., chain expansion) effects. For example, the claim that "local expansion is offset by local compaction" in Ash1 is presented as a general principle, but it is unclear how this would apply to other sequences with different charge patterning or proline content. The authors also do not discuss the potential role of phosphorylation in modulating interactions with other molecules (e.g., binding partners), which is a major functional consequence of phosphorylation in IDPs.
- **Why it matters** The manuscript aims to provide a framework for understanding phosphorylation effects on IDP conformations. If the framework is too narrowly based on a small number of systems, it may not be generalizable, and readers may over-interpret the findings.
- **Resolution test** Expand the discussion to include a more systematic analysis of sequence features that correlate with the observed effects. Consider additional test systems or provide a more detailed analysis of the existing systems to identify sequence determinants of local vs. global responses. Discuss the implications of the findings for phosphorylation-dependent interactions with binding partners.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity and reproducibility
- **Affected element** Methods, "Code and distribution"
- **Evidence pointer** Methods section
- **Issue** The manuscript states that parameter files and a tutorial are available on GitHub, but the specific version of CAMPARI used is not clearly stated. The text mentions "CAMPARI v3" but does not specify the exact version or commit, which is important for reproducibility.
- **Required correction** Specify the exact version of CAMPARI used (e.g., v3.5, with a specific commit hash) and provide a direct link to the parameter files and tutorial. Consider adding a version number to the parameter file names.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Technical detail
- **Affected element** Methods, "Calculation of persistence lengths from simulations"
- **Evidence pointer** Methods section, Equations 2 and 3
- **Issue** The manuscript describes two methods for calculating persistence length but does not discuss the potential discrepancies between them. The text states that both methods show the same trend (Figure 3D) but does not provide a quantitative comparison or discuss which method is more reliable for short peptides.
- **Required correction** Add a brief discussion of the advantages and limitations of each method and provide a quantitative comparison of the values obtained from each method for all systems.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Interpretation
- **Affected element** Discussion, "Limitations and caveats"
- **Evidence pointer** Discussion section
- **Issue** The authors note that Na+ chelation may be artifactual but do not discuss the potential implications for simulations performed at higher salt concentrations or with divalent cations, which are common in experimental conditions.
- **Required correction** Add a brief comment on the expected behavior of the parameters at higher salt concentrations or with divalent cations, and whether the same artifacts are likely to occur.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Results, "All-atom MC simulations of phosphorylated IDPs in CAMPARI"
- **Evidence pointer** Results section
- **Issue** The text states that "the simulations reported herein use a phosphoryl group with a −1 charge, with ΔGsolv on the order of ~ −300 kcal/mol" but does not explain why this specific combination was chosen over the z = −2 state, beyond the sampling issues mentioned later.
- **Required correction** Move the explanation for the choice of the z = −1 charge state with z = −2 FOS from the Results to the Methods section, where it can be more fully justified.

- **Technical failings that need to be addressed before the case is established**
  - R1-M1: Incomplete description of parameterization methodology and lack of sensitivity analysis
  - R1-M2: Absence of all figures and tables, making quantitative claims unverifiable

- **Assessment against Nature-style criteria**
  - **Originality**: The work is original in its specific contribution (pSer/pThr parameters for ABSINTH-OPLS) but builds on established approaches for parameter development in IDP simulations. The conceptual framework for understanding phosphorylation effects is not entirely new, but the systematic comparison across four systems adds value.
  - **Scientific importance**: The work addresses a practical need in the IDP simulation community and provides a resource that could enable new studies. The findings on phosphomimetic limitations are important for experimentalists. However, the importance is incremental rather than transformative.
  - **Interdisciplinary readership**: The work is primarily of interest to computational biophysicists and IDP researchers. The discussion of phosphomimetic limitations may attract experimentalists, but the technical nature of the parameterization limits broader appeal.
  - **Technical soundness**: The technical approach is reasonable, but the lack of methodological detail and the absence of figures prevent full assessment. The choice of the z = −1/z = −2 approximation is a concern that needs more thorough justification.
  - **Readability for nonspecialists**: The manuscript is generally well-written and accessible to a broad biophysics audience. The introduction and discussion are clear, but the methods section assumes familiarity with the CAMPARI/ABSINTH framework.

- **Recommendation posture** Supportive if technical concerns are resolved. The work addresses a clear need and the validation strategy is appropriate, but the manuscript cannot be fully evaluated without the figures and tables, and the parameterization methodology needs more detail and sensitivity analysis. Once these issues are addressed, the work would be a valuable contribution to the IDP simulation community.