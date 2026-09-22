## Review setup
- **Input scope** Full manuscript text, including main text, methods, and supplementary section S1
- **Assessment boundary** Scientific claims, model assumptions, theoretical derivations, simulation methodology, and agreement with experimental data as presented
- **Shared manuscript claim summary** The authors propose that intrinsically disordered regions (IDRs) in transcription factors (TFs) enhance both binding affinity and search speed through a "tentacle" or "octopusing" mechanism, and derive design principles governing IDR length, binding site spacing, and binding energy
- **Visible evidence base** Main text equations (1)-(5), Figures 1-4 (referenced but not visible), supplementary sections S1-S11 (only S1 text visible), simulation methodology in Materials and Methods
- **Missing materials affecting confidence** Figures 1-4 are not provided; supplementary sections S2-S11 are referenced but not included; experimental data from Ref. [12] is described but not shown; simulation parameters and code are not available for inspection

## Reviewer

- **Overall assessment** The manuscript addresses a timely and important question in gene regulation: how intrinsically disordered regions in transcription factors contribute to target search efficiency. The authors develop a coarse-grained polymer model and identify several plausible design principles. However, the current presentation has significant gaps that prevent full evaluation. The central claims rest on figures and supplementary materials that are not available in the provided scope. The theoretical derivations are presented in compressed form, and the connection between the equilibrium binding analysis and the dynamical search results requires clearer exposition. The comparison with experimental data from Ref. [12] is promising but the fitting procedure and its uniqueness are not fully described. The manuscript has potential but the evidence base as provided is insufficient to fully establish the case.

- **Who would be interested in the results, and why** Researchers in gene regulation, biophysics of protein-DNA interactions, and theoretical biology would find these results relevant. The work connects to ongoing debates about how eukaryotic TFs achieve rapid and specific target localization despite genomic complexity. The proposed "octopusing" mechanism and the design principles (l0 = d, n_b = n_t, E_B > E_th) could inform experimental design in synthetic biology and genome engineering. The polymer physics approach may also interest the soft matter community studying facilitated diffusion and polymer dynamics near surfaces.

- **Major Strengths**
  - The manuscript addresses a biologically important and mechanistically unresolved question with a physically grounded approach
  - The use of the Rouse model provides a tractable framework that connects equilibrium binding thermodynamics to dynamical search processes
  - The identification of concrete, testable design principles (l0 = d, n_b = n_t, E_B > E_th) is valuable and could guide future experiments
  - The proposed "octopusing" mechanism offers a novel conceptual contribution distinct from the classical facilitated diffusion model
  - The authors explicitly discuss experimental validation strategies, including DNA scrambling and time-resolved binding measurements

- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence completeness
- **Claim pointer** The manuscript claims quantitative agreement with experimental binding probability data from Ref. [12] using only the DBD binding energy as a fitting parameter
- **Evidence pointer** Figure 4, described in text but not visible; experimental data from Ref. [12] not shown
- **Concern** The central validation claim cannot be assessed without seeing Figure 4 and the underlying experimental data. The fitting procedure is described in a single sentence, and it is unclear whether the agreement is robust to reasonable variations in other model parameters (e.g., l0, d, E_B values, polymer length). The claim of "quantitative agreement" requires statistical measures of fit quality and a demonstration that the model is not overparameterized or trivially flexible.
- **Why it matters** The experimental comparison is the primary evidence that the model captures biologically relevant behavior. Without this, the design principles remain theoretical predictions without empirical grounding.
- **Resolution test** Provide Figure 4 with error bars on experimental data, the fitted model curve, and a description of the fitting procedure including parameter ranges explored and sensitivity analysis. Report goodness-of-fit statistics and demonstrate that the single fitted parameter is identifiable.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Theoretical derivation clarity
- **Claim pointer** The manuscript claims that the enhancement factor P is always positive and that the design principle l0 = d maximizes binding affinity
- **Evidence pointer** Equations (1)-(2), main text; derivation in Supplementary S2 (not visible)
- **Concern** The derivation of equations (1) and (2) is not shown in the provided material. The claim that P is always positive is stated without proof. The condition l0 = d is asserted to maximize P, but the functional form of P in the multi-site case is not given explicitly. The transition from the single-site case to the multi-site case is described qualitatively, and it is unclear whether the l0 = d principle holds under all parameter regimes or only in specific limits.
- **Why it matters** The design principles are the core intellectual contribution. If the derivations contain hidden assumptions or are only valid in narrow regimes, the generality of the claims is overstated.
- **Resolution test** Provide the full derivation in the main text or supplement, including explicit expressions for P in the multi-site case. State the conditions under which l0 = d is exactly optimal versus approximately optimal. Demonstrate that the positivity of P holds for all parameter values considered.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Simulation methodology and validation
- **Claim pointer** The manuscript claims that the optimal search process consists of a single round of 3D-1D search, and that equation (5) agrees well with simulation results
- **Evidence pointer** Figure 3, described in text but not visible; Materials and Methods simulation description; Supplementary S7-S8 (not visible)
- **Concern** The simulation methodology is described at a high level, but critical details are missing. The coarse-graining procedure maps IDR sites to point particles with spring connections, but the mapping between simulation units and physical units (base pairs, nanometers, seconds) is not specified. The claim that a single round of 3D-1D search is optimal is stated to be derived in Supplementary S8, but this derivation is not visible. The fitting parameters alpha = 0.5 and beta = 14.5 are presented without uncertainty estimates or a demonstration that the fit is unique. The simulation time of 10^5 CPU hours suggests significant computational cost, but convergence criteria and error bars on the reported search times are not given.
- **Why it matters** The dynamical results are the second pillar of the manuscript. Without proper validation of the simulation methodology and the analytical approximation, the claim of a new search mechanism is not fully supported.
- **Resolution test** Provide convergence tests for the simulations, error bars on reported search times, a sensitivity analysis of the fitted parameters alpha and beta, and a clear statement of the unit mapping. Show that the single-round 3D-1D claim holds across a range of parameter values, not just at the optimal point.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Biological realism and parameter regime
- **Claim pointer** The manuscript claims that the model shows good agreement with experimental results and that the design principles are robust across diverse molecular systems
- **Evidence pointer** Main text discussion; Supplementary S6, S9, S10 (not visible)
- **Concern** The model assumes a straight-line antenna with regularly spaced targets, which is a significant idealization of chromatin structure. The authors acknowledge that curved antennas do not change results (Supplementary S9), but the visible text does not describe how curvature was modeled or over what range of curvatures the result holds. The model also assumes specific interactions between IDR sites and targets, but the biological specificity of IDR-DNA interactions is not addressed. The claim of applicability to "other biophysical contexts" such as RNA polymerase binding and antibody binding is speculative and not supported by any analysis in the visible text.
- **Why it matters** The generality of the design principles depends on the robustness of the model to biological complexity. If the principles only hold for idealized straight DNA with regularly spaced targets, their relevance to real chromatin is limited.
- **Resolution test** Provide the results from Supplementary S9 and S10 in the main text or clearly summarize the range of conditions tested. Discuss the limitations of the straight-line antenna assumption and how chromatin structure might modify the predictions.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity of notation
- **Affected element** Equations (1)-(5)
- **Evidence pointer** Main text
- **Issue** The notation is dense and some symbols are not defined at first use. For example, the relationship between l0 (statistical segment length) and the physical length of the IDR is not stated explicitly. The parameter n~ = n_b + 1 is introduced in the dynamics section but its relationship to the total number of binding sites is not made clear.
- **Required correction** Define all symbols at first use and provide a table of parameters with their physical meanings and typical values used in simulations.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Experimental comparison details
- **Affected element** Figure 4 and associated text
- **Evidence pointer** Main text, "Comparing with experimental results" section
- **Issue** The description of the experimental data from Ref. [12] is brief. It is unclear how the experimental binding probability was measured, what the error bars represent, and how the IDR truncation was performed. The statement that the DBD binding energy is the "only fitting parameter" needs clarification on how this parameter was constrained.
- **Required correction** Provide a brief description of the experimental setup from Ref. [12] and state the fitted value of E_DBD with its uncertainty.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Computational cost and reproducibility
- **Affected element** Materials and Methods, simulation description
- **Evidence pointer** Main text
- **Issue** The manuscript states that simulations require 10^5 CPU hours, which is substantial. The code availability statement says data and code are available from the authors, but no repository or accession number is provided.
- **Required correction** Provide a public repository link for code and data, and include a statement on how to reproduce the simulations.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Terminology
- **Affected element** "Octopusing" mechanism
- **Evidence pointer** Main text, dynamics section
- **Issue** The term "octopusing" is introduced without a clear definition. The analogy to octopus tentacles is evocative but the precise mechanism (multiple binding sites alternately engaging and releasing) should be described more explicitly.
- **Required correction** Provide a clear mechanistic description of the octopusing walk, including how it differs from standard facilitated diffusion and how the feedback mechanism operates.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Scope of claims
- **Affected element** Discussion of applicability to other systems
- **Evidence pointer** Main text, final paragraph
- **Issue** The claim that the design principles apply to "nonspecific RNA polymerase binding" and "multivalent antibody binding" is speculative. No analysis is presented to support these extensions.
- **Required correction** Either provide supporting analysis or clearly label these as speculative extensions that require future work.

- **Technical failings that need to be addressed before the case is established**
  - R1-M1: Experimental comparison cannot be evaluated without Figure 4 and the underlying data
  - R1-M2: Derivations of equations (1)-(2) and the multi-site generalization are not visible
  - R1-M3: Simulation methodology lacks unit mapping, convergence criteria, and error analysis
  - R1-M4: Robustness claims rely on supplementary sections not provided in the review scope

- **Assessment against Nature-style criteria**
  - **Originality** The work presents a novel conceptual framework for IDR function in TF search, particularly the "octopusing" mechanism and the identification of specific design principles. This goes beyond prior work that treated IDRs as nonspecific tethers. The connection between polymer physics and gene regulation is creative.
  - **Scientific importance** The question of how TFs find their targets efficiently in eukaryotic cells is fundamental. If the design principles hold, they could explain why many TFs contain IDRs and guide engineering of synthetic TFs. The potential impact is high.
  - **Interdisciplinary readership** The work bridges biophysics, molecular biology, and polymer physics. The concepts are accessible to a broad audience, though the mathematical presentation may be challenging for experimentalists. The biological motivation is clearly stated.
  - **Technical soundness** The theoretical framework is plausible but cannot be fully assessed from the provided material. The simulation methodology is described at a level that prevents independent reproduction. The agreement with experiment is claimed but not verifiable from the visible text.
  - **Readability for nonspecialists** The main text is generally well-written and the biological motivation is clear. However, the equations are introduced with minimal context, and the connection between the equilibrium binding analysis and the dynamical results could be explained more clearly. The term "octopusing" is memorable but needs a clearer mechanistic definition.

- **Recommendation posture** Supportive if technical concerns are resolved. The manuscript addresses an important question with a creative approach and identifies testable design principles. However, the current evidence base is insufficient to fully establish the case. The missing figures, supplementary derivations, and simulation details must be provided for a complete evaluation. The experimental comparison is the most critical missing piece, as it is the primary validation of the model. If the authors can demonstrate robust quantitative agreement with experiment and provide transparent derivations and simulation methodology, the work would be a valuable contribution.