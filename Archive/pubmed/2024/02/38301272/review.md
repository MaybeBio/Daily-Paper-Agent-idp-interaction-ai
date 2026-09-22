## Review setup
- **Input scope** Full manuscript text, including abstract, introduction, results, discussion, materials and methods, and supplementary figure/table references.
- **Assessment boundary** Scientific content, methodological rigor, phylogenetic and biophysical evidence, and interpretation. Not assessed: editorial quality, formatting, or literature completeness beyond cited works.
- **Shared manuscript claim summary** The authors propose that the p53/MDM2 interaction in ray-finned fishes is maintained by stabilizing selection on binding affinity rather than sequence conservation. They report recurrent, lineage-specific loss-of-affinity mutations in the canonical binding motif of p53TAD, compensated by flanking regions that restore affinity to a functional range similar to that of the human interaction.
- **Visible evidence base** Phylogenetic reconstructions of p53TAD and MDM2 from 51 actinopterygian species; ancestral sequence reconstructions (maximum likelihood and AltAll variants); fluorescence polarization binding assays for 12 extant and 4 ancestral complexes; ITC validation for two D. rerio constructs; ColabFold structural predictions.
- **Missing materials affecting confidence** Supplementary Spreadsheets S1–S6, Text Files S1–S2, and Figures S1–S10 were referenced but not provided. Full sequence alignment and posterior probability tables are unavailable for independent verification. Raw binding isotherms and replicate data are not shown in the main text.

## Reviewer
- **Overall assessment** This is a well-conceived and carefully executed study addressing an important question in molecular evolution: how functional affinity is maintained in a motif-mediated interaction despite extensive sequence divergence. The combination of ancestral reconstruction, phylogenetic analysis, and direct binding measurements is powerful and appropriate. The finding that flanking regions compensate for loss-of-affinity mutations in the canonical motif is novel and likely generalizable. However, the manuscript has several technical and interpretive issues that must be addressed before the central claims are fully established.
- **Who would be interested in the results, and why** Evolutionary biologists studying protein-protein interaction evolution, biochemists interested in intrinsically disordered regions and short linear motifs, and researchers in the p53 field. The work provides a concrete example of affinity conservation despite sequence divergence, with implications for predicting binding from sequence alone.
- **Major strengths** 1) The study combines robust phylogenetic analysis with direct biophysical measurements, a rare and powerful integration. 2) The use of ancestral sequence reconstruction with AltAll variants to test robustness is exemplary. 3) The discovery that flanking regions compensate for motif mutations is significant and mechanistically insightful. 4) The sampling across diverse fish lineages is broad and well chosen.
- **Major Concerns** See detailed items below.
- **Minor Comments** See detailed items below.
- **Technical failings that need to be addressed before the case is established** R1-M1 (model selection for p53TAD reconstruction), R1-M2 (lack of full-length ancestral constructs), R1-M3 (limited ITC validation), R1-M4 (incomplete evidence for the "functional affinity" claim).
- **Assessment against Nature-style criteria**  
  *Originality*: High. The concept of affinity conservation via flanking-region compensation in a motif-mediated interaction is novel and not previously demonstrated for p53/MDM2.  
  *Scientific importance*: High. The findings challenge sequence-based prediction of binding and highlight the need for experimental validation, with broad implications for understanding motif-mediated interactions.  
  *Interdisciplinary readership*: Moderate to high. The work bridges evolutionary biology, biochemistry, and structural biology, and should appeal to readers across these fields.  
  *Technical soundness*: Generally strong, but with specific concerns (see R1-M1 to R1-M4) that need resolution.  
  *Readability for nonspecialists*: Good. The writing is clear, and the figures (as described) should aid comprehension, though the supplementary material is essential for full understanding.
- **Recommendation posture** Supportive if technical concerns are resolved. The core findings are likely correct and important, but the manuscript requires additional analyses and clarifications to fully substantiate the claims.

### Major Concerns

