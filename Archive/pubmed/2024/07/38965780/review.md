## Review setup
- **Input scope** Full manuscript text (abstract, introduction, methods, results, discussion, conclusion) and figure captions. No supplementary material was provided.
- **Assessment boundary** Scientific validity of the proposed SA-LR colloidal model for reflectin A1 assembly, the methodology used to parameterize and extrapolate the interaction potential, the simulation results, and the interpretation of these results in the context of experimental observations.
- **Shared manuscript claim summary** The authors propose that the equilibrium assembly and liquid-liquid phase separation of the intrinsically disordered protein reflectin A1 can be described by a simple colloidal model with short-range attraction and long-range repulsion (SA-LR) interactions. They parameterize this potential from SAXS data at pH 4.5, extrapolate it to higher pH using Gouy-Chapman theory, and use molecular dynamics simulations to predict pH-dependent cluster formation and phase behavior, which they compare to experimental observations.
- **Visible evidence base** Main text, equations 1-10, Figures 1-6, and figure captions. No supplementary figures or tables were available for review.
- **Missing materials affecting confidence** Supplementary material (Figures S1-S3, Table S1) referenced in the text was not provided. This includes the pH-dependent potential parameters, the phase diagram (Figure 9 is mentioned but not shown), and details of the liquid-state perturbation theory calculations. Experimental SAXS data and DLS data are referenced but not shown in full.

## Reviewer
- **Overall assessment** The manuscript presents a compelling and potentially significant hypothesis: that the complex assembly behavior of the intrinsically disordered protein reflectin A1 can be captured by a remarkably simple isotropic SA-LR pair potential. The authors have developed a clear workflow combining SAXS experiments, liquid-state theory, and molecular dynamics simulations. The qualitative agreement between simulation predictions and experimental observations of cluster size and pH dependence is encouraging. However, the manuscript has several critical weaknesses that prevent full acceptance. The most significant concern is the lack of a rigorous, quantitative validation of the model against experimental data. The comparison between simulated and experimental cluster sizes (Figure 6) is presented as an "error area" without clear statistical measures of agreement. The extrapolation of the potential to higher pH relies on assumptions that are acknowledged but not thoroughly tested. The phase diagram, a central result, is not shown in the provided material. The claim that this is the first experimental system fitting a "type III" SA-LR potential is not well supported. The manuscript would be significantly strengthened by a more detailed presentation of the model parameterization, a quantitative comparison with experiments, and a discussion of the limitations and potential alternative interpretations.
- **Who would be interested in the results, and why** Researchers in the fields of intrinsically disordered proteins, protein self-assembly, biophysics, soft matter physics, and biomaterials. The work is relevant to those studying phase separation in biology and those interested in designing stimuli-responsive protein-based materials. The demonstration that a simple colloidal model can capture IDP behavior is of broad interest.
- **Major strengths**
    1.  The central hypothesis is clear, bold, and testable: that a simple SA-LR potential can explain the complex assembly of an IDP.
    2.  The methodology is interdisciplinary and well-structured, combining experiments (SAXS), theory (Gouy-Chapman, liquid-state perturbation theory), and simulation (MD).
    3.  The use of Hamiltonian replica exchange to address slow dynamics in simulations is a sophisticated and appropriate approach.
    4.  The authors identify and discuss the limitations of their model, particularly regarding kinetic trapping at high pH.
    5.  The potential implications for understanding other IDPs are significant and well-articulated.
