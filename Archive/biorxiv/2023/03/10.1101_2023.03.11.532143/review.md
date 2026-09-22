## Review setup

- **Input scope** Full manuscript text, including abstract, main text, methods, and supplementary figure references. No supplementary files were provided.
- **Assessment boundary** The scientific claims, experimental design, data interpretation, and internal consistency of the presented work, as described in the manuscript.
- **Shared manuscript claim summary** The authors propose that a significant fraction of antimicrobial peptides (AMPs) have an intrinsic propensity to undergo liquid-liquid phase separation (LLPS) with nucleic acids, and that this activity constitutes a previously unrecognized mechanism of antimicrobial action. They support this with computational predictions, in vitro biophysical assays, and cell-based imaging.
- **Visible evidence base** Main text figures (Fig. 1-6), supplementary figure references (Fig. S1-S24), methods section, and supplementary movie references (Movies S1-3). No raw data, code, or supplementary files were available for review.
- **Missing materials affecting confidence** Supplementary figures (S1-S24), supplementary movies (S1-3), raw data files, analysis code, and detailed model parameters for the DeeLearn retraining. The absence of these materials limits the ability to fully verify the quantitative claims and the robustness of the computational analysis.

## Reviewer

- **Overall assessment** This manuscript presents a novel and potentially significant hypothesis regarding the mechanism of action of a subset of antimicrobial peptides. The authors combine computational predictions with a range of in vitro biophysical assays and cellular imaging to build a case for AMP-driven nucleic acid phase transitions as a new antimicrobial paradigm. The work is timely and will be of interest to the antimicrobial, phase separation, and biophysics communities. However, the current evidence base has several gaps that prevent the case from being fully established. The link between the in vitro phase separation propensity and the observed in vivo effects is largely correlative, and the specificity of the proposed mechanism is not sufficiently tested against alternative explanations. The lack of key methodological details and the absence of supplementary data further limit the strength of the claims.
- **Who would be interested in the results, and why** Researchers in the fields of antimicrobial peptide biology, bacterial cell biology, and biomolecular condensates. The work is also relevant to drug discovery efforts focused on novel antibiotic targets. The proposed mechanism offers a new lens through which to view AMP function, which could stimulate new research directions in both basic and translational science.
- **Major strengths**
    1.  The central hypothesis is novel and conceptually interesting, connecting the fields of AMP research and biomolecular phase separation.
    2.  The combination of computational screening, in vitro biophysics, and cellular imaging provides a multi-pronged approach to address the hypothesis.
    3.  The use of the PhaseScan platform to generate high-density phase diagrams is a powerful and appropriate technique for this type of analysis.
    4.  The study identifies a clear correlation between the predicted and experimentally measured phase separation propensity of the selected AMPs.
