## Review setup
- **Input scope** Full manuscript text including main text, appendices, and figure descriptions
- **Assessment boundary** Theoretical and computational study of programmable biomolecular condensate self-assembly using mean-field models and lattice simulations
- **Shared manuscript claim summary** The authors develop a minimal model to show that the number of distinct biomolecular condensates that can be reliably self-assembled grows superlinearly with the number of species when condensates share components, and that this capacity can be predicted without detailed knowledge of pairwise interactions
- **Visible evidence base** Main text equations, appendices A-E, figure descriptions (Figures 1-4), simulation methodology descriptions
- **Missing materials affecting confidence** Actual figures and numerical data tables are not provided; only figure captions and descriptions are available

## Reviewer
- **Overall assessment** This manuscript presents a theoretically elegant and computationally supported framework for understanding the combinatorial capacity of multicomponent biomolecular condensates. The central claim, that shared components enable superlinear scaling of assemblable condensate number with species count, is well-motivated and supported by both analytical arguments and simulation evidence. The work bridges statistical mechanics, graph theory, and cell biology in a way that should interest a broad readership. However, the manuscript would benefit from clearer presentation of the key equations and more explicit discussion of biological relevance and limitations.

- **Who would be interested in the results, and why** Researchers studying biomolecular condensates and phase separation in cell biology, particularly those interested in the physical principles governing spatial organization in the nucleus and cytoplasm. Also relevant to the broader soft matter and statistical physics community working on programmable self-assembly, and to synthetic biologists interested in designing multicomponent compartmentalization systems.

- **Major strengths** The inverse-problem formulation is a creative and powerful approach to a question that has largely been addressed through forward modeling. The graph-theoretical scaling prediction provides a simple, testable rule that does not require detailed interaction parameters. The combination of mean-field theory, convex optimization, and lattice simulations provides a multi-pronged validation strategy. The demonstration that condensate number can exceed species number is conceptually striking and has clear biological implications.

- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors claim that the number of distinct condensates that can be reliably assembled grows superlinearly with the number of species, scaling as n* ~ N^gamma with gamma = (2M-1)/(M+1)
- **Evidence pointer** Main text, Figure 2b,c; Appendix C
- **Concern** The graph-theoretical scaling argument assumes that the only obstruction to encoding is the presence of off-target cliques of size M+1. However, the stability condition (third constraint) involves the full Hessian of the free energy, and it is not demonstrated that the random matrix approximation used to derive the QP objective captures all relevant instabilities. The authors state that the QP and SDP solutions give the same threshold, but the argument for why this must be the case is not fully developed.
- **Why it matters** If the QP approximation misses certain instability modes, the predicted scaling could be an overestimate. The central quantitative claim of the paper depends on the validity of this approximation.
- **Resolution test** Provide a more rigorous argument for why the QP objective captures the relevant stability condition, or present numerical evidence that the minimum eigenvalue of the full Hessian is well-approximated by the random matrix estimate across a range of N, M, and n values.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** No
- **Axis** Scientific importance
- **Claim pointer** The authors claim that the scaling behavior predicted by the mean-field model holds for both stability and growth simulations in the lattice model, and that the empirical values converge as the number of components increases
- **Evidence pointer** Main text, Figure 3c
- **Concern** The convergence of the lattice model results to the mean-field prediction is stated but the quantitative degree of agreement is not presented. The manuscript notes that n1/2 values are "generally lower" for the lattice model, but does not specify by how much or how this discrepancy depends on N and M. Without this information, it is difficult to assess whether the mean-field prediction is quantitatively reliable for finite-range interaction systems.
- **Why it matters** The biological relevance of the results depends on whether the mean-field scaling is a good approximation for realistic systems with finite interaction ranges. If the discrepancy is large for biologically relevant parameters, the practical utility of the prediction is limited.
- **Resolution test** Present the numerical values of n1/2 for the lattice model alongside the mean-field predictions for several N and M combinations, and quantify the convergence as N increases.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Interdisciplinary readership
- **Claim pointer** The authors state that the results "highlight the vast possibilities of programmable self-assembly in systems with thousands of components" and suggest implications for transcriptional control
- **Evidence pointer** Main text, concluding paragraphs
- **Concern** The biological implications are stated but not developed. The connection to transcriptional condensates is mentioned but the specific predictions that could be tested experimentally are not articulated. For a readership that includes cell biologists, the manuscript would benefit from a more explicit discussion of what experimental observations would confirm or refute the model's predictions.
- **Why it matters** The interdisciplinary impact of the work depends on its accessibility and relevance to experimental biologists. Without clear experimental predictions, the work may be seen as purely theoretical.
- **Resolution test** Add a paragraph in the discussion that translates the scaling prediction into specific experimental predictions, such as expected relationships between condensate number, component number, and interaction specificity in engineered or natural systems.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Readability for nonspecialists
- **Affected element** Main text, equations (1)-(3)
- **Evidence pointer** Main text, equations section
- **Issue** The key equations are presented without derivation or intuitive explanation. A reader unfamiliar with regular solution models or grand potential formalism may struggle to understand the physical content of the constraints.
- **Required correction** Provide brief physical interpretations of each constraint in the main text, or move some derivational detail to the appendices and add a short paragraph explaining the physical meaning of the three conditions.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Technical soundness
- **Affected element** Appendix B, choice of zeta and kappa
- **Evidence pointer** Appendix B
- **Issue** The values of zeta = 10^-3 and kappa = 10^-5 are stated but the sensitivity of the results to these choices is not discussed. The authors note that zeta closer to unity increases n1/2 for SDP solutions, but the robustness of the scaling exponent to these parameter choices is not examined.
- **Required correction** Add a brief discussion of how the results depend on zeta and kappa, or state that the scaling behavior is robust to reasonable variations in these parameters.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Scientific importance
- **Affected element** Discussion of non-equilibrium nature
- **Evidence pointer** Main text, final paragraph before acknowledgments
- **Issue** The statement that the results are "not at odds with the Gibbs Phase Rule" because the system is inherently non-equilibrium is interesting but underdeveloped. The relationship between the finite driving force, the timescale of condensate assembly, and the practical relevance of the predicted scaling is not explored.
- **Required correction** Expand this discussion to clarify what is meant by "inherently non-equilibrium" in this context and how the finite driving force affects the practical timescales over which the predicted condensate configurations can be maintained.

- **Technical failings that need to be addressed before the case is established** The primary technical concern is the validity of the QP approximation for the stability condition (R1-M1). The manuscript should provide a more rigorous justification or additional numerical evidence that the QP objective correctly identifies the threshold for successful encoding. Additionally, the quantitative agreement between mean-field predictions and lattice simulations should be presented more explicitly.

- **Assessment against Nature-style criteria** 
  - Originality: High. The inverse-problem approach to condensate design and the graph-theoretical scaling prediction are novel contributions that go beyond existing forward-modeling studies.
  - Scientific importance: High. The result that shared components enable superlinear scaling of condensate number has implications for understanding the complexity of intracellular organization and for synthetic biology.
  - Interdisciplinary readership: Moderate to high. The work bridges statistical physics, computational biology, and cell biology, but the presentation is currently more accessible to physicists than to biologists.
  - Technical soundness: Moderate. The mean-field theory and optimization framework are sound, but the QP approximation requires further justification, and the quantitative agreement with lattice simulations needs to be documented more fully.
  - Readability for nonspecialists: Moderate. The main text is concise but assumes familiarity with statistical mechanics formalism. The biological motivation is clear but the implications could be developed further.

- **Recommendation posture** Supportive if technical concerns are resolved. The central idea is compelling and the results are likely to be of broad interest, but the manuscript needs to address the QP approximation validity and provide more quantitative detail on the simulation results before the case is fully established.