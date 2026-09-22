## Review setup
- **Input scope** Full manuscript text (abstract, introduction, materials, methods, notes, acknowledgement) as provided
- **Assessment boundary** Methodological protocol chapter in *Methods in Molecular Biology*; evaluation limited to the supplied text, with no access to figures, tables, supplementary data, or the original research article referenced as [11]
- **Shared manuscript claim summary** The authors present a hybrid NMR-guided protocol combining chemical shift information, amino acid substitution effects on NMR spectra, residual dipolar coupling, and molecular dynamics simulation to determine the structure of a moderate-affinity complex between an intrinsically disordered leiomodin peptide (Lmod2s1) and a folded tropomyosin N-terminal coiled-coil peptide (αTM1a1–14Zip). They claim the protocol resolved a long-standing debate about leiomodin's role in actin filament length regulation and is generalizable to other moderate-affinity IDP–folded protein complexes.
- **Visible evidence base** Abstract; introduction; materials and methods section headings; notes section headings; acknowledgement. No figures, tables, spectra, structural coordinates, or quantitative results are provided.
- **Missing materials affecting confidence** All experimental data (NMR spectra, chemical shift assignments, RDC values, MD simulation trajectories, structural ensembles, validation statistics); the original research article [11] containing the actual structure determination; figures and tables referenced in the methods; detailed protocols within the methods subsections; the Notes section content.

## Reviewer
- **Overall assessment** This manuscript is a methods protocol chapter describing a hybrid NMR-MD approach for structural characterization of moderate-affinity IDP–folded protein complexes. The conceptual framework is sound and the motivation is clearly articulated. However, as supplied, the manuscript is essentially a skeleton: the methods subsections contain only headings, the Notes section is empty, and no data, figures, or validation results are presented. The scientific claims, particularly the assertion that the protocol resolved a long-standing biological debate, cannot be evaluated from the provided material. The chapter may be useful as a procedural reference once fully written, but in its current form it does not constitute a complete, assessable methods contribution.
- **Who would be interested in the results, and why** Structural biologists, NMR spectroscopists, and researchers studying intrinsically disordered proteins and moderate-affinity protein complexes. The protocol addresses a recognized gap in structural biology, namely the difficulty of determining structures of complexes where standard NMR and crystallographic approaches fail due to intermediate exchange line broadening and weak binding. Laboratories with NMR expertise and interest in IDP interactions would find a complete version of this protocol valuable.
- **Major strengths** The manuscript addresses a genuine methodological gap with a clearly stated rationale. The hybrid approach is sensible and leverages complementary information sources. The authors explicitly acknowledge the limitations of the resulting structure definition, which is honest. The claim of generalizability is tempered by recognition that hybrid methods require case-by-case adaptation. The introduction is well-written and accessible to a broad structural biology audience.
- **Major Concerns**
  - **Concern ID** R1-M1
  - **Severity** Major
  - **Blocking** Yes
  - **Axis** Completeness
  - **Claim pointer** The manuscript claims to present a detailed protocol for expression, purification, NMR data collection, and MD simulation of the Lmod2s1–αTM1a1–14Zip complex.
  - **Evidence pointer** Methods section, all subsections; Notes section
  - **Concern** The Methods section consists entirely of subsection headings with no procedural content. The Notes section is empty. No buffers, temperatures, concentrations, spectrometer frequencies, pulse sequences, simulation parameters, force fields, or analysis thresholds are provided. The reader cannot execute any step of the protocol.
  - **Why it matters** A methods protocol chapter is only useful if it contains sufficient procedural detail for replication. Without the actual methods text, the manuscript fails its primary purpose.
  - **Resolution test** Provide the full methods text and notes content for all subsections.
  - **Concern ID** R1-M2
  - **Severity** Major
  - **Blocking** Yes
  - **Axis** Evidence
  - **Claim pointer** The abstract and introduction claim that the protocol "allowed us to determine the structure" of the complex and "resolved a long-standing debate about the role of leiomodin in actin filament length regulation and maintenance."
  - **Evidence pointer** Abstract; Introduction, paragraph 3; location not provided for structural data
  - **Concern** No structural results, validation statistics, or biological interpretation are presented. The claim of resolving a biological debate is made without any supporting data or discussion. The reader cannot assess the quality of the structure, the significance of the finding, or the validity of the biological conclusion.
  - **Why it matters** The scientific significance of the protocol rests on its demonstrated utility. Without presentation of the resulting structure and its biological implications, the claim of resolving a debate is unsupported.
  - **Resolution test** Include a summary of the structural results, validation metrics, and a discussion of the biological implications, or explicitly reference the original publication [11] for these details and frame the chapter strictly as a procedural guide.
  - **Concern ID** R1-M3
  - **Severity** Major
  - **Blocking** Yes
  - **Axis** Reproducibility
  - **Claim pointer** The protocol claims to be generalizable to other moderate-affinity IDP–folded protein complexes.
  - **Evidence pointer** Abstract; Introduction, paragraph 4; Methods subsections on NMR data collection and MD simulation
  - **Concern** The generalizability claim cannot be evaluated because the specific parameters, decision criteria, and troubleshooting guidance are absent. For example, the methods mention "influence of amino acid substitution" and "NMR-guided MD" but provide no details on how many substitutions are needed, how to interpret spectral changes, how to set up the MD simulations, or how to judge convergence.
  - **Why it matters** A generalizable protocol requires explicit guidance on parameter selection and interpretation. Without this, the reader cannot adapt the method to their own system.
  - **Resolution test** Provide detailed procedural steps, parameter values, and decision points for each stage of the protocol.
