## Review setup
- **Input scope** Full manuscript text (abstract, introduction, results, discussion, materials and methods) as provided
- **Assessment boundary** Scientific content, experimental design, data interpretation, and claims as presented in the provided text; no external data or supplementary files were assessed
- **Shared manuscript claim summary** The authors propose that Arabidopsis Tudor staphylococcal nuclease (TSN) is an intrinsically disordered protein that acts as a scaffold or docking platform for stress granule (SG) components, forming a pre-existing protein-protein interaction network before stress, and that TSN and SG formation are required for heat-induced activation of SnRK1 kinase and downstream signalling.
- **Visible evidence base** Proteomics (TSN2 and RBP47 interactomes under NS, HS, salt), co-localisation studies, BiFC, FRET, FRAP, immunoblotting for phospho-SnRK1α, RT-qPCR of SnRK1 target genes, mutant phenotyping (tsn1 tsn2, snrk1α1 −/− snrk1α2 −/+), complementation experiments
- **Missing materials affecting confidence** Figures and figure legends (referenced but not provided), supplementary datasets (EV1-EV5, Appendix figures and tables), full statistical details, raw mass spectrometry data, details of antibody validation, and complete experimental replicates

## Reviewer

### Overall assessment
This manuscript addresses an important and timely question in plant stress biology: the molecular composition and function of stress granules, and the role of the conserved protein TSN in their assembly and downstream signalling. The work combines proteomics, cell biology, genetics, and biochemistry to propose a model in which TSN acts as a pre-existing scaffold for SG components and is required for heat-induced SnRK1 activation. The topic is of broad interest, and the data presented are potentially valuable. However, several major concerns limit the strength of the conclusions as currently presented. The claim that TSN is a "docking platform" for SG components is supported by interaction data, but the functional evidence that this platform is essential for SnRK1 activation is incomplete. The genetic rescue experiments, the specificity of the SnRK1 activation phenotype, and the mechanistic link between SG formation and kinase activation require further substantiation. The manuscript would be strengthened by additional experiments and by more cautious interpretation of correlative data.

### Who would be interested in the results, and why
Plant stress biologists, particularly those studying stress granule biology, phase separation, and energy signalling (SnRK1/AMPK/SNF1 pathways). The work also has relevance for researchers studying the conserved functions of TSN/Tudor-SN proteins in RNA metabolism and stress responses across eukaryotes, and for those interested in the intersection of biomolecular condensates and kinase signalling. The proposed link between SG formation and SnRK1 activation could have implications for understanding how plants integrate stress signals with metabolic and growth responses.

