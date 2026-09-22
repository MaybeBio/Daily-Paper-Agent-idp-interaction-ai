## Review setup
- **Input scope** Full manuscript text (abstract, introduction, results, discussion, methods, supplementary figure legends)
- **Assessment boundary** Scientific claims, methodological soundness, evidence consistency, and alignment with stated conclusions
- **Shared manuscript claim summary** The authors identify and characterize four partially cryptic druggable pockets in the Nsp1 N-terminal domain of SARS-CoV-2 using molecular dynamics, enhanced sampling (SWISH), solvent mapping, and X-ray crystallography. One pocket (pocket 1) is validated by a fragment-bound crystal structure. The authors further propose that ligand binding to pocket 1 can disrupt the Nsp1-RNA interaction and that the pockets are conserved across β-coronavirus homologues.
- **Visible evidence base** Results and discussion sections, methods, figure legends (Figures 1-9 and associated supplements), crystallographic data summary, phylogenetic analysis
- **Missing materials affecting confidence** Coordinates and electron density maps for the fragment-bound structure are not provided; crystallographic refinement statistics are only summarized in a supplement table not fully described; no PDB accession codes are given; the fragment screening details (concentrations, soaking times, hit rates) are incomplete; the computational fragment screening method is not described in the methods section; no negative control experiments for the MST binding assay are reported

