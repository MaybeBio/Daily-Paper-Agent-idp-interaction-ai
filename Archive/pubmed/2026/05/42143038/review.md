## Review setup
- **Input scope** Full manuscript text including abstract, introduction, results, discussion, methods, and supplementary figure/table references
- **Assessment boundary** Scientific validity, technical soundness, reproducibility, and claims as supported by the provided evidence
- **Shared manuscript claim summary** The authors present a computational pipeline combining coarse-grained simulations, machine learning, and mixed-integer linear programming to design 30-residue peptides that preferentially localize at the interface of biomolecular condensates. They validate the approach experimentally for three condensate-forming proteins (hnRNPA1-LCD, LAF-1-RGG, DDX4N) and propose design rules based on scaffold net charge.
- **Visible evidence base** Main text figures 1-5, methods section, supplementary figure references (Supplementary Figs. 1-23), supplementary tables (Supplementary Table 3)
- **Missing materials affecting confidence** Supplementary Information content not provided, including detailed derivations, model hyperparameters, full Pareto front data, and additional experimental controls; raw simulation trajectories and analysis scripts not available for inspection

## Reviewer
- **Overall assessment** This manuscript presents a novel and potentially impactful computational framework for designing interface-localizing peptides for biomolecular condensates. The integration of coarse-grained simulations with MILP-based global optimization is methodologically interesting and represents a meaningful advance over heuristic search methods. The experimental validation across three distinct condensate systems strengthens the claims. However, several technical concerns regarding the simulation methodology, the interpretation of experimental results, and the generalizability of the design rules require clarification before the case is fully established.

- **Who would be interested in the results, and why** Researchers in the fields of biomolecular condensates, protein engineering, and computational protein design would find this work of interest. The demonstrated ability to computationally design short peptides with tailored interfacial localization could enable applications in synthetic biology, biomaterials, and therapeutic intervention in condensate-associated diseases. The methodological framework combining simulation, machine learning, and global optimization may also appeal to computational biologists developing design tools for other molecular systems.

- **Major strengths** The work addresses an important and timely problem in condensate biology, namely the molecular determinants of interfacial localization. The computational pipeline is well-conceived, combining physics-based simulation with rigorous global optimization. The experimental validation across three different condensate systems provides strong support for the approach. The identification of scaffold net charge as a key design parameter offers a simple and testable design rule.

- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness of simulation methodology
- **Claim pointer** The authors claim that the Mpipi force field with the described slab geometry accurately captures interfacial localization behavior, and that pint* is a reliable objective for peptide design.
- **Evidence pointer** Methods section "Interface partitioning"; Figure 2A; Equation 1
- **Concern** The slab geometry uses only 16 protein copies with harmonic walls to maintain the dense phase. This is a highly simplified representation of a condensate interface. The authors state that this small system size was validated by comparison with a 128-copy system for one peptide-protein pair (Supplementary Fig. 23), but this validation is only mentioned in passing and the results are not shown in the main text. More critically, the harmonic walls impose an artificial flat interface geometry that may not represent the curved, fluctuating interfaces of real condensates. The authors should demonstrate that the qualitative design outcomes (i.e., which sequences are predicted to localize at the interface) are robust to system size and wall placement. Additionally, the use of only 16 copies may not capture the full range of local environments experienced by a peptide at a realistic condensate interface.
- **Why it matters** The entire design pipeline rests on the accuracy of the simulation-based objective function. If the simplified geometry introduces systematic biases in the predicted free energy differences, the designed peptides may not perform as expected in real condensate systems. The authors do show experimental validation, which mitigates this concern, but the limited validation (one peptide per system) does not fully establish that the simulation methodology is unbiased across sequence space.
- **Resolution test** Provide a systematic comparison of predicted pint* values for a diverse set of peptide sequences (including both designed and random sequences) between the 16-copy and 128-copy systems. Additionally, test the sensitivity of the design outcomes to the harmonic wall parameters and demonstrate that the top-ranked peptides remain similar under different simulation conditions.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Experimental validation and interpretation
- **Claim pointer** The authors claim that the designed peptides localize at the interface of condensates and that this localization is thermodynamically driven, based on confocal microscopy showing a fluorescent rim.
- **Evidence pointer** Figure 4A-C; Supplementary Figs. 8-10
- **Concern** The experimental validation relies primarily on fluorescence confocal microscopy showing a fluorescent rim around condensates. While this is consistent with interfacial localization, the authors do not provide quantitative analysis of the fluorescence intensity profiles to demonstrate that the peptide is truly enriched at the interface relative to both the dense and dilute phases. The claim that localization is "thermodynamically driven" is supported by the observation that the order of addition does not matter, but this does not rule out kinetic trapping or non-equilibrium effects. Additionally, the authors report that peptide 2 decreases condensate size, but the mechanism for this effect is not investigated. Does the peptide alter interfacial tension, change the supersaturation concentration, or affect Ostwald ripening? The DLS and FCS experiments provide some supporting evidence, but the interpretation is not fully developed.
- **Why it matters** The central claim of the paper is that the designed peptides localize at the interface. The evidence for this is largely qualitative (visual inspection of fluorescent rings). A more rigorous quantitative analysis would strengthen the claim and rule out alternative explanations, such as the peptide being excluded from the dense phase but not specifically enriched at the interface, or the peptide partitioning into a distinct phase at the interface.
- **Resolution test** Provide quantitative fluorescence intensity profiles across condensates, normalized to the intensity in the dilute phase, for both the designed peptide and a control peptide. Demonstrate that the designed peptide shows a statistically significant peak at the interface. Additionally, perform fluorescence recovery after photobleaching (FRAP) experiments to show that the interfacial peptide is mobile and in dynamic exchange, supporting a thermodynamic rather than kinetic explanation.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Generalizability of design rules
- **Claim pointer** The authors claim that the net charge of the condensate-forming protein is a key physicochemical feature for designing interface-localizing peptides, and that the design rules can be generalized across different condensate systems.
- **Evidence pointer** Figure 5; Discussion section
- **Concern** The three condensate systems studied (hnRNPA1-LCD, LAF-1-RGG, DDX4N) differ in net charge, but also in many other properties including sequence composition, aromatic content, and predicted phase behavior. The attribution of the observed design differences primarily to net charge is not fully supported by the data. The authors do not systematically vary net charge while holding other properties constant. Furthermore, the design rules are derived from only three systems, which is a small sample size for drawing general conclusions. The authors acknowledge that the optimality depends on force field accuracy, but the broader question of whether the identified design principles extend to other condensate types (e.g., those formed by folded domains or RNA-binding proteins) remains open.
- **Why it matters** The paper claims to provide "design rules" for interface-localizing peptides. If these rules are not generalizable, the practical utility of the approach is limited. The identification of net charge as the key parameter may be an oversimplification that could mislead future design efforts.
- **Resolution test** Test the design rules on additional condensate systems with systematically varied net charge (e.g., mutants of hnRNPA1-LCD with different charge distributions). Alternatively, perform a computational analysis where the net charge is varied in silico while keeping other sequence properties fixed, and show that the predicted design outcomes change in the expected direction.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Reproducibility and transparency of the optimization pipeline
- **Claim pointer** The authors claim that the MILP-based optimization provides globally optimal solutions and that the pipeline is a general strategy for designing interface-localizing peptides.
- **Evidence pointer** Methods section "Machine learning and optimization"; Figure 2C
- **Concern** The details of the neural network architecture, training procedure, and MILP formulation are only partially described in the main text, with additional details deferred to the Supplementary Methods. The feature engineering approach (44 features based on composition and spatial distribution) is described, but the specific features are not listed in the main text. The convergence criteria for the active learning loop are not clearly defined. For a computational pipeline that is claimed to be a "general strategy," the reproducibility of the method is critical. The authors should provide sufficient detail for others to implement the pipeline, including the exact MILP formulation, the handling of the nonlinear pint* objective, and the hyperparameter selection process.
- **Why it matters** The methodological contribution of this work is a key part of its significance. If the pipeline cannot be readily implemented by others, its impact will be limited. The claim of "global optimality" is strong and should be accompanied by clear statements about the assumptions and limitations of the MILP formulation.
- **Resolution test** Provide a complete description of the pipeline in the main text or a dedicated methods section, including the full list of 44 features, the MILP formulation with all constraints, and the convergence criteria. Ideally, make the code and trained models available as open-source software.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity of presentation
- **Affected element** Figure 3A
- **Evidence pointer** Figure 3A
- **Issue** The improvement in pint* over iterations is described as "approximately three orders of magnitude," but the y-axis scale and the specific values are not clearly visible in the figure. It would be helpful to show the actual values or a table of the progression.
- **Required correction** Add axis labels with clear units and consider showing the actual pint* values for each iteration in the figure or a supplementary table.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Statistical analysis
- **Affected element** Figure 4C
- **Evidence pointer** Figure 4C
- **Issue** The size distributions are reported as mean ± SD with n = 100, but the statistical significance of the difference between peptide 2 and control conditions is not reported. A statistical test (e.g., t-test or Mann-Whitney U test) should be performed.
- **Required correction** Add statistical analysis to the size distribution data and report p-values.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Completeness of experimental details
- **Affected element** Methods section "Brightfield and confocal microscopy"
- **Evidence pointer** Methods section
- **Issue** The concentration of the peptides used in the experiments is not explicitly stated. The protein-to-peptide ratio is given as 10:1, but the absolute concentrations are not provided.
- **Required correction** Specify the absolute concentrations of both protein and peptide in the experimental methods.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Interpretation of control experiments
- **Affected element** Figure 4B
- **Evidence pointer** Figure 4B
- **Issue** The control peptide (peptide 4) is described as having a "much lower value for pint*", but the specific value is not given. It would be helpful to know the quantitative difference in predicted pint* between the designed and control peptides.
- **Required correction** Report the predicted pint* values for both the designed and control peptides in the text or a supplementary table.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Discussion of limitations
- **Affected element** Discussion section
- **Evidence pointer** Discussion section
- **Issue** The authors acknowledge the dependence on force field accuracy but do not discuss the potential limitations of the coarse-grained model in capturing specific interactions (e.g., cation-pi interactions) that may be important for interfacial localization.
- **Required correction** Add a brief discussion of the known limitations of the Mpipi force field and how they might affect the design outcomes.

## Risk / unsupported claims
- The claim that the designed peptides are "thermodynamically driven" to localize at the interface is not fully supported by the experimental evidence, which does not rule out kinetic effects or non-equilibrium trapping.
- The claim that scaffold net charge is "a key physicochemical feature" for design is based on only three systems and may not be generalizable.
- The claim of "global optimality" of the MILP solutions is conditional on the accuracy of the surrogate model, which is not fully validated across the entire sequence space.
- The statement that the pipeline offers "a general strategy for rationally designing interface-localizing peptides" is not fully established given the limited number of experimental validations (one peptide per system).
- The assertion that the designed peptides "modify condensate size distribution" is supported, but the mechanism and the relationship to interfacial localization are not fully explored.
- The claim that the pipeline "enables a more thorough exploration of the design space" compared to previous approaches is not quantitatively supported by comparisons with alternative search methods.