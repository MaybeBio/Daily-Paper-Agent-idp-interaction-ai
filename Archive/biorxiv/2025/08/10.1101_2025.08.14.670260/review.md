## Review setup
- **Input scope** Full manuscript text (abstract, introduction, methods, results, discussion, data availability, author contributions, acknowledgements)
- **Assessment boundary** Scientific and technical evaluation of the described database resource, its construction methodology, and its stated utility for the community
- **Shared manuscript claim summary** The authors present DynaRepo, a repository of macromolecular conformational dynamics comprising approximately 450 complexes and 270 single-chain proteins, simulated in triplicate for 500 ns each, totaling over 1100 µs of molecular dynamics data with extensive pre-computed analyses, positioned as a resource to enable dynamics-aware deep learning frameworks
- **Visible evidence base** Abstract, introduction, methods (data selection, MD simulation protocol, database implementation, post-simulation analysis), results (database contents, overview/trajectory pages, analyses page, downloads page), discussion, data availability statement
- **Missing materials affecting confidence** Supplementary figures S1-S15 referenced but not provided; no validation metrics for simulation stability or convergence; no comparison with existing MD repositories beyond a brief mention; no quantitative assessment of data quality or usability; no demonstration of the claimed downstream applications (e.g., binding site prediction improvements) with actual results

## Reviewer
- **Overall assessment** The manuscript describes a potentially valuable community resource for macromolecular dynamics, addressing a genuine gap in the availability of large-scale, standardized MD simulation data. The scale of simulations (~1100 µs total) and the focus on complexes, including protein-nucleic acid assemblies, are commendable. However, the manuscript as presented is largely descriptive and lacks critical validation and quality assessment. The absence of any demonstration that the data are reliable, consistent, or fit for the stated purpose of training deep learning models substantially weakens the case. The resource may be useful, but the evidence provided in this manuscript does not currently establish its scientific value or technical soundness beyond the fact of its existence.

- **Who would be interested in the results, and why** Computational biologists and bioinformaticians developing machine learning methods for protein structure and dynamics prediction would be the primary audience. Researchers studying protein-protein interactions, antibody-antigen recognition, and protein-nucleic acid complexes would find the data relevant. The resource could also interest method developers in the MD simulation community who seek standardized benchmark datasets. However, the impact will depend on demonstrated data quality and usability, which are not established here.

- **Major strengths**
  1. Addresses a real and recognized gap: the scarcity of large-scale, openly available MD simulation data for macromolecular complexes, particularly for training dynamics-aware deep learning models
  2. The selection of diverse systems (PDBbind complexes, antibody antigens, transient complexes, nucleosomes) provides broad coverage of biologically relevant interaction types
  3. Integration with the MDDB federated infrastructure and FAIR principles is a sensible approach that promotes interoperability and community adoption
  4. The provision of pre-computed analyses (RMSD, RMSF, PCA, pocket detection, etc.) lowers the barrier for non-specialist users

- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The manuscript claims the repository provides "a foundation for dynamics-aware deep learning frameworks" and that the data are suitable for training models in binding site prediction, functional annotation, stability assessment, and binding affinity estimation
- **Evidence pointer** Results section, Discussion section; location not provided
- **Concern** No validation of simulation quality is presented. There is no assessment of equilibration, convergence, force field appropriateness, or comparison with experimental data. The manuscript states that RMSD values are reported but does not show or summarize them in the main text. For a resource intended to train predictive models, the quality and reliability of the trajectories are paramount. Without any demonstration that the simulations are physically meaningful, the utility of the entire dataset is questionable.
- **Why it matters** If the simulations contain artifacts, poor equilibration, or force field inaccuracies, models trained on these data will learn incorrect dynamics. The claim that this resource can serve as a foundation for deep learning frameworks cannot be evaluated without quality metrics. The scientific community cannot trust or effectively use data of unverified quality.
- **Resolution test** Provide quantitative validation metrics in the main text or supplementary material, including: (a) RMSD and RMSF distributions across all systems, (b) assessment of equilibration (e.g., energy drift, temperature/pressure stability), (c) comparison of simulated ensembles with experimental observables where available (e.g., B-factors, SAXS profiles, NMR order parameters), and (d) convergence analysis (e.g., block averaging, split-half comparisons). At minimum, show that the simulations are stable and that the ensembles are reproducible across replicas.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Reproducibility and completeness
- **Claim pointer** The abstract states the repository contains "~450 complexes and ~270 single-chain proteins," while the Results section states "405 macromolecular complexes," "220 single-chain antigens," and "53 protein-protein complexes in both bound and unbound forms," totaling 405 + 220 + 53 = 678 systems, with nucleosome simulations adding 7 more
- **Evidence pointer** Abstract; Results section; location not provided
- **Concern** The numbers in the abstract and results are inconsistent. The abstract claims ~450 complexes and ~270 single-chain proteins (total ~720), while the results section gives 405 complexes, 220 single-chain antigens, and 53 transient complexes (total 678), plus 7 nucleosome variants. The discrepancy is not explained. Additionally, the "Testing Transient" dataset is described as 53 complexes in both bound and unbound forms, which could mean 53 or 106 systems depending on counting. The total simulation time is given as "approximately 1065 µs" in Results but ">1100 µs" in the abstract. These inconsistencies undermine confidence in the accuracy of the reported resource.
- **Why it matters** Accurate accounting of the database contents is essential for users who need to know exactly what data are available. Inconsistencies between the abstract and results, and ambiguity in counting, make it difficult to assess the true scope of the resource and may indicate broader issues with data management and reporting.
- **Resolution test** Provide a clear, consistent breakdown of the database contents, including exact numbers for each dataset, how bound and unbound forms are counted, and a reconciliation of the total simulation time. Ensure the abstract and results sections are numerically consistent.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Scientific importance and novelty
- **Claim pointer** The manuscript claims DynaRepo "complements and extends current resources" and is distinct from existing repositories by focusing on macromolecular complexes including protein-nucleic acid assemblies
- **Evidence pointer** Introduction, Discussion; location not provided
- **Concern** The novelty and differentiation from existing resources are not clearly established. The authors mention MDRepo, MDDB, MemProtMD, GPCRmd, SCoV2-MD, MoDEL, Dynameomics, and ATLAS, but do not provide a systematic comparison of what these resources contain, how they differ, and what specific gap DynaRepo fills. The claim that DynaRepo is unique in focusing on complexes is not substantiated with a survey of existing resources. Furthermore, the nucleosome simulations are taken from previous studies, and the "Testing Transient" dataset appears to be from an existing benchmark, so the genuinely new simulation data may be limited to the PDBbind and antigen sets.
- **Why it matters** For a database resource paper, establishing the unique contribution relative to existing resources is essential. Without a clear comparative analysis, it is difficult to assess whether this resource provides significant new value or is largely redundant with existing efforts. The scientific impact of the resource depends on its distinctiveness.
- **Resolution test** Provide a systematic comparison table of existing MD repositories, including their contents, focus areas, data formats, and accessibility. Clearly articulate what DynaRepo offers that others do not, with specific examples. Quantify the proportion of genuinely new simulation data versus data derived from previous studies.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Technical soundness
- **Claim pointer** The methods state that missing residues were added using MODELLER for gaps of maximum 5 residues or AlphaFold3 for longer gaps, and that ligands were removed but ions were kept
- **Evidence pointer** Materials and Methods, Molecular Dynamics Simulations; location not provided
- **Concern** The structural preparation protocol raises several concerns. (a) Removing all ligands from protein complexes may significantly alter the conformational dynamics, particularly for systems where ligands stabilize specific conformations. (b) The use of AlphaFold3 to model missing residues introduces predicted structures that may not be consistent with the experimental structure, potentially creating artifacts at the junction regions. (c) The criteria for choosing between MODELLER and AlphaFold3 (gap length) is arbitrary and not justified. (d) The manuscript does not state how many systems required gap filling or what fraction of residues were modeled. (e) The equilibration protocol mentions "lipid and solvent components" but no lipids are mentioned elsewhere in the methods.
- **Why it matters** The structural preparation directly affects the quality and biological relevance of the simulations. If ligands are removed, the dynamics may not reflect the functional state of the complexes. If a significant fraction of residues are modeled by prediction methods, the simulations may not accurately represent the experimental structures. Users of the database need to understand these limitations to interpret the data correctly.
- **Resolution test** Provide a detailed analysis of the structural preparation, including: (a) the number and fraction of systems with missing residues, (b) the total number of residues modeled by MODELLER versus AlphaFold3, (c) an assessment of whether ligand removal affects the dynamics of specific systems, and (d) clarification of the equilibration protocol. Consider providing simulations with and without ligands for a subset of systems to assess the impact.

