## Review setup
- **Input scope** Abstract only
- **Assessment boundary** Claims and evidence presented in the abstract; no access to full manuscript, figures, tables, or supplementary materials
- **Shared manuscript claim summary** The authors report that simulation technique and force field parameter choice affect predicted secondary structure properties of disordered proteins, but not of an ordered protein. They compare molecular dynamics simulations without parallel tempering using various force field parameter sets and temperature-replica exchange molecular dynamics simulations for one ordered protein (GB3) and two disordered proteins (amyloid-β(1–40) and α-synuclein) in water. They conclude that results for the ordered protein are consistent across techniques, whereas results for disordered proteins are not, and call for further development in simulation techniques and force fields for disordered proteins.
- **Visible evidence base** Abstract text only; no quantitative data, simulation details, or methodological descriptions are provided
- **Missing materials affecting confidence** Full manuscript, simulation protocols, force field parameter sets used, system preparation details, simulation lengths, convergence criteria, secondary structure assignment methods, statistical analyses, and all figures and tables

## Reviewer
- **Overall assessment** The abstract presents a potentially important observation regarding the sensitivity of secondary structure predictions for disordered proteins to simulation methodology. However, the current abstract provides insufficient detail to evaluate the robustness of the claims. The central conclusion, that temperature-replica exchange molecular dynamics and standard molecular dynamics yield similar results for an ordered protein but not for disordered proteins, is plausible but not substantiated with quantitative evidence in the provided material. The call for consensus development is reasonable but lacks specificity. The work may interest computational biophysicists and those studying intrinsically disordered proteins, but the evidence base as presented is too limited to assess technical soundness or generalizability.
- **Who would be interested in the results, and why** Computational biophysicists and molecular dynamics practitioners studying protein secondary structure, particularly those working with intrinsically disordered proteins, would be interested because the findings address a known challenge in the field, namely the sensitivity of disordered protein simulations to methodological choices. Researchers developing or benchmarking force fields and enhanced sampling techniques would also find the comparative assessment relevant to their work.
- **Major strengths** The abstract addresses a timely and practically important question in biomolecular simulation. The choice of model systems, including one ordered and two disordered proteins, provides a reasonable comparative framework. The explicit comparison between standard molecular dynamics and temperature-replica exchange molecular dynamics across multiple force field parameter sets is a useful design.
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
  Originality: The observation that disordered protein secondary structure predictions vary with simulation technique and force field is not entirely new, as the authors themselves note prior work, but the systematic comparison across techniques and force fields for both ordered and disordered proteins adds a comparative element. The originality is moderate.  
  Scientific importance: The issue of methodological sensitivity in disordered protein simulations is important for the field, and a robust demonstration could influence best practices. However, the abstract does not provide enough evidence to establish the importance of the specific findings.  
  Interdisciplinary readership: The topic is primarily of interest to computational biophysicists and structural biologists; broader interdisciplinary appeal is limited unless the findings are linked to biological or clinical implications, which are not mentioned.  
  Technical soundness: Cannot be assessed from the abstract alone. No simulation details, convergence metrics, or statistical validation are provided.  
  Readability for nonspecialists: The abstract is written in a clear and accessible style, with minimal jargon, and the main message is understandable to a broad scientific audience.
- **Recommendation posture** Currently not established from the provided evidence. The abstract presents a plausible claim, but the lack of quantitative results and methodological detail prevents a supportive recommendation. A revised version with substantive evidence would be needed for further consideration.

### Major Concerns

- **Concern ID** R1-M1  
- **Severity** Major  
- **Blocking** Yes  
- **Axis** Evidence sufficiency  
- **Claim pointer** The authors claim that temperature-replica exchange molecular dynamics simulations and molecular dynamics simulations without special sampling techniques yield similar results for the ordered GB3 protein, whereas such agreement could not be obtained for disordered proteins.  
- **Evidence pointer** Abstract only; location not provided  
- **Concern** The abstract provides no quantitative data, such as secondary structure percentages, root-mean-square fluctuations, or similarity metrics, to support the claim of agreement for GB3 and disagreement for the disordered proteins. No statistical measures are reported, and it is unclear how "similar" or "not similar" was defined.  
- **Why it matters** The central conclusion of the manuscript rests on a comparative claim that requires quantitative support. Without defined criteria for agreement and reported values, the claim cannot be evaluated or reproduced.  
- **Resolution test** Provide quantitative secondary structure metrics for each system and simulation condition, with statistical comparisons and defined thresholds for agreement or disagreement.

