## Review setup
- **Input scope** Full manuscript text (abstract, introduction, results, discussion, methods) as provided
- **Assessment boundary** Scientific validity, technical soundness, and significance of the claims as supported by the provided evidence
- **Shared manuscript claim summary** The authors present a computational pipeline combining coarse-grained simulations, machine learning, and mixed-integer linear programming to design 30-residue peptides that preferentially localize at the interface of biomolecular condensates. They report successful design and experimental validation for three distinct condensate-forming IDRs (hnRNPA1-LCD, LAF-1-RGG, DDX4N), with peptides exhibiting surfactant-like architectures. The authors propose net charge of the scaffold as a key physicochemical parameter governing interfacial localization.
- **Visible evidence base** Abstract, introduction, results and discussion sections (workflow, simulation setup, hnRNPA1-LCD results, other condensate targets), conclusions, methods (simulation parameters, protein production, microscopy, DLS), data availability statement
- **Missing materials affecting confidence** Figures 1-6 and all supplementary figures/tables referenced but not provided; detailed derivation of equation (1); full peptide sequences; quantitative data for LAF-1-RGG and DDX4N experimental validation; statistical analysis details; control experiment details

## Reviewer

- **Overall assessment** This manuscript addresses an important and timely problem in the condensate field: the rational design of peptides that localize at condensate interfaces. The computational approach combining coarse-grained simulations with ML and MILP is innovative and technically sophisticated. However, the provided text lacks critical quantitative data and figures necessary to fully evaluate the claims. The experimental validation appears limited in scope, and several methodological details require clarification. The central claim regarding net charge as a key design parameter is plausible but not fully established from the evidence presented.

- **Who would be interested in the results, and why** Researchers in the fields of biomolecular condensates, protein phase separation, and membraneless organelles would find this work of high interest. Additionally, the computational methodology (ML-guided design with global optimization guarantees) will appeal to the broader protein design and engineering community. The potential applications in modulating condensate properties and correcting aberrant aggregation behaviors make this relevant to those studying neurodegenerative diseases and RNA metabolism.

- **Major strengths**
  1. The computational pipeline is novel, combining state-of-the-art methods (coarse-grained simulations, ML surrogates, MILP with global optimality guarantees) in a way not previously applied to condensate interface targeting
  2. The work addresses a significant gap: molecular grammar for condensate interface localization is largely unknown
  3. Experimental validation across three distinct condensate systems strengthens the generality of the findings
  4. The identification of net charge as a key parameter provides a simple, testable design rule
  5. The surfactant-like architecture concept is physically intuitive and well-motivated

- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence sufficiency
- **Claim pointer** "These peptides exhibit surfactant-like architectures, with one tail incorporated into the condensate and the other excluded from the dense phase" and "peptide 2 exhibits the strong predicted interface partitioning"
- **Evidence pointer** Figures 3, 4, 5; location not provided
- **Concern** The manuscript text describes experimental validation but the actual data (fluorescence microscopy images, intensity profiles, size distributions) are not visible in the provided material. The claim of "strong predicted interface partitioning" for peptide 2 is based on a single peptide per condensate system, with only one control peptide (peptide 4) for hnRNPA1-LCD. No quantitative metrics for interface partitioning (e.g., enrichment ratios, partition coefficients) are provided in the text.
- **Why it matters** The central claim of the paper is that designed peptides localize at condensate interfaces. Without visible quantitative data and appropriate statistical analysis, this claim cannot be adequately assessed. The limited number of validated peptides (one per system) raises questions about the robustness of the design approach.
- **Resolution test** Provide the actual microscopy data with quantitative intensity profiles across condensates, statistical comparison between interface-localizing and control peptides, and ideally validation of multiple designed peptides per target to demonstrate reproducibility.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** "The optimization problem containing the trained neural network was formulated as a mixed-integer linear programming formulation, which led to globally optimal sequences for each iteration"
- **Evidence pointer** Methods section, "Machine learning and optimization"; location not provided
- **Concern** The manuscript claims global optimality of the MILP approach, but the details of the neural network architecture, feature engineering, and the MILP formulation are only partially described. The text mentions "engineered features, obtained through a linear transformation of the peptide sequence" but does not specify what these features are. The conversion of the nonlinear objective (equation 1) to a linear form using "supporting hyperplanes" is mentioned but not detailed. The convergence criteria and the number of iterations required are not stated.
- **Why it matters** The claim of global optimality is a key differentiator from genetic algorithms and other heuristic approaches. Without sufficient detail on the formulation and its validation, readers cannot assess whether the claim is justified or reproduce the method.
- **Resolution test** Provide complete details of the feature set, the MILP formulation including all constraints and the linearization approach, validation of the surrogate model accuracy, and a comparison of MILP solutions against exhaustive search or other global optimization methods on test cases.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Generalizability
- **Claim pointer** "we identified design rules for interface-partitioning peptides, highlighting the net charge of the condensate-forming protein as a key physicochemical feature"
- **Evidence pointer** Results section, "Designing peptides targeting other protein condensates"; Figures 5, 6; location not provided
- **Concern** The manuscript proposes net charge as the key parameter governing the design of interface-localizing peptides. However, only three condensate systems were tested, with a limited range of net charge values (NCPR from -0.017 to +0.057). The DDX4N case, which has the lowest charge density, required a qualitatively different design strategy (valine-rich tails), suggesting that the design rules may not be universal. The text does not discuss potential confounding factors such as sequence composition, aromatic content, or specific interaction motifs.
- **Why it matters** The claim of a general design rule based on net charge has significant implications for the field. If the rule only applies within a narrow parameter range, its practical utility is limited. The mechanistic explanation for why net charge matching works (electrostatic repulsion) is plausible but not directly tested.
- **Resolution test** Test the design rules on additional condensate systems with a wider range of net charges and sequence compositions. Provide systematic variation of charge while controlling for other parameters to isolate the effect of net charge.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Experimental rigor
- **Claim pointer** "peptide 2 also caused a significant decrease in average condensate diameter (from 5.6 ± 2.3 µm to 1.7 ± 0.7 µm, mean ± standard deviation, n = 50)"
- **Evidence pointer** Results section, "Peptides targeting the interface of hnRNPA1-LCD condensates"; Figure 4C; location not provided
- **Concern** The manuscript reports a significant decrease in condensate size upon addition of the interface-localizing peptide, but the mechanism is not investigated. The text does not discuss whether this is due to changes in interfacial tension, altered coalescence dynamics, or other effects. The biological or functional consequences of this size reduction are not addressed. Additionally, the DLS data mentioned in the methods are not presented in the text.
- **Why it matters** The observed effect on condensate size suggests that the designed peptides may have functional consequences beyond simple localization. Understanding the mechanism and potential applications (e.g., modulating condensate properties) would significantly enhance the impact of the work.
- **Resolution test** Provide additional characterization of the peptide-condensate interaction, such as measurements of interfacial tension, condensate viscosity, or fusion dynamics. Discuss the potential functional implications of the observed size reduction.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Equation (1) and its derivation
- **Evidence pointer** Results section, "Simulation, machine learning, and optimization setup"; location not provided
- **Issue** The equation defining the interface partitioning objective is presented without the actual mathematical expression in the provided text. The description of the derivation is incomplete.
- **Required correction** Provide the full equation and a clear derivation in the main text or supplementary information.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Reproducibility
- **Affected element** Simulation parameters
- **Evidence pointer** Methods section, "Molecular simulations"; location not provided
- **Issue** The methods describe the simulation setup but do not provide specific parameters such as the number of simulation steps, the criteria for convergence of the adaptive biasing force calculations, or the temperature and pressure conditions beyond the Langevin thermostat at 300 K.
- **Required correction** Include all relevant simulation parameters to enable reproduction of the computational results.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Statistical rigor
- **Affected element** Experimental measurements
- **Evidence pointer** Results section, "Peptides targeting the interface of hnRNPA1-LCD condensates"; Figure 4; location not provided
- **Issue** The manuscript reports mean and standard deviation for condensate diameter measurements but does not specify the number of independent experiments or whether measurements were blinded.
- **Required correction** Clarify the experimental design, including the number of replicates and any blinding procedures used.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Control experiments
- **Evidence pointer** Results section, "Peptides targeting the interface of hnRNPA1-LCD condensates"; location not provided
- **Issue** The text mentions a control peptide (peptide 4) that distributes uniformly, but the criteria for selecting this control are not described. It is unclear whether the control was designed to be similar in composition but lacking the interface-targeting features.
- **Required correction** Describe the design of control peptides and the rationale for their selection.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Presentation
- **Affected element** Figure references
- **Evidence pointer** Throughout the results section; location not provided
- **Issue** The text references Figures 1-6 and supplementary figures, but the actual figures are not provided in the manuscript text. This makes it difficult to follow the narrative.
- **Required correction** Ensure all figures are included and properly referenced in the final submission.

- **Concern ID** R1-m6
- **Severity** Minor
- **Axis** Language
- **Affected element** Typographical errors
- **Evidence pointer** Results section, "Designing peptides targeting other protein condensates"; location not provided
- **Issue** The text contains a typographical error: "such architectures ere explored" should read "such architectures were explored".
- **Required correction** Proofread the manuscript for typographical errors.

## Risk / unsupported claims
- The claim that designed peptides "exhibit surfactant-like architectures" is supported only by computational predictions and limited experimental data; the structural characterization of the peptides at the interface is not provided
- The claim that "net charge of the condensate-forming protein is a key physicochemical parameter" is based on only three systems and lacks systematic variation to isolate this parameter
- The claim of "global optimality" of the MILP approach cannot be fully assessed without complete formulation details
- The statement that this is "the first study showing that short (30-residue long) peptides can preferentially partition at the interface of the condensates" requires a more thorough literature search to substantiate
- The functional significance of the observed condensate size reduction is not established
- The generalizability of the design approach to other condensate systems beyond the three tested is not demonstrated