### Major strengths
1. The study addresses a significant gap in plant biology: the composition and function of plant stress granules, which are far less characterised than their yeast and mammalian counterparts.
2. The combination of proteomics (TSN2 and RBP47 interactomes) with validation by co-localisation, BiFC, FRET, and co-immunoprecipitation provides a multi-layered approach to identify and verify protein-protein interactions.
3. The finding that TSN is an intrinsically disordered protein with a highly disordered N-terminal region is interesting and mechanistically plausible in the context of phase separation and scaffold function.
4. The demonstration that TSN deficiency alters the number and size of SnRK1α foci, and that TSN is required for heat-induced SnRK1α phosphorylation and target gene expression, provides a novel functional link between SG components and energy signalling.
5. The use of multiple Arabidopsis mutants (tsn1 tsn2, snrk1α1 −/− snrk1α2 −/+) and complementation adds genetic rigour.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Experimental support for central claim
- **Claim pointer** The authors claim that TSN is "essential for SnRK1 activation" in Arabidopsis under heat stress.
- **Evidence pointer** Figure 8 (referenced); Results section "TSN and SGs confer heat-induced activation of SnRK1"
- **Concern** The central claim that TSN is essential for SnRK1 activation is based on the observation that tsn1 tsn2 mutants show reduced heat-induced phosphorylation of SnRK1α at Thr175 and reduced expression of SnRK1 target genes (DIN2, DIN6). However, the manuscript does not provide evidence that this effect is specific to TSN's role in SGs. TSN has multiple functions in RNA metabolism, and its loss could affect SnRK1 activation indirectly through global changes in gene expression, mRNA stability, or protein homeostasis. The authors show that complementation with TSN2 rescues the phenotype, but this does not distinguish between a direct role in SG-mediated SnRK1 activation and a more general requirement for TSN in stress responses. Furthermore, the claim that SG formation itself is required for SnRK1 activation is based on the CHX experiment, which is a blunt tool that inhibits translation globally and may have many off-target effects. The manuscript lacks a more specific perturbation of SG assembly (e.g., mutation of a core SG component) to test this requirement.
- **Why it matters** The title and abstract make a strong causal claim: TSN is essential for SnRK1 activation. If the effect is indirect or non-specific, the central message of the paper is overstated. The distinction between TSN as a specific scaffold for SnRK1 activation versus TSN as a general stress-response factor is critical for the paper's significance.
- **Resolution test** Provide evidence that the effect on SnRK1 phosphorylation is specific to the TSN-SG axis. This could include: (i) rescue of the tsn1 tsn2 phenotype with a TSN2 variant that cannot localise to SGs or cannot interact with SnRK1α; (ii) analysis of SnRK1 activation in mutants of other core SG components (e.g., RBP47 knockdown); (iii) in vitro or in vivo evidence that TSN directly promotes SnRK1α phosphorylation by upstream kinases (e.g., SnRK1-activating kinases); (iv) demonstration that the effect is not due to global changes in protein synthesis or stress responses.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Quantitative data and statistical rigour
- **Claim pointer** The authors state that TSN deficiency leads to a "significant decrease in the number of SnRK1α foci and a simultaneous increase in their size" (Figure 7E, F), and that TSN is required for "full mobility of the SnRK1α1 isoform" (Figure 7G, H).
- **Evidence pointer** Figure 7 (referenced); Results section "TSN interacts with and mediates assembly of SnRK1α in heat SGs"
- **Concern** The manuscript does not provide details on the number of biological replicates, the number of cells/foci analysed, the statistical tests used, or the effect sizes for the quantitative imaging data (foci number, size, FRAP recovery). Without this information, it is impossible to assess the robustness of the conclusions. The FRAP data, in particular, are complex to interpret and require careful controls (e.g., for photobleaching depth, mobile vs. immobile fractions, and cell-to-cell variability). The claim that TSN is required for "full mobility" of SnRK1α1 is based on a single FRAP experiment (as described), and the manuscript does not report the mobile fraction or the half-time of recovery, which are standard parameters.
- **Why it matters** The quantitative imaging data are central to the claim that TSN mediates the assembly and dynamics of SnRK1α in SGs. If these data are not statistically robust, the conclusion is weakened. The FRAP data, in particular, are used to support a mechanistic claim about TSN's role in SG dynamics, and this requires rigorous analysis.
- **Resolution test** Provide full statistical details for all quantitative imaging data, including: (i) number of independent experiments (biological replicates); (ii) number of cells/foci analysed per condition; (iii) statistical test used and p-values; (iv) effect sizes with confidence intervals. For FRAP, report the mobile fraction, half-time of recovery, and the number of cells analysed, and ensure that the analysis is blinded where possible.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Specificity of the TSN-SnRK1α interaction
- **Claim pointer** The authors claim that TSN interacts with SnRK1α1 and SnRK1α2 (Figure 7A, B) and that this interaction is mediated by the N-terminal SN domain (Figure 4D).
- **Evidence pointer** Figure 7A, B (referenced); Figure 4D (referenced); Results section "TSN interacts with and mediates assembly of SnRK1α in heat SGs"
- **Concern** The manuscript does not provide evidence that the TSN-SnRK1α interaction is direct. The co-immunoprecipitation experiments (Figure 7A, B) were performed in plant extracts and could be mediated by bridging proteins or RNA. The BiFC experiments (Figure 4D) show that the SN domain of TSN is sufficient for interaction with SnRK1α, but BiFC can produce false positives due to non-specific association of the split YFP fragments at high expression levels. The manuscript does not include a negative control for the BiFC experiments (e.g., a mutated TSN variant that cannot interact, or a non-interacting protein pair). The FRET experiments (Figure 7C) provide additional support, but the manuscript does not report the FRET efficiency values or the number of cells analysed.
- **Why it matters** The claim that TSN is a "docking platform" for SG components, including SnRK1α, implies a direct physical interaction. If the interaction is indirect, the model needs to be revised. The specificity of the interaction is also important for understanding the mechanism by which TSN promotes SnRK1 activation.
- **Resolution test** Provide evidence for a direct interaction, for example: (i) in vitro pull-down with recombinant proteins; (ii) co-immunoprecipitation after RNase treatment to rule out RNA-mediated bridging; (iii) a negative control for BiFC (e.g., a TSN variant with a mutated interaction surface, or a known non-interactor); (iv) report FRET efficiency values and the number of cells analysed.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Generalisability of the interactome data
- **Claim pointer** The authors state that "approximately 30% of TSN interactors are recruited to stress granules de novo upon stress perception, while 70% form a protein-protein interaction network present before the onset of stress."
- **Evidence pointer** Figure 1 (referenced); Results section "TSN forms a network of SG protein-protein interactions before the onset of stress"
- **Concern** This is a key quantitative claim, but the manuscript does not provide details on how the 30%/70% split was calculated. The classification of interactors as "stress-dependent" or "stress-independent" appears to be based on the presence/absence in the TSN2_NS vs TSN2_HS pools, but the criteria for inclusion (e.g., fold-change threshold, statistical significance) are not stated. The manuscript also does not discuss the potential for false positives/negatives in the proteomics data, or the possibility that some interactors may be present in both pools but with different stoichiometries. The overlap with the RBP47 SG proteome is also only partial, and the significance of this overlap is not fully discussed.
- **Why it matters** The claim that TSN forms a pre-existing network before stress is a central part of the proposed model. If the classification of interactors is not robust, the model is weakened. The quantitative split (30%/70%) is a memorable figure that may be cited, so it needs to be well-supported.
- **Resolution test** Provide a clear description of the criteria used to classify interactors as stress-dependent, stress-independent, or stress-sensitive, including the statistical thresholds. Provide a more detailed comparison of the TSN2 and RBP47 interactomes, including a discussion of the significance of the overlap and the potential reasons for the differences.

