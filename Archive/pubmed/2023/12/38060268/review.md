## Review setup
- **Input scope** Full manuscript text (Summary, Availability and implementation, Supplementary Material note, Conflict of interest, Funding, Acknowledgements)
- **Assessment boundary** The provided text is a software application note. The assessment is limited to the claims made in the Summary and the implementation details provided. No figures, tables, or supplementary data were available for review.
- **Shared manuscript claim summary** The manuscript presents LDRS, a new module for the IDPConformerGenerator suite, designed to generate all-atom conformational ensembles for disordered regions (N-/C-termini, loops, linkers) of proteins that are missing from experimental structures or have low confidence in predicted structures. The tool requires only a structural template and the full-length sequence, and it claims capabilities for modeling phosphorylation sites, transmembrane proteins in a bilayer, and multi-chain complexes. The tool is reported to be modular, usable as a library or via command line, and computationally fast.
- **Visible evidence base** The visible evidence base consists solely of the Summary and Availability/implementation sections. No performance benchmarks, validation data, case studies, or comparisons to other methods are provided in the supplied text.
- **Missing materials affecting confidence** The following materials are not provided and would be essential for a full assessment: all figures and tables, the supplementary data (including conformational ensembles and analyses), any validation metrics (e.g., agreement with experimental data, sampling convergence), and a detailed description of the algorithms (e.g., the enhanced Monte Carlo-Side Chain Entropy method). The absence of these materials severely limits the ability to evaluate the technical soundness and the validity of the stated capabilities.

## Reviewer
- **Overall assessment** The manuscript describes a potentially useful software tool that addresses a real need in structural biology, namely the modeling of disordered regions that are often missing from experimental or predicted structures. The integration into the existing IDPConformerGenerator platform is a sensible approach. However, the provided text is essentially a software announcement. The core scientific claims regarding the tool's capabilities and performance are not substantiated by any data in the supplied material. The assessment of the tool's validity, accuracy, and utility cannot be made from the current evidence base. The manuscript is well-written and clear in its scope, but the lack of validation data is a major shortcoming for a scientific publication.
- **Who would be interested in the results, and why** Structural biologists, computational biophysicists, and researchers studying intrinsically disordered proteins (IDPs) would be interested. The tool addresses a practical bottleneck in building complete all-atom models of proteins for downstream simulations or analysis. The specific capabilities for phosphorylation sites and transmembrane proteins broaden the potential user base within these subfields.
- **Major strengths** The tool addresses a clear and important gap in the field. The software is presented as open-source, integrated into an existing and validated platform, and is designed for ease of use via both API and command line. The modular design is a positive feature for maintainability and extension.
- **Major Concerns** The primary concern is the complete absence of validation data in the provided text. The claims of "physically meaningful" ensembles and specific modeling capabilities are unsupported. The manuscript does not provide any benchmarks, case studies, or comparisons to experimental data or other methods. The scientific case for the tool's utility is therefore not established.
- **Minor Comments** The manuscript would benefit from a brief description of the algorithm's core principles in the Summary. The claim of "computational speed" is vague and should be quantified. The list of capabilities (phosphorylation, transmembrane, multi-chain) is presented as a list of features without any demonstration.
- **Technical failings that need to be addressed before the case is established** The lack of any validation data is the primary technical failing. The manuscript must include evidence that the generated ensembles are physically reasonable and that the tool performs as claimed. This includes, but is not limited to, validation against experimental data (e.g., SAXS, FRET, NMR), demonstration of sampling convergence, and a comparison with existing methods for modeling disordered regions.
- **Assessment against Nature-style criteria** 
  - **Originality** The concept of a modular tool for sampling disordered regions within a larger modeling suite is not entirely novel, but the specific combination of features (e.g., handling of phosphorylation, transmembrane contexts) may offer some originality. This is not fully assessable from the text.
  - **Scientific importance** The problem addressed is of high importance to the structural biology community. However, the importance of this specific tool is not demonstrated without validation.
  - **Interdisciplinary readership** The tool is relevant to computational biologists, structural biologists, and biophysicists. The writing is accessible to these groups.
  - **Technical soundness** Not assessable from the provided text. The algorithms are not described in sufficient detail, and no validation is presented.
  - **Readability for nonspecialists** The Summary is clear and accessible. The technical details are appropriately placed in the implementation section.