- **Major Concerns**

    - **Concern ID** R1-M1
    - **Severity** Major
    - **Blocking** Yes
    - **Axis** Experimental Design and Controls
    - **Claim pointer** The authors claim that the AMP-induced inhibition of transcription and translation in vitro is due to the sequestration of nucleic acids via phase separation.
    - **Evidence pointer** Figure 5, Figure S14-S16, "In vitro transcription and translation experiments" section.
    - **Concern** The cell-free expression assays demonstrate that AMPs inhibit protein production, but the causal link to phase separation is not established. The authors argue that since reaction rates are unaffected, the mechanism is a reduction in effective nucleic acid concentration. However, this is also consistent with a simple, non-specific electrostatic binding of the AMPs to the nucleic acid templates, which would block polymerase or ribosome processivity without necessarily forming visible condensates. The manuscript lacks a critical control where an AMP with high phase separation propensity but a mutated, non-condensing variant is tested in the same assay. Furthermore, the claim that the effect is due to phase separation is not directly tested by, for example, adding a known phase-separation disruptor to the reaction and observing a rescue of expression.
    - **Why it matters** This is the central mechanistic claim of the paper. Without directly linking the observed functional inhibition to the physical process of phase separation, the proposed mechanism remains one of several possible explanations for the observed data. The current data cannot distinguish between a general "nucleic acid binder" model and a specific "phase transition modulator" model.
    - **Resolution test** To resolve this, the authors should perform cell-free expression assays with a control peptide that binds nucleic acids but is computationally and experimentally shown to have a low phase separation propensity. Alternatively, they could attempt to rescue the inhibition by adding a molecular crowder or a specific peptide that disrupts the condensate, or by using a mutant nucleic acid that is resistant to condensation. Direct visualization of condensates in the cell-free reaction mixture would also strengthen the link.

    - **Concern ID** R1-M2
    - **Severity** Major
    - **Blocking** Yes
    - **Axis** Specificity and In Vivo Relevance
    - **Claim pointer** The authors claim that the formation of AMP-nucleic acid foci in bacteria supports the model that phase separation is a mechanism of action.
    - **Evidence pointer** Figure 6, Figures S17-S24, "Cell imaging" section.
    - **Concern** The imaging data show that AMPs and nucleic acids colocalize in foci, but this is a static observation. It does not demonstrate that these foci are liquid-like condensates, nor does it prove that their formation is the cause of cell death. The foci could be aggregates, membrane vesicles, or other types of inclusion bodies. The authors do not perform any in vivo FRAP or other rheological tests to confirm the liquid-like nature of these structures. More importantly, the manuscript does not demonstrate that the formation of these foci is required for antimicrobial activity. A mutant AMP that cannot form foci but retains membrane activity would be a critical control. The authors also do not address the possibility that the observed foci are a consequence of cell death, rather than the cause.
    - **Why it matters** The in vivo relevance of the proposed mechanism is a key part of the paper's significance. The current evidence is purely correlative and does not establish a causal or mechanistic link between the observed foci and the antimicrobial effect. The claim that this is a "mechanism of action" is therefore overstated.
    - **Resolution test** To strengthen this claim, the authors should perform time-lapse microscopy to show that foci formation precedes cell death. They should also attempt to characterize the physical state of the foci in vivo (e.g., using FRAP). Most critically, they need to demonstrate that the ability to form these foci is genetically or pharmacologically separable from the antimicrobial effect.

    - **Concern ID** R1-M3
    - **Severity** Major
    - **Blocking** No
    - **Axis** Computational Analysis and Data Availability
    - **Claim pointer** The authors claim that a significant fraction of AMPs are predicted to undergo phase separation, and that this propensity is linked to their antimicrobial activity.
    - **Evidence pointer** Figure 1, Figures S1-S2, "Antimicrobial peptide sequence analysis via DeeLearn LLPS predictor" section.
    - **Concern** The manuscript relies heavily on a retrained DeeLearn model, but the details of this retraining are insufficient. The methods state that the model was retrained on a dataset of proteins that partition into RNA-rich condensates, but the size, composition, and source of this dataset are not described. The performance of the retrained model (e.g., AUC, precision-recall) is not reported. Without this information, it is impossible to assess the validity of the computational predictions. Furthermore, the claim that the phase separation propensity is "linked" to antimicrobial activity is based on a comparison of a small number of selected AMPs, which is not a robust statistical test.
    - **Why it matters** The computational analysis is the foundation of the paper, as it motivates the entire study. If the model is poorly trained or its predictions are not well-calibrated, the subsequent experimental work is built on a weak foundation. The lack of model details and performance metrics prevents the reader from evaluating the reliability of the core predictions.
    - **Resolution test** The authors must provide a full description of the training dataset, the model architecture, and the training procedure. They should report the model's performance on a held-out test set. To support the link between phase separation propensity and antimicrobial activity, they should perform a statistical analysis on a larger, unbiased set of AMPs with known antimicrobial activity, rather than just the three selected for this study.

