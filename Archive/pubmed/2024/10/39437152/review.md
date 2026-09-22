## Review setup
- **Input scope** Abstract only
- **Assessment boundary** Claims and evidence as presented in the abstract; no access to full manuscript, figures, tables, or supplementary materials
- **Shared manuscript claim summary** The authors use well-tempered metadynamics simulations to study full-length alpha-synuclein (alphaS) adsorption on gold nanoclusters (AuNCs) of varying size (Au(n), n = 25, 36, 44, 68, 102) with thiolated ligands. They report that uncharged Au(n)@SCH2OH preserves the intrinsically disordered conformation of alphaS, while charged AuNCs increase beta-sheet propensity. They further claim that medium-sized Au(36)@SCH2OH significantly inhibits alphaS misfolding into beta-sheet domains, offering design guidelines for AuNC-based PD therapeutics.
- **Visible evidence base** Abstract text only; no simulation details, convergence metrics, free energy surfaces, or structural analyses are provided
- **Missing materials affecting confidence** Full methods, force field parameters, simulation lengths, convergence criteria, free energy error estimates, structural ensemble analyses, ligand coverage details, and any comparison with experimental data

## Reviewer
- **Overall assessment** The abstract presents a potentially interesting computational study on the molecular basis of alphaS-AuNC interactions, with a specific claim about size-dependent modulation of beta-sheet propensity. However, the evidence provided in the abstract is insufficient to evaluate the technical soundness of the simulations or the robustness of the central claims. The key conclusion regarding Au(36)@SCH2OH as an inhibitor is stated without quantitative support, and the absence of methodological details precludes assessment of convergence and accuracy. The work may be of interest to the computational biophysics and nanomedicine communities, but the case is not established from the supplied material.
- **Who would be interested in the results, and why** Computational biophysicists studying protein-nanoparticle interactions, researchers in Parkinson's disease therapeutics exploring nanomaterial-based inhibitors of alpha-synuclein aggregation, and developers of coarse-grained or atomistic simulation methods for intrinsically disordered proteins would find the results relevant. The proposed size-dependent effect of AuNCs on protein misfolding could inform rational design of nanocluster-based interventions.
- **Major strengths** The study addresses a clinically relevant problem with a well-defined computational approach. The systematic variation of AuNC size and surface charge is a logical design. The focus on full-length alphaS at the single-cluster level is appropriate for capturing initial interaction events.
- **Major Concerns**  
  - R1-M1  
  - R1-M2  
  - R1-M3
- **Minor Comments**  
  - R1-m1  
  - R1-m2  
  - R1-m3
- **Technical failings that need to be addressed before the case is established** R1-M1, R1-M2, R1-M3
- **Assessment against Nature-style criteria**  
  Originality: The concept of using medium-sized AuNCs to modulate alphaS misfolding is not entirely novel, as AuNC-protein interactions have been studied, but the specific focus on size-dependent beta-sheet inhibition may offer a new angle. Scientific importance: The potential therapeutic relevance for PD is high, but the abstract does not demonstrate that the computational predictions translate to experimental outcomes. Interdisciplinary readership: The topic bridges nanoscience, biophysics, and neurology, which could attract broad interest if the claims are robustly supported. Technical soundness: Cannot be assessed from the abstract alone; critical details on simulation convergence and force field accuracy are missing. Readability for nonspecialists: The abstract is reasonably clear but uses specialized terms without sufficient context for a general audience.
- **Recommendation posture** Currently not established from the provided evidence. The central claims require substantial additional technical validation before the case can be considered.

### Major Concerns

- **Concern ID** R1-M1  
- **Severity** Major  
- **Blocking** Yes  
- **Axis** Technical soundness  
- **Claim pointer** The authors claim that "uncharged Au(n)@SCH2OH chaperones the native intrinsically disordered conformations of alphaS, while negatively and positively charged AuNCs greatly increase the likelihood of forming intramolecular beta-sheet domains."  
- **Evidence pointer** Abstract text; location not provided  
- **Concern** The abstract provides no quantitative data, such as free energy differences, beta-sheet population fractions, or statistical uncertainties, to support the claim that charged AuNCs "greatly increase" beta-sheet likelihood. Without these numbers, the magnitude of the effect is unverifiable.  
- **Why it matters** The central mechanistic conclusion depends on a comparative assessment of beta-sheet propensity across different AuNC types. If the effect sizes are small or within statistical error, the claim would be overstated.  
- **Resolution test** Provide free energy surfaces or population distributions for beta-sheet content for each AuNC system, with error bars and convergence tests, demonstrating that differences between charged and uncharged AuNCs exceed simulation uncertainty.

