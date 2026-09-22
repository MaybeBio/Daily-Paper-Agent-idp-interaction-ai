## Review setup
- **Input scope** Full manuscript text (abstract, introduction, materials and methods, results, discussion, conclusion, supplementary material references)
- **Assessment boundary** Scientific validity, technical soundness, and support of claims based solely on the provided manuscript text. No external data, figures, or supplementary files were available for direct inspection.
- **Shared manuscript claim summary** The authors report the design, expression, purification, and characterization of fusion proteins comprising the IL-17A-inhibitory peptide HAP and elastin-like polypeptides (ELPs) with different phase transition temperatures. They claim that (1) AlphaFold3 predicts retention of HAP binding to IL-17A upon ELP fusion, (2) the fusions retain binding and inhibitory activity in vitro, (3) ELP composition controls pharmacokinetics and depot persistence after local injection, and (4) the purified materials do not stimulate innate or adaptive immune responses in mice.
- **Visible evidence base** Text descriptions of results including in silico predictions (Fig. 1), cloning and purification data (Fig. 2, Table 1, Supplementary Figs. S1–S2), thermoresponsive behavior (Fig. 3), SPR binding (Fig. 4, Supplementary Figs. S4–S5), in vitro inhibition (Fig. 5, Supplementary Fig. S6), pharmacokinetics (Fig. 6, Table 2, Supplementary Fig. S8), and immunogenicity (Fig. 7, Supplementary Figs. S9–S10). Actual figures, tables, and supplementary files were not provided.
- **Missing materials affecting confidence** All figures, tables, and supplementary files. Numerical data for pharmacokinetic parameters (Table 2) and detailed statistical outputs are not available. The in silico analysis script (Script S1) and protocol (Supplementary Method 1) are referenced but not provided. Animal numbers, sex, and randomization details for in vivo studies are not stated.

## Reviewer
- **Overall assessment** The manuscript presents a conceptually interesting approach to local IL-17A inhibition using peptide-ELP fusions, with a logical progression from in silico prediction to in vitro and in vivo characterization. The central claims are plausible and the work addresses a genuine clinical need. However, the evidence base as presented in the text is incomplete, and several claims cannot be fully evaluated without access to the figures and supplementary data. The in silico validation, while useful, is limited by the likely inclusion of the reference structure in the training set, and the authors acknowledge this. The in vivo pharmacokinetic and immunogenicity data are described but key quantitative details are missing. The manuscript would be strengthened by clearer presentation of statistical methods, animal study design, and a more critical discussion of the limitations of the AlphaFold3 predictions.
- **Who would be interested in the results, and why** Researchers in drug delivery, protein engineering, and ocular immunology would find this work relevant. The demonstration of tunable ELP-based depots for local cytokine inhibition could inform the design of similar systems for other therapeutic targets. The use of AlphaFold3 as a screening tool for fusion protein design may also be of interest to the broader protein engineering community.
- **Major strengths** The study addresses a clinically relevant problem with a rational design strategy. The combination of in silico prediction, biophysical characterization, and in vivo assessment is comprehensive. The use of two ELPs with different transition temperatures provides a clear demonstration of tunable pharmacokinetics. The immunogenicity assessment is an important and often-overlooked component for biologic therapies.
- **Major Concerns**
  - **Concern ID** R1-M1
  - **Severity** Major
  - **Blocking** Yes
  - **Axis** Evidence completeness
  - **Claim pointer** The authors claim that AlphaFold3 predictions align with in vitro binding and inhibition data, and that the fusions retain HAP activity.
  - **Evidence pointer** Fig. 1, Fig. 4, Fig. 5, Supplementary Figs. S4–S6
  - **Concern** The manuscript text describes the results but the actual figures and supplementary data are not provided. Without these, it is impossible to verify the quality of the SPR sensorgrams, the statistical significance of the RMSD comparisons, the dose-response curves for the inhibition assays, or the specificity of the depletion experiments. The claim of alignment between prediction and experiment cannot be assessed.
  - **Why it matters** The central thesis of the paper rests on the concordance between computational prediction and experimental validation. If the data are not presented clearly or are of insufficient quality, the conclusion that AlphaFold3 can be used to design functional fusion proteins is not supported.
  - **Resolution test** Provide the figures and supplementary data for inspection. The SPR sensorgrams should show clear, concentration-dependent binding with appropriate controls. The RMSD comparisons should include appropriate statistical tests. The inhibition curves should show complete dose-response with calculated IC50 values and confidence intervals.
  - **Concern ID** R1-M2
  - **Severity** Major
  - **Blocking** Yes
  - **Axis** Experimental design and reporting
  - **Claim pointer** The authors claim that HAP-ELP fusions do not measurably stimulate the innate or adaptive immune system based on in vivo studies.
  - **Evidence pointer** Fig. 7, Supplementary Figs. S9–S10
  - **Concern** The in vivo immunogenicity study is described with minimal detail. The number of animals per group, sex, age, and statistical methods are not reported. The CRP assay is described but the time point for measurement is only stated as 16 h. The ADA assay is described but the sensitivity and specificity are not fully validated. The histological analysis is mentioned but no criteria for inflammation scoring are provided.
  - **Why it matters** Immunogenicity is a critical safety concern for any biologic. If the study is underpowered or the assays are not properly validated, the conclusion that the fusions are non-immunogenic is not reliable.
  - **Resolution test** Provide full details of the animal study design, including group sizes, sex, age, and statistical analysis. Describe the validation of the ADA ELISA, including the limit of detection and the positive control used. Provide the criteria used for histological scoring of inflammation.
  - **Concern ID** R1-M3
  - **Severity** Major
  - **Blocking** No
  - **Axis** Interpretation of pharmacokinetic data
  - **Claim pointer** The authors claim that ELP composition allows manipulation of pharmacokinetics, specifically mean absorption time, and that HAP-V96 forms persistent depots.
  - **Evidence pointer** Fig. 6, Table 2, Supplementary Fig. S8
  - **Concern** The pharmacokinetic analysis relies on fluorescent labelling and IVIS imaging. The text states that HAP-V96 showed 52% of initial signal at day 12, but the calculation of mean residence time (81 h) and mean absorption time are not described in detail. The bioavailability calculation for HAP-V96 is stated to be low, but the value is not given. The use of HAP-A96 as a proxy for systemic clearance of both constructs is a potential confounder, as the authors acknowledge.
  - **Why it matters** The pharmacokinetic claims are central to the therapeutic potential of the system. If the analysis is not robust or the assumptions are not clearly stated, the conclusion that HAP-V96 provides extended local therapy is weakened.
  - **Resolution test** Provide the full non-compartmental analysis, including the method for calculating MRT and MAT. Report the bioavailability value for HAP-V96. Discuss the potential impact of using HAP-A96 for systemic clearance on the interpretation of HAP-V96 absorption.
