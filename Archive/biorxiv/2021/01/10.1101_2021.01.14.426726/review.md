## Review setup
- **Input scope** Full manuscript text (abstract, introduction, results, discussion, conclusion, methods, footnotes) from bioRxiv preprint
- **Assessment boundary** Scientific claims, methodological soundness, evidence quality, and internal consistency as presented in the supplied material
- **Shared manuscript claim summary** The authors propose that the R203K and G204R mutations in the SARS-CoV-2 nucleocapsid (N) protein alter protein structure, phosphorylation-dependent dynamics, subcellular localization, and HLA-specific antigen presentation, with population-level implications for COVID-19 severity and mortality
- **Visible evidence base** Sequence alignments (Fig. 1), energy calculations (Fig. 3), phosphorylation predictions (Figs. 4, 5), localization predictions (Fig. 6), B-cell epitope predictions (Fig. 7, Fig. S2), T-cell epitope predictions (Tables 1, 2), and population frequency data (Section 2.6)
- **Missing materials affecting confidence** No raw sequence data, no structural coordinates or validation metrics beyond ProSA, no detailed HLA allele frequency tables, no statistical analysis, no experimental validation, no figure images, no supplementary methods details

## Reviewer
- **Overall assessment** This manuscript presents a purely computational analysis of two SARS-CoV-2 N protein mutations with claims spanning structural biology, phosphorylation dynamics, immunogenicity, and population-level disease correlation. While the topic is timely and potentially relevant, the evidence provided is almost entirely predictive and lacks experimental validation, statistical rigor, and methodological transparency. The central claims, particularly those linking HLA allele frequencies to COVID-19 mortality, are speculative and not supported by the data presented. The manuscript requires substantial revision and additional evidence before the case can be considered established.
- **Who would be interested in the results, and why** Researchers studying SARS-CoV-2 evolution and variant surveillance, immunologists focused on HLA-restricted T-cell responses, and computational biologists developing structure-based prediction methods. The potential link between specific HLA alleles and disease severity could interest epidemiologists and public health researchers, though the speculative nature of these claims limits immediate utility.
- **Major strengths** The manuscript addresses a relevant and timely question regarding the functional impact of prevalent SARS-CoV-2 N protein mutations. The use of multiple computational tools (ClustalW, NetPhos, DeepLoc, IEDB, TepiTool) demonstrates a broad approach. The identification of phosphorylation sites near the mutation region and the consideration of population-level HLA frequencies are conceptually interesting angles.
- **Major Concerns** See detailed items below.
- **Minor Comments** See detailed items below.
- **Technical failings that need to be addressed before the case is established** R1-M1 (structural modeling validation), R1-M2 (phosphorylation claim support), R1-M3 (HLA prediction methodology), R1-M4 (population correlation claim), R1-M5 (statistical analysis absence)
- **Assessment against Nature-style criteria** Originality: Moderate. The specific mutation pair has been noted in surveillance studies, but the structural and immunological modeling is somewhat novel. Scientific importance: Potentially high if validated, but current evidence is insufficient. Interdisciplinary readership: The topic bridges virology, immunology, and population genetics, which could attract broad interest. Technical soundness: Weak. Multiple methodological gaps and unsupported claims undermine confidence. Readability for nonspecialists: Generally accessible, though some sections lack clarity and precision.
- **Recommendation posture** Currently not established from the provided evidence. The manuscript requires major revisions, additional validation, and significant methodological clarification before it could be considered for publication.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors claim to present a "structure-based model" of the N protein and its mutations, with energy calculations indicating "enhanced structural flexibility" for the mutant.
- **Evidence pointer** Section 2.2, Fig. 3, Section 5.2, Section 5.3
- **Concern** The structural modeling methodology is critically underdescribed. The authors state that the tertiary structure was predicted using IntFOLD5, but no details are provided regarding model quality, template selection, or confidence scores. The energy calculations are attributed to ProSA, but the specific implementation, reference structures, and validation metrics are absent. The claim of "enhanced structural flexibility" is based on a single energy plot without any conformational sampling or dynamics simulation. The statement that "the relative orientation of NTD and CTD, as well as the conformations of the disordered regions, are drawn randomly" (Section 2.2) is particularly concerning, as it suggests the structural model is not deterministic or reproducible.
- **Why it matters** The structural claims form the foundation for subsequent arguments about phosphorylation, immunogenicity, and functional impact. Without a validated and reproducible structural model, all downstream conclusions are compromised.
- **Resolution test** Provide detailed structural modeling methodology, including template selection, model quality scores (e.g., QMEAN, pLDDT), and validation metrics. Include explicit coordinates or a reproducible pipeline. If flexibility is claimed, provide molecular dynamics simulations or other conformational analysis with quantitative metrics.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence sufficiency
- **Claim pointer** The authors claim that the RG>KR mutation affects phosphorylation-dependent binding and sequestration, specifically that "the G204R mutation decreases the conformational entropy of neutralization by increasing the positive charge in the vicinity of negatively charged P-Ser202/205 phosphate groups."
- **Evidence pointer** Section 2.3, Figs. 4, 5
- **Concern** The phosphorylation analysis relies solely on NetPhos 3.1 predictions, which are computational predictions and not experimental evidence. The claim about "charge neutralization" and "conformational entropy" is presented as a mechanistic conclusion but is not supported by any direct measurement, simulation, or experimental data. The predicted phosphorylation sites (Ser202, Ser205, Ser206) are identified, but no validation of these predictions is provided. The functional significance of these phosphorylation events is asserted without evidence.
- **Why it matters** The phosphorylation-dependent mechanism is a central pillar of the proposed model. Without experimental validation or at minimum rigorous computational support (e.g., molecular dynamics with phosphorylated residues), this claim is speculative.
- **Resolution test** Provide experimental validation of phosphorylation (e.g., in vitro kinase assays, mass spectrometry) or, at minimum, molecular dynamics simulations comparing phosphorylated and non-phosphorylated states with quantitative free energy calculations.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors claim that wild-type N protein binds HLA-A*30:01 and HLA-A*30:21, while mutant N protein binds HLA-A*31:01 and HLA-A*68:01, and that this differential binding has functional consequences.
- **Evidence pointer** Section 2.6, Tables 1, 2, Section 5.5
- **Concern** The T-cell epitope prediction methodology is inadequately described. The authors state they used TepiTool with default parameters, but the specific HLA allele panel, peptide length, and prediction algorithm versions are not specified. The results in Tables 1 and 2 are not shown in the supplied material, so the actual predictions cannot be evaluated. The claim that "HLA-A*31:01, associated with mutant and wild type strains" (Section 3) is confusing, as the abstract and results state that wild type binds HLA-A*30:01/30:21 and mutant binds HLA-A*31:01/68:01. This inconsistency is not addressed.
- **Why it matters** The differential HLA binding is the core immunogenicity claim. Without transparent methodology and accessible results, the claim cannot be evaluated or reproduced.
- **Resolution test** Provide complete tables of predicted peptides with percentile ranks, specify the exact HLA allele panel and prediction algorithm versions, and clarify the inconsistency regarding HLA-A*31:01 association with both wild type and mutant.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** Yes
- **Axis** Scientific importance
- **Claim pointer** The authors claim that "HLA-A*68:01 allele frequencies worldwide could positively correlate with the severity of coronavirus cases and a high number of deaths" and that "low HLA-A*68:01 expression could correlate with the low number of COVID-19-attributable deaths seen in Japan."
- **Evidence pointer** Section 3, Section 2.6
- **Concern** This population-level claim is a major extrapolation from computational epitope predictions. No epidemiological data, statistical correlation analysis, or adjustment for confounding variables is provided. The comparison between South America and Japan is anecdotal and ignores numerous other factors (healthcare infrastructure, testing rates, population demographics, public health measures) that influence COVID-19 mortality. The claim is presented as a conclusion rather than a hypothesis.
- **Why it matters** This claim has significant public health implications and could be misinterpreted. Making such assertions without rigorous epidemiological evidence is scientifically irresponsible.
- **Resolution test** Provide a formal epidemiological analysis with appropriate statistical methods, controlling for confounders, or clearly reframe this as a speculative hypothesis requiring further investigation.

