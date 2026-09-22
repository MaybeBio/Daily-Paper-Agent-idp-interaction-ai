## Review setup

- **Input scope** Full manuscript text including abstract, introduction, results sections, discussion, funding, author contributions, and acknowledgments. Supplementary figure and table references are noted but supplementary materials were not provided.
- **Assessment boundary** Scientific claims, methodological soundness, evidence quality, and alignment with Nature-style criteria. No assessment of editorial fit or publication policy.
- **Shared manuscript claim summary** The authors claim that de novo designed protein interfaces can control metal-carbonate mineralization across multiple scales: polymorph selection (aragonite vs calcite), templating over reconfigurable 2D arrays, and confined nucleation within protein cages. They further claim that a designed D3 cage templating CoCO3 produces electrocatalytically active hybrid materials for oxygen evolution.
- **Visible evidence base** Main text figures referenced (Fig. 1a–e, 2a–g, 3a–i, 4a–i, 5a–n), supplementary figures and tables referenced but not provided (Fig. S1–S34, Tables S1–S3), XRD patterns, optical micrographs, TEM/HRTEM with FFT analyses, CD spectra, SEC traces, ATR-FTIR kinetics, cryo-EM reconstruction, and electrochemical measurements.
- **Missing materials affecting confidence** Supplementary figures and tables (S1–S34, Tables S1–S3) are referenced extensively but not provided. Experimental methods section is absent. Detailed parameters for RFdiffusion2-repeat training, LigandMPNN design, and electrochemical protocols are not described. Raw data and statistical analyses are not available.

## Reviewer

