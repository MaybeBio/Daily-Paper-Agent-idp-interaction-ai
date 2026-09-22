## Review setup
- **Input scope** Full manuscript text (review article, no abstract provided separately)
- **Assessment boundary** Scientific content, methodological rigor, internal consistency, and support for claims based solely on the provided manuscript text
- **Shared manuscript claim summary** The authors present a systematic review of 32 cryo-EM and cryo-ET studies deposited in the EMDB in 2024, reporting that 78.1% (25/32) explicitly used AlphaFold2. They identify three recurrent modes of AlphaFold use (initial model generation, domain-level fitting/validation, functional inference), report no significant statistical association between map resolution and AlphaFold usage, and argue that AlphaFold is most effective as a complementary tool requiring experimental validation, particularly for dynamic or heterogeneous systems.
- **Visible evidence base** Main text including Introduction, Results (three sections), Discussion, Conclusion, Methods; Table 1 (32 EMDB entries with resolution, AlphaFold usage, DOI); Figures 1–7 (cryo-EM reconstructions); references to Supplementary Figures S1, Tables S1–S2, Data File 1, and Code
- **Missing materials affecting confidence** Supplementary Information (figures, tables, data file, code) not provided; figure images not viewable; specific pLDDT values and statistical outputs not fully reported in text; DOI links in Table 1 not resolved; no abstract provided

## Reviewer
- **Overall assessment** This manuscript provides a useful and timely synthesis of AlphaFold2 usage in cryo-EM and cryo-ET workflows, drawing on a defined corpus of 2024 EMDB depositions. The central message, that AlphaFold2 is most effective as an integrative tool requiring experimental validation rather than a standalone solution, is reasonable and consistent with the broader literature. However, the manuscript has several significant weaknesses that currently limit its impact. The dataset of 32 studies is small and the sampling strategy is described as purposive rather than systematic, which weakens the quantitative claims. The statistical analysis is underpowered and the interpretation of the null result is not sufficiently cautious. The manuscript also contains internal inconsistencies, including a mismatch between the stated study period (2022–2025 in the Introduction) and the Methods (2024 only), and a reference to a "PROTAC ternary complex case (Fig. 5C)" for which no corresponding figure panel is described. The distinction between the authors' own analysis and claims drawn from cited studies is sometimes unclear, and several statements in the Discussion and Future Perspectives sections are presented without direct support from the dataset. The writing is generally clear but would benefit from more precise language regarding the strength of the evidence.

- **Who would be interested in the results, and why** Structural biologists using cryo-EM or cryo-ET who are considering whether and how to integrate AlphaFold2 predictions into their workflows would find this review relevant. Computational biologists developing or benchmarking structure prediction tools may also be interested in the observed patterns of AlphaFold adoption. The manuscript offers a practical framing of AlphaFold's strengths and limitations in the context of experimental structure determination, which could be useful for method selection and experimental design.

- **Major strengths**
  1. The manuscript addresses a timely and important question: how AlphaFold2 is actually being used in cryo-EM and cryo-ET workflows, and where it falls short.
  2. The authors provide a concrete, tabulated dataset (Table 1) with EMDB accessions, resolutions, and AlphaFold usage, which supports transparency and reproducibility.
  3. The case studies are diverse, spanning viral assemblies, chromatin, nuclear pore complexes, and protein engineering, which gives the review breadth.
  4. The authors explicitly acknowledge the limitations of their dataset and frame their conclusions as descriptive rather than definitive.
  5. The operational definition of "AlphaFold contribution" is clearly stated, which helps the reader interpret the quantitative claims.

- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Internal consistency
- **Claim pointer** The Introduction states the review covers studies from 2022–2025, while the Methods and Conclusion state the dataset is restricted to 2024 EMDB depositions.
- **Evidence pointer** Introduction, "Transitional Summary and Study Rationale"; Methods, "EMDB-Based Dataset Collection and Literature Screening"; Conclusion
- **Concern** The stated study period is inconsistent. The Introduction says "we critically examine recent studies (2022–2025)", but the Methods clearly state that the EMDB search was restricted to entries deposited between 1 January and 31 December 2024, and the Conclusion repeats "32 EMDB-linked studies from a single year". This is a substantive discrepancy that affects the reader's understanding of the scope of the review. If the dataset is indeed limited to 2024, the Introduction should be corrected. If the dataset includes studies from 2022–2025, the Methods need to be revised to reflect the actual search and inclusion criteria.
- **Why it matters** The scope of the review is a core element of its contribution. An inconsistent statement of the study period undermines the credibility of the entire manuscript and makes it difficult for readers to assess the generalizability of the findings.
- **Resolution test** The authors must reconcile the stated study period across the Introduction, Methods, and Conclusion. The final manuscript should state a single, consistent time window for the dataset, and the Methods should describe the search and inclusion criteria that match that window.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Support for claims
- **Claim pointer** The manuscript states that "AlphaFold2 predicted the structures of five core proteins (A3, A4, L10, L4, and F17) with high confidence (pLDDT > 90)" and that these models were "docked into cryo-EM maps at 7.7–13.4 Å resolution (EMD-17704, EMD-17708, EMD-17753)".
- **Evidence pointer** Results, "Structural Elucidation of Viral Core Proteins"; Table 1
- **Concern** The claim that AlphaFold2 predicted these five proteins with pLDDT > 90 is presented as a finding of the reviewed study, but the manuscript does not provide the source of this pLDDT value. It is unclear whether this value was reported in the original publication, was computed by the authors of this review, or is an interpretation. Additionally, the manuscript does not specify which of the three EMDB entries (EMD-17704, EMD-17708, EMD-17753) corresponds to which protein, making it difficult to verify the claim. The text also states that "A10 and A4 form a curved heterodimeric scaffold" and that "L4 and F17 stabilize the genomic core", but the supporting evidence for these specific structural assignments is not described.
- **Why it matters** The pLDDT value is a quantitative claim that the reader cannot verify from the provided text. If the value is not from the original publication, the authors must state how it was obtained. The lack of correspondence between proteins and EMDB entries also prevents the reader from assessing whether the docking and structural interpretation are appropriate.
- **Resolution test** The authors should specify the source of the pLDDT values (original publication, recomputation, or other) and provide a clear mapping between the five proteins and the three EMDB entries. If the pLDDT values were not reported in the original studies, the authors should either recompute them and state the method, or remove the specific value and describe the confidence qualitatively.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Support for claims
- **Claim pointer** The manuscript states that "AlphaFold2 predicted that ORF6 binds the cytoplasmic filaments of NPCs via a helical domain, sterically blocking nuclear import. This prediction was experimentally confirmed by fluorescence polarization assays."
- **Evidence pointer** Results, "Nuclear Pore Dynamics and Viral Antagonism"
- **Concern** The manuscript does not provide a citation for the fluorescence polarization assay or describe the experimental details. It is unclear whether this confirmation was performed in the original study being reviewed, in a separate study, or by the authors of this review. The claim is presented as a fact without sufficient attribution.
- **Why it matters** The claim that a prediction was "experimentally confirmed" is a strong statement that requires a clear source. Without a citation or description of the experiment, the reader cannot assess the validity of the confirmation or the strength of the evidence.
- **Resolution test** The authors should provide a citation for the fluorescence polarization assay and clarify whether the confirmation was part of the reviewed study or a separate publication. If the confirmation was not performed, the claim should be rephrased to reflect the level of evidence actually available.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Statistical interpretation
- **Claim pointer** The manuscript reports that "chi-square (χ² = 0.20, p = 0.656), Fisher's exact (p = 0.640), and Spearman's ρ (ρ = –0.163, p = 0.640)" revealed no significant association between nominal map resolution and AlphaFold usage.
- **Evidence pointer** Results, "Statistical Analysis of AlphaFold Usage by Resolution"
- **Concern** The interpretation of the null result is presented as evidence that "the decision to use AlphaFold2 is driven more by local interpretability and compositional complexity than by global nominal resolution." This is an overinterpretation. A null result with n = 32 does not provide positive evidence for any particular driver of AlphaFold usage; it only indicates that the test lacked power to detect an association. The authors acknowledge the power limitation but still draw a causal inference that is not supported by the data.
- **Why it matters** The claim about what "drives" AlphaFold usage is a causal statement that cannot be supported by a correlational analysis with a small sample. This overreach weakens the scientific credibility of the manuscript.
- **Resolution test** The authors should rephrase the interpretation to state that no significant association was detected in this sample, and that the drivers of AlphaFold usage remain to be determined. Alternatively, they could present the qualitative observations from the case studies as hypotheses rather than conclusions.