- **Concern ID** R1-M5
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors claim that the mutant strain shows "slightly high free energy at residues 203/204" and that this indicates "enhanced structural flexibility and increased the tendency for the formation of a coil or a bend."
- **Evidence pointer** Section 2.2, Fig. 3
- **Concern** No statistical analysis is provided for any of the computational predictions. The energy differences between wild type and mutant are described as "slightly high" without quantification or error estimates. The population frequency comparisons (18.38% vs 28.25%) are presented without confidence intervals or significance testing. Throughout the manuscript, claims are made without any measure of uncertainty.
- **Why it matters** Without statistical rigor, the reader cannot assess whether the observed differences are meaningful or within the noise of the prediction methods.
- **Resolution test** Provide statistical analysis for all quantitative comparisons, including confidence intervals, p-values, or effect sizes, and clearly state the uncertainty associated with each prediction method.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Abstract
- **Evidence pointer** Abstract
- **Issue** The abstract states "HLA-A*30:01 and HLA-A*30:21" for wild type, but Section 2.6 states "HLA-A*30:01 and HLA 31:01 predictions" for wild type. This inconsistency is confusing.
- **Required correction** Reconcile the HLA allele lists between the abstract and results sections.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Reproducibility
- **Affected element** Methods
- **Evidence pointer** Section 5.1
- **Issue** The methods state that sequences were analyzed "up to September 07th, 2020," but the manuscript was posted in January 2021. The number of sequences analyzed is not reported, and the selection criteria for sequences are unclear.
- **Required correction** Report the number of sequences analyzed, the database version, and the inclusion criteria.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Section 2.1
- **Evidence pointer** Section 2.1, Fig. 1
- **Issue** The text states the LKR is "68 nucleotides long" in Section 2.1 but "43 nucleotides long" in Section 5.1. This discrepancy is not explained.
- **Required correction** Clarify the correct length of the LKR region and ensure consistency between sections.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Technical soundness
- **Affected element** Section 2.4
- **Evidence pointer** Section 2.4, Fig. 6
- **Issue** The DeepLoc predictions (0.861 and 0.913) are described as suggesting "predominantly found in the nucleus," but the threshold for nuclear localization is not stated, and the biological significance of the difference between wild type and mutant is not discussed.
- **Required correction** Provide the DeepLoc classification thresholds and discuss whether the difference is biologically meaningful.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Section 3
- **Evidence pointer** Section 3
- **Issue** The discussion introduces the concept of "favorable electrostatic interaction between positively charged Arg and the negatively charged P-Ser202/205" but does not explain how this interaction was modeled or quantified.
- **Required correction** Provide details on the electrostatic calculations or clearly state this is a qualitative hypothesis.