- **Major Concerns**

    - **Concern ID** R1-M1
    - **Severity** Major
    - **Blocking** Yes
    - **Axis** Technical Soundness / Model Validation
    - **Claim pointer** The authors claim that the SA-LR model "successfully capture[s] a number of qualitative features of reflectin, including pH-dependent formation of discrete-sized nanoclusters and liquid-liquid phase separation at high pH."
    - **Evidence pointer** Figure 6, Section "Results and discussion, Determination of a colloidal SA-LR potential for solution-phase reflectin"
    - **Concern** The validation of the model against experimental data is only qualitative. The comparison in Figure 6 shows simulated cluster sizes as a shaded "error area" and experimental DLS data as points. There is no quantitative metric (e.g., R^2, chi-squared, mean absolute error) to assess the agreement. The text states the results are "quantitatively similar" but this is not supported by any statistical analysis. The "error area" itself is not clearly defined; it appears to represent the range between two different methods of calculating hydrodynamic radius, not a statistical uncertainty. A more rigorous, quantitative comparison is required to substantiate the claim that the model captures the experimental behavior.
    - **Why it matters** The central claim of the paper is that the model is predictive. Without a quantitative measure of agreement, the reader cannot judge the validity of the model. The claim of "quantitative similarity" is a key piece of evidence for the model's success and must be rigorously demonstrated.
    - **Resolution test** Provide a quantitative comparison between simulated and experimental cluster sizes, including appropriate error bars and a statistical measure of agreement (e.g., reduced chi-squared). The authors should also clearly define the "error area" in Figure 6.

    - **Concern ID** R1-M2
    - **Severity** Major
    - **Blocking** Yes
    - **Axis** Technical Soundness / Model Parameterization
    - **Claim pointer** The authors claim that the interaction potential is "parameterized... from small-angle x-ray scattering measurements" and then "extrapolate[d]... to a range of pH values using Gouy-Chapman theory."
    - **Evidence pointer** Section "Methods, Estimation of the interaction potential from SAXS measurements", Figure 3, Equation 10
    - **Concern** The details of the SAXS fitting are insufficient. The authors state that they fit the two-Yukawa parameters but do not provide the fitted values (K1, Z1, K2, Z2) in the main text. The quality of the fit is only shown visually in Figure 3a. More critically, the extrapolation to higher pH is based on the assumption that only the repulsive part (K2, Z2) changes with pH, while the attractive part (K1, Z1) remains constant. This is a significant assumption, especially as the authors themselves note that the attractive interactions may change near the point of zero charge. The manuscript does not provide a sensitivity analysis or a test of this assumption. The derivation of Equation 10 is not fully explained.
    - **Why it matters** The entire simulation and phase diagram depend on the accuracy of the interaction potential. If the parameterization is not robust or the extrapolation is based on an invalid assumption, all subsequent results are questionable. The authors must provide the fitted parameters and a clear justification for the extrapolation method.
    - **Resolution test** Provide the fitted values of the two-Yukawa parameters in the main text or a table. Provide a more detailed derivation of Equation 10. Test the sensitivity of the simulation results to the assumption that the attractive part of the potential is pH-independent, perhaps by comparing to a model where both parts change.

    - **Concern ID** R1-M3
    - **Severity** Major
    - **Blocking** Yes
    - **Axis** Technical Soundness / Reproducibility
    - **Claim pointer** The authors claim to have created a "putative phase diagram for reflectin" and that the model predicts "liquid-liquid phase separation at high pH."
    - **Evidence pointer** Section "Results and discussion, Phase diagram and LLPS driven by SA-LR interactions", Figure 9 (not shown in provided material)
    - **Concern** The phase diagram, which is a central result of the paper, is not shown in the provided material. The text describes four regions (dispersed fluid, cluster fluid, percolated cluster, two-phase region) and the methods used to define them, but the actual diagram is missing. This makes it impossible to evaluate the predicted phase boundaries, the location of the critical point, or the comparison to experimental observations of LLPS. The description of the "type III" vs "type II" classification is confusing without the figure.
    - **Why it matters** The phase diagram is a key prediction of the model and is essential for understanding the relationship between cluster formation and LLPS. Without seeing it, the reader cannot assess the validity of the claims about phase behavior.
    - **Resolution test** Include Figure 9 in the manuscript. The figure should clearly show the phase boundaries, the location of the critical point, and the experimental conditions (pH, concentration) at which LLPS is observed.

    - **Concern ID** R1-M4
    - **Severity** Major
    - **Blocking** No
    - **Axis** Scientific Importance / Originality
    - **Claim pointer** The authors claim that "the success of SA-LR interactions presented in this study demonstrates the potential of a colloidal interpretation of interactions and phenomena in a range of intrinsically disordered proteins."
    - **Evidence pointer** Section "Conclusion"
    - **Concern** While the application of the SA-LR model to an IDP is novel, the manuscript does not fully discuss the limitations of this approach. The model treats the protein as a spherical particle, ignoring its conformational flexibility and internal structure. The authors acknowledge this but do not discuss under what conditions this approximation might break down. For example, would the model be applicable to IDPs that form fibrils or other anisotropic structures? The claim of broad applicability is therefore somewhat overstated.
    - **Why it matters** The significance of the work lies in its potential generalizability. A more nuanced discussion of the model's limitations would strengthen the claim and provide a more balanced perspective for the reader.
    - **Resolution test** Add a paragraph to the discussion or conclusion that explicitly addresses the limitations of the spherical, isotropic model and discusses the conditions under which it is likely to be valid or invalid for other IDPs.

