## Review setup

- **Input scope** Full manuscript text, including abstract, introduction, results and discussion, experimental methods, and supplementary material references.
- **Assessment boundary** Scientific content, methodological rigor, validity of claims relative to the evidence presented, and clarity of presentation. No assessment of editorial fit or journal policy.
- **Shared manuscript claim summary** The authors present the first full-length model of the c-Myc/Max heterodimer and use Gaussian-accelerated molecular dynamics (GaMD) simulations to characterize the conformational behavior of c-Myc in three states: monomeric, Max-bound, and post-Max-removal. They report that Max binding stabilizes the bHLH-Zipper motif, that the TAD region remains highly plastic, that electrostatic interactions dominate the c-Myc/Max interface with key residues Arg299, Ile403, and Leu420, and that three potential drug binding pockets exist within c-Myc.
- **Visible evidence base** RMSD, radius of gyration, RMSF, free-energy landscape analyses, MM-PBSA calculations, hydrogen bond analysis, α-helix counts, and P2Rank binding pocket predictions. Figures referenced include Figures 2–11 and Supplementary Figures S2–S8. Tables 1 and 2 are referenced.
- **Missing materials affecting confidence** The manuscript text was provided without figures, tables, or supplementary material. Numerical values for MM-PBSA energy components (Table 1) and P2Rank scores (Table 2) are not visible. Simulation convergence criteria, force field validation details, and reweighting procedures for GaMP are described only briefly. No trajectory validation metrics (e.g., potential energy drift, equilibration checks) are shown.

## Reviewer

- **Overall assessment** The manuscript addresses a relevant and challenging topic: the conformational behavior of the intrinsically disordered protein c-Myc and its modulation by the binding partner Max. The use of GaMD to enhance sampling of an IDP is appropriate and timely. The authors present a novel full-length c-Myc/Max heterodimer model, which is a useful contribution. However, the evidence as presented is insufficient to fully support several key claims. The analysis relies heavily on descriptive metrics (RMSD, RGyr, RMSF) without clear statistical treatment across replicates, and the connection between simulation observations and biological function is largely speculative. The MM-PBSA and binding pocket analyses are potentially valuable but cannot be fully assessed without the corresponding tables and figures. The manuscript would benefit from more rigorous quantitative comparisons, explicit convergence assessments, and a clearer articulation of what is novel relative to prior c-Myc simulation studies.

- **Who would be interested in the results, and why** Researchers in the fields of intrinsically disordered proteins, transcription factor biology, and computational drug discovery would find this work of interest. The full-length c-Myc/Max heterodimer model could serve as a starting point for future simulation studies. The identification of potential binding pockets within c-Myc may inform structure-based drug design efforts targeting this challenging protein. The methodological approach, combining GaMD with MM-PBSA and pocket prediction, is transferable to other IDP systems.

- **Major strengths** The study addresses a biologically important and technically challenging target. The use of GaMD is well justified for IDP systems. The construction of a full-length c-Myc/Max heterodimer model fills a gap in the literature. The multi-pronged analytical approach (dynamics, energetics, structure prediction) is comprehensive. The authors are appropriately cautious in some interpretations, acknowledging the speculative nature of links to biological function.

- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors claim that "the monomeric c-Myc structure showed a higher RMSD fluctuation as compared with the c-Myc/Max heterodimer in the bHLH-Zipper motif," indicating that Max binding stabilizes this motif.
- **Evidence pointer** Figure 2a, Section "Max Protein Stabilizes the bHLH-Zipper Motif of c-Myc"
- **Concern** The claim of differential stability between monomeric and Max-bound states is based on average RMSD values across three replicates. However, no statistical analysis (e.g., standard deviations, confidence intervals, or significance testing) is presented. Replicate 1 of the monomer shows an average RMSD of 6.13 Å, while replicates 2 and 3 show 3.85 and 3.77 Å, respectively. This large inter-replicate variability suggests that the monomeric state may not have converged, and the difference between monomeric and Max-bound states may not be robust. Without error bars or statistical comparison, the claim of stabilization by Max is not quantitatively supported.
- **Why it matters** The central conclusion of the paper, that Max binding stabilizes the bHLH-Zipper motif, rests on this comparison. If the difference is not statistically significant or is an artifact of insufficient sampling, the main message of the manuscript is undermined.
- **Resolution test** Provide per-replicate time series and ensemble averages with standard deviations or standard errors. Perform a statistical test (e.g., a two-sample t-test or Mann-Whitney U test) comparing the RMSD distributions of monomeric versus Max-bound states. If convergence is a concern, extend simulations or use block averaging to demonstrate that the observed differences are stable over time.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors state that "the interaction between c-Myc and Max is driven by electrostatic interactions" based on MM-PBSA calculations, with key residues Arg299, Ile403, and Leu420.
- **Evidence pointer** Table 1, Figure 9a–f, Section "MM-PBSA Calculations Revealed That the Interaction between c-Myc and Max Is Driven by Electrostatic Interactions"
- **Concern** The MM-PBSA results are referenced but the actual energy components (electrostatic, van der Waals, polar solvation, nonpolar solvation) are not visible in the provided text. The claim that electrostatic interactions dominate cannot be verified without seeing the numerical breakdown. Furthermore, the per-residue decomposition identifies Arg299, Ile403, and Leu420 as key contributors, but the text states that "all residues that show high contributions (<−3 kcal/mol) in all three replicates are charged residues," which is contradictory because Ile403 and Leu420 are hydrophobic. This inconsistency needs clarification. Additionally, MM-PBSA is known to be sensitive to the choice of solute dielectric constant and radii; no sensitivity analysis is mentioned.
- **Why it matters** The energetic driving force of the c-Myc/Max interaction is a key finding with implications for drug design. If the electrostatic dominance claim is not robustly supported, or if the residue-level analysis is internally inconsistent, the conclusion is weakened.
- **Resolution test** Show the full MM-PBSA energy decomposition table with all components and standard errors. Clarify the residue classification and reconcile the statement about charged residues with the identification of Ile403 and Leu420. Perform a sensitivity analysis with different dielectric constants or radii sets to demonstrate robustness.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors claim that "three potential drug binding pockets were identified within c-Myc" with "good pocket and probability scores."
- **Evidence pointer** Table 2, Figure 11a–c, Section "Three Potential Drug Binding Pockets Were Identified within c-Myc in Conformation 1, Conformation 3, and Conformation 4"
- **Concern** The P2Rank results are referenced but the actual scores are not visible. The claim of "good" scores cannot be evaluated without knowing the numerical values and how they compare to known druggable pockets in other proteins. Moreover, the authors note that conformation 2 did not show potential binding pockets, which raises the question of whether the identified pockets are stable features of c-Myc or artifacts of specific conformational states. The functional relevance of these pockets is not demonstrated; the authors only note that they include residues known to bind small molecules, but no validation (e.g., docking, comparison to known binding sites) is provided.
- **Why it matters** The identification of druggable pockets is a central motivation for the study. If the pockets are not robust across conformations or are not validated as druggable, the practical utility of the findings is limited.
- **Resolution test** Provide the P2Rank scores for all identified pockets and compare them to scores for known druggable proteins. Assess pocket stability across the simulation trajectories. If possible, perform docking of known c-Myc inhibitors into the predicted pockets to validate their potential druggability.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Reproducibility
- **Claim pointer** The authors state that "we performed 0.5 μs long all-atom GaMD simulations in triplicate" and that the force field and water model combination "had previously shown to improve atomistic simulations of IDPs."
- **Evidence pointer** Section "GaMD Simulations", Section "MD Simulations"
- **Concern** The description of the simulation protocol is incomplete. The GaMD implementation details (e.g., the specific GaMD module used, the threshold for applying the boost potential, the frequency of boost updates) are not provided. The equilibration protocol is described for cMD but not for GaMD. The criteria for determining that the system was equilibrated before production are not stated. The reference for the force field/water model combination is cited as reference 32, but the specific improvement claimed is not described.
- **Why it matters** Reproducibility is a core requirement for computational studies. Without a complete description of the simulation parameters and convergence criteria, other researchers cannot replicate the work or assess its reliability.
- **Resolution test** Provide a complete description of the GaMD protocol, including all parameters, the equilibration procedure, and convergence metrics. State the criteria used to determine that the simulations were sufficiently converged for analysis.

