## Review setup
- **Input scope** Full manuscript text (preprint, bioRxiv)
- **Assessment boundary** Scientific content, methodological validity, and claims as presented in the provided manuscript text. No supplementary material, figures, or source code were available for inspection.
- **Shared manuscript claim summary** The authors introduce a computational framework (b-CR-MC) that couples grand-canonical ion/buffer exchange with explicit charge regulation of titratable residues, and apply it to sequence-resolved coarse-grained simulations of FUS and PGL-3 condensates. They report sequence-dependent pH gradients (alkaline for FUS, acidic for PGL-3) that shift condensate interior pH toward the protein isoelectric point, and identify buffer depletion as a primary determinant of condensate electrochemistry.
- **Visible evidence base** Abstract, Introduction, Methods (theoretical derivations, simulation protocols), Results (qualitative descriptions of Figs. 1–5), Conclusions. Figures and supplementary material referenced but not provided.
- **Missing materials affecting confidence** All figures, supplementary information (including the thermodynamic equivalence proof, reaction sets, benchmarking results, sequences, parameters), and source code. These are essential for verifying the central methodological claims and quantitative results.

## Reviewer
- **Overall assessment** This manuscript addresses a significant and timely problem in biomolecular condensate biophysics: the molecular origin of pH gradients in charge-regulated condensates. The proposed b-CR-MC framework is a logical and potentially powerful extension of existing methods, and the application to FUS and PGL-3 is well motivated. However, the manuscript as presented is a methods paper whose central claims rest on materials (figures, supplementary derivations, benchmarks) that were not available for review. The theoretical foundation is described with insufficient detail to assess its correctness, and the results are presented qualitatively without supporting quantitative data. The scientific premise is strong and the potential impact is high, but the evidence base provided is inadequate to establish the case.
- **Who would be interested in the results, and why** Researchers in biomolecular condensates, phase separation, and biophysical chemistry. The framework offers a computationally tractable route to predicting condensate internal pH and ion composition from sequence, which is directly relevant to understanding charge-dependent client recruitment, post-translational modification effects, and disease-associated mutations. The method could also interest the broader simulation community working on grand-canonical and constant-pH methods.
- **Major strengths** The problem is important and the proposed framework directly addresses a known limitation of fixed-charge models. The extension of CR-MC to buffered multicomponent reservoirs is a sensible and potentially impactful methodological advance. The application to two proteins with opposite net charge provides a clear and compelling test of the central hypothesis. The authors are transparent about model limitations (monovalent buffer approximation, RPM assumptions, slab-geometry issues).
- **Major Concerns**
  - **Concern ID** R1-M1
  - **Severity** Major
  - **Blocking** Yes
  - **Axis** Technical soundness
  - **Claim pointer** The claim that b-CR-MC is thermodynamically equivalent to g-G-RxMC under the RPM, and that the ion-merging strategy reduces the reaction pool without altering thermodynamic observables.
  - **Evidence pointer** Methods (Theoretical and Computational Methods, "Buffered Charge-Regulation Monte Carlo (b-CR-MC)"); Results (Section "b-CR-MC Preserves Thermodynamic Accuracy..."); Supplementary Material Section S1 (referenced, not provided)
  - **Concern** The central methodological claim of thermodynamic equivalence is stated but not demonstrated in the provided text. The derivation is relegated to supplementary material that was not available for review. The definitions of the composite quantities Φ and Ksalt are introduced but their derivation and physical meaning are not explained. The acceptance probability expression is given, but the connection between the reaction set, the equilibrium constants, and the claimed equivalence to g-G-RxMC is not established in the main text. Without the derivation, the core validity of the method cannot be assessed.
  - **Why it matters** The entire framework rests on this equivalence. If the ion-merging is not thermodynamically exact, all subsequent results (pH gradients, buffer partitioning) are potentially compromised. This is a foundational claim that must be verifiable from the provided materials.
  - **Resolution test** Provide the full derivation of the thermodynamic equivalence in the main text or ensure the supplementary material is available for review. The derivation must show, step by step, that the partition function of b-CR-MC is identical to that of g-G-RxMC under the stated assumptions. The definitions of Φ and Ksalt must be derived, not just stated.
  - **Concern ID** R1-M2
  - **Severity** Major
  - **Blocking** Yes
  - **Axis** Technical soundness
  - **Claim pointer** The claim that the μ-tuning procedure faithfully recovers the target reservoir composition (150 mM NaCl, 12 mM buffer, pH 7.40) and that the resulting Ki set is transferable to protein-containing simulations.
  - **Evidence pointer** Results (Section "A Transferable Thermodynamic Reference..."); Methods (Chemical potential tuning); Figure 1 (referenced, not provided)
  - **Concern** The convergence of the μ-tuning procedure is described qualitatively ("converged within eight cycles") and the claim of transferability is asserted, but no quantitative data are shown. The target particle counts are given, but the actual converged values, the tolerances used, and the statistical uncertainties are not reported. The claim that the Ki set is applied "without further adjustment" to protein-containing simulations is critical, but the sensitivity of the results to this choice is not explored. Without seeing the convergence data and the actual particle counts, the reliability of the reservoir coupling cannot be evaluated.
  - **Why it matters** The entire grand-canonical framework depends on the accuracy of the chemical potential calibration. If the reservoir composition is not faithfully reproduced, the computed pH gradients and ion partitioning are meaningless. The transferability claim is essential for the interpretation of the protein simulations.
  - **Resolution test** Show the convergence trajectory of the μ-tuning procedure, the final particle counts with uncertainties, and a demonstration that the Ki set indeed reproduces the target composition in a protein-free system. Ideally, also show that small perturbations to Ki do not qualitatively change the protein simulation results.
  - **Concern ID** R1-M3
  - **Severity** Major
  - **Blocking** Yes
  - **Axis** Technical soundness
  - **Claim pointer** The claim that the slab-geometry simulation resolves the spatial structure of condensate electrochemistry, including the pH profile and ion distributions across the interface.
  - **Evidence pointer** Results (Section "A Slab-Geometry Simulation Resolves the Spatial Structure..."); Figure 5 (referenced, not provided); Methods (Slab-geometry protocol)
  - **Concern** The slab-geometry results are described qualitatively. The authors state that the pH profile "reproduc[es] the sign and direction of the alkaline pH gradient" and that ion profiles reveal "marked enrichment of anions," but no quantitative values are given. More critically, the authors acknowledge that the slab simulation did not yield a coexisting dilute protein phase, meaning the system is not at true phase coexistence. This is a significant limitation that is discussed, but its impact on the interpretation of the interfacial profiles is not fully addressed. The claim that the framework "directly resolves the continuous electrochemical structure across a condensate phase boundary" is weakened by the absence of a proper two-phase equilibrium.
  - **Why it matters** The slab geometry is presented as a complementary validation of the dual-box results and as a tool for resolving interfacial structure. If the simulation is not at coexistence, the profiles may reflect kinetic or finite-size artifacts rather than equilibrium properties. The authors acknowledge this, but the claim of resolving the "continuous electrochemical structure" is overstated given the acknowledged limitations.
  - **Resolution test** Provide the actual pH and ion concentration profiles from the slab simulation. Discuss how the absence of a dilute phase affects the interpretation of the interfacial profiles. Ideally, demonstrate that the dense-phase properties are consistent between the slab and dual-box simulations, and that the interfacial structure is converged with respect to simulation time and system size.
  - **Concern ID** R1-M4
  - **Severity** Major
  - **Blocking** No
  - **Axis** Scientific importance
  - **Claim pointer** The claim that the simulated pH gradients are in "qualitative agreement with experimental observations by Ausserwöger et al." and that the framework provides a "sequence-resolved predictive platform."
  - **Evidence pointer** Results (Sections "Protein Net Charge Determines..." and "Charge Redistribution..."); Conclusions
  - **Concern** The comparison to experiment is only qualitative and is not quantified. The authors state that the simulated gradients are "in qualitative agreement" but do not provide a quantitative comparison (e.g., magnitude of pH shift, dependence on protein concentration, salt concentration). The claim of a "predictive platform" is strong, but the manuscript does not demonstrate predictive power beyond the two proteins studied. The discussion of experimental relevance is largely deferred to the conclusions.
  - **Why it matters** The significance of the work depends on its ability to explain or predict experimental observations. A qualitative agreement with a single experimental study is suggestive but not conclusive. The claim of predictive power requires demonstration on a broader set of sequences or conditions.
  - **Resolution test** Provide a quantitative comparison with the experimental data, including the magnitude of the pH shift and its dependence on relevant parameters. Ideally, include predictions for additional proteins or mutants that could be tested experimentally.