- **Recommendation posture** Currently not established from the provided evidence. The manuscript is a software description, but the scientific claims require substantial validation data to be convincing. The recommendation is to request major revisions that include a thorough validation section.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The tool "will automatically generate physically meaningful conformational ensembles of the missing flexible regions."
- **Evidence pointer** Summary; location not provided
- **Concern** The central claim of generating "physically meaningful" ensembles is not supported by any data in the provided text. No validation against experimental data, no comparison to known structures or other sampling methods, and no metrics of ensemble quality are presented.
- **Why it matters** This is the core scientific claim of the manuscript. Without evidence, the tool's utility and reliability are unknown. A reader cannot judge whether the output of LDRS is trustworthy for their research.
- **Resolution test** The authors must provide a validation section demonstrating that LDRS-generated ensembles reproduce experimental observables (e.g., SAXS profiles, FRET efficiencies, chemical shifts) for a set of test proteins with known disordered regions. The test should include a quantitative comparison of the generated ensembles to those from established methods.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The tool has "capabilities of modeling phosphorylation sites using enhanced Monte Carlo-Side Chain Entropy, transmembrane proteins within an all-atom bilayer, and multi-chain complexes."
- **Evidence pointer** Summary; location not provided
- **Concern** These are significant and specific capabilities, but they are only listed as features. There is no description of how these are implemented, no test cases, and no results demonstrating that these features work correctly.
- **Why it matters** These features are likely to be a major draw for potential users. If they are not properly implemented or validated, users may waste significant time and effort. The claims are currently unverifiable.
- **Resolution test** The authors should provide at least one case study for each of these three capabilities. For example, a phosphorylation site should be modeled and the resulting ensemble compared to a known or predicted structure. A transmembrane protein should be modeled in a bilayer and the ensemble's properties (e.g., membrane embedding) should be analyzed. A multi-chain complex should be modeled and the inter-chain contacts should be assessed for physical plausibility.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The tool "capitalizes on the modularity, the ability to be used as a library and via command-line, and the computational speed of the IDPConformerGenerator platform."
- **Evidence pointer** Summary; Availability and implementation; location not provided
- **Concern** The claim of "computational speed" is not quantified. No benchmarks are provided to show how fast the tool is or how it scales with system size. The modularity and usability are described, but not demonstrated.
- **Why it matters** Computational cost is a critical factor for users deciding whether to adopt a new tool. A vague claim of "speed" is not useful. The lack of benchmarks makes it impossible to compare LDRS to other tools or to estimate the resources required for a given modeling task.
- **Resolution test** The authors should provide a benchmark table showing the wall-clock time and memory usage for generating a defined number of conformers for a set of test proteins of varying sizes (e.g., 50, 100, 200, 400 residues). This should be compared to a relevant existing tool, if possible.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Readability for nonspecialists
- **Affected element** Summary
- **Evidence pointer** Summary; location not provided
- **Issue** The Summary does not explain the basic principle behind the LDRS sampling method. A reader unfamiliar with the IDPConformerGenerator platform will not understand how the tool works.
- **Required correction** Add one or two sentences in the Summary describing the core algorithm, e.g., how the disordered region is grown or sampled, and how the "enhanced Monte Carlo-Side Chain Entropy" method works.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Technical soundness
- **Affected element** Availability and implementation
- **Evidence pointer** Availability and implementation; location not provided
- **Issue** The text states that the tool works on "Mac OS versions that support DSSP." This is an unusual and potentially limiting statement. It is unclear if this is a limitation of LDRS or of the DSSP software itself.
- **Required correction** Clarify the statement. For example, specify the minimum required version of DSSP or explain that DSSP is a third-party dependency that must be installed separately.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Scientific importance
- **Affected element** Summary
- **Evidence pointer** Summary; location not provided
- **Issue** The Summary does not mention any potential limitations of the method. For example, are there any types of disordered regions or protein contexts that LDRS cannot handle?
- **Required correction** Add a sentence acknowledging known limitations, if any, to provide a balanced view of the tool's applicability.

## Risk / unsupported claims
- The claim that LDRS generates "physically meaningful" ensembles is unsupported by any data in the provided text.
- The specific capabilities for modeling phosphorylation sites, transmembrane proteins, and multi-chain complexes are unverified and lack any demonstration.
- The claim of "computational speed" is unquantified and cannot be evaluated.
- The overall utility and accuracy of the tool cannot be assessed from the supplied material.