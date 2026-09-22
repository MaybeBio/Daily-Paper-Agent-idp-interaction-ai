## Review setup
- **Input scope** Full manuscript text (abstract, introduction, materials and methods, results and discussion, conflicts of interest, acknowledgments)
- **Assessment boundary** Resonance assignment completeness, secondary structure inferences, validation strategy, and consistency of claims with presented data
- **Shared manuscript claim summary** The authors report near-complete 1H, 13C, and 15N backbone and partial side chain resonance assignments for full-length SARS-CoV-2 nsp1 at pH 7.5, validated using two mutants and MUSIC-type experiments. They infer secondary structure in solution, report discrepancies with the X-ray structure (notably absence of the β5 strand), and propose intramolecular interactions between folded and disordered domains.
- **Visible evidence base** Text descriptions of NMR experiments, assignment statistics, TALOS+ predictions, CSP analyses, NOE observations, and reference to deposited BMRB accession 50915. Figures and tables are referenced but not provided in the supplied material.
- **Missing materials affecting confidence** Figures 1-3, Table 1, BMRB deposition contents, chemical shift lists, and experimental NMR spectra are not available for direct inspection. This limits verification of assignment quality, peak counts, and spectral overlap claims.

## Reviewer
- **Overall assessment** This manuscript reports a technically demanding NMR assignment of a 19.8 kDa protein containing both folded and disordered regions, which is a nontrivial achievement. The use of two mutants and MUSIC experiments for validation is thoughtful. However, the manuscript is presented as a resource paper, and the central claims regarding secondary structure differences and intramolecular interactions rest on interpretations that cannot be fully verified from the text alone. The writing is generally clear but contains some imprecise statements and overreach relative to the data shown. The work is likely to be useful to the SARS-CoV-2 structural biology community, but the case for the more interpretive conclusions is not fully established from the provided evidence.
- **Who would be interested in the results, and why** Structural biologists studying SARS-CoV-2 nsp1, NMR spectroscopists working on proteins with mixed folded/disordered architecture, and researchers investigating nsp1 function in viral replication and host translation shutoff. The assignment provides a foundation for interaction studies with ribosomes, RNA, and host factors, and for drug discovery efforts targeting nsp1.
- **Major strengths** 1) The assignment of a full-length protein with both folded and disordered domains at near-physiological pH is technically challenging and valuable. 2) The validation strategy using two rationally chosen mutants and MUSIC experiments is rigorous and appropriate for resolving ambiguities. 3) The comparison between solution NMR-derived secondary structure and X-ray structure highlights potentially important conformational differences. 4) The deposition of chemical shifts in BMRB enables community use.
- **Major Concerns** 
  - R1-M1
  - R1-M2
  - R1-M3
  - R1-M4
- **Minor Comments** 
  - R1-m1
  - R1-m2
  - R1-m3
  - R1-m4
  - R1-m5
