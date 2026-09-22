## Review setup
- **Input scope** Full manuscript text, including abstract, introduction, methods, results, conclusions, and supplementary figure descriptions as referenced in the text.
- **Assessment boundary** The review is limited to the scientific content, methodology, and claims presented in the provided manuscript. No external data, unpublished results, or experimental validation beyond what is described are considered.
- **Shared manuscript claim summary** The authors use all-atom molecular dynamics simulations and free energy perturbation calculations to characterize the binding between the secreted amyloid-β precursor protein (sAPP) peptides (APP 17-mer and APP 9-mer) and the intrinsically disordered sushi 1 domain of GABABR1a. They identify key residues (D4, W6, W7) responsible for binding, propose a stacking interaction between W6 and Y20, and report a double mutation (D1A + D2N) from vertebrate evolution that enhances binding affinity, suggesting a potential GABABR1a modulator.
- **Visible evidence base** The manuscript includes simulation methods, MD trajectory analyses (RMSD, contact probabilities, interaction energies), FEP results (Tables 1-3), and structural figures (Fig. 1-5) as described in the text. Supplementary figures (S1-S4) are referenced but not provided in the submitted material.
- **Missing materials affecting confidence** The NMR structure coordinates (PDB 6HKC) are referenced but not included. Supplementary figures and tables (S1-S4, ESI descriptions) are not provided. Experimental validation of the in silico predictions is absent. The exact simulation parameters for FEP (e.g., soft-core parameters, convergence criteria) are not fully detailed.

## Reviewer
- **Overall assessment** The manuscript presents a computational study that aims to elucidate the molecular mechanism of sAPP peptide binding to the GABABR1a sushi 1 domain. The work is timely and relevant given the recent experimental identification of this interaction. The use of MD and FEP is appropriate, and the identification of key residues is plausible. However, the study relies entirely on computational predictions without experimental validation, and several methodological details and statistical analyses are insufficiently reported. The claim of a "potentially enhanced GABABR1a modulator" is speculative and not supported by functional assays. The manuscript would benefit from stronger validation, clearer presentation of uncertainties, and a more cautious interpretation of the results.
- **Who would be interested in the results, and why** Researchers in the fields of Alzheimer's disease, GABAergic signaling, and neuropharmacology would be interested. The study provides a structural and mechanistic basis for sAPP-GABABR1a interaction, which could inform drug design targeting GABABR1a. Computational biophysicists studying protein-peptide interactions and intrinsically disordered proteins may also find the methodology and findings relevant.
- **Major strengths**
  1. The study addresses a novel and biologically important interaction with potential therapeutic implications.
  2. The combination of MD simulations and FEP calculations is a rigorous approach to study binding mechanisms at atomic resolution.
  3. The identification of specific residues (D4, W6, W7) and the proposed stacking interaction provide testable hypotheses.
  4. The exploration of evolutionary sequences to design enhanced binders is a creative and interesting approach.
