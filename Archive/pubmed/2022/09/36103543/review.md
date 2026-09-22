## Review setup
- **Input scope** Full manuscript text (abstract, introduction, results, discussion, materials and methods) as provided by the user. Supplementary materials referenced but not provided.
- **Assessment boundary** Scientific soundness, internal consistency, and support of claims based solely on the supplied text. No external literature verification or replication of calculations performed.
- **Shared manuscript claim summary** The authors propose a molecular mechanism for the dual (enhancing and inhibiting) effect of ATP on phase separation of FUS protein solutions. They combine semiempirical quantum mechanical (SQM) calculations, mean-field theory, and coarse-grained molecular dynamics (CGMD) simulations to argue that ATP acts as a multivalent (bivalent or trivalent) binder to arginine residues, leading to reentrant phase separation: enhancement at low ATP concentrations and inhibition at high concentrations, with dissolution of condensates at approximately 10 mM ATP, consistent with prior experiments.
- **Visible evidence base** Main text figures (Figures 1–5) are referenced but not shown. Equations 1–12 are provided. Methods descriptions for SQM, mean-field theory, and CGMD are present. Supplementary figures (figs. S1–S4) and movies (S1–S3) are referenced but not provided.
- **Missing materials affecting confidence** All figures, supplementary figures, and movies are absent. Parameter values for the mean-field theory (e.g., interaction strengths, chain length N1, solvent length N2) are only partially given. Details of the phase diagram calculation (binodal construction, common tangent construction) are relegated to Supplementary Materials. Experimental data used for comparison are cited but not reproduced.

