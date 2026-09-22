## Review setup
- **Input scope** Full manuscript text including abstract, introduction, methods, results, discussion, and data availability statements
- **Assessment boundary** Scientific validity, technical soundness, and significance of the claims as presented in the provided manuscript text
- **Shared manuscript claim summary** The authors report that E. coli RecG binds directly and specifically to the carboxy-terminal tip of SSB (SSB-Ct) with a KD of 3-4 μM, that this interaction is mediated by a conserved pocket in the RecG HD2 domain involving residues Arg474, Arg467, and Arg614, that disruption of this interaction sensitizes cells to DNA damage and induces SOS, and that large deletions of the SSB intrinsically disordered linker (IDL), including all PxxP motifs, are well tolerated in vivo.
- **Visible evidence base** Fluorescence anisotropy binding assays with SSB peptides; isothermal titration calorimetry with full-length SSB and SSB-Ct peptide; yeast two-hybrid assays; ATPase activity assays; chromosomal recG mutant phenotyping (UV sensitivity, SOS induction, microscopy); chromosomal ssb IDL deletion mutant phenotyping (growth curves, Western blots, whole-genome sequencing, competition assays)
- **Missing materials affecting confidence** Supplementary figures and tables referenced but not provided; raw binding isotherms and ITC thermograms not shown in main text; AlphaFold-Multimer model confidence metrics not fully described; statistical details for microscopy quantifications partially described; whole-genome sequencing analysis details not provided

## Reviewer
- **Overall assessment** This manuscript addresses a significant and timely question in bacterial genome maintenance: the molecular basis of the RecG-SSB interaction. The authors use a combination of in vitro biophysical assays, computational modeling, and in vivo phenotyping to challenge a recently proposed model of SSB recognition involving IDL PxxP motifs. The evidence that RecG binds the SSB-Ct through a canonical SIP pocket in the HD2 domain is compelling and well-supported by multiple complementary approaches. The in vivo data demonstrating that disruption of this interaction phenocopies aspects of recG deletion are important. The IDL deletion experiments are a valuable contribution to understanding SSB architecture-function relationships. However, several technical concerns regarding binding assay interpretations, the strength of the in vivo conclusions, and the generalizability of the IDL findings warrant attention before the case is fully established.

- **Who would be interested in the results, and why** Researchers studying bacterial DNA replication, recombination, and repair will find this work directly relevant. The SSB interaction network is a central organizing principle in bacterial genome maintenance, and defining the RecG-SSB interface has implications for understanding how helicases are recruited to ssDNA. The study also speaks to the broader question of how intrinsically disordered regions in hub proteins contribute to interaction specificity. The IDL deletion data will interest those studying SSB structure-function relationships across bacterial species. The methodological approach combining AlphaFold predictions with biochemical validation may also appeal to the structural biology community.

- **Major strengths** The study uses multiple orthogonal approaches to establish the RecG-SSB interaction interface, including equilibrium binding assays, calorimetry, two-hybrid analysis, and in vitro ATPase measurements. The combination of computational prediction with experimental validation is rigorous. The chromosomal-level genetic manipulations avoid artifacts associated with plasmid-based overexpression. The IDL deletion panel is systematic and includes appropriate controls. The in vivo phenotyping is comprehensive, including UV sensitivity, SOS induction, microscopy, and competition assays.

- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness of binding measurements
- **Claim pointer** The authors claim that RecG binds directly and specifically to the SSB-Ct with a KD of 3.1 ± 0.4 μM, and that the SSB-Ct comprises the complete binding site for RecG based on similar thermodynamic parameters for full-length SSB and SSB-Ct peptide binding.
- **Evidence pointer** Results section "RecG binds directly and specifically to the SSB-Ct"; Figure 2; Table 1
- **Concern** The fluorescence anisotropy assay uses a labeled SSB-Ct peptide, but the authors do not report the concentration range of RecG used in the titrations. If the RecG concentration is not in excess over the peptide concentration, the KD determination may be unreliable. Additionally, the ITC experiments with full-length SSB report a stoichiometry of 1.05 ± 0.07 per protomer, but SSB is a homotetramer. The authors should clarify whether the stoichiometry is per tetramer or per monomer, and whether the four protomers of SSB each bind one RecG molecule. The claim that the SSB-Ct comprises the "complete" binding site is strong given that the ITC data show similar ΔG° values, but the error margins and the fact that only one RecG variant (R474E) was tested in ITC limit the strength of this conclusion.
- **Why it matters** The central claim of the manuscript is that RecG binds specifically to the SSB-Ct. If the binding measurements are not quantitatively reliable, the KD values and the conclusion that the SSB-Ct is necessary and sufficient for binding would be weakened. The stoichiometry question is important for understanding the architecture of the RecG-SSB complex in vivo.
- **Resolution test** The authors should provide full titration curves with protein concentration ranges, report the stoichiometry of binding in terms of SSB tetramer versus RecG monomer, and ideally test at least one additional HD2 pocket variant (e.g., R467E or R614E) in ITC to confirm the binding model quantitatively.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** No
- **Axis** Strength of in vivo conclusions
- **Claim pointer** The authors claim that "interaction with SSB is critical for RecG function in vivo" based on UV sensitivity and SOS induction phenotypes of recG HD2 pocket mutants.
- **Evidence pointer** Results section "Interaction with SSB is critical for RecG function in vivo"; Figure 5
- **Concern** The UV sensitivity phenotypes of the recG pocket mutants appear less severe than the ΔrecG strain, and the authors acknowledge this. However, the conclusion that the interaction is "critical" is somewhat stronger than the data support. The SOS induction data show constitutive activation for some mutants, but the magnitude and statistical significance relative to wild-type are not fully described. Additionally, the authors do not test whether the RecG pocket mutants retain DNA binding or helicase activity in vivo, which would help distinguish between a specific defect in SSB interaction versus a general defect in RecG function. The microscopy data show filamentation in a subpopulation of cells, but the quantification and statistical analysis are not fully described.
- **Why it matters** The in vivo significance of the RecG-SSB interaction is a key conclusion of the manuscript. If the phenotypes are modest or if the mutations affect RecG function independently of SSB binding, the conclusion that SSB interaction is critical for RecG function would be weakened.
- **Resolution test** The authors should provide quantitative data on the fraction of filamented cells with statistical analysis, test whether the RecG pocket mutants retain DNA binding and helicase activity in vitro, and consider whether the residual function in pocket mutants reflects SSB-independent RecG activities.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Generalizability of IDL deletion findings
- **Claim pointer** The authors claim that "the SSB PxxP motifs are not major contributors to SSB cellular functions" based on the normal growth and DNA repair phenotypes of IDL deletion mutants.
- **Evidence pointer** Results section "Cell expressing large chromosomally-encoded SSB IDL deletion variants are indistinguishable from wildtype E.coli"; Figures 6-8
- **Concern** The IDL deletion experiments are performed under standard laboratory growth conditions. The authors acknowledge that there may be specialized situations where IDL functions are important, but the claim that PxxP motifs are "not major contributors" is broad. The competition assays show a fitness defect for the largest deletion (ssbΔ120-166), which is rescued by adding back 10 residues in randomized order. This supports a spacer model, but the authors do not test whether the specific PxxP motifs are required for any condition, such as replication stress or specific DNA damage repair pathways. The Western blot data suggest lower SSB levels for the deletion mutants, which could confound phenotypic interpretations.
- **Why it matters** The conclusion that PxxP motifs are dispensable challenges a growing literature proposing IDL-mediated interactions. If the conclusion is too broad, it could mislead the field. The reduced SSB levels in deletion mutants raise the question of whether the phenotypes reflect loss of IDL function or reduced SSB abundance.
- **Resolution test** The authors should test the IDL deletion mutants under conditions of replication stress or specific DNA repair challenges, and should address whether the reduced SSB levels in deletion mutants affect the interpretation of the phenotypic data.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Computational model validation
- **Claim pointer** The authors use AlphaFold-Multimer to predict the RecG-SSB complex and identify Arg474, Arg467, and Arg614 as key binding residues.
- **Evidence pointer** Results section "Identification of the SSB-binding pocket on the HD2 domain of RecG"; Figure 3
- **Concern** The AlphaFold-Multimer predictions are described as producing five high-confidence models, but the authors do not provide the model confidence metrics (pLDDT, PAE) or the predicted aligned error for the interface. The statement that the SSB-Ct docked against the same surface in all five models is reassuring, but the authors do not show the superposition of the models or quantify the interface conservation. The conservation analysis is described but the results are not shown in the main text. The authors also do not discuss potential limitations of AlphaFold for predicting protein-peptide interactions involving disordered regions.
- **Why it matters** The computational model is used to guide the mutagenesis strategy. If the model is not rigorously validated or if the confidence metrics are not reported, the interpretation of the mutagenesis results could be questioned.
- **Resolution test** The authors should provide the AlphaFold confidence metrics, show the predicted interface in detail, and discuss the limitations of the approach for this specific protein-peptide interaction.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity of methods
- **Affected element** Fluorescence anisotropy assay description
- **Evidence pointer** Materials and Methods section "Fluorescence anisotropy"
- **Issue** The buffer composition for the fluorescence anisotropy assay is not fully described. The authors mention "1 × RecA buffer" but do not specify the components. The peptide concentrations and the range of RecG concentrations used are not stated.
- **Required correction** Provide the full buffer composition and the concentration ranges used in the binding assays.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Statistical reporting
- **Affected element** Microscopy quantification
- **Evidence pointer** Results section "Interaction with SSB is critical for RecG function in vivo"; Figure 5
- **Issue** The microscopy data on cell length and SOS induction are described qualitatively. The number of cells analyzed, the number of biological replicates, and the statistical tests used are not fully described.
- **Required correction** Provide the number of cells analyzed per strain, the statistical tests used, and the p-values for the comparisons.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Data presentation
- **Affected element** ITC data
- **Evidence pointer** Figure 2B-E; Table 1
- **Issue** The ITC thermograms and binding isotherms are not shown in the main text. The authors state that the data fit well to a one-site model, but the quality of the fits is not visually assessable.
- **Required correction** Include representative ITC thermograms and binding isotherms in the main text or supplementary material.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Literature context
- **Affected element** Discussion of prior RecG-SSB interaction studies
- **Evidence pointer** Discussion section
- **Issue** The authors mention that prior studies proposed IDL-mediated interactions but do not provide a detailed comparison of their results with those studies. The discussion of why the co-purification assay used previously may have given different results is brief.
- **Required correction** Expand the discussion of discrepancies with prior studies and provide a more detailed analysis of potential reasons for the different conclusions.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Terminology
- **Affected element** Use of "critical" in the title and text
- **Evidence pointer** Title; Abstract; Discussion
- **Issue** The title states that interaction with the SSB-Ct is "critical" for RecG function. The data show that disruption of this interaction causes moderate phenotypes, but the term "critical" may overstate the findings.
- **Required correction** Consider using a more measured term such as "important" or "required for full function" in the title and throughout the text.

