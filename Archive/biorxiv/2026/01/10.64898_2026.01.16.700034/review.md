## Review setup
- **Input scope** Full manuscript text (abstract, introduction, results, discussion, methods, supporting information references)
- **Assessment boundary** Scientific claims, experimental design, data interpretation, and internal consistency based solely on the provided manuscript text
- **Shared manuscript claim summary** The authors report that the isolated GPR126/ADGRG6 Stachel peptide is predominantly disordered in aqueous and membrane-mimetic environments, despite structure prediction tools (AlphaFold3, Pepfold4) modeling it as helical. A single-turn helix (L846-L849) is induced by trifluoroethanol (TFE), and the authors propose a conformational-selection activation mechanism for adhesion GPCRs.
- **Visible evidence base** Abstract; Introduction; Results sections (three subsections); Discussion; Materials and Methods (peptide synthesis, modeling, CD, NMR assignment, secondary shift calculation, temperature shift calculation); Supporting Information references (Tables S1-S2, Figure S1)
- **Missing materials affecting confidence** Figures 1-5 are referenced but not provided; Supporting Information (Tables S1-S2, Figure S1) not provided; raw NMR chemical shift assignments, CD spectra, and deconvolution outputs not provided; no sequence coordinates or construct details beyond text description; no statistical analysis details for CD deconvolution or NMR parameter comparisons

