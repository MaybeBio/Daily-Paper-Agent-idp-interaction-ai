## Review setup
- **Input scope** Full manuscript text including abstract, main text, figure legends, and supplementary information list
- **Assessment boundary** Scientific claims, methodology, data interpretation, and conclusions as presented in the provided manuscript text
- **Shared manuscript claim summary** The authors quantify partitioning of ~1,700 small molecules into four different biomolecular condensates, find that partitioning varies ~1,000,000-fold but is correlated across condensates, provide evidence against site-specific binding as the dominant mechanism, and develop a machine learning model using only physicochemical features that predicts partitioning with quantitative accuracy
- **Visible evidence base** Main text with four figures (Fig 1-4), extended data figures 1-10 (referenced), supplementary tables 1-13 (referenced), supplementary methods, and source data statements
- **Missing materials affecting confidence** Actual figure images, extended data figures, supplementary tables and methods content, experimental protocols, raw data files, and code are not provided in the submitted text

## Reviewer
- **Overall assessment** This manuscript addresses an important and timely question in the condensate field, namely what governs small-molecule partitioning into biomolecular condensates. The authors present a large dataset of partitioning measurements across four condensate systems, provide evidence against a dominant role for stereospecific binding, and develop a predictive machine learning model based on physicochemical properties. The central claim that hydrophobic environment emerges upon condensate formation and drives small-molecule partitioning is interesting and potentially impactful. However, several technical concerns need to be addressed, particularly regarding the interpretation of the ITC experiments, the generalizability of the machine learning model, and the mechanistic interpretation of the correlation between condensates. The manuscript is well-written and accessible to a broad readership, but the strength of the conclusions relative to the evidence presented needs careful evaluation.

- **Who would be interested in the results, and why** Researchers in the fields of biomolecular condensates, phase separation, chemical biology, drug discovery, and cellular organization would be interested. The findings have direct implications for understanding how small molecules, including drugs and metabolites, distribute within cells and how condensate composition is determined. The machine learning model could be of practical use for predicting small-molecule partitioning and for designing drugs that target condensates. The work also speaks to fundamental questions about the physical chemistry of condensate interiors.

- **Major strengths** 
  1. The study addresses a significant gap in the condensate field, as small-molecule composition has been understudied relative to macromolecular composition.
  2. The dataset is large and spans diverse chemical space, providing a valuable resource for the community.
  3. The combination of experimental measurements, biophysical characterization, and machine learning is methodologically strong.
  4. The finding that partitioning is correlated across different condensates is surprising and conceptually important.
  5. The machine learning model is validated on held-out data and could be practically useful.

- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness of ITC interpretation
- **Claim pointer** The authors state that "Twelve of the 13 drugs analysed using ITC do not bind the polySUMO–polySIM complex tightly in the absence of phase separation but are recruited strongly into SUMOSIM condensates" and use this to support the claim that partitioning is not governed by site-specific interactions.
- **Evidence pointer** Figure 2, Supplementary Figure 2, Discussion section
- **Concern** The ITC experiments were performed at a scaffold concentration of 20 µM (below the phase separation threshold) with compounds titrated up to 200 µM. The authors interpret flat ITC profiles as evidence of no binding. However, the absence of measurable heat in ITC does not necessarily mean no binding occurs. Weak binding with small enthalpy changes, or binding with compensating entropic and enthalpic contributions, can produce flat ITC profiles. Additionally, the authors only tested 13 compounds out of ~1,700, and these were selected based on high partitioning. The claim that "most compounds" do not bind scaffolds is extrapolated from a very small sample. Furthermore, the ITC experiments were performed under non-phase-separating conditions, and it is possible that binding interactions are different or enhanced within the condensed phase. The authors should acknowledge these limitations more explicitly and consider additional controls, such as testing compounds with low partitioning as negative controls, or using a different biophysical method to confirm the absence of binding.
- **Why it matters** The interpretation of the ITC data is central to the claim that partitioning is not driven by stereospecific binding. If this interpretation is flawed, the mechanistic conclusion of the paper would be substantially weakened.
- **Resolution test** The authors should provide additional evidence that the tested compounds do not bind the scaffolds, such as NMR or surface plasmon resonance experiments, or demonstrate that the ITC experiments are sufficiently sensitive to detect weak binding. They should also test a broader and more diverse set of compounds, including those with low partitioning, to strengthen the generalizability of the claim.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Generalizability of machine learning model
- **Claim pointer** The authors claim that "a machine learning model accurately predicts partitioning using only computed physicochemical features of the compounds" and that this model "provides potential routes to drugs that target condensates."
- **Evidence pointer** Figure 3, Extended Data Figure 8, Supplementary Tables 9-10
- **Concern** The machine learning model is trained and tested on data from four condensate systems, all of which are protein-based and formed by folded domains. The authors show that a combined model performs similarly to individual models, suggesting that partitioning is similar across these systems. However, the claim that the model can predict partitioning into condensates in general, and that it can be used for drug development, requires validation on a more diverse set of condensates, including those formed by intrinsically disordered proteins, RNA-based condensates, and condensates with different physical properties. The model's performance on the validation set (R2 = 0.44) is modest, and the authors acknowledge "undertraining" due to data sparsity. The claim that the model can "accurately predict" partitioning may be overstated given the validation performance. The authors should temper their claims about the model's generalizability and provide a more nuanced discussion of its limitations.
- **Why it matters** The practical utility of the model for drug development and for predicting partitioning in cellular contexts depends on its generalizability beyond the four tested systems. Overstating the model's capabilities could mislead researchers who wish to use it.
- **Resolution test** The authors should validate the model on at least one or two additional condensate systems with different compositions (e.g., an IDP-based condensate or an RNA-containing condensate). They should also provide a more detailed analysis of the model's failure modes and discuss the conditions under which the model is likely to be less accurate.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Mechanistic interpretation of correlation between condensates
- **Claim pointer** The authors state that "the different condensates showed similar ranges of PC values for the small molecules" and that "there is an underlying physical similarity between the condensates such that the same small molecules tend to be enriched or excluded by each condensate system."
- **Evidence pointer** Figure 1d-e, Extended Data Figures 4-5
- **Concern** The correlation in partitioning across condensates is a key finding, but the mechanistic interpretation is somewhat vague. The authors suggest that a "hydrophobic environment emerges upon condensate formation," but they do not provide direct evidence for this. The correlation could also be explained by other factors, such as the excluded volume effect, the ionic environment, or the presence of common chemical groups in the scaffolds. The authors should provide a more rigorous test of the "hydrophobic environment" hypothesis, for example by measuring the polarity or solvation properties of the condensate interior using environment-sensitive probes, or by comparing partitioning into condensates with systematically varied hydrophobicity.
- **Why it matters** The mechanistic claim about the hydrophobic environment is a central conclusion of the paper. Without direct evidence, it remains a hypothesis that is consistent with the data but not uniquely determined by it.
- **Resolution test** The authors should perform additional experiments to directly probe the chemical environment within condensates, such as using solvatochromic dyes or measuring the partitioning of a series of compounds with systematically varied hydrophobicity. Alternatively, they could use molecular dynamics simulations to characterize the condensate interior.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Effect of compound library composition on conclusions
- **Claim pointer** The authors claim that "the data suggest that partitioning is not driven by stereospecific binding to condensate scaffolds but rather by the general physical properties of the compounds."
- **Evidence pointer** Figure 1c, Extended Data Figures 6-7, Supplementary Tables 2-3
- **Concern** The compound library consists of ~200 metabolites and ~1,500 FDA-approved drugs. This is a biased library, as drugs are typically designed to be hydrophobic and to have good membrane permeability. The metabolites are also a specific subset of the metabolome. The authors' conclusion that partitioning is driven by hydrophobicity may be a property of this particular library and may not generalize to all small molecules. The authors should discuss this limitation and ideally test a more chemically diverse set of compounds, such as fragments or compounds from a diversity-oriented synthesis library.
- **Why it matters** The conclusions about the physical principles governing partitioning are based on a specific and potentially biased compound set. If the library is biased towards hydrophobic compounds, the importance of hydrophobicity may be overestimated.
- **Resolution test** The authors should analyze the chemical diversity of their library relative to a broader chemical space and discuss the potential impact of library composition on their conclusions. They could also test a small set of compounds with diverse physicochemical properties to see if the model's predictions hold.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity of methods
- **Affected element** Methods section
- **Evidence pointer** Main text, "location not provided"
- **Issue** The manuscript does not provide sufficient detail on the mass spectrometry-based partitioning assay. Specifically, the authors do not describe how the pellet and supernatant fractions were separated, how the compounds were extracted, or how the mass spectrometry data were processed to obtain PC values. This information is presumably in the Supplementary Methods, but it should be summarized in the main text for readers who do not consult the supplement.
- **Required correction** Add a brief description of the mass spectrometry assay in the main text, including the key steps of sample preparation, separation, and quantification.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Statistical analysis
- **Affected element** Figure 1e, Extended Data Figure 4
- **Evidence pointer** Figure 1e, Extended Data Figure 4
- **Issue** The authors report correlation coefficients (R2) between PC values for different condensates but do not report confidence intervals or p-values. Given the large number of compounds, even weak correlations may be statistically significant. The authors should report the statistical significance of the correlations and consider whether the correlations are practically meaningful.
- **Required correction** Report p-values or confidence intervals for the correlation coefficients and discuss the practical significance of the observed correlations.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Discussion of limitations
- **Affected element** Discussion section
- **Evidence pointer** Discussion section
- **Issue** The authors do not discuss the potential impact of compound concentration on partitioning. All compounds were tested at 1 µM, which is a relatively low concentration. It is possible that at higher concentrations, compound-compound interactions or saturation effects could alter partitioning behavior. The authors should discuss this limitation.
- **Required correction** Add a sentence or two in the Discussion acknowledging the potential concentration dependence of partitioning and its implications for the physiological relevance of the findings.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Terminology
- **Affected element** Abstract, Main text
- **Evidence pointer** Abstract, Main text
- **Issue** The term "partitioning" is used throughout, but the authors do not clearly define what is meant by "partition coefficient" in the context of their measurements. Is it a concentration ratio, a mole fraction ratio, or something else? This should be defined explicitly.
- **Required correction** Define the partition coefficient in the main text, ideally in the Results section where it is first introduced.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Reproducibility
- **Affected element** Data availability
- **Evidence pointer** Source data section
- **Issue** The authors state that source data are available, but the specific files are not described in detail. It is unclear what data are included in each file and in what format. This makes it difficult for readers to reproduce the analysis.
- **Required correction** Provide a more detailed description of the source data files, including the columns, units, and any processing steps applied.

## Risk / unsupported claims
- The claim that "a hydrophobic environment emerges upon condensate formation" is presented as a conclusion but is not directly tested. It is a plausible hypothesis that is consistent with the data but is not uniquely supported by the evidence presented.
- The claim that "most compounds" do not bind scaffolds is based on ITC experiments with only 13 compounds, which is a small and potentially biased sample. This claim is not fully supported by the data.
- The claim that the machine learning model "accurately predicts partitioning" is somewhat overstated given the validation R2 of 0.44. The model is predictive but with substantial error.
- The generalizability of the findings to condensates beyond the four tested systems is not established. The authors acknowledge this in the Discussion but do not provide evidence to support broader generalizability.
- The claim that "the data suggest that partitioning is not driven by stereospecific binding" is supported by the correlation analysis and the ITC data, but the ITC data are limited, and the correlation analysis does not rule out the possibility that weak, non-specific binding contributes to partitioning.