- **Overall assessment** This manuscript presents an ambitious and potentially significant advance in de novo protein design for biomineralization. The authors demonstrate polymorph control, 2D array templating, and cage-confined mineralization, extending prior work on designed mineral-binding proteins. The claims are bold and the scope is broad. However, the evidence base as provided is incomplete. Several key claims, particularly regarding aragonite selectivity, 2D array templating of calcite, and electrocatalytic activity, rely on data presented in supplementary materials that were not available for review. The manuscript would benefit from clearer quantitative comparisons, additional controls, and more rigorous statistical treatment. The work is likely of high interest to the protein design and biomineralization communities, and potentially to broader materials science and catalysis audiences, but the current evidence does not fully establish all claims.
- **Who would be interested in the results, and why** Protein designers and computational biologists will be interested in the extension of RFdiffusion2 to mineral interface design. Biomineralization researchers will value the demonstration of polymorph control and 2D array templating with designed proteins. Materials scientists and catalysis researchers may be interested in the protein-cage CoCO3 electrocatalyst. The work also has potential relevance for synthetic biology and sustainable materials communities.
- **Major strengths** The work addresses a challenging and important problem: achieving programmable control over inorganic mineralization using designed proteins. The use of RFdiffusion2 for mineral interface design is novel and represents a methodological advance. The demonstration of aragonite selectivity, 2D array templating, and cage-confined CoCO3 formation, if fully supported, would be significant. The electrocatalytic activity of the hybrid material adds a functional dimension that strengthens the impact. The writing is clear and the logical flow from design to characterization to function is commendable.
- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence sufficiency
- **Claim pointer** "ARAG64 produced needle-like aragonite crystals... whereas FD11 produced rhombohedral calcite crystals... These results demonstrate that de novo designed proteins can direct polymorph outcome in CaCO3 mineralization."
- **Evidence pointer** Figure 2c–g, Figure S3, location not provided
- **Concern** The claim of polymorph selectivity rests on XRD and optical microscopy data. However, the XRD patterns shown in Figure 2c are not quantitatively analyzed. The relative abundance of aragonite vs calcite phases is not quantified, and the optical micrographs in Figure 2d and 2f are not statistically representative. The no-protein control shows mixed phases, but the proportion of each phase is not reported. The claim that ARAG64 "selectively" promotes aragonite requires quantitative phase analysis, such as Rietveld refinement or peak intensity ratios, across multiple independent experiments.
- **Why it matters** Polymorph selectivity is a central claim of the manuscript. Without quantitative evidence, the reader cannot assess the degree of selectivity or its reproducibility. The claim of "selective" formation is stronger than what the current evidence supports.
- **Resolution test** Provide quantitative XRD phase analysis (e.g., weight fractions of aragonite vs calcite) for ARAG64, FD31, and no-protein controls across at least three independent replicates. Report standard deviations and statistical significance. If possible, include Raman spectroscopy or electron diffraction as complementary evidence.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence sufficiency
- **Claim pointer** "CALC_HEX24 arrays induce localized, protein-templated calcite mineralization."
- **Evidence pointer** Figure 3e–i, Figures S5–S10, location not provided
- **Concern** The claim that CALC_HEX24 arrays template calcite mineralization is based on HRTEM of small nanoparticles (5–10 nm) and larger crystals (up to 2 μm). The FFT analyses are used to index lattice spacings, but the assignment of the 3.02 Å and 2.41 Å spacings to calcite (104) and (110) is not definitive without additional confirmation. The claim of "localized" templating is supported by AFM showing crystals on protein array layers, but the specificity of this localization is not quantified. The control experiments (no protein, BSA) are referenced in supplementary figures but not described in the main text. The distinction between templated and non-templated mineralization is not rigorously established.
- **Why it matters** The 2D array templating is a key advance over previous work. If the evidence for templated calcite formation is not robust, the claim of "reconfigurable two-dimensional arrays which template calcite nanocrystals" is weakened. The reader needs to be convinced that the protein array is actively directing mineralization rather than passively coexisting with it.
- **Resolution test** Provide quantitative analysis of crystal size distribution, location relative to protein arrays, and phase identification using multiple techniques (e.g., selected area electron diffraction, electron energy loss spectroscopy). Include statistical comparison of mineralization outcomes between CALC_HEX24 arrays, non-arrayed CALC_HEX24, and negative controls. Show that crystals are preferentially associated with protein arrays.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence sufficiency
- **Claim pointer** "COCA46... selectively forms aragonite... and the designed protein interface directs CoCO3 mineralization."
- **Evidence pointer** Figure 4a–i, Figures S11–S21, location not provided
- **Concern** The claim that COCA46 directs CoCO3 mineralization is based on ATR-FTIR kinetics and HRTEM of the final products. The FTIR data show carbonate-associated signal accumulation, but the assignment of these signals to specific carbonate species is not detailed. The HRTEM lattice spacings (2.74 Å and 1.95 Å) are assigned to CoCO3 (104) and (202), but the (202) reflection is a second-order reflection of (101), and its appearance is used to support "engagement of the intended non-natural facet." This is a weak argument, as second-order reflections can arise from multiple orientations. The claim that the designed interface is "required" for CoCO3 formation is supported by the H→N mutant control, but the mutant may have altered overall stability or folding, not just the designed interface. The no-protein control producing amorphous precipitates is useful, but the comparison to FD31 is not fully described.
- **Why it matters** The extension to a non-biological carbonate is a significant claim. If the evidence for CoCO3 formation and the role of the designed interface is not robust, the broader applicability of the design strategy is called into question. The reader needs to be confident that the observed crystalline product is indeed CoCO3 and that the protein interface is specifically responsible.
- **Resolution test** Provide more definitive phase identification of CoCO3, such as X-ray photoelectron spectroscopy or extended X-ray absorption fine structure. Include a detailed characterization of the H→N mutant to show that it folds correctly and only differs at the designed interface. Quantify the yield and size distribution of CoCO3 particles under different conditions.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence sufficiency
- **Claim pointer** "COCA_BRL11 acts as a protein container that templates and confines CoCO3 crystal formation within a defined oligomeric framework."
- **Evidence pointer** Figure 5a–j, Figures S22–S31, Table S2–S3, location not provided
- **Concern** The claim that COCA_BRL11 confines CoCO3 within its interior is based on cryo-EM reconstruction showing additional density in the cavity. However, the resolution of the reconstruction is not stated, and the assignment of the additional density to CoCO3 is speculative. The cryo-EM data are referenced in supplementary figures but not described in sufficient detail. The claim of "confinement" requires evidence that the CoCO3 is indeed inside the cage and not merely associated with the exterior. The size distribution of the nanoparticles is described as "homogeneous," but quantitative data are not provided.
- **Why it matters** Confinement within a designed cage is a novel and potentially powerful capability. If the evidence for internal mineralization is not convincing, the claim of "bounded geometric confinement" is not established. The reader needs to be confident that the cage is actively constraining crystal growth.
- **Resolution Test** Provide the resolution of the cryo-EM reconstruction and a difference map showing the additional density. Use energy-dispersive X-ray spectroscopy or electron energy loss spectroscopy in scanning transmission electron microscopy to confirm the elemental composition of the internal density. Quantify the size distribution of the internal nanoparticles and compare to the cage interior dimensions.