## Reviewer
- **Overall assessment** The manuscript addresses a relevant question in adhesion GPCR biology, namely the conformational properties of the isolated Stachel peptide and their implications for activation mechanisms. The combination of prediction tools with biophysical solution-state measurements is appropriate. However, the evidence presented is insufficient to fully support the central claims. Key concerns include the absence of quantitative comparisons between prediction and experiment, incomplete NMR analysis (no assignment completeness statistics, no error estimates for secondary shifts or temperature coefficients), and a mismatch between the CD-derived secondary structure estimates and the NMR-derived helix location. The claim of a conformational-selection mechanism is speculative and not directly tested. The manuscript would benefit from additional experiments (e.g., relaxation dispersion, binding assays with TM domain) and clearer presentation of quantitative data.
- **Who would be interested in the results, and why** Researchers studying adhesion GPCR activation mechanisms, peptide-receptor interactions, intrinsically disordered proteins, and biophysicists interested in conformational equilibria of signaling peptides. The findings may also be relevant to drug discovery efforts targeting aGPCR Stachel sites.
- **Major strengths** 1) The question is timely and mechanistically important for aGPCR biology. 2) The combination of multiple biophysical techniques (CD, NMR) with prediction tools is appropriate. 3) The study addresses a previously uncharacterized aspect of Stachel peptide behavior in solution. 4) The authors acknowledge limitations regarding physiological relevance of TFE conditions.
- **Major Concerns** See detailed items below.
- **Minor Comments** See detailed items below.
- **Technical failings that need to be addressed before the case is established** R1-M1 (quantitative comparison between prediction and experiment), R1-M2 (NMR analysis completeness and error reporting), R1-M3 (CD-NMR consistency), R1-M4 (conformational-selection claim unsupported)
- **Assessment against Nature-style criteria** **Originality** Moderate. The observation that a peptide predicted to be helical is disordered in solution is not entirely novel, but the specific application to aGPCR Stachel peptides and the proposed two-state equilibrium adds some originality. **Scientific importance** Moderate to high. Understanding Stachel peptide conformational behavior is relevant to aGPCR activation mechanisms, but the direct physiological implications are not established. **Interdisciplinary readership** Moderate. The topic will appeal to GPCR biologists and biophysicists, but the narrow focus on a single peptide may limit broader interest. **Technical soundness** Currently insufficient. Several technical aspects require clarification and additional analysis (see Major Concerns). **Readability for nonspecialists** Acceptable. The manuscript is generally well-written, but some sections (e.g., NMR methods) assume specialist knowledge. The abstract is clear and accessible.
- **Recommendation posture** Currently not established from the provided evidence. The manuscript addresses an interesting question and presents preliminary data, but the central claims require additional quantitative analysis, experimental support, and clarification of inconsistencies before the case is convincing.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence strength
- **Claim pointer** The authors state that "despite high AIUPred-predicted disorder scores for many aGPCR Stachel peptides, Pepfold4 predicted that all adopt structured conformations with relatively high confidence" and that "the isolated Stachel peptide shows almost an entirely disordered character" based on AIUPred predictions.
- **Evidence pointer** Results section "AlphaFold3 and Pepfold4 Model a Structured Stachel Peptide Despite Disorder Prediction"; Figure 2C; SI Table 2
- **Concern** The manuscript does not provide a quantitative comparison between the AIUPred disorder predictions and the Pepfold4 structural predictions. The text states that AIUPred predicts disorder and Pepfold4 predicts structure, but no numerical values (e.g., disorder scores, confidence metrics, per-residue probabilities) are presented in the main text. The claim that the peptide is "almost entirely disordered" is based on a prediction, not on experimental data. The CD data in aqueous buffer are described as "44% stranded, 14% turn, and 42% other," which does not directly support a predominantly disordered state. The authors need to provide quantitative disorder scores and a direct comparison with the experimental CD-derived secondary structure estimates.
- **Why it matters** The central premise of the manuscript is that prediction tools and experiments disagree, motivating the biophysical characterization. Without quantitative prediction data, the reader cannot assess the strength of this claimed discrepancy. Furthermore, the CD data do not clearly support the "predominantly disordered" claim, as 44% stranded character is substantial.
- **Resolution test** Provide per-residue AIUPred scores for the GPR6 Stachel peptide in the three states (inactive, intermediate, active-like) and compare them quantitatively with the Pepfold4 per-residue confidence scores. Additionally, present the CD-derived secondary structure percentages with error estimates and discuss how 44% stranded character is reconciled with the "predominantly disordered" conclusion.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors claim that NMR analysis "revealed, through both a reduction in amide protein exchange (temperature coefficient) and an increase in backbone secondary chemical shift changes, that the helical segment likely forms between L846-L849."
- **Evidence pointer** Results section "NMR Defines Region of TFE-Induced Helicity"; Figures 4B, 4C, 5A, 5B
- **Concern** The NMR analysis is presented without key quantitative details. The authors state that resonances were assigned to 85% completion but do not provide assignment completeness per residue or per atom type. The secondary chemical shift analysis (Figure 4B) is described qualitatively ("subtle induction of helical character") without numerical values or error estimates. The temperature coefficient data (Figure 4C) are presented for only a few residues, and the threshold for "structured" (greater than -4.6 ppb/K) is cited from the literature, but the authors do not report the actual values for all assigned residues. The NOE data (Figure 5A, 5B) are described qualitatively, and the authors do not provide a quantitative comparison of NOE patterns between the two conditions (aqueous vs. TFE). The claim that the helix is localized to L846-L849 is based on a small number of parameters, and the authors do not discuss the possibility of other helical populations or dynamic exchange.
- **Why it matters** The NMR data are the primary experimental evidence for the location and nature of the TFE-induced helix. Without quantitative reporting of chemical shifts, temperature coefficients, and NOE assignments, the reader cannot evaluate the robustness of the helical assignment. The 85% assignment completeness is not sufficient to rule out additional structured regions.
- **Resolution test** Provide a table of assigned chemical shifts (H, C, N) for both conditions, with per-residue completeness. Report secondary chemical shift values (C, C, H, N) with uncertainties for all assigned residues. Provide temperature coefficient values for all assigned amides, with the threshold clearly marked. Quantify the number and type of NOEs observed in each condition and provide a per-residue summary of NOE patterns. Discuss how the 15% unassigned residues might affect the conclusions.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Internal consistency
- **Claim pointer** The authors state that "TFE promotes a transition from ~20% beta-stranded to 20% helical character" based on CD deconvolution, and that NMR localizes the helix to L846-L849.
- **Evidence pointer** Results section "Trifluoroethanol Reversibly Induces Local Stachel Helicity"; Figure 3D; Results section "NMR Defines Region of TFE-Induced Helicity"; Figure 4B
- **Concern** The CD data in aqueous buffer indicate 44% stranded character, but the TFE titration data (Figure 3D) are described as showing a transition from ~20% beta-stranded to 20% helical. This is inconsistent with the aqueous buffer data presented in Figure 3A. The authors do not explain this discrepancy. Additionally, the CD-derived helix content in TFE (~20%) corresponds to approximately 3-4 residues, which is consistent with a single turn, but the NMR data suggest the helix is localized to L846-L849 (4 residues). However, the CD data in aqueous buffer suggest significant stranded character (44%), which is not discussed in the context of the NMR data. The authors need to reconcile these observations.
- **Why it matters** The manuscript's central claim is that the peptide is predominantly disordered, but the CD data in aqueous buffer suggest substantial secondary structure. The inconsistency between the aqueous buffer CD data and the TFE titration data undermines the interpretation of the two-state equilibrium. The reader cannot assess whether the peptide is truly disordered in solution or whether the CD deconvolution is unreliable.
- **Resolution test** Provide the full CD spectra for all conditions (aqueous, LMNG, DHPC, and each TFE concentration) and the deconvolution results with error estimates. Explain the discrepancy between the 44% stranded character in aqueous buffer and the ~20% beta-stranded character in the TFE titration. Discuss whether the CD deconvolution algorithm (BeStSel) is appropriate for this peptide and whether the results are consistent with the NMR data.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** Yes
- **Axis** Claim support
- **Claim pointer** The authors propose that "small populations may adopt a helix-containing conformer that seems to support a conformational-selection activation mechanism."
- **Evidence pointer** Abstract; Discussion section
- **Concern** The conformational-selection mechanism is proposed based on the observation of a TFE-induced helix in the isolated peptide. However, no experimental evidence directly links the TFE-induced conformational state to the receptor-bound state. The authors do not provide binding data, kinetic measurements, or any direct test of the conformational-selection hypothesis. The statement "seems to support" is speculative and not supported by the data presented. The authors acknowledge that "further work is needed to determine if these TFE-induced secondary structure changes represent physiologically relevant data," which undermines the claim.
- **Why it matters** The proposed mechanism is a key conclusion of the manuscript and is highlighted in the abstract. Without direct evidence linking the solution-state conformation to the activation mechanism, the claim is not established. The manuscript would be strengthened by either removing the mechanistic claim or providing additional experimental support.
- **Resolution test** Either remove the conformational-selection claim from the abstract and discussion, or provide direct experimental evidence (e.g., binding assays with the TM domain, kinetic measurements, or mutagenesis studies) that links the TFE-induced helical conformation to receptor activation.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Abstract
- **Evidence pointer** Abstract, first sentence
- **Issue** The phrase "that's exposed upon removal or conformational changes" uses a contraction ("that's") which is informal for a scientific manuscript.
- **Required correction** Replace "that's" with "that is."

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Reproducibility
- **Affected element** Methods, Circular Dichroism
- **Evidence pointer** Methods section "Circular Dichroism"
- **Issue** The CD methods state that samples were prepared at 60 uM peptide, but the pathlength is described as "1cm." This is an unusually long pathlength for CD measurements at this concentration, which may lead to high absorbance and unreliable data. The authors do not specify the cuvette volume or the exact instrument parameters (e.g., bandwidth, scan speed, number of accumulations).
- **Required correction** Clarify the pathlength and provide additional experimental details (e.g., cuvette volume, instrument settings, number of scans, temperature control). If the pathlength is indeed 1 cm, justify this choice or correct the typo.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Data presentation
- **Affected element** Results, NMR section
- **Evidence pointer** Results section "NMR Defines Region of TFE-Induced Helicity"; Figure 4B
- **Issue** The authors state that "there is a subtle induction of helical character within residues L846-L849" but do not provide the actual secondary chemical shift values or a statistical comparison between the two conditions (aqueous vs. TFE). The figure is referenced but not provided.
- **Required correction** Provide the numerical secondary chemical shift values for all assigned residues in both conditions, with uncertainties, and indicate which residues show statistically significant changes.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Literature context
- **Affected element** Introduction
- **Evidence pointer** Introduction, paragraph 1
- **Issue** The introduction states that aGPCRs "represent the second largest subclass of GPCRs" but does not provide a citation for this claim. Additionally, the statement that "the mechanism of activation remains arguably the most understudied" is subjective and not supported by specific references.
- **Required correction** Add appropriate citations for the size of the aGPCR subfamily and for the claim that their activation mechanism is understudied.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Terminology
- **Affected element** Results, first subsection
- **Evidence pointer** Results section "AlphaFold3 and Pepfold4 Model a Structured Stachel Peptide Despite Disorder Prediction"
- **Issue** The term "Stachel" is used interchangeably with "Stachel peptide" and "Stachel sequence." While this is understandable, the authors should define the term clearly at first use and use consistent terminology throughout.
- **Required correction** Define "Stachel" at first use (e.g., "the Stachel sequence, also referred to as the Stachel peptide") and use consistent terminology.

