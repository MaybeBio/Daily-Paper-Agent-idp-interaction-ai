## Review setup
- **Input scope** Full manuscript text, including abstract, introduction, methods, results, conclusions, and supplementary figure captions. No supplementary PDF or raw data files were provided for inspection.
- **Assessment boundary** Scientific content, methodological soundness, internal consistency, and support of claims by the presented evidence. No assessment of language polish or editorial fit beyond Nature-style criteria.
- **Shared manuscript claim summary** The authors use classical molecular dynamics simulations to characterize the adsorption of silica monomers, dimers, and trimers onto five biomolecular substrates (ubiquitin, SUMO-1, EGFP, lysozyme T4, and Aβ1-40). They report that oligomers adsorb more strongly than monomers, that disordered/unfolded regions recruit more silica, and that silica adsorption dampens fluctuations in disordered domains and may stabilize metastable helical conformations in Aβ1-40. They frame these findings as relevant to the atom probe tomography (APT) workflow for biomolecular structural characterization.
- **Visible evidence base** Main text figures 1-7, supplementary figure references (S1-S5), methods descriptions, and simulation parameters. No raw trajectories, force field validation data, or convergence metrics were visible in the provided material.
- **Missing materials affecting confidence** Supplementary PDF (including Figures S1-S5 and the "Alternative mixed scenarios of SUMO-1" section), Zenodo raw data, simulation input files, and any convergence or reproducibility analyses. These are referenced but not available for verification.