- **Technical failings that need to be addressed before the case is established** R1-M1 (completeness claim), R1-M2 (β5 strand inference), R1-M3 (intramolecular interaction claim), R1-M4 (mutant validation scope)
- **Assessment against Nature-style criteria** Originality: The assignment itself is not conceptually novel but is valuable as a resource; the secondary structure discrepancies and interaction proposal add interpretive interest. Scientific importance: Moderate to high for the SARS-CoV-2 field, as nsp1 is a key virulence factor and structural data in solution are limited. Interdisciplinary readership: Primarily NMR spectroscopists and virologists; broader interest is limited by the specialized nature of the report. Technical soundness: The experimental approach is sound in principle, but verification is limited by missing figures and tables; some claims exceed what can be supported from the text. Readability for nonspecialists: The manuscript is accessible to structural biologists but assumes familiarity with NMR terminology; some sections are dense and could be clarified.
- **Recommendation posture** Supportive if technical concerns are resolved, particularly regarding completeness quantification, β5 strand evidence, and tempering of the intramolecular interaction claim.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Completeness and accuracy of assignment statistics
- **Claim pointer** The authors state "For the folded domain (aa 14-125) we assigned 95% 1HN and 95% 15N including prolines, 96% of 13Cα, 88% of 13Cβ, 94% of 13C' and 83% of all Hα. For the two disordered fragments (aa 1-13 and aa 126-180) we assigned 91% 1HN, 91% 15N, 93% of 13Cα, 93% of 13Cβ, 94% of 13C' and 76% of all Hα."
- **Evidence pointer** Results and discussion, Assignment protocol section; location not provided
- **Concern** The completeness percentages are presented without specifying the denominators. It is unclear whether prolines are included in the 15N counts, how many residues were unassigned in each region, and whether the percentages refer to unique assignments or include redundant observations. The statement "including prolines" is ambiguous because prolines lack amide protons, so their inclusion in 1HN and 15N counts is not meaningful. Additionally, the authors do not report which specific residues remain unassigned, which is critical for users of the BMRB deposition. Without this information, the completeness claim cannot be independently assessed.
- **Why it matters** Assignment completeness is the primary deliverable of this manuscript. Users need to know exactly which residues are reliably assigned and which are missing to plan downstream experiments. Ambiguous statistics undermine the utility of the resource.
- **Resolution test** Provide a residue-by-residue assignment table or a clear statement of unassigned residues per region, with explicit definitions of the denominators used for each percentage. Clarify how prolines are treated in each count.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Secondary structure inference for β5 strand
- **Claim pointer** The authors state "the presence of β5-strand folded between aa 95 and 97 could not be confirmed" and that "amide protons between residues I95 and G98 were not observed at 308K and 298K, suggesting their involvement in multiple conformational exchange and exposure to the solvent."
- **Evidence pointer** Results and discussion, Secondary structure section; location not provided
- **Concern** The absence of amide proton signals for residues I95-G98 is interpreted as evidence against the β5 strand. However, missing signals could also result from fast solvent exchange, intermediate timescale dynamics, or technical limitations, none of which directly disprove the presence of a transient or weakly populated β-strand. The authors also state that NOE contacts between β4 and β5 were not observed, but do not specify which NOEs were searched for or whether the absence is statistically meaningful given the missing backbone signals. The conclusion that the β5 strand is absent in solution is stronger than the evidence supports.
- **Why it matters** The β5 strand has been proposed as a distinguishing feature of SARS-CoV-2 nsp1 relative to SARS-CoV-1. If the claim is incorrect or overstated, it could mislead downstream structural and functional interpretations.
- **Resolution test** Provide a more nuanced interpretation, such as "the β5 strand is not stably populated under our conditions" or "the data are consistent with a dynamic or partially populated β5 region." Include a discussion of alternative explanations for missing signals and, if possible, show representative spectral regions or relaxation data supporting the dynamics interpretation.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Intramolecular interaction claim
- **Claim pointer** The authors state "we propose that in the full-length SARS-CoV-2 nsp1, the folded and disordered parts of the protein behave not as fully independent units but are rather involved in intramolecular interactions."
- **Evidence pointer** Results and discussion, Secondary structure section; location not provided
- **Concern** This proposal is presented as a conclusion but is supported only by indirect evidence: differences in order parameters and signal intensities between disordered regions. No direct evidence for intramolecular contacts, such as intermolecular NOEs between folded and disordered regions, concentration-dependent chemical shift changes, or relaxation dispersion data, is presented. The claim is speculative and should be clearly framed as a hypothesis requiring further testing.
- **Why it matters** The interaction proposal is one of the more biologically interesting claims in the manuscript. If it is not supported by direct evidence, it should not be stated as a finding, as it could be cited inappropriately by others.
- **Resolution test** Reframe the statement as a hypothesis and explicitly state what additional experiments would be needed to test it. Alternatively, provide direct evidence for intramolecular contacts if available.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Mutant validation scope
- **Claim pointer** The authors state "Validation of assignment have been done by using two different mutants, H81P and K129E/D48E as well as by amino acid specific experiments."
- **Evidence pointer** Results and discussion, Assignment protocol section; location not provided
- **Concern** The manuscript does not describe how the mutants were used for validation in sufficient detail. It is unclear whether the mutants were assigned independently or only used to confirm specific resonances. The CSP data shown in Figure 3d are described qualitatively, but the criteria for "significant" CSP are not defined. The statement that mutant data "helped to resolve some ambiguities" is vague.
- **Why it matters** The validation strategy is a key strength of the manuscript, but the lack of detail prevents readers from assessing its rigor. If the mutants were not fully assigned, their utility for validation is limited.
- **Resolution test** Provide a clear description of the validation workflow, including how mutant spectra were compared to the wild type, which resonances were confirmed or reassigned, and what criteria were used to define significant CSPs.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity of writing
- **Affected element** Abstract and Introduction
- **Evidence pointer** Abstract, Introduction; location not provided
- **Issue** The phrase "flaking N- and C-terminal intrinsically disordered fragments" contains a typo ("flaking" should be "flanking"). Additionally, the abstract states "The 19.8 kD protein was characterized" but the unit should be "kDa" for consistency with standard usage.
- **Required correction** Correct the typo and use "kDa" throughout.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Referencing of deposited data
- **Affected element** Results and discussion, Assignment protocol section
- **Evidence pointer** Results and discussion, Assignment protocol section; location not provided
- **Issue** The BMRB accession number is mentioned, but the manuscript does not state which specific data were deposited (e.g., chemical shift lists for 1H, 13C, 15N, and 13Cβ) or whether the deposition includes both temperatures and all three protein variants.
- **Required correction** Specify the contents of the BMRB deposition and confirm that all reported data are included.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Experimental details
- **Affected element** Materials and Methods, NMR experiments
- **Evidence pointer** Materials and Methods, NMR experiments; location not provided
- **Issue** The manuscript states that experiments were performed at 298 K and 308 K but does not specify which experiments were run at which temperature. This information is relevant for reproducing the assignment strategy.
- **Required correction** Add a table or text specifying the temperature for each experiment type.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Figure accessibility
- **Affected element** Figures 1-3
- **Evidence pointer** Figures 1-3; location not provided
- **Issue** The figures are referenced extensively but are not available in the supplied material. The text descriptions are insufficient to evaluate the quality of the spectra, the CSP plots, or the TALOS+ predictions.
- **Required correction** Ensure figures are included in any revised submission and that they are legible at publication resolution.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Terminology consistency
- **Affected element** Results and discussion, Secondary structure section
- **Evidence pointer** Results and discussion, Secondary structure section; location not provided
- **Issue** The terms "disordered" and "unstructured" are used interchangeably. While this is common, the manuscript should define what is meant by these terms in the context of the NMR data, particularly given the proposal of intramolecular interactions.
- **Required correction** Add a brief definition or clarification of how disorder is assessed from the NMR data.

## Risk / unsupported claims
- The claim that the β5 strand is absent in solution is not fully supported by the presented evidence, as missing backbone signals could have multiple explanations.
- The proposal of intramolecular interactions between folded and disordered domains is speculative and not directly evidenced.
- The completeness percentages for resonance assignments cannot be independently verified without a residue-level breakdown.
- The statement that "the secondary structure of the folded domain in solution was almost identical to its previously published X-ray structure" is presented as a conclusion, but the supporting TALOS+ data are not shown in the supplied material.
- The claim that the two mutants "helped to resolve some ambiguities" is not substantiated with specific examples or criteria.