- **Concern ID** R1-m6
- **Severity** Minor
- **Axis** Data availability
- **Affected element** Methods, NMR
- **Evidence pointer** Methods section "Nuclear Magnetic Resonance Assignment"
- **Issue** The authors state that spectra were processed using nmrPipe and assigned using CCPNMR, but they do not mention whether the chemical shift assignments have been deposited in a public database (e.g., BMRB). This is standard practice for NMR studies.
- **Required correction** State whether the assignments have been deposited and provide the accession number, or explain why deposition is not applicable.

## Risk / unsupported claims
- The claim that the GPR126 Stachel peptide is "predominantly disordered" in aqueous solution is not fully supported by the CD data presented (44% stranded character in aqueous buffer).
- The claim that the TFE-induced helix (L846-L849) supports a conformational-selection activation mechanism is speculative and not directly tested.
- The statement that "the majority" of aGPCR Stachel peptides adopt an ordered state based on Pepfold4 predictions is not quantitatively supported in the text (no confidence metrics or per-residue scores provided).
- The claim that "inclusion of the N-terminal GAIN domain dramatically orders the Stachel" is based on AIUPred predictions, not experimental data, and the quantitative comparison is not provided.
- The statement that "the proline immediately after this unit (P850) likely acts as a hinge residue" is speculative and not supported by experimental evidence in this manuscript.
- The claim that the findings "seem to support a conformational-selection activation mechanism" is not established from the provided data.