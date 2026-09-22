## Review setup
- **Input scope** Full manuscript text, including abstract, introduction, results, discussion, materials and methods, and data availability statements.
- **Assessment boundary** Structural characterisation of a non-canonical CP12 protein from *Thalassiosira pseudonana* using a combination of AlphaFold prediction, SDSL-EPR (cw-EPR and DEER), SAXS, and MD simulations; functional implications for Calvin cycle regulation in diatoms.
- **Shared manuscript claim summary** The authors claim that (i) the tp-CP12 dimer is organised in an antiparallel arrangement of the coiled-coil region, (ii) the C-terminal regions are highly flexible and partly disordered, contrary to the AlphaFold prediction, (iii) the protein contains four structured domains likely to bind phosphoribulokinase (PRK) regardless of redox state, and (iv) the structural organisation of this diatom CP12 is completely different from homologous counterparts in Plantae and cyanobacteria.
- **Visible evidence base** Abstract, full results section with figures referenced (Figs 1-5, S1-S7), discussion, materials and methods, data availability statements.
- **Missing materials affecting confidence** Raw EPR spectra and DEER time-domain data; SAXS data files; MD simulation parameters and force field details; AlphaFold confidence maps (pLDDT plots); sequence alignment details; experimental validation of PRK binding; statistical analysis of distance distributions; details of the manual modification of the AF2 model.

## Reviewer

### Overall assessment
This manuscript presents a technically sophisticated combination of experimental and computational approaches to characterise the structure and dynamics of an atypical CP12 protein from a diatom. The work addresses a genuine gap in knowledge, as diatom CP12 proteins have been scarcely studied and their structural organisation remains poorly understood. The authors provide convincing evidence for the antiparallel organisation of the coiled-coil domain and demonstrate that the C-terminal regions are more flexible than predicted by AlphaFold. However, several concerns need to be addressed, particularly regarding the validation of the modified starting model, the interpretation of DEER distance distributions, the convergence of MD simulations, and the strength of the claims regarding PRK binding. The manuscript would benefit from clearer presentation of the experimental data and a more cautious interpretation of the functional implications.

### Who would be interested in the results, and why
Researchers studying intrinsically disordered proteins, photosynthetic regulation, CP12 biology, and the application of integrative structural biology approaches. The work is also relevant to those interested in the limitations and appropriate use of AlphaFold predictions for flexible and oligomeric proteins. The methodological framework combining EPR, SAXS, and MD simulations will be of interest to the structural biology community.

