## Review setup
- **Input scope** Full manuscript text (abstract, introduction, results, discussion, conclusions) without supplementary figures, tables, or methods section
- **Assessment boundary** Scientific claims, experimental design logic, data interpretation, and internal consistency as presented in the main text; supplementary materials referenced but not independently verifiable
- **Shared manuscript claim summary** The authors report that a ~33 kDa mini-spidroin engineered with cysteine residues at the edges of polyalanine segments forms high-performance artificial spider silk (tensile strength 531 ± 33 MPa, toughness 182 ± 6 MJ/m³) via disulfide-mediated liquid-liquid phase separation and subsequent acidification and shear-induced β-sheet assembly, outperforming larger recombinant spidroins and approaching native dragline silk toughness
- **Visible evidence base** Mechanical testing data (strength, toughness, modulus), FTIR secondary structure quantification, SEM morphology, AFM phase imaging and nano-indentation, SAXS lamellar spacing, polarized Raman spectroscopy, CD spectroscopy, SEC-MALS, LLPS phase diagrams, ThT fluorescence kinetics, MD simulation force-displacement curves, and β-propensity heatmaps
- **Missing materials affecting confidence** Supplementary figures (S1-S18) and tables (S1-S2) referenced but not provided; detailed methods section absent; raw mechanical testing curves not shown; statistical analysis details (n numbers, error bar definitions, significance tests) not reported; MD simulation parameters and force field details not described; exact amino acid sequences of variants not shown in main text

## Reviewer
- **Overall assessment** This manuscript presents a conceptually interesting approach to addressing a well-known challenge in artificial spider silk production: the difficulty of expressing high-molecular-weight spidroins. The authors propose that site-specific cysteine engineering at polyalanine segment edges can compensate for low molecular weight by enabling disulfide-mediated pre-organization during LLPS. The reported mechanical properties (531 MPa strength, 182 MJ/m³ toughness) are notable for a ~33 kDa construct and would represent a meaningful advance if fully substantiated. However, the manuscript as presented has several significant gaps that prevent full evaluation. The most critical issues are the absence of a methods section, the lack of statistical detail, the incomplete presentation of control experiments, and the reliance on referenced supplementary materials that are not available for assessment. The causal chain from cysteine engineering to LLPS behavior to β-sheet alignment to mechanical performance is plausible but not fully established with the evidence shown. The MD simulations are suggestive but limited in scope, and the relationship between simulated single-crystal behavior and macroscopic fiber mechanics requires more careful articulation. The comparison to literature values, while favorable, needs more rigorous benchmarking against comparable low-molecular-weight systems processed under similar conditions. Overall, the work addresses an important problem with a creative approach, but the current evidence base is insufficient to fully support the strength of the claims made.

- **Who would be interested in the results, and why** Researchers in biomimetic materials, protein engineering, and structural biology would find this work relevant. Specifically, groups working on recombinant silk production, LLPS-mediated assembly of protein materials, and the design of high-performance biofibers would be the primary audience. The demonstration that a small, easily expressible protein can achieve mechanical properties approaching native silk could have practical implications for scalable fiber manufacturing. Additionally, the fundamental insight that disulfide bonds can modulate LLPS behavior and subsequent β-sheet organization may interest researchers studying phase separation in biological systems beyond silk. The work could also attract attention from the broader materials science community interested in sustainable, bio-derived high-performance fibers.

- **Major strengths** 
  1. The conceptual approach of using edge-cysteine engineering to enable disulfide-mediated pre-organization in low-molecular-weight spidroins is creative and addresses a real bottleneck in the field
  2. The reported mechanical properties, particularly toughness of 182 MJ/m³, are impressive for a ~33 kDa construct and would be a significant advance if reproducible
  3. The combination of experimental characterization (FTIR, SAXS, AFM, Raman) with MD simulations provides a multi-scale perspective on the assembly mechanism
  4. The fully aqueous processing route, avoiding organic solvents, represents an environmentally beneficial approach
  5. The demonstration of continuous fiber production (~150 m from 200 mg protein) suggests practical scalability

- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The manuscript claims that C1_MS fibers achieve tensile strength of 531 ± 33 MPa, toughness of 182 ± 6 MJ/m³, and Young's modulus of 12.3 ± 3.6 GPa, representing 2.4-fold, 2.8-fold, and 1.1-fold increases over C1_CS fibers
- **Evidence pointer** Figure 4d, 4e; location not provided
- **Concern** The mechanical testing data are presented only as summary statistics without raw stress-strain curves, sample numbers, or statistical test details. The error bars are not defined (standard deviation vs. standard error), and no information is provided about the number of fibers tested, the number of independent spinning runs, or the variability between batches. The gage length, strain rate, and testing environment are not specified. Without this information, the reported values cannot be independently evaluated, and the claimed differences between conditions cannot be assessed for statistical significance.
- **Why it matters** The central claim of the paper is that the engineered mini-spidroin produces fibers with exceptional mechanical properties. If the mechanical testing methodology is not rigorously documented, the primary quantitative result of the study is not verifiable. This is particularly important given that the reported toughness exceeds that of native Nephila clavipes dragline silk, a claim that requires robust statistical support.
- **Resolution test** Provide complete mechanical testing details including stress-strain curves, number of replicates, statistical analysis (with test names and p-values), and clear definition of error bars. Ideally, include a comparison table with all tested conditions and sample sizes.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The manuscript states that "C1 displayed an immediate fluorescence increase, whereas Ori exhibited a pronounced lag phase before signal development" in ThT assays, and that endpoint measurements confirmed higher β-sheet content in C1 condensates
- **Evidence pointer** Figure 3b, Figure S7c; location not provided
- **Concern** The ThT fluorescence data are described qualitatively without quantitative values, time points, or statistical comparison. The claim of "higher β-sheet content" is based on endpoint measurements, but the absolute values and the difference between C1 and Ori are not reported. Additionally, ThT fluorescence can be influenced by factors other than β-sheet content, such as dye concentration, sample turbidity, and the specific morphology of aggregates. The manuscript acknowledges turbidity issues in condensates, which could confound ThT measurements. No control experiments (e.g., ThT binding in the presence of denaturants, or comparison with a known β-sheet standard) are described.
- **Why it matters** The kinetic difference in β-sheet formation between C1 and Ori is presented as evidence that cysteine engineering promotes ordered pre-assembly. If this claim is not quantitatively supported, the mechanistic narrative of the paper is weakened. The ThT data are also used to support the interpretation of the LLPS-to-fiber transition, making this a key piece of evidence.
- **Resolution test** Provide quantitative ThT fluorescence data with time courses, endpoint values, and statistical analysis. Include appropriate controls to rule out turbidity artifacts. If possible, corroborate β-sheet content with an orthogonal technique such as FTIR or solid-state NMR on the condensates.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The manuscript claims that "disulfide bonds reinforce inter-strand interactions and prevent chain slippage under shear" based on MD simulations showing a rupture force of 23.7 nN for C1, 13% greater than the cysteine-free Ori control
- **Evidence pointer** Figure 5b, 5c, 5d, 5e; location not provided
- **Concern** The MD simulation methodology is not described. No information is provided about the force field, water model, simulation box size, equilibration protocol, pulling rate, or the number of independent simulations. The simulation model uses a 3 × 5 antiparallel polyalanine lattice, which is a highly simplified representation of the actual fiber structure. The relationship between the simulated single-crystal rupture force and the macroscopic fiber mechanical properties is not established. The claim that "disulfide anchoring favors strain-induced ordering rather than disruption" is based on a single simulation condition without systematic variation of pulling direction, rate, or disulfide position.
- **Why it matters** The MD simulations are presented as providing mechanistic insight into the experimental observations. If the simulation methodology is not rigorous and the connection to experiment is not clearly articulated, the mechanistic claims are not supported. The 13% increase in rupture force is a modest effect that may not be statistically significant without replicate simulations.
- **Resolution test** Provide complete simulation details, including force field parameters, system setup, equilibration and production protocols, and the number of replicates. Show that the observed differences are statistically significant. Discuss the limitations of the simplified model and how the simulation results relate to the macroscopic fiber properties.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** Yes
- **Axis** Scientific importance
- **Claim pointer** The manuscript claims that "C1_MS fibers achieved a toughness of 182 MJ/m³, exceeding that of Nephila clavipes dragline silk" and that the approach "surpasses many bulkier (>100 kDa) recombinant spidroins"
- **Evidence pointer** Figure 4f, Table S2; location not provided
- **Concern** The comparison to literature values is presented in a single figure panel and a supplementary table, but the specific references, testing conditions, and sample preparation methods for the literature data are not described in the main text. The comparison to native dragline silk is particularly problematic because native silk properties vary significantly depending on the species, spinning conditions, and testing protocol. The claim that the approach surpasses larger recombinant spidroins requires a systematic comparison with appropriate controls, including fibers spun from the same mini-spidroin without cysteine engineering under identical conditions.
- **Why it matters** The significance of the work depends on the claim that a small construct can outperform larger ones. If the comparison is not rigorous, the importance of the finding is diminished. The toughness value of 182 MJ/m³ is exceptionally high and would benefit from independent verification or at least a more detailed comparison with the literature.
- **Resolution test** Provide a comprehensive comparison table with literature values, including testing conditions, sample preparation, and references. Include a direct comparison of C1_MS with Ori_MS and with at least one high-molecular-weight recombinant spidroin processed under similar conditions. Discuss the variability in native silk properties and how the comparison was made.