- **Concern ID** R1-M5
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence sufficiency
- **Claim pointer** "COCA_BRL11-mineralized CoCO3 sustained oxygen evolution reaction (OER) activity under alkaline conditions."
- **Evidence pointer** Figure 5k–n, Figures S32–S34, location not provided
- **Concern** The electrochemical data are presented as "collision events" with mean amplitudes of 25 pA and durations of 0.54 ms. The interpretation of these events as OER is not fully justified. The controls (BSA, H→N mutant, DHR46) show initial responses but fail to sustain activity, but the basis for "sustained" activity is not defined. The electrochemical measurements appear to be single-particle collision experiments, which are complex and can be influenced by many factors. The claim that the hybrid material is an "electrocatalyst" requires more rigorous electrochemical characterization, such as Tafel analysis, overpotential measurements, and comparison to standard OER catalysts.
- **Why it matters** The functional claim of electrocatalytic activity is a significant addition to the manuscript. If the electrochemical evidence is not robust, the claim of "functional hybrid bioinorganic materials" is weakened. The reader needs to be confident that the observed activity is due to the CoCO3-protein hybrid and not to artifacts of the measurement.
- **Resolution Test** Provide a more complete electrochemical characterization, including cyclic voltammetry, linear sweep voltammetry, and chronoamperometry on bulk electrodes. Report overpotential at a defined current density, Tafel slope, and Faradaic efficiency. Include control experiments with the protein alone, CoCO3 alone, and physical mixtures.

- **Concern ID** R1-M6
- **Severity** Major
- **Blocking** No
- **Axis** Methodological transparency
- **Claim pointer** "We fine-tuned RFdiffusion2 on repeat protein scaffolds" and "we positioned glutamate residues so that the oxygen atoms at the end of each carboxylate group aligned with the oxygen atoms of carbonate groups on the mineral surface."
- **Evidence pointer** Methods section not provided, Figure 1a–b, location not provided
- **Concern** The methods for fine-tuning RFdiffusion2, training data composition, and the specific design protocol are not described. The criteria for "tip-atom guided" design and the selection of facet-specific alignments are not detailed. The manuscript states that scripts will be available at publication, but for review purposes, the methodological details are insufficient to assess reproducibility.
- **Why it matters** The computational design approach is a central contribution. Without detailed methods, the reader cannot evaluate the novelty of the approach or its generalizability. The claim of "fine-tuning" RFdiffusion2 requires a description of the training procedure, data, and hyperparameters.
- **Resolution Test** Provide a detailed methods section describing the RFdiffusion2 fine-tuning procedure, including training data, loss functions, and validation. Describe the design protocol for each target facet, including the criteria for residue placement and the use of LigandMPNN. Provide access to the design scripts and weights for review.

