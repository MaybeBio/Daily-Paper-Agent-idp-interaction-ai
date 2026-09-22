## Review setup
- **Input scope** Full manuscript text including abstract, main text, methods, and figure legends as provided.
- **Assessment boundary** Scientific content, technical soundness, and internal consistency of the presented claims based solely on the supplied material. No external literature verification or data reanalysis performed.
- **Shared manuscript claim summary** The authors present a synthetic phase separation system (synDrops) to study how the intracellular environment affects mesoscale molecular assembly. They claim that macromolecular crowding promotes droplet nucleation but inhibits growth, and that ATP-dependent actomyosin dynamics promote droplet growth by reducing cytoplasmic confinement and elasticity.
- **Visible evidence base** Main text figures 1-4 (referenced but not shown), Extended Data figures 1-4 (referenced but not shown), supplementary movies (referenced), methods section, and figure legends embedded in text.
- **Missing materials affecting confidence** Actual figure images, numerical data values, statistical analyses, simulation parameter tables, and supplementary materials were not provided. This limits quantitative verification of all claims.

## Reviewer
- **Overall assessment** This manuscript addresses an important question in cell biology: how the complex intracellular environment influences biomolecular condensate formation. The synDrops system is thoughtfully designed with well-defined geometry and inducible assembly, enabling both experimental and computational analysis. The combination of in vivo experiments in yeast and mammalian cells with agent-based simulations is a strength. However, the manuscript as presented has several technical concerns that need to be addressed, particularly regarding the interpretation of crowding effects, the specificity of the actomyosin contribution, and the quantitative rigor of some analyses. The core claims are plausible but not fully established from the provided evidence.

- **Who would be interested in the results, and why** Researchers studying biomolecular condensates, phase separation, intracellular organization, and cytoplasmic biophysics would find this work of interest. The synDrops system provides a useful tool for probing how physical properties of the cytoplasm affect assembly processes. The findings on crowding and active matter effects have implications for understanding endogenous condensate regulation and could inform biophysical models of intracellular organization.

- **Major strengths** The synDrops system is a well-designed synthetic tool with clear advantages for quantitative analysis. The combination of experimental and computational approaches is powerful. The study addresses an important gap in understanding how the complex intracellular environment, beyond simple dilute solution conditions, affects condensate formation. The findings on opposing effects of crowding on nucleation versus growth are conceptually interesting.

- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness of experimental manipulation
- **Claim pointer** The authors claim that osmotic compression increases macromolecular crowding and that this is the primary cause of the observed changes in synDrop nucleation and growth.
- **Evidence pointer** Figure 2a-b, Extended Data Figure 2a-d, Methods section "Drug treatment"
- **Concern** Osmotic compression is a pleiotropic perturbation that affects cell volume, ionic strength, protein concentration, and potentially signaling pathways. The authors attempt to control for protein concentration using expression level quartiles, but this does not fully separate crowding effects from other consequences of osmotic stress. The claim that increased nucleation is specifically due to macromolecular crowding requires more direct manipulation of crowding.
- **Why it matters** The central conclusion that crowding promotes nucleation but inhibits growth depends on the interpretation of the osmotic compression experiments. If other factors contribute significantly, the mechanistic model would need revision.
- **Resolution test** Provide experiments with alternative crowding manipulations (e.g., acute overexpression of inert proteins, or genetic perturbations of ribosome levels) that do not involve osmotic stress. Alternatively, demonstrate that the observed effects scale quantitatively with measured crowding levels across multiple independent perturbations.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Causal attribution of actomyosin contribution
- **Claim pointer** The authors conclude that actomyosin dynamics is the dominant ATP-dependent activity that promotes synDrop growth by reducing confinement and elasticity.
- **Evidence pointer** Figure 3c-e, Figure 4d-e, Methods section "Drug treatment"
- **Concern** The JLY drug cocktail inhibits actin polymerization, depolymerization, and myosin II activity simultaneously. This broad inhibition cannot specifically attribute the observed effects to actomyosin contractility versus other actin-dependent processes such as cytoplasmic streaming, vesicle trafficking, or structural support. Additionally, ATP depletion affects all ATP-dependent processes, not just actomyosin.
- **Why it matters** The mechanistic model proposes a specific role for actomyosin contractility in fluidizing the cytoplasm. Without more specific perturbations, alternative explanations remain viable.
- **Resolution test** Use more specific inhibitors (e.g., blebbistatin for myosin II alone, or latrunculin alone) and rescue experiments with constitutively active myosin. Alternatively, measure actin dynamics directly and correlate with synDrop growth.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Quantitative rigor of simulation-experiment comparison
- **Claim pointer** The authors state that simulations with 30-35% crowder volume fraction reproduce experimental observations, and that 50% crowding mimics osmotically compressed cells.
- **Evidence pointer** Figure 2j-l, Extended Data Figure 3a-e, Methods section "Simulations set up using HOOMD-blue"
- **Concern** The mapping between simulation crowder volume fraction and cellular conditions is not quantitatively justified. The claim that 30-35% mimics normal cytoplasm and 50% mimics compressed cells requires calibration against experimental measurements. Additionally, the simulation parameters (binding rates, interaction strengths) are not shown in the provided material, making it impossible to assess whether the simulations are predictive or fitted to match experiments.
- **Why it matters** The simulation results are used to support mechanistic interpretations. If the simulation parameters are not constrained by independent measurements, the conclusions drawn from them are weakened.
- **Resolution test** Provide the simulation parameter tables and a clear calibration procedure linking crowder volume fraction to cellular crowding levels. Show sensitivity analyses demonstrating that conclusions are robust to reasonable parameter variations.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Generalizability of findings
- **Claim pointer** The authors suggest their findings on crowding and active matter effects on synDrops may apply to endogenous condensates.
- **Evidence pointer** Discussion section
- **Concern** The synDrops system uses designed proteins with specific valency and interaction strengths. Endogenous condensates vary widely in their composition, interaction mechanisms, and size scales. The extent to which these findings generalize to other systems is unclear.
- **Why it matters** The broader significance of the work depends on its relevance to endogenous condensate biology.
- **Resolution test** Discuss specific predictions for endogenous systems that could be tested, or provide preliminary data on at least one endogenous condensate system.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity of presentation
- **Affected element** Figure 2h-i phase diagram analysis
- **Evidence pointer** Figure 2h-i, Methods section "Image analyses"
- **Issue** The phase diagram analysis in HeLa cells relies on highly variable transfection expression levels. The criteria for defining the phase boundary and the statistical treatment of this heterogeneity are not fully described.
- **Required correction** Provide a clearer description of how the phase boundary was determined and how variability was handled statistically.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Technical detail
- **Affected element** Angle correlation analysis
- **Evidence pointer** Figure 4a, Methods section "Image analyses"
- **Issue** The angle correlation function is described but the specific calculation method, including how angles are defined and how ensemble averaging is performed, is not fully detailed.
- **Required correction** Provide a more complete description of the angle correlation calculation, including any normalization procedures.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Interpretation
- **Affected element** Discussion of crowding effects on nucleation
- **Evidence pointer** Figure 2n, Extended Data Figure 3f-g
- **Issue** The claim that crowding reduces effective Kd by increasing kon is based on simulations with simplified monovalent components. The relevance of this simplified system to the full multivalent synDrops system is not discussed.
- **Required correction** Add a brief discussion of how the simplified simulation relates to the full system and any limitations of this approach.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Methods section
- **Evidence pointer** Methods section "Simulations set up using HOOMD-blue" and "Simulations set up using custom-developed Java program"
- **Issue** The parameter tables for both simulation platforms are referenced but not included in the provided material.
- **Required correction** Ensure the parameter tables are included in the final manuscript.

- **Technical failings that need to be addressed before the case is established** R1-M1, R1-M2, R1-M3. The manuscript cannot be fully evaluated without addressing these concerns. The core claims about crowding and actomyosin contributions require more rigorous causal evidence.

- **Assessment against Nature-style criteria** 
  - Originality: The synDrops system is a novel tool, and the combination of crowding and active matter effects on condensate assembly is a fresh perspective. However, individual components (crowding effects on phase separation, actomyosin effects on cytoplasmic properties) have been studied separately.
  - Scientific importance: Understanding how the complex intracellular environment affects condensate formation is important for cell biology and biophysics. The findings could have broad implications.
  - Interdisciplinary readership: The work bridges cell biology, biophysics, and computational modeling, which would appeal to a broad readership.
  - Technical soundness: The experimental design is thoughtful, but the causal attribution of specific mechanisms (crowding vs. other osmotic effects; actomyosin vs. other ATP-dependent processes) needs strengthening. The simulation-experiment comparison lacks quantitative rigor as presented.
  - Readability for nonspecialists: The manuscript is generally well-written and accessible, though some biophysical concepts may require background knowledge.

- **Recommendation posture** Supportive if technical concerns are resolved. The manuscript addresses an important question with a well-designed system, but the current evidence does not fully establish the specific mechanistic claims. Addressing the concerns about causal attribution and quantitative rigor would significantly strengthen the case.

## Risk / unsupported claims
- The claim that macromolecular crowding specifically promotes nucleation (as opposed to other osmotic stress effects) is not fully supported by the experimental design.
- The claim that actomyosin dynamics is the dominant ATP-dependent activity promoting synDrop growth is not established given the broad nature of the perturbations used.
- The quantitative mapping between simulation crowder volume fractions and cellular conditions is not provided or justified.
- The generalizability of findings to endogenous condensate systems is speculative without additional evidence.
- The claim that ATP depletion increases cytoplasmic elasticity is based on indirect measurements and requires more direct validation.