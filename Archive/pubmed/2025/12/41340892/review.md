## Review setup
- **Input scope** Full manuscript text (abstract, introduction, methods, results, discussion) without figures or supplementary materials
- **Assessment boundary** Scientific content, model formulation, claims versus evidence, and presentation quality as inferable from text alone
- **Shared manuscript claim summary** The authors present a reaction-diffusion model with thermodynamic constraints to describe RAD23B-mediated proteasomal liquid-liquid phase separation (LLPS) during substrate degradation. They claim the model reproduces experimental LLPS dynamics, reveals a concentration-dependent phase transition boundary modulated by proteasome activity and molecular interactions, and predicts bidirectional (enhancing or suppressing) context-dependent effects of LLPS on degradation efficiency.
- **Visible evidence base** Text descriptions of model equations (Eqs. 1-9), parameter values, simulation protocols, and qualitative references to experimental data from Ref. [19]; figure captions for Figs. 1-5; GitHub repository link for code and data
- **Missing materials affecting confidence** Figures and their actual plotted data; quantitative comparison metrics between simulation and experiment; parameter fitting procedures; sensitivity analysis details; supplementary information; code verification details

## Reviewer
- **Overall assessment** The manuscript addresses a timely and important question in proteasome biology, namely the functional consequences of LLPS on substrate degradation. The modeling framework is physically motivated and the authors make a serious attempt to connect their simulations to published experimental observations. However, the current text does not provide sufficient quantitative evidence to fully support several central claims, particularly the claimed "successful" reproduction of experimental dynamics and the generality of the bidirectional effect. The derivation of the boundary condition (Eq. 9) relies on assumptions that are not fully justified. The manuscript would benefit from clearer presentation of quantitative validation, sensitivity analyses, and a more careful treatment of parameter choices.

- **Who would be interested in the results, and why** Researchers studying phase separation in cellular processes, particularly those interested in the ubiquitin-proteasome system, protein quality control, and the physical chemistry of biomolecular condensates. The modeling approach may also interest computational biologists working on reaction-diffusion systems coupled to phase behavior. The proposed link between LLPS and UPS overload could attract cell biologists studying stress responses and protein homeostasis.

- **Major strengths** The manuscript addresses a significant gap in the field by providing a quantitative framework for proteasomal LLPS. The model incorporates thermodynamic constraints in a physically reasonable manner. The authors explicitly connect their work to experimental observations and propose testable predictions. The bidirectional effect on degradation efficiency is an interesting and non-obvious prediction. The code and data are made publicly available.

- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence sufficiency
- **Claim pointer** "The model successfully captures experimental LLPS dynamics" (Abstract) and "These simulation results show qualitative agreement with experimental observations [19]" (Results, Temporal evolution section)
- **Evidence pointer** Fig. 3 and accompanying text; location not provided for quantitative metrics
- **Concern** The claim of successful capture of experimental dynamics is supported only by qualitative statements and a figure that is not visible in the provided text. No quantitative error metrics, correlation coefficients, or statistical tests comparing simulation output to experimental data are reported. The normalization and scaling of experimental time axes (described as "scaled and shifted to align with the simulation") raise concerns about the strength of the comparison, as arbitrary scaling can make many curves appear similar.
- **Why it matters** The central claim of the paper rests on the model's ability to reproduce experimental observations. Without quantitative validation, the reader cannot assess how well the model captures the essential physics or whether the agreement is trivial or meaningful.
- **Resolution test** Provide quantitative comparison metrics (e.g., time to peak droplet count, peak droplet count value, decay time constants) with confidence intervals. Report the scaling and shifting parameters used for experimental alignment and justify them on physical grounds. If possible, perform the comparison without arbitrary rescaling or with clearly stated and justified normalization procedures.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Model justification
- **Claim pointer** "The transition boundary is also modulated by the R-S interaction strengths χ's" and "decreasing the proteasomal degradation rate kd initially shifts the transition boundary toward higher initial S fraction" (Results, Transition boundary section)
- **Evidence pointer** Fig. 4 and accompanying text; location not provided for parameter ranges
- **Concern** The parameter values used in the simulations are stated once in the methods section, but no justification is provided for these choices. The manuscript does not report how parameter values were estimated from experimental data, whether they fall within physiologically plausible ranges, or how sensitive the results are to parameter variations. The sensitivity analysis shown in Figs. 4E and 4F is limited to ±5% variation in interaction parameters only, and does not explore the full parameter space.
- **Why it matters** For a quantitative model, parameter choices determine the validity of predictions. Without justification or broader sensitivity analysis, the reader cannot determine whether the reported phase boundaries and bidirectional effects are robust features of the model or artifacts of particular parameter choices.
- **Resolution test** Provide a table of all parameters with their biological or physical basis, and report sensitivity analyses over a wider range of parameter values. Show that the qualitative conclusions (existence of phase boundary, bidirectional effect) hold across reasonable parameter ranges.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Theoretical derivation
- **Claim pointer** "The critical boundary distinguishing the bidirectional effects of LLPS can be derived as follows... From T>T′, one has Eq. (8)" (Results, Impact of LLPS section)
- **Evidence pointer** Equations 8-9 and accompanying text
- **Concern** The derivation of the boundary condition (Eq. 9) from Eq. (8) is not shown in detail. The relationship between the scaling factors αb and αd and the model parameters (k+b, kd) is not specified. The assumption that αb and αd are constant across varying k+b and kd is stated but not justified. The coefficient ϑ in Eq. (8) is not defined or estimated.
- **Why it matters** The linear boundary (Eq. 9) is presented as a key theoretical result, but without a complete derivation and justification of assumptions, its validity and generality are unclear.
- **Resolution test** Provide a step-by-step derivation of Eq. (8) from the model equations, define all symbols, justify the constancy assumption for αb and αd, and show how γ in Eq. (9) relates to model parameters.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Claim support
- **Claim pointer** "LLPS was found to have bidirectional (enhancing or suppressing), context-dependent effects on degradation efficiency" (Abstract) and "LLPS enhances degradation in regions with high kd and low k+b; LLPS suppresses degradation when kd is low and k+b is high" (Results, Impact of LLPS section)
- **Evidence pointer** Fig. 5 and accompanying text; location not provided for quantitative thresholds
- **Concern** The bidirectional effect is demonstrated only within a specific parameter range shown in Fig. 5B. The text does not report the range of kd and k+b values explored, the magnitude of enhancement or suppression, or whether these parameter ranges are biologically relevant. The claim of "context-dependent" effects would be strengthened by identifying which biological contexts correspond to the enhancing versus suppressing regimes.
- **Why it matters** The bidirectional effect is a central novel prediction of the model. Without clear reporting of the parameter ranges and biological correspondence, the practical significance of this prediction is unclear.
- **Resolution test** Report the full parameter ranges explored, the magnitude of the effect (e.g., fold-change in degradation time), and discuss which biological scenarios (e.g., stress conditions, cell types) might correspond to each regime.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Model description
- **Evidence pointer** Equations 1-6 and accompanying text
- **Issue** The model description is dense and some symbols are not clearly defined at first use. For example, the relationship between the chemical potential μi in Eq. (4) and the free energy f in Eq. (5) is not explicitly stated. The physical meaning of the wi parameters in Eq. (6) is not explained.
- **Required correction** Define all symbols at first use, explicitly state the relationship between chemical potential and free energy, and provide physical interpretations for the wi parameters.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Reproducibility
- **Affected element** Numerical methods
- **Evidence pointer** Temporal evolution section, first paragraph
- **Issue** The numerical method is described as "finite difference method" but no details are given about time stepping scheme, convergence criteria, or numerical stability. The domain sizes and grid resolutions are stated, but the time step and total simulation time are not reported.
- **Required correction** Provide details on the time integration scheme, time step size, total simulation duration, and any convergence or stability checks performed.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Presentation
- **Affected element** Figure captions
- **Evidence pointer** Fig. 4 caption
- **Issue** The caption for Fig. 4 is incomplete. It describes panels A-D but does not describe panels E and F, which are referenced in the text.
- **Required correction** Complete the figure caption to describe all panels.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Terminology
- **Affected element** Discussion section
- **Evidence pointer** Discussion, paragraph 2
- **Issue** The term "UPS overload" is used to describe the phase boundary, but the relationship between the model's phase boundary and the physiological concept of overload is not precisely defined. The text states the phase boundary "effectively defines" the overloaded state, but the operational definition is not explicit.
- **Required correction** Provide an explicit operational definition of "UPS overload" in terms of model variables or observables.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Discussion
- **Evidence pointer** Discussion, final paragraph
- **Issue** The discussion of future work mentions integrating the model with an autophagic flux model but does not provide any preliminary results or even a sketch of how this integration would be achieved.
- **Required correction** Either remove this speculative paragraph or provide a more concrete outline of the proposed integration approach.

- **Concern ID** R1-m6
- **Severity** Minor
- **Axis** Language
- **Affected element** Throughout
- **Evidence pointer** Multiple locations
- **Issue** Several typographical and grammatical errors are present, including "writen" (should be "written"), "to some extend" (should be "to some extent"), and inconsistent use of subscripts (k₂ vs k2).
- **Required correction** Careful proofreading and consistent notation throughout.

## Risk / unsupported claims
- The claim that the model "successfully captures experimental LLPS dynamics" is not quantitatively supported in the provided text; only qualitative agreement is described, and the comparison involves arbitrary scaling of experimental time axes.
- The claim of bidirectional effects on degradation efficiency is supported only within an unspecified parameter range; the biological relevance of the enhancing and suppressing regimes is not established.
- The theoretical derivation leading to Eq. (9) is incomplete, with undefined symbols and unjustified assumptions.
- The statement that "weakening molecular interactions... or reducing proteasomal degradation rates can shift this saturation boundary" is presented as a general result but is only demonstrated for specific parameter variations.
- The claim that the model "provides a quantitative definition for the hypothesized UPS saturation state" is not fully supported, as the relationship between the model's phase boundary and the physiological concept of UPS overload is not rigorously established.
- The generalization of the model to p62-mediated LLPS is speculative and not supported by any simulation results in the provided text.