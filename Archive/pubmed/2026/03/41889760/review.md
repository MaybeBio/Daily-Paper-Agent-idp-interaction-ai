## Review setup
- **Input scope** Full manuscript text, including abstract, introduction, results, discussion, methods, and supplementary figure/table references
- **Assessment boundary** Scientific content, methodological rigor, validity of claims relative to presented evidence, and alignment with Nature-style criteria
- **Shared manuscript claim summary** The authors use all-atom explicit-solvent MD simulations to show that spermine modulates fibril-associated intrachain contact propensities in a residue-specific manner across three IDPs (Tau K18, α-synuclein, Aβ40), with divergent outcomes: inhibition of Tau aggregation, enhancement of α-synuclein aggregation-prone interactions, and mixed effects on Aβ40. ThT fluorescence assays for Tau constructs are presented as experimental validation.
- **Visible evidence base** Main text figures (referenced as Figure 1 through Figure 5, with subpanels), supplementary figures S1–S17, supplementary tables S1–S3, methods section, and prior literature citations
- **Missing materials affecting confidence** Actual figure images and numerical data values are not provided; supplementary figures and tables are referenced but not included; NMR chemical shift comparison data (Figure S2) is described but not shown; simulation parameter details (force field validation, convergence metrics beyond contact relaxation times) are partially described

## Reviewer

- **Overall assessment** This manuscript presents a systematic computational investigation of spermine interactions with three disease-associated IDPs, with a novel analytical framework linking monomeric conformational ensembles to fibril-derived contact maps. The central claim that spermine exerts sequence- and residue-specific effects that cannot be predicted from net charge alone is well-motivated and supported by the simulation data as described. The experimental ThT validation for Tau provides an important anchor, though its scope is limited to one of three systems. The work is technically sound in its use of established simulation protocols and analysis methods, and the conceptual advance regarding decoupling of phase separation from aggregation is significant. However, several concerns regarding the strength of the experimental validation, the generalizability of the conclusions, and the interpretation of simulation-derived metrics warrant attention before the case is fully established.
- **Who would be interested in the results, and why** Researchers in the fields of neurodegenerative disease mechanisms, IDP biophysics, polyamine biology, and computational chemistry would find this work relevant. The residue-level mechanistic insights into how a small molecule differentially modulates aggregation across three major disease proteins could inform therapeutic strategies targeting polyamine metabolism or IDP conformational regulation. The analytical framework connecting monomer simulations to fibril structures may also be of methodological interest to the simulation community.
- **Major strengths** The study addresses a clinically important and mechanistically underexplored question with a well-designed computational approach. The use of patient-derived fibril structures as reference states is a strength, as it grounds the analysis in disease-relevant conformations. The comparative design across three IDPs with different charge distributions allows for meaningful conclusions about sequence specificity. The experimental validation for Tau, while limited in scope, provides a direct test of a simulation-derived prediction. The discussion of how these findings relate to prior observations of spermine-enhanced α-synuclein aggregation and the decoupling of LLPS from aggregation is thoughtful and well-contextualized.
- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Experimental validation scope
- **Claim pointer** The manuscript states that "ThT fluorescence experiments demonstrate a clear correlation between fibril-like contacts in the monomeric state and the overall aggregation propensity of these IDPs" and that the combined simulation-experimental framework provides a mechanistic basis for spermine effects across all three proteins.
- **Evidence pointer** Section "Experimental Validation of Spermine-Mediated Inhibition of Tau Aggregation", Figure 3 (referenced), Figure S9
- **Concern** Experimental validation is provided only for Tau (K18 and full-length), not for α-synuclein or Aβ40. The claim of a general correlation between simulation-predicted contact changes and aggregation outcomes across all three systems is therefore not directly tested. For α-synuclein, the authors cite prior literature for spermine-enhanced aggregation, but no new experimental data are presented. For Aβ40, no experimental validation is provided at all.
- **Why it matters** The central thesis is that the simulation framework can predict aggregation outcomes from monomeric contact changes. Without experimental validation for at least two of the three systems, the generalizability of this framework remains unproven. The divergent predictions (inhibition for Tau, enhancement for α-synuclein, mixed for Aβ40) are the key novel findings, and validation for only one system weakens the overall case.
- **Resolution test** Provide ThT or other aggregation assays for α-synuclein and Aβ40 in the presence of spermine, or clearly reframe the claims to indicate that experimental validation is limited to Tau and that the other predictions are testable hypotheses.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** No
- **Axis** Simulation validation and force field sensitivity
- **Claim pointer** The manuscript claims that the simulation results provide a reliable basis for understanding spermine effects on IDP conformations, with the implicit assumption that the chosen force field and simulation conditions adequately capture the relevant physics.
- **Evidence pointer** Section "All-atom MD Simulation" in Methods; Figure S2 (NMR chemical shift comparison); Table S1
- **Concern** The validation of the simulation model against experimental data is described only qualitatively ("good qualitative agreement" for chemical shifts, Figure S2). No quantitative metrics (e.g., RMSD between calculated and experimental chemical shifts, correlation coefficients) are provided. The manuscript does not discuss whether the AMBER ff99SBws force field has been specifically benchmarked for these IDPs or for spermine interactions. Additionally, the use of a single force field without cross-validation (e.g., with a different force field or water model) leaves open the question of whether the observed effects are force-field-dependent.
- **Why it matters** IDP simulations are notoriously sensitive to force field choice, and the conclusions about residue-specific modulation depend on the reliability of the conformational ensembles. If the force field biases certain secondary structure propensities or interaction patterns, the reported contact changes could be artifacts.
- **Resolution test** Provide quantitative validation metrics for the chemical shift comparison, and either include a discussion of force field sensitivity with supporting citations or perform a subset of simulations with an alternative force field to confirm the qualitative trends.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Statistical significance and sampling adequacy
- **Claim pointer** The manuscript reports specific changes in contact probabilities and modulation coefficients (k i,j) that are interpreted as systematic effects of spermine.
- **Evidence pointer** Section "Residue-Specific Interaction Patterns Underlying Spm-Mediated Modulation"; Figures 4 and 5 (referenced); Figure S17 (contact relaxation times)
- **Concern** The manuscript does not report statistical uncertainties for the contact probability differences or modulation coefficients. While contact relaxation times are discussed to support sampling adequacy, no error bars, confidence intervals, or statistical tests are presented for the key quantitative claims. It is unclear whether the reported differences between conditions (e.g., with and without spermine) are statistically distinguishable given the inherent variability of IDP simulations.
- **Why it matters** The conclusions rest on quantitative comparisons of contact maps across conditions. Without uncertainty estimates, it is impossible to assess whether the observed differences are robust or within the noise of the simulations.
- **Resolution test** Provide error estimates (e.g., block averaging, bootstrapping across trajectory segments) for the contact probability differences and modulation coefficients, and indicate which differences are statistically significant.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Interpretation of modulation coefficients
- **Claim pointer** The manuscript uses the modulation coefficient k i,j, defined as the slope from linear regression of contact probabilities versus spermine ratios, to identify systematically enhanced or suppressed contacts.
- **Evidence pointer** Section "Protocol for Investigating Spermine-Mediated Modulation of Disease-Relevant Structures"; Figure 1F (referenced)
- **Concern** The linear regression approach assumes a monotonic relationship between spermine concentration and contact probability. However, the manuscript also reports non-monotonic behavior in R g for K18 (initial increase followed by return to baseline at higher concentrations). It is unclear whether contact probabilities also exhibit non-monotonic responses, which would invalidate the linear regression approach. Additionally, the number of spermine concentrations used for the regression is not stated in the visible text.
- **Why it matters** If the relationship is non-monotonic, the modulation coefficient could misrepresent the actual effect of spermine, potentially overstating or understating the impact on specific contacts.
- **Resolution test** Show the raw contact probability data as a function of spermine concentration for representative residue pairs, and justify the linear regression approach or use a more flexible model if non-monotonicity is present.