- **Concern ID** R1-M5
- **Severity** Major
- **Blocking** No
- **Axis** Technical soundness
- **Claim pointer** The manuscript states that "C1 had a substantially lower LLPS threshold compared to Ori. For instance, at 0.5 M KPi, C1 formed droplets at 10 µm (~0.33 mg/mL), whereas Ori required ~60 µm"
- **Evidence pointer** Figure 2f; location not provided
- **Concern** The phase diagram data are presented without error bars or replicate measurements. The concentration units are unclear (10 µm and 60 µm are presumably protein concentrations, but the units are not specified). The method for determining the LLPS threshold is not described. The relationship between the LLPS threshold and the subsequent fiber properties is not quantitatively established.
- **Why it matters** The claim that cysteine engineering lowers the LLPS threshold is a key part of the mechanistic narrative. If this is not rigorously demonstrated, the proposed mechanism is weakened. The phase diagram is also used to justify the choice of processing conditions.
- **Resolution test** Provide phase diagrams with error bars and replicate measurements. Clearly define the concentration units and the method for determining the LLPS boundary. Show that the difference between C1 and Ori is statistically significant.

- **Concern ID** R1-M6
- **Severity** Major
- **Blocking** No
- **Axis** Technical soundness
- **Claim pointer** The manuscript claims that "AFM phase imaging revealed a homogeneous morphology in C1 with low phase contrast, consistent with a well-integrated crystalline-amorphous network" and that "AFM nano-indentation confirmed greater mechanical homogeneity in C1, showing higher average modulus and reduced spatial variation"
- **Evidence pointer** Figure 5f, Figure S17; location not provided
- **Concern** The AFM data are presented qualitatively without quantitative analysis. The number of images, scan areas, and the criteria for "homogeneous" or "fragmented" are not defined. The nano-indentation data are described as showing "higher average modulus" but the values are not reported. The relationship between surface morphology and bulk mechanical properties is not established.
- **Why it matters** The AFM data are used to support the claim that cysteine engineering improves structural integration. Without quantitative analysis, this claim is not supported. The nano-indentation data could provide important evidence for the mechanical uniformity of the fibers.
- **Resolution test** Provide quantitative AFM analysis, including roughness values, phase contrast distributions, and modulus maps with statistics. Show representative images from multiple regions and fibers. Discuss the limitations of surface characterization for inferring bulk properties.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Readability for nonspecialists
- **Affected element** Abstract
- **Evidence pointer** Abstract; location not provided
- **Issue** The abstract states "surpassing many bulkier (>100 kDa) recombinant spidroins" without specifying which ones or by what margin. This is vague and could be interpreted as overclaiming.
- **Required correction** Provide specific examples or a range of values for comparison, or soften the claim to "comparable to or exceeding" with appropriate references.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Technical soundness
- **Affected element** Figure 1a description
- **Evidence pointer** Figure 1a; location not provided
- **Issue** The description of the three positional variants (C1, C3, C5) states that "we strategically substituted alanine residues at flanking sites of the polyA blocks with cysteines" but does not explain the rationale for the specific positions chosen or why these particular variants were selected.
- **Required correction** Add a brief explanation of the design logic, including why these positions were chosen and what differences were expected between C1, C3, and C5.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Technical soundness
- **Affected element** Figure 2a description
- **Evidence pointer** Figure 2a; location not provided
- **Issue** The text states that "C5 exhibited two closely spaced bands near 33 kDa together with markedly reduced yield" but does not explain what these two bands represent or whether this was investigated further.
- **Required correction** Provide a brief interpretation of the two bands (e.g., degradation products, different oligomeric states) or acknowledge that this was not further characterized.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Technical soundness
- **Affected element** Figure 3c, 3d description
- **Evidence pointer** Figure 3c, 3d; location not provided
- **Issue** The description of the microfluidic spinning process mentions "systematically tuning the flow-rate ratio" but does not provide the specific ratios tested or the rationale for the chosen range.
- **Required correction** Provide the range of flow-rate ratios tested and explain how the optimal conditions were identified.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Readability for nonspecialists
- **Affected element** Introduction
- **Evidence pointer** Introduction, paragraph 3; location not provided
- **Issue** The introduction discusses the "modular domain architecture of spidroins" and the roles of NTD and CTD without clearly defining these terms for readers who may not be familiar with spidroin biology.
- **Required correction** Briefly define N-terminal domain (NTD) and C-terminal domain (CTD) and their functions in the context of silk assembly.