- **Concern ID** R1-m6
- **Severity** Minor
- **Axis** Reproducibility
- **Affected element** Section 5.2
- **Evidence pointer** Section 5.2
- **Issue** The methods state that structures were visualized using "PYMOL Chimera software Version 1.7.4," which appears to conflate two separate software packages (PyMOL and Chimera). The specific software used for each step is unclear.
- **Required correction** Clarify which software was used for which step and provide correct version numbers.

## Risk / unsupported claims
- The claim that the RG>KR mutation "expands the ability for differential expression of the N protein epitope on MHC" is unsupported by experimental evidence and relies entirely on computational predictions.
- The claim that HLA-A*68:01 allele frequencies "could positively correlate with the severity of coronavirus cases and a high number of deaths" is an unsupported extrapolation from in silico epitope predictions to population-level outcomes.
- The claim that "low HLA-A*68:01 expression could correlate with the low number of COVID-19-attributable deaths seen in Japan" is anecdotal and not supported by any epidemiological analysis.
- The structural claims regarding "enhanced structural flexibility" and "decreased conformational entropy" are not supported by the evidence presented, as no dynamics simulations or experimental structural data are provided.
- The claim that the mutant N protein is "predominantly found in the nucleus" based on DeepLoc predictions is not validated experimentally and the difference between wild type and mutant is not contextualized.
- The overall conclusion that the mutations "affected the viral structure, function, and immunogenicity" is not established, as the evidence is entirely computational and lacks validation.