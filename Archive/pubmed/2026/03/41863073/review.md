## Review setup
- **Input scope** Full manuscript text including abstract, introduction, methods, results, discussion, and appendix
- **Assessment boundary** Scientific validity, methodological soundness, and significance of the computational rheometry framework as presented; no assessment of editorial fit or publication venue
- **Shared manuscript claim summary** The authors introduce a computational rheometry framework that models biomolecular condensates as networks of Stokes-Maxwell elements embedded in a Stokes fluid, enabling calculation of viscoelastic moduli and mechanical responses from graph-based representations of condensate structures derived from coarse-grained simulations. The framework reproduces frequency-dependent responses observed in passive microrheology experiments and allows simulation of creep tests.
- **Visible evidence base** Figures 1-7, equations 1-33, descriptions of simulation protocols for LaSSI, Mpipi-Recharged, and CALVADOS, and comparisons to experimental observations
- **Missing materials affecting confidence** No quantitative comparison to experimental data is shown; no error bars or statistical analysis of variability across simulation snapshots; no validation against analytical solutions or experimental rheological data; code availability is promised but not yet accessible; no details on convergence testing of the numerical integration

## Reviewer

- **Overall assessment** This manuscript presents a conceptually interesting extension of graph-based approaches to condensate rheology by embedding networks in a Stokes fluid, thereby incorporating hydrodynamic interactions. The framework is clearly described and the implementation appears technically sound. However, the central claim that this approach "reproduces" experimental observations is not directly demonstrated with quantitative comparisons. The parameter regime proposed for matching experiments (E=η=50) is asserted without systematic fitting or validation. The distinction between the presented approach and prior work by Cohen et al. is clear in terms of hydrodynamic coupling, but the added scientific value for understanding condensate physics requires stronger demonstration.

- **Who would be interested in the results, and why** Researchers studying the material properties of biomolecular condensates, particularly those using coarse-grained simulations and seeking to connect molecular-scale interactions to mesoscale rheological responses. The framework could also interest computational biophysicists developing methods for simulating viscoelastic networks and experimentalists interpreting microrheology data on condensates.

- **Major strengths** The manuscript addresses an important gap by incorporating hydrodynamic interactions into graph-based rheological models of condensates. The framework is general and could be applied to condensates from various simulation platforms. The inclusion of creep tests as a complementary probe to oscillatory shear is valuable. The appendix provides a useful analytical estimate of hydrodynamic screening lengths in condensates.

- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence for central claim
- **Claim pointer** The abstract states that computational rheometry "reproduces the full spectrum of frequency-dependent responses that have been reported for condensates probed using passive microrheology."
- **Evidence pointer** Results section, Figures 4-5; location not provided
- **Concern** The manuscript claims reproduction of experimental frequency-dependent responses, but no direct quantitative comparison to experimental data is presented. The computed moduli are shown only in dimensionless form for E=η=1, 10, 50, and 100. The claim that E=η=50 "is likely to be in the regime of rheological measurements" is not supported by any fitting procedure or quantitative comparison to measured moduli from experiments on A1-LCD condensates.
- **Why it matters** The central scientific claim of the paper is that this framework can bridge molecular and mesoscale descriptions to explain experimental observations. Without quantitative validation against experimental data, the framework remains a methodological proposal rather than a demonstrated tool for understanding condensate rheology.
- **Resolution test** Provide a quantitative comparison between computed and experimentally measured G'(ω) and G''(ω) for A1-LCD condensates, including the fitting procedure used to determine E and η values, or clearly state that such validation is beyond the current scope and temper the claims accordingly.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Parameter interpretation
- **Claim pointer** The manuscript states that "the values of E=η=50 are likely to be in the regime of rheological measurements for A1-LCD condensates and similar systems."
- **Evidence pointer** Results section, Figure 4; location not provided
- **Concern** The physical meaning of the dimensionless parameters E and η is not clearly established. The manuscript does not explain how these parameters relate to molecular-scale properties such as interaction strengths, bond lifetimes, or monomer friction coefficients. The claim that E=η=50 corresponds to experimental conditions is therefore difficult to evaluate or interpret.
- **Why it matters** Without a clear mapping between the dimensionless model parameters and physical quantities, the framework cannot generate testable predictions or provide mechanistic insight into how molecular interactions give rise to mesoscale rheology.
- **Resolution test** Provide a derivation or discussion that connects E and η to molecular-scale parameters, or demonstrate through systematic variation that the qualitative behaviors are robust across a wide parameter range and identify which parameter combinations are constrained by experimental data.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Comparison to prior work
- **Claim pointer** The introduction states that the generalized Rouse model of Cohen et al. "ignores the effects of hydrodynamic interactions" and that the present framework remedies this deficiency.
- **Evidence pointer** Introduction, Discussion; location not provided
- **Concern** The manuscript does not provide a direct comparison between the predictions of the generalized Rouse model and the Stokes-Maxwell framework for the same condensate graphs. The claim that hydrodynamic interactions are important is supported only by the analytical estimate in the appendix, not by a demonstration that including them changes the predicted moduli in a significant way.
- **Why it matters** The scientific contribution of the framework depends on whether hydrodynamic coupling materially affects the predicted rheological responses. Without a direct comparison, it is unclear whether the added complexity of the Stokes-Maxwell approach is necessary or whether the simpler Rouse-based model is sufficient.
- **Resolution test** Compute moduli using both the generalized Rouse model and the Stokes-Maxwell framework on the same graphs and show where and why the predictions differ, or provide a quantitative analysis of when hydrodynamic effects become important.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Statistical robustness
- **Claim pointer** The manuscript states that "networks extracted from all three simulations exhibit small-world-like features" and that comparisons reveal "a consistent temperature dependence."
- **Evidence pointer** Results section, Figure 3; location not provided
- **Concern** The analysis appears to be based on a single representative network configuration at each temperature for each simulation method. No information is provided about variability across independent simulation snapshots or across different random seeds. The claim of consistency across methods is based on qualitative visual inspection rather than quantitative statistical comparison.
- **Why it matters** Condensate structures fluctuate over time, and rheological properties are ensemble-averaged quantities. Without an assessment of variability, it is unclear whether the reported differences between simulation methods are significant or within expected fluctuations.
- **Resolution test** Provide statistics over multiple independent snapshots for each simulation method and temperature, including error bars on computed moduli and creep responses, and perform a statistical test for differences between methods.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity of methods
- **Affected element** Materials and Methods, Framework for computational rheometry
- **Evidence pointer** Materials and Methods; location not provided
- **Issue** The description of how the graph is converted into a Stokes-Maxwell network is brief. It is not clear how the elastic modulus E and viscosity η are assigned to each edge, whether these are uniform across all edges, and how the initial rest lengths are determined from the simulation snapshots.
- **Required correction** Provide a more detailed description of the mapping from simulation structures to Stokes-Maxwell parameters, including any assumptions about uniformity and how rest lengths are initialized.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Reproducibility
- **Affected element** Data and code availability
- **Evidence pointer** Data and code availability; location not provided
- **Issue** The code is stated to be "will be made available" but no repository link or access information is provided in the manuscript.
- **Required correction** Provide the actual repository link or state clearly that code will be available upon publication.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Parameter exploration
- **Affected element** Results, Impact of changes to E and η
- **Evidence pointer** Results, Figures 4-5; location not provided
- **Issue** The parameter sweep is limited to a few discrete values of E and η. A more systematic exploration of the parameter space would help establish the robustness of the observed behaviors and the boundaries of different rheological regimes.
- **Required correction** Consider presenting a phase diagram or heat map of rheological behavior across a wider range of E and η values.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Experimental context
- **Affected element** Discussion
- **Evidence pointer** Discussion; location not provided
- **Issue** The discussion of experimental comparisons is largely qualitative. Specific experimental studies on A1-LCD condensates are cited, but the quantitative values of measured moduli, crossover frequencies, or creep responses are not presented alongside the computed results.
- **Required correction** Include a table or figure comparing computed and experimental values for key rheological quantities, or clearly state which experimental quantities the framework is designed to predict.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Terminology
- **Affected element** Throughout
- **Evidence pointer** Throughout; location not provided
- **Issue** The term "computational rheometry" is used throughout, but its precise definition and scope are not explicitly stated. It is unclear whether this refers to the specific Stokes-Maxwell implementation or to a broader class of computational approaches.
- **Required correction** Provide a clear definition of "computational rheometry" in the introduction and use the term consistently.

## Risk / unsupported claims
- The claim that the framework "reproduces the full spectrum of frequency-dependent responses" reported in experiments is not supported by direct quantitative comparison.
- The assertion that E=η=50 corresponds to the experimental regime for A1-LCD condensates is not justified by any fitting or validation procedure.
- The claim that hydrodynamic interactions are important for condensate rheology is supported only by an analytical estimate, not by a direct comparison of model predictions with and without hydrodynamic coupling.
- The statement that "the three models generate results that are congruent with one another" is based on qualitative visual comparison without statistical analysis.
- The claim that creep tests can distinguish between glass transition and fluid-to-solid transition aging mechanisms is presented as a possibility but not demonstrated with specific examples or predictions.