## Review setup
- **Input scope** Full manuscript text, including Significance, Results, Discussion, Materials and Methods, and supplementary figure/table references
- **Assessment boundary** Scientific validity, technical soundness, and conceptual contribution of the reported findings on hollow condensate formation via gelation-induced spinodal decomposition
- **Shared manuscript claim summary** The authors report that p53 protein (p534M ΔTAD) forms homogeneous condensates with low-affinity random dsDNA, and that subsequent addition of high-affinity p21 DNA induces a transition to hollow condensates. They propose a mechanism involving p21 DNA-induced peripheral gelation, core depletion of protein and random DNA, and spinodal decomposition in the condensate interior. A three-component continuum model is presented to support this mechanism.
- **Visible evidence base** Main text figures 1–6 (referenced), SI Appendix figures S1–S8 (referenced), Movies S1–S4 (referenced), experimental methods (droplet assays, FRAP, AFM-FS, FCS, EMSA), and numerical simulation details (in SI Appendix)
- **Missing materials affecting confidence** SI Appendix content (detailed methods, supplementary figures, model equations, parameter values) is not provided in the submitted material. Movies S1–S4 are not viewable. Raw data and statistical details are not available. The GitHub repository is referenced but not assessed.

## Reviewer
- **Overall assessment** This manuscript presents an interesting and potentially significant observation: the formation of hollow condensates from a three-component system of p53 protein, random DNA, and p21 DNA. The experimental work is carefully designed and the kinetic staging of the transition is compelling. The proposed mechanism of gelation-induced spinodal decomposition is plausible and the continuum model provides useful qualitative support. However, the manuscript has several technical weaknesses that need to be addressed before the case is fully established. The model's inability to reproduce key experimental observations (compositional separation of p21 and random DNA, condensate growth) is acknowledged but not resolved. The quantitative match between model and experiment is not demonstrated with rigorous statistical comparison. The claim of spinodal decomposition as the mechanism is inferred from model calculations rather than directly measured. The generality of the phenomenon beyond this specific p53-DNA system is not explored. Overall, the work is a solid contribution to the biophysics of biomolecular condensates, but the mechanistic claim requires stronger evidence.

- **Who would be interested in the results, and why** Researchers in the fields of biomolecular condensates, phase separation in biology, biophysics of DNA-protein interactions, and soft matter physics would be interested. The work addresses a fundamental question about how condensate architecture (hollow vs. homogeneous) can emerge from multicomponent interactions, which has implications for understanding cellular organization and for designing synthetic condensate-based materials. The proposed mechanism of gelation-induced spinodal decomposition could be relevant to other systems where condensates undergo morphological transitions.

- **Major strengths** 1) The observation of hollow condensate formation is novel and clearly demonstrated with confocal microscopy and fluorescence intensity analysis. 2) The kinetic staging (three distinct stages with characteristic timescales) provides a clear phenomenological framework. 3) The combination of experimental techniques (FRAP, AFM-FS, FCS) to characterize material properties is thorough. 4) The continuum model, while simplified, captures the essential qualitative features and provides a mechanistic hypothesis that can be tested. 5) The authors are transparent about the model's limitations.

- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Mechanistic claim
- **Claim pointer** The manuscript claims that hollow condensate formation is driven by gelation-induced spinodal decomposition, specifically that p21 DNA induces peripheral gelation, leading to core depletion and spinodal decomposition in the condensate interior.
- **Evidence pointer** Figures 4–6, Discussion section
- **Concern** The claim of spinodal decomposition as the underlying mechanism is inferred primarily from the continuum model, not from direct experimental measurement. The Min Eigenvalue analysis (Fig. 6A) is a model output, not an experimental observable. The authors do not provide direct experimental evidence that the system enters a spinodally unstable region of the phase diagram. The "abrupt transition" in Stage II (Fig. 2B) is consistent with spinodal decomposition, but could also be explained by other mechanisms such as nucleation and growth or a gelation-induced collapse. The model's assumption of a gelation field is introduced ad hoc, and the authors acknowledge the model cannot reproduce several key experimental observations (compositional separation, condensate growth, molecular escape). Without direct experimental validation of the spinodal decomposition mechanism, the central claim remains speculative.
- **Why it matters** The mechanistic claim is the central contribution of the paper. If the mechanism is not firmly established, the paper's significance is substantially reduced. The distinction between spinodal decomposition and other phase separation mechanisms has important implications for understanding and controlling condensate morphology.
- **Resolution test** Provide direct experimental evidence for spinodal decomposition, for example by measuring concentration fluctuations in the condensate interior during Stage II, or by demonstrating that the system follows the predicted scaling laws for spinodal decomposition. Alternatively, design experiments that can distinguish between spinodal decomposition and nucleation-and-growth, such as measuring the kinetics of the transition as a function of quench depth.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Model validation
- **Claim pointer** The manuscript claims that the continuum model "quantitatively recapitulates the key experimental observations presented in Figs. 1–3."
- **Evidence pointer** Figure 5, Figure 6, Discussion section
- **Concern** The claim of quantitative recapitulation is not supported by the evidence presented. The model outputs (Fig. 5B) are shown as representative snapshots, but no quantitative comparison between model and experiment is provided. The characteristic timescales τ1 and τ2 from the model (Fig. 5C) are compared to experimental values (Fig. 3B) only qualitatively, with no statistical analysis or error bars. The model does not reproduce the experimentally observed compositional separation of p21 DNA and random DNA (Fig. 2A), the increase in condensate size (Fig. S4), or the escape of molecules into the dilute phase (Fig. S5). These are significant discrepancies that undermine the claim of quantitative agreement.
- **Why it matters** A quantitative model that captures the key features of the system is essential to support the proposed mechanism. If the model cannot reproduce important experimental observations, its predictive power and the validity of the mechanistic insight derived from it are questionable.
- **Resolution test** Provide a rigorous quantitative comparison between model and experiment, including statistical measures of agreement. Address the discrepancies noted above, either by modifying the model or by explaining why these discrepancies do not affect the central mechanistic claim. Provide sensitivity analysis of model parameters.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Generality
- **Claim pointer** The manuscript implies that the findings reveal "fundamental principles of three-component hollow condensate formation" with "broader implications for disease mechanisms and therapeutic strategies."
- **Evidence pointer** Significance statement, Discussion section
- **Concern** The study is limited to a single protein (p534M ΔTAD) and two specific DNA sequences (random DNA and p21 DNA). The generality of the proposed mechanism is not tested. It is unclear whether the observed phenomenon is specific to this p53-DNA system or whether it represents a general principle applicable to other multicomponent condensate systems. The claim of broader implications for disease and therapy is speculative and not supported by any data.
- **Why it matters** The significance of the work depends on its generality. If the mechanism is specific to this particular system, the impact is limited. The authors should either provide evidence for generality or temper their claims.
- **Resolution test** Test the proposed mechanism in other protein-DNA or protein-RNA systems with different binding affinities and stoichiometries. Alternatively, clearly state the limitations of the study and avoid overgeneralizing the conclusions.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Technical rigor
- **Claim pointer** The manuscript claims that "the addition of p21 DNA induces a striking transition to hollow condensates" and that this is driven by p21 DNA preferentially localizing to the condensate surface.
- **Evidence pointer** Figures 1–2, SI Appendix Figures S2–S3
- **Concern** The evidence for p21 DNA localization at the condensate surface is based on fluorescence microscopy, but the resolution may be insufficient to definitively establish surface localization versus a gradient in the shell. The authors do not provide quantitative analysis of the p21 DNA distribution across the condensate. Additionally, the claim that p21 DNA "displaces" random DNA from the protein is inferred from the narrowing of the random DNA fluorescence signal, but alternative explanations (e.g., differential photobleaching, changes in quantum yield) are not ruled out.
- **Why it matters** The proposed mechanism relies on the specific localization of p21 DNA at the periphery. If this is not firmly established, the mechanism is weakened.
- **Resolution test** Provide high-resolution imaging (e.g., STED or confocal with improved resolution) to quantify the p21 DNA distribution. Use alternative labeling strategies (e.g., different fluorophores, FRET) to confirm the displacement of random DNA by p21 DNA.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Figure 2A
- **Evidence pointer** Figure 2A
- **Issue** The time points shown in Figure 2A (t = 2, 20, 26, 27, 28, 29, 40, 120 min) are not evenly spaced, and the abrupt transition in Stage II is described as occurring within a ~2-min interval. It is unclear how the time points were chosen and whether the transition could be missed between the 20 and 26 min time points.
- **Required correction** Provide a more detailed time course, particularly around the expected transition time, or justify the choice of time points.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Statistical rigor
- **Affected element** Figure 3B, Figure 4B
- **Evidence pointer** Figure 3B, Figure 4B
- **Issue** The manuscript reports τ1 and τ2 values and Young's modulus measurements, but the number of replicates and statistical analysis are not described in the main text. It is unclear how many independent experiments were performed and whether the differences are statistically significant.
- **Required correction** Provide the number of replicates, error bars, and statistical tests in the figure legends or main text.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Model description
- **Evidence pointer** SI Appendix (referenced)
- **Issue** The continuum model is described only briefly in the main text, with details relegated to the SI Appendix. The model equations, parameters, and numerical methods are not available in the submitted material, making it impossible to assess the model's validity.
- **Required correction** Ensure the SI Appendix provides a complete description of the model, including all equations, parameters, and numerical methods.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Interpretation
- **Affected element** Figure 6C
- **Evidence pointer** Figure 6C
- **Issue** The energy landscape schematic in Figure 6C is qualitative and not directly derived from the model calculations. It is unclear how this schematic relates to the quantitative results in Figures 6A and 6B.
- **Required correction** Either derive the energy landscape from the model or clearly label it as a schematic illustration.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Literature context
- **Affected element** Discussion section
- **Evidence pointer** Discussion section
- **Issue** The discussion of related work on hollow condensates and spinodal decomposition in biomolecular systems is brief. A more thorough comparison with existing literature would help position this work in the field.
- **Required correction** Expand the discussion to include a more comprehensive comparison with prior work on hollow condensates and related phase separation phenomena.

## Risk / unsupported claims
- The claim that spinodal decomposition is the mechanism underlying hollow condensate formation is not directly supported by experimental evidence and relies on model inference.
- The claim of "quantitative recapitulation" of experimental observations by the model is not supported by the data presented.
- The claim of "broader implications for disease mechanisms and therapeutic strategies" is speculative and not supported by any data in the manuscript.
- The claim that p21 DNA "displaces" random DNA from the protein is inferred from fluorescence intensity changes and is not directly demonstrated.
- The generality of the findings beyond the specific p53-DNA system is not established.