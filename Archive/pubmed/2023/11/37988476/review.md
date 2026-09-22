## Review setup
- **Input scope** Full manuscript text (abstract, introduction, methods, results, discussion, conclusions) without supplementary material
- **Assessment boundary** Technical soundness, methodological novelty, validation adequacy, and support for stated claims based on the provided text only
- **Shared manuscript claim summary** The authors present a new coarse-grained (CG) DNA model with two or three beads per nucleotide, parameterized to reproduce experimental DNA melting thermodynamics and structural properties. The model is made compatible with the HPS-Urry CG protein model via an all-atom hydropathy scale for protein-DNA cross-interactions. The authors demonstrate the model's utility by simulating a nucleosome with and without histone tails and investigating the role of histone tails in modulating liquid-liquid phase separation (LLPS) of HP1α proteins.
- **Visible evidence base** Main text figures (Figures 1-9), tables (Tables 1-5), and equations (Eqs 1-9); references to supplementary figures, tables, and movies
- **Missing materials affecting confidence** Supplementary Information (SI) including Tables S1-S5, Figures S1-S9, and Movies S1-S2; experimental data sources for melting temperature and structural properties; simulation input files or parameter tables with full numerical values; convergence and error analysis details

## Reviewer

- **Overall assessment** The manuscript presents a useful and potentially transferable CG DNA model that addresses a real gap in the field, namely the compatibility of CG DNA models with existing CG protein models for studying protein-DNA interactions and LLPS. The parameterization strategy is reasonable, and the validation against experimental melting temperatures and structural properties is encouraging. The nucleosome simulations and the LLPS analysis provide a compelling demonstration of the model's capabilities. However, several technical concerns need to be addressed, particularly regarding the transferability of the hydropathy-based cross-interaction parameters, the sensitivity of results to parameter choices, and the interpretation of the LLPS findings given the simplified representation of the nucleosome. The manuscript is generally well-written and accessible, though some methodological details require clarification.

- **Who would be interested in the results, and why** Researchers in computational biophysics, particularly those studying protein-DNA interactions, chromatin structure and dynamics, and biomolecular phase separation. The model's compatibility with the widely used HPS-Urry protein model makes it potentially attractive for the LLPS community. Additionally, researchers in DNA nanotechnology and those interested in multiscale simulation methods would find the approach relevant.

- **Major strengths** 
  1. The development of a CG DNA model that is directly compatible with an established CG protein model (HPS-Urry) addresses a practical need in the field.
  2. The parameterization strategy using experimental melting data and structural properties is systematic and transparent.
  3. The use of an all-atom hydropathy scale to define protein-DNA cross-interactions is a novel and potentially transferable approach that avoids system-specific reparameterization.
  4. The demonstration of the model on a full nucleosome system, including the analysis of histone tail effects on DNA unwrapping and HP1α LLPS, showcases the model's utility for biologically relevant questions.
  5. The reported computational speedup compared to all-atom simulations is significant and practically important.

- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness of cross-interaction parameterization
- **Claim pointer** The authors claim that using the all-atom hydropathy scale to define protein-DNA nonbonded interactions makes the model "compatible" with the HPS-Urry protein model and that this approach avoids system-specific reparameterization, thereby improving transferability.
- **Evidence pointer** Section "Protein–DNA Cross-Interactions", Section "CG DNA–Protein Interaction Parameters in the HPS Modeling Framework", Table 5, Figure 5
- **Concern** The cross-interaction parameters are derived from hydropathy values assigned to DNA beads based on CHARMM27 partial charges, but the mapping from atomic partial charges to a single hydropathy value per nucleotide bead is not described in sufficient detail. The authors state that the KR hydropathy scale is used "similar to" the approach for amino acids, but the specific algorithm for assigning hydropathy to the sugar-phosphate backbone bead versus the base bead is unclear. Furthermore, the validation of the cross-interaction parameters is limited to a single protein-DNA system (C-terminus of histone H1 with a 20-bp dsDNA). The claim of transferability is therefore not well-supported by the evidence presented.
- **Why it matters** The transferability of the cross-interaction parameters is a central claim of the manuscript and is critical for the model's utility in studying diverse protein-DNA systems. If the hydropathy-based assignment is not robust or if the validation is too narrow, the model's applicability is questionable.
- **Resolution test** The authors should provide a detailed description of the hydropathy assignment procedure, including a clear mapping from atomic partial charges to bead-level hydropathy values. They should also validate the cross-interaction parameters on at least one additional, distinct protein-DNA system with known binding affinity, and ideally demonstrate that the model can capture sequence-specific binding preferences.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Adequacy of validation for LLPS claims
- **Claim pointer** The authors claim that their simulations provide "molecular insights into the role of histone tails in influencing the liquid-liquid phase separation (LLPS) of HP1α proteins" and that histone tails "antagonize the contacts between HP1α and DNA, thus affecting the ability of DNA to promote LLPS of HP1α."
- **Evidence pointer** Section "Molecular Insights into the Role of Histone Tails in Modulating LLPS of HP1α Proteins", Figure 9, SI Figures S6-S9
- **Concern** The LLPS simulations are performed with a single nucleosome and 50 HP1α chains in a box of 17 × 17 × 100 nm³. This is a very small system for studying phase separation, and finite-size effects are likely to be significant. The authors report concentration profiles and contact maps, but do not provide a rigorous analysis of whether the observed behavior represents equilibrium phase separation or a kinetically trapped state. The comparison between "free DNA" and "nucleosome" conditions is also complicated by the fact that the free DNA is a single 20-bp fragment, whereas the nucleosomal DNA is ~147 bp wrapped around the histone core. The claim that histone tails "antagonize" HP1α-DNA contacts is inferred from contact maps, but the statistical significance of these differences is not assessed.
- **Why it matters** The LLPS application is a key demonstration of the model's utility. If the simulations are not adequately converged or if the system size is too small to draw reliable conclusions about phase behavior, the biological insights claimed may not be robust.
- **Resolution test** The authors should perform simulations with multiple system sizes to assess finite-size effects, and/or provide a more rigorous analysis of phase coexistence (e.g., using slab geometry with a larger box, or computing binodals). They should also provide error bars or statistical analysis for the contact maps and concentration profiles, and discuss the sensitivity of their conclusions to the choice of simulation parameters (e.g., temperature, salt concentration).

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Model limitations and parameter sensitivity
- **Claim pointer** The authors state that the model "provides a reasonable description of various aspects of dsDNA, including Watson-Crick base pairing, melting, hybridization, and major and minor grooves" and that it can be used for "micrometer-scale studies with sub-nm resolution."
- **Evidence pointer** Section "Parameterization Strategy of the CG DNA Models", Section "Melting Behavior of dsDNA", Section "Structural Properties of dsDNA", Tables 2-4, Figure 4
- **Concern** The model is parameterized using a single 14-bp DNA sequence at a single salt concentration (120 mM). The authors demonstrate sequence-dependent melting for a few additional sequences (SI Table S5), but the sensitivity of the model to salt concentration is not systematically explored. The model's ability to capture salt-dependent effects, which are crucial for protein-DNA interactions and LLPS, is not demonstrated. Additionally, the model does not include explicit ions or a treatment of ion competition, which may limit its applicability to physiological conditions where ion concentrations vary.
- **Why it matters** The model's predictive power for biologically relevant conditions depends on its ability to capture salt-dependent behavior. If the model is only valid at a narrow range of salt concentrations, its utility for studying chromatin and LLPS, where salt conditions vary, is limited.
- **Resolution test** The authors should test the model at different salt concentrations and compare the predicted melting temperatures and structural properties with experimental data. They should also discuss the limitations of the implicit-solvent treatment and the potential impact on the model's applicability.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity of methods
- **Affected element** Simulation protocol details
- **Evidence pointer** Section "Large-Scale Langevin Dynamics Simulations of Nucleosomes and LLPS"
- **Issue** The description of the LLPS simulation setup is incomplete. The authors state that they placed 50 HP1α chains and one nucleosome in a box, but do not specify the initial configuration of the HP1α chains (e.g., random distribution, pre-formed condensate), the equilibration protocol, or the criteria used to determine that the system reached steady state.
- **Required correction** Provide a more detailed description of the simulation setup, including initial conditions, equilibration procedure, and criteria for assessing convergence.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Statistical analysis
- **Affected element** Contact maps and concentration profiles
- **Evidence pointer** Figure 9, SI Figures S6-S9
- **Issue** The contact maps and concentration profiles are presented as single snapshots or averages, but no error estimates or statistical analysis are provided. It is unclear whether the observed differences between conditions (e.g., with and without histone tails) are statistically significant.
- **Required correction** Provide error bars or confidence intervals for the reported quantities, and perform statistical tests to assess the significance of observed differences.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Comparison with previous work
- **Affected element** Discussion of nucleosome dynamics
- **Evidence pointer** Section "DNA Repositioning around the Histone Core", Figure 8
- **Issue** The authors compare their findings on DNA repositioning with previous studies, but the comparison is somewhat superficial. The free energy surfaces shown in Figure 8 are not quantitatively compared with previous results, and the authors do not discuss whether the observed preference for the loop propagation model is consistent with the specific DNA sequence used.
- **Required correction** Provide a more quantitative comparison with previous studies, and discuss the potential influence of DNA sequence on the observed repositioning mechanism.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Readability
- **Affected element** Figure 1
- **Evidence pointer** Figure 1
- **Issue** The schematic in Figure 1 is not fully described in the text. The relationship between the 2-bead and 3-bead models and the placement of the hydrogen-bonding beads is not immediately clear from the figure alone.
- **Required correction** Add a more detailed figure caption or refer to the figure more explicitly in the text to guide the reader.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Completeness of parameter reporting
- **Affected element** Tables 2-5
- **Evidence pointer** Tables 2-5
- **Issue** The parameter tables list values for the optimized parameters, but the units are not always explicitly stated. Additionally, the relationship between the parameters in the tables and the equations in the methods section is not always clear.
- **Required correction** Ensure that all parameters are reported with appropriate units and that the connection between the tables and the equations is explicitly stated.

## Risk / unsupported claims
- The claim that the model is "suitable to facilitate micrometer-scale studies with sub-nm resolution" is not directly demonstrated in the manuscript. The largest system simulated is a single nucleosome with 50 HP1α chains, which is far from micrometer scale.
- The claim that the model "can be applied to investigate the mechanisms of DNA hybridization, protein-DNA binding, and nucleosome modeling and explore the origins of binding affinities between proteins and specific DNA sequences" is presented as a general statement of applicability, but the validation is limited to a single protein-DNA system and a few DNA sequences.
- The statement that "histone tails interact favorably with DNA, influencing the conformational ensemble of the DNA and antagonizing the contacts between HP1α and DNA" is supported by the simulation data, but the statistical significance of these findings is not established.
- The claim that the model "does not require tuning process to define protein-DNA interactions for better transferability of parameters" is not fully supported, as the validation is limited to one system and the sensitivity of the results to the hydropathy assignment is not explored.