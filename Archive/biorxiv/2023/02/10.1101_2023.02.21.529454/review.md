## Review setup
- **Input scope** Full manuscript text including abstract, introduction, results, discussion, materials and methods, author contributions, and footnotes
- **Assessment boundary** Scientific validity, technical soundness, clarity of claims, and alignment with Nature-style criteria based solely on the provided manuscript content
- **Shared manuscript claim summary** The authors use AlphaFold2 and AlphaFold-Multimer to predict the full-length structure of the TrkB receptor, its dimeric assemblies with ligands, transmembrane helix dimers with antidepressant binding sites, and intracellular complexes with signaling proteins, proposing that AI-based structure prediction can expand antidepressant drug discovery to include RTK targets
- **Visible evidence base** Abstract, Introduction, Results sections 2.1-2.4, Discussion, Materials and Methods sections 4.1-4.8, Author Contributions, Footnotes. No figures, tables, or supplementary materials were provided for inspection
- **Missing materials affecting confidence** All figures (Fig 1-5, Fig S1-S12), supplementary tables, sequence alignment data, molecular dynamics trajectories, and binding free energy calculations are referenced but not available for verification

## Reviewer
- **Overall assessment** The manuscript presents a computational study applying AlphaFold2 and AlphaFold-Multimer to predict structures of the TrkB receptor in various assembly states, including ligand-bound extracellular domains, transmembrane helix dimers with antidepressant binding sites, and intracellular kinase-signaling protein complexes. The work addresses a relevant topic in structural biology and antidepressant drug discovery. However, the manuscript has substantial limitations. The claims are largely descriptive and lack experimental validation. The prediction of a novel antidepressant binding site in the transmembrane helix dimer is based solely on computational docking without experimental confirmation. The authors acknowledge that AlphaFold-Multimer fails to produce a reasonable full-length dimeric structure, which undermines confidence in the overall approach. The writing contains numerous grammatical errors and unclear statements that impede comprehension. The methods section contains inconsistencies, such as conflicting simulation times and force field parameters. The manuscript does not provide sufficient evidence to establish the central claims, and the scientific impact is limited by the absence of experimental verification or novel methodological advances.

- **Who would be interested in the results, and why** Computational structural biologists studying receptor tyrosine kinase assemblies and researchers interested in the application of AlphaFold to membrane proteins may find the approach relevant. Scientists working on antidepressant mechanisms, particularly those investigating TrkB as a therapeutic target, might be interested in the proposed transmembrane binding site. However, the lack of experimental validation and the acknowledged limitations of the predictions will likely limit enthusiasm. The broader readership of a high-impact journal would require stronger evidence that these computational predictions have biological or therapeutic relevance.

- **Major strengths** The manuscript addresses a timely topic, applying state-of-the-art deep learning methods to a receptor of clinical relevance. The authors appropriately acknowledge limitations of AlphaFold-Multimer for full-length dimer prediction and adopt a divide-and-conquer strategy. The comparison of three prediction approaches for the monomer and the use of known experimental structures as benchmarks for the extracellular domain are reasonable. The discussion of how AlphaFold predictions could guide Cryo-EM data interpretation is a useful perspective.

- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence sufficiency
- **Claim pointer** The manuscript claims that "AF-M predicts the antidepressant binding pocket at the crossover of TrkB transmembrane segment dimer" and that (2R,6R)-HNK binds to this site with a binding free energy of -17.14 kcal/mol
- **Evidence pointer** Section 2.3, Figure 3, Figure S7, Section 4.5, Section 4.7, Section 4.8
- **Concern** The central claim of an antidepressant binding site in the TrkB transmembrane helix dimer is supported only by computational docking and molecular dynamics simulations. No experimental validation, such as mutagenesis, binding assays, or functional studies, is provided. The binding free energy calculation is presented without error estimates or convergence analysis. The authors do not compare their predicted binding site with any known TrkB ligand binding data. The claim that this site is a "potential drug binding site" is speculative and not established by the evidence presented.
- **Why it matters** The identification of a novel drug binding site is a strong claim that requires experimental corroboration. Without validation, the therapeutic relevance of the predicted site remains uncertain, and the manuscript does not advance beyond computational speculation.
- **Resolution test** Provide experimental evidence such as site-directed mutagenesis of the predicted binding residues followed by binding assays, or demonstrate that the predicted binding site is supported by existing experimental data. Alternatively, provide orthogonal computational evidence, such as extensive sampling with multiple docking tools and long-timescale molecular dynamics with binding free energy convergence analysis.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The manuscript claims that AlphaFold-Multimer can predict "the essential posture of the assemblies during phosphorylation using related signal substrates like PLCγ1, SHP2, and SHC1"
- **Evidence pointer** Section 2.4, Figures 4-5, Figures S8-S12, Section 4.2
- **Concern** The authors acknowledge that AlphaFold-Multimer fails to produce a reasonable full-length dimeric structure of TrkB, yet they proceed to use the same method for intracellular complexes. The predicted complexes with SHP2 and SHC1 are described as having contacts in disordered regions, which the authors attribute to missing post-translational modifications. The manuscript does not provide any scoring metrics, confidence values, or comparison with known experimental structures for these complexes. The claim that these predictions represent "signal assemblies" is not supported by the evidence.
- **Why it matters** The reliability of AlphaFold-Multimer for predicting transient signaling complexes is not established. Without validation or confidence metrics, the predicted intracellular assemblies cannot be considered reliable, and the conclusions drawn from them are not justified.
- **Resolution test** Provide confidence metrics (e.g., predicted aligned error, interface pLDDT) for the predicted complexes. Compare predictions with any available experimental structures of TrkB kinase complexes. Validate at least one predicted interaction experimentally, such as co-immunoprecipitation or pull-down assays.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Reproducibility
- **Claim pointer** The methods section describes molecular dynamics simulations with conflicting parameters, including simulation times of 100 ns and 50 ns, and inconsistent force field and water model descriptions
- **Evidence pointer** Section 4.7
- **Concern** The methods section contains internal contradictions. The text states "molecular dynamics simulations were performed for 100 ns" and later states "the MDS simulations were performed for 50 ns." The force field is described as amber14sb, but the small molecule topology is generated with GAFF2, which is inconsistent. The water model is described as TIP3P, but the equilibration and production parameters are not clearly specified. These inconsistencies prevent reproduction of the simulations and undermine confidence in the reported results.
- **Why it matters** Reproducibility is a fundamental requirement for scientific claims. Conflicting methodological descriptions make it impossible for other researchers to replicate the simulations or assess the validity of the results.
- **Resolution test** Correct the methods section to provide a consistent and complete description of the simulation protocol, including exact simulation times, force field parameters, water model, and equilibration procedures.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Scientific importance
- **Claim pointer** The manuscript claims that "AI will provide crucial points of the unresolved protein architectures associated with pathologies, broadening the scope of structure-based drug discovery to all coding sequences"
- **Evidence pointer** Abstract, Discussion
- **Concern** The broader claim that this approach will enable drug discovery across all coding sequences is not supported by the data presented. The manuscript demonstrates predictions for one receptor with acknowledged limitations. The leap from these results to a general paradigm for drug discovery is not justified.
- **Why it matters** Overstated claims diminish the credibility of the work and may mislead readers about the current capabilities of AI-based structure prediction for drug discovery.
- **Resolution test** Temper the claims to reflect the actual scope of the study, or provide additional evidence demonstrating the generalizability of the approach across multiple receptor families.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Abstract
- **Evidence pointer** Abstract, "In silicon" phrase
- **Issue** The phrase "In silicon" appears to be a typographical error for "In silico". This error appears in the abstract and should be corrected.
- **Required correction** Change "In silicon" to "In silico".

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Section 2.1
- **Evidence pointer** Section 2.1, numbered list items 4-6
- **Issue** The numbered list in section 2.1 begins with items numbered 4, 5, and 6, which is confusing. The list should be renumbered starting from 1.
- **Required correction** Renumber the list items to 1, 2, and 3.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Section 4.8
- **Evidence pointer** Section 4.8, final sentence
- **Issue** The sentence "The entropy change is neglected in this study due to the high computational resources and low precision. this study is neglected." contains a duplicated and incomplete phrase.
- **Required correction** Remove the duplicated phrase and correct the sentence to read "The entropy change is neglected in this study due to the high computational resources required and the low precision of entropy estimates."

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Technical accuracy
- **Affected element** Section 4.4
- **Evidence pointer** Section 4.4, docking parameters
- **Issue** The docking parameters are described inconsistently. The text states "the approximation (exhaustiveness) of docking was 80, the box size of docking was 40 Å, and 80 Å conformations were generated each time." The term "80 Å conformations" is unclear and likely should be "80 conformations."
- **Required correction** Clarify the docking parameters, likely changing "80 Å conformations" to "80 conformations."

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Section 2.2
- **Evidence pointer** Section 2.2, final paragraph
- **Issue** The sentence "This indicated that AF2 can predict the structure of complexes with ligands encompassing minimal ligand-binding structural domain sequences" is ambiguous. It is unclear whether "encompassing" refers to the complexes or the ligands.
- **Required correction** Rephrase for clarity, such as "This indicated that AF2 can predict the structure of complexes formed between ligands and minimal ligand-binding domain sequences."