- **Concern ID** R1-M2  
- **Severity** Major  
- **Blocking** Yes  
- **Axis** Methodological transparency  
- **Claim pointer** The authors state that they used molecular dynamics simulations without parallel tempering techniques using various force field parameter sets and temperature-replica exchange molecular dynamics simulations.  
- **Evidence pointer** Abstract only; location not provided  
- **Concern** The abstract does not specify which force field parameter sets were used, how many simulations were performed, the simulation lengths, the temperature ranges for replica exchange, the water model, or the secondary structure assignment method. These details are essential for assessing the validity and generalizability of the findings.  
- **Why it matters** Simulation outcomes are highly sensitive to these parameters. Without this information, the reader cannot determine whether the observed differences are due to the technique, the force field, or other uncontrolled variables.  
- **Resolution test** Include a complete description of simulation protocols, force fields, system setup, and analysis methods in the full manuscript, and summarize key parameters in the abstract or a methods summary.

- **Concern ID** R1-M3  
- **Severity** Major  
- **Blocking** Yes  
- **Axis** Generalizability  
- **Claim pointer** The authors conclude that a consensus has to be reached via further development in computer simulation technique and force field parameter sets for disordered proteins.  
- **Evidence pointer** Abstract only; location not provided  
- **Concern** The conclusion is based on two disordered proteins, amyloid-β(1–40) and α-synuclein, and one ordered protein, GB3. The abstract does not discuss whether these systems are representative of broader classes of disordered and ordered proteins, nor does it address potential confounding factors such as protein length, sequence composition, or aggregation propensity.  
- **Why it matters** A general conclusion about the need for consensus in disordered protein simulations requires evidence that the observed behavior is not specific to the chosen test systems.  
- **Resolution test** Discuss the representativeness of the chosen proteins, and ideally include additional disordered and ordered proteins to test the generality of the findings, or clearly state the limitations of the current scope.

### Minor Comments

- **Concern ID** R1-m1  
- **Severity** Minor  
- **Axis** Clarity  
- **Affected element** Abstract wording  
- **Evidence pointer** Abstract, first sentence  
- **Issue** The phrase "identifying the secondary structure properties" is vague. It is unclear whether the authors refer to secondary structure content, specific structural motifs, or conformational ensembles.  
- **Required correction** Specify what secondary structure properties are being measured, such as helix and sheet content, or conformational populations.

- **Concern ID** R1-m2  
- **Severity** Minor  
- **Axis** Context  
- **Affected element** Abstract background  
- **Evidence pointer** Abstract, second sentence  
- **Issue** The authors mention "our recent studies" without providing citations or context. This makes it difficult for the reader to understand the prior work that motivated this study.  
- **Required correction** Add citations to the relevant prior studies and briefly state what those studies found.

- **Concern ID** R1-m3  
- **Severity** Minor  
- **Axis** Terminology  
- **Affected element** Abstract, last sentence  
- **Evidence pointer** Abstract, final sentence  
- **Issue** The term "consensus" is used without definition. It is unclear whether the authors mean a consensus on force field parameters, simulation protocols, or both.  
- **Required correction** Clarify what type of consensus is needed and in what form, such as standardized benchmarking or community-endorsed force field parameters.

## Risk / unsupported claims
- The claim that temperature-replica exchange molecular dynamics and standard molecular dynamics yield similar results for GB3 is unsupported by quantitative evidence in the abstract.
- The claim that agreement between simulation techniques could not be obtained for disordered proteins is unsupported by quantitative evidence in the abstract.
- The general conclusion that further development in simulation techniques and force fields is needed for disordered proteins is not substantiated with specific evidence of failure modes or limitations.
- The representativeness of the chosen proteins for broader classes of ordered and disordered proteins is not addressed and cannot be assessed from the abstract.