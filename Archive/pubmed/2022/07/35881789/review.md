## Review setup
- **Input scope** Full manuscript text, including Significance statement, main text, Materials and Methods, and references to supplementary materials.
- **Assessment boundary** The review is based solely on the provided manuscript text. Supplementary figures, videos, and code repositories are referenced but were not provided for direct evaluation.
- **Shared manuscript claim summary** The authors investigate the biophysics of transcription factor (TF) condensates of the progesterone receptor (PR) in living cells. Using single-molecule tracking, machine learning, and theoretical modeling, they report that PR condensates grow via Brownian motion coalescence (BMC) at short times but reach a finite, nanoscale size at steady state. They propose that stochastic particle unbinding from condensates modulates growth dynamics and controls condensate size in this nonequilibrium system.
- **Visible evidence base** Main text figures (Fig. 1, 2, 3, 4) are described but not shown. The manuscript includes equations for tMSD, confinement size, cumulative probability distribution, and turning angle. References to SI Appendix figures (S1–S12), videos (Video S1), and a public GitHub repository are provided.
- **Missing materials affecting confidence** The actual figures, supplementary figures, videos, and code are not provided. This limits the ability to independently verify the quality of the data, the robustness of the image analysis, the accuracy of the ML classifications, and the validity of the simulation results.

## Reviewer
- **Overall assessment** This manuscript presents a compelling and timely study on the biophysics of transcription factor condensates in living cells. The combination of single-molecule tracking, machine learning, and theoretical modeling is powerful and appropriate. The observation that condensate growth deviates from classical BMC and reaches a finite size, with a proposed mechanism of particle unbinding, is novel and of significant interest. However, the strength of the conclusions is currently limited by the lack of direct visualization of the data and a clear quantitative link between the model's key parameter (Pu) and the experimental observations. The manuscript is well-written and the logic is clear, but several technical aspects require clarification and additional analysis to fully establish the case.
- **Who would be interested in the results, and why** This work will be of high interest to researchers in the fields of biophysics, cell biology, and gene regulation. Specifically, those studying phase separation, biomolecular condensates, transcription factor dynamics, and the physical principles governing nuclear organization will find the results valuable. The methodological approach combining single-molecule imaging with ML and theory will also appeal to a broad audience interested in quantitative biology.
- **Major strengths**
    1.  The study addresses a fundamental and timely question about the physical mechanisms governing TF condensate growth in living cells.
    2.  The combination of advanced single-molecule imaging (SPT), machine learning for trajectory analysis, and theoretical modeling is a powerful and modern approach.
    3.  The identification of a steady-state plateau in condensate size and the proposal of particle unbinding as a regulatory mechanism is a novel and significant contribution.
    4.  The model makes testable predictions, and the authors attempt to validate these with experimental data.
- **Major Concerns**
    - **R1-M1**
        - **Severity** Major
        - **Blocking** Yes
        - **Axis** Evidence
        - **Claim pointer** The manuscript claims that PR condensates grow via a Brownian motion coalescence (BMC) mechanism, supported by the log-normal distribution of condensate radii and a growth exponent β = 0.3505.
        - **Evidence pointer** Fig. 3D, Fig. 3E, and related text.
        - **Concern** The evidence for the BMC mechanism is based on a single fitted exponent (β = 0.3505) and a log-normal distribution. The fit quality, the statistical significance of the exponent compared to the expected 1/3, and the robustness of the log-normal fit are not presented. Furthermore, the manuscript states that a similar size distribution was observed in the absence of hormone, indicating a pre-existing population of condensates. This complicates the interpretation of the growth dynamics, as the measured growth may be a convolution of the growth of new condensates and the pre-existing population.
        - **Why it matters** The central claim of the paper is that growth is BMC-dominated at short times. If the evidence for this is weak or confounded by a pre-existing population, the foundation of the model is undermined.
        - **Resolution test** The authors should provide a more detailed analysis of the growth kinetics, including the distribution of growth exponents across individual condensates, a direct comparison of the fitted exponent to the theoretical value with error bars, and a clear demonstration that the pre-existing condensates do not confound the growth measurement. Ideally, they would track individual condensates over time to directly observe coalescence events and measure their growth trajectories.
    - **R1-M2**
        - **Severity** Major
        - **Blocking** Yes
        - **Axis** Evidence
        - **Claim pointer** The manuscript claims that stochastic particle unbinding (Pu) is the mechanism that leads to arrested growth and finite condensate size at steady state.
        - **Evidence pointer** Fig. 4 and related text.
        - **Concern** The theoretical model introduces a parameter Pu (probability of unbinding) and shows that it can lead to a plateau in condensate size. However, the manuscript does not provide a direct, quantitative link between this parameter and the experimental system. The observation of "escaping events" is mentioned, but the authors state that "their statistical quantification was challenging." The model's prediction of the percentage of condensed particles over time is compared qualitatively to experimental data, but a rigorous quantitative fit of the model to the experimental data to extract a value of Pu is not presented.
        - **Why it matters** The paper's central thesis is that particle unbinding controls condensate size. Without a quantitative link between the model's key parameter and the experimental data, the model remains a plausible hypothesis rather than a validated mechanism.
        - **Resolution test** The authors should attempt to quantitatively fit their model to the experimental data (e.g., the percentage of condensed particles vs. time, or the steady-state size distribution) to extract a best-fit value for Pu. They should also provide a more robust statistical analysis of the escaping events in their SPT data, perhaps by using longer trajectories or more sophisticated analysis methods, to directly measure the unbinding rate and compare it to the model's prediction.
    - **R1-M3**
        - **Severity** Major
        - **Blocking** No
        - **Axis** Technical Soundness
        - **Claim pointer** The manuscript claims that the slow-diffusing population of PR molecules within condensates corresponds to DNA-bound PR, and that the faster-diffusing population corresponds to unbound PR.
        - **Evidence pointer** Fig. 2, SI Appendix Fig. S8, and related text.
        - **Concern** The assignment of the two diffusing populations to DNA-bound and unbound states is inferred from their diffusion coefficients. While plausible, this assignment is not directly validated. For example, it is not shown that the slow population is immobile or exhibits binding kinetics consistent with specific DNA interactions. The authors also note a potential bias in their data towards slower molecules due to their longer residence time in the focal plane.
        - **Why it matters** The interpretation of the two populations is crucial for the biological model. If the slow population is not actually DNA-bound, the proposed mechanism of unbinding from DNA as the source of particle escape would be incorrect.
        - **Resolution test** The authors could use a more detailed analysis of the SPT data, such as the distribution of displacement steps or the residence time of molecules in the slow state, to provide stronger evidence for specific binding. They could also perform experiments with a DNA-binding mutant of PR to see if the slow population is abolished.