- **Concern ID** R1-M5
- **Severity** Major
- **Blocking** No
- **Axis** Scientific importance
- **Claim pointer** The authors claim that "this is the first MD simulation study ever done with the full-length c-Myc and c-Myc/Max heterodimers."
- **Evidence pointer** Abstract, Introduction, Section "Modeling of Full-Length c-Myc and c-Max Heterodimers"
- **Concern** The claim of novelty is strong and should be verified with a thorough literature search. While the authors state that no full-length heterodimer model is available, there may be other simulation studies of c-Myc that include large portions of the protein or use different enhanced sampling methods. The novelty claim should be supported by a more comprehensive literature review.
- **Why it matters** The novelty of the model is a key selling point of the paper. If the claim is overstated, the contribution is diminished.
- **Resolution test** Expand the literature review to include all prior simulation studies of c-Myc, including those using coarse-grained models, enhanced sampling, or partial constructs. Clearly state what is new about the full-length model and the GaMD approach relative to prior work.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Abstract
- **Evidence pointer** Abstract
- **Issue** The abstract states that the TAD region "in both monomeric and Max-bound states showed similar plasticity in terms of RMSD." However, the results section reports that the TAD region "did not stabilize" in either state, which is consistent but the term "similar plasticity" is vague.
- **Required correction** Define "plasticity" quantitatively (e.g., range of RMSD values or variance) and state whether the similarity was tested statistically.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Results section
- **Evidence pointer** Section "Max Protein Stabilizes the bHLH-Zipper Motif of c-Myc"
- **Issue** The text states that "the high RMSD in the bHLH-Zipper motif is largely associated with residues between Gln411 and Ala439." This is a qualitative statement without supporting data.
- **Required correction** Provide per-residue RMSD plots or a quantitative decomposition showing that these residues contribute most to the overall RMSD.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Results section
- **Evidence pointer** Section "Removal of Max Protein from c-Myc Increased the Compactness Significantly in the bHLH-Zipper Motif Than in the TAD Region"
- **Issue** The term "significantly" is used in the section title, but no statistical test is reported for the RGyr comparisons.
- **Required correction** Either perform a statistical test and report the p-value, or rephrase the title to avoid implying statistical significance.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Results section
- **Evidence pointer** Section "Amino Acid Residues from the Disordered Regions of bHLH-Zipper Motif in Monomeric c-Myc Exhibited Higher Fluctuations Than That in Max-Bound c-Myc"
- **Issue** The text states that "the overall RMSF of the TAD region was greater than the bHLH-Zipper motif in the c-Myc/Max heterodimer." This is a comparison across regions, but the biological relevance is not explained.
- **Required correction** Clarify why this comparison is meaningful and what it implies for TAD function.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Conclusions
- **Evidence pointer** Conclusions section
- **Issue** The conclusion states that "we demonstrated two potential druggable pockets in c-Myc when bound to Max and one pocket in c-Myc in the monomeric state." However, the results section describes three pockets total, with the highest scores for conformation 1 (Max-bound), followed by conformation 4 (monomeric) and conformation 3 (Max-bound). The conclusion is ambiguous about which pockets are being counted.
- **Required correction** Clarify the count and specify which conformations correspond to which pockets.

- **Concern ID** R1-m6
- **Severity** Minor
- **Axis** Technical soundness
- **Affected element** Methods
- **Evidence pointer** Section "MD Simulations"
- **Issue** The methods state that "restraints were applied using the SHAKE algorithm." SHAKE is a constraint algorithm, not a restraint method. This is a technical inaccuracy.
- **Required correction** Correct the wording to state that bonds involving hydrogen atoms were constrained using the SHAKE algorithm.

- **Concern ID** R1-m7
- **Severity** Minor
- **Axis** Reproducibility
- **Affected element** Methods
- **Evidence pointer** Section "Analysis"
- **Issue** The analysis section states that "12500 frames from each simulation" were used, but the total number of frames generated is not stated. It is unclear what fraction of the trajectory was analyzed.
- **Required correction** State the total number of frames and the sampling interval, and justify the choice of 12500 frames.

- **Technical failings that need to be addressed before the case is established** R1-M1 (lack of statistical analysis for the central stability claim), R1-M2 (incomplete and internally inconsistent MM-PBSA data), R1-M3 (unverifiable pocket prediction scores and lack of validation), R1-M4 (incomplete simulation protocol description). These issues must be resolved before the main conclusions can be considered robust.

- **Assessment against Nature-style criteria** Originality: The full-length c-Myc/Max heterodimer model is a novel contribution, but the overall approach (GaMD on IDPs) is not new. Scientific importance: The topic is important, but the findings are largely descriptive and the link to drug discovery is speculative. Interdisciplinary readership: The work is primarily of interest to computational biophysicists and structural biologists; the broader cancer biology community may find the implications interesting but the technical content is specialized. Technical soundness: The study has significant technical weaknesses, particularly in statistical treatment and protocol description. Readability for nonspecialists: The manuscript is generally readable, but the results section is dense and would benefit from clearer framing of the biological significance of each analysis.

- **Recommendation posture** Supportive if technical concerns are resolved. The manuscript addresses a relevant problem and presents a useful model, but the current evidence does not robustly support the central claims. The authors should address the statistical analysis, provide complete MM-PBSA and pocket prediction data, and improve the simulation protocol description before the conclusions can be considered established.

## Risk / unsupported claims

- The claim that Max binding stabilizes the bHLH-Zipper motif is not statistically supported due to lack of error analysis and inter-replicate variability.
- The claim that electrostatic interactions dominate the c-Myc/Max interaction is unverifiable without the MM-PBSA energy components table.
- The identification of Arg299, Ile403, and Leu420 as key residues is internally inconsistent with the statement that all high-contribution residues are charged.
- The claim of "good" binding pocket scores is unverifiable without the P2Rank output values.
- The statement that the force field and water model combination "had previously shown to improve atomistic simulations of IDPs" is not substantiated with specific evidence.
- The biological interpretations linking TAD plasticity to protein-protein interactions and bHLH-Zipper stability to protection from ubiquitination are speculative and not directly tested.
- The claim of being the "first MD simulation study ever done with the full-length c-Myc and c-Myc/Max heterodimers" requires a more thorough literature search to verify.