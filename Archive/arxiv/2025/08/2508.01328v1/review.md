## Review setup
- **Input scope** Full manuscript text including main text and supplementary materials
- **Assessment boundary** Scientific content, methodology, evidence quality, and claims as presented in the provided manuscript
- **Shared manuscript claim summary** The authors propose a new mechanism termed "electrostatic depletion" arising from electrostatic correlations within complex coacervates, which drives aggregation of guest macromolecules including neutral polymers, low-charge-density polyelectrolytes, and intrinsically disordered proteins, even in the absence of chemical incompatibility. They support this claim with coarse-grained molecular dynamics simulations and present implications for encapsulation efficiency.
- **Visible evidence base** Main text Figures 1, 2, and 4 (referenced but not fully visible in provided material); Supplementary Figures S1-S6; simulation methodology described in Supplementary Sections S1-S3
- **Missing materials affecting confidence** Actual figure images and numerical data are not provided; simulation parameter details are partially available; no quantitative error analysis or convergence metrics beyond stated simulation times; no experimental validation

## Reviewer
- **Overall assessment** The manuscript presents an intriguing and potentially significant hypothesis regarding a new depletion-type force in complex coacervates. The concept of electrostatic depletion driven by charge correlations is conceptually appealing and could fill a genuine gap in understanding guest behavior in coacervates. However, the evidence as presented is primarily qualitative, and several technical aspects require clarification before the claims can be fully evaluated. The theoretical framework, while plausible, needs more rigorous development and quantitative validation. The manuscript would benefit from clearer presentation of simulation details, more systematic parameter sweeps, and direct comparison with alternative explanations.

- **Who would be interested in the results, and why** Researchers in soft matter physics, polymer physics, biophysics, and physical chemistry would find this work relevant. Specifically, those studying liquid-liquid phase separation, membraneless organelles, coacervate-based drug delivery, and protocell design would be interested. The proposed mechanism could have implications for understanding protein aggregation in cellular contexts and for designing encapsulation systems.

- **Major strengths**  
  1. The identification of a potentially universal aggregation mechanism in coacervates addresses a significant unexplained experimental observation.  
  2. The systematic exploration across neutral polymers, polyelectrolytes, and IDPs suggests generality.  
  3. The connection to encapsulation efficiency provides practical relevance.  
  4. The use of a simplified model (GCMe) allows for controlled investigation of electrostatic effects.

- **Major Concerns**

- **Concern ID** R1-M1  
- **Severity** Major  
- **Blocking** Yes  
- **Axis** Evidence sufficiency  
- **Claim pointer** The authors claim that "electrostatic depletion" is a universal mechanism driving guest aggregation in coacervates, distinct from classical depletion effects.  
- **Evidence pointer** Figures 1, 2, 4; Supplementary Sections S4-S8  
- **Concern** The central claim of universality is supported primarily by simulation snapshots and PMF curves, but the evidence is largely qualitative. The manuscript does not provide a systematic quantitative comparison between the proposed electrostatic depletion mechanism and alternative explanations (e.g., excluded volume effects, specific ion effects, or local charge patterning effects). The scaling argument presented in Equation (1) is not rigorously derived or validated against simulation data across a range of parameters.  
- **Why it matters** Without quantitative validation and exclusion of alternative mechanisms, the claim of a new universal force remains speculative. The scientific community requires clear evidence that the observed aggregation is specifically due to electrostatic correlations rather than other coexisting effects.  
- **Resolution test** Provide quantitative comparison between simulation results and theoretical predictions from Equation (1) across varying chain lengths, host concentrations, and charge densities. Perform control simulations where electrostatic correlations are artificially suppressed (e.g., by screening) to demonstrate the specific role of this mechanism. Show that the magnitude of the effect scales as predicted by the theory.

- **Concern ID** R1-M2  
- **Severity** Major  
- **Blocking** Yes  
- **Axis** Technical soundness  
- **Claim pointer** The authors state that "the electrostatic depletion is stronger for higher host polymer concentration" and that the effect depends on guest chain length relative to electrostatic blob size.  
- **Evidence pointer** Figure 2C; Supplementary Section S4  
- **Concern** The simulation methodology for PMF calculations uses the adaptive bias force (ABF) algorithm, but convergence criteria are not fully described. The manuscript states each window ran for 1×10^6 τ₀, but does not provide error estimates or convergence checks. Additionally, the system sizes appear small (50σ₀ box for bulk coacervate), and finite-size effects are not discussed. The relationship between the blob size ξ = 2.7σ₀ and the observed chain-length dependence is not systematically explored.  
- **Why it matters** PMF calculations are computationally demanding and prone to convergence issues. Without proper convergence validation and finite-size analysis, the quantitative claims about interaction strengths and their parameter dependence may be unreliable.  
- **Resolution test** Provide convergence plots for PMF calculations, block-averaged error estimates, and demonstrate that results are robust to system size. Perform simulations with varying box sizes to rule out finite-size artifacts. Show that the blob size determination is robust and that the chain-length threshold for aggregation correlates with the blob size as claimed.

- **Concern ID** R1-M3  
- **Severity** Major  
- **Blocking** No  
- **Axis** Conceptual clarity  
- **Claim pointer** The authors distinguish electrostatic depletion from classical depletion and suggest it operates at comparable length scales between guest and host polymers.  
- **Evidence pointer** Discussion section; Figure 4A  
- **Concern** The physical picture of "electrostatic blobs" and their role in generating depletion forces is not fully developed. The manuscript invokes blob concepts from polyelectrolyte physics but does not clearly explain how the correlated structure of oppositely charged blobs creates an effective attraction between guest chains. The analogy to solvation and hydrogen bonding networks is suggestive but not quantitatively developed.  
- **Why it matters** For the concept to be adopted and tested by the community, the physical mechanism must be clearly articulated. A vague mechanistic picture limits the ability of others to design experiments or simulations to validate the claims.  
- **Resolution test** Provide a more rigorous theoretical derivation of the electrostatic depletion force from the correlated blob structure. Include a schematic or quantitative model showing how guest chains disrupt blob correlations and why this leads to effective attraction. Discuss the range of validity of the blob approximation for the systems studied.