- **Concern ID** R1-M5
- **Severity** Major
- **Blocking** No
- **Axis** Relevance of monomeric simulations to fibril formation
- **Claim pointer** The manuscript claims that changes in monomeric intrachain contact propensities provide a mechanistic basis for understanding spermine effects on aggregation, with the implicit assumption that monomeric conformational biases directly influence fibril nucleation.
- **Evidence pointer** Section "Discussion"; Section "Residue-Specific Interaction Patterns Underlying Spm-Mediated Modulation"
- **Concern** The link between monomeric contact changes and aggregation outcomes is inferred rather than demonstrated. Fibril formation involves intermolecular interactions, oligomerization, and nucleation steps that may not be captured by monomeric simulations alone. The authors acknowledge that fibril formation is multimeric, but the framework's predictive power for aggregation outcomes rests on the assumption that monomeric biases are rate-limiting or determinative.
- **Why it matters** If the relationship between monomeric contacts and aggregation is indirect or system-dependent, the conclusions about spermine's pro- or anti-aggregation effects may not hold under conditions where intermolecular interactions dominate.
- **Resolution test** Discuss the mechanistic link more explicitly, citing literature that supports the connection between monomeric conformational biases and aggregation kinetics, or perform coarse-grained or oligomeric simulations to test whether the predicted effects persist in multimeric contexts.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity of figure references
- **Affected element** Results section
- **Evidence pointer** Section "Protocol for Investigating Spermine-Mediated Modulation of Disease-Relevant Structures"
- **Issue** Several figure references are incomplete in the text (e.g., "Figure  " with no number, "Figure  A" without specifying which figure). This makes it difficult to follow the results.
- **Required correction** Complete all figure references with the correct figure numbers.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Temperature consistency
- **Claim pointer** The manuscript states that simulations were run at temperatures consistent with NMR experiments (283 K for K18, 288 K for α-synuclein, 278 K for Aβ40), while ThT assays were performed at 37 °C.
- **Evidence pointer** Section "All-atom MD Simulation" in Methods; Section "ThT Kinetics" in Methods
- **Issue** The temperature mismatch between simulations and experiments is acknowledged but not discussed in terms of its potential impact on the comparison. Spermine-protein interactions and conformational preferences could be temperature-dependent.
- **Required correction** Add a brief discussion of whether the temperature difference could affect the qualitative agreement between simulations and experiments, and justify the choice of simulation temperatures.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Spermine concentration units
- **Affected element** Methods and Results
- **Evidence pointer** Table S1 (referenced); Section "Protocol for Investigating Spermine-Mediated Modulation of Disease-Relevant Structures"
- **Issue** The manuscript refers to "protein:Spermine ratios" but does not clearly state the absolute concentrations used in the simulations or experiments. This makes it difficult to assess physiological relevance.
- **Required correction** Provide absolute concentrations (e.g., µM spermine) alongside the ratios, and state the concentration range tested.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Statistical treatment of ThT data
- **Affected element** Section "Experimental Validation of Spermine-Mediated Inhibition of Tau Aggregation"
- **Evidence pointer** Figure 3 (referenced); Section "ThT Kinetics" in Methods
- **Issue** The ThT data are described as fitted to a sigmoidal function with bootstrapped uncertainties, but the number of replicates (stated as three) is low, and no statistical comparison between conditions (e.g., with and without spermine) is reported beyond qualitative descriptions.
- **Required correction** Report the statistical significance of differences between conditions, or clearly state that the results are descriptive given the limited replicates.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Discussion of prior work
- **Affected element** Introduction and Discussion
- **Evidence pointer** Section "Introduction"; Section "Discussion"
- **Issue** The manuscript cites prior work on spermine effects on α-synuclein and Aβ aggregation but does not critically compare the present findings with those studies in detail, particularly regarding any discrepancies in the direction or magnitude of effects.
- **Required correction** Add a more detailed comparison with prior experimental and computational studies on polyamine-IDP interactions, highlighting agreements and disagreements.

