## Review setup
- **Input scope** Full manuscript text (main text, methods, figure legends referenced but not all figures provided)
- **Assessment boundary** Scientific content, methodological rigor, conceptual framework, and claims as presented in the provided text
- **Shared manuscript claim summary** The authors propose that sequence-dependent dynamics in biomolecular condensates formed by charge-neutral E-K polyampholytes are governed by transient electrostatic interactions, and that a "sticky Rouse-like" framework quantitatively connects sequence features (chain length N and charge patterning nSCD) to chain relaxation times, diffusivity, and viscosity across multiple length scales.
- **Visible evidence base** Main text with equations, methods section, references to figures (Figs. 1–6) and SI Appendix figures/tables; specific numerical values for scaling exponents and fitted parameters are reported in text
- **Missing materials affecting confidence** Actual figure panels, SI Appendix figures and tables, simulation trajectory data, and convergence analyses are not directly inspectable; this limits verification of quantitative claims

## Reviewer
- **Overall assessment** This manuscript presents a systematic computational study addressing an important question in biomolecular condensate physics: how amino acid sequence encodes material properties. The authors combine coarse-grained simulations with polymer theory to propose a predictive framework connecting sequence features to dynamics and rheology. The work is timely and potentially impactful, but several technical concerns regarding the validity of the sticky Rouse-like framework, the interpretation of scaling exponents, and the robustness of viscosity calculations need to be addressed before the central claims can be fully accepted.

- **Who would be interested in the results, and why** Researchers in biomolecular condensates, intrinsically disordered proteins, polymer physics, and soft matter physics would find this work relevant. The proposed framework could inform rational design of synthetic condensates and help interpret experimental measurements of condensate dynamics. The connection between sequence features and material properties is of broad interest to the biophysics and cell biology communities.

- **Major strengths** The study addresses a fundamental question with systematic parameter variation. The multiscale approach connecting monomer-level interactions to macroscopic properties is conceptually appealing. The authors test their framework across two different force fields (HPS and Martini), which strengthens the generality of their conclusions. The control simulations removing electrostatics provide a useful comparison. The phenomenological model linking sequence features to contact lifetimes is a valuable contribution.

- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Conceptual validity of the sticky Rouse-like framework
- **Claim pointer** The authors claim that a "sticky Rouse-like framework" using contact lifetimes τEK as an effective monomer relaxation time quantitatively predicts chain relaxation times, diffusivity, and viscosity across all sequences (Eq. 8, Fig. 6C–D).
- **Evidence pointer** Methods section "Phenomenological Model for Sequence-Dependent Contact Lifetimes"; Fig. 6; SI Appendix Figs. S21–S22
- **Concern** The central theoretical claim is that Eq. 8, τRs = τEK N²/3π², accurately predicts chain relaxation times. However, the classical sticky Rouse model requires that sticker lifetimes be comparable to or longer than Rouse times for the model to apply. The authors acknowledge that their measured contact lifetimes (4–83 ps) are much shorter than chain relaxation times, which means the system is not in the sticky Rouse regime as originally formulated. The authors call this a "sticky Rouse-like framework" but do not provide a rigorous derivation or justification for why replacing τ₀ with τEK in Eq. 7 is valid when the underlying assumptions of the sticky Rouse model are violated. This is a significant conceptual gap that undermines the theoretical foundation of the paper.
- **Why it matters** The predictive framework is the central contribution of the paper. If the theoretical basis for Eq. 8 is not rigorously justified, the claim of establishing a "predictive framework for sequence–dynamics–rheology relationships" is weakened. The agreement with simulation data could be fortuitous or could reflect a more general relationship that needs proper theoretical grounding.
- **Resolution test** Provide a derivation or theoretical argument for why τEK can serve as an effective monomer relaxation time in the Rouse model when τEK << τR. Alternatively, demonstrate that the predictions are insensitive to the specific form of the model and hold for a broader class of theories. The authors should clarify what "sticky Rouse-like" means precisely and what assumptions are being made.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Robustness of viscosity calculations
- **Claim pointer** The authors report viscosity scaling exponents between 1.91 and 2.14 with chain length N (Fig. 3B) and state that "we believe that the scaling trends remain robust" despite acknowledging "larger uncertainties due to statistical noise" in the Green–Kubo method.
- **Evidence pointer** Methods section "Calculation of Dense Phase Viscosity and Solvent Viscosity"; Fig. 3B; SI Appendix Figs. S25–S26
- **Concern** The Green–Kubo method is known to be challenging for viscous systems, with slow convergence and significant statistical noise. The authors acknowledge this but do not provide quantitative measures of uncertainty (e.g., error bars, confidence intervals) for the reported viscosity values or scaling exponents. The statement "we believe that the scaling trends remain robust" is not a substitute for statistical analysis. Without error quantification, the reported exponents (1.91–2.14) cannot be distinguished from the Rouse prediction (1.0) or the reptation prediction (3.4) with confidence.
- **Why it matters** The scaling exponents are used to support the claim that the system is in a crossover regime between Rouse and reptation dynamics. If the uncertainties are large, this conclusion is not well supported. The viscosity data also underpin the master curve collapse in SI Appendix Fig. S10, which is used to validate the Stokes–Einstein relation.
- **Resolution test** Provide error bars or confidence intervals for viscosity values and scaling exponents. Show convergence plots for the Green–Kubo integrals. If possible, use an alternative method (e.g., nonequilibrium simulations or periodic shear) to cross-validate viscosity values for at least a subset of systems.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Interpretation of scaling exponents and crossover regime
- **Claim pointer** The authors interpret scaling exponents for diffusivity (−1.70 to −2.24) and viscosity (1.91 to 2.14) as indicating a "crossover regime between Rouse and reptation behavior" and state that the system is "close to the onset of reptation-like behavior only at higher nSCD and longer N."
- **Evidence pointer** Fig. 3; SI Appendix Figs. S8–S10
- **Concern** The interpretation of the scaling exponents as indicating a crossover regime is plausible but not rigorously established. The exponents span a wide range, and the system sizes (N up to 250) may not be sufficient to observe asymptotic scaling behavior. The authors acknowledge that their N range spans less than two decades, which limits the reliability of power-law fits. However, they do not discuss whether finite-size effects or the specific range of N values could produce apparent exponents that do not reflect true asymptotic behavior. Additionally, the crossover interpretation is based on comparing exponents to theoretical predictions (Rouse: D∼N⁻¹, η∼N¹; reptation: D∼N⁻², η∼N³), but the observed exponents for viscosity (1.91–2.14) are far from both predictions, making the "crossover" interpretation somewhat ambiguous.
- **Why it matters** The crossover interpretation is used to motivate the need for the sticky Rouse-like framework. If the scaling exponents are not reliable or the crossover interpretation is not well supported, the motivation for the theoretical framework is weakened.
- **Resolution test** Perform simulations at longer chain lengths (e.g., N = 400, 500) to test whether scaling exponents approach asymptotic values. Alternatively, use more sophisticated finite-size scaling analysis to account for the limited N range. Discuss alternative interpretations of the observed exponents.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Generalizability of the phenomenological model
- **Claim pointer** The authors claim that their phenomenological model "allows τEK to be estimated directly from sequence features such as N and nSCD" and that this provides "a direct link between sequence-level features and local interaction timescales."
- **Evidence pointer** Methods section "Phenomenological Model for Sequence-Dependent Contact Lifetimes"; Fig. 6B
- **Concern** The phenomenological model (Eq. 27) is fitted to simulation data with four parameters (a, b, c, γ). The model is tested only on E-K sequences with a specific charge composition (equal numbers of E and K). It is unclear whether this model would generalize to other amino acid compositions, other types of interactions (e.g., hydrophobic, aromatic), or sequences with net charge. The authors acknowledge that their study focuses on charge-neutral E-K sequences but do not discuss the limits of applicability of their model.
- **Why it matters** The stated goal is to establish a "predictive framework for sequence–dynamics–rheology relationships." If the model only works for a narrow class of sequences, its predictive power is limited. The broader relevance to natural IDPs, which have diverse amino acid compositions, is not demonstrated.
- **Resolution test** Test the model on additional sequence families (e.g., sequences with different charge fractions, hydrophobic residues, or net charge). Discuss the expected range of applicability and potential modifications needed for other interaction types.

- **Concern ID** R1-M5
- **Severity** Major
- **Blocking** No
- **Axis** Comparison with experimental timescales
- **Claim pointer** The authors state that their findings "offer a generalizable framework for predicting how sequence-level features of intrinsically disordered proteins (IDPs) govern the material properties of biomolecular condensates" and that the framework could be used for "rational design of synthetic condensates with programmable properties."
- **Evidence pointer** Discussion section
- **Concern** The simulations use a coarse-grained model with implicit solvent (HPS) and a specific parameterization. The timescales reported (contact lifetimes of 4–83 ps) are much faster than typical experimental timescales for condensate dynamics (microseconds to milliseconds). The authors do not discuss how their simulation timescales relate to experimentally measurable quantities, nor do they provide any experimental validation or comparison with experimental data. The claim of "predictive" power for experimental systems is therefore not substantiated.
- **Why it matters** For the framework to be useful to the broader community, it needs to make predictions that can be tested experimentally. Without a clear connection to experimental observables, the practical impact of the work is limited.
- **Resolution test** Discuss how the simulation timescales can be mapped to experimental timescales (e.g., through dimensionless numbers or comparison with experimental measurements of condensate viscosity or diffusion). If possible, compare predictions with available experimental data on E-K or similar systems.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity of the "sticky Rouse-like" terminology
- **Affected element** Title and throughout
- **Evidence pointer** Title; Discussion
- **Issue** The term "sticky Rouse-like" is used throughout but is never precisely defined. The authors state that the classical sticky Rouse model assumptions do not strictly apply, but do not clearly articulate what "sticky Rouse-like" means as a distinct framework.
- **Required correction** Provide a clear definition of what is meant by "sticky Rouse-like" and how it differs from the classical sticky Rouse model. This could be a brief paragraph in the Discussion or a schematic in Fig. 6.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Statistical analysis of scaling exponents
- **Affected element** Fig. 3 and related text
- **Evidence pointer** Fig. 3; SI Appendix Figs. S8–S10
- **Issue** The scaling exponents are reported without confidence intervals or goodness-of-fit measures. Given the acknowledged statistical noise, it is important to know how well-constrained the exponents are.
- **Required correction** Report confidence intervals for all fitted exponents and provide goodness-of-fit statistics (e.g., R² values) for the power-law fits.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Justification for the range of nSCD values
- **Affected element** Methods section "Sequence Generation"
- **Evidence pointer** Methods; Fig. 3
- **Issue** The authors selected nSCD values of 0, 0.02, 0.20, 0.46, and 1 for each N. The rationale for these specific values is not provided. It is unclear whether these values sample the relevant parameter space adequately.
- **Required correction** Provide justification for the chosen nSCD values, or state that they were selected to span the range from alternating to diblock sequences.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Presentation of the master curve collapse
- **Affected element** SI Appendix Fig. S10
- **Evidence pointer** SI Appendix Fig. S10
- **Issue** The master curve collapse demonstrating D∼η⁻¹ is mentioned in the text but the quality of the collapse is not discussed. It is unclear how well the data collapse across different N and nSCD values.
- **Required correction** Provide a quantitative measure of the quality of the collapse (e.g., root-mean-square deviation from the master curve) and discuss any systematic deviations.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Discussion of limitations
- **Affected element** Discussion
- **Evidence pointer** Discussion
- **Issue** The Discussion does not explicitly address the limitations of the study, such as the use of a specific coarse-grained model, the limited sequence space explored, and the absence of experimental validation.
- **Required correction** Add a paragraph discussing the limitations of the study and the conditions under which the proposed framework is expected to hold.

