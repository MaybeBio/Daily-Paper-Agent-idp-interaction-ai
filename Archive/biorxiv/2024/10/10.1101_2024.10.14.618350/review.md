## Review setup
- **Input scope** Full manuscript text including abstract, introduction, results, discussion, methods, and acknowledgments
- **Assessment boundary** Scientific validity of claims, methodological soundness, interpretation of AlphaFold2/AlphaFold-Multimer outputs, and generalizability of conclusions
- **Shared manuscript claim summary** The authors use AlphaFold2 and AlphaFold-Multimer to predict leucine zipper dimer structures for AP-1 transcription factors (FosB, JunD) and additional human L-zip pairs, finding that high-confidence scores (pLDDT, ipTM, PAE) do not discriminate between physiologically probable and improbable dimers, and that electrostatic incompatibility is not reflected in these confidence metrics
- **Visible evidence base** Abstract, full introduction, full results section, full discussion, full methods, figure references (Figures 1-7), supplementary figure references, table references (Tables 1-2)
- **Missing materials affecting confidence** Figures and supplementary figures not provided; Table 1 and Table 2 not provided; no raw AlphaFold output files; no statistical analysis details; no sequence alignments or multiple sequence alignment data; no code or analysis scripts

## Reviewer
- **Overall assessment** This manuscript presents a timely and relevant case study on the limitations of AlphaFold2 and AlphaFold-Multimer for predicting protein-protein interactions, specifically leucine zipper coiled-coil dimers. The authors demonstrate that confidence metrics (pLDDT, ipTM, PAE) are insufficient to distinguish between dimers that form in vivo and those that are electrostatically forbidden. The work is conceptually important for the structural biology community, as it cautions against over-reliance on AI-predicted structures without biophysical validation. However, the manuscript has several methodological weaknesses, including a lack of quantitative comparison across models, absence of negative control validation, and incomplete reporting of the electrostatic analysis. The claim that AlphaFold cannot account for electrostatics is plausible but not fully established from the provided evidence, as the authors do not systematically vary electrostatic features while controlling for other variables. The study would benefit from a more rigorous quantitative framework and a clearer articulation of what "validity" means in this context.

- **Who would be interested in the results, and why** Structural biologists using AlphaFold for complex prediction, computational biologists developing or benchmarking protein structure prediction tools, researchers studying coiled-coil and leucine zipper biology, and scientists using AI-based tools for drug design or protein engineering. The results are also relevant to the broader community interested in the interpretability and limitations of deep learning-based structure prediction methods.

- **Major strengths** 1) The study addresses a critical and timely question about the limitations of AlphaFold confidence metrics for discriminating biologically relevant interactions. 2) The use of a well-characterized biological system (AP-1 transcription factors) provides a clear test case. 3) The authors include multiple complementary analyses (pLDDT, ipTM, PAE, electrostatic surface potentials) to assess prediction quality. 4) The synthetic peptide experiment is a creative approach to test the limits of AlphaFold-Multimer. 5) The discussion appropriately contextualizes the findings within the broader literature on AlphaFold limitations.

- **Major Concerns** 
  - R1-M1: The central claim that AlphaFold-Multimer cannot differentiate probable from improbable dimers is based on a limited set of examples without systematic quantitative comparison.
  - R1-M2: The electrostatic surface potential analysis is qualitative and lacks a quantitative metric to support the claim that the FosB homodimer is electrostatically implausible.
  - R1-M3: The manuscript does not provide a clear definition of what constitutes a "valid" prediction, making it difficult to assess the strength of the conclusions.
  - R1-M4: The generalizability of the findings beyond the specific test cases is not established, and the authors do not discuss potential exceptions or conditions under which AlphaFold-Multimer might perform better.

- **Minor Comments** 
  - R1-m1: The abstract states that AlphaFold2 predicts the FosB monomer as an α-helix covering residues P152-G221, but the results section reports residues 152±1-219±1 for the dimer constructs; the discrepancy should be clarified.
  - R1-m2: The methods state that "all AlphaFold computations were run using the default settings" but do not specify the version of AlphaFold-Multimer or the exact parameters used for multimer prediction.
  - R1-m3: The authors mention that "five PDB protein structure files were produced" but do not report whether the top-ranked model was consistently used or whether there was variability across ranked models.
  - R1-m4: The discussion mentions AlphaFold3 but does not provide a detailed comparison of whether the identified limitations persist in the newer version.
  - R1-m5: The manuscript would benefit from a figure showing the electrostatic surface potentials of the FosB homodimer compared to the heterodimer to visually support the qualitative claims.

- **Technical failings that need to be addressed before the case is established** R1-M1, R1-M2, R1-M3

- **Assessment against Nature-style criteria** 
  - Originality: The manuscript addresses a known but under-explored limitation of AlphaFold-Multimer, specifically in the context of leucine zipper dimers. The synthetic peptide experiment adds a novel element. However, the core finding that confidence scores do not always reflect biological plausibility is not entirely new, and the manuscript does not substantially advance methodological approaches to address this limitation.
  - Scientific importance: The work is important for the structural biology community as a cautionary note, but its impact is limited by the narrow scope of the test cases and the lack of a quantitative framework for assessing prediction validity.
  - Interdisciplinary readership: The manuscript is likely to appeal to structural biologists, computational biologists, and researchers in protein engineering. The writing is accessible, but the lack of quantitative rigor may limit its appeal to more methodologically oriented readers.
  - Technical soundness: The experimental design is reasonable but incomplete. The absence of negative controls, the qualitative nature of the electrostatic analysis, and the lack of statistical comparisons weaken the technical foundation.
  - Readability for nonspecialists: The manuscript is generally well-written and accessible, with clear explanations of the biological context and the significance of the findings. However, some technical terms (e.g., ipTM, pLDDT) are introduced without sufficient explanation for nonspecialists.

- **Recommendation posture** Supportive if technical concerns are resolved. The manuscript addresses an important question and provides a useful case study, but the current evidence does not fully establish the central claim. The authors should strengthen the quantitative analysis, add appropriate controls, and clarify the definition of prediction validity.

## Risk / unsupported claims
- The claim that AlphaFold-Multimer "cannot account for other effects (for example electrostatic) that can modify proximity" is not fully supported by the data, as the authors do not systematically test this across a range of electrostatic conditions.
- The statement that the FosB homodimer is "unlikely to form in vivo" is based on prior literature, but the manuscript does not provide direct experimental evidence to confirm this for the specific constructs used.
- The claim that the synthetic peptide pair is "as energetically unfavourable as possible" is not quantitatively supported, as the authors do not provide calculated or measured energies for the designed peptides.
- The generalizability of the findings to other coiled-coil systems or other types of protein-protein interactions is not established and should be discussed more cautiously.