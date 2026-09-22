## Review setup
- **Input scope** Full manuscript text (Introduction, Results, Discussion, Materials and Methods, Data Availability, Acknowledgments) without figures, tables, or supplementary material
- **Assessment boundary** Scientific claims, experimental logic, and internal consistency based solely on the provided text; figure contents and numerical data cannot be independently verified
- **Shared manuscript claim summary** The leader (L) proteins of Theiler's murine encephalomyelitis virus (TMEV) and Boone cardiovirus (BCV) contain a second short linear motif (SLiM), termed "M-acidic," which acts in combination with the previously described DDVF SLiM to target RSK kinases to the nuclear pore complex (NPC), specifically to the RAE1-NUP98 complex, thereby disrupting nucleocytoplasmic trafficking.
- **Visible evidence base** Text descriptions of split-GFP localization assays (Fig. 1, 2), alanine-scanning mutagenesis (Fig. 3), viral infection experiments with mutant viruses (Fig. 4, S1), AlphaFold structural predictions (Fig. 5), co-immunoprecipitation and competition experiments (Fig. 6), and comparative nucleocytoplasmic trafficking assays (Fig. 7)
- **Missing materials affecting confidence** All figures, figure legends, supplementary figures, tables (including Table S1), and statistical details are not provided; numerical data, exact sample sizes, and quantification methods cannot be assessed

