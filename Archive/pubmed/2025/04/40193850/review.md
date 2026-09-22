## Review setup
- **Input scope** Full manuscript text (Abstract, Introduction, Model, Results, Discussion, Methods) as provided by the user.
- **Assessment boundary** The review is based solely on the content of the provided manuscript text. No external data, figures, or supplementary files were available for inspection.
- **Shared manuscript claim summary** The authors propose a mathematical model, derived from polymer scaling theory, that relates the rate of molecular transport through the nuclear pore complex (NPC) to pore diameter and cargo size. The model is validated against coarse-grained Brownian dynamics simulations, and its applicability to small-to-medium-sized cargoes (∼5 nm) with weak FG-Nup interactions is claimed.
- **Visible evidence base** The manuscript text includes the model derivation, simulation methodology, and results presented in Figures 2, 4, 5, 6, 7, and 8 (figure content not visible). The text describes the simulation parameters and the use of forward flux sampling.
- **Missing materials affecting confidence** The actual figures, tables, and the supplementary file (S1 Text) are not provided. This limits the ability to independently verify the quantitative claims, the quality of the fit between model and simulation, and the robustness of the simulation methodology.

## Reviewer
- **Overall assessment** The manuscript addresses a timely and relevant question in NPC biology, namely how pore dilation modulates molecular transport. The authors present a clear theoretical framework based on polymer scaling theory and support it with extensive coarse-grained simulations. The model is elegant and the simulation results, as described, appear to support the main claims. However, the lack of access to the figures and supplementary material prevents a full assessment of the quantitative rigor and the validity of the fitting procedures. The manuscript is well-written and the logic is easy to follow, but several technical details and potential limitations need to be clarified before the case is fully established.
- **Who would be interested in the results, and why** This work will be of interest to biophysicists, cell biologists, and computational biologists studying nucleocytoplasmic transport, the biophysical properties of FG-Nups, and the mechanosensitivity of the NPC. The model provides a quantitative framework that could be used to interpret experimental data on transport rates under varying mechanical conditions, and it offers a testable prediction for how pore dilation affects flux. The findings are also relevant to researchers interested in the general physics of polymer solutions in confined geometries.
- **Major strengths**
    1. The manuscript addresses a significant gap in the field by providing a quantitative, mechanistic model for how pore size affects transport, moving beyond purely descriptive studies.
    2. The theoretical derivation is clearly presented and grounded in established polymer physics, making the model transparent and accessible.
    3. The use of Brownian dynamics simulations with a coarse-grained NPC model is appropriate for testing the theoretical predictions, and the use of forward flux sampling to compute rare transport events is a sophisticated and suitable approach.
    4. The model's predictions are shown to be robust across different FG-Nup lengths, and the authors honestly discuss the limitations of their approach, particularly regarding the range of cargo sizes and interaction strengths.
