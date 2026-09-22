## Review setup
- **Input scope** Full manuscript text (preprint, bioRxiv)
- **Assessment boundary** Scientific content, methodological soundness, and claims as presented in the provided manuscript text
- **Shared manuscript claim summary** The authors construct a deep Markov state model (deep MSM) using a multi-input neural network architecture to characterize folding-upon-binding pathways of the intrinsically disordered protein NTAIL to the X domain (XD) of the measles virus phosphoprotein complex, based on a 200 μs MD simulation. They report resolving two distinct encounter complexes and a kinetic trap, and conclude that folding-upon-binding is not well described by a conformational selection / induced fit dichotomy.
- **Visible evidence base** Main text, Methods, Supplementary Figures 1–19, Supplementary Tables 1–2 (referenced but not fully visible in the provided material)
- **Missing materials affecting confidence** Supplementary figures and tables referenced in the text are not provided in the submitted material. This limits the ability to fully assess the validity of the MSM validation, state assignments, and quantitative claims.

## Reviewer
- **Overall assessment** This manuscript presents a technically sophisticated application of deep learning-based Markov state modeling to a challenging and biologically relevant problem: the folding-upon-binding mechanism of an intrinsically disordered protein. The multi-input neural network architecture is a novel and potentially valuable contribution. The central claim that the observed pathways are inconsistent with a simple conformational selection / induced fit dichotomy is interesting and potentially important. However, the manuscript as presented has several significant weaknesses. The most critical is the lack of the supplementary material, which contains essential validation data (CK tests, implied timescales, state properties). Without these, the validity of the deep MSM cannot be fully assessed. Additionally, the comparison with the conventional tICA-based HMSM is presented descriptively but lacks a rigorous quantitative framework for establishing the superiority of the deep MSM. The connection to experimental data, while discussed, is largely qualitative. The manuscript would be significantly strengthened by a more direct and quantitative comparison of the two modeling approaches and a clearer demonstration of the biological novelty of the findings beyond what was already known from the original simulation study.
- **Who would be interested in the results, and why** Researchers in the fields of computational biophysics, intrinsically disordered proteins, and Markov state model methodology. The work is directly relevant to those studying protein-protein interactions involving IDPs and to method developers interested in applying deep learning to biomolecular simulations. The findings on the nature of encounter complexes and the lack of a simple induced-fit/conformational-selection dichotomy would be of interest to a broad biophysical audience.
- **Major strengths**
    1.  The use of a multi-input neural network architecture that combines convolutional and fully connected layers to process different types of structural features is a novel and well-motivated methodological contribution.
    2.  The study addresses a fundamental and challenging question in IDP biology: the atomic-level mechanism of folding-upon-binding.
    3.  The analysis is based on a long (200 μs) unbiased MD simulation, which is a valuable resource.
    4.  The authors are appropriately cautious in interpreting their results in the context of experimental data and acknowledge limitations of the simulation temperature.
- **Major Concerns**
    - **Concern ID** R1-M1
    - **Severity** Major
    - **Blocking** Yes
    - **Axis** Technical soundness / Validation
    - **Claim pointer** The deep MSM is a valid and improved model compared to the tICA HMSM, as evidenced by resolved and converged implied timescales and a valid Chapman-Kolmogorov test.
    - **Evidence pointer** Supplementary Figures 2 and 11, "location not provided" for the specific CK test results of the deep MSM.
    - **Concern** The manuscript states that the tICA HMSM failed the CK test and that the deep MSM passes it, but the actual validation data for the deep MSM (CK test, implied timescales) is only in the supplementary material, which was not provided. The claim of improved model quality is central to the paper's narrative and cannot be verified from the main text alone. The authors state the tICA HMSM "failed to satisfy the generalized Chapman-Kolmogorov (CK) test" but do not show this failure, nor do they show the successful CK test for the deep MSM in the main text.
    - **Why it matters** The validity of all subsequent kinetic and mechanistic conclusions rests on the quality of the MSM. Without seeing the validation data, the core technical foundation of the paper is unverifiable.
    - **Resolution test** Provide the supplementary figures (CK test plots, implied timescale plots) for both the tICA HMSM and the deep MSM in the main text or as accessible supplementary material. The CK test for the deep MSM should clearly show that predicted and observed transition probabilities agree within error for all states at multiple lag times.
    - **Concern ID** R1-M2
    - **Severity** Major
    - **Blocking** No
    - **Axis** Scientific importance / Novelty
    - **Claim pointer** The deep MSM resolves two structurally and kinetically distinct encounter complex states and a kinetic trap, providing new mechanistic insight beyond the previous 1D reaction coordinate analysis.
    - **Evidence pointer** Figures 4–5, Supplementary Figures 12–18.
    - **Concern** The authors demonstrate that the deep MSM provides higher resolution than the tICA HMSM and the 1D reaction coordinate. However, the biological significance of this increased resolution is not fully established. The key claim is that the pathways are not consistent with induced fit or conformational selection. This is an important claim, but the manuscript does not provide a clear, quantitative definition of what would constitute these mechanisms in the context of the MSM, nor does it compare the observed flux to a null model or a model with these mechanisms imposed. The conclusion is largely based on the observation that both encounter complexes proceed through similar downstream states, but a more rigorous analysis of the flux distribution and its statistical significance is needed.
    - **Why it matters** The central scientific message is that the mechanism is more complex than the classic dichotomy. If this is not rigorously demonstrated, the paper's impact is significantly reduced.
    - **Resolution test** Provide a quantitative analysis of the transition paths, e.g., using transition path theory to calculate the flux through different pathways and compare the observed flux distribution to what would be expected if the system followed a strict conformational selection or induced fit mechanism. This could involve defining order parameters that distinguish these mechanisms and showing that the flux does not partition accordingly.
    - **Concern ID** R1-M3
    - **Severity** Major
    - **Blocking** No
    - **Axis** Technical soundness / Comparison with previous work
    - **Claim pointer** The deep MSM approach provides advantages over the previously published 1D reaction coordinate analysis of the same simulation.
    - **Evidence pointer** Supplementary Figure 19.
    - **Concern** The comparison with the 1D reaction coordinate is made by showing that the deep MSM states overlap in the projection onto the reaction coordinate. This is a valid point, but it is somewhat weak. A more compelling comparison would be to show that the deep MSM can predict experimental observables (e.g., chemical shifts, FRET efficiencies) more accurately than the 1D reaction coordinate model, or that it provides a more statistically robust description of the kinetics (e.g., lower Bayesian evidence).
    - **Why it matters** The paper's methodological contribution is the deep MSM. To be impactful, it must be shown to be not just different, but better in a meaningful way.
    - **Resolution test** Perform a quantitative comparison of the two models, e.g., by computing the Akaike or Bayesian information criterion, or by comparing the ability of each model to reproduce the simulation data (e.g., via cross-validation).