### Major strengths
1. The combination of multiple complementary techniques (SDSL-EPR, DEER, SAXS, MD) provides a robust integrative approach to characterise a challenging protein system.
2. The study addresses an important biological question regarding the structural organisation of a poorly characterised CP12 from a major phytoplankton group.
3. The authors critically evaluate the limitations of AlphaFold predictions and demonstrate the value of experimental validation.
4. The data deposition is commendable, with models and ensembles made publicly available.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors state that they "manually modified the AF2 model by moving away the two C-termini from the coiled-coil region" to generate the starting structure for MD simulations.
- **Evidence pointer** Materials and methods, "Refinement by molecular dynamics simulations"; Figure S5
- **Concern** The manual modification of the AF2 model is a critical step in the workflow, yet the details of this modification are insufficiently described. The authors do not specify the extent of the movement, the criteria used to determine the new positions, or whether this modification was guided by any experimental data. This introduces a potential source of bias in the refinement process. The modified structure should be validated, for example by checking for steric clashes, maintaining reasonable backbone geometry, and ensuring that the modification does not disrupt the overall fold in an unrealistic manner.
- **Why it matters** The starting structure of MD simulations significantly influences the resulting conformational ensemble. If the manual modification is arbitrary or biased, the final ensemble may not represent the true conformational space of the protein, undermining the validity of the conclusions drawn from the MD analysis.
- **Resolution test** Provide a detailed description of the modification procedure, including the specific dihedral angles modified, the rationale for the new positions, and validation of the modified structure (e.g., Ramachandran plot statistics, clash scores). Ideally, the authors should also perform a control simulation starting from the unmodified AF2 model to demonstrate that the final ensemble is not dependent on the initial modification.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors claim that the DEER distance distributions validate the antiparallel organisation of the coiled-coil and reveal the flexibility of the C-terminal regions.
- **Evidence pointer** Results, "Dimer organisation probed by DEER measurements"; Figures 3, S3, S4
- **Concern** The comparison between experimental DEER distance distributions and those predicted from the AF2 model shows significant discrepancies for all positions tested. While the authors interpret these differences as evidence for conformational flexibility, the possibility that the spin labels themselves perturb the local structure or that the labelling efficiency is not uniform across sites is not thoroughly discussed. Additionally, the DEER data for the C150 position show a very broad distribution that extends beyond the reliable detection range, yet the authors use this to draw conclusions about the flexibility of the C-terminus. The quantitative analysis of the distance distributions (e.g., mean distances, widths) is not presented in a systematic manner.
- **Why it matters** DEER is a powerful technique, but its interpretation requires careful consideration of potential artefacts. If the observed discrepancies are due to spin label artefacts rather than genuine conformational differences, the conclusions about the antiparallel organisation and C-terminal flexibility would be weakened.
- **Resolution test** Provide a more detailed analysis of the DEER data, including the quality of the fits, the reliability of the distance ranges, and a discussion of potential spin label artefacts. Consider performing control experiments with different labelling positions or using alternative spin labels to confirm the results. Present the distance distributions in a more quantitative manner, with mean distances and widths for each position.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors claim that the MD simulations, constrained by SAXS and DEER data, provide a refined ensemble of structures that fits the experimental data.
- **Evidence pointer** Results, "Molecular dynamic simulations"; Figures 4, 5
- **Concern** The convergence of the MD simulations is not adequately demonstrated. The authors state that "the simulated distance distributions from the five independent simulations were strikingly similar," but no quantitative measure of convergence is provided. Furthermore, the simulation time of 2 ns for the production runs is relatively short for a protein of this size, and it is unclear whether the conformational space has been adequately sampled. The authors also do not discuss the choice of force field parameters for the spin labels or the potential impact of the CHARMM36m force field on the results.
- **Why it matters** MD simulations are only meaningful if they have converged and adequately sampled the relevant conformational space. If the simulations are too short or have not converged, the resulting ensemble may not be representative, and the conclusions drawn from it would be unreliable.
- **Resolution test** Provide quantitative measures of convergence, such as the root-mean-square deviation of the distance distributions between independent simulations, or block averaging analysis. Consider extending the simulation time or using enhanced sampling techniques to ensure adequate sampling. Discuss the choice of force field parameters and validate the simulation setup.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Scientific importance
- **Claim pointer** The authors state that "this diatom CP12 contains four structured domains likely to bind phosphoribulokinase regardless of their redox state" and that "our structural data therefore provide insights into the function of this protein in the regulation of the Calvin cycle and of photosynthesis in diatoms."
- **Evidence pointer** Abstract; Discussion; Figure 6
- **Concern** The claim that the four structured domains are "likely to bind phosphoribulokinase" is based solely on structural modelling and sequence similarity, without any direct experimental evidence of binding. The authors acknowledge that "further experimental evidence is required," but the claim is presented prominently in the abstract and discussion. The functional significance of the structural findings is therefore overstated.
- **Why it matters** The functional implications of the structural work are a key aspect of the manuscript's significance. If the binding to PRK is not experimentally validated, the claims about the functional relevance of the structural findings are speculative and may mislead readers.
- **Resolution test** Either provide experimental evidence of CP12-PRK binding (e.g., pull-down assays, ITC, or NMR titration) or temper the claims to clearly indicate that the binding is hypothetical and requires experimental validation.