- **Concern ID** R1-m6
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Section 4.2
- **Evidence pointer** Section 4.2, sequence combinations
- **Issue** The methods state that "the sequence combinations used are shown in the Supplementary Material," but the supplementary material is not provided. This prevents assessment of the construct design.
- **Required correction** Include the supplementary material or describe the sequence combinations in the main text.

- **Concern ID** R1-m7
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Section 2.3
- **Evidence pointer** Section 2.3, first paragraph
- **Issue** The sentence "The transmembrane helix dimerization structure of TrkA has been resolved previously" is followed by a comparison, but the transition is abrupt and the significance of the comparison is not clearly explained.
- **Required correction** Expand the comparison to explain how the TrkA structure informs the TrkB prediction and what the differences mean functionally.

- **Concern ID** R1-m8
- **Severity** Minor
- **Axis** Technical accuracy
- **Affected element** Section 4.7
- **Evidence pointer** Section 4.7, equilibration description
- **Issue** The text states "elastic simulation by Verlet and cg algorithms respectively" which is unclear. The Verlet algorithm is an integration scheme, not an equilibration method, and "cg" likely refers to conjugate gradient energy minimization. The description is imprecise.
- **Required correction** Clarify the equilibration and minimization procedures, specifying which algorithm is used for which step.

## Risk / unsupported claims
- The claim of a specific antidepressant binding site in the TrkB transmembrane helix dimer is unsupported by experimental evidence and relies solely on computational docking and short-timescale molecular dynamics.
- The claim that AlphaFold-Multimer can predict "signal assemblies" of TrkB with PLCγ1, SHP2, and SHC1 is not supported by confidence metrics or experimental validation.
- The statement that "AI will provide crucial points of the unresolved protein architectures associated with pathologies, broadening the scope of structure-based drug discovery to all coding sequences" is an overgeneralization not supported by the data presented.
- The claim that the predicted (2R,6R)-HNK binding free energy of -17.14 kcal/mol indicates "a high probability of interaction" is not supported by error estimates or comparison with known binding affinities.
- The assertion that the predicted transmembrane helix dimer is "stable in the lipid raft environment" is based on a single 100 ns simulation without replicate runs or convergence analysis.
- The statement that "AF-M has the ability to predict the fixed structure of RTKs undergoing dimerization" is contradicted by the authors' own finding that AlphaFold-Multimer fails to produce a reasonable full-length TrkB dimer.
- The claim that the predicted structures can "enhance the resolution of highly flexible dimeric transmembrane helices of RTKs under Cryo-EM" is speculative and not demonstrated in this work.