## Reviewer
- **Overall assessment** This manuscript addresses a timely and relevant question at the interface of biomolecular simulation and an emerging experimental technique (APT). The simulation setup is reasonable, the system choices are diverse and well-motivated, and the observation that oligomers behave differently from monomers is potentially useful. However, the central claims regarding adsorption affinity, the role of disorder, and the stabilization of metastable conformations are supported by qualitative or indirect evidence. Key quantitative analyses (binding free energies, residence times, statistical uncertainties) are absent. The link to APT remains largely speculative, and the authors do not demonstrate that the observed effects would persist under the cryogenic, vacuum, and high-field conditions of the actual APT experiment. The manuscript is technically sound in its execution but does not yet establish its broader claims with the rigor expected for a high-impact venue.
- **Who would be interested in the results, and why** Researchers in biomolecular simulation, biomineralization, and the growing APT community interested in soft-matter or biological applications. The work may also appeal to those studying silica-biomolecule interactions in materials science or bionanotechnology. The specific finding that disordered regions recruit silica oligomers could inform future experimental designs for APT-based structural biology.
- **Major strengths** 1) The study addresses a genuinely open question with practical relevance to an emerging experimental technique. 2) The choice of five structurally diverse substrates is thoughtful and enables comparative analysis. 3) The simulation protocol is standard and reproducible in principle. 4) The observation of differential behavior between monomers and oligomers is a clear, testable result. 5) The authors are appropriately cautious in some interpretations, acknowledging the need for further scrutiny.
- **Major Concerns** 
- **Minor Comments** 
- **Technical failings that need to be addressed before the case is established** R1-M1, R1-M2, R1-M3, R1-M4, R1-M5
- **Assessment against Nature-style criteria** Originality: moderate. The application of MD to silica-biomolecule interactions is not new, and the specific APT context is novel but the simulation approach is standard. Scientific importance: potentially high if the APT workflow becomes established, but the current evidence does not yet demonstrate that the simulated conditions are relevant to the experimental ones. Interdisciplinary readership: the topic bridges simulation, materials science, and structural biology, which is attractive, but the manuscript is written primarily for a simulation-savvy audience. Technical soundness: the simulations appear competently executed, but the analysis lacks quantitative rigor in several key areas. Readability for nonspecialists: the manuscript is generally clear, but the significance of the findings for APT is not made concrete enough for a broad audience.
- **Recommendation posture** Currently not established from the provided evidence. The authors should be encouraged to resubmit after addressing the major concerns, particularly the quantitative analysis of adsorption affinity, the statistical treatment of uncertainties, and a more direct discussion of the APT relevance.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence strength
- **Claim pointer** "The analysis of the radial distribution functions (RDF) in Fig. 2 shows a consistent pattern, whereby all silica species establish a first embedding shell within 4 Å of the protein surface, peaking at approximately 3.5 Å. However, the cumulative distribution of the RDFs reveals a significantly larger fraction of silicon atoms about the substrate in the mixed scenario than in the monomeric scenario, with the silica dimers and trimers exhibiting the strongest affinity."
- **Evidence pointer** Figure 2, Results section "Silica encapsulation of proteins: adsorption patterns and structural determinants"
- **Concern** The claim of "significantly larger fraction" and "strongest affinity" is based on visual inspection of RDFs and cumulative distributions. No quantitative measure of binding affinity (e.g., binding free energy, potential of mean force, residence time) is provided. The RDF is a structural observable, not a thermodynamic one. The authors do not report error bars or statistical uncertainties on the RDFs across replicates, so it is impossible to assess whether the observed differences are statistically meaningful.
- **Why it matters** The central conclusion of the paper, that oligomers adsorb more strongly than monomers, rests on this comparison. Without a quantitative and statistically robust measure, the claim is not established.
- **Resolution test** Provide a quantitative metric of adsorption affinity (e.g., binding free energy via umbrella sampling or free energy perturbation, or at minimum a time-averaged contact number with standard errors across replicates). Report the statistical significance of the difference between monomer and oligomer populations.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Claim-support gap
- **Claim pointer** "Notably, this inhibition of structural fluctuations seemingly biases the selection of locally metastable conformations within the (otherwise degenerate) ensemble of disordered and unstructured moieties. This phenomenon is illustrated better by the observed evolution of the secondary structures in Aβ1−40... residues 30-38, which sample a mostly unstructured configurational ensemble in the control scenario, while consistently folding into a helical motif in the mixed scenario."
- **Evidence pointer** Figure 7, Results section "Silica encapsulation modulates the structural dynamics of disordered domains"
- **Concern** The claim that silica adsorption "biases the selection of locally metastable conformations" is a strong statement. The evidence is a hierarchical clustering analysis of secondary structure propensity in aggregated trajectories. However, the authors do not report the population weights of the clusters, the free energy differences between conformational states, or the statistical significance of the difference between control and mixed scenarios. The representative structures shown in Figure 7 are qualitative. The claim of "stabilizing metastable helical motifs" implies a thermodynamic effect that is not demonstrated.
- **Why it matters** This is the most biologically significant claim of the paper, with implications for how silica encapsulation might affect protein structure. If the effect is not robust or is a sampling artifact, the conclusion is invalid.
- **Resolution test** Quantify the free energy landscape of Aβ1-40 in both scenarios (e.g., via Markov state models or umbrella sampling along relevant collective variables). Report cluster populations with uncertainties. Demonstrate that the helical state at residues 30-38 is thermodynamically stabilized, not just more frequently sampled in one trajectory set.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** External validity
- **Claim pointer** "For this technique to be effective, it is critical that the APT embedding stage keeps the native framework of the biomolecule, while minimizing the mechanical stress." and "These findings suggest APT as a suitable technique for the structural characterization of intrinsically disordered regions and the metastable conformational landscapes thereof."
- **Evidence pointer** Abstract, Introduction, Conclusions
- **Concern** The simulations are performed at 298 K in explicit water with physiological salt, conditions that are far from the actual APT experimental environment, which involves cryogenic temperatures, ultra-high vacuum, and intense electric fields. The authors do not discuss how their results at ambient conditions translate to the APT context. The claim that the findings "suggest APT as a suitable technique" is a leap that is not supported by the simulation evidence presented.
- **Why it matters** The entire motivation of the paper is the APT application. If the simulated conditions are not representative of the experimental ones, the relevance of the findings to APT is unclear.
- **Resolution test** Add a discussion section addressing the temperature, pressure, and field differences between simulation and experiment. If possible, perform simulations at lower temperatures or with applied electric fields to test the robustness of the observed adsorption behavior. Alternatively, temper the claims about APT suitability to what the simulations can actually support.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Technical rigor
- **Claim pointer** "The applicability of the Lorentz-Berthelot combination rules for the calculation of Lennard-Jones interactions ensures the formal cross-compatibility between the Amber ff14sb and PolCA force fields: We shall remark that no specific tuning of the interactions has been performed - which would rely on the availability of experimental data and/or on an a posteriori validation anyway."
- **Evidence pointer** Materials and Methods, "Crystal structures and MD setup"
- **Concern** The combination of two different force fields (Amber ff14SB for proteins and PolCAFF for silica) without any cross-validation is a significant source of potential error. The authors acknowledge this but do not address the consequences. The PolCAFF force field is not widely used, and its compatibility with Amber has not been established. The lack of any validation of the mixed force field against experimental data or higher-level theory weakens the reliability of the results.
- **Why it matters** Force field inaccuracies can lead to qualitatively wrong adsorption behavior. If the silica-protein interactions are not well described, all subsequent conclusions are compromised.
- **Resolution test** Validate the mixed force field against experimental adsorption data, or at minimum against DFT or ab initio calculations for a representative silica-protein interaction. Discuss the sensitivity of the results to force field parameters.