- **Minor Comments**

    - **Concern ID** R1-m1
    - **Severity** Minor
    - **Axis** Readability for Nonspecialists
    - **Affected element** Introduction, Figure 1
    - **Evidence pointer** Figure 1
    - **Issue** The schematic in Figure 1 is helpful, but the text introducing the SA-LR model could be clearer for a reader unfamiliar with colloid science. The terms "short-range attraction" and "long-range repulsion" are used, but the physical origin of these forces in the context of a disordered protein is not fully explained.
    - **Required correction** Briefly explain in the introduction what kind of molecular interactions could give rise to short-range attraction (e.g., hydrophobic effect) and long-range repulsion (e.g., electrostatic) in the context of a disordered protein.

    - **Concern ID** R1-m2
    - **Severity** Minor
    - **Axis** Technical Soundness
    - **Affected element** Methods, SAXS
    - **Evidence pointer** Section "Methods, SAXS"
    - **Issue** The manuscript states that SAXS data were reported previously. It is not clear if the data used here are exactly the same or if any re-analysis was performed. The buffer conditions for the SAXS experiments are mentioned, but the ionic strength is not explicitly stated.
    - **Required correction** Clarify whether the SAXS data are from a previous publication and if so, provide the reference. State the ionic strength of the buffer used for the SAXS experiments.

    - **Concern ID** R1-m3
    - **Severity** Minor
    - **Axis** Technical Soundness
    - **Affected element** Methods, Simulations
    - **Evidence pointer** Section "Methods, Colloidal reflectin molecular dynamics simulations"
    - **Issue** The simulation details are sparse. The number of particles (500) is given, but the integration time step, the total simulation time, and the equilibration protocol are not described in the main text. The use of Hamiltonian replica exchange is mentioned, but the number of replicas and the range of pH values sampled are not specified.
    - **Required correction** Provide more details on the simulation setup, including time step, total simulation time, number of replicas, and the range of pH values used in the replica exchange.

    - **Concern ID** R1-m4
    - **Severity** Minor
    - **Axis** Readability for Nonspecialists
    - **Affected element** Results, Phase diagram
    - **Evidence pointer** Section "Results and discussion, Phase diagram and LLPS driven by SA-LR interactions"
    - **Issue** The text mentions "type III" and "type II" SA-LR systems without defining them. This classification is likely not familiar to all readers.
    - **Required correction** Define the classification of SA-LR systems (e.g., based on the range of attraction relative to repulsion) when it is first mentioned.

    - **Concern ID** R1-m5
    - **Severity** Minor
    - **Axis** Technical Soundness
    - **Affected element** Results, Figure 6
    - **Evidence pointer** Figure 6
    - **Issue** The figure caption mentions "error area" but does not define what this area represents. It is also unclear if the experimental DLS data points have error bars.
    - **Required correction** Define the "error area" in the figure caption and include error bars on the experimental data points if available.

- **Technical failings that need to be addressed before the case is established**
    - R1-M1: Lack of quantitative validation of the model against experimental data.
    - R1-M2: Insufficient detail and justification for the SAXS parameterization and pH extrapolation of the interaction potential.
    - R1-M3: The central phase diagram (Figure 9) is not shown, making a key prediction impossible to evaluate.

## Risk / unsupported claims
- The claim that the model "successfully capture[s] a number of qualitative features" is supported, but the stronger claim of "quantitative similarity" is not supported by the evidence provided.
- The claim that this is "the first experimental system that fits this type of SA-LR potential" is unsupported, as no comparison to other systems is made.
- The claim that the model can be generalized to "a range of intrinsically disordered proteins" is speculative and not directly supported by the data presented.
- The prediction of the phase diagram and the location of the LLPS boundary is unverifiable without Figure 9.
- The assumption that the attractive part of the potential is pH-independent is not tested and could be a major source of error in the model predictions.