- **Minor Comments**
    - **Concern ID** R1-m1
    - **Severity** Minor
    - **Axis** Clarity
    - **Affected element** Abstract
    - **Evidence pointer** Abstract, "location not provided"
    - **Issue** The abstract states "We do not, however, find evidence for the existence of canonical conformational selection or induced fit binding pathways." This is a strong negative claim. It would be more precise to state that the observed pathways are not well described by a simple dichotomy, as is done in the Discussion.
    - **Required correction** Rephrase the abstract to be more nuanced, e.g., "The observed pathways are not consistent with a simple conformational selection or induced fit dichotomy."
    - **Concern ID** R1-m2
    - **Severity** Minor
    - **Axis** Clarity / Technical soundness
    - **Affected element** Methods, "Input data for Markov State Models"
    - **Evidence pointer** Methods, "location not provided"
    - **Issue** The authors state that the simulation was performed at 400 K, which is above the physiological temperature. The rationale for this choice is not given in the main text, only referenced to the original simulation study.
    - **Required correction** Briefly state the rationale for using 400 K (e.g., to enhance sampling of binding/unbinding events) in the main text.
    - **Concern ID** R1-m3
    - **Severity** Minor
    - **Axis** Readability
    - **Affected element** Results, "A deep Markov state model resolves two structurally and kinetically distinct encounter complex states and a kinetic trap"
    - **Evidence pointer** Figure 5, "location not provided"
    - **Issue** The description of the differences between the two encounter complexes (states 6 and 7) is clear, but the description of the kinetic trap (state 5) is less so. The text mentions it transitions almost exclusively to state 6, but the structural basis for this trap (the non-native contacts) could be described more explicitly in the main text.
    - **Required correction** Add a sentence in the main text explicitly describing the non-native contacts that stabilize state 5 and how they differ from those in state 6.
    - **Concern ID** R1-m4
    - **Severity** Minor
    - **Axis** Technical soundness
    - **Affected element** Methods, "Estimation of trajectory observables and error analysis"
    - **Evidence pointer** Methods, "location not provided"
    - **Issue** The authors state that error estimates from the deep MSM are "lower bounds of the trial errors" because they used the same unconstrained VAMPnet for all 30 constrained training runs. This is an important caveat, but it is only mentioned in the Methods. It should be highlighted in the Results or Discussion when presenting the quantitative results (e.g., MFPTs, populations).
    - **Required correction** Add a sentence in the Results or Discussion reminding the reader that the reported error bars for the deep MSM are likely underestimated.
- **Technical failings that need to be addressed before the case is established**
    - R1-M1: The validation of the deep MSM (CK test, implied timescales) is not visible in the provided material. This is a blocking issue.
    - R1-M2: The central mechanistic claim (no induced fit / conformational selection) is not rigorously demonstrated with quantitative flux analysis.
- **Assessment against Nature-style criteria**
    - **Originality** High. The application of a multi-input deep MSM with a convolutional neural network to an IDP folding-upon-binding problem is novel.
    - **Scientific importance** Potentially high. The findings could challenge the prevailing simple models of IDP binding mechanisms and provide a more nuanced view of the energy landscape. However, the importance is contingent on the robustness of the mechanistic claims.
    - **Interdisciplinary readership** Moderate. The work is primarily of interest to computational biophysicists and biochemists. The biological implications are clear but the methods are specialized.
    - **Technical soundness** Currently not fully assessable. The methodological approach is sound in principle, but the lack of validation data in the provided material is a major concern. The comparison with the tICA HMSM is not quantitative enough.
    - **Readability for nonspecialists** The abstract and introduction are accessible. The results and methods sections are dense and will be challenging for nonspecialists, but this is typical for a methods-focused paper.
- **Recommendation posture** Supportive if technical concerns are resolved. The core idea is interesting and the methods are sophisticated. However, the manuscript cannot be accepted in its current form. The authors must provide the supplementary validation data and strengthen the quantitative analysis supporting their central mechanistic claim.

## Risk / unsupported claims
- The claim that the deep MSM is a valid and superior model to the tICA HMSM is unsupported without the supplementary validation data.
- The claim that the observed pathways are inconsistent with canonical conformational selection or induced fit is not rigorously supported by the quantitative analysis presented in the main text.
- The claim that the deep MSM identifies a "kinetic trap" is based on the transition probabilities, but the biological or functional significance of this trap is not established.
- The comparison with experimental data (NMR, stopped-flow, phi-values) is qualitative and does not constitute a validation of the model.