- **Concern ID** R1-M5
- **Severity** Major
- **Blocking** No
- **Axis** Mechanistic link between SG formation and SnRK1 activation
- **Claim pointer** The authors propose that SG formation promotes SnRK1 activation, based on the observation that CHX treatment (which prevents SG formation) also blocks heat-induced SnRK1α phosphorylation.
- **Evidence pointer** Figure 8B (referenced); Results section "TSN and SGs confer heat-induced activation of SnRK1"
- **Concern** The use of CHX to link SG formation to SnRK1 activation is problematic. CHX inhibits translation elongation, which has widespread effects on cellular physiology beyond SG formation. It is possible that CHX blocks SnRK1 activation through a mechanism unrelated to SGs (e.g., by affecting the synthesis of a protein required for SnRK1 activation, or by altering the cellular energy status). The manuscript does not provide a more specific test of the requirement for SGs in SnRK1 activation.
- **Why it matters** The claim that SG formation is required for SnRK1 activation is a novel and important finding. If the only evidence is the CHX experiment, the claim is not well-supported. A more specific perturbation of SG assembly would strengthen the paper considerably.
- **Resolution test** Use a more specific approach to disrupt SG formation, such as: (i) knockdown or knockout of a core SG nucleating protein (e.g., RBP47) and test SnRK1 activation; (ii) expression of a dominant-negative SG assembly factor; (iii) pharmacological inhibition of SG assembly with a more specific drug than CHX. Alternatively, provide evidence that the CHX effect is specifically due to SG disruption (e.g., by showing that CHX does not affect SnRK1 activation in a mutant that cannot form SGs).

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity of terminology
- **Affected element** Title and abstract
- **Evidence pointer** Title; Abstract
- **Issue** The term "docking platform" is used in the title and abstract, but the manuscript does not provide a clear definition of what constitutes a "docking platform" in this context. Is it a physical scaffold that nucleates SG assembly? A hub that organises protein-protein interactions? The term is evocative but potentially ambiguous.
- **Required correction** Define "docking platform" more precisely in the introduction or discussion, and ensure that the data presented support this specific definition.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Completeness of methods
- **Affected element** Methods section
- **Evidence pointer** Methods section "Liquid chromatography and mass spectrometry analysis for TAPa procedure"
- **Issue** The methods for mass spectrometry data analysis are described, but the manuscript does not state the number of biological replicates for the proteomics experiments. It is stated that "Two biological replicates were performed," but it is not clear if these are independent biological replicates or technical replicates.
- **Required correction** Clarify the number of independent biological replicates and whether the data were pooled or analysed separately.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Data presentation
- **Affected element** Figure 1
- **Evidence pointer** Figure 1 (referenced)
- **Issue** The manuscript states that "analysis of eggNOG orthologs revealed that ~20% of proteins from both TSN2_NS and TSN2_HS pools are known components of human or yeast SGs." It is not clear how this percentage was calculated and whether the overlap is statistically significant.
- **Required correction** Provide a more detailed description of the analysis, including the statistical test used to assess the significance of the overlap.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Interpretation of FRAP data
- **Affected element** Figure 7G, H
- **Evidence pointer** Figure 7G, H (referenced)
- **Issue** The FRAP data are interpreted as showing that TSN is required for "full mobility" of SnRK1α1. However, the manuscript does not report the mobile fraction or the half-time of recovery, which are the standard parameters used to interpret FRAP data. Without these values, it is difficult to assess the biological significance of the observed difference.
- **Required correction** Report the mobile fraction and half-time of recovery for the FRAP experiments, and discuss the implications of these values for SnRK1α1 dynamics in SGs.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Discussion of limitations
- **Affected element** Discussion
- **Evidence pointer** Discussion section
- **Issue** The discussion does not acknowledge the limitations of the study, such as the potential for indirect effects in the mutant analyses, the use of overexpression for some localisation studies, and the correlative nature of some of the data.
- **Required correction** Add a paragraph to the discussion acknowledging the limitations of the study and suggesting future experiments to address them.