- **Minor Comments**

    - **Concern ID** R1-m1
    - **Severity** Minor
    - **Axis** Clarity and Presentation
    - **Affected element** Figure 2d and related text
    - **Evidence pointer** Figure 2d, "Results and Discussion" section.
    - **Issue** The text states that 1,6-hexanediol had no effect on condensates, but the figure is not shown in the provided text. The authors should clarify the concentration of 1,6-hexanediol used and whether a positive control was performed to show that the reagent was active.
    - **Required correction** Please provide the data for Figure 2d and specify the concentration of 1,6-hexanediol used. Include a positive control to demonstrate the efficacy of the reagent in disrupting hydrophobic interactions.

    - **Concern ID** R1-m2
    - **Severity** Minor
    - **Axis** Data Presentation
    - **Affected element** Figure 4c and related text
    - **Evidence pointer** Figure 4c, "Condensate-forming AMPs compact structured structured RNA" section.
    - **Issue** The MDS data show a decrease in hydrodynamic radius, which is interpreted as compaction. However, the authors should also report the polydispersity of the samples. A broad distribution could indicate aggregation rather than a uniform compaction event.
    - **Required correction** Report the polydispersity index or show the full size distribution for the MDS data.

    - **Concern ID** R1-m3
    - **Severity** Minor
    - **Axis** Terminology
    - **Affected element** Title and Abstract
    - **Evidence pointer** Title, Abstract.
    - **Issue** The title and abstract use the term "Mechanism of Action," which is a strong claim. Given the correlative nature of the in vivo data, a more cautious term such as "Potential Mechanism" or "A Contributing Mechanism" might be more appropriate.
    - **Required correction** Consider revising the title and abstract to reflect the level of evidence presented, e.g., "Modulating Nucleic Acid Phase Transitions as a Potential Mechanism of Action for Cell-Penetrating Antimicrobial Peptides."

    - **Concern ID** R1-m4
    - **Severity** Minor
    - **Axis** Internal Consistency
    - **Affected element** Section heading
    - **Evidence pointer** "Condensate-forming AMPs compact structured structured RNA" section.
    - **Issue** There is a typo in the section heading: "structured structured RNA" should be "structured RNA".
    - **Required correction** Correct the typo in the section heading.

- **Assessment against Nature-style criteria**
    - **Originality** High. The concept of AMPs acting via phase transition modulation is a novel and creative hypothesis that has not been previously proposed in this context.
    - **Scientific importance** Potentially high. If the mechanism is confirmed, it would represent a paradigm shift in the understanding of how a class of antimicrobials functions and would open new avenues for drug discovery.
    - **Interdisciplinary readership** High. The work bridges the fields of microbiology, biophysics, and computational biology, and would be of interest to a broad readership across these disciplines.
    - **Technical soundness** The in vitro biophysical techniques (PhaseScan, MDS, FRAP) are state-of-the-art and well-suited for the study of phase separation. However, the technical soundness of the computational analysis is currently unverifiable due to missing methodological details. The lack of critical controls in the functional assays is a significant weakness.
    - **Readability for nonspecialists** The manuscript is generally well-written and the concepts are explained clearly. The abstract and introduction are accessible. However, the methods section is dense and would be challenging for a non-specialist to follow.

- **Recommendation posture** Currently not established from the provided evidence. The central hypothesis is intriguing and the initial data are promising, but the lack of direct causal evidence linking phase separation to the observed functional inhibition, the absence of key controls, and the incomplete description of the computational methods prevent the case from being made convincingly. The manuscript would be suitable for reconsideration after major revisions that address the blocking concerns.

## Risk / unsupported claims

- The claim that AMP-induced inhibition of transcription/translation is *caused by* phase separation is unsupported. The data are consistent with this model but do not exclude other mechanisms of nucleic acid binding and sequestration.
- The claim that the foci observed in bacteria are liquid-like condensates is unsupported. No in vivo physical characterization was performed.
- The claim that the formation of these foci is a *mechanism of action* for antimicrobial activity is unsupported. The causal link between foci formation and cell death is not established.
- The claim that a "significant fraction" of AMPs have high phase separation propensity is unverifiable without details on the retrained DeeLearn model's performance and the statistical significance of the analysis.
- The claim that the phase separation propensity is "linked" to antimicrobial activity is based on a very small sample size (n=3) and is not a robust statistical claim.