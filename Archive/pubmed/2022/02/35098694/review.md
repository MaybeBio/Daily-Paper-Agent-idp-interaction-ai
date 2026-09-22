## Review setup
- **Input scope** Full manuscript text (abstract, introduction, classification sections, conclusion, and supporting statements) provided without figures, tables, or supplementary materials.
- **Assessment boundary** Assessment is limited to the written content as supplied. Figures, tables, and any associated supplementary data referenced in the text were not available for evaluation.
- **Shared manuscript claim summary** The authors propose a structural classification system for intrinsically disordered protein regions (IDRs) that bind RNA, based on a survey of 24 experimentally determined complexes from the Protein Data Bank. They identify two major binding modes (alpha-helical and turn/loop) and use molecular dynamics simulations to support their proposed structural preferences. They also compare RNA-binding IDRs with DNA-binding disordered proteins and discuss small-molecule RNA ligands.
- **Visible evidence base** The manuscript text describes a PDB survey (24 complexes), references to specific structures (e.g., FMRP, FUS, Tat-TAR, nucleolin, RBMY), and two illustrative modeling examples (RBMX-WECcore and LUC7L3). No figures, tables, or simulation details are visible in the provided material.
- **Missing materials affecting confidence** Figures 1–8, Table 1, simulation parameters and trajectories, PDB accession codes, and any quantitative binding or stability data are not provided. These are essential for verifying the classification scheme, the modeling results, and the atomic-level interaction claims.

## Reviewer
- **Overall assessment** This manuscript addresses a timely and important topic: the structural basis of RNA recognition by intrinsically disordered protein regions. The authors have identified a genuine gap in the literature, as most structural studies of RNA-protein interactions focus on folded domains. The proposed classification into alpha-helical and turn/loop binding modes is conceptually useful and likely to be of interest to the RNA biology and structural biology communities. However, the evidence base as presented is thin. The classification rests on only 24 complexes, and the manuscript does not provide sufficient quantitative or comparative analysis to establish the robustness of the proposed categories. The molecular dynamics simulations are described only in passing, with no methodological detail or validation. The comparison with DNA-binding disordered proteins is qualitative and somewhat superficial. The manuscript reads more as a perspective or hypothesis-generating review than a definitive structural analysis. The writing is generally clear, but the lack of access to figures and tables makes it impossible to assess the quality of the visual evidence. The claims about atomic-level interactions and the role of specific residues would be strengthened by direct reference to structural data, which is not visible here.

- **Who would be interested in the results, and why** Researchers studying RNA-protein interactions, particularly those interested in the role of disordered regions in RNA recognition, will find this manuscript relevant. The proposed classification system could serve as a framework for future studies. The discussion of RGG motifs and their role in phase separation and disease will appeal to investigators working on RNA granules, stress responses, and neurodegeneration. The comparison with DNA-binding IDRs may interest researchers studying transcription regulation. The brief discussion of small-molecule RNA ligands could attract medicinal chemists, though this section is underdeveloped.

- **Major strengths** The manuscript identifies a real gap in structural knowledge and proposes a simple, memorable classification. The emphasis on structural features rather than sequence motifs is a useful corrective to sequence-centric views. The discussion of the physicochemical basis of IDR-RNA interactions, particularly the role of arginine, is insightful. The inclusion of disease-relevant examples (ALS, FUS, TAT) adds translational relevance. The authors are appropriately cautious about the limited number of available structures.

- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence sufficiency
- **Claim pointer** The manuscript claims to have conducted a "comprehensive search" of the PDB and identified 24 complexes of IDRs bound to RNA, from which two major structural classes are derived.
- **Evidence pointer** Section "Classification of disordered RNA binding regions"; Table 1 (not visible); Figure 1 (not visible)
- **Concern** The search methodology is not described. No search terms, inclusion criteria, or filtering steps are provided. It is unclear whether the 24 complexes represent a complete census or a curated subset. The classification into two major modes is based on this small set, and the manuscript does not report how many complexes fall into each category, whether there are outliers, or how robust the categories are. Without this information, the classification cannot be evaluated for completeness or bias.
- **Why it matters** The central contribution of the manuscript is the classification system. If the underlying dataset is incomplete or unrepresentative, the classification may be misleading. A "comprehensive search" claim requires a transparent and reproducible methodology.
- **Resolution test** Provide a detailed description of the PDB search strategy, including search terms, filters, and manual curation steps. Report the number of complexes in each class, list any excluded structures with reasons, and discuss potential biases in the dataset.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The manuscript states that molecular dynamics simulations were integrated into the study and that their results "support the proposed structural preferences of specific RNA-binding IDRs."
- **Evidence pointer** Section "Modeling of RNA-protein complexes complements our knowledge"; Figure 3 (not visible)
- **Concern** No methodological details of the simulations are provided. The force field, simulation length, temperature, solvent model, starting structures, and analysis protocols are not described. The manuscript does not state how many simulations were run, whether they were replicated, or how convergence was assessed. The claim that simulations "support" the proposed preferences is therefore unverifiable.
- **Why it matters** Molecular dynamics results are only meaningful if the methods are reproducible and the analysis is rigorous. Without these details, the simulation results cannot be distinguished from anecdotal observations.
- **Resolution test** Provide full simulation parameters, including software, force field, water model, ion conditions, simulation time, and temperature coupling. Describe the analysis protocol, including how stability was assessed (e.g., RMSD, contact maps) and how the results support the classification. If possible, include a convergence check or replicate simulations.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Claim strength
- **Claim pointer** The manuscript states that "arginine is the most versatile of all chemical structures" in RNA binding and that glycine residues act as spacers enabling stacking interactions.
- **Evidence pointer** Section "RNA-protein contacts at an atomic level"; Figure 4 (not visible)
- **Concern** These claims are presented as general principles but are supported by only a few examples. The manuscript does not provide a systematic analysis of residue frequencies or interaction types across the 24 complexes. The claim that arginine is "the most versatile" is a strong statement that would require comparative analysis across all amino acids and interaction types.
- **Why it matters** If these are intended as general principles of IDR-RNA recognition, they need to be supported by quantitative evidence. If they are only observations from a few structures, the language should be tempered.
- **Resolution test** Provide a systematic analysis of amino acid contributions to RNA binding across the surveyed complexes, including interaction frequencies, types of contacts, and a comparison with folded RNA-binding domains. Alternatively, revise the language to reflect the limited evidence base.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Scope and focus
- **Claim pointer** The manuscript includes a section on small-molecule RNA ligands and compares their binding strategies to those of IDRs.
- **Evidence pointer** Section "Other RNA ligands: Small molecules versus proteins and peptides"; Figures 6 and 7 (not visible)
- **Concern** This section is brief and does not provide a clear comparative framework. The manuscript does not systematically compare the structural features of small-molecule binding sites with those of IDR binding sites. The relevance of this section to the main classification is not well articulated.
- **Why it matters** The inclusion of this topic broadens the scope but dilutes the focus. If the comparison is intended to be informative, it needs to be more rigorous. If it is tangential, it should be removed or shortened.
- **Resolution test** Either expand this section with a systematic comparison of binding site features (e.g., pocket shape, residue composition, RNA structural context) or remove it to sharpen the manuscript's focus.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Abstract
- **Evidence pointer** Abstract
- **Issue** The abstract states that the authors "found two major binding modes" but does not name them. This is a missed opportunity to communicate the key finding clearly.
- **Required correction** Name the two binding modes explicitly in the abstract.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Terminology
- **Affected element** Section "Alpha-helical RNA binding motifs"
- **Evidence pointer** Section "Alpha-helical RNA binding motifs"
- **Issue** The term "R/E/S-rich repeats" is used without definition. It is unclear whether this refers to a specific sequence pattern or a general compositional bias.
- **Required correction** Define the term and provide examples of proteins containing such repeats.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Section "DNA versus RNA: Shared and distinct protein partnerships"
- **Evidence pointer** Section "DNA versus RNA: Shared and distinct protein partnerships"
- **Issue** The comparison with DNA-binding IDRs is qualitative and does not reference specific structures or quantitative data.
- **Required correction** Add specific examples with PDB codes and, if available, quantitative comparisons of binding affinities or structural features.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Consistency
- **Affected element** Section "The role of repeats and multivalency"
- **Evidence pointer** Section "The role of repeats and multivalency"
- **Issue** The manuscript discusses liquid-liquid phase separation but does not clearly distinguish between IDR-RNA interactions that drive phase separation and those that do not.
- **Required correction** Clarify the relationship between the proposed classification and phase separation behavior.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Accessibility
- **Affected element** Section "True RNA structure is almost never two-dimensional"
- **Evidence pointer** Section "True RNA structure is almost never two-dimensional"
- **Issue** The statement that "RNA is rarely ever single-stranded in real structures" is an overgeneralization. Many functional RNAs contain single-stranded regions that are biologically important.
- **Required correction** Qualify this statement to acknowledge the context-dependence of RNA structure.

- **Technical failings that need to be addressed before the case is established** The absence of methodological detail for the PDB search and the molecular dynamics simulations is a critical failing. The classification system cannot be evaluated without a transparent description of the dataset. The simulation results are presented as supporting evidence but are not reproducible from the information provided. The manuscript also lacks quantitative analysis of the structural features it describes, relying instead on qualitative descriptions.

- **Assessment against Nature-style criteria**  
  *Originality*: The topic is original in the sense that few reviews focus specifically on the structural biology of RNA-binding IDRs. However, the conceptual framework (disordered regions binding RNA via electrostatic and stacking interactions) is not entirely new.  
  *Scientific importance*: The importance is moderate to high. Understanding how IDRs recognize RNA is relevant to many biological processes, including phase separation and gene regulation. However, the manuscript does not provide enough new data to substantially advance the field.  
  *Interdisciplinary readership*: The topic bridges structural biology, RNA biology, and biophysics. The manuscript is likely to appeal to researchers in these areas, but the lack of quantitative detail may limit its impact.  
  *Technical soundness*: The technical soundness cannot be fully assessed because the methods for the PDB search and simulations are not described. The qualitative structural analysis is plausible but not rigorously supported.  
  *Readability for nonspecialists*: The manuscript is generally well-written and accessible. The concepts are explained clearly, and the authors avoid excessive jargon. However, the lack of figures in the provided material makes it difficult to assess the visual clarity.

- **Recommendation posture** Currently not established from the provided evidence. The manuscript has merit as a perspective or hypothesis-generating review, but the central claims about classification and simulation support cannot be verified without additional methodological detail and access to the figures and tables. If the authors can provide a transparent description of their PDB search, detailed simulation parameters, and a more quantitative analysis of the structural features, the manuscript could become a valuable contribution. As presented, it is more of a qualitative overview than a rigorous structural analysis.

## Risk / unsupported claims
- The claim of a "comprehensive search" of the PDB is unsupported without a description of the search methodology.
- The claim that molecular dynamics simulations "support" the proposed structural preferences is unsupported without simulation details.
- The claim that arginine is "the most versatile" amino acid in RNA binding is an overgeneralization not supported by systematic analysis.
- The statement that "RNA is rarely ever single-stranded in real structures" is an overgeneralization that is not supported by the evidence presented.
- The classification into two major binding modes is presented as definitive, but the small dataset and lack of quantitative analysis make this claim premature.
- The comparison between small-molecule RNA ligands and IDR binding strategies is not supported by a systematic analysis.