- **Concern ID** R1-m6
- **Severity** Minor
- **Axis** Accessibility of the phenomenological model
- **Affected element** Eq. 27 and related text
- **Evidence pointer** Methods section "Phenomenological Model for Sequence-Dependent Contact Lifetimes"
- **Issue** The derivation of the phenomenological model is not fully explained. The relationship between nc (average number of like-charge nearest neighbors) and nSCD (nc = 1.76 nSCD^0.24) is presented as empirical, but the physical reasoning behind this relationship is not discussed.
- **Required correction** Provide additional physical reasoning for the empirical relationships used in the model, or acknowledge that they are purely empirical fits.

## Risk / unsupported claims
- The claim that the sticky Rouse-like framework provides a "quantitative" prediction of chain relaxation times, diffusivity, and viscosity is not fully supported because the theoretical basis for Eq. 8 is not rigorously justified when τEK << τR (R1-M1).
- The claim that the system is in a "crossover regime between Rouse and reptation dynamics" is not well supported given the large uncertainties in viscosity measurements and the limited range of N values (R1-M2, R1-M3).
- The claim that the framework is "generalizable" to natural IDPs is not supported by the data, as only E-K sequences with a specific composition were studied (R1-M4).
- The claim that the framework could enable "rational design of synthetic condensates with programmable properties" is speculative and not supported by experimental validation (R1-M5).
- The statement that "we believe that the scaling trends remain robust" is an opinion, not a quantitative claim, and should be replaced with statistical measures of uncertainty.
- The relationship between simulation timescales and experimental observables is not established, making the practical relevance of the quantitative predictions unclear.

## Assessment against Nature-style criteria
- **Originality**: The work addresses a timely and important question with a systematic approach. The idea of using a sticky Rouse-like framework to connect sequence features to condensate dynamics is conceptually interesting, though the theoretical foundation needs strengthening. The study does not introduce entirely new concepts but applies and extends existing polymer physics frameworks to a biologically relevant problem.
- **Scientific importance**: The question of how sequence encodes material properties of condensates is of high importance to the fields of biomolecular condensates and IDP biophysics. If the framework is validated, it could have significant impact on understanding condensate function and design.
- **Interdisciplinary readership**: The work bridges polymer physics, computational biophysics, and cell biology. The findings would be of interest to researchers in these fields, though the technical nature of the presentation may limit accessibility to a broader biological audience.
- **Technical soundness**: The simulation methodology is standard and appropriate for the questions addressed. However, the central theoretical claim (Eq. 8) lacks rigorous justification, and the statistical uncertainties in key measurements (viscosity, scaling exponents) are not adequately quantified. These issues need to be resolved before the technical soundness can be fully assessed.
- **Readability for nonspecialists**: The manuscript is generally well-written and the logical flow is clear. However, the polymer physics concepts and the distinction between the classical Rouse model, sticky Rouse model, and the proposed "sticky Rouse-like" framework may be challenging for nonspecialist readers. The Significance statement provides a helpful overview.

## Recommendation posture
Supportive if technical concerns are resolved. The manuscript addresses an important question with a systematic approach and the core idea is promising. However, the central theoretical claim needs rigorous justification, and the statistical uncertainties in key measurements need to be quantified. The authors should also clarify the scope and limitations of their proposed framework. If these concerns are adequately addressed, the work could make a valuable contribution to the field.