## Reviewer
- **Overall assessment** This manuscript presents a multidisciplinary approach to identify cryptic pockets in SARS-CoV-2 Nsp1, a target of high biomedical relevance. The computational workflow combining unbiased MD, SWISH enhanced sampling, and fragment mapping is well conceived and the identification of a crystallographically validated pocket is a meaningful advance. However, the evidence linking pocket binding to functional disruption of the Nsp1-RNA complex is indirect and based on modeling rather than direct experimental demonstration. The conservation analysis across homologues is limited by sequence identity considerations and the phylogenetic framing is underdeveloped. The crystallographic validation, while encouraging, rests on a single weak-affinity fragment and the authors themselves note that crystal packing occludes most predicted pockets, which raises questions about the generalizability of the experimental validation. The manuscript would be strengthened by direct binding data for the fragment, functional assays linking pocket occupancy to RNA displacement, and a more rigorous treatment of the conservation claims.
- **Who would be interested in the results, and why** Structural biologists and computational chemists working on cryptic pocket discovery will find the SWISH-based methodology and its integration with crystallographic fragment screening of interest. Antiviral drug discovery groups focused on SARS-CoV-2 and broader coronavirus preparedness will be interested in the identification of a potentially druggable pocket in Nsp1, particularly given the limited structural information on this protein. The work may also appeal to researchers studying protein-RNA interfaces as therapeutic targets, though the functional evidence here is preliminary.
- **Major Strengths** The combination of multiple computational methods (unbiased MD, SWISH, FTMap/FTDyn) with experimental crystallographic validation is a rigorous approach to a challenging problem. The identification of a partially cryptic pocket that is confirmed by a fragment-bound crystal structure provides a concrete starting point for drug design. The authors are appropriately cautious about the limitations imposed by crystal packing on fragment screening. The potential functional relevance of pocket 1, located near the RNA binding interface, is biologically plausible and well reasoned.
- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence strength for functional claim
- **Claim pointer** The authors state that "the binding of a ligand in this pocket could also interfere with the interaction with SL1 of viral RNA, leading to the failure in evasion of translation shutdown and cleavage of viral RNA" and later conclude that fragments bound to these pockets "can disrupt the Nsp1-RNA complex."
- **Evidence pointer** Results section "Disrupting Nsp1-RNA complex by means of cryptic pockets", Figure 8
- **Concern** The functional claim that pocket 1 ligands can disrupt the Nsp1-RNA complex is supported only by a structural superposition of the fragment-bound Nsp1 structure onto a modeled Nsp1-RNA complex. No experimental data demonstrate that fragment binding reduces RNA affinity or displaces RNA. The modeled RNA complex itself is based on docking without experimental validation, and the authors acknowledge that they cannot distinguish between two alternative binding models. The argument that residue rearrangements upon fragment binding would preclude RNA interaction is speculative, as the fragment is small (172.9 Da) and the observed conformational changes are not quantified.
- **Why it matters** The stated therapeutic rationale for targeting Nsp1 depends on the ability of small molecules to disrupt its RNA binding function. Without direct evidence of functional interference, the translational significance of the identified pockets remains unsubstantiated. The conclusion as written overstates what the data can support.
- **Resolution test** Provide experimental evidence that fragment 2E10 or a close analog reduces Nsp1-RNA binding in a biochemical assay (e.g., electrophoretic mobility shift, fluorescence polarization, or surface plasmon resonance). Alternatively, demonstrate in a cellular or translation assay that fragment treatment relieves Nsp1-mediated translation suppression. If such experiments are not feasible, the claims should be revised to state that pocket 1 is proximal to the RNA interface and that this proximity is suggestive but not demonstrative of functional relevance.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Crystallographic validation completeness
- **Claim pointer** The authors state that "the results of fragment-based screening via X-ray crystallography confirm the druggability of the major pocket of Nsp1" and that the presented structures are "the first fragment-bound SARS-CoV-2 Nsp1 crystal structures to date."
- **Evidence pointer** Results section "Crystallographic confirmation of Nsp1 cryptic pockets", Figure 6, Figure 6-Table supplement 1
- **Concern** The crystallographic evidence is presented without sufficient detail to assess its quality. No PDB accession codes are provided, the resolution of the fragment-bound structure is not stated in the main text, and the refinement statistics are only referenced in a supplement table that is not described in the visible material. The occupancy of the fragment, B-factors, and the quality of the electron density for the ligand are not discussed. The authors note that only one fragment bound out of 60 tested, and they attribute the low hit rate to crystal packing, but this explanation is not experimentally verified. The claim of "confirming druggability" based on a single weak-affinity fragment (Kd in the millimolar range) requires more careful qualification.
- **Why it matters** The crystallographic validation is the central experimental pillar of the manuscript. If the structural evidence is not presented to a standard that allows independent assessment, the claim of druggability is not established. The lack of deposited coordinates prevents the community from using this structure for follow-up work.
- **Resolution test** Deposit the coordinates and structure factors in the PDB and provide the accession codes. Report the resolution, R-factors, ligand occupancy, and B-factors in the main text or a fully described supplement table. If the electron density for the fragment is ambiguous, state this explicitly and temper the druggability claim accordingly.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Conservation claim support
- **Claim pointer** The authors state that "the pockets are conserved across multiple coronavirus species" and suggest that "ligands binding to any of the pockets identified in Nsp1 N of SARS-CoV-2, could also target the corresponding pocket in the evaluated homologues."
- **Evidence pointer** Results section "The conservation of Nsp1 in different CoV genera", Figure 9
- **Concern** The conservation analysis is based on sequence identity (86-93%) and SWISH simulations of three homologues, but the presentation is incomplete. The phylogenetic tree in Figure 9A is described but not shown in the visible material. The sequence alignment in Figure 9-Table supplement 1 is referenced but not provided. The SWISH simulations for homologues are stated to show conserved pockets, but no quantitative comparison of pocket volumes, residue identities, or structural alignments is presented. Sequence identity in the range of 86-93% does not guarantee structural conservation of a specific pocket, particularly for partially cryptic sites that require conformational rearrangements to open.
- **Why it matters** The claim of cross-coronavirus applicability is important for the broader impact of the work, as it underpins the suggestion that a single drug could target multiple β-coronaviruses. If the conservation evidence is not rigorously presented, this claim is not supported.
- **Resolution test** Provide the phylogenetic tree and sequence alignment as main or supplementary figures. Present a quantitative comparison of pocket volumes, key residue identities, and structural superposition metrics for the four Nsp1 homologues. If the pockets are not fully conserved in all homologues, specify which pockets are conserved in which species and adjust the claims accordingly.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Crypticity claim robustness
- **Claim pointer** The authors state that pockets 3 and 4 are "cryptic" based on their absence in the crystal structure and their opening during SWISM simulations, and that pocket 1 is "partially cryptic" based on volume differences between crystal structure and simulations.
- **Evidence pointer** Results sections "Structural assessment of Nsp1 pockets" and "Crypticity assessment of Nsp1 pockets", Figures 3 and 4
- **Concern** The definition of crypticity used here relies on the absence of a pocket in a single crystal structure and its presence in enhanced-sampling simulations. This is a reasonable operational definition, but the evidence for pockets 3 and 4 is based solely on SWISM simulations with benzene as a co-solvent. The authors note that pocket 4 opened in only two of six replicas, which suggests that its identification is not robust. The claim that pocket 1 is "partially cryptic" is based on a volume difference between the crystal structure (217 Å³) and MD simulations (410 ± 150 Å³), but the large standard deviation in the simulation value and the different residue sets identified in each case make this comparison difficult to interpret. No free energy calculations or quantitative measures of pocket opening probability are provided.
- **Why it matters** The crypticity of the pockets is a central conceptual claim of the manuscript and is used to justify the enhanced-sampling approach. If the crypticity classification is not robust, the methodological novelty and the interpretation of the fragment screening results are weakened.
- **Resolution test** Provide quantitative measures of pocket opening probability or free energy profiles for pocket opening from the SWISM simulations. Report the fraction of simulation time each pocket is open across all replicas. For pocket 1, compare the residue composition of the pocket in the crystal structure versus simulations and discuss whether the volume difference reflects genuine conformational change or methodological differences in pocket detection.