- **Concern ID** R1-M1  
- **Severity** Major  
- **Blocking** Yes  
- **Axis** Technical soundness  
- **Claim pointer** The authors state that ancestral sequence reconstructions were performed using the JTT + G + I model, and that model selection was only undertaken after reviewer feedback. For p53TAD, the JTT + G + I model ranked 8th by AIC and 3rd by BIC, with the JTT + G + I + F model being strongly preferred.  
- **Evidence pointer** Materials and Methods, "Model Selection for the Reconstruction of Ancestral Sequences"; Supplementary Spreadsheet S3.  
- **Concern** The authors acknowledge that model selection impacts ancestral sequence reconstructions, yet they do not present reconstructions based on the best-fit model (JTT + G + I + F) for p53TAD. The claim that "the majority of p53TAD reconstructions based on these 2 models exhibit strong similarities" is vague and not supported by quantitative data in the main text. If the preferred model yields different ancestral sequences at key positions (e.g., positions 26–27), the central conclusions about ancestral affinity could be affected.  
- **Why it matters** Ancestral sequence reconstruction is foundational to the study's evolutionary inferences. If the reconstructions are sensitive to model choice, the conclusions about ancestral affinity and the direction of evolutionary change may not be robust.  
- **Resolution test** Provide ancestral reconstructions for p53TAD using the JTT + G + I + F model, and show that the key residues (positions 18, 24–27) and the resulting affinity predictions are consistent with those from the JTT + G + I model. If differences exist, discuss their implications for the conclusions.

- **Concern ID** R1-M2  
- **Severity** Major  
- **Blocking** Yes  
- **Axis** Technical soundness  
- **Claim pointer** The authors conclude that flanking regions increase affinity 4- to 73-fold for 11 of 12 extant fish interactions, and that this compensation maintains "functional affinity" comparable to the human interaction.  
- **Evidence pointer** Results, "Flanking Regions Increase the Affinity between p53TAD and MDM2"; Table 1; Figures 3 and 5.  
- **Concern** The full-length p53TAD constructs were only tested for extant species, not for the ancestral reconstructions. The authors state that ancestral full-length p53TAD sequences could not be reconstructed due to poor conservation, but this limits the ability to directly test whether ancestral complexes had similar affinity to extant ones. The conclusion that "the ancestral complex likely possessed similar functional affinity" is therefore inferred rather than demonstrated.  
- **Why it matters** The central claim of the paper is that affinity, not sequence, is conserved. Without direct measurement of ancestral full-length complexes, the authors cannot rule out that ancestral affinities were different and that the observed pattern in extant species is a derived state.  
- **Resolution test** If ancestral full-length p53TAD reconstruction is truly impossible, the authors should clearly state this limitation and temper the claim. Alternatively, they could test chimeric constructs combining ancestral motifs with extant flanking regions to estimate ancestral full-length affinity.

- **Concern ID** R1-M3  
- **Severity** Major  
- **Blocking** No  
- **Axis** Technical soundness  
- **Claim pointer** The authors state that ITC experiments with D. rerio MDM2 and p53TAD constructs (short and full-length) were in "excellent agreement" with fluorescence polarization data.  
- **Evidence pointer** Results, "Flanking Regions Increase the Affinity between p53TAD and MDM2"; Supplementary Figure S5.  
- **Concern** ITC was performed for only one species (D. rerio) and two constructs. The agreement with FP is reassuring, but the thermodynamic parameters (ΔH, ΔS) are not reported in the main text, and the authors state that differences are "too small to draw any conclusions." This limits the mechanistic insight into how flanking regions enhance affinity.  
- **Why it matters** The claim that flanking regions increase affinity via extended helix formation (as predicted by ColabFold) would be strengthened by thermodynamic data showing, for example, a more favorable enthalpy change consistent with additional contacts.  
- **Resolution test** Report the full thermodynamic parameters from ITC for both constructs and discuss whether they support the proposed mechanism. If the data are insufficient, acknowledge this and suggest future experiments.

