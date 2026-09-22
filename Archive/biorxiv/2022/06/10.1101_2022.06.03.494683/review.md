## Review setup
- **Input scope** Full manuscript text (summary, introduction, results, discussion, limitations, author information)
- **Assessment boundary** Scientific claims, methodological soundness, evidence quality, and generalizability of the INSRTR platform as presented in the provided text
- **Shared manuscript claim summary** The authors propose a generalizable allosteric regulation platform (INSRTR) based on inserting a short unstructured peptide into solvent-exposed loops of diverse proteins. Binding of a complementary coiled-coil peptide induces a rigid dimer, disrupting local conformation and modulating protein function. The platform is claimed to enable ON/OFF switches, small-molecule regulation, and Boolean logic in mammalian cells, demonstrated across ten diverse proteins.
- **Visible evidence base** Results sections describing principle, ON switch variants, Boolean logic gates, and application to ten proteins; figures referenced but not provided; supplementary figures referenced but not provided
- **Missing materials affecting confidence** All figures, supplementary figures, experimental protocols, quantitative data, statistical analyses, and structural or biophysical validation data are not provided. This severely limits independent verification of the claims.

## Reviewer
- **Overall assessment** The manuscript presents a conceptually appealing and potentially generalizable strategy for allosteric regulation of proteins. The breadth of demonstrated targets (ten proteins) is impressive and suggests practical utility. However, the provided text lacks the experimental detail, quantitative data, and figure evidence necessary to rigorously evaluate the claims. The mechanistic model is plausible but not directly validated. The work is likely of interest to the synthetic biology and protein engineering communities, but the current evidence base is insufficient to fully establish the platform's generality and mechanism.
- **Who would be interested in the results, and why** Researchers in synthetic biology, protein engineering, cell signaling, and therapeutic protein design would be interested. The potential to regulate diverse proteins with a simple, modular insertion strategy could enable new tools for controlling cellular processes, building genetic circuits, and developing safer cell therapies (e.g., regulatable CAR T cells).
- **Major strengths** 1) The concept is simple, modular, and potentially generalizable, addressing a known limitation in protein regulation. 2) Demonstration across ten diverse proteins spanning enzymes, signaling mediators, DNA binders, fluorescent proteins, and antibodies is a significant breadth. 3) The inclusion of ON/OFF switches, small-molecule regulation, and Boolean logic extends the platform's utility. 4) The use of designed orthogonal coiled-coil pairs offers tunability and specificity.
- **Major Concerns** [R1-M1, R1-M2, R1-M3, R1-M4, R1-M5]
- **Minor Comments** [R1-m1, R1-m2, R1-m3, R1-m4]
- **Technical failings that need to be addressed before the case is established** R1-M1 (mechanism unvalidated), R1-M2 (quantitative data missing), R1-M3 (generality overclaimed), R1-M4 (logic gate validation incomplete), R1-M5 (specificity and off-target effects unaddressed)
- **Assessment against Nature-style criteria** Originality: High. The INSRTR concept is a novel and potentially transformative approach to protein regulation. Scientific importance: High if the claims are fully substantiated, as it could provide a general tool for controlling protein function. Interdisciplinary readership: Broad, spanning synthetic biology, cell biology, immunology, and bioengineering. Technical soundness: Currently not fully assessable due to missing data and figures. The rationale is sound, but the mechanistic evidence is indirect. Readability for nonspecialists: The text is generally clear, but the lack of figures and detailed methods makes it difficult for nonspecialists to follow the experimental logic.
- **Recommendation posture** Supportive if technical concerns are resolved. The core concept is promising and the breadth of targets is compelling, but the current evidence base is insufficient to fully establish the claims. Substantial additional data, including quantitative results, mechanistic validation, and full figures, are required.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Mechanistic validation
- **Claim pointer** The authors claim that coiled-coil formation within the inserted loop disrupts local conformation and inhibits protein function via allosteric coupling.
- **Evidence pointer** Results section "The principle of inserted peptide structure allosteric regulation (INSRTR)", Figure 1B-C; molecular dynamics simulation mentioned but not shown
- **Concern** The proposed mechanism is supported only by indirect functional assays and an unshown molecular dynamics simulation. No direct structural or biophysical evidence (e.g., X-ray crystallography, NMR, cryo-EM, or hydrogen-deuterium exchange) is provided to demonstrate that coiled-coil formation induces the predicted conformational change in the host protein. The claim that inhibition results from "subtle perturbation" rather than steric hindrance is speculative without such data.
- **Why it matters** The generalizability of INSRTR depends on a reliable and predictable mechanism. If the effect is instead due to nonspecific steric clashes or misfolding, the platform's utility would be severely limited. Direct mechanistic validation is essential to support the proposed design principles and to guide future applications.
- **Resolution test** Provide structural or biophysical data (e.g., crystal structure of a regulated protein with and without the peptide, or HDX-MS showing conformational changes) that directly demonstrates the allosteric mechanism. Alternatively, provide a series of control experiments with peptides of varying length, rigidity, and binding affinity that systematically support the proposed model.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Quantitative evidence
- **Claim pointer** The authors claim up to 30-fold repression of luciferase activity and up to 90% inhibition for other enzymes.
- **Evidence pointer** Results sections "The principle of inserted peptide structure allosteric regulation (INSRTR)" and "INSRTR regulation of diverse protein types and functions in an OFF or ON format", Figures 1C, 5A-E
- **Concern** The text reports key quantitative outcomes (e.g., fold repression, percent inhibition) but provides no raw data, error bars, replicates, or statistical analysis. It is unclear how many independent experiments were performed, what the variability is, and whether the reported values are representative or best-case. The claim of "perfect success" on ten proteins is not supported by any quantitative threshold or criteria for success.
- **Why it matters** Quantitative rigor is essential for evaluating the robustness and reproducibility of the platform. Without statistical analysis, it is impossible to assess whether the observed effects are significant and reliable, or whether they vary substantially between proteins and conditions.
- **Resolution test** Provide full dose-response curves, time courses, and replicate data for all key experiments. Include statistical tests (e.g., t-tests, ANOVA) and clearly define success criteria for "functional" and "regulated" variants. Present data as mean ± SD or SEM with individual data points.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Generalizability
- **Claim pointer** The authors claim the INSRTR platform is "generally applicable" and demonstrate it on ten diverse proteins.
- **Evidence pointer** Results section "INSRTR regulation of diverse protein types and functions in an OFF or ON format", Figures 5A-L, S2-S5
- **Concern** While ten proteins is a substantial number, the selection criteria for these proteins and the insertion sites are not described in sufficient detail. It is unclear whether these proteins were chosen randomly or because they were predicted to be amenable. The text states that "at least one—but often up to three—sites were found to be amenable," but the success rate per protein and per site is not quantified. The claim of "perfect success" is therefore difficult to evaluate. The platform's true generalizability cannot be assessed without a larger, more systematic screen or a clear rationale for protein selection.
- **Why it matters** The central claim of the manuscript is that INSRTR is a general platform. If the demonstrated proteins are not representative or if the success rate is low, the claim of general applicability would be overstated.
- **Resolution test** Provide a systematic analysis of insertion site success rates across all tested proteins, including negative results. Describe the criteria for selecting proteins and sites. Ideally, include a larger panel of proteins with diverse folds and functions to demonstrate broad applicability.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** Yes
- **Axis** Logic gate validation
- **Claim pointer** The authors claim construction of a full set of Boolean logic functions based on INSRTR and proteases.
- **Evidence pointer** Results section "Construction of Boolean protein logic gates based on intramolecular interacting segments", Figure 4A-D, Figure S1
- **Concern** The description of the Boolean logic gates is brief and lacks critical details. The truth tables for all logic functions are not shown, and the response dynamics (e.g., speed, amplitude, leakiness) are not quantified. It is unclear how the logic gates perform in terms of signal-to-noise ratio, crosstalk between inputs, and scalability. The claim of "all combinations of two signal inputs" needs to be explicitly demonstrated with data for each gate.
- **Why it matters** Boolean logic is a key extension of the platform and a major selling point. Without rigorous validation, the utility of INSRTR for complex circuit design is not established.
- **Resolution test** Provide complete truth tables and representative time-course data for all logic gates. Quantify gate performance (e.g., ON/OFF ratios, response times, leakiness) and demonstrate orthogonality of the protease inputs.

