## Review setup
- **Input scope** Abstract only
- **Assessment boundary** Claims and conclusions as stated in the abstract; no methods, figures, or supplementary data were provided for verification
- **Shared manuscript claim summary** The authors propose that NaCl promotes phase separation of the hnRNPA1 low-complexity domain (A1-LCD) through two direct mechanisms (charge neutralization and ion-mediated bridging) and one indirect mechanism (water withdrawal enhancing π-type interactions), and they predict four classes of salt dependence for IDP phase separation based on amino-acid composition
- **Visible evidence base** Abstract text only; no simulation details, system setup, force field parameters, analysis protocols, or quantitative results are available
- **Missing materials affecting confidence** Full manuscript, methods section, all figures and tables, simulation trajectories or derived metrics, statistical analyses, and any comparison with experimental data

## Reviewer
- **Overall assessment** The abstract presents a mechanistically plausible and potentially interesting explanation for the atypical salt dependence of A1-LCD phase separation. The proposed dual direct roles of ions and the indirect water-mediated effect are coherent and testable. However, the evidence base is entirely absent from the supplied material, and the abstract alone cannot establish the validity of the simulation results, the robustness of the mechanistic conclusions, or the predictive power of the proposed classification scheme. The claim of four predicted classes of salt dependence is particularly under-supported without a clear derivation or validation.
- **Who would be interested in the results, and why** Researchers studying phase separation of intrinsically disordered proteins, biophysicists interested in ion-protein interactions, and computational chemists developing or applying all-atom simulations to biomolecular condensates. The work could also inform experimentalists seeking to modulate phase behavior through ionic conditions and those interested in the molecular determinants of salt-dependent condensation.
- **Major strengths** The abstract identifies a clear and biologically relevant puzzle, namely the atypical salt dependence of A1-LCD. The proposed mechanism integrates direct ion binding with indirect solvent-mediated effects, which is a sophisticated and physically reasonable framework. The prediction of a composition-based classification scheme is ambitious and could provide a useful organizing principle for the field.
- **Major Concerns** The abstract provides no quantitative evidence for any of the mechanistic claims. The statements about ion occupancy, binding preferences, charge neutralization, bridging, and water withdrawal are presented as conclusions but no data are shown. The prediction of four classes of salt dependence is stated without derivation or validation, making it impossible to assess its basis or reliability. The relationship between simulation conditions and experimental observations is not described, so the relevance of the findings to real A1-LCD behavior cannot be evaluated.
- **Minor Comments** The abstract would benefit from specifying the number of chains simulated, the simulation length, and the force field used. The term "first-shell" is used without definition. The phrase "drawing water away from the interaction partners" is vague and could be made more precise. The abstract does not state whether the predictions were tested against any experimental data.
- **Technical failings that need to be addressed before the case is established** None can be identified from the abstract alone, but the complete absence of methods and results means that the technical soundness of the simulations cannot be assessed. The core mechanistic claims are unverifiable from the supplied material.
- **Assessment against Nature-style criteria** Originality: The proposed combination of direct and indirect salt effects is not entirely novel, but the specific application to A1-LCD and the predictive classification scheme add an original element. Scientific importance: The topic is of significant interest to the phase separation community, and a robust mechanistic understanding would be valuable. Interdisciplinary readership: The work could appeal to biophysicists, biochemists, and computational biologists, but the abstract is written in a specialized manner that may limit broader accessibility. Technical soundness: Cannot be assessed from the abstract; no methods or data are provided. Readability for nonspecialists: The abstract is reasonably clear but uses field-specific terminology without sufficient context.
- **Recommendation posture** Currently not established from the provided evidence. The abstract presents a plausible framework, but the absence of any supporting data or methods means that the claims cannot be evaluated. A full manuscript with detailed simulation results, validation, and a rigorous derivation of the classification scheme would be required to assess the work properly.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence sufficiency
- **Claim pointer** The authors claim that ions play two direct roles in driving A1-LCD condensation, namely charge neutralization and ion-mediated bridging, and that at high concentrations NaCl indirectly strengthens π-type interactions by drawing water away from interaction partners.
- **Evidence pointer** Abstract only; location not provided
- **Concern** The abstract states these mechanistic conclusions without presenting any quantitative data, such as radial distribution functions, coordination numbers, binding free energies, or interaction energy decompositions. No figures or tables are referenced, and no statistical measures are given.
- **Why it matters** The central claims of the paper rest on molecular-level interpretations of simulation trajectories. Without access to the underlying data and analysis, it is impossible to verify that the proposed mechanisms are actually supported by the simulations rather than being speculative interpretations.
- **Resolution test** The full manuscript must provide quantitative evidence for each claimed mechanism, including but not limited to ion-protein coordination numbers, charge neutralization calculations, bridging frequency analyses, and solvent-accessible surface area or water density measurements around interaction partners.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Claim validation
- **Claim pointer** The authors state that "four classes of salt dependence of IDP phase separation can be predicted from amino-acid composition."
- **Evidence pointer** Abstract only; location not provided
- **Concern** This predictive claim is presented as a key outcome, but the abstract provides no derivation, no definition of the four classes, no criteria for classification, and no validation against experimental or simulation data.
- **Why it matters** A predictive framework is only valuable if its basis is transparent and its accuracy is demonstrated. As stated, the claim is unfalsifiable from the abstract and could be an overreach if the underlying analysis is not rigorous.
- **Resolution test** The manuscript must define the four classes explicitly, show how they derive from amino-acid composition, and test the predictions against a set of known IDPs with experimentally characterized salt dependence.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical reproducibility
- **Claim pointer** The authors report all-atom molecular dynamics simulations of multiple A1-LCD chains at NaCl concentrations from 50 to 1000 mM.
- **Evidence pointer** Abstract only; location not provided
- **Concern** No simulation details are provided, including the number of chains, box size, force field, water model, ion parameters, temperature, pressure coupling, simulation length, equilibration protocol, or replica handling. Without these, the simulations cannot be reproduced or evaluated for convergence and sampling adequacy.
- **Why it matters** All-atom simulations of multi-chain systems are computationally demanding and prone to sampling limitations. The validity of the mechanistic conclusions depends critically on whether the simulations were sufficiently long and well-converged to capture equilibrium behavior.
- **Resolution test** The methods section must provide complete simulation parameters and demonstrate convergence through appropriate metrics, such as block averaging, multiple independent runs, or assessment of system-size effects.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Definition of "first-shell"
- **Evidence pointer** Abstract; location not provided
- **Issue** The term "first-shell" is used without definition, which may be ambiguous for readers unfamiliar with ion coordination chemistry.
- **Required correction** Define the first-shell criterion, for example, as ions within a specific distance cutoff from protein atoms, and state the cutoff value.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Precision
- **Affected element** Phrase "drawing water away from the interaction partners"
- **Evidence pointer** Abstract; location not provided
- **Issue** This phrase is vague and could be interpreted in multiple ways, such as a reduction in local water density or a change in water dynamics.
- **Required correction** Provide a more precise description of the indirect effect, such as a quantified decrease in water occupancy or hydration shell thickness around specific residue types.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Comparison with experimental data
- **Evidence pointer** Abstract; location not provided
- **Issue** The abstract does not mention any comparison with experimental observations of A1-LCD phase separation, which would strengthen the relevance of the simulation findings.
- **Required correction** State whether the simulation results are consistent with experimental phase diagrams or other quantitative measurements, and if so, include a brief description of the comparison.

## Risk / unsupported claims
- The claim that ions neutralize the net charge of A1-LCD by an excess of bound Cl- over Na+ is unsupported without quantitative binding data.
- The claim that ions bridge between A1-LCD chains is unsupported without evidence of stable ion-mediated contacts.
- The claim that NaCl strengthens π-π, cation-π, and amino-π interactions by drawing water away is unsupported without solvent analysis.
- The prediction of four classes of salt dependence from amino-acid composition is entirely unsubstantiated in the abstract.
- The overall mechanistic model is presented as established fact, but no data are available to evaluate its validity.