## Review setup
- **Input scope** Full manuscript text (abstract, introduction, methods, results, discussion, conclusions) as provided
- **Assessment boundary** Scientific validity, methodological soundness, reproducibility, and support of claims based solely on the supplied text; no supplementary figures, tables, or videos were accessible for direct inspection
- **Shared manuscript claim summary** The authors report the first application of supervised molecular dynamics (SuMD) to reconstruct RNA recognition by intrinsically disordered regions (IDRs), using two retrospective systems (SF3A1-UBL/U1-SL4, FUS RRM/U1-SL3) and one prospective system (SERF2/TERRA12), with a two-step supervision protocol that first guides the disordered region and then the structured domain toward the RNA. They claim reproduction of experimental binding modes, discrimination of near-native poses from decoys via stability metrics, and generation of a prospective model consistent with experimental mutagenesis data.
- **Visible evidence base** Main text methods and results sections; references to Figures 1–6 (not shown), Tables 1–2 (not shown), Tables S1–S3, Figures S1–S9, and Videos S1–S3 (all in Supporting Information, not provided)
- **Missing materials affecting confidence** All figures, tables, supplementary tables, supplementary figures, and videos; specific numerical values for RMSD, interaction energies, and statistical measures; details of SuMD supervision parameters (e.g., distance thresholds, step lengths, number of resimulations); force field validation details; system size and simulation time for each replicate

## Reviewer

- **Overall assessment** The manuscript addresses a timely and important problem: modeling RNA recognition by intrinsically disordered regions, which remains a major computational challenge. The two-step SuMD protocol is a sensible adaptation of an established enhanced sampling method, and the choice of retrospective and prospective systems is well motivated. However, the evidence presented in the text alone is insufficient to fully evaluate the central claims. Key quantitative results, figures, and supplementary data are referenced but not visible, and several methodological details are underspecified. The claim of "first application" of SuMD to RNA-IDR systems is plausible but requires a more thorough comparison with prior SuMD studies on nucleic acid systems. The prospective SERF2/TERRA12 model is described as consistent with experimental data, but the strength of this consistency cannot be assessed without the referenced figures and tables. The manuscript is well written and logically structured, but the current evidence base does not fully establish the case.

- **Who would be interested in the results, and why** Computational biophysicists and chemists working on enhanced sampling methods for biomolecular recognition, particularly those studying protein-RNA interactions and intrinsically disordered proteins. Structural biologists interested in RNA-binding proteins and the role of RGG motifs. Researchers in the RNA therapeutics field who need structural models of RNA-IDR complexes for drug design. Method developers in the molecular dynamics community who would be interested in the two-step supervision strategy as a general approach for flexible macromolecular complexes.

- **Major strengths**
  1. The problem is well chosen and significant: RNA-IDR recognition is poorly understood and computationally challenging, and the manuscript addresses a genuine gap.
  2. The two-step supervision protocol is a logical and potentially generalizable methodological contribution, with clear rationale based on preliminary observations that disordered regions initiate contact.
  3. The inclusion of both retrospective validation and a prospective application is a strong study design, allowing assessment of both reproducibility and predictive utility.
  4. The use of multiple independent replicates and stability-based selection criteria (RMSD plus interaction energy) is methodologically sound and addresses the stochastic nature of SuMD.
  5. The writing is clear and accessible, with appropriate context for the biological relevance of each system.

- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence completeness
- **Claim pointer** The authors claim that SuMD "can reproduce association pathways involving both disordered and structured regions, capturing transient contacts and interaction hierarchies" and that the method "reproduce[s] experimental binding modes" for the retrospective systems.
- **Evidence pointer** Results sections for SF3A1/U1-SL4 and FUS/U1-SL3; Figures 1–6 (not provided); Tables 1–2 (not provided); Tables S2–S3 and Figures S2–S7 (not provided)
- **Concern** The central quantitative evidence for the reproduction of experimental binding modes is not visible in the provided text. The manuscript references RMSD values (e.g., 4.2 Å for SF3A1 Run1), but the figures and tables that would show structural overlays, interaction energy profiles, and comparisons across replicates are all in the Supporting Information or in figures that were not included. Without these, the reader cannot verify the strength of the structural agreement, the magnitude of interaction energies, or the statistical significance of differences between runs.
- **Why it matters** The core claim of the paper is that SuMD can reproduce known binding modes and discriminate near-native poses from decoys. This claim rests entirely on quantitative comparisons that are not accessible in the provided material. The text alone is insufficient to establish that the method works as claimed.
- **Resolution test** Provide all figures and tables in the main text or as accessible supplementary material, with clear numerical values for RMSD, interaction energies, and their uncertainties. Show structural overlays of the SuMD-generated poses against experimental structures. Include a quantitative comparison of interaction energy profiles between SuMD-generated and experimental complexes.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Methodological reproducibility
- **Claim pointer** The authors state that "a two-step supervision protocol was introduced" and describe the general strategy, but the specific implementation details are incomplete.
- **Evidence pointer** Materials and Methods, "Supervised Molecular Dynamics (SuMD) Simulation" section
- **Concern** The description of the SuMD protocol lacks critical parameters needed for reproduction. The text states that SuMD steps last 300 ps and that the distance between centers of mass is monitored, but does not specify: the distance threshold that defines a "productive" step, the number of steps per supervision phase, the criteria for switching from Step-1 to Step-2, the number of resimulations allowed per step, the initial distance between protein and RNA, the random seed handling, or the temperature coupling details during SuMD. The two-phase supervision is the methodological core of the paper, and these details are essential.
- **Why it matters** Without full methodological detail, the work cannot be reproduced by other groups, which is a fundamental requirement for a methods-oriented paper. The novelty claim rests on the specific implementation of the two-step protocol, and the reader cannot assess whether the approach is genuinely new or a trivial modification of existing SuMD implementations.
- **Resolution test** Provide a complete description of all SuMD parameters, including distance thresholds, step counts, switching criteria, resimulation limits, and any system-specific adjustments. Consider providing the SuMD code or a pseudocode algorithm in the Supporting Information.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Claim substantiation
- **Claim pointer** The authors state that the prospective SERF2/TERRA12 model is "consistent with experimental mutagenesis data" and that the predicted binding mode "closely reflects the interaction pattern inferred from experimental data."
- **Evidence pointer** Results section for SERF2/TERRA12; Figures 5–6 (not provided); Figures S8–S9 (not provided)
- **Concern** The text describes agreement with NMR-HSQC chemical shift perturbation data, but the specific comparison is not shown. The manuscript states that nucleotides G4, G5, G9, and G10 were identified as key, and that the SuMD model shows interactions in the G4–G11 region, but the degree of overlap, the quantitative measure of consistency, and the significance of the agreement are not presented. Furthermore, the text mentions "experimental mutagenesis data" in the abstract but the main text does not describe any mutagenesis experiments or their results.
- **Why it matters** The prospective application is a key differentiator of this work, demonstrating the method's utility for systems without known structures. If the consistency with experimental data is not rigorously quantified and presented, the claim of predictive utility is weakened. The discrepancy between the abstract (mentioning mutagenesis) and the main text (mentioning only NMR data) is also a concern.
- **Resolution test** Provide a direct, quantitative comparison between the SuDM-predicted interaction footprint and the experimental NMR data (e.g., a bar chart of chemical shift perturbations overlaid with predicted contact frequencies). Clarify whether mutagenesis data exist and, if so, present them explicitly. If no mutagenesis data exist, revise the abstract accordingly.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Novelty assessment
- **Claim pointer** The authors state this is the "first application of supervised molecular dynamics (SuMD) to investigate recognition processes between nucleic acids and intrinsically disordered proteins."
- **Evidence pointer** Introduction and Discussion sections
- **Concern** The novelty claim is stated without a systematic comparison to prior SuMD applications on nucleic acid systems. The introduction mentions that SuMD has been applied to "diverse ligand types (small molecules, macrocycles, and peptides) and targets (soluble proteins, membrane receptors, and nucleic acids)," which implies SuMD has been used on nucleic acid targets before. The specific novelty of applying SuMD to IDR-containing proteins needs to be positioned more carefully against this prior work. What exactly is new: the two-step protocol, the application to IDRs, or both?
- **Why it matters** The novelty claim is a central part of the paper's contribution. If SuMD has been applied to protein-RNA complexes before, even without IDRs, the claim of "first application" needs to be qualified. A thorough literature comparison would strengthen the paper and help readers understand the specific advance.
- **Resolution test** Provide a more detailed comparison with prior SuMD studies on nucleic acid systems, explicitly stating what has and has not been done before. Clarify whether the novelty lies in the two-step protocol, the application to IDR-containing proteins, or both.

