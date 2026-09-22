## Review setup
- **Input scope** Full manuscript text (abstract, introduction, results, discussion, methods) as provided
- **Assessment boundary** Scientific content, experimental logic, data interpretation, and claims as presented in the supplied text; no supplementary figures or tables were available for direct inspection
- **Shared manuscript claim summary** The authors identify a conserved short linear motif (FRM) in the disordered regions of Msb3, Msb4, Ste7, and Mkk1 that binds the SHD1 domain of the yeast scaffold protein Spa2. They use AlphaFold predictions, mutagenesis, split-ubiquitin assays, competition assays, and localization studies to support this interaction and its functional relevance. They further predict homologous SHD1-FRM complexes across Opisthokonta and perform a proteome-wide search to identify Dse3 as a novel Spa2-binding partner.
- **Visible evidence base** Text descriptions of results, including reference to Figures 1-7 and supplementary figures/tables; no raw data, images, or numerical values were directly visible
- **Missing materials affecting confidence** Supplementary figures (S1-S4), supplementary tables (S1-S4), raw microscopy images, western blot images, statistical details, AlphaFold confidence metrics beyond ipTM, and experimental replicates were not accessible; this limits full verification of quantitative claims

## Reviewer
- **Overall assessment** This manuscript presents a well-structured and conceptually interesting study identifying a conserved linear motif that mediates binding to Spa2 family scaffold proteins. The combination of computational prediction with experimental validation is commendable, and the evolutionary perspective adds breadth. However, several technical concerns regarding the strength of experimental evidence, the interpretation of AlphaFold predictions, and the functional significance of the identified interactions require clarification before the conclusions can be fully accepted.
- **Who would be interested in the results, and why** Researchers studying cell polarity, tip growth, and polarisome function in fungi; those interested in short linear motif-mediated protein interactions; and scientists working on scaffold protein networks in eukaryotic cell signaling. The evolutionary conservation aspect may also appeal to comparative cell biologists.
- **Major strengths** The study addresses a clear gap in understanding how Spa2 recruits its binding partners. The identification of a specific motif and its validation through multiple complementary approaches (mutagenesis, competition assays, localization) is methodologically sound. The use of AlphaFold to predict cross-species interactions is timely and adds predictive value. The proteome-wide search strategy is innovative and provides a template for future motif discovery.
- **Major Concerns**
  - **Concern ID** R1-M1
  - **Severity** Major
  - **Blocking** Yes
  - **Axis** Evidence strength for core interaction claim
  - **Claim pointer** The authors claim that the FRM mediates binding of Msb3, Msb4, and Ste7 to Spa2, and that mutations in key residues disrupt this interaction.
  - **Evidence pointer** Figure 1C-E, Figure 2C-D, text in Results section "A conserved five-residue motif mediates binding..."
  - **Concern** The split-ubiquitin assay is used as the primary evidence for interaction and for assessing the effects of mutations. However, the text does not provide quantitative data or statistical analysis for these assays. The claim that mutations "abolished" or "reduced" binding is based on qualitative growth assays, which may not be sufficiently sensitive to distinguish between complete loss and significant reduction of interaction. Additionally, the split-ubiquitin assay can produce false positives due to overexpression or non-specific interactions.
  - **Why it matters** The central conclusion of the manuscript rests on the specificity and strength of the FRM-SHD1 interaction. Without quantitative binding data or an orthogonal biochemical assay (e.g., co-immunoprecipitation, isothermal titration calorimetry), the possibility remains that the observed effects are due to indirect or non-specific effects of the mutations.
  - **Resolution test** Provide quantitative data from the split-ubiquitin assays (e.g., growth rates, β-galactosidase activity) with statistical analysis. Alternatively, perform an independent biochemical assay such as pull-down with purified proteins or microscale thermophoresis to confirm direct binding and quantify affinity changes upon mutation.
  - **Concern ID** R1-M2
  - **Severity** Major
  - **Blocking** Yes
  - **Axis** Functional relevance of the interaction
  - **Claim pointer** The authors conclude that the SHD1-FRM interaction directs vesicle fusion to the bud tip by recruiting Sec4-GAP activity, and that this is functionally important for tip growth.
  - **Evidence pointer** Figure 5A-C, text in Results section "The SHD1Spa2-FRM interaction targets the complex to sites of polar growth"
  - **Concern** The functional experiments rely on morphological measurements (L/W ratio) and electron microscopy to assess vesicle accumulation. However, the text does not provide quantitative data or statistical analysis for these measurements. The claim that "no vesicle accumulation occurs" in mutant strains is based on visual inspection of EM images, which is subjective. Furthermore, the L/W ratio differences, while statistically significant, are modest and may not fully capture the functional impact of the interaction.
  - **Why it matters** The authors argue that the interaction is physiologically relevant for tip growth. Without robust quantitative data, the functional significance of the interaction remains correlative rather than causal. The lack of a clear phenotype in cells lacking the interaction (e.g., no vesicle accumulation) is puzzling and needs explanation.
  - **Resolution test** Provide quantitative analysis of vesicle density from EM images with statistical comparison. Include a more detailed analysis of bud morphology, such as cell wall thickness or chitin distribution, to strengthen the functional link. Consider rescue experiments where the interaction is restored to demonstrate causality.
  - **Concern ID** R1-M3
  - **Severity** Major
  - **Blocking** No
  - **Axis** Interpretation of AlphaFold predictions
  - **Claim pointer** The authors use AlphaFold predictions to propose that the FRM adopts an alpha-helical conformation upon binding and to predict cross-species interactions.
  - **Evidence pointer** Figure 2A, Figure 6C-F, Figure S2, text in Results sections "AlphaFold predicts the FRM-SHD1 complex..." and "Predicting SHD1-FRM complexes in other members of the Opisthokonta"
  - **Concern** The manuscript relies heavily on AlphaFold predictions without providing sufficient validation for the predicted structures. The correlation between ipTM scores and experimental binding strength is described as "loose," which raises questions about the reliability of using ipTM as a filter for identifying functional interactions. The predicted "flipped orientation" of the Dse3 helix is presented without experimental validation.
  - **Why it matters** AlphaFold predictions are valuable for generating hypotheses, but they are not experimental evidence. The authors use these predictions to make broad claims about evolutionary conservation and to identify new interaction partners. If the predictions are inaccurate, these claims could be misleading.
  - **Resolution test** Provide experimental validation for at least one cross-species prediction (e.g., the Fusarium graminearum interaction). For the Dse3 interaction, perform mutagenesis of the predicted contact residues to confirm the binding mode. Discuss the limitations of ipTM as a predictor of binding affinity more explicitly.
  - **Concern ID** R1-M4
  - **Severity** Major
  - **Blocking** No
  - **Axis** Specificity of the motif
  - **Claim pointer** The authors claim that the FRM is a specific motif that binds to Spa2 family members, and that it is conserved from yeast to human.
  - **Evidence pointer** Figure 1B, Figure 6A-B, text in Results section "A conserved five-residue motif mediates binding..."
  - **Concern** The consensus sequence (V/I)-(I/L)-(D/S)-(L/A)-Y is relatively short and degenerate. The authors do not demonstrate that this motif is not present in other proteins that do not bind Spa2. The specificity of the interaction is not fully established, and the possibility of non-specific binding to hydrophobic grooves cannot be excluded.
  - **Why it matters** The claim of a conserved, specific motif is central to the paper's significance. If the motif is too degenerate, it may not be a reliable predictor of Spa2 binding, limiting its utility for identifying new interactions.
  - **Resolution test** Perform a systematic analysis of the motif frequency in the yeast proteome and test a negative control protein containing the motif that does not bind Spa2. Use alanine scanning to define the minimal motif required for binding and compare with the natural variation seen across species.