## Reviewer
- **Overall assessment** This manuscript presents a conceptually interesting extension of prior work on viral SLiM mimicry, proposing that cardiovirus L proteins use two SLiMs in combination to hijack RSK kinases and target them to the NPC. The identification of an M-acidic SLiM shared with other viral proteins (VSV M, SARS-CoV-2 ORF6, KSHV ORF10) is plausible and consistent with a growing literature on convergent evolution of viral SLiMs. However, the evidence as presented in the text has significant gaps. The co-immunoprecipitation data for TMEV L are negative, and the authors rely on indirect competition experiments and AlphaFold predictions to support the model. The functional distinction between TMEV and BCV L proteins in terms of RAE1 binding affinity is inferred but not directly demonstrated. The claim that the M-acidic SLiM is a bona fide SLiM requires more rigorous biophysical or mutational evidence than alanine scanning alone. The manuscript would benefit from direct binding assays, quantitative imaging, and clearer presentation of the competition data.
- **Who would be interested in the results, and why** Virologists studying picornavirus-host interactions, particularly those interested in viral modulation of nucleocytoplasmic trafficking and innate immune evasion. Also, researchers in the field of SLiM biology and viral mimicry of host motifs, as the study provides another example of convergent evolution of SLiMs across unrelated pathogens. The potential competition between viral proteins and host factors like NXF1 for RAE1 binding may interest researchers studying mRNA export mechanisms.
- **Major strengths** The study addresses a mechanistically important question: how viral L proteins achieve NPC targeting. The combination of two SLiMs (DDVF and M-acidic) is a conceptually novel finding. The use of multiple approaches (split-GFP, alanine scanning, viral mutants, AlphaFold, co-IP, competition assays) is commendable. The identification of a conserved M-acidic motif shared with other viral proteins strengthens the evolutionary argument. The authors are appropriately cautious in interpreting negative co-IP results for TMEV L.
- **Major Concerns**
  - **Concern ID** R1-M1
  - **Severity** Major
  - **Blocking** Yes
  - **Axis** Evidence sufficiency for the central mechanistic claim
  - **Claim pointer** The manuscript claims that TMEV L and BCV L use an M-acidic SLiM to target RSK kinases to the NPC via interaction with RAE1-NUP98.
  - **Evidence pointer** Results sections describing Fig. 5 and Fig. 6; location not provided
  - **Concern** The central claim that TMEV L interacts with RAE1-NUP98 via the M-acidic SLiM is not directly supported by biochemical evidence. Co-immunoprecipitation of TMEV L with RAE1 was not detected (Fig. 6A), and the authors attribute this to lower affinity. However, no direct binding assay (e.g., pull-down with purified components, surface plasmon resonance, or quantitative co-IP with titration) is presented to substantiate this interpretation. The competition experiments (Fig. 6D, E) are indirect and rely on fluorescence microscopy, which is semi-quantitative at best. The AlphaFold predictions (Fig. 5) are computational and not experimentally validated for the L-RAE1 interaction. Without direct biochemical evidence, the claim that TMEV L targets the NPC through the same M-acidic mechanism as BCV L remains speculative.
  - **Why it matters** The manuscript's central conclusion is that both TMEV and BCV L proteins use the M-acidic SLiM to engage RAE1-NUP98. If TMEV L does not measurably interact with RAE1 in co-IP, the mechanism for TMEV L-mediated NPC targeting is unclear. The authors' explanation of lower affinity is plausible but untested. This weakens the generalizability of the proposed mechanism across cardioviruses.
  - **Resolution test** Provide direct biochemical evidence for TMEV L-RAE1 interaction, such as co-IP with higher sensitivity (e.g., crosslinking, more sensitive detection), in vitro pull-down with recombinant proteins, or quantitative binding assays. Alternatively, demonstrate that the M-acidic SLiM of TMEV L is necessary and sufficient for NPC targeting in a heterologous system with a defined RAE1 dependence (e.g., RAE1 knockdown or knockout).
  - **Concern ID** R1-M2
  - **Severity** Major
  - **Blocking** No
  - **Axis** Functional significance of the second SLiM relative to the first
  - **Claim pointer** The manuscript claims that the M-acidic SLiM acts "in combination" with the DDVF SLiM to target RSK to the NPC.
  - **Evidence pointer** Results sections describing Fig. 3, Fig. 4, and Fig. 7; location not provided
  - **Concern** The text does not clearly demonstrate that the M-acidic SLiM and the DDVF SLiM function combinatorially rather than additively or independently. The alanine-scanning data (Fig. 3) identify residues critical for NPC localization, and the viral mutant experiments (Fig. 4) show that M60 mutation in TMEV L abrogates nucleocytoplasmic trafficking disruption. However, the manuscript does not present experiments where both SLiMs are mutated simultaneously, nor does it show whether the DDVF SLiM is required for NPC targeting in the absence of the M-acidic SLiM. The claim of "combination" implies a mechanistic synergy that is not directly tested.
  - **Why it matters** The title and discussion emphasize the combinatorial use of two SLiMs as a novel finding. If the two SLiMs function independently or if the M-acidic SLiM is merely a localization signal while DDVF is the RSK-binding motif, the conceptual advance is less significant. The manuscript should clarify whether the combination is truly synergistic or simply two sequential requirements.
  - **Resolution test** Construct L mutants lacking each SLiM individually and both together, and assess RSK recruitment, NPC localization, and nucleocytoplasmic trafficking disruption. If both SLiMs are required for full activity, the combination claim is supported. If one SLiM is sufficient for NPC localization and the other only for RSK binding, the model should be revised accordingly.
  - **Concern ID** R1-M3
  - **Severity** Major
  - **Blocking** No
  - **Axis** Specificity of the M-acidic SLiM for RAE1-NUP98
  - **Claim pointer** The manuscript claims that the M-acidic SLiM in L proteins interacts specifically with the RAE1-NUP98 complex, similar to other viral proteins.
  - **Evidence pointer** Results sections describing Fig. 5 and Fig. 6; location not provided
  - **Concern** The co-immunoprecipitation data show RAE1 co-precipitating with BCV L, but NUP98 co-precipitation is described as "unclear though suggested in some experiments." The AlphaFold predictions are for L-RAE1-NUP98 complexes, but the text does not specify whether the predicted interface involves both RAE1 and NUP98 or primarily RAE1. The competition experiments with ORF6 peptides suggest competition for a shared binding site, but the readout is NPC localization, not direct RAE1 binding. The manuscript does not exclude the possibility that L proteins interact with other NPC components independently of RAE1.
  - **Why it matters** The manuscript positions the M-acidic SLiM as a RAE1-NUP98 interaction motif shared across viral proteins. If NUP98 is not robustly co-immunoprecipitated, the evidence for the trimeric complex is weak. The specificity of the interaction is central to the proposed mechanism and to the evolutionary comparison with other viral proteins.
  - **Resolution test** Perform co-immunoprecipitation with antibodies against both RAE1 and NUP98 with quantitative analysis across multiple experiments. Use RAE1 or NUP98 knockdown to test whether NPC localization of L depends on both proteins. Alternatively, perform in vitro binding assays with recombinant RAE1-NUP98 complex and L peptides to demonstrate direct interaction.