- **Major Concerns**
    - **Concern ID** R1-M1
    - **Severity** Major
    - **Blocking** Yes
    - **Axis** Technical soundness
    - **Claim pointer** The authors claim that the simulation data for both full and partial transport rates align well with the model formula (Eq. 6), and that the parameters γ and k0 are consistent across different FG-Nup lengths.
    - **Evidence pointer** Results section, Figures 5, 6, and 7; location not provided.
    - **Concern** The central validation of the model rests on the quality of the fit between the simulation data and the exponential relationship predicted by Eq. 5. The manuscript text states that the data "aligned linearly" and "fell on the same line," but without seeing the actual plots, it is impossible to assess the scatter, the range of x values over which the fit is valid, and whether the deviations at large x (acknowledged in the text) are significant enough to undermine the model's predictive power. The claim that γ and k0 are independent of N is a strong one that requires a quantitative comparison of the fitted parameters and their uncertainties across the three N values.
    - **Why it matters** The entire premise of the paper is that the model provides a quantitative description of transport. If the fit is poor or the parameters are not truly universal, the model's utility is significantly diminished. The authors' own admission of deviation at large x suggests the model's range of validity is limited, and this needs to be quantified and discussed more rigorously.
    - **Resolution test** The authors should provide the actual fit plots with error bars, the fitted values of γ and k0 with their confidence intervals for each N, and a statistical test (e.g., an F-test) to demonstrate that the parameters are not significantly different across N. They should also explicitly define the range of x (or cargo size) over which the model is valid and discuss the implications of the deviation at large x.
    - **Concern ID** R1-M2
    - **Severity** Major
    - **Blocking** Yes
    - **Axis** Technical soundness
    - **Claim pointer** The model assumes that the free energy of insertion, ΔG, is proportional to the polymer volume fraction, φ, and that the relevant length scale is the mesh size, ξ. The authors state that the model is valid for cargoes with weak, transient interactions with FG-Nups.
    - **Evidence pointer** Model section, Eq. 3; Results section, Figure 8; location not provided.
    - **Concern** The extension of the model to attractive cargoes is a key claim of the paper. The authors state that the data for attractive cargoes "conformed to our model equation," but the mechanism is unclear. The model's free energy term (Eq. 3) is derived for purely repulsive (steric) interactions. By absorbing the attractive interactions into the phenomenological parameter γ, the model loses its predictive power, as γ is no longer a simple function of the polymer properties. The authors need to clarify whether the model is truly predictive for attractive cargoes or merely a fitting function. The claim that the KD for importin-β (1-8 mM) is similar to the simulation's KD (10 mM) is interesting but needs more context. How sensitive is the model's validity to the KD value? What happens at lower KD (stronger binding)?
    - **Why it matters** The applicability to biologically relevant cargoes, which often have attractive interactions with FG-Nups, is a major selling point of the paper. If the model only works for a narrow range of interaction strengths, its biological relevance is limited. The current treatment of attractive interactions as a simple modification of γ is a significant simplification that needs to be justified.
    - **Resolution test** The authors should provide a more detailed analysis of the attractive cargo simulations, including the range of KD values tested. They should show how γ varies with the interaction strength and whether there is a critical KD beyond which the model breaks down. A more mechanistic treatment of the attractive interactions in the free energy model would strengthen the paper.
    - **Concern ID** R1-M3
    - **Severity** Major
    - **Blocking** No
    - **Axis** Scientific importance
    - **Claim pointer** The authors claim their model is complementary to that of Klughammer et al. [23], which applies to the regime where D > D*, while their model applies to D < D*.
    - **Evidence pointer** Discussion section; location not provided.
    - **Concern** The distinction between the two regimes (D < D* vs. D > D*) is a critical point. The authors state that for the yeast NPC, D* = 102 nm, while the physiological pore size is 40-60 nm, placing it in their model's regime. However, the transition between the two regimes is likely not sharp. Is there a smooth crossover? How does the model behave as D approaches D* from below? The authors should discuss the behavior of their model at the boundary of its validity and how it connects to the model of Klughammer et al. A more detailed comparison, perhaps with a figure showing both models' predictions across a range of D, would be very informative.
    - **Why it matters** The claim of complementarity is important for positioning the work in the field. If the two models do not connect smoothly, it suggests that neither fully captures the physics of the system. A clear demonstration of how the two models relate would significantly enhance the impact of the paper.
    - **Resolution test** The authors should provide a figure or a more detailed discussion showing the predictions of both models (theirs and Klughammer et al.'s) as a function of D, highlighting the crossover region. They should also discuss the physical origin of the transition between the two regimes.
- **Minor Comments**
    - **Concern ID** R1-m1
    - **Severity** Minor
    - **Axis** Readability for nonspecialists
    - **Affected element** Model section, Eq. 1
    - **Evidence pointer** Model section; location not provided.
    - **Issue** The derivation of the mesh size scaling (Eq. 1) is presented very briefly. The jump from the general scaling law to the specific form of Eq. 1 is not fully explained.
    - **Required correction** A few more sentences explaining the physical reasoning behind the scaling of ξ with φ would be helpful for readers not deeply familiar with polymer physics.
    - **Concern ID** R1-m2
    - **Severity** Minor
    - **Axis** Technical soundness
    - **Affected element** Methods section, Coarse-grained model
    - **Evidence pointer** Methods section; location not provided.
    - **Issue** The manuscript states that the NPC is modeled as a "cylindrical conduit" but does not specify the height (h) of the cylinder in the main text. The value of h is mentioned in the Discussion (h = 40 nm), but it should be defined in the Methods.
    - **Required correction** Please define all geometric parameters (h, D, etc.) in the Methods section when the model is first introduced.
    - **Concern ID** R1-m3
    - **Severity** Minor
    - **Axis** Technical soundness
    - **Affected element** Results section, Validation of the model formula
    - **Evidence pointer** Results section; location not provided.
    - **Issue** The manuscript states that the Flory exponent was close to ν = 0.588, indicating a good solvent. However, the value of ν is used as an input to the model. It is not clear if the simulations were designed to have ν = 0.588 or if this was an emergent property.
    - **Required correction** Please clarify whether the simulation parameters were chosen to reproduce a specific ν, or if ν was measured and then used in the model. This distinction is important for understanding the circularity of the validation.
    - **Concern ID** R1-m4
    - **Severity** Minor
    - **Axis** Readability for nonspecialists
    - **Affected element** Discussion section
    - **Evidence pointer** Discussion section; location not provided.
    - **Issue** The discussion of the biological implications is somewhat brief. The connection to mechanotransduction is mentioned, but the specific predictions of the model for this process could be elaborated.
    - **Required correction** A more detailed discussion of how the model's predictions could be tested in the context of mechanotransduction would strengthen the paper's impact.
- **Technical failings that need to be addressed before the case is established**
    - R1-M1: The quantitative fit of the model to the simulation data needs to be demonstrated with actual figures and statistical analysis.
    - R1-M2: The extension of the model to attractive cargoes needs a more rigorous justification and a clear definition of the range of validity.
- **Assessment against Nature-style criteria**
    - **Originality** The work is original in its specific application of polymer scaling theory to derive a closed-form relationship between pore size and transport rate in the NPC. While the general concept of the NPC as a polymer brush has been explored, the explicit derivation of a scaling law for transport rate as a function of pore dilation is a novel contribution.
    - **Scientific importance** The question of how NPC permeability is regulated is of high importance in cell biology. The model provides a quantitative framework that could be used to interpret a range of experimental observations and make testable predictions. The work is likely to be of interest to a specialized but significant community.
    - **Interdisciplinary readership** The work is inherently interdisciplinary, combining polymer physics, computational biology, and cell biology. However, the presentation is likely to be most accessible to readers with a background in biophysics or computational modeling. The biological implications are discussed, but the core of the paper is the model and its validation.
    - **Technical soundness** The theoretical derivation appears sound, and the simulation methodology is appropriate. However, the lack of access to the figures and supplementary material prevents a full assessment of the technical rigor. The concerns raised above regarding the fit quality and the treatment of attractive interactions are key to establishing technical soundness.
    - **Readability for nonspecialists** The manuscript is generally well-written and logically structured. The model derivation is clear, but some steps may be challenging for readers without a background in polymer physics. The biological context is well-established in the introduction and discussion.
- **Recommendation posture** Supportive if technical concerns are resolved. The core idea is interesting and the approach is sound, but the validation needs to be presented more rigorously. The authors must provide the actual data plots and a more detailed analysis of the model's limitations, particularly regarding attractive cargoes and the range of validity. Once these issues are addressed, the paper would be a valuable contribution to the field.

## Risk / unsupported claims
- The claim that the model is "comprehensive" in its applicability is not fully supported, as the authors themselves note deviations at large x and limitations for strongly attractive cargoes.
- The claim that the model is directly applicable to transcription factors and signaling molecules is based on size estimates, but the model does not account for specific molecular features beyond size and weak interactions.
- The comparison of the simulation's KD (10 mM) to the experimental KD for importin-β (1-8 mM) is presented as a validation, but the sensitivity of the model to this parameter is not explored.
- The statement that the model "offers a comprehensive understanding of the transport phenomena" is an overstatement, as the model is limited to a specific regime of pore sizes and interaction strengths.