- **Concern ID** R1-M5
- **Severity** Major
- **Blocking** No
- **Axis** Validation rigor
- **Claim pointer** The authors claim that stability-based selection (RMSD and interaction energy from 100 ns MD extensions) can "discriminate" near-native poses from decoys.
- **Evidence pointer** Results sections for both retrospective systems; Tables S2–S3 (not provided); Figures S4–S7 (not provided)
- **Concern** The discrimination of near-native poses from decoys is a strong claim that requires a rigorous statistical framework. The text reports average RMSD and interaction energy values for three replicates, but does not provide error bars, statistical tests, or a clear decision threshold. It is unclear whether the differences between runs (e.g., Run1 vs. Run2 for SF3A1) are statistically significant or within the noise of the method. Furthermore, the selection criteria were applied post hoc, and it is not clear whether they would have identified the correct run prospectively.
- **Why it matters** The practical utility of the method for prospective applications depends on the ability to reliably select the best pose. If the discrimination is not statistically robust, the method's predictive value is questionable.
- **Resolution test** Provide statistical analysis of the differences between runs (e.g., standard deviations, confidence intervals, or a formal hypothesis test). Describe the decision rule for selecting the best run in a prospective scenario. Consider cross-validation or a blinded test to demonstrate the method's predictive power.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Abstract
- **Evidence pointer** Abstract, last sentence
- **Issue** The abstract mentions "experimental mutagenesis data" but the main text does not describe any mutagenesis experiments. This is confusing and potentially misleading.
- **Required correction** Either add a description of the mutagenesis experiments and their results to the main text, or revise the abstract to refer only to the NMR-HSQC data that are actually presented.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Materials and Methods, "Hardware Overview"
- **Evidence pointer** Materials and Methods, "Hardware Overview" section
- **Issue** The hardware description is minimal and does not specify the number of GPUs used per simulation, the CPU/GPU balance, or the wall-clock time per simulation. This information is useful for readers assessing the computational cost of the method.
- **Required correction** Provide additional details on the computational resources used per simulation, including the number of GPUs, the simulation wall-clock time, and the total computational cost for all simulations reported.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Reproducibility
- **Affected element** Materials and Methods, "Structure Preparation"
- **Evidence pointer** Materials and Methods, "Structure Preparation" section
- **Issue** The text states that the "first conformer was selected" for NMR structures but does not specify the selection criteria for the deposited conformers or whether the choice of conformer affects the results.
- **Required correction** Clarify the selection criteria for the NMR conformer and, if possible, test the sensitivity of the results to the choice of conformer.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Interpretation
- **Affected element** Results, SF3A1/U1-SL4 section
- **Evidence pointer** Results, SF3A1/U1-SL4 section, final paragraph
- **Issue** The text states that the SuMD-generated complex from Run1 was stable over 500 ns, but it is not clear whether this stability is comparable to that of the experimental complex simulated under the same conditions. A direct comparison of RMSD distributions or interaction energy profiles would be more informative.
- **Required correction** Provide a direct, quantitative comparison of the stability metrics between the SuMD-generated and experimental complexes over the 500 ns simulation.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Generalizability
- **Affected element** Discussion and Conclusions
- **Evidence pointer** Discussion and Conclusions, final paragraph
- **Issue** The authors suggest the method could be used for "structure-based drug discovery pipelines that target RNA-IDR interactions," but no discussion is provided on the limitations of the method for this purpose, such as the need for prior knowledge of binding sites or the computational cost for large-scale screening.
- **Required correction** Add a brief discussion of the practical considerations and limitations for drug discovery applications, including the need for experimental input and the scalability of the method.

- **Technical failings that need to be addressed before the case is established**
  - R1-M1: Central quantitative evidence (figures, tables, supplementary data) not visible in the provided material
  - R1-M2: Incomplete methodological detail for SuMD parameters, preventing reproduction
  - R1-M3: Inconsistency between abstract (mutagenesis) and main text (NMR only); lack of quantitative comparison for prospective case

- **Assessment against Nature-style criteria**
  - **Originality**: The two-step supervision protocol is a reasonable adaptation of existing SuMD methodology, but the conceptual advance over prior SuMD applications to nucleic acid systems needs to be more clearly articulated. The application to IDR-containing proteins is timely, but the novelty claim requires a more thorough literature comparison.
  - **Scientific importance**: The problem is important, and a reliable method for modeling RNA-IDR recognition would be valuable. However, the importance of the specific methodological contribution is not fully established without a clearer demonstration of its advantages over existing approaches.
  - **Interdisciplinary readership**: The work bridges computational chemistry, structural biology, and RNA biology, and the writing is accessible to a broad audience. The biological context for each system is well explained.
  - **Technical soundness**: The general approach is sound, but the lack of visible quantitative evidence and incomplete methodological detail prevent a full assessment. The stability-based selection criteria need statistical validation.
  - **Readability for nonspecialists**: The manuscript is well written and logically structured. The concepts are explained clearly, and the figures (not visible) are presumably well designed. The abstract is accessible, though the mutagenesis reference is misleading.

- **Recommendation posture** Supportive if technical concerns are resolved. The manuscript addresses an important problem with a plausible methodological approach, and the study design is sound. However, the current evidence base is insufficient to fully establish the central claims. The authors must provide the missing figures, tables, and supplementary data, complete the methodological description, and strengthen the statistical analysis of their results. The novelty claim should be refined with a more thorough comparison to prior work. If these concerns are addressed, the manuscript could make a valuable contribution to the field.