- **Minor Comments**
  - **Concern ID** R1-m1
  - **Severity** Minor
  - **Axis** Clarity of experimental presentation
  - **Affected element** Fig. 6 competition experiments
  - **Evidence pointer** Results section describing Fig. 6D and E; location not provided
  - **Issue** The text states that competition experiments were performed with "less toxic mutants or truncated proteins" but does not specify which constructs were used in each panel or how the results were quantified. The statement that results "were reproducible" lacks statistical detail.
  - **Required correction** Specify the exact constructs used in each competition experiment, the number of independent replicates, and the statistical test used to assess significance. Provide quantification of the percentage of cells showing NPC localization with appropriate error bars.
  - **Concern ID** R1-m2
  - **Severity** Minor
  - **Axis** Interpretation of EMCV data
  - **Affected element** Results section describing Fig. 2A
  - **Evidence pointer** Results section, paragraph on EMCV; location not provided
  - **Concern** The text states that EMCV L was not targeted to the NPC as a short peptide but that full-length EMCV L was. The authors conclude the EMCV signal is "multipartite or conformational." This is a reasonable interpretation but is presented without discussion of alternative explanations, such as the possibility that the EMCV L peptide was not properly folded or exposed in the fusion context.
  - **Required correction** Add a brief discussion of alternative explanations for the EMCV result, such as fusion protein misfolding or steric hindrance, and consider testing additional EMCV L fragments to strengthen the conclusion.
  - **Concern ID** R1-m3
  - **Severity** Minor
  - **Axis** Statistical reporting
  - **Affected element** Fig. 4 and Fig. S1
  - **Evidence pointer** Results section describing Fig. 4 and Fig. S1; location not provided
  - **Concern** The text reports that nucleocytoplasmic trafficking disruption occurred in a percentage of cells but does not provide the number of cells counted, the number of independent experiments, or the statistical methods used.
  - **Required correction** Provide detailed statistical information for all quantitative microscopy data, including sample sizes, number of replicates, and statistical tests used.
  - **Concern ID** R1-m4
  - **Severity** Minor
  - **Axis** AlphaFold methodology
  - **Affected element** Fig. 5
  - **Evidence pointer** Results section describing Fig. 5; location not provided
  - **Concern** The text mentions AlphaFold3 for predictions involving full-length L proteins and AlphaFold2 multimer v3 for the database screen, but does not provide confidence metrics (e.g., pLDDT, PAE) or describe how predictions were filtered or ranked.
  - **Required correction** Include confidence scores for the key predictions shown in Fig. 5 and describe the criteria used to select and interpret the predicted complexes.
  - **Concern ID** R1-m5
  - **Severity** Minor
  - **Axis** Nomenclature consistency
  - **Affected element** Throughout
  - **Evidence pointer** Location not provided
  - **Concern** The term "M-acidic SLiM" is introduced, but the manuscript does not define the consensus sequence or the precise boundaries of the motif beyond the methionine and surrounding acidic residues. The relationship between the M-acidic SLiM and the previously described DDVF SLiM in terms of sequence proximity is not clearly stated.
  - **Required correction** Provide a clear definition of the M-acidic SLiM consensus sequence, its position within the L protein, and its spatial relationship to the DDVF SLiM.

## Risk / unsupported claims
- The claim that TMEV L interacts with RAE1-NUP98 via the M-acidic SLiM is unsupported by direct biochemical evidence; co-IP was negative and the interaction is inferred from competition experiments and AlphaFold predictions.
- The claim that the two SLiMs act "in combination" is not directly tested; no double-mutant experiments are described.
- The claim that EMCV L has a "multipartite or conformational" NPC targeting signal is weakly supported, as only a limited set of fragments was tested.
- The claim that NCTD precedes viral replication is based on timing observations but the text does not provide quantitative data on the kinetics of NCTD relative to viral RNA replication.
- The prediction that RVFV NSs and human NXF1 interact with RAE1-NUP98 through M-acidic SLiMs is purely computational and not experimentally validated.
- The statement that "L proteins use a combination of 2 SLiMs, both being shared by other pathogens" is an overgeneralization, as the sharing of the M-acidic SLiM with other pathogens is based on sequence similarity and AlphaFold predictions, not functional validation.

## Assessment against Nature-style criteria
- **Originality** Moderate. The concept of viral SLiM mimicry is well established, and the identification of a second SLiM in cardiovirus L proteins is incremental. The specific finding that two SLiMs are used in combination is somewhat novel but not conceptually transformative.
- **Scientific importance** Moderate. The study provides mechanistic insight into how cardiovirus L proteins disrupt nucleocytoplasmic trafficking, which is relevant to understanding viral pathogenesis and innate immune evasion. However, the importance is limited by the lack of direct biochemical evidence and the focus on a relatively narrow family of viruses.
- **Interdisciplinary readership** Limited. The manuscript is primarily of interest to virologists and SLiM biologists. The broader cell biology community may find the RAE1-NUP98 interaction interesting, but the study does not reveal new principles of NPC function or nucleocytoplasmic transport.
- **Technical soundness** The experimental approaches are generally appropriate, but the central claim relies heavily on indirect evidence. The alanine-scanning and viral mutant experiments are well designed, but the lack of direct binding data and the semi-quantitative nature of the microscopy-based competition assays weaken the technical rigor.
- **Readability for nonspecialists** The manuscript is clearly written and the logic is easy to follow. The introduction and discussion effectively contextualize the findings. However, the reliance on AlphaFold predictions without adequate explanation of the method's limitations may be challenging for nonspecialist readers.

## Recommendation posture
Currently not established from the provided evidence. The manuscript presents a plausible and interesting model, but the central claim that TMEV L interacts with RAE1-NUP98 via the M-acidic SLiM is not directly supported. The authors should provide direct biochemical evidence for the TMEV L-RAE1 interaction, test the combinatorial requirement of both SLiMs with double mutants, and strengthen the quantitative analysis of the competition experiments. If these concerns are addressed, the manuscript could be suitable for publication in a specialized virology journal, though the scope and importance may not meet the bar for a high-impact general journal.