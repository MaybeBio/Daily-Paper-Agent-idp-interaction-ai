## Review setup
- **Input scope** Full manuscript text (abstract, introduction, results, discussion, supplementary information description)
- **Assessment boundary** Scientific content, methodological soundness, claims versus evidence, and presentation quality as presented in the provided text. No external literature verification performed.
- **Shared manuscript claim summary** The authors develop a multiscale computational approach combining atomistic simulations and coarse-grained modelling to show that accumulation of inter-protein β-sheets in RNA-binding protein condensates (FUS, hnRNPA1) increases viscosity and can drive liquid-to-gel transitions, while high RNA concentrations decelerate this process.
- **Visible evidence base** Results sections describing atomistic PMF calculations, coarse-grained phase diagrams, viscoelastic property calculations, network connectivity analyses, and kinetic modelling. Figures referenced: Figures 1–5, Supplementary Figures 1 and 3, Supplementary Movies 1 and 2.
- **Missing materials affecting confidence** Supplementary Methods, Supplementary Figures 1–3, Supplementary Movies, Reporting Summary, and all methodological details referenced as "Supplementary" were not provided. This limits verification of simulation protocols, parameter choices, and analysis details.

## Reviewer
- **Overall assessment** This manuscript presents a timely and potentially impactful multiscale computational study addressing a central question in the biology of biomolecular condensates: how structural transitions (β-sheet formation) transform material properties, and how RNA modulates this process. The integration of atomistic and coarse-grained approaches is conceptually appealing and the qualitative predictions align with experimental observations. However, the manuscript as presented has several significant issues that must be addressed. The central claim that "RNA can prevent" the structural transitions is not convincingly supported by the evidence shown, as the reported effect is a deceleration rather than prevention. The kinetic model appears oversimplified, and the lack of quantitative comparison to experimental timescales or material property measurements weakens the translational relevance. The network connectivity analysis is described but its quantitative output is not clearly presented. The claim regarding conservation of critical parameters during ageing requires more careful justification given the non-equilibrium nature of the model. The writing is generally clear but some methodological details are only available in supplementary material, which was not assessable.

- **Who would be interested in the results, and why** Researchers in the fields of biomolecular condensates, phase separation, neurodegeneration (ALS, FTD), and computational biophysics would find this work relevant. The study addresses a fundamental question about the molecular mechanisms underlying condensate ageing and offers a computational framework that could be adapted by others. The potential protective role of RNA against pathological solidification is of broad interest to cell biologists and neurobiologists studying stress granules and RNA-binding protein pathologies.

- **Major strengths**  
  1. The multiscale approach bridging atomistic simulations with coarse-grained modelling is innovative and addresses a genuine gap in the field.  
  2. The study tackles a biologically and clinically important question: what drives liquid-to-solid transitions in condensates and what can prevent them.  
  3. The dynamical algorithm for modelling time-dependent β-sheet accumulation is a novel methodological contribution.  
  4. The comparison between FUS and hnRNPA1, two disease-relevant proteins, adds biological significance.  
  5. The inclusion of RNA as a modulating factor addresses a key aspect of the physiological environment of these condensates.

- **Major Concerns**

- **Concern ID** R1-M1  
- **Severity** Major  
- **Blocking** Yes  
- **Axis** Claim-evidence alignment  
- **Claim pointer** The title and abstract state that RNA "can prevent" the structural transitions that drive condensate ageing.  
- **Evidence pointer** Results section "Emergence of inter-protein β-sheets during ageing increases droplet viscosity", Figures 4c and 5a  
- **Concern** The data presented show a deceleration of β-sheet accumulation kinetics at high RNA concentrations, not prevention. The kinetic constant decreases with increasing RNA concentration, but the process still proceeds. The term "prevent" implies cessation or complete inhibition, which is not demonstrated. The authors themselves use "decelerate" in the Discussion, which is inconsistent with the title and abstract.  
- **Why it matters** The title and abstract are the most visible parts of the manuscript and set expectations for the findings. Overstating the effect of RNA misrepresents the results and could mislead readers about the protective capacity of RNA. This is a fundamental accuracy issue.  
- **Resolution test** Either provide evidence that at sufficiently high RNA concentrations the β-sheet accumulation rate approaches zero (complete prevention), or revise the title, abstract, and relevant text to accurately state that RNA "decelerates" or "slows" the structural transitions.