- **Concern ID** R1-M7
- **Severity** Major
- **Blocking** No
- **Axis** Experimental design
- **Claim pointer** "The disassembly of the arrays at low salt... enables convenient soluble expression and purification of the single-component array."
- **Evidence pointer** Figure 3c, Figure S5, location not provided
- **Concern** The claim of reversible assembly is based on negative-stain EM and dilution experiments. However, the reversibility is not quantitatively demonstrated. The manuscript states that arrays disassemble upon dialysis and reassemble upon salt addition, but the efficiency of reassembly and the structural fidelity of the reassembled arrays are not shown. The claim of "convenient" purification is subjective and not supported by yield or purity data.
- **Why it matters** The reversible assembly is presented as a practical advantage. If the reassembly is not efficient or the arrays are not structurally identical, the practical utility is diminished. The reader needs to see quantitative data on assembly/disassembly cycles.
- **Resolution Test** Provide quantitative data on the fraction of protein in assembled vs. disassembled states as a function of salt concentration. Show that reassembled arrays have the same lattice parameters and order as the original arrays. Report yields and purity for the purification process.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Abstract
- **Evidence pointer** Abstract, location not provided
- **Issue** The abstract states "we show that de novo designed protein interfaces can be assembled into reconfigurable two-dimensional arrays which template calcite nanocrystals." The term "reconfigurable" is not defined in the abstract or introduction. It is unclear whether this refers to the salt-dependent assembly described later or to some other property.
- **Required correction** Define "reconfigurable" in the abstract or introduction, or use a more precise term such as "salt-responsive" or "conditionally assembling."

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Introduction
- **Evidence pointer** Introduction, location not provided
- **Issue** The introduction states "we focused on metal carbonates as particularly compelling targets because they are central both to the biogeochemical carbon cycle and to broader materials applications." The connection between the biogeochemical carbon cycle and the specific applications described later (electrocatalysis) is not made explicit.
- **Required correction** Briefly explain why metal carbonates are relevant to the carbon cycle and how this relevance connects to the applications pursued in the manuscript.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Technical detail
- **Affected element** Figure 2c
- **Evidence pointer** Figure 2c, location not provided
- **Issue** The XRD patterns in Figure 2c are not labeled with the specific peaks. The text mentions a characteristic aragonite peak near 27.2° and a calcite peak near 29.4°, but the figure should clearly indicate these peaks.
- **Required correction** Add peak labels to Figure 2c and include a legend identifying the aragonite and calcite reflections.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Technical detail
- **Affected element** Figure 3e–f
- **Evidence pointer** Figure 3e–f, location not provided
- **Issue** The HRTEM images in Figure 3e–f show lattice fringes, but the scale bars are not visible in the provided text. The reader cannot assess the size of the nanoparticles or the lattice spacing without scale bars.
- **Required correction** Ensure all HRTEM images include clear scale bars and indicate the magnification.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Statistical rigor
- **Affected element** Figure 4f
- **Evidence pointer** Figure 4f, location not provided
- **Issue** The FTIR kinetic profiles in Figure 4f show differences between conditions, but no error bars or statistical analysis are presented. The reader cannot assess the variability or significance of the differences.
- **Required correction** Add error bars (e.g., standard deviation or standard error) to the kinetic profiles and report the number of independent replicates. Perform and report appropriate statistical tests.

- **Concern ID** R1-m6
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Discussion
- **Evidence pointer** Discussion, location not provided
- **Issue** The discussion states "the results establish de novo design as a tractable route to recreate some of the most distinctive features of biological mineralization." This is a strong claim. The manuscript demonstrates control over polymorph, array templating, and confinement, but does not address other features of biological mineralization such as hierarchical organization or mechanical properties.
- **Required correction** Soften the claim or provide a more nuanced statement that acknowledges the specific features demonstrated and the remaining challenges.