- **Concern ID** R1-M4  
- **Severity** Major  
- **Blocking** No  
- **Axis** Generalizability  
- **Claim pointer** The authors claim the mechanism applies to "neutral polymers, low-charge-density polyelectrolytes, and intrinsically disordered proteins (IDPs)."  
- **Evidence pointer** Figures 1B-D, 2E-F; Supplementary Sections S5-S6  
- **Concern** The IDP model used is highly simplified (50 monomers, specific charge patterns). Real IDPs have sequence complexity, post-translational modifications, and heterogeneous interactions that may alter the behavior. The claim of relevance to real IDPs is extrapolated from a minimal model. Additionally, the study only considers one host coacervate composition (fully charged polyelectrolytes at specific lengths), and the generality across different coacervate types is not established.  
- **Why it matters** The manuscript positions this as a universal mechanism with implications for biological systems. Overgeneralization from simplified models could mislead the field and lead to incorrect predictions for real systems.  
- **Resolution test** Test additional IDP sequences with varying charge distributions, lengths, and compositions. Explore different host coacervate systems (e.g., different charge densities, chain lengths, salt conditions). Discuss limitations of the model and conditions under which the mechanism may break down.

- **Minor Comments**

- **Concern ID** R1-m1  
- **Severity** Minor  
- **Axis** Presentation  
- **Affected element** Abstract and Introduction  
- **Evidence pointer** Abstract; Introduction paragraph 1  
- **Issue** The abstract states "guest macromolecules exhibit a strong tendency to aggregate within coacervates even in the absence of apparent chemical incompatibility" but does not cite specific experimental observations. The introduction mentions experiments but does not provide specific references for the aggregation phenomenon.  
- **Required correction** Add specific experimental references in the introduction that document the unexplained aggregation of guest polymers in coacervates, and briefly describe these observations in the abstract to establish the empirical motivation.

- **Concern ID** R1-m2  
- **Severity** Minor  
- **Axis** Technical clarity  
- **Affected element** Methods and Supplementary Section S1  
- **Evidence pointer** Supplementary Section S1  
- **Issue** The GCMe model parameters are described, but the mapping to physical units is not fully explained. The relationship between σ₀ = 0.64 nm and the actual polymer properties (persistence length, excluded volume) is not discussed. The choice of bond strength K_bond = 100 k_BT/σ₀² is not justified.  
- **Required correction** Provide a more detailed description of the model parameterization, including how the chosen parameters relate to real polymer systems. Justify the choice of bond strength and discuss the sensitivity of results to these parameters.

- **Concern ID** R1-m3  
- **Severity** Minor  
- **Axis** Data presentation  
- **Affected element** Figures 1, 2, 4  
- **Evidence pointer** Figures 1, 2, 4 (referenced)  
- **Issue** The manuscript references figures but the actual figure content is not visible in the provided material. Based on the text, it is unclear whether error bars are shown, how many independent simulations were performed, and whether representative snapshots or averaged quantities are displayed.  
- **Required correction** Ensure all figures include error estimates where applicable, state the number of independent simulations, and clearly label whether snapshots are representative or averaged.

- **Concern ID** R1-m4  
- **Severity** Minor  
- **Axis** Interpretation  
- **Affected element** Discussion of entropy versus energy  
- **Evidence pointer** Discussion section  
- **Issue** The discussion of whether electrostatic depletion is entropy- or energy-driven is somewhat speculative. The authors reference work by Chen and Wang on electrostatic entropy but do not provide a clear analysis for their specific system.  
- **Required correction** Either provide a quantitative decomposition of the free energy into entropic and enthalpic contributions from simulations, or clearly frame this as an open question requiring future investigation.

- **Concern ID** R1-m5  
- **Severity** Minor  
- **Axis** Completeness  
- **Affected element** Encapsulation efficiency analysis  
- **Evidence pointer** Figure 4D-E  
- **Issue** The spinodal concentration calculation relies on the second virial coefficient from PMF, but the derivation is not shown in the main text. The practical implications for encapsulation are stated but not quantitatively connected to the simulation results.  
- **Required correction** Show the derivation of the spinodal concentration from the virial coefficient, and provide a more explicit discussion of how the simulation results translate to practical encapsulation predictions.

## Risk / unsupported claims
- The claim that electrostatic depletion is a "universal" mechanism is not fully supported given the limited parameter space explored and the simplified model systems used.
- The assertion that the mechanism applies to real IDPs is extrapolated from a minimal model and requires validation with more realistic IDP sequences.
- The statement that electrostatic depletion "fills the gap in the aggregation mechanisms between nanoscale hydrophobic effect and macroscopic depletion effect" is speculative and not quantitatively justified.
- The claim that encapsulation efficiency can be "substantially improved by grafting more charged residues" is based on simulation trends but lacks experimental validation.
- The thermodynamic origin (entropy versus energy) of electrostatic depletion is discussed but not resolved, and the manuscript acknowledges this uncertainty.
- The relationship between the blob size ξ = 2.7σ₀ and the observed chain-length threshold for aggregation is asserted but not rigorously demonstrated across conditions.