## Reviewer
- **Overall assessment** The manuscript addresses a timely and important question: how ATP can both promote and dissolve biomolecular condensates. The combination of quantum-chemical, analytical, and simulation methods is ambitious and potentially valuable. However, the provided text alone does not allow verification of the central quantitative claims. The mean-field theory is presented in outline, but key steps and parameter values are missing. The SQM results are summarized qualitatively, and the CGMD results are described only in general terms. The conceptual framework is plausible, but the evidence as presented is insufficient to establish the mechanism conclusively.
- **Who would be interested in the results, and why** Researchers in the fields of biomolecular condensates, phase separation, intrinsically disordered proteins, and cellular organization. Also of interest to computational biophysicists and chemists working on multivalent interactions and coarse-grained modeling. The potential link to ATP's physiological concentration and neurodegenerative disease broadens the appeal to cell biologists and neurobiologists.
- **Major strengths** 1. The study tackles a genuinely puzzling experimental observation (dual effect of ATP) with a multi-scale approach. 2. The combination of SQM, mean-field theory, and CGMD is methodologically ambitious and could provide a template for future studies. 3. The prediction of a maximum binding valence of three for ATP-Arg interactions is a concrete, testable claim. 4. The connection between microscopic binding parameters and macroscopic phase diagrams is conceptually appealing. 5. The authors engage with prior experimental work and place their findings in a broader context.
- **Major Concerns** See detailed items below.
- **Minor Comments** See detailed items below.
- **Technical failings that need to be addressed before the case is established** R1-M1 (missing parameter values and derivation steps), R1-M2 (unverifiable SQM results), R1-M3 (unverifiable CGMD results), R1-M4 (incomplete comparison with experiments).
- **Assessment against Nature-style criteria** **Originality:** The question is important and the multi-scale approach is not entirely novel but is applied to a specific and timely problem. The claim of a maximum ATP valence of three is a potentially original contribution. **Scientific importance:** High, given the widespread interest in ATP as a biological hydrotrope and the general phenomenon of reentrant phase separation. **Interdisciplinary readership:** The topic bridges physical chemistry, biophysics, and cell biology, and should appeal to a broad audience. **Technical soundness:** Cannot be fully assessed from the provided text. The theoretical framework is plausible, but key details are missing. The SQM and CGMD results are presented without sufficient quantitative detail. **Readability for nonspecialists:** The introduction and discussion are accessible, but the results section is dense and assumes familiarity with polymer theory and simulation methods. The manuscript would benefit from clearer explanations of the mean-field approach and the physical meaning of key parameters.
- **Recommendation posture** Supportive if technical concerns are resolved. The conceptual framework is promising, but the current evidence base is insufficient to establish the mechanism. The authors must provide full derivations, parameter values, and quantitative results for all three methods.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The mean-field theory provides phase diagrams with full binodals that can be directly compared with experimental phenomena.
- **Evidence pointer** Results section "Mean-field theory on the relationship between microscopic interactions and macroscopic phase behaviors"; Materials and Methods "Theoretical modeling of FUS solutions in the absence of ATP" and "Theoretical modeling of FUS solutions in the presence of ATP"; Equations 1–12.
- **Concern** The mean-field theory is the central quantitative pillar of the manuscript, but the provided text does not contain sufficient detail to evaluate its correctness or reproducibility. Key parameter values are missing: the chain length N1 is given as 526, but the number of Tyr and Arg residues (m1 = m2 = 34) is stated only in the predictions section, not in the main model description. The solvent chain length N2 is introduced but its value is only mentioned as a fitting parameter (N2 = 65) without justification. The interaction strengths ϵ1 and ϵ2 are not given numerical values. The derivation of the free energy expressions (Equations 6 and 12) is not shown, and the steps from the partition function to the final free energy are not explained. The construction of the phase diagram (binodal calculation, common tangent construction, spinodal) is relegated to Supplementary Materials, which were not provided. Without these details, the phase diagrams in Figure 3 cannot be reproduced or independently verified.
- **Why it matters** The central claim of a reentrant phase separation and the quantitative prediction of dissolution at approximately 10 mM ATP depend entirely on the mean-field theory. If the theory contains errors or if the parameter values are not physically justified, the conclusions are unsupported. The manuscript cannot be evaluated without full transparency of the model and its parameters.
- **Resolution test** The authors must provide a complete derivation of the free energy, all parameter values (with physical justification), and a detailed description of the phase diagram construction. The binodal curves should be reproducible from the provided information. Ideally, the authors should provide the code or a detailed algorithmic description.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The SQM method reveals that ATP acts as a bivalent or trivalent binder to arginine, with binding free energies of approximately −2.0 kBT for Tyr-Arg and stronger for ATP-Arg.
- **Evidence pointer** Results section "SQM methods on the microscopic interactions between ATP and Arg"; Figure 2; Figure 1 (A and B); Materials and Methods "The SQM method".
- **Concern** The SQM results are presented only as qualitative statements. The binding free energies for ATP-Arg are not reported numerically, despite the claim that the CGMD interaction strength (U0 = −75ϵ0) was chosen because "the binding free energy of ATP-Arg was nearly four times as strong as that of Tyr-Arg." The reader cannot verify this factor of four. The binding modes shown in Figure 2 are not described in the text. The dependence of binding free energy on the number of arginine residues (L = 1, 2, 3, 4) is mentioned, but the actual values are not given. The comparison with the tripeptide model (fig. S1) is mentioned but the results are not summarized. The SQM method (GFN2-xTB) is a semiempirical method, and its accuracy for this type of interaction should be discussed, particularly the choice of implicit solvent model and the treatment of entropic contributions.
- **Why it matters** The SQM results provide the microscopic input for the mean-field theory. If the binding free energies and valences are incorrect, the entire theoretical framework is compromised. The quantitative relationship between SQM and CGMD parameters is asserted but not demonstrated.
- **Resolution test** The authors must report the numerical values of all computed binding free energies (for Tyr-Arg and ATP-Arg with L = 1, 2, 3, 4), including error estimates or at least a discussion of the method's accuracy. The binding modes should be described in the text. The relationship between the SQM binding free energies and the CGMD interaction potentials should be explicitly derived.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** CGMD simulations confirm the reentrant phase separation and show that the dynamic exchange of molecules between condensate and surroundings is nonmonotonic with ATP concentration.
- **Evidence pointer** Results section "CGMD simulation on the effect of ATP on the phase separation from the dynamic view"; Figure 4; figs. S2–S4; movies S1–S3; Materials and Methods "The CGMD simulation".
- **Concern** The CGMD results are described only in qualitative terms. No quantitative data are provided in the main text: no cluster sizes, no critical concentrations, no exchange rates. The claim of "reentrant phase separation" is supported only by reference to figures that are not shown. The simulation parameters are given, but the mapping between the simulation model and the real FUS protein is not justified. The choice of U0 = −75ϵ0 for ATP-Arg is based on the SQM result, but the relationship between the two energy scales is not explained. The simulation time (50 ms total) and system size (50 × 50 × 250 nm) are stated, but it is not clear whether these are sufficient to achieve equilibrium or to observe the reported phenomena. The analysis of molecular exchange (Figure 4) is described only qualitatively.
- **Why it matters** The CGMD simulations are presented as independent verification of the mean-field theory. Without quantitative results, the reader cannot assess whether the simulations actually support the theoretical predictions or whether they are consistent with experimental observations.
- **Resolution test** The authors must provide quantitative measures of phase separation from the simulations, such as cluster size distributions, coexistence concentrations, and order parameters, as a function of ATP concentration. The exchange dynamics should be quantified (e.g., residence times, flux across the interface). The mapping between simulation and experimental conditions should be clarified.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** Yes
- **Axis** Scientific importance
- **Claim pointer** The predicted ATP concentration for dissolving protein condensates is about 10 mM, agreeing with experimental results.
- **Evidence pointer** Abstract; Results section "Mean-field theory on the relationship between microscopic interactions and macroscopic phase behaviors"; Figure 3C.
- **Concern** The comparison with experimental data is cursory. The authors state agreement with experiments by Patel et al. (35) (8–12 mM) but do not provide a quantitative comparison. The experimental conditions (e.g., FUS concentration, buffer, temperature) are not stated. The theoretical prediction depends on the parameter values, which are not fully disclosed. The agreement could be fortuitous if the parameters are not well constrained. The authors also do not discuss the sensitivity of the predicted dissolution concentration to the model parameters.
- **Why it matters** The agreement with experiment is a key selling point of the manuscript. If the comparison is not rigorous, the claim of experimental validation is weakened.
- **Resolution test** The authors should provide a detailed comparison with the experimental data, including the experimental conditions and the range of theoretical predictions given reasonable parameter variations. A sensitivity analysis of the predicted dissolution concentration to the model parameters would strengthen the claim.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Readability
- **Affected element** Introduction and Results
- **Evidence pointer** Introduction, first paragraph; Results section "The relationship between Tyr-Arg binding and phase separation in FUS solution"
- **Issue** The introduction does not clearly define what is meant by "phase separation" for readers unfamiliar with the field. The term "reentrant phase separation" is used without definition.
- **Required correction** Provide a brief definition of phase separation and reentrant phase separation in the introduction, or at least a clear explanation of the phenomenon in the context of FUS.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Technical soundness
- **Affected element** Materials and Methods, "Theoretical modeling of FUS solutions in the absence of ATP"
- **Evidence pointer** Equation 1 and surrounding text
- **Issue** The Flory-Huggins-type free energy in Equation 1 does not include an explicit interaction term between FUS and solvent. The only interaction is introduced through the binding free energy. It is unclear whether this is a deliberate simplification or an omission.
- **Required correction** Clarify whether the model includes non-specific FUS-solvent interactions and, if not, justify this simplification.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Technical soundness
- **Affected element** Materials and Methods, "Theoretical modeling of FUS solutions in the presence of ATP"
- **Evidence pointer** Equation 7 and surrounding text
- **Issue** The chemical potential term μATP is introduced, but its physical meaning and the choice of the semiclosed system are not explained clearly. The relationship between μATP and the ATP volume fraction φ is given, but the derivation is not shown.
- **Required correction** Provide a brief explanation of the semiclosed system and the physical meaning of μATP.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Readability
- **Affected element** Results section "CGMD simulation on the effect of ATP on the phase separation from the dynamic view"
- **Evidence pointer** Figure 4 and accompanying text
- **Issue** The description of molecular exchange is vague. The terms "exchanged chains" and "molecular exchange" are not defined quantitatively.
- **Required correction** Define how molecular exchange is measured and what quantity is plotted in Figure 4.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Scientific importance
- **Affected element** Discussion
- **Evidence pointer** Discussion, first paragraph
- **Issue** The discussion of implications for neurodegenerative disease is brief and not well supported by the results. The connection between ATP-mediated phase separation and disease is speculative.
- **Required correction** Either expand the discussion with specific hypotheses or temper the claims about disease relevance.

## Risk / unsupported claims
- The claim that ATP acts as a trivalent binder with a maximum of three arginine residues is not quantitatively supported in the text; the SQM binding free energies are not reported.
- The claim that the predicted dissolution concentration of approximately 10 mM agrees with experiments is not rigorously established; the comparison is qualitative and the parameter dependence is not discussed.
- The claim that the CGMD simulations confirm the reentrant phase separation is not supported by quantitative data in the text.
- The claim that the three methods (SQM, mean-field theory, CGMD) are consistent with each other is asserted but not demonstrated with quantitative comparisons.
- The claim that the model provides "a clear physical description of the microscopic interaction and macroscopic phase diagram" is not fully supported because the phase diagrams are not shown and the derivation is incomplete.