- **Concern ID** R1-M5
- **Severity** Major
- **Blocking** No
- **Axis** Internal consistency
- **Claim pointer** The manuscript refers to a "PROTAC ternary complex case (Fig. 5C)" in the Future Perspectives section, but Figure 5 is described in the Results as showing only a single panel (A) depicting the human cardiac thick filament.
- **Evidence pointer** Results, "Dynamic Structural Transitions and Conformational Flexibility"; Future Perspectives
- **Concern** The reference to "Fig. 5C" for a PROTAC ternary complex is inconsistent with the description of Figure 5 in the Results, which describes only one panel (A) for the cardiac thick filament. This suggests either a missing figure panel, an incorrect figure reference, or a claim that is not supported by the described data.
- **Why it matters** Inconsistent figure references undermine the reader's ability to follow the argument and suggest that the manuscript may not have been carefully checked. If the PROTAC case is discussed, it should be either properly referenced to a figure that exists or described in the text without a figure reference.
- **Resolution test** The authors should correct the figure reference or remove it. If the PROTAC case is discussed in the text, it should be supported by a citation to the original study and, if a figure is needed, a new panel should be added to the appropriate figure.

- **Concern ID** R1-M6
- **Severity** Major
- **Blocking** No
- **Axis** Support for claims
- **Claim pointer** The manuscript states that "template- or fragment-based approaches (e.g., RosettaFold in low-homology membrane proteins) often fail to converge, whereas AlphaFold2 maintains plausible topology."
- **Evidence pointer** Results, "Comparison with Alternative Modeling Approaches"
- **Concern** This claim is presented without a citation or specific example. The section is titled "Comparison with Alternative Modeling Approaches" but does not provide a systematic comparison or reference to the studies that support this statement. The claim is also vague, as "often fail to converge" and "plausible topology" are not defined.
- **Why it matters** The manuscript makes a comparative claim about the performance of different methods, which is a strong statement that requires evidence. Without citations or specific examples, the claim is unsupported and could be misleading.
- **Resolution test** The authors should either provide citations to specific studies that support this comparison, or remove the claim and focus on the case studies that are actually described in the manuscript.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Results, "Prevalence, Advantages, and Limitations of AlphaFold Utilization in Structural Biology Studies"
- **Evidence pointer** Table 1
- **Issue** The table caption states "deposited between [insert date range]" with placeholder text. This appears to be an incomplete template that was not filled in.
- **Required correction** Replace the placeholder with the actual date range used for the EMDB search (presumably 1 January to 31 December 2024, as stated in the Methods).

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Methods, "Structural Visualization and Fit Assessment"
- **Evidence pointer** Methods section
- **Issue** The Methods contain placeholder text for software versions, e.g., "UCSF ChimeraX (v <ChimeraX_version>)" and "UCSF Chimera (v <Chimera_version>)". These placeholders should be replaced with the actual versions used.
- **Required correction** Provide the specific software versions used for visualization and fitting.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Results, "Prevalence, Advantages, and Limitations of AlphaFold Utilization in Structural Biology Studies"
- **Evidence pointer** Table 1
- **Issue** The table lists "EMD-40476" with a resolution of 21.7 Å, but the text in the Results states the overall resolution window is "3.0 Å to ~31.7 Å". The table also lists "EMD-37002" at 31.7 Å. The text should be consistent with the table.
- **Required correction** Ensure that the resolution range stated in the text matches the values in Table 1. If the range is 3.0–31.7 Å, the text should say so explicitly.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Results, "Structural Elucidation of Viral Core Proteins"
- **Evidence pointer** Figure 2
- **Issue** The figure legend describes panels A–E, but the text refers to "Fig. 2D–E" for the immature viral core. The text should be consistent with the figure panels.
- **Required correction** Verify that the figure panels are correctly labeled and that the text references match the figure.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Methods, "EMDB-Based Dataset Collection and Literature Screening"
- **Evidence pointer** Methods section
- **Issue** The Methods state that "two reviewers independently performed full-text manual screening" and that "Cohen's κ for the binary label 'AF used vs not used' is reported in Supplementary Table S1." However, the actual κ value is not reported in the main text.
- **Required correction** Either report the κ value in the main text or ensure it is clearly presented in the Supplementary Table.