- **Minor Comments**
    - **R1-m1**
        - **Severity** Minor
        - **Axis** Clarity
        - **Affected element** Fig. 1C
        - **Evidence pointer** Fig. 1C and related text.
        - **Issue** The manuscript describes a "sharp transition" in the bound fraction at a critical ligand concentration of 10^-10 M. It is unclear how this critical concentration was determined and what the statistical significance of this transition is.
        - **Required correction** Please provide a more detailed description of how the critical concentration was identified and the statistical analysis used to support the claim of a sharp transition.
    - **R1-m2**
        - **Severity** Minor
        - **Axis** Technical Soundness
        - **Affected element** ML analysis
        - **Evidence pointer** Materials and Methods, SI Appendix Fig. S4, S5.
        - **Issue** The ML model for classifying diffusion models was trained on simulated data. The accuracy of the model is reported as an F1-score. However, it is not clear how the model's performance on simulated data translates to its performance on experimental data, which may have different noise characteristics.
        - **Required correction** Please discuss the potential limitations of applying a model trained on simulated data to experimental data and, if possible, provide a validation of the model on a subset of experimentally curated trajectories.
    - **R1-m3**
        - **Severity** Minor
        - **Axis** Clarity
        - **Affected element** Model description
        - **Evidence pointer** Materials and Methods, Fig. 4.
        - **Issue** The description of the theoretical model is clear but could be enhanced by a more explicit statement of the assumptions. For example, it is assumed that all particles have the same size and that coalescence is instantaneous upon contact.
        - **Required correction** Please explicitly state the key assumptions of the model and briefly discuss their potential impact on the results.
- **Technical failings that need to be addressed before the case is established**
    - R1-M1: The evidence for the BMC mechanism is not quantitatively robust.
    - R1-M2: The link between the model's key parameter (Pu) and the experimental data is not established.
    - R1-M3: The assignment of the slow-diffusing population to DNA-bound PR is not directly validated.
- **Assessment against Nature-style criteria**
    - **Originality** High. The study presents a novel mechanism (particle unbinding) for controlling condensate size, which goes beyond the classical BMC model. The combination of techniques is also innovative.
    - **Scientific importance** High. Understanding the physical principles governing TF condensate formation and size is crucial for understanding gene regulation and nuclear organization. The findings have broad implications for the field of phase separation in biology.
    - **Interdisciplinary readership** High. The work bridges biophysics, cell biology, and computational modeling, making it of interest to a wide range of scientists.
    - **Technical soundness** Moderate. The experimental and theoretical approaches are sophisticated, but the current analysis does not fully support the central claims. The lack of a quantitative link between the model and experiment is a significant weakness.
    - **Readability for nonspecialists** Good. The manuscript is well-written and the logic is clear. The concepts are introduced in an accessible manner, although some parts of the methods may be challenging for a purely biological audience.
- **Recommendation posture** Supportive if technical concerns are resolved. The core idea is novel and interesting, but the evidence presented is not yet sufficient to fully establish the case. The authors need to provide a more rigorous quantitative analysis to link their model to the experimental data and to validate their key interpretations.

## Risk / unsupported claims
- The claim that the slow-diffusing population within condensates is DNA-bound is an interpretation that is not directly supported by the presented data.
- The claim that the model "fully recapitulate[s]" the experimental data is an overstatement, as the comparison appears to be qualitative rather than a rigorous quantitative fit.
- The claim that the system is in a "nonequilibrium" state is plausible but not explicitly demonstrated.
- The biological significance of the "pre-existing population of small condensates" in the absence of hormone is not discussed.