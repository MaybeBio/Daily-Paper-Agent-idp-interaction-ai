## Review setup
- **Input scope** Full manuscript text and abstract
- **Assessment boundary** Scientific claims, methodology, and evidence presented in the provided text
- **Shared manuscript claim summary** The authors use atomistic simulations of 20 peptide-RNA mixtures to classify amino acid residues into four groups based on their propensity to promote, maintain, suppress, or disrupt protein-RNA phase separation, and propose a ternary phase diagram of interactions.
- **Visible evidence base** Abstract, Computational Methods section, and reference to supplementary figures (Figure S1)
- **Missing materials affecting confidence** Full results section, all figures and tables, supplementary data, and detailed analysis outputs are not provided

## Reviewer
- **Overall assessment** The manuscript addresses a timely and important question in the field of biomolecular condensates, namely the molecular grammar governing protein-RNA phase separation. The use of atomistic simulations with a systematic library of 20 amino acid variants is a commendable approach. However, the provided text is largely limited to methods and a high-level summary, with no quantitative results or detailed analysis presented. The core claims regarding the classification of amino acids and the ternary phase diagram cannot be evaluated from the supplied material. The methodological choices are reasonable but some details require clarification to assess technical soundness.
- **Who would be interested in the results, and why** Researchers studying liquid-liquid phase separation, RNA-binding proteins, and the molecular determinants of condensate formation. The systematic classification of amino acid behavior in the presence of RNA would be of interest to computational biophysicists and experimentalists working on condensate biology, as it could guide mutagenesis studies and the design of synthetic condensates.
- **Major strengths** The systematic approach of testing all 20 amino acids in a controlled peptide-RNA system is a clear strength. The use of atomistic simulations with explicit solvent and ions provides a detailed molecular view. The proposed classification into four functional groups offers a potentially useful framework for understanding protein-RNA phase separation.
- **Major Concerns** The absence of any quantitative results, figures, or detailed analysis in the provided text makes it impossible to assess the validity of the central claims. The manuscript as presented is essentially a methods description with a summary of conclusions, lacking the evidence needed to support those conclusions.
- **Minor Comments** Several methodological details require clarification, including the rationale for the specific peptide and RNA sequences, the justification for the simulation length, and the statistical treatment of cluster analysis.
- **Technical failings that need to be addressed before the case is established** The lack of presented results and analysis is a fundamental failing. Without quantitative data on cluster sizes, residue fractions, interaction energies, or the proposed phase diagram, the core claims are unsupported.
- **Assessment against Nature-style criteria** Originality: The systematic amino acid scan in the context of RNA is a novel contribution. Scientific importance: The question is important, but the significance of the findings cannot be judged without results. Interdisciplinary readership: The topic bridges biophysics, computational chemistry, and cell biology, but the current text is too methods-focused for a broad audience. Technical soundness: The methods are plausible but not fully verifiable from the provided text. Readability for nonspecialists: The abstract is accessible, but the methods section is highly technical and the lack of results limits overall readability.
- **Recommendation posture** Currently not established from the provided evidence. The manuscript requires a full presentation of results and analysis to support its claims.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence sufficiency
- **Claim pointer** The manuscript claims to identify four distinct groups of amino acids that promote, maintain, suppress, or disrupt protein-RNA clusters, and to map a ternary phase diagram of interactions.
- **Evidence pointer** Abstract; location not provided for results
- **Concern** The central claims of the paper, namely the classification of amino acids into four functional groups and the construction of a ternary phase diagram, are presented in the abstract but no supporting quantitative data, figures, or tables are provided in the supplied text. The results section is entirely absent.
- **Why it matters** Without the actual data showing cluster sizes, residue fractions, interaction profiles, or the phase diagram itself, the claims are unverifiable. The reader cannot assess whether the classification is robust, statistically significant, or correctly interpreted.
- **Resolution test** Provide the full results section with figures and tables showing the quantitative analysis of cluster properties, interaction energies, hydration profiles, and ion distributions for all 20 systems, along with the proposed ternary phase diagram.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The methods state that a 2 μs productive run was performed, with analyses conducted on the final one-microsecond equilibrated trajectory, and cluster sizes confirmed through bootstrapping.
- **Evidence pointer** Computational Methods; location not provided
- **Concern** The choice to analyze only the final microsecond of a 2 μs trajectory is not justified. It is unclear whether the system reached equilibrium within the first microsecond, and whether the final microsecond is representative of steady-state behavior. Additionally, the bootstrapping procedure is mentioned but not described in sufficient detail to assess its validity.
- **Why it matters** If the systems are not fully equilibrated, the cluster properties and interaction analyses may be biased by transient states. The lack of a clear equilibrium assessment undermines confidence in the reported results.
- **Resolution test** Provide evidence of equilibration, such as time series of cluster sizes or potential energy, and describe the bootstrapping procedure in detail, including the number of resamples and the metrics compared.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Reproducibility
- **Claim pointer** The methods describe the use of specific software and force fields, including PeptideBuilder, X3DNA, packmol, TIP3P water, and amber99SB*-ILDN-Q.
- **Evidence pointer** Computational Methods; location not provided
- **Concern** The force field combination is unusual, as amber99SB*-ILDN-Q is not a standard or widely validated force field for RNA simulations. The authors do not provide a citation for this force field or justify its use over more established options. Additionally, the statement that TIP3P is "optimal" for phase separation is not supported by a specific reference or comparative data.
- **Why it matters** The choice of force field can significantly affect simulation outcomes, particularly for RNA and protein-RNA interactions. Without proper validation or justification, the results may not be reproducible or transferable to other systems.
- **Resolution test** Provide a citation for the amber99SB*-ILDN-Q force field, justify its selection, and include validation data or comparisons with other force fields if available.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Methods description
- **Evidence pointer** Computational Methods; location not provided
- **Issue** The description of the system setup states a "biomolecular system density of ~100 mg/mL" but does not specify how this density was calculated or whether it includes both peptide and RNA mass.
- **Required correction** Clarify the calculation of the system density and specify the mass ratio of peptide to RNA in the initial setup.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Methods description
- **Evidence pointer** Computational Methods; location not provided
- **Issue** The methods mention "a detailed contact analysis" and "water-bridged interaction analysis" but do not provide the specific criteria used to define contacts or water bridges.
- **Required correction** Define the distance or geometric criteria used for identifying contacts and water bridges in the analysis.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Statistical rigor
- **Affected element** Cluster analysis
- **Evidence pointer** Computational Methods; location not provided
- **Issue** The use of DBSCAN for cluster extraction is mentioned, but the parameters (e.g., epsilon, minimum samples) are not specified, and the sensitivity of results to these parameters is not discussed.
- **Required correction** Provide the DBSCAN parameters used and include a sensitivity analysis or justification for the chosen values.

## Risk / unsupported claims
- The classification of amino acids into four groups (promote, maintain, suppress, disrupt) is unsupported without quantitative results.
- The ternary phase diagram of interactions is mentioned but not shown or described in any detail.
- The claim that the general classification is consistent across water models is unsupported, as no comparative data are provided.
- The statement that U3 and GXG are "featureless biomolecules" is an assertion without supporting evidence or citation.
- The claim that TIP3P is optimal for phase separation is not substantiated with specific references or data.