- **Concern ID** R1-M5
- **Severity** Major
- **Blocking** No
- **Axis** Originality
- **Claim pointer** The authors claim that "the structural organisation of this diatom CP12 is completely different from any of its homologous counterparts from Plantae and cyanobacteria."
- **Evidence pointer** Abstract; Discussion
- **Concern** While the structural organisation of tp-CP12 is indeed distinct from previously characterised CP12 proteins, the claim of "completely different" is strong and may be overstated. The authors have not performed a comprehensive structural comparison with all known CP12 proteins, and the functional significance of the observed differences is not fully explored. The novelty of the work lies in the specific combination of techniques applied to this particular protein, but the broader implications for CP12 biology could be more clearly articulated.
- **Why it matters** The claim of uniqueness is important for establishing the novelty of the work. If the structural differences are not as pronounced as claimed, or if similar features exist in other CP12 proteins, the novelty of the findings would be diminished.
- **Resolution test** Provide a more detailed structural comparison with known CP12 proteins, including quantitative measures of structural similarity. Discuss the functional implications of the observed differences in the context of the diverse roles of CP12 across different organisms.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Readability for nonspecialists
- **Affected element** Introduction
- **Evidence pointer** Introduction, paragraph 1
- **Issue** The introduction assumes a high level of familiarity with CP12 biology and the techniques used. A brief explanation of the significance of CP12 in the context of photosynthesis and the rationale for studying a diatom CP12 would improve accessibility for a broader readership.
- **Required correction** Add a brief introductory paragraph explaining the role of CP12 in photosynthetic carbon fixation and why diatoms are of particular interest.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Technical soundness
- **Affected element** Materials and methods, "Spin labelling procedure"
- **Evidence pointer** Materials and methods, "Spin labelling procedure"
- **Issue** The labelling efficiency values are reported with uncertainties (e.g., "81(5)%"), but the method for determining these uncertainties is not described. Additionally, the impact of incomplete labelling on the DEER data is not discussed.
- **Required correction** Specify how the labelling efficiencies and their uncertainties were determined. Discuss the potential impact of incomplete labelling on the DEER distance distributions.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Technical soundness
- **Affected element** Materials and methods, "Refinement by molecular dynamics simulations"
- **Evidence pointer** Materials and methods, "Refinement by molecular dynamics simulations"
- **Issue** The description of the MD simulation protocol is incomplete. The authors do not specify the temperature and pressure coupling methods, the equilibration protocol, or the total simulation time for the harmonic restrained MD simulations.
- **Required correction** Provide a complete description of the MD simulation protocol, including all relevant parameters.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Readability for nonspecialists
- **Affected element** Results, "Local dynamics probed by rt cw-EPR"
- **Evidence pointer** Results, "Local dynamics probed by rt cw-EPR"; Figure 2
- **Issue** The interpretation of the cw-EPR spectra in terms of rotational correlation times and mobility is presented without sufficient context for readers unfamiliar with EPR spectroscopy. A brief explanation of how spectral shapes relate to protein dynamics would be helpful.
- **Required correction** Add a brief explanation of the relationship between EPR spectral shapes and spin label mobility.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Scientific importance
- **Affected element** Discussion
- **Evidence pointer** Discussion, paragraph 3
- **Issue** The discussion of the potential functional implications of the structural findings is somewhat speculative and could be more focused. The authors mention several possible functions but do not prioritise them or provide a clear hypothesis for future testing.
- **Required correction** Refine the discussion to present a clear, testable hypothesis regarding the function of tp-CP12, based on the structural findings.

### Technical failings that need to be addressed before the case is established
1. Insufficient description and validation of the manually modified starting structure for MD simulations (R1-M1).
2. Inadequate demonstration of MD simulation convergence and sampling (R1-M3).
3. Lack of quantitative analysis of DEER distance distributions and insufficient discussion of potential artefacts (R1-M2).

### Assessment against Nature-style criteria
- **Originality**: The work is original in its application of an integrative structural biology approach to a previously uncharacterised diatom CP12 protein. The finding of an antiparallel coiled-coil organisation and flexible C-termini is novel. However, the claim of "completely different" structural organisation may be overstated without a comprehensive comparison.
- **Scientific importance**: The work addresses an important question about the structural basis of CP12 function in diatoms, a major group of primary producers. The findings have implications for understanding the diversity of CP12 regulation mechanisms. However, the functional significance is not directly demonstrated, limiting the immediate impact.
- **Interdisciplinary readership**: The work will appeal to researchers in structural biology, photosynthesis research, and biophysics. The combination of EPR, SAXS, and MD simulations is of broad interest. However, the presentation may be too specialised for a general audience.
- **Technical soundness**: The experimental techniques are applied appropriately, and the data quality appears good. However, the MD simulation protocol and the validation of the modified starting structure need to be strengthened. The interpretation of the DEER data could be more rigorous.
- **Readability for nonspecialists**: The manuscript is clearly written but assumes a high level of expertise in the techniques used. The introduction and some results sections could be made more accessible.

### Recommendation posture
Supportive if technical concerns are resolved. The manuscript presents a valuable contribution to the structural characterisation of a poorly understood protein. The combination of techniques is appropriate and the data are generally of good quality. However, the concerns regarding the MD simulation protocol, the validation of the modified starting structure, and the interpretation of the DEER data need to be addressed before the conclusions can be fully accepted. The claims regarding PRK binding should also be tempered or supported by experimental evidence.

## Risk / unsupported claims
1. The claim that the four structured domains are "likely to bind phosphoribokinase" is unsupported by direct experimental evidence and is based solely on structural modelling.
2. The claim that the structural organisation is "completely different" from all homologous counterparts is not fully supported by a comprehensive structural comparison.
3. The conclusion that the C-terminal regions are "highly flexible and partly disordered" is based on indirect evidence from DEER and MD simulations and would be strengthened by direct experimental validation (e.g., NMR relaxation measurements).
4. The functional implications for the regulation of the Calvin cycle in diatoms are speculative and not directly tested.