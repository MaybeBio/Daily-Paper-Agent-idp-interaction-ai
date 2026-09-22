## Review setup
- **Input scope** Full manuscript text (abstract, introduction, results, discussion, methods) without figures or supplementary material
- **Assessment boundary** Scientific claims, methodological soundness, and interpretation as presented in the text; figure content assessed only through textual descriptions
- **Shared manuscript claim summary** The authors propose that the intrinsically disordered C-terminal region (C-IDR) of the pioneer transcription factor Sox2 engages in dynamic electrostatic interactions with the folded DNA-binding domain (DBD), and that DNA or nucleosome binding redistributes the conformational ensemble of the C-IDR, altering the accessibility of two activation domains (AD1 and AD2) in a manner that may be functionally relevant for transcriptional regulation.
- **Visible evidence base** Single-molecule FRET (smFRET) with transfer efficiency histograms and fluorescence lifetime analysis; NMR spectroscopy including chemical shift assignments, CSPs, and relaxation measurements; far-UV circular dichroism; coarse-grained Langevin dynamics simulations with FRET-derived validation; binding affinity measurements
- **Missing materials affecting confidence** Figures and supplementary figures are referenced but not provided; supplementary tables, movies, and source data are not available; specific labelling positions and dye attachment details are only partially described; simulation validation statistics beyond concordance correlation coefficient are not shown

## Reviewer
- **Overall assessment** This manuscript presents a technically sophisticated integration of smFRET, NMR, and coarse-grained simulations to address a significant question in transcription factor biology: how DNA binding modulates the conformational ensemble of an intrinsically disordered activation domain. The combination of experimental and computational approaches is commendable, and the observation that DNA binding redistributes interdomain interactions and activation domain accessibility is potentially important. However, the manuscript as presented has several concerns that need to be addressed. The claim that DNA binding "redistributes" the ensemble is supported by FRET and CSP data, but the functional implications remain speculative. The simulation approach, while reasonable, relies on a single tuned parameter and the validation is presented with limited statistical depth. The relationship between the observed conformational changes and transcriptional function is not directly tested, which limits the strength of the conclusions. The writing is generally clear, though some methodological details require clarification.

- **Who would be interested in the results, and why** Researchers studying transcription factor mechanisms, particularly pioneer factors and their intrinsically disordered regions; structural biologists interested in IDR conformational ensembles; computational biologists developing coarse-grained models of protein-DNA complexes; and investigators interested in the role of electrostatic interactions in modulating IDR conformations. The work provides a methodological template for integrating multiple biophysical techniques to study IDR behavior in the context of DNA binding.

- **Major strengths**
  1. The integration of multiple orthogonal techniques (smFRET, NMR, CD, simulations) to study a full-length transcription factor with its IDR is a significant technical achievement.
  2. The use of 22 unique FRET pairs to validate the coarse-grained simulations provides a robust experimental constraint.
  3. The observation that DNA binding does not simply release the C-IDR from the DBD but rather creates a different ensemble is a nuanced and interesting finding.
  4. The salt sensitivity of the interdomain interactions in the physiologically relevant range is a notable observation with potential functional implications.
  5. The work addresses a gap in the field by providing a structural ensemble model for a full-length TF, which is rarely attempted.

- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Functional significance
- **Claim pointer** The abstract and discussion state that DNA binding "redistributes" the ensemble and accessibility of activation domains, implying functional relevance for transcriptional regulation.
- **Evidence pointer** Abstract; Discussion section; Results section "DNA and nucleosome binding expands dimensions of C-IDR"
- **Concern** The manuscript demonstrates conformational changes in the C-IDR upon DNA binding but does not provide direct evidence that these changes affect transcriptional activity, cofactor recruitment, or any functional output. The term "accessibility" is used as a proxy based on contact patterns and relaxation times, but no functional assay (e.g., transcriptional activation assays, coactivator binding measurements) is presented to link the observed conformational redistribution to biological function.
- **Why it matters** The title and framing of the manuscript suggest that the conformational changes are functionally important for Sox2's role as a pioneer factor. Without functional validation, the significance of the observed ensemble redistribution remains correlative. The claim of "accessibility" is inferred from simulations rather than directly measured.
- **Resolution test** Provide experimental evidence linking the conformational changes to function, such as mutations that disrupt the interdomain interactions and measurement of transcriptional activity, or coactivator binding assays in the presence and absence of DNA. Alternatively, temper the claims to be explicitly descriptive of conformational changes without asserting functional consequences.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Simulation validation
- **Claim pointer** The coarse-grained simulations are stated to "reproduce" the FRET efficiencies with a concordance correlation coefficient of 0.92, and the resulting ensembles are used to draw conclusions about contact redistribution and activation domain accessibility.
- **Evidence point** Results section "Coarse-grained simulation reveals redistributed accessibility of activation domains"; Methods section "Langevin dynamics simulations"
- **Concern** The simulation validation relies on a single concordance correlation coefficient (ρc = 0.92) across 11 FRET pairs per condition. The manuscript does not report uncertainty estimates, error bars on the simulated ensembles, or sensitivity analyses. The tuning of a single parameter (εpp) to match experimental data may lead to overfitting, and the manuscript does not demonstrate that the model can predict behaviors beyond the fitted data. Additionally, the use of the same starting structure for free and DNA-bound Sox2 (from the nucleosome complex) may bias the free-state simulations.
- **Why it matters** The conclusions about ensemble redistribution and differential activation domain accessibility are derived from the simulations. If the model is not robustly validated or is sensitive to parameter choices, these conclusions may not be reliable. The lack of uncertainty quantification undermines confidence in the quantitative claims.
- **Resolution test** Provide additional validation metrics, such as cross-validation (e.g., fitting to a subset of FRET pairs and predicting the rest), uncertainty estimates on simulated ensembles (e.g., block averaging or multiple independent runs), and a sensitivity analysis showing how conclusions change with εpp values. Justify the use of the nucleosome-bound structure for free-state simulations or demonstrate that results are insensitive to this choice.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Interpretation of NMR CSPs
- **Claim pointer** The manuscript states that "most of the CSPs localise to the regions we had previously observed to make contacts with the DBD" and that the chemical shifts "imply a different structural ensemble" for the C-IDR in the DNA-bound state.
- **Evidence point** Results section "DNA and nucleosome binding expands dimensions of C-IDR"; Figure 3h
- **Concern** The CSP analysis is used to support the claim of a different ensemble, but the manuscript does not provide a quantitative interpretation of the CSP magnitudes. It is unclear whether the observed CSPs are large enough to indicate significant conformational changes or could arise from minor local perturbations. Additionally, the CSPs are compared to the free C-IDR construct, but the appropriate comparison for understanding the effect of DNA binding on the full-length protein may be different.
- **Why it matters** The NMR data are a key experimental pillar supporting the ensemble redistribution claim. Without a clear threshold or quantitative framework for interpreting CSPs, the strength of this evidence is unclear.
- **Resolution test** Provide a quantitative analysis of CSPs, such as comparing them to a significance threshold (e.g., based on spectral noise), or use CSPs to derive structural restraints in the simulations. Clarify the appropriate reference state for CSP interpretation.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Generalizability
- **Claim pointer** The discussion states that "this type of charge-driven IDR ensemble modulation is likely to be common among eukaryotic TFs."
- **Evidence point** Discussion section
- **Concern** The claim of generalizability is based on a single transcription factor. While the authors note shared sequence features, no bioinformatic analysis or experimental evidence from other TFs is presented to support this extrapolation. The discussion of other TFs (B-MYB, p53, MYC/MAX) is anecdotal and does not establish a systematic pattern.
- **Why it matters** The broader significance of the work depends on whether the observed phenomenon is general. Without evidence for generalizability, the claim remains speculative.
- **Resolution test** Provide a bioinformatic analysis of charge distributions across TF families to support the claim, or temper the statement to be more clearly speculative.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Methodological clarity
- **Affected element** FRET labelling positions
- **Evidence point** Methods section "Protein labelling"; Results section "Coarse-grained simulation reveals redistributed accessibility of activation domains"
- **Issue** The manuscript does not clearly specify how the 11 FRET labelling positions were chosen and whether they cover the entire C-IDR or are concentrated in specific regions. The positions are described in Figure 4a, but the figure is not provided.
- **Required correction** Provide a table or explicit list of labelling positions with residue numbers and a rationale for their selection, ensuring coverage of the full C-IDR.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Statistical reporting
- **Affected element** Binding affinity measurements
- **Evidence point** Methods section "Binding affinity measurements"
- **Issue** The KD values are reported as mean ± SEM, but the number of independent replicates is not stated. The manuscript also does not specify whether the binding assays were performed in replicate on different days or with different protein preparations.
- **Required correction** State the number of independent replicates and the statistical methods used to determine the reported uncertainties.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Terminology
- **Affected element** "Accessibility" terminology
- **Evidence point** Title; Abstract; Discussion
- **Issue** The term "accessibility" is used to describe the exposure of activation domains, but it is not defined operationally. It is unclear whether this refers to solvent accessibility, availability for cofactor binding, or something else.
- **Required correction** Define "accessibility" in operational terms and specify how it is measured or inferred from the simulations and experiments.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Literature context
- **Affected element** Discussion of other TFs
- **Evidence point** Discussion section
- **Issue** The discussion of other TFs with similar interdomain interactions is brief and does not critically evaluate differences or similarities with the Sox2 system.
- **Required correction** Expand the discussion to more thoroughly compare and contrast the Sox2 findings with those from other systems, noting any discrepancies or unique features.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Data availability
- **Affected element** Simulation trajectories
- **Evidence point** Methods section "Langevin dynamics simulations"
- **Issue** The manuscript does not state whether simulation trajectories or analysis scripts will be made publicly available.
- **Required correction** Include a data availability statement specifying where simulation data and analysis code can be accessed.

- **Concern ID** R1-m6
- **Severity** Minor
- **Axis** Figure accessibility
- **Affected element** All figures
- **Evidence point** Throughout
- **Issue** The manuscript relies heavily on figures that are not provided in the review materials, making it difficult to fully assess the data quality and the strength of the visual evidence.
- **Required correction** Ensure that all figures are of high quality and clearly support the claims made in the text, with appropriate statistical annotations.

## Risk / unsupported claims
- The claim that DNA binding "redistributes activation domain ensemble and accessibility" is supported by the data but the functional significance is not established; the term "accessibility" is inferred rather than directly measured.
- The claim that "this type of charge-driven IDR ensemble modulation is likely to be common among eukaryotic TFs" is speculative and not supported by systematic evidence.
- The statement that the C-IDR "may be an evolved strategy to protect against unwanted interactions, premature degradation, aggregation, or condensate formation" is presented without direct evidence and should be clearly framed as speculation.
- The claim that phosphorylation events "might be expected to enhance the interaction with the positively charged DBD" is hypothetical and not tested in this work.
- The assertion that the structural model "will aid in rationalising the effects of PTMs" is forward-looking but not demonstrated.
- The statement that the ensemble "will also be generally populated on nucleosomes" is based on similar FRET values but the manuscript acknowledges differences in dynamics, making this claim somewhat uncertain.