- **Minor Comments**
  - **Concern ID** R1-m1
  - **Severity** Minor
  - **Axis** Clarity
  - **Affected element** Introduction, paragraph 3
  - **Evidence pointer** Introduction, paragraph 3
  - **Issue** The sentence "Although the structure did not achieve the level of definition typical of an NMR structure of a protein of equal size, it resolved a long-standing debate" is vague. The reader does not know what level of definition was achieved or what the debate was.
  - **Required correction** Provide specific structural statistics (e.g., RMSD, number of restraints, backbone precision) and a brief statement of the biological question that was resolved.
  - **Concern ID** R1-m2
  - **Severity** Minor
  - **Axis** Completeness
  - **Affected element** Methods, "Expression and Purification of Lmod2s1"
  - **Evidence pointer** Methods section, subsection headings
  - **Issue** The methods mention the MFH expression tag and cyanogen bromide cleavage but provide no details on the tag sequence, cleavage conditions, or expected yields.
  - **Required Correction** Add the MFH tag sequence, cleavage buffer composition, and typical yields.
  - **Concern ID** R1-m3
  - **Severity** Minor
  - **Axis** Referencing
  - **Affected element** Introduction, paragraph 3
  - **Evidence pointer** Introduction, paragraph 3; reference [11]
  - **Issue** The manuscript repeatedly refers to reference [11] for key details, including the actual structure determination. This makes the chapter dependent on an external source and reduces its standalone utility.
  - **Required Correction** Either include the essential results and parameters in this chapter or clearly state that the chapter is a companion to [11] and should be read alongside it.
- **Technical failings that need to be addressed before the case is established** The manuscript as supplied contains no technical content in the Methods and Notes sections. All procedural details are absent. No data are presented to support the claims of successful structure determination or biological significance. The chapter cannot be used, evaluated, or replicated in its current form.
- **Assessment against Nature-style criteria**  
  *Originality*: The hybrid approach itself is not entirely novel, as the authors acknowledge the broader field of hybrid structural biology. The specific combination of chemical shift perturbation, substitution effects, RDC, and MD for moderate-affinity IDP complexes has some originality, but this cannot be fully assessed without the procedural details.  
  *Scientific importance*: The problem addressed is important, as moderate-affinity IDP complexes are biologically prevalent and structurally challenging. However, the importance of this specific protocol is not demonstrated without results.  
  *Interdisciplinary readership*: The topic bridges NMR spectroscopy, molecular dynamics simulation, and IDP biology, which would interest a multidisciplinary audience. The introduction is written accessibly.  
  *Technical soundness*: Cannot be assessed. No technical content is provided.  
  *Readability for nonspecialists*: The introduction is clear and well-motivated. The methods, once written, would likely be accessible to researchers with standard biophysical training.

## Risk / unsupported claims
- The claim that the protocol "allowed us to determine the structure" of the Lmod2s1–αTM1a1–14Zip complex is unsupported in the provided material.
- The claim that the structure "resolved a long-standing debate about the role of leiomodin in actin filament length regulation and maintenance" is unsupported.
- The claim that the protocol "can be used for other moderate-affinity complexes" is plausible but not demonstrated.
- All statements regarding the quality, precision, or accuracy of the resulting structure are unevaluable.
- The generalizability of the protocol to other systems is unevaluable without procedural details.