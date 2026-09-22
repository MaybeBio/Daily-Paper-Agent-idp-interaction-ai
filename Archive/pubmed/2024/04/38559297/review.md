## Review setup
- **Input scope** Full manuscript text including abstract, introduction, results and discussion, conclusions, and supplementary material references.
- **Assessment boundary** Scientific content, methodology, data interpretation, and claims as presented in the provided manuscript text. No external validation of experimental procedures or data was performed.
- **Shared manuscript claim summary** The authors propose that molecular shape, not just chemical composition, is a key determinant of aggregation inhibitor efficacy for intrinsically disordered tau protein. They designed four isatin-pyrrolidinylpyridine isomers (IPP1–IPP4) with identical functional groups but different spatial arrangements, and report that IPP1 uniquely inhibits tau aggregation in vitro, in cells, and in a 3xTg mouse model, attributed to its "molecular clip" binding mode.
- **Visible evidence base** Abstract, Introduction, Results and Discussion sections covering synthesis, DFT calculations, MST binding assays, ThS fluorescence aggregation assays, TEM imaging, CD spectroscopy, molecular docking, MD simulations with MM-PBSA analysis, cell viability assays, immunofluorescence staining, Western blotting, and a preliminary mouse study. Figures 1–9 and Tables 1 and S1 are referenced. Supplementary Figures S1–S17 are mentioned.
- **Missing materials affecting confidence** Full experimental methods section, detailed synthesis procedures, raw data files, statistical analysis details, figure quality and full legends, supplementary figures S1–S17 content, and complete animal study protocols are not available in the provided text. The manuscript appears to be a preprint or accepted version without full methods.

## Reviewer
- **Overall assessment** The manuscript addresses an important and underexplored question in tau aggregation inhibitor design: the role of molecular shape in inhibitor efficacy for intrinsically disordered proteins. The use of isomeric compounds to isolate shape effects is a clever and potentially impactful approach. However, the evidence presented is largely correlative, and several key claims, particularly the proposed "molecular clip" mechanism and the in vivo efficacy, are not fully supported by the data shown. The manuscript would benefit from stronger quantitative analysis, clearer mechanistic evidence, and more rigorous statistical treatment.
- **Who would be interested in the results, and why** Researchers in the fields of Alzheimer's disease drug discovery, protein aggregation, intrinsically disordered proteins, and medicinal chemistry. The concept of shape-based inhibitor design for disordered targets could have broad implications for other protein misfolding diseases and for the general understanding of ligand–IDP interactions.
- **Major strengths** 1. The study design using isomers to isolate molecular shape as a variable is elegant and addresses a gap in the field. 2. The multi-level validation from in vitro to cellular to animal models is commendable. 3. The combination of experimental and computational approaches provides a comprehensive picture. 4. The identification of a specific binding mode ("molecular clip") offers a testable hypothesis for future work.
- **Major Concerns**
  - **Concern ID** R1-M1
  - **Severity** Major
  - **Blocking** Yes
  - **Axis** Mechanistic evidence
  - **Claim pointer** The claim that IPP1 acts as a "molecular clip" that binds and fixes the tau polypeptide chain at a multipoint to prevent conformational transition before nucleation.
  - **Evidence pointer** Figures 5 and 6, Table 1, and related text in the docking and MD sections.
  - **Concern** The "molecular clip" mechanism is inferred primarily from docking poses and MD simulations. The docking results are acknowledged by the authors as limited, and the MD simulations, while more robust, still rely on a single starting conformation and a relatively short timescale. The experimental evidence (CD, ThS, TEM) shows that IPP1 inhibits aggregation but does not directly demonstrate the proposed multipoint binding or the prevention of conformational transition. The claim that IPP1 induces an "aggregation noncompetent conformation" is speculative and not directly measured.
  - **Why it matters** The proposed mechanism is the central novel contribution of the paper. Without direct experimental evidence for the multipoint binding and conformational fixation, the mechanism remains a hypothesis rather than an established finding. This weakens the paper's impact and its ability to guide future inhibitor design.
  - **Resolution test** Provide experimental evidence for the binding mode, such as NMR chemical shift perturbation or hydrogen-deuterium exchange mass spectrometry, to map the interaction interface. Alternatively, use single-molecule FRET or other conformational probes to directly demonstrate that IPP1 locks tau in a non-aggregation-competent conformation.
  - **Concern ID** R1-M2
  - **Severity** Major
  - **Blocking** Yes
  - **Axis** In vivo data robustness
  - **Claim pointer** The claim that IPP1 reduces total tau levels in the hippocampus of 3xTg mice, confirming its effectiveness at the animal level.
  - **Evidence pointer** Figure 9 and related text in the animal study section.
  - **Concern** The animal study is severely underpowered (n = 3 per group), lacks behavioral or functional readouts, and only shows a single immunohistochemistry result. No statistical analysis is presented. The route of administration (intracerebroventricular injection) is invasive and not a clinically relevant dosing paradigm. The claim of "effectiveness" at the animal level is premature given the limited data.
  - **Why it matters** In vivo efficacy is a critical step in drug development, and overstating results from a small, preliminary study could mislead the field. The current data are insufficient to support the strong claim made in the abstract and conclusions.
  - **Resolution test** Increase group sizes, include a positive control, provide quantitative analysis of tau levels with appropriate statistics, and ideally include behavioral assessments or additional biochemical markers. If the study is intended as a pilot, the claims should be tempered accordingly.
  - **Concern ID** R1-M3
  - **Severity** Major
  - **Blocking** No
  - **Axis** Quantitative analysis
  - **Claim pointer** The claim that IPP1 has a significantly lower IC50 (3.2 μM) compared to previously reported inhibitors (cyanidin, tannic acid, curcumin).
  - **Evidence pointer** Figure 3B,C and related text.
  - **Concern** The IC50 comparison is made across different studies with potentially different experimental conditions (e.g., tau isoform, aggregation inducer, buffer, incubation time). A direct head-to-head comparison under identical conditions is needed to support the claim of superior potency. Additionally, the dose-response curve and IC50 calculation are not described in sufficient detail.
  - **Why it matters** The claim of superior potency is a key selling point for IPP1 as a lead compound. Without a controlled comparison, this claim is not rigorously established.
  - **Resolution test** Perform a direct comparison of IPP1 with at least one or two known inhibitors under identical assay conditions. Provide full details of the IC50 calculation, including the model used and error estimates.