- **Concern ID** R1-M5
- **Severity** Major
- **Blocking** No
- **Axis** Reproducibility
- **Claim pointer** "Classical atomistic MD simulations were performed with the Gromacs 2021.5 software [24] in explicit TIP3P [25] water and a 150 mM concentration of monovalent salt."
- **Evidence pointer** Materials and Methods, "Crystal structures and MD setup"
- **Concern** The methods section does not report the number of ions added, the exact box size, the equilibration protocol details (e.g., how the restraints were applied, how the system was heated), or the criteria for considering a system equilibrated. The number of replicates is mentioned (1.5 μs per scenario) but the number of independent replicates is not stated. The simulation input files are not provided in the manuscript or referenced in a repository.
- **Why it matters** Reproducibility is a core requirement for computational studies. Without full details, other groups cannot replicate the simulations or assess their quality.
- **Resolution test** Provide complete simulation parameters, including ion concentrations, box dimensions, equilibration steps, and the number of independent replicates. Deposit input files and topologies in a public repository.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Figure 2
- **Evidence pointer** Figure 2 caption
- **Issue** The figure caption states "averaged over MD replicates" but does not specify how many replicates or how the averaging was performed. The left and right axes are not clearly distinguished in the caption.
- **Required correction** Specify the number of replicates and the averaging procedure. Clarify which curves correspond to which axis.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Methods, "Analysis protocol"
- **Evidence pointer** Materials and Methods, "Analysis protocol"
- **Issue** The hierarchical clustering analysis of Aβ1-40 is described briefly, but the number of clusters, the choice of linkage criterion, and the threshold for cluster significance are not reported.
- **Required correction** Provide details on the clustering parameters and the criteria for selecting the "most representative" clusters.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Interpretation
- **Affected element** Results, "Heterogeneous coating of proteins by silica"
- **Evidence pointer** Figure 5
- **Issue** The heatmaps in Figure 5 are described qualitatively. The authors state that disordered regions show more contacts, but no quantitative comparison (e.g., average contacts per residue in ordered vs. disordered regions) is provided.
- **Required correction** Add a quantitative analysis comparing contact densities in ordered vs. disordered regions, with statistical significance.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Context
- **Affected element** Introduction
- **Evidence pointer** Introduction, paragraph 1
- **Issue** The introduction cites reference [4] for the APT proof-of-concept on IgG, but does not discuss any limitations or alternative interpretations of that work.
- **Required correction** Briefly acknowledge the limitations of the experimental APT study to provide balanced context.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Presentation
- **Affected element** Conclusions
- **Evidence pointer** Conclusions, final paragraph
- **Issue** The discussion of Eriksson and co-workers [44] is interesting but tangential. It is not clear how this work directly supports or extends the present findings.
- **Required correction** Either integrate this discussion more tightly with the present results or move it to a "Future Directions" section.

## Risk / unsupported claims
- The claim that silica oligomers "exhibit the strongest affinity" for biomolecular surfaces is not quantitatively supported (no binding free energies or statistical tests).
- The claim that silica adsorption "stabilizes metastable helical conformations" in Aβ1-40 is not thermodynamically demonstrated.
- The claim that the findings "suggest APT as a suitable technique" for structural characterization of disordered regions is speculative, given the mismatch between simulation and experimental conditions.
- The assertion that disordered regions recruit silica "on account of their inherent flexibility and availability of hydrogen-bonding moieties" is a plausible hypothesis but is not directly tested (e.g., no mutation or chemical modification studies).
- The statement that "the process is enthalpy-driven to a certain extent" is not supported by any thermodynamic analysis in the provided text.