- **Minor Comments**
  - **Concern ID** R1-m1
  - **Severity** Minor
  - **Axis** Clarity of presentation
  - **Affected element** Figure 1A description
  - **Evidence pointer** Figure 1A, text in Results section
  - **Issue** The description of the split-ubiquitin screen is brief, and it is unclear how the 530 proteins were selected and whether the screen was saturated.
  - **Required correction** Provide more detail on the library construction and the criteria for identifying positive hits.
  - **Concern ID** R1-m2
  - **Severity** Minor
  - **Axis** Statistical reporting
  - **Affected element** L/W ratio measurements
  - **Evidence pointer** Figure 5C
  - **Issue** The text states that "red bars represent the mean±s.d." but does not specify the number of biological replicates or the statistical test used for each comparison.
  - **Required correction** Add a detailed statistical methods section and specify the n and p-values for each comparison in the figure legends.
  - **Concern ID** R1-m3
  - **Severity** Minor
  - **Axis** Nomenclature consistency
  - **Affected element** Use of "SHD1" and "SDH1"
  - **Evidence pointer** Text in Results section "A conserved five-residue motif mediates binding..."
  - **Issue** The abbreviation "SDH1" appears once in the text (likely a typo for SHD1).
  - **Required correction** Correct the typo and ensure consistent use of SHD1 throughout.
  - **Concern ID** R1-m4
  - **Severity** Minor
  - **Axis** Discussion of limitations
  - **Affected element** Discussion section
  - **Evidence pointer** Discussion section
  - **Issue** The discussion does not address the limitations of the split-ubiquitin assay or the potential for false positives/negatives in the interaction studies.
  - **Required correction** Add a paragraph acknowledging the limitations of the methods used and how they might affect the conclusions.
  - **Concern ID** R1-m5
  - **Severity** Minor
  - **Axis** Completeness of methods
  - **Affected element** AlphaFold methods
  - **Evidence pointer** Methods section "Structure prediction"
  - **Issue** The methods for AlphaFold prediction are very brief and do not specify the version of AlphaFold3 used, the input sequences, or the parameters for ranking models.
  - **Required correction** Provide more detailed methods for the AlphaFold predictions, including any filtering criteria and the specific models used.
  - **Concern ID** R1-m6
  - **Severity** Minor
  - **Axis** Data availability
  - **Affected element** Source data
  - **Evidence pointer** Figure S4
  - **Issue** The source data for western blots are mentioned but not described in detail.
  - **Required correction** Clarify how the source data are provided and ensure they are accessible to readers.