- **Concern ID** R1-M4  
- **Severity** Major  
- **Blocking** No  
- **Axis** Scientific importance  
- **Claim pointer** The authors conclude that "stabilizing selection of functional affinity" underlies the evolution of the p53/MDM2 interaction, and that this is likely a general mechanism for motif-mediated interactions.  
- **Evidence pointer** Abstract; Discussion.  
- **Concern** The evidence for stabilizing selection is indirect. The authors show that extant affinities cluster around 100 nM, but they do not provide a formal test of selection (e.g., dN/dS analysis, comparison to neutral expectations, or fitness measurements). The claim of "stabilizing selection" is an interpretation, not a demonstrated result.  
- **Why it matters** The paper's broader significance rests on the claim that selection acts on affinity rather than sequence. Without a formal test, this remains a plausible hypothesis rather than a demonstrated conclusion.  
- **Resolution test** Either add a formal test of selection (e.g., comparing observed sequence variation to neutral models) or soften the language to "consistent with stabilizing selection" and discuss alternative explanations.

### Minor Comments

- **Concern ID** R1-m1  
- **Severity** Minor  
- **Axis** Clarity  
- **Affected element** Abstract  
- **Evidence pointer** Abstract, last sentence.  
- **Issue** The phrase "nonspecific interactions by nonconserved disordered regions" is somewhat ambiguous. It could be read as implying that the interactions are nonspecific in a biochemical sense, whereas the data suggest they are specific but mediated by nonconserved residues.  
- **Required correction** Rephrase to "interactions involving nonconserved residues in disordered regions" or similar.

- **Concern ID** R1-m2  
- **Severity** Minor  
- **Axis** Reproducibility  
- **Affected element** Materials and Methods, "Fluorescence Polarization Experiments"  
- **Evidence pointer** Materials and Methods, "Fluorescence Polarization Experiments".  
- **Issue** The concentrations of MDM2 used in the FP experiments are listed for some constructs but not all. The buffer conditions are described, but the temperature at which FP experiments were performed is not stated.  
- **Required correction** Specify the temperature for all FP experiments and provide a table of all protein concentrations used.

- **Concern ID** R1-m3  
- **Severity** Minor  
- **Axis** Interpretation  
- **Affected element** Results, "Phylogenetic Analysis of Fish p53TAD"  
- **Evidence pointer** Results, "Phylogenetic Analysis of Fish p53TAD"; Figure 2.  
- **Issue** The authors state that "in several species, we found 2 distinct p53 proteins" and that these are paralogs from the teleost whole-genome duplication. However, the criteria for distinguishing paralogs from alleles or assembly artifacts are not fully described.  
- **Required correction** Briefly describe the criteria used to confirm paralog identity (e.g., phylogenetic placement, synteny, sequence divergence).

- **Concern ID** R1-m4  
- **Severity** Minor  
- **Axis** Presentation  
- **Affected element** Discussion  
- **Evidence pointer** Discussion, paragraph 2.  
- **Issue** The discussion of alternative scenarios for the order of evolutionary events is speculative and could be more clearly framed as hypotheses.  
- **Required correction** Clearly label these as speculative scenarios and suggest how they could be tested in future work.

## Risk / unsupported claims
- The claim that "stabilizing selection of functional affinity" is the underlying mechanism is not formally tested and should be presented as an interpretation.
- The inference that ancestral full-length p53TAD/MDM2 complexes had similar affinity to extant ones is not directly supported by experimental data.
- The statement that "it is likely that the evolution of affinity in motif-mediated interactions often involves an interplay between specific interactions made by conserved motif residues and nonspecific interactions by nonconserved disordered regions" is a generalization beyond the data presented.
- The claim that "the ancestral complex likely possessed similar functional affinity" (Discussion) is based on indirect reasoning and should be tempered.
- The assertion that "the lack of correlation between KD values for the motif and full-length p53TAD (R2 = 0.014) reinforces the notion that the flanking regions make affinities more similar" is suggestive but not a statistical test of convergence.