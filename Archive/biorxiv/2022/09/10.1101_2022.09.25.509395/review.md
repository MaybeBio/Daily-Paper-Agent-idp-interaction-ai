## Review setup
- **Input scope** Full manuscript text, including abstract, introduction, results, discussion, methods, and figure legends (where present)
- **Assessment boundary** Scientific validity, methodological soundness, and support of claims by the presented evidence; no assessment of editorial fit or publication policy
- **Shared manuscript claim summary** The authors propose that AF2-multimer can accurately predict canonical and non-canonical ATG8/LC3-interacting motif (AIM/LIR) sequences in autophagy-related proteins, including previously uncharacterized motifs, and can identify cross-kingdom host-pathogen AIM/LIR-ATG8 interactions, thereby providing a framework for discovery of new autophagy receptors and adaptors
- **Visible evidence base** Abstract, Introduction, Results sections (three subsections), Discussion, Materials and Methods, one supplementary table referenced, multiple figures referenced (Figure 1A-H, Figure 2A-H, Figure 3A-G, Figure 4A-E, Supplemental Figures S1-S3)
- **Missing materials affecting confidence** Figure files and supplemental figures/tables were not provided; specific numerical data for accuracy claims (e.g., 90% accuracy, 33/36) are only stated in text without underlying dataset; statistical details for co-immunoprecipitation and puncta quantification are partially described but no raw data or full statistical outputs are shown

## Reviewer
- **Overall assessment** This manuscript presents a potentially valuable application of AlphaFold-Multimer to a well-recognized problem in autophagy research, namely the identification of functional AIM/LIR motifs. The authors demonstrate that AF2-multimer can recapitulate known canonical and non-canonical motifs with high accuracy, and they provide experimental validation for a newly predicted non-canonical motif in plant ATG3. The work is timely and of interest to the autophagy and structural biology communities. However, the manuscript as presented has several limitations that temper enthusiasm. The central accuracy claim (90%, 33/36) is presented without a clear description of the prediction criteria or a full dataset. The failure cases (Joka2, Calreticulin, DVL2) are discussed but not systematically analyzed. The claim that AF2-multimer "prioritises the first functional AIM/LIR" is based on limited evidence (NEDD4, ATI-2) and may not generalize. The cross-kingdom section is promising but includes a negative result (PbUIS3) that is not experimentally resolved. The methods for experimental validation are described but the results are not shown in the provided text. Overall, the core idea is sound and the potential impact is real, but the evidence as presented is incomplete for a strong claim of high-accuracy prediction.

- **Who would be interested in the results, and why** Autophagy researchers studying selective autophagy, cargo receptor biology, and ATG8-family interactions would be the primary audience. The work is also relevant to scientists studying host-pathogen interactions, particularly those investigating how pathogen effectors manipulate autophagy. Additionally, the broader structural biology community interested in applications of AlphaFold-Multimer to protein-protein interaction prediction would find this study of interest. The potential to accelerate discovery of new autophagy receptors and adaptors makes this relevant to a wide range of cell biology and plant biology researchers.

- **Major strengths** 
  1. The study addresses a genuine and well-recognized problem in the field: the difficulty of identifying functional AIM/LIR motifs from sequence alone, given the prevalence of false positives.
  2. The application of AF2-multimer to this problem is novel and timely, leveraging a state-of-the-art tool in a creative way.
  3. The inclusion of non-canonical motifs is a significant strength, as these are often missed by sequence-based predictors.
  4. The experimental validation of the predicted ATG3 motif in potato provides direct evidence for the utility of the approach.
  5. The phylogenetic analysis adds an evolutionary dimension that strengthens the interpretation of predicted motifs.
  6. The authors are transparent about limitations, including failure cases and the need for experimental validation.

- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence sufficiency
- **Claim pointer** "AF2-multimer showed 90% accuracy in determining AIM/LIR motifs in 33 experimentally validated proteins that carry functional AIM/LIR motifs"
- **Evidence pointer** Results section "AF2-multimer predicts experimentally validated canonical AIM/LIR motifs with high accuracy"; Supplemental Table 1; location not provided for specific data
- **Concern** The central accuracy claim of 90% (33/36) is presented without a clear description of the prediction criteria. It is unclear what constitutes a "correct" prediction. Was it based on the top-ranked model? On the presence of the motif in any predicted interface? What was the threshold for considering a prediction successful? The authors also do not provide a breakdown of the 36 proteins by species, ATG8 isoform, or motif type. Without this information, the accuracy claim is difficult to evaluate or reproduce. Additionally, the three failure cases (Joka2, Calreticulin, DVL2) are mentioned but not analyzed in detail. Understanding why these failed would be informative for users of the method.
- **Why it matters** The accuracy claim is the central quantitative result of the manuscript. If the criteria for success are not clearly defined, the claim cannot be independently assessed or compared to other methods. This undermines the utility of the proposed framework.
- **Resolution test** Provide a clear definition of prediction success (e.g., correct identification of the experimentally validated motif in the top-ranked model, or in any model above a certain pLDDT threshold). Provide a supplementary table with per-protein results, including the predicted motif, the experimentally validated motif, the model confidence, and the success/failure classification. Discuss the three failure cases in more detail, including possible reasons for failure.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** No
- **Axis** Generalizability
- **Claim pointer** "AF2-multimer can predict multiple AIM/LIR motifs" and "AF2 prioritises the first functional AIM/LIR"
- **Evidence pointer** Results section "AF2-multimer can predict multiple AIM/LIR motifs"; Figure 2A-F; location not provided
- **Concern** The claim that AF2-multimer prioritizes the first functional AIM/LIR is based on two examples: NEDD4 and ATI-2. In NEDD4, the authors show that LIR1 is predicted over LIR2, and that truncating LIR1 allows prediction of LIR2. In ATI-2, the predicted AIM1 is shown to be the functional one, and truncating AIM1 abolishes prediction of AIM2. While these results are consistent with the claim, the sample size is very small. It is not clear whether this prioritization is a general property of AF2-multimer or specific to these proteins. The authors do not test whether the order of motifs in the sequence, the spacing between motifs, or the local sequence context affects prioritization.
- **Why it matters** If the prioritization of the first motif is a general property, it has practical implications for users who need to identify all functional motifs in a protein. If it is not general, the method may miss functional motifs in proteins with multiple AIM/LIRs, limiting its utility.
- **Resolution test** Test the prioritization claim on a larger set of proteins with multiple experimentally validated AIM/LIRs. If possible, include proteins where the second motif is known to be the primary functional one. Alternatively, temper the claim to reflect the limited evidence.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Experimental validation
- **Claim pointer** "we demonstrate that AF2-multimer predicts the physiologically relevant AIM motif in the ATG8-interacting protein 2 (ATI-2) as well as the previously uncharacterized non-canonical AIM motif in ATG3 from potato"
- **Evidence pointer** Results section "AF2-multimer can predict non-canonical AIM/LIRs"; Figure 3F-G; Methods section "Co-immunoprecipitation experiments and immunoblot analysis"; location not provided
- **Concern** The experimental validation of the ATI-2 and ATG3 predictions is described in the text, but the actual results (blots, microscopy images, quantification) are not shown in the provided manuscript text. The co-immunoprecipitation experiments are described in the methods, and the puncta quantification is described, but the data are not presented. Without seeing the experimental results, it is not possible to assess the quality of the validation or the strength of the conclusions drawn from it.
- **Why it matters** The experimental validation is a key part of the manuscript's claim that AF2-multimer predictions are physiologically relevant. If the experimental data are not shown, the claim cannot be evaluated.
- **Resolution test** Include the experimental data (blots, microscopy images, quantification) in the manuscript, either in the main figures or as supplementary material. Ensure that the data support the stated conclusions.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Negative result interpretation
- **Claim pointer** "AF2-multimer predicted a previously unidentified LC3 binding interface in the malaria virulence factor PbUIS3, which lacks a typical LIR motif"
- **Evidence pointer** Results section "AF2-multimer predicts cross-kingdom AIM/LIR-ATG8 interactions in host–pathogen interactions"; Figure 4D; Supplemental Figure S3E; location not provided
- **Concern** The PbUIS3 result is presented as a potential new finding, but the authors note that the previously characterized residues important for LC3 binding are not in the predicted interface. They suggest that these residues might indirectly affect LC3 binding. This is a speculative interpretation. The authors do not provide any experimental validation for the predicted PbUIS3-LC3 interface, nor do they discuss alternative explanations, such as the possibility that the AF2-multimer prediction is incorrect. The claim that this is a "previously unidentified LC3 binding interface" is not supported by experimental evidence.
- **Why it matters** The PbUIS3 result is presented as an example of AF2-multimer's ability to identify novel interfaces. If the prediction is not validated, it weakens the claim that AF2-multimer can be used to discover new binding interfaces. It also raises questions about the reliability of the method for proteins that do not have a typical AIM/LIR.
- **Resolution test** Either provide experimental validation for the predicted PbUIS3-LC3 interface, or temper the claim and present it as a hypothesis that requires testing. Discuss alternative explanations for the discrepancy between the predicted interface and the previously characterized residues.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Abstract
- **Evidence pointer** Abstract, location not provided
- **Issue** The abstract states "AF2-multimer can be modified to detect additional functional AIM/LIR motifs by using protein sequences with mutations in primary AIM/LIR residues." This is an important methodological point, but it is not clear what "modified" means in this context. Does it refer to a specific protocol change, or simply to the use of mutated sequences as input?
- **Required correction** Clarify the wording to describe the specific approach, e.g., "by running AF2-multimer on protein sequences in which the primary AIM/LIR residues have been mutated."

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Results section "AF2-multimer predicts experimentally validated canonical AIM/LIR motifs with high accuracy"
- **Evidence pointer** Results section, location not provided
- **Issue** The authors state that "nearly all AF2-multimer predicted AIM/LIRs appeared in IDPRs, while a few were predicted to be partially disordered." This is an interesting observation, but the authors do not provide a quantitative analysis or a comparison to the location of the experimentally validated motifs. It would be useful to know how many of the 33 correctly predicted motifs were in IDPRs, and whether the three failures were also in IDPRs.
- **Required correction** Provide a quantitative analysis of the location of predicted and validated motifs relative to predicted disorder, possibly as a supplementary figure or table.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Methodological detail
- **Affected element** Methods section "Structural analysis using AF2"
- **Evidence pointer** Methods, location not provided
- **Issue** The methods state that "AF2-multimer was used through a subscription to the Google Colab." It is not clear what parameters were used for the predictions, such as the number of models generated, the number of recycles, or the choice of template. These details are important for reproducibility.
- **Required correction** Provide the specific parameters used for AF2-multimer predictions, or cite a protocol that describes the default settings.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Statistical reporting
- **Affected element** Methods section "Confocal microscopy and quantitative analysis of GFP-ATG8CL autophagosome puncta"
- **Evidence pointer** Methods, location not provided
- **Issue** The methods describe the use of the Wilcoxon test for statistical significance, but the number of biological replicates and the number of cells imaged per replicate are not stated. This information is necessary to assess the robustness of the puncta quantification.
- **Required correction** State the number of biological replicates and the number of cells analyzed per condition.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Terminology
- **Affected element** Throughout
- **Evidence pointer** Location not provided
- **Issue** The authors use the terms "AIM/LIR" and "LIR/AIM" interchangeably. While this is common in the field, it would be clearer to use one term consistently, or to define the terms at first use.
- **Required correction** Use "AIM/LIR" consistently throughout, or define both terms and use them consistently.

## Risk / unsupported claims
- The claim of "90% accuracy" is not fully supported without a clear definition of prediction success criteria and a per-protein breakdown of results.
- The claim that "AF2-multimer prioritises the first functional AIM/LIR" is based on only two examples and may not be generalizable.
- The claim that AF2-multimer predicted a "previously unidentified LC3 binding interface" in PbUIS3 is not experimentally validated and should be presented as a hypothesis.
- The experimental validation of the ATI-2 and ATG3 predictions is described but the data are not shown in the provided text, making the claims unverifiable from the supplied material.
- The statement that "AF2-multimer can be modified to detect additional functional AIM/LIR motifs" is vague and not clearly defined.