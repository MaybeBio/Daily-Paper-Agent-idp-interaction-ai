## Review setup
- **Input scope** Full manuscript text, including abstract, introduction, results, methods, discussion, and supplementary figure descriptions.
- **Assessment boundary** Scientific content, methodological soundness, internal consistency, and support of claims by presented evidence. No assessment of formatting, grammar, or editorial fit.
- **Shared manuscript claim summary** The manuscript uses coarse-grained molecular dynamics simulations and analytical theory to investigate how EPYC1 linker length affects phase separation in the Rubisco-EPYC1 system of the algal pyrenoid. The authors report that shorter linkers decrease critical concentrations by approximately ten-fold, attribute this to a molecular "fit" between EPYC1 and Rubisco, find that native Rubisco sticker locations are optimal for phase separation, and report a transition to a gas of rods when stickers are moved toward the poles.
- **Visible evidence base** Simulation snapshots, density profiles, dissociation constant measurements, order parameter calculations, analytical theory derivations, and comparisons across linker lengths and sticker locations. Figures 1-5 and Supplementary Figures 1-4 are referenced.
- **Missing materials affecting confidence** Simulation parameter files, full trajectory data, error bars on key quantities, details on the number of independent runs for each condition, and the full derivation of the dimer-gel theory are not provided. The manuscript states data/code availability upon request, which limits reproducibility assessment.

