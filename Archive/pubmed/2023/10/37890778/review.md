## Review setup
- **Input scope** Full manuscript text, including abstract, results, discussion, conclusion, and experimental procedures. No supplementary information or figures were provided for review.
- **Assessment boundary** The review is limited to the claims and evidence presented in the provided manuscript text. No external validation of the simulation data or methodology was performed.
- **Shared manuscript claim summary** The authors use molecular dynamics simulations to propose that "boundary residues" (369–377 AA) between the folded RNA recognition motif and the disordered RGG2 domain of FUS are critical for stable RNA binding. They further propose a division of labor between RRM, RGG1, and RGG2 in binding a stem-loop RNA, with RGG2 interactions confined to the stem-loop junction and RGG1 binding the RNA stem. The number of RGG repeats is proposed to modulate binding affinity, with glycine residues contributing weak hydrophobic interactions.
- **Visible evidence base** The manuscript text describes simulation results, including minimum distance plots, interatomic distance matrices, hydrogen bond analyses, interaction histograms, and clustering analyses. Figures and tables are referenced but not provided. The experimental procedures section describes the simulation setup, force fields, and analysis methods.
- **Missing materials affecting confidence** The following materials were not provided and would be essential for a full assessment: all figures (Figures 1–9, S1–S14), all tables (Tables 1, S1, S2), the supporting information document, and the supplementary movie. Without these, the quantitative results and visual evidence cannot be independently evaluated.

## Reviewer
- **Overall assessment** This manuscript presents a molecular dynamics study of FUS-RNA interactions, focusing on the role of boundary residues between the RRM and RGG2 domains. The study addresses a relevant question in the field of RNA-binding proteins and phase separation. The authors propose a novel functional role for a previously underappreciated region of FUS. However, the manuscript has significant limitations in its current form. The central claim regarding the critical role of boundary residues is based on simulations of a truncated RRM construct that shows RNA dissociation, but the comparison to the full-length context is not rigorously established. The study relies heavily on qualitative visual inspection of trajectories and distance-based metrics, and the statistical robustness of the conclusions is not clearly demonstrated. The modeling of the RGG domains, particularly the sequential fragment addition protocol, raises concerns about potential biases in the resulting conformations. The manuscript would benefit from a more rigorous quantitative analysis, a clearer presentation of the evidence, and a more cautious interpretation of the results. The work is of interest to the biophysics and RNA biology communities, but the current evidence does not fully support all the claims made.
- **Who would be interested in the results, and why** Researchers studying RNA-binding proteins, particularly those involved in phase separation and neurodegeneration (e.g., FUS, TDP-43, hnRNPs), would be interested in this work. The study provides a molecular-level model for how ordered and disordered domains cooperate in RNA binding, which is relevant to understanding the function of a large class of proteins. The proposed role of boundary residues and the division of labor between RGG domains could inform future experimental studies on FUS and related proteins. The methodological approach, using MD simulations to study IDP-RNA complexes, may also be of interest to computational biophysicists.
- **Major strengths**
    1. The study addresses a relevant and timely question about the molecular basis of FUS-RNA interactions, which is important for understanding FUS function and dysfunction.
    2. The authors use a state-of-the-art force field (a99SB-disp) that is designed to handle proteins with both folded and disordered regions, which is appropriate for the system under study.
    3. The study provides a detailed molecular model of how the RRM and RGG domains cooperate to bind RNA, proposing a "division of labor" that is a useful conceptual framework.
    4. The authors identify a specific region (boundary residues 369–377) as functionally important, which is a testable hypothesis for experimentalists.
    5. The manuscript is generally well-written and the logic of the study is clear.