- **Concern ID** R1-M5
- **Severity** Major
- **Blocking** No
- **Axis** Computational screening methodology transparency
- **Claim pointer** The authors state that 60 fragment hits "obtained by computational methods" were tested experimentally, and that the fragment 2E10 was found in pocket 1.
- **Evidence pointer** Results section "Crystallographic confirmation of Nsp1 cryptic pockets", Methods section
- **Concern** The computational fragment screening method used to select the 60 fragments is not described anywhere in the methods. The reader cannot assess the quality of the screening, the criteria for fragment selection, or whether the screening was biased toward particular chemotypes. The authors mention "virtual screening" in the introduction but provide no details on the docking software, scoring functions, or validation of the screening protocol.
- **Why it matters** The selection of fragments for experimental testing is a critical step in the workflow. Without transparency on the computational screening methodology, the reproducibility of the work is compromised and the significance of obtaining one hit out of 60 is difficult to interpret.
- **Resolution test** Add a subsection to the methods describing the virtual screening protocol, including the software used, the fragment library composition, the docking and scoring procedures, and the criteria for selecting the 60 fragments for experimental testing.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity of figure presentation
- **Affected element** Figure 9A and Figure 9-Table supplement 1
- **Evidence pointer** Results section "The conservation of Nsp1 in different CoV genera"
- **Issue** The phylogenetic tree and sequence alignment are referenced but not visible in the provided material, making it impossible to assess the conservation analysis.
- **Required correction** Ensure that Figure 9A and Figure 9-Table supplement 1 are included as actual figures or tables in the manuscript, with clear labels and legends.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Binding affinity data presentation
- **Affected element** MST binding assay for fragment 2E10
- **Evidence pointer** Results section "Crystallographic confirmation of Nsp1 cryptic pockets"
- **Issue** The Kd value of 2.74 ± 2.63 mM is reported without details on the experimental conditions, the number of replicates, or the quality of the binding curve. The large error relative to the Kd value suggests weak or poorly characterized binding.
- **Required correction** Provide the MST experimental details, including the number of independent measurements, the fitting procedure, and a representative binding curve. Discuss the limitations of a millimolar Kd for a fragment and what this implies for the druggability assessment.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Terminology precision
- **Affected element** Use of "druggable" throughout the manuscript
- **Evidence pointer** Abstract, Results, Conclusions
- **Issue** The term "druggable" is used to describe pockets based on computational predictions and a single weak-affinity fragment. Druggability typically implies the potential for a pocket to bind drug-like molecules with sufficient affinity and selectivity, which is not demonstrated here.
- **Required correction** Consider using "potentially druggable" or "targetable" in place of "druggable" where the evidence is based on computational predictions or weak fragment binding, and reserve "druggable" for cases where more substantial evidence exists.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Reference completeness
- **Affected element** Crystallization methods
- **Evidence pointer** Methods section "Crystallographic data"
- **Issue** The crystallization protocol is referenced as "previously described (add ref)" with a placeholder, which is not acceptable for a manuscript intended for public dissemination.
- **Required correction** Provide the full citation for the crystallization protocol or describe the method in sufficient detail in the current manuscript.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Statistical treatment of simulation data
- **Affected element** Pocket volume analysis
- **Evidence pointer** Results sections "Structural assessment of Nsp1 pockets" and "Crypticity assessment of Nsp1 pockets"
- **Issue** Pocket volumes are reported as averages with standard deviations, but the number of independent samples and the autocorrelation time of the volume time series are not reported. This makes it difficult to assess the statistical significance of differences between conditions.
- **Required correction** Report the effective number of independent samples for each volume estimate, or provide the volume time series as supplementary data so that readers can assess the statistical robustness of the comparisons.

- **Concern ID** R1-m6
- **Severity** Minor
- **Axis** Figure quality
- **Affected element** Figure 7
- **Evidence pointer** Results section "Crystallographic confirmation of Nsp1 cryptic pockets"
- **Issue** The description of Figure 7 indicates that crystal packing contacts occlude the predicted pockets, but the figure itself is not visible in the provided material. This is a key point for interpreting the low fragment hit rate.
- **Required correction** Ensure that Figure 7 is included with sufficient resolution to visualize the crystal packing contacts and the spatial relationship between neighboring molecules and the predicted pockets.

## Risk / unsupported claims
- The claim that fragment binding to pocket 1 "could disrupt the Nsp1-RNA complex" is unsupported by direct experimental evidence; it is inferred from structural superposition of a modeled complex.
- The claim that the identified pockets are "conserved across multiple coronavirus species" is not fully supported by the visible evidence, as the phylogenetic tree, sequence alignment, and quantitative pocket comparisons are not provided.
- The claim that the presented structures are "the first fragment-bound SARS-CoV-2 Nsp1 crystal structures to date" cannot be independently verified without PDB accession codes and a literature search context.
- The druggability of pockets 3 and 4 is based solely on computational predictions from SWISM simulations with no experimental validation, and pocket 4 opened in only two of six replicas, making its identification uncertain.
- The statement that "the crucial information arising from our multidisciplinary approach can provide a solid foundation for the rational drug discovery of new inhibitors" overstates the current evidence, as no functional or cellular data support the therapeutic relevance of the identified pockets.