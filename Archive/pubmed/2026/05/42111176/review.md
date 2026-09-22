## Review setup
- **Input scope** Full manuscript text, including abstract, introduction, results, discussion, methods, and figure/table legends.
- **Assessment boundary** Scientific validity, technical soundness, and significance of the claims as presented in the provided manuscript. No assessment of editorial fit or publication policy.
- **Shared manuscript claim summary** The authors report that the standard AlphaFold (AF) pipeline fails to produce credible structural models for the complex between the ALS-associated dipeptide repeat protein GR20 and the stress granule protein G3BP1, despite experimental evidence of high-affinity binding. They employ a constraint-based extension of AlphaFold, termed AFEX, to generate a complex model with improved confidence metrics and structural plausibility, supported by molecular dynamics simulations. The authors argue this demonstrates a fundamental limitation of AF for disordered complexes and advocates for integrative, knowledge-guided approaches.
- **Visible evidence base** BLI binding curves (Figure 1B, 3A-D), LLPS assays (Figure 1C, 3E), AF prediction metrics and structures (Figure 2, Table 1, Figure S1), AFEX model and MD simulation analyses (Figure 4, Figure S3, S4), and comparison with Boltz-2 (Figure S5).
- **Missing materials affecting confidence** The manuscript does not provide the AFEX code or detailed input parameters used for the AFEX runs beyond a brief description in the Methods. The specific sequences of GR20 and PR20 peptides are not given in the main text. The criteria for selecting the "best" AF model for AFEX initialization are not fully detailed. The statistical analysis of BLI data (e.g., number of replicates, error bars) is not described in the figure legends or methods. The MD simulation setup (e.g., force field parameters, water model details, equilibration protocol) is only partially described.

## Reviewer

- **Overall assessment** This manuscript addresses a timely and important problem: the limitations of AlphaFold in modeling protein complexes involving intrinsically disordered regions (IDRs). The authors present a clear case study using the G3BP1-GR20 interaction, which is biologically relevant to ALS. The experimental data (BLI, LLPS) are solid and establish the biochemical interaction. The failure of standard AF is convincingly demonstrated. However, the central claim regarding the AFEX-generated model is weakened by a lack of rigorous validation. The model is presented as "improved" based on confidence scores and MD stability, but the authors themselves acknowledge it is not a definitive structure. The key question of whether the AFEX model is *correct* or merely *plausible* is not addressed. The study is a useful demonstration of a workflow, but the scientific insight derived from the specific model is limited. The manuscript would be significantly strengthened by experimental validation of the predicted interface (e.g., mutagenesis of predicted contact residues) or by a more quantitative comparison of the AFEX model's features against known biophysical data.

- **Who would be interested in the results, and why** Computational biologists and structural biologists working on protein-protein interactions, particularly those involving IDRs. Researchers studying stress granules, liquid-liquid phase separation, and the molecular mechanisms of C9-ALS/FTD will find the biological context relevant. Developers and users of AI-based structure prediction tools will be interested in the documented failure mode and the proposed extension strategy. The work is also relevant to the broader community interested in the "invisible proteome" and the integration of computational and experimental methods.

- **Major Strengths**
    1.  The study addresses a critical and well-recognized limitation of AlphaFold, using a biologically and pathologically relevant system.
    2.  The experimental characterization (BLI, LLPS) is straightforward and provides a clear "ground truth" for the interaction.
    3.  The systematic evaluation of standard AF protocols (v2.2, v2.3, v3) is a useful contribution, documenting their failure mode for this class of complexes.
    4.  The AFEX approach is a logical and potentially powerful extension of AF, and the manuscript provides a clear conceptual framework for it.
    5.  The inclusion of MD simulations to assess the stability of the predicted model is a good practice.