- **Technical failings that need to be addressed before the case is established** The lack of experimental validation for α-synuclein and Aβ40 predictions (R1-M1) is the most significant gap. Without this, the claim of a generalizable framework is not fully supported. Additionally, the absence of statistical uncertainties for the key simulation-derived metrics (R1-M3) undermines confidence in the quantitative claims. The potential non-monotonicity of contact probability responses to spermine (R1-M4) needs to be addressed to validate the modulation coefficient approach.

- **Assessment against Nature-style criteria**  
  *Originality*: The work is original in its systematic comparison of spermine effects across three IDPs using a consistent analytical framework, and in its attempt to link monomeric conformational changes to fibril-relevant contact propensities. The concept of decoupling phase separation from aggregation via residue-specific modulation is a novel contribution.  
  *Scientific importance*: The findings have potential importance for understanding how cellular metabolites influence IDP aggregation and for designing therapeutic strategies. However, the importance is somewhat tempered by the limited experimental validation and the reliance on simulation-derived metrics whose connection to aggregation outcomes is inferred rather than directly demonstrated.  
  *Interdisciplinary readership*: The work bridges computational biophysics, protein chemistry, and neurodegeneration research, and would appeal to readers across these fields. The conceptual framework is accessible, though the technical details of the simulation analysis may be challenging for non-specialists.  
  *Technical soundness*: The simulation protocols are generally sound, with appropriate force fields, long simulation times, and validation against NMR chemical shifts. However, the lack of statistical rigor in reporting uncertainties and the limited experimental validation are notable weaknesses.  
  *Readability for nonspecialists*: The manuscript is generally well-written and the logic is clear. The figures, as described, appear to support the narrative, though the incomplete figure references in the text hinder readability. The discussion effectively contextualizes the findings for a broad audience.

- **Recommendation posture** Supportive if technical concerns are resolved. The core computational framework and the divergent predictions for the three IDPs are interesting and potentially significant. However, the manuscript currently does not fully establish the case due to the limited experimental validation (only Tau), the absence of statistical uncertainties for key simulation metrics, and the unaddressed question of whether the linear modulation coefficient adequately captures the spermine-concentration dependence. Addressing these concerns would substantially strengthen the manuscript.

## Risk / unsupported claims
- The claim that the combined simulation-experimental framework provides a mechanistic basis for how spermine modulates aggregation across all three IDPs is not fully supported, as experimental validation is provided only for Tau.
- The claim of a "clear correlation between fibril-like contacts in the monomeric state and the overall aggregation propensity" is not quantitatively demonstrated; no correlation coefficient or statistical test is reported.
- The assertion that spermine binding near residue 46 in α-synuclein promotes aggregation through a mechanism akin to the E46K mutation is speculative and not directly tested.
- The statement that the qualitative trend of spermine-mediated disruption of fibril-like contacts is "preserved across structurally diverse Tau polymorphs" is based on analysis described in the text but the supporting data (Figure S7) is not visible for verification.
- The relevance of the simulation temperatures (283 K, 288 K, 278 K) to the physiological conditions where aggregation occurs (37 °C) is not discussed, leaving the physiological relevance of the findings partially unaddressed.