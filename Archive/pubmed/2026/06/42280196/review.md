## Review setup
- **Input scope** Full manuscript text (abstract, introduction, results, discussion, conclusions, methods) as provided
- **Assessment boundary** Scientific validity, internal consistency, and evidentiary support of the modeling claims; no assessment of experimental data quality beyond what is reported
- **Shared manuscript claim summary** The authors propose a colloid model to explain how HEPES, an additive that decreases lysozyme crystal solubility (salting-out), simultaneously lowers the liquid-liquid phase separation (LLPS) temperature. They attribute this to an increase in protein-protein attraction energy in the crystal (2.7% increase) combined with increased anisotropy of interactions in solution, modeled via a modified Barker-Henderson perturbation theory with a temperature-dependent effective attraction energy.
- **Visible evidence base** Solubility data (van't Hoff plots, Figure 2), LLPS boundary data (Figure 5), diffusion coefficient data referenced from prior work, crystal structure information (pdb 1E8L), Monte Carlo simulation comparisons (Figure 4)
- **Missing materials affecting confidence** Experimental LLPS data points are not shown numerically; diffusion coefficient data are referenced but not presented; no error analysis for LLPS fits; no sensitivity analysis for parameter choices; supplementary materials (WPT comparison) not provided

## Reviewer
- **Overall assessment** The manuscript addresses a genuinely interesting and non-obvious phenomenon: an additive that strengthens protein-protein attractions in the crystal lattice while weakening them in solution. The authors propose a plausible physical mechanism (increased anisotropy) and develop a tractable analytical model. However, the central claim rests on a parameter (α) that is adjusted post hoc to fit the data, and the physical interpretation of this parameter is speculative. The model's predictive power is limited, and the connection between the fitted α values and molecular reality is not established. The work is a useful phenomenological description but falls short of a mechanistic demonstration.

- **Who would be interested in the results, and why** Researchers in protein phase behavior, protein crystallization, and biopharmaceutical formulation science. The work is relevant to those studying how buffer components and additives modulate protein-protein interactions and phase diagrams, particularly in the context of crystallization yield enhancement via LLPS. The modeling framework may also interest the colloid science community working on anisotropic interactions.

- **Major strengths**
  1. The phenomenon is clearly identified and experimentally grounded: HEPES shows opposite effects on solubility and LLPS, which is counterintuitive and worth explaining.
  2. The modeling approach is systematic: starting from a standard perturbation theory, the authors identify a deficiency (incorrect second virial coefficient) and correct it, improving agreement with simulations.
  3. The use of a single adjustable parameter (α) to capture anisotropy is elegant and parsimonious.
  4. The consistency requirement (εSW = εS) between crystal and fluid models is a good check on internal coherence.
  5. The manuscript is clearly written and accessible to a broad physical chemistry audience.

- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence sufficiency
- **Claim pointer** The claim that the model "successfully explains" the effect of HEPES on LLPS temperature and second virial coefficient using only the parameter α.
- **Evidence pointer** Section 2.4, Figure 5
- **Concern** The model is fit to the LLPS data by adjusting α, and the authors report that α = 0.037 for REF and α = 0.027 for HEPES reproduce the data. However, no goodness-of-fit statistics, confidence intervals, or comparison of model predictions against independent data are provided. The claim of "successful" fitting is therefore not quantitatively established. Moreover, the model is not tested against any prediction outside the fitted dataset.
- **Why it matters** A model that is only shown to reproduce the data it was fit to has limited evidentiary value. The central conclusion that anisotropy (quantified by α) is the mechanism requires either independent validation or at least a demonstration that the fit is statistically meaningful and that alternative explanations are excluded.
- **Resolution test** Provide goodness-of-fit metrics (e.g., RMSD, chi-squared), confidence intervals on α, and ideally a prediction for a condition not used in fitting (e.g., a different additive concentration or temperature range).

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Physical interpretation
- **Claim pointer** The interpretation that α represents the fractional surface coverage of attractive sites and that its decrease from 0.037 to 0.027 corresponds to a physical change in interaction anisotropy due to HEPES.
- **Evidence pointer** Section 2.4, Equation (14)
- **Concern** The physical meaning of α is asserted but not derived from any molecular model. The authors estimate that the change in α corresponds to a reduction in binding area from ~100 Å² to ~10 Å² for one site, but this calculation assumes a specific mapping between α and surface area that is not justified. The temperature dependence of εeff in Equation (14) is a mathematical construct, and its connection to actual anisotropic interactions (e.g., patchy colloids, specific binding sites) is not established.
- **Why it matters** The manuscript's central mechanistic claim is that HEPES increases anisotropy. If α is merely a fitting parameter with no clear physical correspondence, the explanation is phenomenological rather than mechanistic. The reader cannot assess whether the proposed mechanism is plausible or merely a mathematical convenience.
- **Resolution test** Derive Equation (14) from a microscopic model of anisotropic interactions, or provide independent experimental evidence (e.g., scattering data, simulation) that quantifies anisotropy changes upon HEPES addition.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Model assumptions
- **Claim pointer** The assumption that HEPES does not alter protein conformation and that the crystal structure is unchanged.
- **Evidence pointer** Section 1, Section 2.2
- **Concern** The authors assume HEPES does not change protein conformation, but the cited crystal structure (pdb 1E8L) is from crystals grown in HEPES buffer. It is not clear whether the REF crystal structure is identical. If HEPES binding alters the protein's conformation or the crystal lattice, the interpretation of the 2.7% increase in εS as purely energetic is questionable. Additionally, the model assumes the same εS applies to both crystal and fluid phases, but the physical environment differs substantially.
- **Why it matters** The consistency requirement (εSW = εS) is central to the model's internal logic. If the crystal and solution environments are not comparable, this assumption is unjustified and could lead to incorrect conclusions about the relative roles of attraction energy and anisotropy.
- **Resolution test** Compare crystal structures grown with and without HEPES; or justify the assumption with structural data showing no conformational change.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Scope of validation
- **Claim pointer** The model's general applicability to "multifaceted effects of additives on the phase diagram of protein solutions" as stated in the Conclusions.
- **Evidence pointer** Section 3
- **Concern** The model is tested on a single additive (HEPES) and a single protein (lysozyme). The conclusion that the model is "useful" for describing additive effects generally is an overreach. No evidence is presented that the framework applies to other additives or proteins, and the specific mechanism (physical cross-linking in the crystal) may be unique to HEPES-lysozyme.
- **Why it matters** The stated scope of the conclusion exceeds the evidence base. A more cautious statement about the model's applicability to the specific system studied would be appropriate.
- **Resolution test** Apply the model to at least one additional additive or protein system, or temper the conclusion to reflect the single-system validation.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Section 2.1, Equation (4)
- **Evidence pointer** location not provided
- **Issue** The Carnahan-Starling equation of state is cited, but the specific form used in Equation (4) is not derived or referenced clearly. The third term appears to be the standard CS form, but the notation is compressed.
- **Required correction** Provide a reference for the Carnahan-Starling form used and clarify the notation.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Reproducibility
- **Affected element** Section 4, Methods
- **Evidence pointer** location not provided
- **Issue** The numerical procedure is described, but convergence criteria and tolerance values are not specified. The statement that "computational errors become ultimately negligible" is vague.
- **Required correction** Specify convergence tolerances and numerical precision used.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Data presentation
- **Affected element** Figure 5
- **Evidence pointer** location not provided
- **Issue** The experimental LLSP data points are shown in Figure 5, but the numerical values are not tabulated or provided in the text. This limits the reader's ability to assess the quality of the fit.
- **Required correction** Provide the experimental data in tabular form or as supplementary material.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Interpretation
- **Affected element** Section 2.4, Equation (15)
- **Evidence pointer** location not provided
- **Issue** The calculation of B from εeff is presented as a prediction, but the relationship between εeff and the actual second virial coefficient is not discussed. The use of εeff in Equation (15) is an approximation that should be justified.
- **Required correction** Discuss the validity of using εeff in the second virial coefficient expression and any limitations.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Literature context
- **Affected element** Section 1
- **Evidence pointer** location not provided
- **Issue** The introduction cites prior work on HEPES effects but does not discuss alternative explanations for the observed phenomenon (e.g., specific ion effects, excluded volume, or changes in hydration).
- **Required correction** Briefly discuss alternative mechanisms and why the proposed model is preferred.

- **Technical failings that need to be addressed before the case is established**
  - R1-M1: Lack of statistical validation of the fit quality for α
  - R1-M2: Unjustified physical interpretation of α
  - R1-M3: Unverified assumption of unchanged protein conformation
  - R1-M4: Overstated generality of conclusions

- **Assessment against Nature-style criteria**
  - **Originality**: The observation of opposite effects of an additive on solubility and LLPS is interesting and somewhat counterintuitive. The proposed mechanism (increased anisotropy) is a reasonable hypothesis, but similar ideas exist in the colloid literature on patchy particles. The specific application to HEPES-lysozyme is novel.
  - **Scientific importance**: The work addresses a practical problem (controlling protein crystallization and phase behavior) and a fundamental question (how anisotropic interactions affect phase diagrams). However, the importance is moderate; the findings are system-specific and the model is phenomenological.
  - **Interdisciplinary readership**: The manuscript is likely to appeal to physical chemists, biophysicists, and formulation scientists. The modeling framework is accessible, but the lack of molecular-level insight limits broader appeal.
  - **Technical soundness**: The thermodynamic framework is standard, and the correction to the second virial coefficient is a valid improvement. However, the central fitting parameter (α) is not independently validated, and the physical interpretation is speculative. The numerical methods appear sound but are not fully documented.
  - **Readability for nonspecialists**: The manuscript is clearly written and the logic is easy to follow. The use of figures helps convey the main ideas. However, the physical meaning of α and the model's limitations could be explained more clearly for a general audience.

- **Recommendation posture** Supportive if technical concerns are resolved. The manuscript presents a plausible and interesting explanation for a non-obvious phenomenon, but the central claims require stronger validation. Specifically, the authors must (1) provide statistical evidence for the quality of the α fits, (2) justify or refine the physical interpretation of α, (3) address the assumption of unchanged protein conformation, and (4) temper the generality of the conclusions. If these issues are addressed, the work would be a valuable contribution to the protein phase behavior literature.

## Risk / unsupported claims
- The claim that HEPES increases protein-protein attraction energy in the crystal by 2.7% is supported by the van't Hoff analysis, but the assumption that this is purely energetic (not entropic) is not tested.
- The claim that the model "successfully" fits the LLSP data is unsupported without goodness-of-fit statistics.
- The physical interpretation of α as fractional surface coverage of attractive sites is unsupported by independent evidence.
- The claim that the model is "useful for describing the multifaceted effects of additives" generally is unsupported, as only one additive-protein system is examined.
- The prediction of B values from εeff is presented without discussion of its validity or comparison to direct measurements.