- **Major Concerns**
    - **Concern ID** R1-M1
    - **Severity** Major
    - **Blocking** Yes
    - **Axis** Technical soundness
    - **Claim pointer** The authors claim that the core RRM (276–368 AA) is insufficient to bind RNA and that the boundary residues (369–377 AA) are critical for stable RNA binding, based on simulations showing RNA dissociation from the core RRM.
    - **Evidence pointer** Figure 2B, 2C; text in "Boundary residues between the folded RRM and RGG2 are critical for tight RNA binding"
    - **Concern** The claim that the core RRM is insufficient for RNA binding is based on a single simulation (or a set of simulations) of a truncated construct. The authors state that the minimum distance between the RRM beta-sheet and RNA increases dramatically after 60 ns, indicating dissociation. However, it is not clear how many replicates were performed for this core RRM construct, and the statistical significance of this dissociation event is not established. A single dissociation event in one trajectory could be a stochastic fluctuation rather than a robust property of the system. Furthermore, the comparison between the core RRM and the longer RRM (276–377) is not quantitative. The authors state that the longer RRM also shows "unstable behavior" and "weak/flexible RNA binding," which seems to contradict the claim that the boundary residues are critical for stable binding. The distinction between the behavior of the core RRM and the longer RRM needs to be more clearly quantified and statistically supported.
    - **Why it matters** The central claim of the paper rests on the difference in RNA binding stability between the core RRM and the RRM with boundary residues. If this difference is not robustly demonstrated, the main conclusion is not supported.
    - **Resolution test** The authors should provide a quantitative comparison of RNA binding stability between the core RRM and the longer RRM constructs, using multiple independent simulations and appropriate statistical tests. Metrics such as the fraction of time the RNA remains bound, the free energy of binding, or the residence time of the RNA should be calculated and compared. The authors should also clarify whether the "unstable behavior" of the longer RRM is qualitatively different from the dissociation observed for the core RRM.

    - **Concern ID** R1-M2
    - **Severity** Major
    - **Blocking** Yes
    - **Axis** Technical soundness
    - **Claim pointer** The authors claim that the number of RGG repeats modulates RNA binding affinity, with three repeats (FUS390) providing a significant increase in binding and the full RGG2 (FUS418) providing a further, smaller increase due to weak glycine interactions.
    - **Evidence pointer** Figure 3B, 3D, 4B, 7; text in "Electrostatically dominant RGG2–RNA interaction is modulated by the number of RGG repeats"
    - **Concern** The claim that the number of RGG repeats modulates binding affinity is based on comparing the number of hydrogen bonds and the interaction patterns in different constructs. However, the authors do not provide a direct measure of binding affinity, such as a calculated binding free energy. The number of hydrogen bonds is a proxy for interaction strength, but it does not directly translate to binding affinity. The comparison between FUS390 and FUS418 is particularly problematic, as the authors state that the increase in binding affinity is "comparatively lesser" and attribute this to weak glycine interactions. This is a qualitative statement that is not supported by a quantitative analysis. The authors should calculate binding free energies or use other rigorous methods to compare the binding affinities of the different constructs.
    - **Why it matters** The claim that the number of RGG repeats modulates binding affinity is a key finding of the paper. Without a quantitative measure of binding affinity, this claim is not well-supported.
    - **Resolution test** The authors should calculate binding free energies for the different constructs (e.g., using MM-PBSA or a similar method) and compare them. They should also provide a more detailed analysis of the contributions of individual residues to the binding free energy, to support the claim that glycine residues contribute weak hydrophobic interactions.

    - **Concern ID** R1-M3
    - **Severity** Major
    - **Blocking** Yes
    - **Axis** Technical soundness
    - **Claim pointer** The authors claim that the boundary residues (369–377 AA) form a single helical turn-like structure that interacts with the RNA, and that this interaction is important for RNA binding.
    - **Evidence pointer** Figure S2; text in "Boundary residues between the folded RRM and RGG2 are critical for tight RNA binding"
    - **Concern** The authors state that in the NMR structure, the boundary residues form a helical turn with six hydrogen bonds and two cation-pi interactions with the RNA. However, the manuscript does not provide a detailed analysis of the stability of this helix during the simulations. The authors mention that the helix unwinds in the core RRM simulation, but it is not clear whether the helix is stable in the longer RRM constructs. The role of the helix in RNA binding should be more directly investigated, for example by analyzing the secondary structure of the boundary residues over time in all simulations.
    - **Why it matters** The helical structure of the boundary residues is proposed to be a key structural feature for RNA binding. If this helix is not stable in the simulations, the proposed mechanism is questionable.
    - **Resolution test** The authors should provide a time-resolved analysis of the secondary structure of the boundary residues in all simulations. They should also analyze the specific interactions (hydrogen bonds, cation-pi) between the boundary residues and the RNA over time, to determine if these interactions are stable and contribute to the binding.

    - **Concern ID** R1-M4
    - **Severity** Major
    - **Blocking** No
    - **Axis** Technical soundness
    - **Claim pointer** The authors claim that the RNA sequence/structure specificity of the RRM is required for initial recognition, but that RGG domains can compensate for loss of specificity.
    - **Evidence pointer** Figure 8, 9; text in "FUS-RRM requires RNA sequence/shape specificity to initiate RNA binding"
    - **Concern** The simulations with the mutant RNA (AAUG) show that the RRM-RNA interaction is weakened, but the RGG2 domain can still bind. This is an interesting observation, but the authors do not provide a quantitative measure of the binding affinity of the mutant RNA compared to the wild-type. The claim that the RGG domains can "compensate" for the loss of specificity is not directly supported by the data. The authors should calculate binding free energies for the mutant RNA complexes and compare them to the wild-type.
    - **Why it matters** The claim about the compensatory role of RGG domains is important for understanding the promiscuous RNA binding of FUS. Without a quantitative comparison, this claim is speculative.
    - **Resolution test** The authors should calculate binding free energies for the wild-type and mutant RNA complexes and compare them. They should also analyze the specific interactions that are lost and gained upon mutation, to understand the molecular basis of the compensation.