- **Major Concerns**
  - **Concern ID** R1-M1
  - **Severity** Major
  - **Blocking** Yes
  - **Axis** Technical soundness
  - **Claim pointer** The authors claim that the APP 9-mer is sufficient to bind and stabilize the sushi 1 domain, and that specific mutations (W6A, W7A, D4A) significantly reduce binding affinity based on FEP calculations.
  - **Evidence pointer** Section "FEP in silico mutagenesis study", Table 1, Table 2, Table 3
  - **Concern** The FEP calculations are presented with mean values and standard deviations, but no statistical tests (e.g., t-tests, confidence intervals) are reported to assess the significance of the differences between wild-type and mutants. The convergence of the FEP calculations is not demonstrated (e.g., no plots of ΔΔG as a function of simulation time). The choice of 5 independent runs of 6 ns each may be insufficient for converged free energy estimates, especially for mutations involving large conformational changes. The soft-core potential parameters are not specified, which could affect the accuracy of the alchemical transformations.
  - **Why it matters** Without proper statistical analysis and convergence assessment, the reported ΔΔG values may not be reliable, and the conclusions about key residues and enhanced binding could be overinterpreted. This undermines the core claims of the study.
  - **Resolution test** The authors should provide convergence plots for all FEP calculations, report standard errors and confidence intervals, and perform statistical tests (e.g., bootstrap analysis) to confirm that the differences are significant. They should also detail the soft-core parameters and consider longer simulations or replica exchange methods to improve sampling.
  - **Concern ID** R1-M2
  - **Severity** Major
  - **Blocking** Yes
  - **Axis** Scientific importance
  - **Claim pointer** The authors claim that the double mutation D1A + D2N, based on APP_frog and APPb_fish sequences, shows stronger binding (ΔΔG = −1.91 ± 0.66 kcal mol−1) and could serve as a "potentially enhanced GABABR1a modulator."
  - **Evidence pointer** Section "Design novel peptides for enhanced binding", Table 2, Table 3, Figure 5
  - **Concern** The claim of an enhanced modulator is purely based on computational predictions of binding free energy changes. No experimental validation (e.g., binding assays, functional studies) is provided to support this claim. The biological relevance of the ΔΔG value (−1.91 kcal mol−1) is not discussed in terms of functional outcomes. The evolutionary rationale is speculative, as the authors do not demonstrate that the fish sequences actually bind GABABR1a in vivo.
  - **Why it matters** The translational significance of the study hinges on the potential for designing better modulators. Without experimental evidence, the claim remains unsubstantiated and could mislead future research efforts.
  - **Resolution test** The authors should either provide experimental validation (e.g., surface plasmon resonance, isothermal titration calorimetry, or cellular assays) or temper their conclusions to clearly state that the predictions require experimental confirmation.
  - **Concern ID** R1-M3
  - **Severity** Major
  - **Blocking** No
  - **Axis** Technical soundness
  - **Claim pointer** The authors state that the APP 17-mer is less stable than the APP 9-mer, with the first nine residues being stable and the remaining eight extending into solution.
  - **Evidence pointer** Section "Key residues for sAPP–GABABR1a binding", Figure 2
  - **Concern** The RMSD analysis for the APP 17-mer shows large fluctuations (0.22-0.89 nm), but the authors do not provide a detailed analysis of the conformational ensemble or the potential impact of the flexible C-terminal tail on the binding interface. The claim that the first nine residues are "as stable as the APP 9-mer" is based on visual inspection of RMSD plots, but no quantitative comparison (e.g., per-residue RMSF) is provided.
  - **Why it matters** Understanding the conformational dynamics of the APP 17-mer is important for interpreting its binding mode and for designing peptides that mimic its function. The lack of quantitative analysis weakens the mechanistic insights.
  - **Resolution test** The authors should provide per-residue root-mean-square fluctuation (RMSF) analysis and compare the stability of the first nine residues between the 17-mer and 9-mer quantitatively. They should also discuss the potential role of the flexible tail in binding or in solution.
  - **Concern ID** R1-M4
  - **Severity** Major
  - **Blocking** No
  - **Axis** Interdisciplinary readership
  - **Claim pointer** The authors claim that the binding of sAPP to GABABR1a "modulates synaptic transmission" and has implications for "GABABR1a-specific therapeutics."
  - **Evidence pointer** Abstract, Introduction, Conclusion
  - **Concern** The manuscript does not provide any functional or physiological context beyond citing the previous experimental study. The authors do not discuss how their computational findings relate to the known biology of GABABR1a or sAPP in synaptic transmission. The potential therapeutic implications are stated but not elaborated in terms of disease mechanisms or drug design strategies.
  - **Why it matters** For a broad readership, the significance of the findings needs to be contextualized within the larger biological and therapeutic landscape. The current presentation is too narrow and may not engage readers outside the computational biophysics community.
  - **Resolution test** The authors should expand the discussion to include the biological implications of their findings, such as how the identified binding residues could be targeted by small molecules or peptides, and how the enhanced binding mutant might affect synaptic function.
