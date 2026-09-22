## Review setup
- **Input scope** Full manuscript text (abstract, introduction, methods, results, discussion) without supplementary material
- **Assessment boundary** Scientific claims, methodology, evidence quality, and internal consistency based solely on the provided text
- **Shared manuscript claim summary** The authors present a coarse-grained molecular dynamics framework to test whether coiled-coil (CC) domains alone can drive liquid-liquid phase separation (LLPS) of proteins. They report that CC domains are sufficient to drive LLPS in their model, that increasing the number of CC domains per protein modestly increases LLPS propensity, and that increasing the multimerization state of CC domains (from dimer- to trimer- to tetramer-forming) dramatically increases LLPS propensity and reduces protein diffusion within droplets.
- **Visible evidence base** Main text figures referenced (Figs. 1–6), supplementary figures referenced (Figs. S2, S4, S5, S7, S8), supplementary tables referenced (Tables S3, S4), and methodological descriptions in the main text
- **Missing materials affecting confidence** Supplementary Material sections S.I, S.II, S.V, S.VI, S.VII, S.VIII are referenced but not provided; all figures and tables are referenced but not visible; no quantitative data (e.g., binodal coordinates, diffusion coefficient values) are given in the text

## Reviewer
- **Overall assessment** The manuscript addresses a timely and interesting question: whether coiled-coil domains, as folded multimerizing stickers, can be sufficient drivers of protein LLPS. The authors have developed a bespoke coarse-grained framework and applied it systematically across polymer valency, multimer valency, and temperature. The central claim, that CC domains are sufficient to drive LLPS in molecular models, is plausible and potentially valuable. However, the evidence as presented in the text alone is insufficient to fully evaluate the strength of this claim. Key quantitative results (binodal coordinates, diffusion coefficients, phase boundaries) are only available in figures and tables that were not provided. The validation of the framework against atomistic simulations and experimental Rg data is described but the actual comparisons are not shown. The moderate specificity of multimer formation, acknowledged by the authors, complicates interpretation of the multimerization effects. The manuscript would benefit from clearer presentation of quantitative results and a more critical discussion of model limitations.

- **Who would be interested in the results, and why** Researchers studying phase separation mechanisms, particularly those focused on the biophysics of membraneless organelle formation; computational biologists developing coarse-grained models for LLPS; experimentalists studying centrosome and central spindle assembly who seek mechanistic hypotheses for how CC proteins such as spd-5, pericentrin, and PRC1 drive condensation. The framework itself may be of interest to method developers in the molecular simulation community.

- **Major strengths**
  1. The question is well-motivated and timely, addressing a gap in understanding whether folded CC domains can act as autonomous drivers of LLPS.
  2. The framework is designed with clear physical principles and simplifying assumptions that are explicitly stated.
  3. The systematic variation of both polymeric and multimeric multivalency allows separation of these two contributions.
  4. The authors validate their CC dimer model against atomistic simulations and parameterize linkers against experimental Rg data, showing attention to model fidelity.
  5. The discussion connects simulation findings to experimental observations in a measured way, acknowledging limitations.

- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence completeness
- **Claim pointer** The authors claim that "small model proteins with as few as two CC domains can phase separate" and that "trimer-forming and tetramer-forming CC domains have a dramatically higher LLPS propensity than dimer-forming coils."
- **Evidence pointer** Figures 2, 3, 5, S5, S8; Tables S3, S4; location not provided for quantitative values
- **Concern** The central quantitative claims are supported only by figures and tables that are not included in the provided material. No numerical values for binodal coordinates, phase boundaries, or diffusion coefficients are given in the text. The reader cannot assess the magnitude of the reported effects, the statistical significance of differences between conditions, or the quality of the phase coexistence data. For example, the claim that trimer- and tetramer-forming coils have "dramatically higher" LLPS propensity than dimers requires quantitative comparison of binodals or critical temperatures, which are not presented in the text.
- **Why it matters** Without access to the actual data, the strength of the central claims cannot be evaluated. The difference between "dramatic" and "modest" effects is a quantitative judgment that requires the underlying numbers.
- **Resolution test** Provide the key quantitative results in the text or ensure the figures and tables are available for review. Report numerical values for binodal endpoints, apparent melting temperatures, and diffusion coefficients with uncertainties.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Model validation
- **Claim pointer** The authors state that the framework was validated by comparing simulated CC dimer structure to atomistic simulations and by comparing simulated Rg of 23 IDPs to experimental values.
- **Evidence pointer** Methods sections "Temperature replica exchange MD to assess dynamics of coarse-grained CC dimer" and "Single molecule MD of intrinsically disordered proteins to parameterize linker segments"; Figures S2, S3; Table S3
- **Concern** The validation results are described but not shown. The KL divergence values in Table S3 are referenced but not provided. The parity plot in Figure S3 is referenced but not visible. The authors state that 5.5 kJ/mol was chosen as the optimal interaction strength based on lowest KL divergence, but the reader cannot see how close the agreement is or whether the choice is well-justified. Similarly, the Rg comparison for 23 IDPs is described as having a Pearson correlation of 0.753, but the scatter of the data and the magnitude of deviations are not assessable.
- **Why it matters** The validity of the entire framework rests on these validation steps. If the model does not faithfully reproduce known CC dimer behavior or IDP dimensions, the subsequent LLPS results are compromised.
- **Resolution test** Show the validation data explicitly, including the KL divergence values, the Rg parity plot with error bars, and a discussion of what level of agreement is considered acceptable.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Interpretation of multimerization effects
- **Claim pointer** The authors claim that "multimerization state has a greater effect on LLPS than the number of CC domains per protein" and that increasing multimer state "dramatically" increases LLPS propensity.
- **Evidence pointer** Figures 4, 5, S8; Methods section "Slab simulations for phase coexistence"
- **Concern** The authors acknowledge that their trimer- and tetramer-forming models have only "moderate control over specific multimer formation," with simulations producing mixtures of multimer species. This means the reported effects of multimerization state are confounded by the actual distribution of multimer species present. A model designed to form tetramers that actually forms mostly trimers and dimers does not cleanly test the effect of tetramerization. The authors state that trends remain valid, but this assertion needs more support.
- **Why it matters** The central mechanistic conclusion, that higher-order multimerization dramatically enhances LLPS, depends on the ability to attribute observed differences to the intended multimer state. If the species distributions overlap substantially between conditions, the interpretation is weakened.
- **Resolution test** Report the actual multimer species distributions for each model at each temperature. Show that the intended multimer state is the dominant species, or perform additional analyses that account for the mixed populations.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Generalizability of conclusions
- **Claim pointer** The authors conclude that "CC domains are sufficient to drive LLPS of proteins" and suggest implications for identifying LLPS-driving regions in centrosomal and central spindle proteins.
- **Evidence pointer** Discussion section; Results section "Dimer-forming coil segments can drive LLPS of CC proteins"
- **Concern** The model uses idealized CC domains with uniform interaction strengths and no sequence specificity. Real CC domains vary in length, stability, orientation (parallel vs. antiparallel), and interaction specificity. The authors acknowledge some of these limitations but do not discuss how they might affect the conclusions. The leap from idealized model systems to biological proteins such as spc-5 and pericentrin requires more careful consideration of whether the model captures the relevant physics.
- **Why it matters** The broader significance of the work depends on its relevance to real biological systems. If the model omits features that are critical for CC-driven LLPS in cells, the conclusions may not transfer.
- **Resolution test** Discuss explicitly which features of real CC domains are captured and which are omitted, and argue why the omitted features are unlikely to change the qualitative conclusions. Consider additional simulations with varied interaction strengths or CC lengths to test robustness.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Introduction, paragraph 2
- **Evidence pointer** "Here we use LLPS broadly to describe condensates of varying visocoelastic characteristics."
- **Issue** The term "visocoelastic" appears to be a typo for "viscoelastic."
- **Required correction** Correct the spelling to "viscoelastic."

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Reproducibility
- **Affected element** Methods, "Common molecular dynamics parameters"
- **Evidence pointer** "Random seeds for each simulation were generated pseudo-randomly by GROMACS."
- **Issue** For reproducibility, the specific method of seed generation should be described, and seeds should be reported or made available.
- **Required correction** Specify how seeds were generated and provide the seeds or a reproducible seed generation protocol.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Statistical reporting
- **Affected element** Results, "Dimer-forming coil segments can drive LLPS of CC proteins"
- **Evidence pointer** "All three CC proteins formed LLPS at 253 K" and related statements throughout Results
- **Issue** The text reports qualitative observations (LLPS present or absent) without quantitative thresholds or uncertainty estimates. It is unclear how LLPS was definitively determined from density profiles and cluster analysis.
- **Required correction** Provide the specific criteria used to classify a system as phase-separated, and report uncertainties or replicate variability.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Methods, "Coarse-grained framework to study coiled-coil driven LLPS"
- **Evidence pointer** "Additional information about the framework's structural features and interaction parameters... are provided in Supporting Material, sections S.I and S.II respectively."
- **Issue** The main text does not provide sufficient detail to understand the model without the supplementary material. Key parameters (e.g., bead types, interaction strengths, bond potentials) are only in the supplement.
- **Required correction** Summarize the most critical model parameters in the main text or ensure the supplementary material is available to reviewers.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Terminology
- **Affected element** Throughout
- **Evidence pointer** "coil segments," "linker segments," "multimerization state"
- **Issue** The terminology is clear but could benefit from a brief definition early in the manuscript for readers unfamiliar with the coiled-coil literature.
- **Required correction** Add a sentence in the Introduction defining these terms as used in the paper.

