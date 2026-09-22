## Review setup
- **Input scope** Full manuscript text, including abstract, introduction, results, discussion, methods, and supplementary information descriptions
- **Assessment boundary** Scientific content, experimental design, data interpretation, computational modeling approach, and claims as presented in the manuscript
- **Shared manuscript claim summary** The authors investigate liquid-liquid phase separation (LLPS) in mixtures of tau and TDP-43 low complexity domain (LCD), demonstrating that scaffold-client roles are concentration-dependent, can be modulated by selectively inhibiting specific intermolecular interactions, and that a tau "halo" forms around TDP-43 LCD droplets due to amphiphilic organization at condensate interfaces, as supported by coarse-grained simulations
- **Visible evidence base** Turbidimetry measurements, fluorescence microscopy images, FRAP data, coarse-grained simulation results, and Flory-Huggins theoretical framework
- **Missing materials affecting confidence** Supplementary figures (Fig. S1-S6), Supplementary Table S1, Supplementary Methods, and Supplementary Data files were not provided for review

## Reviewer
- **Overall assessment** This manuscript addresses an important and timely question in the field of biomolecular condensates: how multicomponent protein systems behave with respect to scaffold-client relationships and structural organization. The tau/TDP-43 system is biologically relevant given the co-occurrence of these proteins in neurodegenerative pathologies. The authors present a clear conceptual framework, supported by both experimental and computational approaches, demonstrating that scaffold-client roles are governed by concentration relative to Csat and can be modulated by selective inhibition of interaction types. The observation of a tau "halo" around TDP-43 LCD droplets is striking and potentially novel. However, several technical concerns regarding quantification rigor, simulation validation, and mechanistic interpretation need to be addressed before the conclusions can be fully established.

- **Who would be interested in the results, and why** Researchers studying biomolecular condensates and liquid-liquid phase separation, particularly those interested in multicomponent systems, scaffold-client relationships, and the molecular determinants of condensate architecture. The work is also relevant to the neurodegeneration community, given the involvement of tau and TDP-43 in Alzheimer's disease and related disorders. The findings on how interaction types (electrostatic vs. hydrophobic) can be selectively modulated to control phase behavior may inform therapeutic strategies targeting aberrant condensation.

- **Major strengths** The study addresses a significant gap in the LLPS field, which has largely focused on single-component systems. The combination of experimental and computational approaches is commendable. The use of selective inhibitors (salt for electrostatic, 1,6-hexanediol for hydrophobic interactions) to dissect interaction contributions is elegant. The identification of a tau halo around TDP-43 LCD droplets and the proposed amphiphilic mechanism is novel and provides a testable model for condensate surface organization. The Flory-Huggins framework provides a useful conceptual interpretation of the observed behavior.

- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness of simulation validation
- **Claim pointer** The coarse-grained simulation framework "successfully recapitulated the experimentally observed enrichment of tau at the surface of TDP-43 LCD droplets" and was used to derive molecular-level insights into interaction mechanisms
- **Evidence pointer** Results section "Coarse-grained simulations model for LLPS of the tau/TDP-43 LCD system"; Figure 7; Supplementary Methods (not provided)
- **Concern** The simulation model is calibrated using two empirical scaling parameters (α and β) that are tuned to match experimental Csat values for individual proteins. However, the manuscript does not provide sufficient detail on how sensitive the simulation outcomes are to these parameters. More critically, the validation of the simulation against experimental data appears limited to qualitative comparisons. The manuscript states that simulations "recapitulated at the qualitative level the key features" but does not provide quantitative metrics for how well the simulated density profiles, halo thickness, or interaction energies match experimental measurements. The claim that simulations reveal "tau's amphiphilic organization at condensate interfaces" requires more rigorous validation that the model faithfully represents the physical system.
- **Why it matters** The molecular-level mechanistic conclusions, particularly regarding the orientation of tau at the interface and the specific interactions driving halo formation, rest on the fidelity of the simulation model. If the model is not adequately validated, the mechanistic interpretations may be artifacts of the coarse-graining approach or parameter choices rather than genuine physical properties of the system.
- **Resolution test** Provide quantitative comparison between simulated and experimental observables (e.g., density profiles, partition coefficients, halo dimensions). Demonstrate robustness of conclusions to variation in scaling parameters α and β. Show that the simulation reproduces additional independent experimental observations beyond those used for calibration.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Quantification and statistical rigor of experimental data
- **Claim pointer** The manuscript states that "tau was especially highly concentrated at the surface of TDP-43 LCD droplets" and that partition coefficients decreased from ~11 at 150 mM to ~3 at 600 mM NaCl
- **Evidence pointer** Results section "Evaluating interactions responsible for reciprocal recruitment"; Figures 5, 6; location not provided
- **Concern** The quantitative claims regarding tau enrichment at droplet surfaces and partition coefficients are based on fluorescence intensity measurements, but the manuscript does not describe how these intensities were calibrated or whether they are proportional to absolute protein concentrations. Fluorescence intensity can be affected by local environment, quenching, and differential labeling efficiency. The partition coefficient measurements appear to be based on a limited number of replicates (n=11 is mentioned for one experiment), but no statistical analysis is presented. The claim that "all 65 condensates displayed TDP-43 LCD intensities markedly above those of the surrounding dilute phase" is presented without statistical testing or error analysis.
- **Why it matters** The central conclusions about scaffold-client behavior and the modulation of this behavior by salt and hexanediol depend on reliable quantification of protein distribution within and between condensate phases. Without proper calibration and statistical analysis, the quantitative claims cannot be evaluated, and the conclusions may not be robust.
- **Resolution test** Provide calibration curves for fluorescence intensity versus protein concentration. Include statistical analysis (e.g., confidence intervals, hypothesis testing) for partition coefficients and enrichment measurements. Describe how many independent experiments and images were analyzed for each condition.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Mechanistic interpretation of halo formation
- **Claim pointer** The manuscript proposes that the tau halo forms due to "tau's amphiphilic organization at condensate interfaces" and that this is driven by a combination of electrostatic and hydrophobic interactions between tau's N-terminal region and TDP-43 LCD
- **Evidence pointer** Results section "Insight from simulations into intermolecular interactions"; Figure 7; Discussion
- **Concern** The mechanistic model proposes that tau's negatively charged N-terminal region interacts with the positively charged N-terminal domain of TDP-43 LCD, while the rest of tau extends into the surrounding phase. However, the manuscript does not adequately address alternative explanations for halo formation, such as excluded volume effects, differential diffusion rates, or depletion interactions. The persistence of the halo at high salt concentrations (600 mM NaCl) is interpreted as evidence for hydrophobic contributions, but the manuscript does not quantify the relative contributions of electrostatic vs. hydrophobic interactions or demonstrate that the halo is not simply a kinetic trapping artifact.
- **Why it matters** The proposed amphiphilic mechanism is a key conceptual contribution of the paper. If alternative mechanisms are not ruled out, the interpretation may be premature. Understanding the physical basis of halo formation is important for predicting how such structures might behave in cellular contexts and for designing experiments to test the model.
- **Resolution test** Perform additional experiments or simulations that distinguish between the proposed amphiphilic mechanism and alternative explanations. For example, test whether a tau construct lacking the N-terminal region still forms a halo, or whether the halo forms under conditions where amphiphilic assembly is disrupted.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Generalizability of findings
- **Claim pointer** The authors state that "information about LLPS behavior of individual proteins may provide a foundation for understanding, and potentially predicting, the scaffold-client behavior of complex multicomponent systems"
- **Evidence pointer** Discussion; location not provided
- **Concern** The study is limited to a single pair of proteins (tau and TDP-43 LCD) under a narrow set of conditions (10% PEG, specific buffer, pH 7.4). The claim that individual protein LLPS behavior can predict multicomponent behavior is presented as a general principle but is only demonstrated for this one system. The manuscript does not discuss how sequence complexity, molecular weight, or other factors might affect the applicability of this principle to other protein pairs.
- **Why it matters** The broader significance of the work depends on whether the observed principles are generalizable. If the findings are system-specific, the impact on the field is more limited. The claim of predictability has practical implications for designing experiments and interpreting cellular phenomena.
- **Resolution test** Acknowledge the limitations of generalizing from a single system, or provide additional data (even preliminary) on a second protein pair to support the generalizability claim. Alternatively, temper the claim to reflect the specific system studied.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity of presentation
- **Affected element** Figure 2e
- **Evidence pointer** Results section "Surface tension differences"; Figure 2e
- **Issue** The interfacial angle measurements are presented as boxplots, but the number of droplets measured and the statistical significance of the difference between tau and TDP-43 LCD angles are not stated in the main text.
- **Required correction** Add the number of measurements and statistical analysis to the figure legend or main text.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Completeness of methods
- **Affected element** FRAP methodology
- **Evidence pointer** Methods section "FRAP experiments"
- **Issue** The FRAP analysis is described briefly, and the manuscript does not specify the mobile fraction calculations, the fitting model used, or how the recovery half-times were determined.
- **Required correction** Provide additional details on FRAP data analysis, including the fitting equation and any corrections applied.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Terminology consistency
- **Affected element** Use of "scaffold" and "client"
- **Evidence pointer** Throughout the manuscript
- **Issue** The terms "scaffold" and "client" are used throughout, but the manuscript does not explicitly define these terms in the context of this work, and the usage may differ from other definitions in the LLPS literature.
- **Required correction** Provide a brief definition of "scaffold" and "client" as used in this study, and clarify how this usage relates to or differs from previous definitions.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Figure quality
- **Affected element** Figure 7a
- **Evidence pointer** Results section "Insight from simulations"; Figure 7a
- **Issue** The pairwise interaction plot in Figure 7a is described as showing interaction strengths, but the color scale and the specific residues involved are difficult to discern from the description provided.
- **Required correction** Ensure the figure is legible and provide a clear description of the color scale and how to interpret the plot in the figure legend.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Discussion of limitations
- **Affected element** Discussion section
- **Evidence pointer** Discussion; location not provided
- **Issue** The discussion does not address potential limitations of the study, such as the use of PEG as a crowding agent, the relevance of in vitro conditions to cellular environments, or the potential effects of post-translational modifications on the observed behavior.
- **Required correction** Add a paragraph acknowledging the limitations of the study and discussing how they might affect the interpretation and generalizability of the findings.

## Risk / unsupported claims
- The claim that the coarse-grained simulation framework "reveals" the molecular mechanism of tau halo formation is not fully supported, as the simulation validation is only qualitative and the sensitivity to model parameters is not assessed
- The quantitative values for partition coefficients (e.g., ~11 at 150 mM NaCl) are presented without calibration details or statistical analysis, making them difficult to evaluate
- The claim that "information about LLPS behavior of individual proteins may provide a foundation for understanding, and potentially predicting, the scaffold-client behavior of complex multicomponent systems" is presented as a general principle but is only demonstrated for a single protein pair
- The statement that "every tau droplet contained detectable TDP-43 LCD" is based on a thresholding method that is described in the Methods but the robustness of this classification is not assessed
- The interpretation that the persistence of the tau halo at high salt concentrations indicates hydrophobic contributions is plausible but not directly tested experimentally
- The relevance of the in vitro findings to cellular contexts, where other factors such as RNA, post-translational modifications, and molecular crowding by diverse macromolecules are present, is not discussed