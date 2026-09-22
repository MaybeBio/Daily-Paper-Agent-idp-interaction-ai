## Review setup
- **Input scope** Full manuscript text (abstract, introduction, methods, results, discussion, conclusion) without supplementary figures or extended data
- **Assessment boundary** Scientific content, methodological rigor, claims versus evidence, and suitability for publication in Communications Chemistry
- **Shared manuscript claim summary** The authors combine confocal microscopy, hyperspectral imaging, FRAP, and two coarse-grained simulation approaches to characterize K10/D10 coacervate interactions with lipid membranes, reporting that membrane fluidity decreases at the coacervate contact region due to lipid crowding and ordering, and that local lipid de-mixing occurs, with simulation parameters calibrated to match experimentally measured contact angles.
- **Visible evidence base** Main text figures 1-5, equations 1-10, methods descriptions, statistical analyses as described
- **Missing materials affecting confidence** Supplementary figures (S1-S10), supplementary tables (S1-S2), detailed simulation parameter tables, raw data files, and full statistical outputs were not provided for assessment

## Reviewer
- **Overall assessment** This manuscript presents a well-structured integration of experimental and computational approaches to study coacervate-membrane interactions. The combination of multiple experimental techniques with two complementary coarse-grained models is commendable and addresses an important gap in the field. However, several technical concerns regarding the simulation methodology, the interpretation of the FRAP data, and the generalizability of the conclusions require careful consideration. The claim of a "nearly two-fold reduced fluidity" is supported by the data presented, but the mechanistic interpretation would benefit from additional validation. The manuscript is potentially suitable for publication in Communications Chemistry after major revisions.

- **Who would be interested in the results, and why** Researchers studying biomolecular condensates, liquid-liquid phase separation, membrane biophysics, and the interplay between membraneless organelles and membrane-bound compartments. The methodological framework combining experiments and simulations will be of interest to the broader soft matter and biophysics community, particularly those working on coacervate-membrane wetting phenomena and their biological implications.

- **Major strengths** 
  1. The integration of multiple experimental techniques (confocal microscopy, hyperspectral imaging, FRAP) with two complementary simulation approaches provides a comprehensive multi-scale perspective.
  2. The calibration of simulation parameters against experimentally measured contact angles is a rigorous approach that strengthens the validity of the computational results.
  3. The observation of lipid de-mixing and reduced fluidity at the coacervate-membrane interface, supported by both experiments and simulations, represents a significant contribution to understanding coacervate-membrane interactions.
  4. The discussion of differences between the two simulation models regarding lipid ordering provides valuable insight into model limitations.

- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness of simulation methodology
- **Claim pointer** The authors claim that the coarse-grained model was "successfully parameterized to accurately reproduce the fluid-elastic parameters observed in experiments" and that simulation results "corroborate well" experimental contact angles.
- **Evidence pointer** Methods section, Computational modeling; Results section, Figure 3e
- **Concern** The manuscript states that the generic coarse-grained model was parameterized to match experimental contact angles, but the specific parameter values used (ε_PL and ω_TT) are only shown in Figure 2b without a systematic description of how these were optimized. More critically, the MARTINI simulations required rescaling of protein-lipid interactions by a factor of 1.20 because the original force field "underestimated" interactions. This rescaling is a significant modification that could affect the quantitative validity of the simulation results. The authors should provide a more detailed description of the parameterization procedure, including how the parameter space was explored, how many independent simulations were performed, and what the sensitivity of the results is to the specific parameter choices.
- **Why it matters** The central claim of the paper relies on the quantitative agreement between simulations and experiments. Without a clear description of the parameterization procedure and its robustness, the reader cannot assess whether the agreement is meaningful or the result of overfitting. The rescaling of MARTINI interactions is particularly concerning as it may introduce artifacts that could affect the conclusions about lipid ordering and de-mixing.
- **Resolution test** Provide a detailed description of the parameterization procedure, including the range of parameters tested, the criteria used for optimization, and the sensitivity of the results to parameter variations. Include a table of all modified MARTINI interaction parameters and justify the rescaling factor. Show that the conclusions are robust across a reasonable range of parameter values.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence sufficiency for mechanistic claims
- **Claim pointer** The authors claim that "the crowding of lipids at the contact region, resulting in decreased area per lipid" is the mechanism behind the reduced membrane fluidity, and that "local lipid de-mixing" occurs upon coacervate adsorption.
- **Evidence pointer** Results section, Membrane dynamics at the contact region; Results section, Membrane packing and lipid ordering at the contact region; Figures 4 and 5
- **Concern** While the FRAP data show reduced diffusion in the wetted region and the simulations show decreased area per lipid, the causal link between these observations is not directly established. The authors infer that lipid crowding causes reduced fluidity, but alternative explanations (e.g., changes in membrane tension, altered hydration, or direct protein-lipid interactions affecting lipid mobility) are not systematically excluded. Additionally, the claim of lipid de-mixing is based primarily on simulation results, with the experimental evidence being indirect (LAURDAN spectral shifts can reflect multiple phenomena beyond lipid demixing). The manuscript would benefit from a more direct demonstration of the proposed mechanism.
- **Why it matters** The mechanistic interpretation is a key contribution of the paper. If the causal relationship between lipid crowding and reduced fluidity is not firmly established, the conclusions may be overstated. The distinction between lipid de-mixing and other forms of membrane reorganization has important implications for understanding the functional consequences of coacervate-membrane interactions.
- **Resolution test** Provide additional experimental or simulation evidence directly linking lipid crowding to reduced fluidity. This could include: (1) analysis of lipid trajectories in simulations to show reduced mobility specifically in crowded regions, (2) experiments with different lipid compositions to test the generality of the effect, or (3) direct measurement of lipid packing using alternative techniques. For the de-mixing claim, provide more direct evidence such as spatial correlation analysis of lipid species in simulations or experiments with labeled lipid species.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Generalizability and biological relevance
- **Claim pointer** The authors state that "this study provides an effective framework for integrating experiment and computation to characterize the properties of coacervate-membrane interfaces that are critical to the functional impacts of these interactions" and suggest broad implications for cellular processes.
- **Evidence pointer** Abstract; Introduction; Conclusion
- **Concern** The study uses a simplified model system (K10/D10 coacervates with synthetic lipids) that may not fully capture the complexity of physiological coacervate-membrane interactions. The relevance to cellular processes is asserted but not demonstrated. The authors do not discuss how the specific properties of K10/D10 coacervates (short peptides, high charge density) compare to physiologically relevant coacervates formed by longer IDPs with more complex sequence features. The claim of broad biological relevance would be strengthened by a more nuanced discussion of the limitations of the model system.
- **Why it matters** The paper positions itself as providing insights into biologically relevant phenomena. If the model system is too simplified, the conclusions may not transfer to physiological contexts. A more careful discussion of the scope and limitations of the findings would help readers assess the broader significance.
- **Resolution test** Add a discussion section addressing the limitations of the model system and the extent to which the findings can be generalized to physiologically relevant coacervates. If possible, include preliminary data with a more complex coacervate system or discuss how the findings relate to existing studies on more complex systems.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity of presentation
- **Affected element** Figure 2b
- **Evidence pointer** Results section, Figure 2b
- **Issue** The parameter values (ε_PL and ω_TT) are shown below Figure 2b but are not clearly labeled or explained in the figure caption. The relationship between these parameters and the experimental systems they correspond to is not immediately clear.
- **Required correction** Add a clear legend or annotation to Figure 2b explaining the parameter values, and include a more detailed description in the figure caption.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Statistical rigor
- **Affected element** Figure 4a
- **Evidence pointer** Results section, Figure 4a
- **Issue** The FRAP curves appear to show mean values, but the number of independent measurements, the error bars, and the statistical comparison between wetted and bare regions are not clearly described in the main text.
- **Required correction** Clearly state the number of independent experiments, the error bar definition, and the statistical test used to compare the wetted and bare regions in the figure caption and/or methods.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Completeness of methods
- **Affected element** Simulation details
- **Evidence pointer** Methods section, Molecular dynamics simulation details
- **Issue** The methods section does not provide sufficient detail on the equilibration protocol, the number of independent simulation replicas, or the criteria used to determine that simulations reached steady state.
- **Required correction** Add details on the number of replicas, equilibration criteria, and any convergence checks performed.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Interpretation of results
- **Affected element** Figure 5f
- **Evidence pointer** Results section, Figure 5f
- **Issue** The APL distributions show differences between upper and lower leaflets, but the biological or physical significance of the bimodal or skewed distributions is not discussed.
- **Required correction** Provide a brief interpretation of the APL distribution shapes and what they indicate about the membrane structure at the contact region.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Literature context
- **Affected element** Introduction
- **Evidence pointer** Introduction section
- **Issue** The introduction could benefit from a more explicit discussion of how this work advances beyond previous studies on coacervate-membrane interactions, particularly regarding the specific methodological innovations.
- **Required correction** Add a brief paragraph explicitly stating the novelty of the integrated approach compared to previous experimental or computational studies.

## Risk / unsupported claims
- The claim that the coarse-grained model "accurately reproduce[s] the fluid-elastic parameters observed in experiments" is not fully supported by the evidence provided, as the parameterization procedure is not described in sufficient detail.
- The mechanistic link between lipid crowding and reduced fluidity is inferred rather than directly demonstrated.
- The claim of "local lipid de-mixing" as a general phenomenon is primarily supported by simulation results, with limited direct experimental evidence.
- The statement that the framework is "critical to the functional impacts of these interactions" is an assertion that goes beyond the data presented.
- The generalizability of the findings to physiologically relevant coacervate systems is not established, given the simplified model system used.
- The rescaling of MARTINI force field parameters (factor 1.20) without extensive validation raises questions about the quantitative reliability of the simulation results.