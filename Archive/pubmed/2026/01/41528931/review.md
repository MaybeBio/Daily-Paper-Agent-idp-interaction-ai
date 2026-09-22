## Review setup
- **Input scope** Full manuscript text (abstract, introduction, methods, example application, conclusion) without supplementary materials or figures
- **Assessment boundary** Evaluation of the scientific claims, technical soundness, and presentation quality based solely on the provided text
- **Shared manuscript claim summary** The authors present the blobulator toolkit, a suite of tools (webtool, CLI, VMD plugin) for detecting, visualizing, and characterizing hydrophobic modules ("h-blobs") in protein sequences. The toolkit is based on a previously published algorithm ("blobulation") and is claimed to fill a gap in existing bioinformatics tools by providing modular hydrophobicity analysis with interactive visualization capabilities.
- **Visible evidence base** Abstract, Introduction, Blobulation algorithm description, Toolkit descriptions (webtool, CLI, VMD plugin), Example application on lysozyme, Conclusion
- **Missing materials affecting confidence** All figures, tables, supplementary materials (Text S1-S4, Figure S1), and the referenced prior publications (Lohia et al., 2019, 2022) are not available for verification. The example application on lysozyme references multiple figures (Figures 1-6) that are not provided.

## Reviewer
- **Overall assessment** The manuscript describes a potentially useful bioinformatics toolkit for hydrophobicity-based sequence analysis. The core algorithm is clearly described and the toolkit appears well-designed with multiple access points (webtool, CLI, VMD plugin). However, the scientific validation is limited to a single detailed example (lysozyme) with additional examples relegated to supplementary materials. The claims about the algorithm's utility and biological relevance rely heavily on prior publications that are not accessible for verification. The manuscript would benefit from more rigorous quantitative validation and clearer demonstration of the toolkit's advantages over existing approaches.

- **Who would be interested in the results, and why** Researchers studying protein sequence-structure relationships, particularly those working with intrinsically disordered proteins, membrane proteins, and proteins with known disease-associated mutations. The toolkit could also be useful for bioinformaticians developing pipelines for sequence analysis and for structural biologists using VMD who want to incorporate hydrophobicity-based segmentation into their visualization workflows.

- **Major strengths** 
  1. The manuscript addresses a genuine gap in available bioinformatics tools, as no existing tools focus specifically on modular hydrophobicity analysis
  2. The toolkit provides multiple access points (webtool, CLI, VMD plugin) making it accessible to users with different technical backgrounds
  3. The algorithm is clearly described with pseudocode provided in supplementary materials
  4. The example application on lysozyme demonstrates the toolkit's ability to identify biologically relevant hydrophobic regions
  5. The authors show sensitivity to single-residue mutations, which is a useful feature for studying disease-associated variants

- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors claim that blobulation provides a "deterministic, lightweight, and biophysically informed route to bioinformatics analyses" and that it is comparable to secondary structure prediction tools
- **Evidence pointer** Conclusion section, location not provided
- **Concern** The manuscript does not provide quantitative benchmarking of the blobulator against existing tools or against alternative approaches for hydrophobicity analysis. The claim of comparable runtime to secondary structure predictors is stated without supporting data. No performance metrics, accuracy assessments, or comparisons with other segmentation methods are presented.
- **Why it matters** Without quantitative benchmarking, it is impossible to assess whether the blobulator offers genuine advantages over existing approaches or whether the runtime claims are substantiated. This is critical for establishing the toolkit's utility for high-throughput applications.
- **Resolution test** Provide benchmarking data comparing blobulator runtime and output against existing tools (e.g., secondary structure predictors, hydrophobicity plotting tools) on a standardized dataset. Include accuracy metrics for blob detection against experimentally validated hydrophobic regions.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Scientific importance
- **Claim pointer** The authors claim that "disease-associated single-nucleotide polymorphisms are more likely to be found in contiguously hydrophobic regions and are particularly likely to bridge two such regions" and that mutations that "split, dissolve, or merge h-blobs are enriched for deleterious mutations"
- **Evidence pointer** Introduction section, Example Application section, location not provided
- **Concern** These claims are presented as established findings from prior work, but the supporting evidence is not provided in this manuscript. The lysozyme example shows two mutations that alter blob topology, but this is anecdotal evidence from a single protein. The statistical enrichment claims require large-scale validation that is not presented here.
- **Why it matters** The biological significance of blobulation depends on these claims. If the association with disease mutations is not robustly demonstrated, the toolkit's relevance for clinical or genetic applications is weakened.
- **Resolution test** Provide the statistical analysis supporting the enrichment claims, either by including the data in this manuscript or by clearly referencing the specific analyses in the prior publications with sufficient detail for verification.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Interdisciplinary readership
- **Claim pointer** The authors state that the webtool provides "accessible, interactive, and scalable implementations" and that users can "interactively tune" parameters
- **Evidence pointer** Webtool section, location not provided
- **Concern** The manuscript describes the webtool's features but does not provide any usability assessment, user testing, or demonstration of the tool's interface. The claim of accessibility is not supported by evidence. Additionally, the manuscript does not discuss potential limitations of the webtool (e.g., maximum sequence length, server capacity, browser compatibility).
- **Why it matters** For a toolkit paper, usability and accessibility are central claims. Without evidence of user testing or performance under realistic conditions, the practical utility of the webtool is uncertain.
- **Resolution test** Include a usability assessment (e.g., user testing results, response time measurements) or at minimum a detailed description of the webtool's interface and any known limitations.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Technical soundness
- **Claim pointer** The authors claim that the VMD plugin allows users to "view blobs on protein structures" and analyze them "across simulation trajectories"
- **Evidence pointer** VMD Plugin section, location not provided
- **Concern** The description of the VMD plugin is brief and lacks technical details. The manuscript does not explain how blob information is mapped onto protein structures, how the plugin handles different structure formats, or how it performs across trajectories. The claim of "maximum compatibility" is not substantiated.
- **Why it matters** The VMD plugin is a key component of the toolkit, and its functionality is central to the visualization claims. Insufficient technical detail makes it difficult for potential users to assess whether the plugin will work for their specific use cases.
- **Resolution test** Provide a more detailed technical description of the VMD plugin, including supported structure formats, trajectory handling, and any known limitations. Include example scripts or usage scenarios.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Readability for nonspecialists
- **Affected element** Introduction section
- **Evidence pointer** Introduction, location not provided
- **Issue** The introduction assumes familiarity with hydrophobicity scales and their applications. The concept of "blobulation" is introduced without a clear intuitive explanation of why contiguous hydrophobicity is biologically meaningful.
- **Required correction** Add a brief, accessible explanation of why hydrophobic modularity matters for protein function, perhaps with a simple analogy or illustrative example.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Technical soundness
- **Affected element** Blobulation algorithm description
- **Evidence pointer** Blobulation section, location not provided
- **Issue** The description of the smoothing step (step 1b) is unclear. The manuscript states that hydropathies are "smoothed for each residue i and the residues adjacent to it in sequence (i - 1, i, and i + 1)" but does not specify the smoothing method (e.g., moving average, weighted average).
- **Required correction** Specify the exact smoothing algorithm and provide the mathematical formula or pseudocode for this step.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Scientific importance
- **Affected element** Example Application section
- **Evidence pointer** Example Application: Lysozyme, location not provided
- **Concern** The lysozyme example is described in detail, but the manuscript does not explain why lysozyme was chosen as the primary example or how representative it is of typical use cases.
- **Required correction** Briefly justify the choice of lysozyme as the example protein and discuss how the findings might generalize to other protein classes.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Readability for nonspecialists
- **Affected element** Conclusion section
- **Evidence pointer** Conclusion, location not provided
- **Issue** The conclusion mentions "Janus regions on the Das-Pappu phase diagram" without explaining what this means for readers unfamiliar with this concept.
- **Required correction** Add a brief explanation of Janus regions and the Das-Pappu phase diagram, or remove this reference if it is not essential to the main argument.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Technical soundness
- **Affected element** Webtool section
- **Evidence pointer** Webtool section, location not provided
- **Issue** The manuscript states that the webtool accepts "either a database ID or manually enter a protein sequence" but does not specify which databases are supported (e.g., UniProt, PDB).
- **Required correction** List the supported database identifiers and provide examples of valid input formats.

- **Concern ID** R1-m6
- **Severity** Minor
- **Axis** Interdisciplinary readership
- **Affected element** Toolkit description
- **Evidence pointer** The Blobulator Toolkit section, location not provided
- **Issue** The manuscript does not discuss the computational requirements of the toolkit (e.g., memory usage, processing time for typical sequences) or the programming language and dependencies for the CLI.
- **Required correction** Add a brief section on system requirements and dependencies, including Python version and required packages.

## Risk / unsupported claims
- The claim that blobulation is "critical" for interpreting IDP simulations and defining "local context" around disease mutations is not verifiable from this manuscript alone, as it relies on prior publications not provided.
- The claim that the toolkit provides "previously unavailable functionality" is not fully substantiated, as the manuscript does not provide a comprehensive survey of existing tools to demonstrate this gap.
- The statement that blobulation "scales about four times more efficiently with sequence length" compared to secondary structure predictors is unsupported by any data in the manuscript.
- The biological significance claims about blob topology changes in disease-associated mutations are based on anecdotal evidence from the lysozyme example and prior work not accessible for review.
- The claim that the VMD plugin enables "publication-quality images and movies" is not demonstrated with any example outputs.
- The manuscript states that "both mutations change the blob topology" for S117V and T157I, but the functional significance of these changes is speculative and not experimentally validated.
- The assertion that "AlphaFold predicts minimal structural differences between these mutants and the wild type" is presented without showing the actual predictions or RMSD values.
- The claim that the toolkit is "accessible" and "interactive" is not supported by any usability data or user feedback beyond the acknowledgements mentioning three testers.