- **Major Concerns**

    - **Concern ID** R1-M1
    - **Severity** Major
    - **Blocking** Yes
    - **Axis** Technical soundness / Validation
    - **Claim pointer** The authors claim that the AFEX-generated model is an "improved model for the G3BP1-GR20 complex" with "improved confidence and structural plausibility" and that it provides "a testable hypothesis" for the binding mechanism.
    - **Evidence pointer** Figure 4, Table 1, Results section "AFEX yields improved model for the G3BP1-GR20 complex"
    - **Concern** The central claim of the paper rests on the validity of the AFEX model. However, the model is not validated against any independent experimental data. The "improvement" is only shown in terms of in-silico metrics (pLDDT, PAE, confidence score) and stability in MD simulations. These metrics are not a substitute for experimental validation. The authors state the model is a "testable hypothesis," but no test is provided. The model's prediction of specific contacts (e.g., between GR20 arginines and G3BP1 acidic residues) is eminently testable via mutagenesis, but this is not performed. Without such validation, the model remains a speculative computational construct, and the paper's main conclusion about the value of AFEX is not fully supported.
    - **Why it matters** The paper's primary contribution is claimed to be the generation of a useful model for a challenging complex. If the model is not validated, its utility is questionable. The reader is left wondering if the AFEX model is any more "correct" than the failed AF models, just with better-looking scores. The paper would be a much stronger contribution if it could demonstrate that the AFEX model correctly predicts the effect of mutations on binding or phase separation.
    - **Resolution test** The authors should provide experimental validation of the AFEX model. This could be achieved by: (1) mutating key residues predicted to be at the G3BP1-GR20 interface (e.g., the acidic residues in IDR1 and the arginines in GR20) and showing that these mutations disrupt binding in BLI assays and/or alter LLPS behavior; or (2) using cross-linking mass spectrometry or NMR chemical shift perturbation to test the predicted contacts. If experimental validation is not possible, the claims about the model's utility must be significantly toned down.

    - **Concern ID** R1-M2
    - **Severity** Major
    - **Blocking** No
    - **Axis** Technical soundness / Reproducibility
    - **Claim pointer** The authors state that "AFEX generated full-length G3BP1-GR20 complexes with significantly improved residue-wise pLDDT scores" and describe the method as a "constraint-based method."
    - **Evidence pointer** Methods section "AFEX loss function and CV selection", Figure 4
    - **Concern** The description of the AFEX method is insufficient for reproduction. The authors state that "Customized CVs were defined between IDR1 and GR20 and between IDR1 and IDR3" and provide a general loss function, but the specific implementation details are missing. How were the "attractive" and "repulsive" restraints defined in practice? What were the specific residues used for the distance calculations? The text mentions residues [174, 187, 167, 163, 154] and [477, 475, 493, 495, 501] for one restraint, but the logic for choosing these specific residues is not explained. The weight scheduling (wc from 1 to 0.1, wr from 0 to 1) is mentioned, but the exact schedule is not given. This level of detail is insufficient for another group to apply AFEX to their own system.
    - **Why it matters** A key part of the paper's value is the demonstration of a new method. If the method is not described in sufficient detail, it cannot be used by others, limiting its impact. The "empirically guided" selection of residues also raises concerns about reproducibility and potential bias.
    - **Resolution test** The authors should provide a complete, step-by-step description of the AFEX protocol, including all input parameters, the exact definition of the collective variables, the residue selection logic, and the weight scheduling. Ideally, the code should be made available in a more complete form than a "min" version, or a detailed tutorial should be provided.

    - **Concern ID** R1-M3
    - **Severity** Major
    - **Blocking** No
    - **Axis** Scientific importance / Interpretation
    - **Claim pointer** The authors state that "the NTF2L domain contributes to GR20 binding but is not the primary driver of direct interactions" and that binding is mediated by "contextual mechanisms involving direct electrostatic contact, structural positioning, and allosteric coupling with IDRs."
    - **Evidence pointer** Results section "NTF2L domain binds GR20 with mild affinity but is not the primary-binding site of G3BP1", Figure 3
    - **Concern** The conclusion that NTF2L is not the primary binding site is based on a comparison of binding affinities: full-length G3BP1 binds GR20 with a KD of 95.6 nM, while the isolated NTF2L domain binds with a KD of 336 nM. However, the authors do not identify the primary binding site. The AFEX model suggests a role for IDR1, but this is not experimentally tested. The statement about "allosteric coupling" is speculative and not supported by any direct evidence. The paper leaves the reader with a key question unanswered: where and how does GR20 primarily bind to G3BP1?
    - **Why it matters** The biological significance of the interaction is tied to understanding the mechanism by which GR20 disrupts G3BP1 function. Simply showing that NTF2L is not the main site, without identifying the main site, limits the mechanistic insight provided by the study.
    - **Resolution test** The authors should perform experiments to identify the primary binding site. This could involve testing the binding of GR20 to other G3BP1 constructs (e.g., IDR1 alone, or a construct lacking NTF2L but containing IDR1), or performing competition experiments. If the primary site is in IDR1, as the model suggests, this should be demonstrated experimentally.