- **Technical failings that need to be addressed before the case is established** R1-M1 (binding assay quantification and stoichiometry) must be addressed to establish the central claim of direct and specific SSB-Ct binding. The lack of full titration data and unclear stoichiometry undermines confidence in the KD values. R1-M3 (IDL deletion interpretation) requires attention because the reduced SSB levels in deletion mutants could confound the phenotypic conclusions.

- **Assessment against Nature-style criteria** 
  - Originality: The manuscript challenges a recently proposed model of SSB recognition and provides evidence for a canonical SSB-Ct binding mode for RecG. While the concept of SSB-Ct binding is not new, the specific application to RecG and the systematic dismantling of the IDL interaction model is original.
  - Scientific importance: The RecG-SSB interaction is relevant to understanding DNA repair pathway coordination in bacteria. The findings have implications for how helicases are recruited to ssDNA and for the broader SSB interaction network. The IDL deletion data contribute to understanding SSB architecture.
  - Interdisciplinary readership: The work will primarily interest molecular biologists, biochemists, and microbiologists. The biophysical methods and computational modeling may also appeal to structural biologists. The broader significance to genome stability is relevant to those studying DNA repair across organisms.
  - Technical soundness: The study is generally well-executed with appropriate controls and complementary methods. However, the binding assay quantification and stoichiometry issues (R1-M1) and the potential confounding effects of reduced SSB levels in IDL mutants (R1-M3) need to be addressed.
  - Readability for nonspecialists: The manuscript is clearly written and the logic is easy to follow. The figures are well-designed. Some sections, particularly the binding assay descriptions, could benefit from additional context for nonspecialists.

- **Recommendation posture** Supportive if technical concerns are resolved. The central claims are likely correct, but the binding assay quantification and the interpretation of the IDL deletion phenotypes require additional experimental detail and analysis. The manuscript would be suitable for publication in a high-impact journal if these concerns are adequately addressed.