- **Concern ID** R1-m7
- **Severity** Minor
- **Axis** Technical detail
- **Affected element** Figure 5k
- **Evidence pointer** Figure 5k, location not provided
- **Issue** The electrochemical data in Figure 5k are presented as current vs. time traces. The potential at which these measurements were performed is not stated in the text. The reader cannot assess the relevance of the observed events without knowing the applied potential.
- **Required correction** State the applied potential and the reference electrode used in the electrochemical measurements.

- **Concern ID** R1-m8
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Author contributions
- **Evidence pointer** Author contributions, location not provided
- **Issue** The author contributions list "ZM, DL" in the methodology section, but these initials do not appear in the author list provided. This may be a typographical error.
- **Required correction** Verify the author initials in the contributions section and correct any errors.

## Risk / unsupported claims

- The claim of "selective" aragonite formation by ARAG64 is not quantitatively supported. The XRD data are not analyzed for phase fractions, and the optical microscopy is not statistically representative.
- The claim that CALC_HEX24 arrays "induce localized, protein-templated calcite mineralization" is not fully supported. The specificity of localization and the active role of the protein array are not rigorously demonstrated.
- The claim that COCA46 directs CoCO3 mineralization is based on limited evidence. The FTIR signal assignment is not detailed, and the HRTEM phase identification relies on a second-order reflection.
- The claim that COCA_BRL11 "confines" CoCO3 within its interior is not fully supported. The cryo-EM reconstruction resolution is not stated, and the assignment of internal density to CoCO3 is speculative.
- The claim of "sustained" OER activity for the COCA_BRL11-CoCO3 hybrid is not rigorously defined. The electrochemical data are presented as collision events, and the basis for "sustained" activity is unclear.
- The methodological details for RFdiffusion2 fine-tuning and design are not provided, making the computational approach not reproducible from the current manuscript.
- The claim that "the results establish de novo design as a tractable route to recreate some of the most distinctive features of biological mineralization" is broader than what the evidence supports.

## Assessment against Nature-style criteria

- **Originality** The work is original in its application of RFdiffusion2 to mineral interface design and in the demonstration of polymorph control, 2D array templating, and cage-confined mineralization. The extension to a non-biological carbonate (CoCO3) is novel. However, the conceptual framework of lattice-matched protein design for mineralization is built on prior work by the same group, and the incremental advance, while significant, is not entirely unprecedented.
- **Scientific importance** The work addresses a fundamental challenge in biomineralization and protein design. If fully supported, the results would represent a significant advance in the ability to program mineral formation with designed proteins. The potential applications in carbon management and electrocatalysis add to the importance. However, the importance is somewhat tempered by the incomplete evidence for some of the central claims.
- **Interdisciplinary readership** The work is likely to appeal to a broad interdisciplinary audience, including protein designers, biomineralization researchers, materials scientists, and catalysis researchers. The potential applications in sustainability and energy are likely to attract interest beyond the immediate field. The writing is generally accessible, though some sections assume familiarity with protein design and mineralization concepts.
- **Technical soundness** The technical approach is sound in principle, but the evidence as presented is incomplete. The lack of quantitative phase analysis, statistical treatment, and detailed methods for the computational design reduces confidence in the technical soundness. The cryo-EM and electrochemical data are not described in sufficient detail to assess their quality.
- **Readability for nonspecialists** The manuscript is generally well-written and the logical flow is clear. The abstract and introduction are accessible. However, some sections, particularly those describing the computational design and the electrochemical measurements, may be challenging for nonspecialists. The figures are referenced but not described in sufficient detail in the text.

## Recommendation posture

**Supportive if technical concerns are resolved.** The manuscript presents a potentially significant advance in de novo protein design for biomineralization. The scope is ambitious and the results, if fully supported, would be of broad interest. However, the current evidence does not fully establish several central claims, particularly regarding polymorph selectivity, 2D array templating, and electrocatalytic activity. The lack of detailed methods and quantitative analyses is a significant concern. The authors should be encouraged to provide a more complete evidence base, including quantitative phase analysis, statistical treatment, and detailed methods, before the claims can be fully evaluated.