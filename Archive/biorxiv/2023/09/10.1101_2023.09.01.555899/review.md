## Review setup
- **Input scope** Full manuscript text, figures, and figure legends
- **Assessment boundary** Scientific claims, experimental design, data interpretation, and conclusions as presented in the provided manuscript
- **Shared manuscript claim summary** The authors report a novel interaction between SARS-CoV-2 NSP3 and fragile X mental retardation proteins (FMRPs), map the binding interface, demonstrate that this interaction is required for efficient viral replication in vitro and in vivo, and propose a mechanism involving competition with UBAP2L for FMRP binding, thereby disrupting stress granule incorporation of FMRPs.
- **Visible evidence base** Abstract, Introduction, Results (narrative), Discussion, Materials and Methods, Figure legends, Supplemental figure legends
- **Missing materials affecting confidence** Raw proteomics data, full Western blot images, microscopy images, histopathology images, viral growth curves, statistical analysis details, and complete figure panels are not provided in the text. The manuscript appears to be a preprint without full figure data available for independent assessment.

## Reviewer
- **Overall assessment** This manuscript presents a potentially interesting and novel finding that SARS-CoV-2 NSP3 binds FMRPs through a defined peptide motif, competing with UBAP2L and thereby affecting stress granule composition. The work combines virology, biochemistry, structural modeling, and in vivo infection studies. However, the evidence as presented in the text is incomplete, and several key claims cannot be fully evaluated without access to the actual figures and raw data. The mechanistic model is plausible but requires stronger experimental support, particularly regarding the functional significance of the NSP3-FMRP interaction during infection and the proposed competition mechanism.
- **Who would be interested in the results, and why** Virologists studying SARS-CoV-2 host-pathogen interactions, researchers interested in stress granule biology and antiviral innate immunity, and investigators studying fragile X syndrome and FMRP function. The work bridges virology and neurobiology, potentially attracting a broad readership interested in host factor hijacking and the molecular basis of genetic disorders.
- **Major strengths** 1) Identification of a novel host-pathogen interaction with potential relevance to viral pathogenesis. 2) Combination of unbiased proteomics with targeted biochemical validation. 3) Demonstration of functional relevance through recombinant viruses in vitro and in vivo. 4) Mechanistic insight into FMRP biology that may have implications beyond virology. 5) The finding that a viral protein mimics RNA binding to KH domains is conceptually interesting.
- **Major Concerns** 
- **Minor Comments** 
- **Technical failings that need to be addressed before the case is established** The manuscript lacks sufficient experimental detail and raw data presentation to fully validate the claims. Key experiments such as the in vivo infection studies, histopathology, and quantitative comparisons are described only in narrative form without supporting data shown.
- **Assessment against Nature-style criteria** 
- **Recommendation posture** Currently not established from the provided evidence

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence completeness
- **Claim pointer** The authors claim that NSP3 mutant viruses have attenuated replication in vitro and delayed disease onset in vivo.
- **Evidence pointer** Results section "SARS-CoV-2 NSP3 mutant viruses have attenuated replication in vitro" and "NSP3 mutants are attenuated during early in vivo infection"; Figures 1D-F, 2A-H
- **Concern** The text describes viral growth curves in VeroE6 and Calu3 cells and hamster infection studies, but the actual data (growth curves, weight loss graphs, viral titers, histopathology images) are not presented in the manuscript text provided. The claims of attenuation and delayed disease onset cannot be independently assessed without seeing the actual data and statistical analyses.
- **Why it matters** The functional relevance of the NSP3-FMRP interaction during infection is a central claim of the manuscript. Without visible data supporting the attenuation phenotype, the significance of the biochemical findings for viral infection remains unsubstantiated.
- **Resolution test** Provide the actual growth curve data with statistical analysis, weight loss curves, viral titer measurements, and histopathology images with quantification. The data should clearly demonstrate the magnitude and statistical significance of the attenuation phenotype.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Mechanistic support
- **Claim pointer** The authors claim that NSP3 binding to FMRPs disrupts their interaction with UBAP2L through direct competition, preventing FMRP incorporation into stress granules.
- **Evidence pointer** Results section "NSP3 disrupts the interaction between FMRPs and UBAP2L" and "The incorporation of FMRPs into stress granules is disrupted by NSP3"; Figures 4A-H, 5A-D
- **Concern** The competition mechanism is supported by proteomics data showing displacement of UBAP2L from FMRP in the presence of NSP3 peptide, and by ITC competition experiments. However, the actual proteomics data, ITC thermograms, and immunofluorescence images are not shown in the provided text. The claim that NSP3 prevents FMRP incorporation into stress granules during infection is based on correlative observations, and the direct demonstration that this occurs during actual viral infection (rather than with overexpressed peptides) is not clearly established.
- **Why it matters** The proposed mechanism of action is the core novelty of the manuscript. Without clear evidence that competition occurs in the context of infection and that this affects stress granule formation functionally, the mechanistic model remains speculative.
- **Resolution test** Show the proteomics data with statistical analysis, ITC thermograms with fitted curves, and immunofluorescence images demonstrating FMRP localization during infection with WT vs mutant viruses. Provide quantitative analysis of stress granule incorporation.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Structural evidence
- **Claim pointer** The authors claim that the NSP3 peptide binds to the KH domains of FMRPs in a manner similar to RNA binding, and that the I304N mutation disrupts this interaction.
- **Evidence pointer** Results section "SARS-CoV-2 NSP3 binds to RNA binding region of the FMRP KH domains"; Figures 3A-E, Supplemental Figures S3A-D
- **Concern** The structural model is based on AlphaFold predictions, which are computational and not experimentally validated. The claim of "RNA mimicry" is inferred from the model and the observation that the peptide binds to the same region where RNA binds. However, the authors state they could not detect RNA binding to the KH domains, which weakens the RNA mimicry analogy. The experimental evidence for the binding interface relies on mutagenesis and ITC, but the actual data are not shown.
- **Why it matters** The structural model underpins the mechanistic interpretation and the proposed relevance to fragile X syndrome. Without experimental structural validation (e.g., co-crystal structure, NMR, or HDX-MS), the model remains speculative.
- **Resolution test** Provide the ITC data showing binding affinities and the effects of mutations. If possible, obtain an experimental structure of the NSP3 peptide bound to FMRP KH domains. Alternatively, provide additional biochemical evidence (e.g., crosslinking, hydrogen-deuterium exchange) to support the proposed binding interface.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Specificity
- **Claim pointer** The authors claim that the NSP3-FMRP interaction is specific to SARS-CoV-2 among coronaviruses, as the binding motif is conserved only in Sarbecoviruses.
- **Evidence pointer** Results section "The SARS-CoV-2 NSP3 protein binds to FMRPs"; Figure 1C, Supplemental Figure S1B-C
- **Concern** The authors tested N-terminal fragments from five other human coronaviruses and found no binding to FMRPs. However, the text does not specify which coronaviruses were tested, and the actual binding data are not shown. The claim of specificity would be strengthened by testing a broader panel of coronaviruses and by demonstrating that the motif is necessary and sufficient for binding in the context of other viral backbones.
- **Why it matters** The specificity of the interaction has implications for understanding the unique pathogenesis of SARS-CoV-2 compared to other coronaviruses and for potential therapeutic targeting.
- **Resolution test** Provide the list of coronaviruses tested and the binding data. Consider testing chimeric viruses or swapping the motif into other coronavirus NSP3 proteins to demonstrate sufficiency.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Abstract
- **Evidence pointer** Abstract
- **Issue** The abstract states that NSP3 mutant viruses have "delayed disease onset in vivo" but does not specify the magnitude or statistical significance of this delay.
- **Required correction** Include quantitative details of the in vivo phenotype in the abstract, such as the delay in days and statistical significance.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Methodology
- **Affected element** ITC experiments
- **Evidence pointer** Materials and Methods, ITC section
- **Issue** The ITC methods describe titrating FXR1 constructs into NSP3, but the exact concentrations and stoichiometry are not clearly stated. The text mentions "approximately 300 μM or 100 μM" for FXR1 constructs and "approximately 20 μM or 10 μM" for NSP3, but the rationale for these concentrations is unclear.
- **Required correction** Clarify the experimental design, including the concentrations used for each titration and the stoichiometry of binding.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Data presentation
- **Affected element** Figure legends
- **Evidence pointer** Figure legends
- **Issue** The figure legends are incomplete and do not provide sufficient detail about the experimental conditions, replicates, or statistical tests used.
- **Required correction** Expand the figure legends to include all relevant experimental details, including the number of replicates, statistical tests used, and significance thresholds.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Interpretation
- **Affected element** Discussion
- **Evidence pointer** Discussion
- **Issue** The discussion speculates about the relevance of the NSP3-FMRP interaction to fragile X syndrome without providing direct experimental evidence linking viral infection to fragile X pathology.
- **Required correction** Soften the speculation or provide additional evidence or rationale for the connection to fragile X syndrome.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Supplemental data
- **Evidence pointer** Supplemental Figure S4A
- **Issue** The text mentions that RNA binding to FMRP KH domains could not be detected, but the actual data are not shown. This negative result is important for the interpretation of the RNA mimicry hypothesis.
- **Required correction** Include the RNA binding data in the supplemental figures to support the claim.

## Risk / unsupported claims
- The claim that NSP3-FMRP binding is required for efficient viral replication in vivo is not fully supported by the data presented in the text, as the actual in vivo data are not shown.
- The claim that NSP3 disrupts FMRP incorporation into stress granules during infection is based on correlative observations and requires direct demonstration in the context of infection.
- The structural model of the NSP3-FMRP complex is based solely on AlphaFold predictions and lacks experimental validation.
- The relevance of the findings to fragile X syndrome is speculative and not directly tested.
- The claim that the NSP3-FMRP interaction is specific to SARS-CoV-2 among coronaviruses is based on limited testing and requires broader validation.