- **Minor Comments**

    - **Concern ID** R1-m1
    - **Severity** Minor
    - **Axis** Clarity / Data presentation
    - **Affected element** Figure 1C and 3E
    - **Evidence pointer** Figure 1C, Figure 3E
    - **Issue** The LLPS assay images are qualitative. The authors state that GR20 modulates phase separation in a concentration-dependent manner, but the images alone do not clearly show a dose-response. It is difficult to assess the difference between "inhibition" at low concentrations and "promotion" at high concentrations from the representative images.
    - **Required correction** Quantify the LLPS data. For example, plot the number or total area of droplets per field of view as a function of GR20 concentration. This would provide a more rigorous and convincing demonstration of the concentration-dependent effect.

    - **Concern ID** R1-m2
    - **Severity** Minor
    - **Axis** Clarity / Data presentation
    - **Affected element** Figure 4C
    - **Evidence pointer** Figure 4C
    - **Issue** The RMSD plot shows the average RMSD over three independent MD simulations. However, the text states that the complex "exhibited large-scale fluctuations" and that the "structured NTF2L domain showed the lowest heavy-atom RMSD (7 Å)". An RMSD of 7 Å for a structured domain is quite high and suggests significant conformational change or instability. This is not discussed.
    - **Required correction** The authors should comment on the relatively high RMSD values for the structured domains. Is this expected for this system? Does it indicate that the model is not stable? A more detailed analysis of the MD trajectories (e.g., RMSF per residue, radius of gyration) would help interpret these results.

    - **Concern ID** R1-m3
    - **Severity** Minor
    - **Axis** Clarity / Data presentation
    - **Affected element** Table 1
    - **Evidence pointer** Table 1
    - **Issue** The table reports "Confidence" and "Ave pLDDT" scores for different models. The "Confidence" score is defined in the methods as 0.8 × ipTM + 0.2 × pTM, but this is not stated in the table legend. The table would be clearer if this definition was included.
    - **Required correction** Add a footnote to Table 1 defining the "Confidence" score.

    - **Concern ID** R1-m4
    - **Severity** Minor
    - **Axis** Clarity / Data presentation
    - **Affected element** Figure 2C and 2D
    - **Evidence pointer** Figure 2C, 2D
    - **Issue** The authors state that AF2.3 predicted a "well-structured NTF2L homodimer" and that GR20 "wrapped across the dimer interface". However, the figure is not very informative. The GR20 peptide is highlighted with a thicker coil, but it is difficult to see the details of the interaction.
    - **Required correction** Provide a zoomed-in view of the predicted interface, showing the specific residues involved in the interaction. This would help the reader evaluate the plausibility of the predicted binding mode.

- **Technical failings that need to be addressed before the case is established**
    - R1-M1: Lack of experimental validation of the central AFEX model prediction.
    - R1-M2: Insufficient methodological detail for the AFEX protocol to be reproduced.

- **Assessment against Nature-style criteria**
    - **Originality** The work is original in its specific application of a constraint-based AF extension to a challenging disordered complex. However, the general concept of using restraints or prior knowledge to guide AF is not new. The originality lies in the specific case study and the demonstration of AF's failure.
    - **Scientific importance** The work highlights a critical limitation of a widely used tool, which is important for the field. The biological system (G3BP1-GR20 in ALS) is of high interest. However, the lack of a validated structural model limits the immediate scientific impact. The paper is more of a "cautionary tale" and a "proof of concept" than a source of new biological or structural insight.
    - **Interdisciplinary readership** The topic is relevant to structural biology, computational biology, and neuroscience. The writing is generally accessible, but the methods section is quite technical. The paper could appeal to a broad readership interested in the applications and limitations of AI in biology.
    - **Technical soundness** The experimental biophysics (BLI, LLPS) appears sound. The computational work is technically competent but the central model is not validated, which is a major technical weakness. The lack of detail in the AFEX method is also a concern.
    - **Readability for nonspecialists** The abstract and introduction are clear. The results are presented logically. However, the discussion of AFEX and MD simulations may be challenging for readers without a strong computational background. The main message, that AF fails for this system and that integrative approaches are needed, is clear.

- **Recommendation posture** Currently not established from the provided evidence. The manuscript presents a well-executed experimental characterization of a biologically relevant interaction and clearly demonstrates the failure of standard AlphaFold. However, the central claim of the paper, that the AFEX model provides a useful and improved structural hypothesis, is not supported by experimental validation. The methodological description of AFEX is also insufficient for reproduction. The paper has potential, but it requires significant additional work, primarily in the form of experimental validation of the predicted model, before the case is established.