- **Concern ID** R1-M5
- **Severity** Major
- **Blocking** No
- **Axis** Reproducibility and completeness
- **Claim pointer** The manuscript states that "DynaRepo accepts contributions from other users" and that the workflow is available in GitLab, but the details of the deposition and quality control process are not described
- **Evidence pointer** Materials and Methods, Database implementation; location not provided
- **Concern** For a community resource, the process for accepting external contributions is critical. The manuscript does not describe: (a) what quality control checks are performed on submitted data, (b) what metadata standards are required, (c) how the scientific community can validate or provide feedback on the data, (d) whether there is a versioning system, and (e) how the resource will be sustained and maintained over time. The mention of a GitLab workflow is helpful but does not address these governance questions.
- **Why it matters** The long-term value of a database resource depends on its sustainability and the trust of the community. Without clear governance and quality control processes, potential contributors and users may be hesitant to engage with the resource. The scientific community needs to know that the data are reliable and that the resource will be maintained.
- **Resolution test** Describe the governance model for the resource, including quality control procedures for external contributions, metadata standards, versioning, and long-term sustainability plans. Provide information on how users can report issues or provide feedback.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity and presentation
- **Affected element** Abstract
- **Evidence pointer** Abstract; location not provided
- **Issue** The abstract states ">1100 µs of molecular dynamics data" while the Results section states "approximately 1065 µs" for the PDBbind, antigen, and transient sets, with nucleosome simulations adding 81 µs. The total should be approximately 1146 µs, which is consistent with ">1100 µs" but the discrepancy between 1065 and 1100 in the two sections is confusing.
- **Required correction** Ensure numerical consistency between the abstract and the Results section. Either use the same total in both places or clearly explain the breakdown.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Clarity and presentation
- **Affected element** Methods, Molecular Dynamics Simulations
- **Evidence pointer** Materials and Methods, Molecular Dynamics Simulations; location not provided
- **Issue** The equilibration description mentions "allowing the lipid and solvent components to relax around the restrained protein" but no lipids are described anywhere in the methods. This appears to be an error or a leftover from a template.
- **Required correction** Correct the description to accurately reflect the system components, or clarify if lipids are present in any systems.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Clarity and presentation
- **Affected element** Results, Database contents
- **Evidence pointer** Results section; location not provided
- **Issue** The manuscript states the database contains "405 macromolecular complexes" from PDBbind, "220 single-chain antigens" from SABDab, and "53 protein-protein complexes" from the Testing Transient set. The abstract claims "~450 complexes and ~270 single-chain proteins." The relationship between these numbers is unclear, particularly whether the 53 transient complexes are included in the 405 PDBbind complexes or are separate.
- **Required correction** Provide a clear breakdown of the database contents, including how the numbers in the abstract relate to those in the Results section.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Technical soundness
- **Affected element** Methods, Post-simulation analysis
- **Evidence pointer** Materials and Methods, Post-simulation analysis; location not provided
- **Issue** The hydrogen bond definition states a distance cutoff of 3 Å and an angle cutoff of 135 degrees. These are reasonable but the manuscript does not state which software or library was used for this calculation, nor whether standard hydrogen bond definitions (e.g., donor-acceptor pairs) were used.
- **Required correction** Specify the software and parameters used for hydrogen bond detection, and clarify the donor and acceptor definitions.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Clarity and presentation
- **Affected element** Discussion
- **Evidence pointer** Discussion; location not provided
- **Issue** The discussion mentions "significant bottlenecks remain, most notably the shortage of dynamic datasets for protein-nucleic acid complexes" but the manuscript includes nucleosome simulations, which are protein-nucleic acid complexes. This statement is somewhat contradictory and should be clarified.
- **Required correction** Clarify what specific types of protein-nucleic acid complexes are lacking and how the nucleosome data address or do not address this gap.

- **Concern ID** R1-m6
- **Severity** Minor
- **Axis** Reproducibility and completeness
- **Affected element** Data availability
- **Evidence pointer** Data availability section; location not provided
- **Issue** The data availability statement only provides the website URL. It does not describe the license, usage terms, or whether the data can be downloaded in bulk. For a resource intended for training deep learning models, bulk download access is essential.
- **Required correction** Provide information on the license, usage terms, and bulk download options.

## Risk / unsupported claims
- The claim that DynaRepo "provides a foundation for dynamics-aware deep learning frameworks" is unsupported by any demonstration of the data's utility for this purpose. The discussion mentions prior work using the data but provides no results or references to specific publications.
- The claim that the repository is "the first MDDB node established in France" is a factual statement that cannot be verified from the provided materials.
- The claim that the data are suitable for "binding site prediction, functional annotation, stability assessment, and binding affinity estimation" is asserted but not demonstrated with any validation or example applications.
- The statement that the database "complies with FAIR principles" is asserted but not substantiated with specific evidence of findability, accessibility, interoperability, or reusability.
- The claim that the workflow is "reproducible" is not supported by sufficient detail on software versions, parameters, or containerization.
- The total simulation time and system counts are inconsistent between the abstract and Results, making the exact scope of the resource unclear.
- The quality of the simulations is entirely unassessed. No metrics of stability, convergence, or physical validity are provided.
- The manuscript does not describe any validation of the AlphaFold3-modeled regions against experimental data or assessment of their impact on simulation quality.