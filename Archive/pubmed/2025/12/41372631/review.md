## Review setup
- **Input scope** Full manuscript text, including abstract, introduction, results, discussion, methods, and figure legends
- **Assessment boundary** Scientific content, technical soundness, logical coherence, and support of claims by presented evidence
- **Shared manuscript claim summary** The authors investigate phosphorylated HP1α (pHP1α) liquid-liquid phase separation (LLPS) and its interactions with chromatin and DNA. They report that pHP1α self-association is driven by electrostatic interactions between the phosphorylated N-terminal extension (NTE) and the hinge region, that pHP1α binds nucleosomes via CD recognition of H3K9me3, and that free DNA competes with the NTE for hinge region binding, thereby modulating LLPS.
- **Visible evidence base** NMR spectroscopy (chemical shift assignments, CSPs, intensity changes), confocal and optical microscopy, FRAP, MD simulations, mass spectrometry validation of histone modification
- **Missing materials affecting confidence** Supplementary figures referenced but not provided; raw NMR spectra not shown; MD simulation convergence metrics not fully described; no quantitative binding affinities; no negative controls for LLPS experiments; no statistical analysis for MD contact maps

## Reviewer
- **Overall assessment** The manuscript addresses an important question regarding the molecular determinants of pHP1α LLPS and its interactions with chromatin. The combination of NMR, microscopy, and MD simulations is appropriate and potentially powerful. However, several technical concerns limit the strength of the conclusions as currently presented. The claim that NTE-hinge interactions are the primary drivers of pHP1α self-association requires stronger quantitative support. The comparison between telomeric and Widom 601 nucleosome arrays is interesting but the mechanistic interpretation is speculative. The DNA competition model is plausible but needs more direct evidence. The manuscript would benefit from additional controls and more rigorous quantitative analysis.
- **Who would be interested in the results, and why** Researchers studying heterochromatin biology, phase separation mechanisms, chromatin structure and epigenetics, and those interested in the biophysical properties of chromatin-associated proteins. The findings on how phosphorylation modulates LLPS and nucleosome interactions have implications for understanding heterochromatin formation and gene silencing.
- **Major strengths** The study combines multiple complementary techniques to address a complex biological question. The NMR approach provides site-specific information that is often lacking in LLPS studies. The comparison between different nucleosome array types is thoughtful and addresses a relevant biological question. The identification of specific residues involved in intermolecular interactions is valuable.
- **Major Concerns** See detailed items below.
- **Minor Comments** See detailed items below.
- **Technical failings that need to be addressed before the case is established** R1-M1, R1-M2, R1-M3, R1-M4
- **Assessment against Nature-style criteria** Originality: The work is original in its site-specific NMR characterization of pHP1α in LLPS contexts, though the general phenomenon of HP1α LLPS has been reported. Scientific importance: The findings have potential importance for understanding heterochromatin regulation, but the mechanistic claims require stronger support. Interdisciplinary readership: The work bridges biophysics, structural biology, and chromatin biology, which would appeal to a broad readership. Technical soundness: The NMR methodology appears sound, but several quantitative aspects and controls are lacking. Readability for nonspecialists: The manuscript is generally well-written but assumes significant background knowledge in NMR spectroscopy and phase separation biology.
- **Recommendation posture** Supportive if technical concerns are resolved

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence sufficiency
- **Claim pointer** The authors claim that "the interaction of pHP1α and nucleosomes is driven by the self-association of pHP1α mediated by intermolecular interaction between the NTE and hinge regions and the specific binding of the pHP1α chromo domain (CD) to the N-terminal histone tail of H3K9me3 in the nucleosomes."
- **Evidence pointer** Results section, Figures 2 and 3
- **Concern** The claim that NTE-hinge interactions are the primary drivers of pHP1α self-association is based on CSP and intensity changes in NMR spectra, but the quantitative contribution of these interactions relative to other regions is not established. The MD simulations show contacts at 80 ns from a single 100-ns trajectory, which is insufficient to demonstrate convergence or statistical significance. The authors state that "the self-interactions within pHP1α, mediated by the NTE and hinge regions, are relatively weaker during the compaction of the more relaxed Widom 601 nucleosome arrays compared to the more tightly stacked telomeric nucleosome arrays," but this is presented as a "putative explanation" without direct evidence. The relative contributions of CD-H3K9me3 binding versus NTE-hinge self-association to the overall LLPS process are not quantitatively deconvoluted.
- **Why it matters** The central mechanistic claim of the paper rests on the relative importance of these interactions. Without quantitative assessment, the model remains speculative.
- **Resolution test** Provide quantitative analysis of interaction contributions, such as mutagenesis experiments disrupting NTE-hinge interactions and assessing effects on LLPS; perform multiple independent MD simulations with convergence analysis; or provide binding affinity measurements for the identified interactions.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical rigor
- **Claim pointer** The authors state that "the addition of DNA perturbs the LLPS propensity of pHP1α" and that "histone-free DNA can compete to form electrostatic attractions with positively charged amino acids in the NTE and hinge regions."
- **Evidence pointer** Results section, Figure 4
- **Concern** The DNA competition model is based on NMR CSP and intensity changes, but the interpretation that DNA competes with NTE for hinge binding is inferred rather than directly demonstrated. The authors do not show whether DNA binding to pHP1α is competitive with NTE-hinge interactions or whether it occurs at distinct sites. The claim that "the NTE is mostly affected in this DNA-mediated protein LLPS" is based on CSP data, but the functional significance of these changes for LLPS is not directly tested. The optical microscopy data show qualitative changes in droplet formation but lack quantitative analysis of droplet properties (size, number, viscosity) across DNA concentrations.
- **Why it matters** The proposed competition mechanism is a key novel finding. If not rigorously supported, the conclusion is weakened.
- **Resolution test** Perform competition experiments with defined components, such as pre-formed pHP1α condensates titrated with DNA and monitored by microscopy and NMR; use mutants that specifically disrupt NTE-hinge interactions to test whether DNA effects are mediated through this interface; provide quantitative droplet characterization across DNA concentrations.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence sufficiency
- **Claim pointer** The authors claim that "the unique columnar structure of telomeric chromatin facilitates a stronger interaction with pHP1α compared to the Widom 601 DNA nucleosome arrays under LLPS conditions."
- **Evidence pointer** Results section, Figure 3 and Supplementary Figures S8-S11
- **Concern** The comparison between telomeric and Widom 601 nucleosome arrays is based on NMR data from different constructs (4x157 bp telomeric vs 12x177 bp Widom 601) and different experimental conditions. The authors do not provide a direct, controlled comparison under identical conditions. The claim that the columnar structure of telomeric chromatin leads to stronger interactions is speculative and not directly tested. The authors do not account for potential differences in nucleosome occupancy, modification status, or array length between the two constructs.
- **Why it matters** The differential interaction with telomeric versus canonical chromatin is a significant claim with implications for telomere biology. Without controlled comparison, this conclusion is not established.
- **Resolution test** Perform side-by-side comparisons using matched array lengths and modification states; directly test the role of columnar packing by comparing telomeric arrays with engineered arrays of similar compaction; provide structural or biophysical evidence for the proposed stronger interaction.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical rigor
- **Claim pointer** The authors state that "the phosphorylation of HP1α does not alter its structure significantly" based on NMR data.
- **Evidence pointer** Results section, Figure 1 and Figure S3
- **Concern** The comparison between pHP1α and unphosphorylated HP1α is only briefly described, and the authors state that "excellent peak overlap for the majority of residues" was observed. However, the extent of phosphorylation is not quantified, and the authors do not demonstrate that the phosphorylation is complete or uniform. The statement that phosphorylation does not change the structure is based on limited analysis, and the authors do not show whether the phosphorylated residues themselves show structural changes or altered dynamics. The functional significance of phosphorylation for LLPS is not directly compared between phosphorylated and unphosphorylated forms under identical conditions.
- **Why it matters** The role of phosphorylation in modulating HP1α structure and function is a key aspect of the study. If the phosphorylation state is not well-defined, the conclusions are compromised.
- **Resolution test** Quantify phosphorylation stoichiometry (e.g., by mass spectrometry); provide direct comparison of pHP1α and HP1α under identical LLPS conditions; show residue-specific structural and dynamic changes upon phosphorylation.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Abstract
- **Evidence pointer** Abstract
- **Issue** The abstract is dense and uses technical terminology without sufficient context for a general readership. The phrase "site-specific molecular features" is vague and could be more specific.
- **Required correction** Consider revising the abstract to provide more context for non-specialists and to more clearly state the specific molecular features identified.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Reproducibility
- **Affected element** Methods, MD simulation section
- **Evidence pointer** Methods section, MD simulation
- **Issue** The MD simulation methods are described briefly. The force field parameters for phosphorylated residues are not specified, and the simulation box size, number of ions, and equilibration protocol are not fully described. The convergence criteria for the 100-ns simulation are not stated.
- **Required correction** Provide complete simulation parameters, including force field parameters for phosphorylated residues, system setup, and convergence analysis.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Statistical rigor
- **Affected element** Figure 2, FRAP data
- **Evidence pointer** Figure 2b, c
- **Issue** The FRAP data are described as representing three replicates, but the variability between replicates is not shown. The recovery curves appear to be averaged without error bars or statistical comparison.
- **Required correction** Show individual replicate data or error bars on the recovery curves, and provide statistical analysis comparing conditions.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Interpretation
- **Affected element** Discussion
- **Evidence pointer** Discussion section
- **Issue** The discussion introduces the concept of "selective molecular partitioning" and references other proteins involved in HP1α-mediated phase separation, but these points are not directly connected to the experimental results presented.
- **Required correction** Either connect these broader implications more explicitly to the specific findings, or remove them to maintain focus.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Figure 5
- **Evidence pointer** Figure 5
- **Issue** The proposed interaction model in Figure 5 is schematic and not directly supported by structural data. The relative orientations and stoichiometries of the interactions are speculative.
- **Required correction** Clearly label the model as a working hypothesis and indicate which aspects are directly supported by data versus inferred.

## Risk / unsupported claims
- The claim that NTE-hinge interactions are the "primary" drivers of pHP1α self-association is not quantitatively supported.
- The claim that telomeric chromatin columnar structure leads to stronger interactions with pHP1α is speculative and not directly tested.
- The DNA competition model is inferred from CSP data without direct competition experiments.
- The statement that phosphorylation does not change HP1α structure is based on limited analysis without quantification of phosphorylation stoichiometry.
- The proposed interaction modes in Figure 5 are not directly supported by structural data.
- The functional significance of the identified interactions for LLPS properties (e.g., viscosity, dynamics) is not directly measured.