- **Concern ID** R1-M2  
- **Severity** Major  
- **Blocking** Yes  
- **Axis** Technical soundness  
- **Claim pointer** The authors claim that their dynamical algorithm models the non-equilibrium process of condensate ageing and that the critical parameters of the phase diagrams are conserved during ageing.  
- **Evidence pointer** Results section "Time-dependent modulation of protein phase diagrams during ageing", Figures 1d and 2a  
- **Concern** The manuscript states that phase diagrams are not affected by ageing, yet the model introduces non-conservative, time-dependent changes to interaction strengths. It is not clear how a system with continuously changing interaction parameters can be meaningfully compared to equilibrium phase diagrams. The criteria for determining phase coexistence in a non-equilibrium system are not described in the main text. The claim of conserved critical parameters requires a rigorous justification that is not provided.  
- **Why it matters** The phase diagram is a central result used to argue that ageing affects material properties without changing thermodynamic stability. If this claim is not rigorously supported, the interpretation of all subsequent results is compromised.  
- **Resolution test** Provide a clear description of how phase coexistence is determined in the non-equilibrium simulations, and demonstrate that the critical parameters are indeed invariant under the ageing protocol. Alternatively, soften the claim to reflect the actual methodology.

- **Concern ID** R1-M3  
- **Severity** Major  
- **Blocking** Yes  
- **Axis** Technical soundness  
- **Claim pointer** The authors state that the network of molecular connections within condensates is "drastically altered" upon ageing, culminating in gelation when the network of strong β-sheets fully percolates.  
- **Evidence pointer** Results section "Liquid-like and gel-like aged condensates present drastic differences in their networks of inter-molecular connections", Figure 3c  
- **Concern** The network connectivity analysis is described qualitatively. The modified primitive path analysis is mentioned, but no quantitative metrics are presented in the main text. The claim of "drastic differences" is not supported by any numerical comparison between liquid-like and gel-like networks. The percolation threshold is not defined or quantified.  
- **Why it matters** The network analysis is central to the mechanistic explanation of gelation. Without quantitative evidence, the claim that percolation of β-sheet networks drives the liquid-to-gel transition remains speculative.  
- **Resolution test** Provide quantitative measures of network connectivity (e.g., percolation probability, cluster size distributions, number of elastically active strands) for both liquid-like and gel-like states, and demonstrate a clear difference that correlates with the observed rheological properties.

- **Concern ID** R1-M4  
- **Severity** Major  
- **Blocking** No  
- **Axis** Scientific importance  
- **Claim pointer** The authors suggest that their findings "suggest a potential mechanism to slow such transitions down" and that high RNA concentrations may prevent pathological liquid-to-solid transitions.  
- **Evidence pointer** Abstract, Discussion  
- **Concern** The physiological relevance of the RNA concentrations used in the simulations is not discussed. The authors do not compare their simulated RNA concentrations to those found in cells or in in vitro experiments. Without this context, it is unclear whether the protective effect of RNA is physiologically achievable.  
- **Why it matters** The translational relevance of the findings depends on whether the RNA concentrations that decelerate ageing are within a biologically meaningful range. If the required concentrations are supra-physiological, the conclusions have limited relevance to disease.  
- **Resolution test** Add a discussion of the physiological range of RNA concentrations in condensates and compare to the concentrations used in the simulations. If the concentrations are not physiological, temper the claims about disease relevance.

- **Concern ID** R1-M5  
- **Severity** Major  
- **Blocking** No  
- **Axis** Technical soundness  
- **Claim pointer** The authors use a second-order kinetic model to extract rate constants for β-sheet formation and claim that RNA reduces these constants.  
- **Evidence pointer** Results section "RNA decelerates the rate of accumulation of inter-protein β-sheets", Figures 4c and 5a–b  
- **Concern** The kinetic model is described as including two forward reactions and one backward reaction, but the details of the fitting procedure, the quality of the fits, and the uncertainty in the extracted rate constants are not presented in the main text. The dashed lines in Figures 4c and 5a are described as fits, but no goodness-of-fit metrics are provided.  
- **Why it matters** The kinetic analysis is used to quantify the effect of RNA on ageing. If the fitting procedure is not transparent or the fits are poor, the quantitative conclusions are unreliable.  
- **Resolution test** Provide details of the kinetic fitting procedure, including the equations used, the fitting algorithm, and the uncertainties in the extracted parameters. Show the fits alongside the data with residual analysis.