- **Minor Comments**
  - **Concern ID** R1-m1
  - **Severity** Minor
  - **Axis** Readability for nonspecialists
  - **Affected element** Introduction and early Methods
  - **Evidence pointer** Introduction; Methods (first paragraphs)
  - **Issue** The introduction assumes significant familiarity with the field. Terms like "charge regulation," "Donnan potential," and "grand-canonical ensemble" are used without definition. The distinction between the proposed b-CR-MC and existing methods (e.g., g-G-RxMC, constant-pH MD) is not clearly explained for a reader who is not an expert in simulation methods.
  - **Required correction** Add brief definitions of key terms and a clearer explanation of what is new about b-CR-MC compared to existing approaches. Consider a schematic figure or a table comparing methods.
  - **Concern ID** R1-m2
  - **Severity** Minor
  - **Axis** Technical soundness
  - **Affected element** Methods, "Monovalent buffer representation"
  - **Evidence pointer** Methods (Monovalent buffer representation)
  - **Issue** The choice of pKa = 7.20 for the buffer is justified by matching phosphoric acid's second pKa, but the authors do not discuss the sensitivity of the results to this choice. The buffer pKa is a key parameter, and the results may depend on it.
  - **Required correction** Add a brief discussion of how the results would change with a different buffer pKa, or cite a reference that addresses this.
  - **Concern ID** R1-m3
  - **Severity** Minor
  - **Axis** Technical soundness
  - **Affected element** Methods, "Hybrid MD/MC scheme"
  - **Evidence pointer** Methods (Hybrid MD/MC scheme in HOOMD-blue)
  - **Issue** The manuscript states that the plugin was verified against ESPResSo, but the benchmarking details are in the supplementary material. A brief summary of the benchmark results in the main text would increase confidence in the implementation.
  - **Required correction** Add a sentence summarizing the benchmark results (e.g., "The plugin reproduced ESPResSo results for [system] to within [statistical measure]").
  - **Concern ID** R1-m4
  - **Severity** Minor
  - **Axis** Readability for nonspecialists
  - **Affected element** Results, Section "Protein Net Charge Determines..."
  - **Evidence pointer** Results (Section "Protein Net Charge Determines...")
  - **Issue** The terms "alkaline shift" and "acidic shift" are used, but the direction of the shift is not intuitively explained. A reader may not immediately understand why a net-positive protein would cause an alkaline shift.
  - **Required correction** Add a brief physical explanation of why the sign of the net charge determines the direction of the pH shift.