- **Minor Comments**
    - **Concern ID** R1-m1
    - **Severity** Minor
    - **Axis** Readability for nonspecialists
    - **Affected element** Abstract
    - **Evidence pointer** Abstract
    - **Issue** The abstract is dense and uses technical terms without sufficient context. The phrase "division of labor" is used but not explained. The significance of the "boundary residues" is not immediately clear to a reader who is not an expert in FUS biology.
    - **Required correction** The abstract should be revised to provide more context for the key concepts. For example, the authors could briefly explain what the RRM and RGG domains are and why their cooperation is important. The term "boundary residues" should be defined more clearly.

    - **Concern ID** R1-m2
    - **Severity** Minor
    - **Axis** Technical soundness
    - **Affected element** Methods section
    - **Evidence pointer** "Modeling of RGG1 and RGG2 stretches"
    - **Issue** The method for modeling the RGG domains by sequential addition of fragments is described, but the rationale for this approach is not fully explained. The authors state that the RGG domains are added in fragments to avoid biases, but it is not clear what biases they are referring to. The potential limitations of this approach are not discussed.
    - **Required correction** The authors should provide a more detailed justification for the fragment-based modeling approach and discuss its potential limitations. They should also describe how they ensured that the final modeled structures are not dependent on the order or details of the fragment addition.

    - **Concern ID** R1-m3
    - **Severity** Minor
    - **Axis** Technical soundness
    - **Affected element** Results section
    - **Evidence pointer** "Electrostatically dominant RGG2–RNA interaction is modulated by the number of RGG repeats"
    - **Issue** The authors state that the FUS380 complex shows a maximum of two hydrogen bonds, FUS385 shows two additional, and FUS390 shows about eight. This is presented as a key result, but the statistical significance of these differences is not assessed. It is not clear if these differences are consistent across the three replicates.
    - **Required correction** The authors should provide the standard deviation or standard error for the hydrogen bond counts and perform a statistical test to determine if the differences between the constructs are significant.

    - **Concern ID** R1-m4
    - **Severity** Minor
    - **Axis** Readability for nonspecialists
    - **Affected element** Results section
    - **Evidence pointer** "FUS-RRM requires RNA sequence/shape specificity to initiate RNA binding"
    - **Issue** The term "NYNY motif" is used without a clear explanation of what it means. The authors mention that Y = C/U and N = A/G/C/U, but this is not explained in a way that is accessible to a general reader.
    - **Required correction** The authors should provide a brief explanation of the NYNY motif and its significance for RNA recognition.

    - **Concern ID** R1-m5
    - **Severity** Minor
    - **Axis** Technical soundness
    - **Affected element** Results section
    - **Evidence pointer** "Force fields and sampling considerations for simulations of IDP–RNA complexes"
    - **Issue** The authors discuss the choice of force field and acknowledge the limitations of their sampling. However, they do not provide a quantitative measure of convergence. The statement that "three qualitatively similar behaving trajectories provides substantial information" is vague.
    - **Required correction** The authors should provide a more quantitative assessment of convergence, such as block averaging or a comparison of the results from different time windows.

- **Technical failings that need to be addressed before the case is established**
    - R1-M1: The central claim about the critical role of boundary residues is not supported by a robust quantitative comparison of the core RRM and the longer RRM constructs.
    - R1-M2: The claim that the number of RGG repeats modulates binding affinity is not supported by a direct measure of binding free energy.
    - R1-M3: The stability and functional role of the helical structure of the boundary residues are not directly analyzed.
    - R1-M4: The claim about the compensatory role of RGG domains in the context of RNA sequence mutations is not supported by quantitative binding affinity calculations.

## Risk / unsupported claims
- The claim that the core RRM (276–368 AA) is insufficient for RNA binding is not robustly supported, as it is based on a single dissociation event in a simulation of a truncated construct.
- The claim that the boundary residues (369–377 AA) are "critical" for RNA binding is not supported by a quantitative comparison of binding stability between the core RRM and the longer RRM.
- The claim that the number of RGG repeats modulates binding affinity is not supported by direct binding free energy calculations.
- The claim that glycine residues in the G-rich region of RGG2 contribute to binding via weak hydrophobic interactions is not supported by a quantitative analysis of their energetic contribution.
- The claim that the RGG domains can compensate for the loss of RNA sequence specificity is not supported by quantitative binding affinity measurements.
- The overall conclusion that the study provides "atomic resolution insights" into FUS-RNA interactions is not fully supported, as the analysis relies heavily on qualitative visual inspection and distance-based metrics, and the statistical robustness of the results is not established.