- **Concern ID** R1-m6
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Discussion, "Understanding the Frontiers of AlphaFold's Predictive Prowess"
- **Evidence pointer** Discussion section
- **Issue** The Discussion states that "AlphaFold's difficulties with intrinsically disordered proteins (IDPs) further illustrate the limits of its design" and provides examples (α-synuclein, Tau, p53). However, these examples are not tied to the dataset of 32 studies and appear to be general statements from the broader literature.
- **Required correction** Either provide citations for these examples or clarify that they are general observations from the literature, not findings from the reviewed dataset.

- **Concern ID** R1-m7
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Results, "Prevalence, Advantages, and Limitations of AlphaFold Utilization in Structural Biology Studies"
- **Evidence pointer** Table 1
- **Issue** The table lists "DOI link" for each entry, but the text does not provide a summary of the types of studies or the distribution of AlphaFold usage across the different topic bins (e.g., Homo sapiens, Sus scrofa, viral assemblies). This information would help the reader understand the composition of the dataset.
- **Required correction** Consider adding a brief summary of the dataset composition in the text, such as the number of studies per topic bin and the proportion using AlphaFold in each bin.

- **Concern ID** R1-m8
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Results, "AlphaFold as a complementary tool: starting models and refinement"
- **Evidence pointer** Figure 6
- **Issue** The text states that "AlphaFold predictions were indeed employed to model ZBTB20's BTB domain, offering 'high-confidence initial structural insights'". The use of quotation marks suggests a direct quote from the original study, but no citation is provided.
- **Required correction** Provide a citation for the quoted phrase or remove the quotation marks if it is not a direct quote.

- **Technical failings that need to be addressed before the case is established**
  1. The inconsistent study period (2022–2025 vs. 2024 only) must be resolved (R1-M1).
  2. The source of the pLDDT > 90 claim must be clarified (R1-M2).
  3. The fluorescence polarization confirmation must be properly cited (R1-M3).
  4. The overinterpretation of the null statistical result must be corrected (R1-M4).
  5. The inconsistent figure reference to "Fig. 5C" must be fixed (R1-M5).
  6. The unsupported comparative claim about alternative modeling approaches must be either cited or removed (R1-M6).

- **Assessment against Nature-style criteria**
  - **Originality**: The manuscript offers a useful synthesis of recent AlphaFold2 usage in cryo-EM and cryo-ET, but the core message, that AlphaFold is a complementary tool requiring experimental validation, is not novel. The dataset of 32 studies is small and the sampling is purposive, which limits the originality of the quantitative claims.
  - **Scientific importance**: The topic is important and timely, and the manuscript addresses a question of practical relevance to structural biologists. However, the small dataset and the descriptive nature of the analysis limit the significance of the findings.
  - **Interdisciplinary readership**: The manuscript is likely to appeal to structural biologists, computational biologists, and researchers using cryo-EM or cryo-ET. The case studies span diverse biological systems, which broadens the potential readership.
  - **Technical soundness**: The methods are described in reasonable detail, but the statistical analysis is underpowered and the interpretation of the null result is overreaching. The lack of citations for several key claims (pLDDT values, fluorescence polarization, comparative performance) is a technical weakness.
  - **Readability for nonspecialists**: The manuscript is generally well-written and accessible, with clear explanations of the methods and findings. However, some sections, such as the Discussion, contain statements that are not directly supported by the dataset and may confuse readers who are not familiar with the broader literature.

- **Recommendation posture** Supportive if technical concerns are resolved. The manuscript addresses a relevant and timely topic, and the case studies are informative. However, the internal inconsistencies, unsupported claims, and overinterpretation of the statistical results must be addressed before the manuscript can be considered for publication. The authors should also clarify the scope of the dataset and ensure that all claims are properly attributed to the reviewed studies or the broader literature.