- **Concern ID** R1-M2  
- **Severity** Major  
- **Blocking** Yes  
- **Axis** Technical soundness  
- **Claim pointer** The authors claim that "the medium-sized Au(36)@SCH2OH" has a "significant inhibitory effect on alphaS misfolding into beta-sheet domains."  
- **Evidence pointer** Abstract text; location not provided  
- **Concern** The basis for singling out Au(36) as "medium-sized" and as the most effective inhibitor is not explained. No comparative data across the five AuNC sizes are shown, and the term "significant" is used without statistical or thermodynamic quantification.  
- **Why it matters** The size-dependent conclusion is the primary novel finding. Without a clear comparison of beta-sheet propensity across all AuNC sizes, the claim that Au(36) is uniquely inhibitory is unsupported.  
- **Resolution test** Present a quantitative comparison of beta-sheet propensity or binding free energies across all five AuNC sizes, with statistical analysis, showing that Au(36) differs significantly from both smaller and larger clusters.

- **Concern ID** R1-M3  
- **Severity** Major  
- **Blocking** Yes  
- **Axis** Reproducibility  
- **Claim pointer** The study uses "well-tempered metadynamics simulations" to explore "structural and thermodynamic characteristics" of alphaS on AuNCs.  
- **Evidence pointer** Abstract text; location not provided  
- **Concern** No simulation parameters are reported, including force field, water model, ligand modeling approach, simulation length, bias deposition rate, or convergence criteria. Without these, the results cannot be reproduced or assessed for reliability.  
- **Why it matters** Metadynamics results are highly sensitive to collective variable choice and convergence. The absence of these details prevents any evaluation of whether the sampled ensembles are physically meaningful.  
- **Resolution test** Provide full simulation methods in the manuscript, including collective variables, bias parameters, simulation lengths, and convergence checks such as free energy error estimates or block analysis.

### Minor Comments

- **Concern ID** R1-m1  
- **Severity** Minor  
- **Axis** Clarity  
- **Affected element** Terminology  
- **Evidence pointer** Abstract text; location not provided  
- **Issue** The term "chaperones" is used metaphorically to describe the effect of uncharged AuNCs on alphaS conformation, which may be misleading as it implies a specific biological function.  
- **Required correction** Replace with a more neutral term such as "preserves" or "maintains" to avoid overinterpretation.

- **Concern ID** R1-m2  
- **Severity** Minor  
- **Axis** Completeness  
- **Affected element** Experimental context  
- **Evidence pointer** Abstract text; location not provided  
- **Issue** The abstract does not mention any experimental validation or comparison with prior experimental studies on alphaS-AuNC interactions, which would strengthen the translational relevance.  
- **Required correction** Add a sentence in the abstract or introduction referencing relevant experimental work and how the simulations align or contrast with those findings.

- **Concern ID** R1-m3  
- **Severity** Minor  
- **Axis** Readability  
- **Affected element** Abstract structure  
- **Evidence pointer** Abstract text; location not provided  
- **Issue** The abstract moves from a broad statement about PD to specific simulation details without a clear logical bridge, which may reduce accessibility for nonspecialist readers.  
- **Required correction** Restructure the abstract to briefly state the biological question, then the computational approach, and finally the key finding with its implication.

## Risk / unsupported claims
- The claim that charged AuNCs "greatly increase" beta-sheet likelihood is unsupported without quantitative data.
- The claim that Au(36)@SCH2OH has a "significant inhibitory effect" is unsupported without comparative statistics.
- The general statement that the findings "provide a valuable guideline for customizing AuNCs" is an extrapolation not directly evidenced by the abstract.
- The relevance to "disease treatments" is asserted without any experimental or in vivo evidence.