- **Concern ID** R1-M5
- **Severity** Major
- **Blocking** No
- **Axis** Specificity and off-target effects
- **Claim pointer** The authors claim that designed coiled-coil pairs are orthogonal to endogenous coiled-coils and that regulation is specific.
- **Evidence pointer** Results section "The principle of inserted peptide structure allosteric regulation (INSRTR)", Figure 1D; Discussion
- **Concern** The text states that the coiled-coil pairs are orthogonal to endogenous ones, but no data are shown to support this claim in the context of the full proteome. Potential off-target effects of the regulatory peptides on other cellular proteins are not addressed. Additionally, the specificity of the allosteric effect (i.e., that only the target protein is affected) is not demonstrated.
- **Why it matters** Off-target effects could compromise the interpretation of functional assays and limit the platform's use in complex biological systems. Demonstrating specificity is crucial for claiming a clean, generalizable tool.
- **Resolution test** Provide data showing that regulatory peptides do not affect the activity of unrelated proteins or cellular viability. Use proteomics or transcriptomics to assess global changes upon peptide expression. Include control experiments with scrambled or mutant peptides.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Figure 1B
- **Evidence pointer** Results section "The principle of inserted peptide structure allosteric regulation (INSRTR)"
- **Issue** The description of the molecular dynamics simulation is vague and the figure is not shown. It is unclear what the simulation adds to the argument.
- **Required correction** Either show the simulation results or remove the reference to it. If shown, provide details on the simulation parameters and what was measured.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Reproducibility
- **Affected element** Methods
- **Evidence pointer** Entire manuscript
- **Issue** No methods section is provided in the text. Key experimental details (e.g., cell lines, transfection protocols, assay conditions, peptide sequences, plasmid construction) are missing.
- **Required correction** Provide a full methods section or a detailed supplementary methods file.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Terminology
- **Affected element** "Perfect success"
- **Evidence pointer** Discussion
- **Issue** The phrase "perfect success" is subjective and not quantitatively defined.
- **Required correction** Replace with a quantitative statement, e.g., "successfully regulated 10 out of 10 tested proteins, with X% showing >Y-fold regulation."

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Limitations section
- **Evidence pointer** Limitations of the study
- **Issue** The limitations section is brief and does not address potential issues with the platform, such as the requirement for a known 3D structure, the potential for insertion to disrupt protein folding, or the long-term stability of the regulated state.
- **Required correction** Expand the limitations section to include these considerations.

## Risk / unsupported claims
- The claim of a "generally applicable" platform is not fully supported without a larger, more systematic screen and quantitative success rates.
- The proposed allosteric mechanism is not directly validated by structural or biophysical data.
- The claim of "perfect success" on ten proteins is not quantitatively defined.
- The orthogonality of the coiled-coil pairs to endogenous proteins is stated but not demonstrated with data.
- The Boolean logic gate performance is not quantitatively characterized.
- The rapid response time (5 minutes) is reported for one experiment but not systematically characterized.
- The potential for off-target effects of the regulatory peptides is not addressed.