- **Minor Comments**
  - **Concern ID** R1-m1
  - **Severity** Minor
  - **Axis** Readability for nonspecialists
  - **Affected element** Abstract
  - **Evidence pointer** Abstract
  - **Issue** The abstract uses technical terms such as "intrinsically disordered sushi 1 domain" and "all-atom molecular dynamics simulations" without brief explanations, which may be inaccessible to readers unfamiliar with these concepts.
  - **Required correction** Provide brief definitions or context for these terms in the abstract to improve accessibility.
  - **Concern ID** R1-m2
  - **Severity** Minor
  - **Axis** Technical soundness
  - **Affected element** Methods section
  - **Evidence pointer** Section "Simulation methods"
  - **Issue** The methods section does not specify the force field parameters for the peptides and the sushi 1 domain, nor the water box dimensions and the number of atoms in each system. The equilibration protocol is described briefly, but details on temperature coupling and pressure control are missing.
  - **Required correction** Provide complete simulation details, including force field versions, system sizes, and coupling algorithms, to ensure reproducibility.
  - **Concern ID** R1-m3
  - **Severity** Minor
  - **Axis** Scientific importance
  - **Affected element** Discussion of evolutionary sequences
  - **Evidence pointer** Section "Design novel peptides for enhanced binding", Table 3
  - **Issue** The authors list sequences from different species but do not provide a phylogenetic context or discuss the functional significance of the sequence variations. The choice of species is not justified.
  - **Required correction** Add a brief discussion of the evolutionary conservation of the binding motif and the rationale for selecting the specific species.
  - **Concern ID** R1-m4
  - **Severity** Minor
  - **Axis** Readability for nonspecialists
  - **Affected element** Figure captions
  - **Evidence pointer** Figures 1-5
  - **Issue** The figure captions are descriptive but do not always explain the biological relevance of the data shown. For example, Figure 2C shows the binding interface but does not clearly state which residues are key and why.
  - **Required correction** Enhance figure captions to include a brief interpretation of the findings and their significance.
  - **Concern ID** R1-m5
  - **Severity** Minor
  - **Axis** Technical soundness
  - **Affected element** FEP decomposition
  - **Evidence pointer** Section "FEP in silico mutagenesis study", Table 1
  - **Issue** The free energy decomposition into electrostatic and van der Waals components is presented, but the method for this decomposition is not described in the methods section. It is unclear how the components were extracted from the FEP calculations.
  - **Required correction** Describe the decomposition method in the methods section, including any approximations or assumptions.
  - **Concern ID** R1-m6
  - **Severity** Minor
  - **Axis** Interdisciplinary readership
  - **Affected element** Conclusion
  - **Evidence pointer** Conclusion
  - **Issue** The conclusion states that the findings "might provide new targets for the development of GABABR1a isotype-specific therapies" but does not specify what these targets are or how they could be exploited.
  - **Required correction** Elaborate on the potential therapeutic targets and strategies, or remove the speculative statement if not supported.

## Technical failings that need to be addressed before the case is established
- R1-M1: Lack of statistical analysis and convergence assessment for FEP calculations.
- R1-M2: Absence of experimental validation for the predicted enhanced binding mutant.
- R1-M3: Insufficient quantitative analysis of conformational stability for the APP 17-mer.
- R1-m2: Incomplete simulation details in the methods section.
- R1-m5: Undescribed method for free energy decomposition.

## Risk / unsupported claims
- The claim that the double mutation D1A + D2N could serve as an "enhanced GABABR1a modulator" is unsupported without experimental validation.
- The statement that the APP 9-mer "is sufficient to bind GABABR1a and stabilize the sushi 1 domain" is based on simulations alone and lacks experimental confirmation.
- The assertion that the identified residues "provide new targets for the development of GABABR1a isotype-specific therapies" is speculative and not substantiated by functional data.
- The evolutionary interpretation of the fish sequences as "learned from evolution" is not rigorously justified.

## Assessment against Nature-style criteria
- **Originality** The study addresses a novel interaction and provides a computational mechanistic model. The approach of using evolutionary sequences to design enhanced binders is creative. However, the originality is somewhat limited by the reliance on a previously published experimental structure and the lack of new experimental data.
- **Scientific importance** The interaction between sAPP and GABABR1a is biologically significant, and understanding its molecular basis could have implications for Alzheimer's disease and other neurological disorders. However, the importance is diminished by the lack of experimental validation and the speculative therapeutic claims.
- **Interdisciplinary readership** The topic bridges structural biology, computational biophysics, and neuropharmacology, which could appeal to a broad audience. However, the presentation is heavily focused on computational details and may not be accessible to nonspecialists without additional context.
- **Technical soundness** The use of MD and FEP is appropriate, but the lack of statistical rigor, convergence analysis, and complete methodological details undermines the technical soundness. The study would benefit from more robust validation and transparency.
- **Readability for nonspecialists** The manuscript is generally well-written but uses technical jargon without sufficient explanation. The figures and tables are informative but could be better annotated for a general audience.

## Recommendation posture
Supportive if technical concerns are resolved. The study addresses a relevant and timely topic with a reasonable computational approach. However, the current evidence is insufficient to fully support the claims, particularly regarding the enhanced binding mutant and the therapeutic implications. The authors should address the statistical and methodological issues, provide experimental validation or clearly state the speculative nature of their predictions, and improve the accessibility of the presentation.