## Reviewer
- **Overall assessment** This manuscript addresses a timely and important question in the field of biomolecular condensates: how linker length relative to other molecular length scales controls phase behavior. The Rubisco-EPYC1 system is an excellent model system, and the combination of simulations and theory is appropriate. The central claim that shorter linkers enhance phase separation due to a poorer molecular fit is plausible and supported by the presented data. However, several technical aspects require clarification and additional analysis before the case is fully established. The claim regarding the ten-fold decrease in critical concentrations is based on a specific ratio calculation that needs more careful presentation. The discovery of a gas of rods is intriguing but its characterization is preliminary. The generalization to carboxysomes is speculative and would benefit from more quantitative support. Overall, the work is potentially significant but requires revisions to fully substantiate its conclusions.
- **Who would be interested in the results, and why** Researchers studying biomolecular phase separation, intrinsically disordered proteins, condensate biophysics, and the structure and function of the pyrenoid and carboxysomes. The work provides a general framework for thinking about how linker length and binding site geometry jointly control phase behavior, which is relevant to the broader condensate community. The specific predictions about EPYC1 linker length effects could guide experimental mutagenesis studies.
- **Major Strengths** The manuscript addresses a clear and important question with a well-chosen model system. The combination of coarse-grained simulations and analytical theory is powerful and appropriate. The concept of molecular "fit" between a flexible multivalent protein and a rigid scaffold is a useful and potentially generalizable idea. The systematic variation of linker length and sticker location provides a thorough exploration of parameter space. The writing is generally clear and accessible.
- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** "we observe an approximately ten-fold decrease in the critical densities when comparing the long EPYC1 linker system to the short EPYC1 linker system. (Computed by the ratio of the product of the dilute phase concentrations of EPYC1s and Rubiscos for the long and short EPYC1 linker systems.)"
- **Evidence pointer** Figure 2, Results section, location not provided
- **Concern** The ten-fold decrease in critical densities is a central quantitative claim, but the method of calculation is described only in a parenthetical remark. The product of dilute phase concentrations is not a standard definition of critical density for a two-component system. It is unclear whether this product is evaluated at the binodal boundary, at a specific total concentration, or at some other reference point. The sensitivity of this factor to the choice of definition is not discussed. Furthermore, the critical density is a property of the phase diagram, and it is not clear how it was extracted from the simulation data.
- **Why it matters** The magnitude of the effect of linker length on phase separation is a headline result. If the calculation method is not rigorous or is not clearly defined, the quantitative claim is not verifiable. This undermines the central message of the manuscript.
- **Resolution test** Provide a clear definition of how the critical density was determined from the simulation data. Show the full phase diagram for both linker lengths, with the binodal curves clearly marked. Demonstrate that the ten-fold factor is robust to the method of extracting the critical point. If the product of dilute concentrations is used, justify this choice and show that it is a meaningful measure of the critical point.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** "We found that an EPYC1 with long linkers has a lower Kd (stronger binding) to Rubisco since it can form more sticker-sticker bonds with Rubisco than can an EPYC1 with short linkers."
- **Evidence pointer** Figure 3a, Results section, location not provided
- **Concern** The dissociation constant Kd is measured in a simulation box of 50 nm x 50 nm x 50 nm with a single EPYC1 and a single Rubisco. The binding criterion is that at least one EPYC1 sticker is within the attractive-interaction cutoff distance of a Rubisco sticker. This is a very weak binding criterion. A single sticker-sticker contact may not represent a stably bound complex, especially at finite temperature. The Kd values extracted from this two-state analysis may therefore be highly sensitive to the choice of cutoff and the definition of the bound state. The manuscript does not discuss the sensitivity of Kd to these choices.
- **Why it matters** The Kd values are used to parameterize the dimer-gel theory and to argue that the molecular fit is worse for short linkers. If the Kd measurements are not robust, the theoretical predictions and the mechanistic interpretation are called into question.
- **Resolution test** Perform a sensitivity analysis of Kd with respect to the binding criterion. For example, require two or more sticker-sticker contacts for a bound state, or use a stricter distance cutoff. Show that the qualitative conclusion (long linkers have lower Kd) is robust. Alternatively, use a more rigorous method to compute Kd, such as umbrella sampling or a potential of mean force calculation.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Scientific importance
- **Claim pointer** "Surprisingly, shorter linkers mediate a transition to a gas of rods as Rubisco stickers approach the poles."
- **Evidence pointer** Figure 5, Results section, location not provided
- **Concern** The discovery of a gas of rods is presented as a surprising and novel finding. However, the characterization of this phase is limited to a single order parameter, the average cosine of the angle between neighboring Rubiscos. It is not clear how this phase differs from a simple disordered fluid of Rubiscos. The manuscript does not provide a structural characterization of the rod phase, such as radial distribution functions, cluster size distributions, or a visual representation. The conditions under which this phase forms are only partially explored.
- **Why it matters** The gas of rods is presented as a new phase of matter in this system. Without a more complete structural and thermodynamic characterization, it is difficult to assess whether this is a genuinely distinct phase or an artifact of the specific simulation conditions. This limits the significance of the finding.
- **Resolution test** Provide a more detailed structural analysis of the rod phase, including radial distribution functions, bond orientational order parameters, and representative snapshots. Map out the region of parameter space where this phase forms. Discuss the thermodynamic stability of this phase relative to the dense phase and the dilute phase.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Technical soundness
- **Claim pointer** "Varying Rubisco sticker locations reveals that the native sites yield the poorest fit, thus optimizing phase separation."
- **Evidence pointer** Figure 5, Results section, location not provided
- **Concern** The claim that native sticker locations are optimal for phase separation is based on simulations where sticker locations are moved to 33 degrees and 79 degrees from the poles. It is not clear how these specific alternative locations were chosen. A more systematic exploration of sticker locations would be needed to support the claim of optimality. Furthermore, the manuscript does not discuss whether the alternative sticker locations are physically realistic or accessible by mutation.
- **Why it matters** The claim of optimality is a strong evolutionary statement. If the parameter space has not been thoroughly explored, the conclusion that the native configuration is optimal is not justified.
- **Resolution test** Perform a more systematic scan of sticker locations, or at least test a few additional configurations. Discuss the relationship between the tested locations and the range of possible locations. If a full scan is not feasible, temper the claim of optimality to "near-optimal among tested configurations."

