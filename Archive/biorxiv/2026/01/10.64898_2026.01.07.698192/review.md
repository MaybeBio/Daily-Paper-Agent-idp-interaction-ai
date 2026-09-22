## Review setup
- **Input scope** Full manuscript text (abstract, introduction, results and discussion, conclusion, acknowledgements) as provided on bioRxiv
- **Assessment boundary** Scientific content, experimental design, data interpretation, and claims as presented in the provided text. Figures and supplementary materials are referenced but not directly examined.
- **Shared manuscript claim summary** The authors report a fully aqueous, genetically encoded platform for assembling micellar protein nanoparticles via electrostatic coacervation between anionic globular proteins and multi-domain intrinsically disordered proteins (mdIDPs) composed of a neutral elastin-like polypeptide (ELP) domain and a cationic disordered histone-derived domain (H5). They claim modular control over charge density, neutral domain length, and stoichiometry, enabling homogeneous micellar nanoparticles with high protein payload retention under mild conditions. They report that globular proteins act as both cargo and assembly drivers, that particle size and composition can be tuned via charge fraction, and that the platform is generalizable across a range of globular protein cargoes.
- **Visible evidence base** Text descriptions of results from DLS, FCS, TEM, cryo-ET, SAXS, optical microscopy, turbidity measurements, and protein production yields. References to Supplementary Figures 1-14 and Figures 1-5 are made but the actual figures and supplementary data are not provided in the submitted material.
- **Missing materials affecting confidence** All figures, supplementary figures, experimental methods section, and quantitative data tables are absent from the provided text. Without these, quantitative claims regarding particle sizes, polydispersity values, protein loading numbers, and SAXS fitting parameters cannot be independently verified.

## Reviewer
- **Overall assessment** The manuscript presents a conceptually interesting approach to protein nanoparticle assembly, leveraging electrostatic coacervation between engineered IDPs and globular proteins. The design space explored is systematic and the parameter space is well chosen. However, the provided text alone does not contain sufficient quantitative evidence to fully evaluate the strength of the claims. The central claims regarding nanoparticle homogeneity, cargo loading numbers, and the proposed charge regulation mechanism require the actual data shown in figures and supplementary materials. The work has potential significance for protein delivery applications, but the case is not fully established from the text alone.
- **Who would be interested in the results, and why** Researchers in protein engineering, drug delivery, biomaterials, and nanomedicine would be interested. The platform offers a potentially generalizable, fully aqueous route to protein nanoparticles without organic solvents or covalent modification, which addresses a known limitation in protein therapeutic formulation. The design rules established could inform broader work on electrostatic assembly of biomacromolecules.
- **Major strengths** The systematic variation of four key design parameters (neutral domain length, cationic domain charge, protein cargo charge, mixing ratio) provides a clear framework for understanding assembly behavior. The use of multiple complementary characterization techniques (DLS, FCS, TEM, SAXS) is appropriate for distinguishing different assembly regimes. The observation that charge density, not just net charge, is critical for assembly is a useful insight. The reported stability of nanoparticles over 43 days and at low concentrations is practically relevant.
- **Major Concerns**
  - **Concern ID** R1-M1
  - **Severity** Major
  - **Blocking** Yes
  - **Axis** Evidence sufficiency
  - **Claim pointer** The manuscript claims formation of "homogeneous micellar nanoparticles" with "low dispersity" and "∼200-400 GFP-24 molecules per nanoparticle."
  - **Evidence pointer** Figures 2b, 2e, 2f, 3a-f, Supplementary Figures 5-10; location not provided
  - **Concern** The quantitative basis for these claims is not present in the provided text. No actual DLS polydispersity values, FCS-derived hydrodynamic diameters, TEM size distributions, or SAXS fitting parameters are given. The claim of 200-400 GFP molecules per nanoparticle is stated but the calculation method and associated uncertainty are not described.
  - **Why it matters** The central advance claimed is the formation of well-defined, homogeneous nanoparticles with high protein loading. Without the actual quantitative data, the reader cannot assess whether the particles are truly monodisperse, whether the loading numbers are reliable, or whether the size control is as precise as claimed.
  - **Resolution test** Provide the actual size distributions, polydispersity indices, FCS fitting results, and the calculation for protein loading per nanoparticle with error estimates.
  - **Concern ID** R1-M2
  - **Severity** Major
  - **Blocking** Yes
  - **Axis** Mechanistic claim support
  - **Claim pointer** The manuscript claims that "charge regulation" of the globular protein accommodates off-stoichiometry mixing and broadens the assembly regime, and that this is why assembly occurs at a constant molar ratio (N+ ~ 0.4) rather than charge ratio.
  - **Evidence pointer** Section 2.4, Supplementary Figure 13d; location not provided
  - **Concern** The charge regulation mechanism is invoked to explain the observation that optimal nanoparticle formation occurs at a constant molar ratio across mdIDPs with different net charges. However, no direct experimental evidence for charge regulation is presented. The claim that "the globular protein's charge regulation accommodates the off-charge stoichiometry mixing" is speculative without measurements of protein charge state or binding stoichiometry under assembly conditions.
  - **Why it matters** The proposed mechanism is central to the design rules presented. If charge regulation is not the correct explanation, the design rules may not generalize as claimed. Alternative explanations, such as differences in binding affinity or steric effects, are not ruled out.
  - **Resolution test** Provide direct evidence of charge regulation, such as zeta potential measurements, isothermal titration calorimetry, or pH-dependent assembly studies, or temper the mechanistic claim to be explicitly speculative.
  - **Concern ID** R1-M3
  - **Severity** Major
  - **Blocking** No
  - **Axis** Generalizability claim
  - **Claim pointer** The manuscript claims the platform is "generalizable" and "cargo-agnostic" based on testing with GFP variants, glucose oxidase, and mTurquoise2.
  - **Evidence pointer** Section 2.5, Figure 5, Supplementary Figure 14; location not provided
  - **Concern** Only three protein types are tested, all of which are relatively acidic (net charge -12 to -30). The claim of generalizability is not supported by testing with proteins of different charge signs, shapes, or surface charge distributions. The text states "diverse sizes, folds, and surface chemistries" but the actual diversity tested appears limited.
  - **Why it matters** The stated potential for broad application in protein delivery depends on the platform working with a wide range of therapeutic proteins. If only acidic, globular proteins work, the platform is more limited than claimed.
  - **Resolution test** Test additional proteins with different charge properties, or revise the generalizability claim to reflect the actual range of proteins tested.