### Technical failings that need to be addressed before the case is established
1. Lack of statistical details for quantitative imaging data (foci number, size, FRAP) - R1-M2
2. Lack of evidence for a direct TSN-SnRK1α interaction - R1-M3
3. The CHX experiment is insufficient to establish a causal link between SG formation and SnRK1 activation - R1-M4
4. The criteria for classifying interactors as stress-dependent vs stress-independent are not described - R1-M4

### Assessment against Nature-style criteria
- **Originality**: The work is original in its focus on plant stress granules and the specific link between TSN, SG assembly, and SnRK1 activation. The concept of a pre-existing interaction network that facilitates rapid SG assembly is not entirely new (similar ideas exist in the yeast/mammalian literature), but its application to plants and the specific involvement of TSN is novel.
- **Scientific importance**: The findings are potentially important for understanding how plants integrate stress signals with energy metabolism. The link between SG components and SnRK1 activation is a new connection that could have broad implications. However, the importance is currently tempered by the lack of mechanistic depth.
- **Interdisciplinary readership**: The topic is of interest to plant biologists, cell biologists studying phase separation, and biochemists studying kinase signalling. The writing is generally accessible, but the manuscript assumes familiarity with both plant stress responses and SG biology.
- **Technical soundness**: The experimental approaches are generally sound, but the lack of statistical detail and the reliance on correlative data for some of the key claims (particularly the CHX experiment) are weaknesses. The proteomics and imaging data are potentially valuable but need to be presented with more rigour.
- **Readability for nonspecialists**: The abstract is clear, but the results section is dense and would be challenging for a non-specialist. The manuscript would benefit from a more accessible summary of the key findings and their significance.

### Recommendation posture
**Supportive if technical concerns are resolved.** The manuscript addresses an important question and presents a potentially valuable dataset. However, the central claim that TSN is essential for SnRK1 activation is not fully supported by the current evidence. The authors need to provide stronger evidence for a direct mechanistic link between TSN's scaffold function, SG assembly, and SnRK1 activation. The lack of statistical detail for the quantitative imaging data is also a concern that needs to be addressed. If these issues are resolved, the manuscript could make a significant contribution to the field.

## Risk / unsupported claims
- The claim that TSN is "essential" for SnRK1 activation is not fully supported; the data show a requirement, but the specificity of this requirement is unclear.
- The claim that SG formation is required for SnRK1 activation is based solely on the CHX experiment, which is not a specific perturbation of SG assembly.
- The claim that TSN acts as a "docking platform" implies a direct physical scaffold function, but the evidence for direct interactions is incomplete.
- The quantitative split of interactors into 30% stress-recruited and 70% pre-existing is not supported by a described statistical analysis.
- The claim that TSN is required for "full mobility" of SnRK1α1 is based on FRAP data that are not fully reported.