## Risk / unsupported claims
- The central claim of thermodynamic equivalence between b-CR-MC and g-G-RxMC is unsupported in the provided text (derivation in unavailable supplementary material).
- The claim that the μ-tuning procedure faithfully recovers the target reservoir composition is unsupported (no quantitative convergence data shown).
- The claim of "quantitative agreement" with g-G-RxMC is unsupported (benchmark data in unavailable supplementary material).
- The claim of "qualitative agreement" with experimental observations is not quantified and cannot be assessed without the referenced figures.
- The claim that the framework is a "sequence-resolved predictive platform" is not demonstrated beyond the two proteins studied.
- The slab-geometry results are described qualitatively, and the acknowledged absence of a coexisting dilute phase limits the interpretation of the interfacial profiles.
- The magnitude of the reported pH shifts (e.g., +0.32 for FUS, −0.29 for PGL-3) is stated without statistical uncertainties or convergence analysis.
- The claim that charge regulation is a "primary determinant rather than a secondary correction" is a strong interpretation that is not directly tested against a fixed-charge model in the provided text.

## Assessment against Nature-style criteria
- **Originality** The work is original in its specific combination of ion-merging, buffered reservoirs, and charge regulation applied to sequence-resolved condensates. The extension of CR-MC to buffered systems is a novel contribution. However, the underlying concepts (charge regulation, Donnan equilibrium, grand-canonical sampling) are established, and the novelty is incremental rather than conceptual.
- **Scientific importance** The problem is important. Predicting condensate internal pH and ion composition from sequence has broad implications for understanding condensate function and disease. If the framework is validated, it could become a standard tool. However, the importance is conditional on the validity of the method, which is not fully established in the provided text.
- **Interdisciplinary readership** The topic is of interest to biophysicists, physical chemists, and cell biologists. The methods are specialized, but the implications for condensate biology are broad. The manuscript is likely to appeal to a reasonably wide readership within these fields, though the technical detail may limit accessibility to a general audience.
- **Technical soundness** The technical soundness cannot be fully assessed from the provided text. The theoretical derivation is missing, the benchmarks are in unavailable supplementary material, and the results are presented qualitatively. The authors are transparent about limitations, which is commendable, but the evidence base is insufficient to establish technical soundness.
- **Readability for nonspecialists** The manuscript is written for a specialist audience. The introduction and methods assume significant background knowledge. The results are described in a way that is accessible to experts but may be challenging for others. The structure is logical, but the lack of quantitative detail makes it difficult to follow the argument.

## Recommendation posture
Currently not established from the provided evidence. The scientific premise is strong and the potential impact is high, but the central methodological claims are not verifiable from the manuscript text alone. The authors must provide the supplementary material (derivations, benchmarks, figures) and ideally present quantitative results in the main text. The manuscript could become suitable for publication in a high-impact journal if the technical concerns are resolved and the claims are supported by the full evidence base.