- **Minor Comments**

- **Concern ID** R1-m1  
- **Severity** Minor  
- **Axis** Readability  
- **Affected element** Introduction  
- **Evidence pointer** Introduction, first paragraph  
- **Issue** The introduction is dense and covers a wide range of concepts (LLPS, condensate ageing, structural transitions, disease relevance) in a compressed manner. Some terms are introduced without sufficient context for a non-specialist reader.  
- **Required correction** Consider expanding the introduction to provide more background on condensate material properties and why viscosity is a key functional parameter. Define terms such as "LARKS" and "percolation" when first used.

- **Concern ID** R1-m2  
- **Severity** Minor  
- **Axis** Technical soundness  
- **Affected element** Results, atomistic simulations  
- **Evidence pointer** Results section "Inter-peptide β-sheet clusters critically enhance protein binding"  
- **Issue** The description of the atomistic simulations is brief. The choice of the a99SB-disp force field and the justification for using it are not discussed. The comparison with CHARMM36m results from a previous study is mentioned but not shown.  
- **Required correction** Provide a brief justification for the force field choice and include the comparison with CHARMM36m results either in the main text or as a supplementary figure.

- **Concern ID** R1-m3  
- **Severity** Minor  
- **Axis** Readability  
- **Affected element** Results, viscoelasticity section  
- **Evidence pointer** Results section "Emergence of inter-protein β-sheets during ageing increases droplet viscosity"  
- **Issue** The relationship between the stress relaxation modulus G(t), viscosity, and the diffusion coefficient is not explained for readers unfamiliar with rheology. The terms "plateau" and "infinite viscosity" are used without definition.  
- **Required correction** Add a brief explanation of how G(t) relates to viscosity and what a plateau in G(t) signifies in terms of material behaviour. Define "infinite viscosity" in the context of the simulations.

- **Concern ID** R1-m4  
- **Severity** Minor  
- **Axis** Presentation  
- **Affected element** Figures  
- **Evidence pointer** Figures 1–5  
- **Issue** The figure captions are detailed but the figures themselves were not provided for review. It is not possible to assess the clarity of the data presentation.  
- **Required correction** Ensure that all figures are self-contained with clear labels, error bars, and legends. Consider adding schematic representations of the simulation protocols to aid understanding.

- **Concern ID** R1-m5  
- **Severity** Minor  
- **Axis** Scientific importance  
- **Affected element** Discussion  
- **Evidence pointer** Discussion  
- **Issue** The discussion of the implications for disease is brief. The authors mention ALS and FTD but do not elaborate on how their findings might inform therapeutic strategies or experimental predictions that could be tested.  
- **Required correction** Expand the discussion to include specific, testable predictions from the model (e.g., how changes in RNA concentration or temperature would affect condensate viscosity) and how these could be validated experimentally.

- **Concern ID** R1-m6  
- **Severity** Minor  
- **Axis** Technical soundness  
- **Affected element** Methods  
- **Evidence pointer** Supplementary Methods (not provided)  
- **Issue** All methodological details are in the Supplementary Methods, which was not available for review. This makes it impossible to assess the robustness of the simulations.  
- **Required correction** Ensure that the Supplementary Methods are comprehensive and include all necessary details for reproducibility, including simulation box sizes, equilibration protocols, and analysis parameters.

## Risk / unsupported claims
- The claim that RNA "can prevent" structural transitions is not supported by the data, which show deceleration rather than prevention.
- The claim that critical parameters of phase diagrams are conserved during ageing is not rigorously justified for a non-equilibrium system.
- The claim of "drastic differences" in network connectivity between liquid-like and gel-like condensates is not quantitatively supported in the main text.
- The physiological relevance of the RNA concentrations used is not established.
- The kinetic model parameters and their uncertainties are not fully reported.
- All methodological details are in supplementary material that was not provided, making the technical soundness of the simulations unverifiable from the supplied text.