- **Minor Comments**
  - **Concern ID** R1-m1
  - **Severity** Minor
  - **Axis** Clarity
  - **Affected element** Introduction, paragraph 1
  - **Evidence pointer** Location not provided
  - **Issue** The introduction states that IL-17A is "the most potent member of the IL-17 cytokine family" without providing a comparative context or citation for this specific claim.
  - **Required correction** Provide a citation or qualify the statement to avoid overstatement.
  - **Concern ID** R1-m2
  - **Severity** Minor
  - **Axis** Reproducibility
  - **Affected element** Materials and methods, "In silico validation" section
  - **Evidence pointer** Location not provided
  - **Issue** The description of the AlphaFold3 analysis states that "at least 15" predictions were used, but the exact number and the criteria for selecting the best prediction are not specified.
  - **Required correction** Specify the exact number of predictions and the selection criteria.
  - **Concern ID** R1-m3
  - **Severity** Minor
  - **Axis** Data presentation
  - **Affected element** Results, "Thermoresponsive behavior" section
  - **Evidence pointer** Fig. 3
  - **Issue** The text describes a phase diagram but does not state the concentration range tested or the number of replicates for each condition.
  - **Required correction** Include the concentration range and replicate numbers in the figure legend or text.
  - **Concern ID** R1-m4
  - **Severity** Minor
  - **Axis** Terminology
  - **Affected element** Results, "In vitro inhibition" section
  - **Evidence pointer** Fig. 5
  - **Issue** The term "IC50" is used, but the text does not specify whether this is the concentration of HAP-ELP that inhibits 50% of the IL-17A response, or the concentration of IL-17A that is inhibited by 50%.
  - **Required correction** Clarify the definition of IC50 in this context.
  - **Concern ID** R1-m5
  - **Severity** Minor
  - **Axis** Completeness
  - **Affected element** Materials and methods, "Animals" section
  - **Evidence pointer** Location not provided
  - **Issue** The sex and age of the mice used in the studies are not stated.
  - **Required correction** Include sex and age of animals in the methods.
  - **Concern ID** R1-m6
  - **Severity** Minor
  - **Axis** Statistical reporting
  - **Affected element** Statistical analysis section
  - **Evidence pointer** Location not provided
  - **Issue** The statistical analysis section mentions ANOVA and Tukey's test but does not state the number of independent experiments or whether the data met the assumptions of the tests.
  - **Required correction** Provide details on the number of independent experiments and any data transformations used.

## Risk / unsupported claims
- The claim that AlphaFold3 predictions "align" with experimental results is not verifiable without the figures and statistical analysis.
- The claim that the fusions do not stimulate the immune system is based on a study with unreported animal numbers and assay validation details.
- The pharmacokinetic parameters (MRT, MAT, bioavailability) are reported without the underlying data or analysis details.
- The statement that the fusions are "bacterially derived" and therefore potentially immunogenic is discussed, but the endotoxin removal efficiency is only stated as below 0.05 EU/kg without showing the data.
- The claim that HAP-V96 has a "low bioavailability" that is "beneficial to treatment" is an interpretation that requires more context on the therapeutic window and target tissue exposure.

## Assessment against Nature-style criteria
- **Originality** The concept of fusing a peptide inhibitor to ELPs for local, depot-forming cytokine inhibition is not entirely new, but the specific application to IL-17A and the use of AlphaFold3 as a design tool adds a novel element. The work is incremental rather than paradigm-shifting.
- **Scientific importance** The clinical need for local IL-17A inhibition is real, and the approach could have impact if the pharmacokinetic and efficacy data are robust. However, the manuscript does not present efficacy data in a disease model, which limits the immediate importance.
- **Interdisciplinary readership** The work bridges protein engineering, drug delivery, and immunology, and would be of interest to researchers in these fields. The use of AI-based prediction tools may attract a broader computational audience.
- **Technical soundness** The experimental design is generally sound, but the lack of detail on animal studies and the incomplete presentation of data prevent a full assessment. The reliance on fluorescent imaging for pharmacokinetics without corroborating methods is a concern.
- **Readability for nonspecialists** The manuscript is clearly written and the logic is easy to follow. The introduction and discussion provide sufficient context for readers outside the immediate field.

## Recommendation posture
Supportive if technical concerns are resolved. The core idea is promising and the preliminary data are encouraging, but the manuscript in its current form does not provide sufficient evidence to fully establish the claims. The authors must provide the missing data, clarify the experimental details, and address the concerns raised above before the case is made.