- **Concern ID** R1-m6
- **Severity** Minor
- **Axis** Technical soundness
- **Affected element** Figure 4g description
- **Evidence pointer** Figure 4g; location not provided
- **Issue** The FTIR analysis reports β-sheet content of ~44% and β-turn content of ~23% for C1_MS fibers, but the error bars and the number of independent measurements are not reported.
- **Required correction** Provide the number of replicate measurements and the uncertainty in the secondary structure quantification.

- **Concern ID** R1-m7
- **Severity** Minor
- **Axis** Technical soundness
- **Affected element** Figure 5g description
- **Evidence pointer** Figure 5g; location not provided
- **Issue** The SAXS data show a shift in the lamellar scattering peak from 0.47 nm⁻¹ in Ori to 0.57 nm⁻¹ in C1, but the interpretation of this shift as a 17% decrease in inter-lamellar spacing assumes a specific structural model that is not described.
- **Required correction** Briefly describe the structural model used to interpret the SAXS data and acknowledge any assumptions.

- **Concern ID** R1-m8
- **Severity** Minor
- **Axis** Readability for nonspecialists
- **Affected element** Conclusions
- **Evidence pointer** Conclusions; location not provided
- **Issue** The conclusion states that the approach "offers a scalable and environmentally benign approach" but does not discuss potential limitations or challenges for scale-up.
- **Required correction** Add a brief discussion of limitations, such as the current production rate, cost considerations, or potential issues with reproducibility at scale.

## Risk / unsupported claims
- The claim that C1_MS fibers achieve toughness exceeding native Nephila clavipes dragline silk is not fully supported without detailed comparison of testing conditions and sample preparation
- The mechanistic claim that disulfide bonds "prevent chain slippage under shear" is based on simplified MD simulations that may not capture the complexity of the full fiber system
- The claim that cysteine engineering "lowers the LLTS threshold" is based on phase diagrams without error bars or replicate measurements
- The statement that the approach "surpasses many bulkier (>100 kDa) recombinant spidroins" is vague and not supported by a systematic comparison
- The claim that "disulfide-mediated LLTS promoted early ordering within the polyA-rich domains" is inferred from indirect evidence (ThT fluorescence, CD) and is not directly demonstrated
- The assertion that the fiber architecture "closely resembled native spider silk" is based on qualitative SAXS and AFM observations and requires more quantitative comparison
- The reported 2.4-fold, 2.8-fold, and 1.1-fold improvements of C1_MS over C1_CS are not supported by statistical analysis
- The claim that the approach provides "a practical and scalable route" is not supported by any cost, yield, or scale-up analysis