- **Minor Comments**
  - **Concern ID** R1-m1
  - **Severity** Minor
  - **Axis** Clarity
  - **Affected element** Figure 3D description
  - **Evidence pointer** Figure 3D and related text
  - **Issue** The description of the CD spectra is somewhat ambiguous. The text states that the CD spectrum of R3 aggregates "did not exhibit a characteristic peak typical for a single conformational structure," but then describes a mixture of β-sheet/β-turn and α-helix. This is confusing.
  - **Required correction** Clarify the interpretation of the CD spectra, possibly by deconvoluting the spectra or providing reference spectra for pure conformations.
  - **Concern ID** R1-m2
  - **Severity** Minor
  - **Axis** Statistical reporting
  - **Affected element** All quantitative data
  - **Evidence pointer** Figures 2, 3, 4, 7, 8
  - **Issue** Error bars and statistical significance are not consistently reported across figures. For example, the MST data in Figure 2 and the cell viability data in Figure 7 lack clear statistical treatment.
  - **Required correction** Add error bars and statistical tests (e.g., t-tests or ANOVA) to all quantitative comparisons, and state the number of replicates in figure legends.
  - **Concern ID** R1-m3
  - **Severity** Minor
  - **Axis** Terminology
  - **Affected element** "Molecular transformers"
  - **Evidence pointer** Introduction and Results sections
  - **Issue** The term "molecular transformers" is used metaphorically but is not defined or standard in the field. It may confuse readers.
  - **Required correction** Define the term clearly or replace with more standard terminology such as "shape isomers" or "regioisomers."
  - **Concern ID** R1-m4
  - **Severity** Minor
  - **Axis** Completeness
  - **Affected element** Methods
  - **Evidence pointer** Entire manuscript
  - **Issue** The manuscript lacks a detailed Methods section. Key experimental parameters (e.g., MD simulation details, force fields, cell culture conditions, animal ethics) are not provided.
  - **Required correction** Add a comprehensive Methods section or refer to the Supporting Information for full experimental details.
- **Technical failings that need to be addressed before the case is established** 1. Lack of direct experimental evidence for the proposed "molecular clip" binding mode (R1-M1). 2. Insufficient in vivo data to support claims of animal-level efficacy (R1-M2). 3. Uncontrolled comparison of IC50 values across different studies (R1-M3). 4. Missing statistical analysis and error reporting across multiple figures (R1-m2). 5. Absence of a detailed Methods section (R1-m4).
- **Assessment against Nature-style criteria**  
  *Originality*: The concept of using isomeric compounds to probe the role of molecular shape in IDP aggregation inhibition is original and addresses a gap in the field. However, the idea that shape matters for ligand–IDP interactions is not entirely new, and the paper's novelty lies more in the specific demonstration than in the general concept.  
  *Scientific importance*: The work has the potential to influence how researchers approach inhibitor design for tau and other IDPs. If the mechanism is rigorously established, it could lead to new screening strategies. However, the current evidence is not yet strong enough to fully realize this impact.  
  *Interdisciplinary readership*: The topic bridges medicinal chemistry, biophysics, and neuroscience, and the findings would be of interest to a broad audience. The writing is generally accessible, though some computational details may be challenging for non-specialists.  
  *Technical soundness*: The experimental design is generally sound, but the lack of direct mechanistic evidence, the underpowered animal study, and the uncontrolled IC50 comparison are significant weaknesses. The computational methods are appropriate but would benefit from more rigorous validation.  
  *Readability for nonspecialists*: The manuscript is well-written and the "molecular clip" metaphor is helpful, but the lack of a Methods section and some ambiguous figure descriptions may hinder comprehension.
- **Recommendation posture** Supportive if technical concerns are resolved. The core idea is promising and the multi-level approach is commendable, but the current evidence does not fully establish the proposed mechanism or the in vivo efficacy. The manuscript would be significantly strengthened by addressing the major concerns outlined above.