- **Technical failings that need to be addressed before the case is established**
  - R1-M1: Quantitative evidence for central claims is not accessible in the provided text
  - R1-M2: Validation data are referenced but not shown
  - R1-M3: Multimer species distributions are not reported, confounding interpretation of multimerization effects

- **Assessment against Nature-style criteria**
  - **Originality**: The question of whether CC domains alone can drive LLPS is relatively underexplored compared to IDP-driven LLPS. The framework is novel in its specific design for CC proteins. However, the conceptual framework (stickers-and-spacers) is well-established, and the finding that multivalency drives LLPS is not surprising. The originality lies in the specific application to CC domains and the systematic comparison of multimerization states.
  - **Scientific importance**: If the conclusions hold, the work would provide a useful mechanistic hypothesis for how CC-rich proteins in centrosomes and the central spindle undergo LLPS. This could inform experimental studies. However, the idealized nature of the model limits direct biological inference. The importance is moderate and depends on the strength of the evidence.
  - **Interdisciplinary readership**: The work bridges biophysics, computational biology, and cell biology. It would appeal to researchers in phase separation and cytoskeletal biology. The writing is accessible to a broad scientific audience, though some familiarity with polymer physics and coarse-grained simulation is assumed.
  - **Technical soundness**: The methodology is reasonable and follows established practices in coarse-grained simulation. The validation approach is appropriate in principle. However, the lack of visible quantitative data and the acknowledged moderate specificity of multimer formation are concerns that need to be addressed.
  - **Readability for nonspecialists**: The manuscript is generally well-written and the logic is clear. The use of figures to convey results is appropriate. However, the heavy reliance on supplementary material for key details reduces accessibility.

- **Recommendation posture** Supportive if technical concerns are resolved. The central question is interesting and the framework is potentially valuable. However, the evidence as presented in the text alone is insufficient to fully establish the claims. The authors must provide the quantitative data underlying their conclusions, show the validation results, and address the multimer specificity issue. If these concerns are resolved, the work could make a meaningful contribution to the phase separation field.