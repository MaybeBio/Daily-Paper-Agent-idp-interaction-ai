## Review setup
- **Input scope** Full manuscript text (main text, methods, and supplementary figure/table references as described)
- **Assessment boundary** Scientific claims, methodology, evidence consistency, and interpretation as presented in the provided manuscript text
- **Shared manuscript claim summary** The authors report that the C-terminal domain of protein 4.1G, an intrinsically disordered protein (IDP), recognizes IDP regions of binding partners through a defined α/β structural module formed via synergetic folding. They combine DHFR PCA mutational analysis, AlphaFold2 (AF2) structure prediction, ABACUS-R sequence design, X-ray crystallography of a designed mutant, NMR, MDS, and MALS to support this model and to predict and validate new binding partners.
- **Visible evidence base** Main text figures (Fig. 1A–D, 2A–D, 3A–C, 4A–D, 5A–D), SI Appendix figures (S1–S14), SI Appendix Table S1 (crystallographic statistics) and Table S2 (candidate fragments), deposited data (Zenodo, PDB 8I8Y)
- **Missing materials affecting confidence** The SI Appendix itself is not provided; only references to its figures and tables are visible. Crystallographic statistics, full enrichment ratio datasets, and detailed sequence alignments are therefore not directly assessable. The REMD simulation details from prior work (ref 9) are referenced but not described. The exact AF2 confidence metrics (e.g., PAE) are not shown.

## Reviewer
- **Overall assessment** This is a well-conceived and carefully executed study that addresses a challenging problem in IDP biology. The integration of deep learning-based structure prediction, computational design, and multiple experimental validations is impressive and largely convincing. The central claim, that a specific α/β module formed by synergetic folding underlies 4.1G CTD target recognition, is supported by multiple convergent lines of evidence. However, the study relies heavily on a single crystal structure of a designed mutant, and the extrapolation to the wild-type complex and to other partners requires careful scrutiny. The manuscript is clearly written and will be of broad interest, but several technical and interpretive issues need to be addressed.
- **Who would be interested in the results, and why** Structural biologists, biochemists, and cell biologists studying IDPs, protein-protein interactions, and molecular recognition. The work also has relevance for the community using deep learning tools for structure prediction of challenging systems, and for those interested in the limits and applications of computational protein design. The demonstration that a "fuzzy" complex can have a defined core structure is conceptually important.
- **Major strengths**
  1. The study tackles a difficult and important problem: the structural basis of IDP-IDP recognition.
  2. The combination of computational prediction (AF2), design (ABACUS-R), and multiple experimental methods (PCA, crystallography, NMR, MALS, MD) is powerful and mutually reinforcing.
  3. The use of saturation mutagenesis and high-throughput sequencing to validate structural models is rigorous and provides a strong link between sequence and structure.
  4. The crystal structure of the designed mutant provides direct structural evidence, and the consistency between the predicted and experimental structures is compelling.
  5. The authors are appropriately cautious about the limitations of AF2 for IDP complexes and provide complementary evidence.
- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence sufficiency
- **Claim pointer** The crystal structure of the designed mutant B5 represents the structure of the wild-type 4.1G57-NuMA16 complex.
- **Evidence pointer** Section "The Crystal Structure of a Fusion Peptide with Designed Mutations", Fig. 1C, Fig. 3A
- **Concern** The crystal structure was obtained for a quadruple mutant (B5) designed to stabilize the complex, not for the wild-type complex. While the authors argue that the wild-type sequence is highly compatible with the structure (based on ABACUS-R analysis), this is an indirect argument. The mutations in B5 could, in principle, induce a different conformation that is not representative of the native complex. The authors do not provide direct experimental evidence (e.g., NMR structure of the wild-type complex, or a structure of a complex with a different set of mutations) that the wild-type complex adopts the same fold.
- **Why it matters** The central claim of the paper is that the identified α/β module is the recognition mechanism for the wild-type proteins. If the crystal structure is an artifact of the stabilizing mutations, the entire mechanistic conclusion is weakened.
- **Resolution test** Provide additional evidence that the wild-type complex adopts the same structure. This could include: (1) NMR-based structural restraints (e.g., chemical shift perturbations, NOEs) on the wild-type complex that are consistent with the crystal structure; (2) a crystal structure of a different designed mutant that retains the same fold; (3) cross-linking mass spectrometry data on the wild-type complex; or (4) a demonstration that the wild-type complex and the B5 mutant have very similar binding affinities and that the B5 mutations do not alter the binding interface (e.g., via HDX-MS).

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** No
- **Axis** Interpretive validity
- **Claim pointer** The electrostatic interactions between the oppositely charged C-terminal region of 4.1G57 and the N-terminal region of NuMA26 contribute to binding but are not the major driving force.
- **Evidence pointer** Section "Essential Regions and Key Residues Identified by DHFR PCA", SI Appendix Fig. S3
- **Concern** The conclusion that electrostatics are secondary is based on the observation that mutating charged residues to opposite charges weakens but does not eliminate binding, and that charge-reversal mutations on both partners do not fully recover binding. However, the interpretation of these results is complicated by the fact that the mutations could affect protein stability, expression, or folding, not just the direct electrostatic interaction. The authors acknowledge this possibility for the PCA results in general, but the specific conclusion about electrostatics relies on these data.
- **Why it matters** The relative contribution of hydrophobic vs. electrostatic forces to binding is a key mechanistic claim. If the interpretation is flawed, the proposed model of "synergetic folding" driven primarily by hydrophobic burial could be incorrect.
- **Resolution test** Perform direct binding measurements (e.g., ITC) with the charge-reversal mutants to confirm that the effects observed in PCA are due to changes in binding affinity and not to indirect effects. Alternatively, use a more quantitative approach, such as measuring the salt dependence of binding, to assess the electrostatic contribution.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Generalizability
- **Claim pointer** The identified α/β module is the preferred mode used by 4.1G CTD to recognize its various ligands.
- **Evidence pointer** Section "Prediction and Assessment of Other 4.1G CTD-Binding Regions", Fig. 5A–D
- **Concern** The authors used AF2 to scan for potential binding regions in 10 known partners and found 7 that interact. However, the positive rate is low (7/38 tested fragments), and the authors do not provide a clear explanation for why many high-confidence AF2 predictions did not show binding. This raises questions about the predictive power of the approach and whether the identified module is truly universal. The authors state that compatibility with the core structure is necessary but insufficient, but this is a post-hoc explanation.
- **Why it matters** The claim that this is a general recognition mechanism for 4.1G CTD is a key part of the paper's significance. If the approach only works for a subset of partners, the generality of the mechanism is questionable.
- **Resolution test** Provide a more detailed analysis of the negative results. For example, are there structural or sequence features that distinguish the positive from the negative fragments? Could the negative results be due to experimental limitations (e.g., expression, solubility) rather than a lack of binding? A more systematic analysis would strengthen the claim of generality.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Technical soundness
- **Claim pointer** The MD simulations show that the complex structure is stable in solution.
- **Evidence pointer** Section "The Structure in Solution Is Ordered but Dynamic", SI Appendix Fig. S12
- **Concern** The MD simulations were started from a model based on the crystal structure of the B5 mutant, not the wild-type complex. The simulations therefore cannot independently validate the wild-type structure. Furthermore, the simulation length (200 ns) is relatively short for a system of this size, and the authors do not report on the convergence of the simulations or the structural fluctuations in detail.
- **Why it matters** The MD simulations are used to support the claim that the crystal structure is representative of the solution state. If the simulations are biased by the starting structure and are not well-converged, this support is weak.
- **Resolution test** Provide more detailed MD analysis, including RMSF, secondary structure stability over time, and a comparison of the simulated ensemble with the NMR data. Consider running longer simulations or multiple replicas to ensure convergence.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Figure 2A
- **Evidence pointer** Section "Essential Regions and Key Residues Identified by DHFR PCA", Fig. 2A
- **Issue** The naming convention for the fragments (4.1G57, 4.1G57′, NuMA26, NuMA16) is not immediately intuitive. The exact residue ranges for each fragment are given in Fig. 2A, but this is not stated in the main text.
- **Required correction** Briefly state the residue ranges of the fragments in the main text when they are first introduced.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Methods section
- **Evidence pointer** Section "Materials and Methods"
- **Issue** The methods for the saturation mutagenesis library construction and high-throughput sequencing are described, but the analysis pipeline for calculating enrichment ratios is not fully detailed. The authors mention a pseudocount and normalization, but the exact formula and statistical tests used are not provided.
- **Required correction** Provide a more detailed description of the enrichment ratio calculation, including the formula, normalization, and any statistical thresholds used to define "hits."

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Interpretation
- **Affected element** Discussion section
- **Evidence pointer** Section "Discussion"
- **Issue** The authors contrast their findings with the "fuzzy complex" model, but they do not discuss how their results relate to other models of IDP binding, such as "conformational selection" vs. "induced fit." The term "synergetic folding" is used, but the distinction from "mutually induced folding" is not clearly articulated.
- **Required correction** Briefly discuss the relationship between the proposed mechanism and other models of IDP binding, and clarify the definition of "synergetic folding" as used here.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Presentation
- **Affected element** Figure 3C
- **Evidence pointer** Section "The Crystal Structure Can Represent the Complex in Solution", Fig. 3C
- **Issue** The enrichment ratio data in Fig. 3C are presented as a heatmap, but the color scale and the exact values are not described in the figure legend or the main text.
- **Required correction** Add a clear description of the color scale and the range of enrichment ratios shown in Fig. 3C.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Reproducibility
- **Affected element** Methods section
- **Evidence pointer** Section "Materials and Methods", "Crystallography"
- **Issue** The crystallization condition is described, but the final refinement statistics (R-factor, R-free, Ramachandran statistics) are only in SI Appendix Table S1, which is not provided. The resolution of the structure is mentioned (2.9 Å), but the completeness and multiplicity of the data are not stated.
- **Required correction** Ensure that the SI Appendix Table S1 includes all relevant crystallographic statistics and that these are summarized in the main text.

## Risk / unsupported claims
- The claim that the crystal structure of the B5 mutant represents the wild-type complex is not directly supported by experimental evidence on the wild-type complex. This is a key inference that needs additional support.
- The claim that the identified α/β module is the "preferred mode" for all 4.1G CTD partners is not fully supported, given the low hit rate in the AF2 scan and the lack of a detailed analysis of the negative results.
- The conclusion that electrostatic interactions are secondary to hydrophobic packing is based on indirect PCA data and needs confirmation with direct binding measurements.
- The MD simulations, starting from the mutant structure, cannot independently validate the wild-type solution structure.
- The generalizability of the "synergetic folding" mechanism to other IDP-IDP systems is speculative and not directly tested.