- **Minor Comments**
  - **Concern ID** R1-m1
  - **Severity** Minor
  - **Axis** Clarity
  - **Affected element** Definition of charge fraction (f+)
  - **Evidence pointer** Section 2.1, location not provided
  - **Issue** The charge fraction f+ is introduced as a key parameter but its precise definition is not stated in the text. It appears to be the fraction of positive charge contributed by the mdIDP, but the calculation method is unclear.
  - **Required correction** Provide an explicit definition of f+ and N+ with equations or a clear verbal description.
  - **Concern ID** R1-m2
  - **Severity** Minor
  - **Axis** Reproducibility
  - **Affected element** Protein production yields
  - **Evidence pointer** Section 2.1, Supplementary Figure 1; location not provided
  - **Issue** The text states that all mdIDPs were "successfully produced in E. coli with reasonable yields" but no yield values are given. This is important for assessing practical utility.
  - **Required correction** Provide quantitative yield data (mg/L culture) for the mdIDP library.
  - **Concern ID** R1-m3
  - **Severity** Minor
  - **Axis** Interpretation
  - **Affected element** Simple coacervation observation at f+ = 0.9 for ELPS96
  - **Evidence pointer** Section 2.2, Figure 2a; location not provided
  - **Issue** The observation of simple coacervation for ELPS96 at f+ = 0.9 is attributed to neutralization of the cationic domain by GFP. However, the alternative explanation that the high local concentration of ELPS96 itself drives phase separation is not fully discussed.
  - **Required correction** Acknowledge alternative explanations or provide additional data to support the proposed mechanism.
  - **Concern ID** R1-m4
  - **Severity** Minor
  - **Axis** Completeness
  - **Affected element** Stability data
  - **Evidence pointer** Section 2.2, Supplementary Figure 6d-e; location not provided
  - **Issue** The claim of stability over 43 days is mentioned but the conditions of storage (temperature, buffer, concentration) are not described in the text.
  - **Required correction** Specify storage conditions and provide the stability data in the main text or clearly reference the supplementary figure with conditions stated.

## Risk / unsupported claims
- The claim of "high protein payload retention" is not quantitatively supported in the provided text.
- The claim of "∼200-400 GFP-24 molecules per nanoparticle" is stated without showing the calculation or the underlying FCS data.
- The claim that charge regulation of the globular protein is the mechanism enabling assembly at off-stoichiometric charge ratios is speculative and not directly evidenced.
- The claim of "cargo-agnostic encapsulation" is not supported by the limited range of proteins tested.
- The claim that nanoparticles are "stable for over a month" is referenced to supplementary data not provided in the submitted material.
- The claim that the platform enables "tunable formulations for downstream applications" is plausible but not demonstrated with functional assays in the provided text.

## Assessment against Nature-style criteria
- **Originality** The concept of using electrostatic coacervation between engineered IDPs and globular proteins for nanoparticle assembly is a meaningful extension of prior work on C3Ms and protein-based assemblies. The systematic exploration of design parameters for mdIDPs is a useful contribution. However, the fundamental concept of C3Ms is well established, and the novelty lies primarily in the specific application to protein cargo and the design rules derived.
- **Scientific importance** The potential for a fully aqueous, genetically encoded platform for protein nanoparticle assembly with tunable properties is significant for the drug delivery field. If the design rules are robust and generalizable, this could provide a practical alternative to existing formulation approaches. The importance is contingent on the strength of the evidence, which cannot be fully assessed from the text alone.
- **Interdisciplinary readership** The work bridges protein engineering, soft matter physics, and drug delivery. The findings would be of interest to researchers in these fields. The text is written in a way that is accessible to a broad scientific audience, though some familiarity with coacervation and polymer physics is assumed.
- **Technical soundness** The experimental design is thoughtful, with systematic variation of parameters and use of multiple characterization techniques. However, the absence of quantitative data in the provided text prevents a full assessment of technical soundness. The reliance on DLS, FCS, TEM, and SAXS is appropriate, but the consistency of results across techniques and the error analysis cannot be evaluated.
- **Readability for nonspecialists** The manuscript is generally well written and the logic is clear. The introduction provides sufficient context for understanding the motivation. However, some terms (e.g., charge fraction, N+, C3M) are used without full definition, which may hinder nonspecialist readers. The abstract is accessible and conveys the key claims effectively.

## Recommendation posture
Supportive if technical concerns are resolved. The conceptual framework and systematic design approach are promising, and the work addresses a relevant problem in protein delivery. However, the current submission does not provide sufficient quantitative evidence in the text to fully establish the central claims regarding nanoparticle homogeneity, loading capacity, and the proposed charge regulation mechanism. Access to the figures and supplementary data is essential for a complete evaluation. The generalizability claim should be tempered or supported with additional protein cargo testing.