- **Concern ID** R1-M5
- **Severity** Major
- **Blocking** No
- **Axis** Interdisciplinary readership
- **Claim pointer** "In other Rubisco condensates such as carboxysomes found in alpha and beta cyanobacteria, other multivalent linker proteins mediate phase separation and the associated stickers on Rubisco are at different locations than in C. reinhardtii."
- **Evidence pointer** Discussion section, location not provided
- **Concern** The manuscript extends its conclusions to carboxysomes, but the analysis is limited to estimating linker lengths and sticker spacings. The authors do not perform simulations or theory for the carboxysome systems. The claim that the geometry of binding may favor condensates in carboxysomes is speculative and not directly tested.
- **Why it matters** The generalization to carboxysomes is presented as a key implication of the work. If this is not supported by direct evidence, it weakens the broader significance of the manuscript.
- **Resolution test** Either perform simulations for the carboxysome systems with appropriate parameters, or clearly label this section as speculation and discuss the conditions under which the prediction would hold or fail.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Readability for nonspecialists
- **Affected element** Introduction
- **Evidence pointer** Introduction, location not provided
- **Issue** The introduction assumes familiarity with the Rubisco-EPYC1 system and the pyrenoid. A brief description of the biological context and why this system is a good model for studying linker length effects would help nonspecialist readers.
- **Required correction** Add a few sentences describing the pyrenoid, its function, and why the Rubisco-EPYC1 interaction is a tractable model system.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Technical soundness
- **Affected element** Methods, Model details
- **Evidence pointer** Methods, location not provided
- **Issue** The effective linker length is set by a spring constant k, but the relationship between k and the effective length l is not explicitly defined in the main text. The reader is referred to Supplementary Note 1, but the main text should be self-contained.
- **Required correction** Define the effective linker length l in terms of the spring constant k, or state clearly that l is a derived quantity defined in the Supplementary Note.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Technical soundness
- **Affected element** Methods, Dissociation constant Kd
- **Evidence pointer** Methods, location not provided
- **Issue** The simulation time for the Kd measurement is 10 ns. It is not clear if this is sufficient for the system to reach equilibrium, especially for the short linker case where binding may be slower.
- **Required correction** Provide evidence that the Kd measurements have converged, such as a plot of Kd as a function of simulation time, or a discussion of the equilibration time.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Readability for nonspecialists
- **Affected element** Results, Figure 2
- **Evidence pointer** Figure 2, location not provided
- **Issue** The density profiles in Figure 2b and 2d are described as showing "an almost two-fold increase of both EPYC1 and Rubisco stickers in the condensed phase." It is not clear how this increase is quantified from the density profiles.
- **Required correction** State explicitly how the condensed phase density was calculated from the density profiles, and provide the numerical values for both linker lengths.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Technical soundness
- **Affected element** Methods, Dimer-gel theory
- **Evidence pointer** Methods, location not provided
- **Issue** The dimer-gel theory is described as having three terms, but the derivation of the free energy expressions is not provided. The reader cannot assess the validity of the theory without this derivation.
- **Required correction** Provide a more complete derivation of the free energy expressions, or refer to the original references (11, 35) for the full derivation.

- **Concern ID** R1-m6
- **Severity** Minor
- **Axis** Interdisciplinary readership
- **Affected element** Discussion
- **Evidence pointer** Discussion, location not provided
- **Issue** The discussion of evolutionary implications is interesting but brief. A more detailed discussion of how the findings relate to the known biology of the pyrenoid and carboxysomes would strengthen the manuscript.
- **Required correction** Expand the discussion of evolutionary implications, including a consideration of other factors that may influence linker length evolution.

## Risk / unsupported claims
- The claim of a ten-fold decrease in critical densities is not fully supported due to the unclear definition of critical density.
- The claim that native Rubisco sticker locations are "optimal" for phase separation is not fully supported due to the limited exploration of sticker location space.
- The generalization to carboxysomes is speculative and not directly tested.
- The characterization of the "gas of rods" phase is preliminary and requires more detailed structural analysis.
- The Kd values are sensitive to the binding criterion, and their robustness is not demonstrated.
- The relationship between the spring constant k and the effective linker length l is not defined in the main text.
- The convergence of the Kd measurements is not demonstrated.