## Technical failings that need to be addressed before the case is established
- R1-M1: Lack of quantitative binding data for the core interaction claim
- R1-M2: Insufficient quantitative analysis of functional phenotypes
- R1-M3: Over-reliance on AlphaFold predictions without adequate experimental validation

## Risk / unsupported claims
- The claim that the FRM is "conserved from yeast to human" is based primarily on sequence similarity and AlphaFold predictions, not on direct experimental evidence of binding across all species.
- The statement that "protein assemblies that spatially confine secretion to specific membrane regions are a common feature of eukaryotic cells" is presented as a general principle but is not directly tested in this study.
- The identification of Dse3 as a novel Spa2-binding partner is based on a computational screen and a single competition assay; the functional relevance of this interaction is acknowledged as unclear but the claim of binding is presented with limited experimental support.
- The assertion that "the structures of the different complexes explain why the Tyr residue at position +2 is conserved" is an interpretation based on predicted structures, not experimentally determined ones.

## Assessment against Nature-style criteria
- **Originality** The identification of a specific conserved motif for Spa2 binding is novel and adds to the understanding of polarisome function. The use of AlphaFold for cross-species prediction is timely. However, the concept of short linear motifs mediating protein interactions is well-established, and the novelty lies primarily in the specific system studied.
- **Scientific importance** The study has potential importance for understanding tip growth in fungi, which is relevant to pathogenicity. The evolutionary conservation aspect broadens the impact. However, the functional significance of the interaction is not fully established, limiting the immediate importance.
- **Interdisciplinary readership** The topic is primarily of interest to cell biologists and microbiologists. The use of AlphaFold may attract computational biologists, but the overall scope is relatively narrow.
- **Technical soundness** The experimental approaches are generally appropriate, but the lack of quantitative data and the heavy reliance on AlphaFold predictions without sufficient validation weaken the technical foundation.
- **Readability for nonspecialists** The manuscript is clearly written and the logic is easy to follow. The abstract and introduction provide sufficient context. However, some sections, particularly the proteome-wide search, may be challenging for non-specialists.

## Recommendation posture
Supportive if technical concerns are resolved. The core hypothesis is interesting and the experimental design is thoughtful, but the current evidence does not fully establish the claims. Quantitative binding data, more robust functional analysis, and experimental validation of at least some AlphaFold predictions are needed to strengthen the case.