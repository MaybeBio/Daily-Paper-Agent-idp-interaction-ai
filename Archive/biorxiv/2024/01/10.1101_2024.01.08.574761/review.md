## Review setup
- **Input scope** Full manuscript text including abstract, introduction, results, discussion, methods, and supplementary figure descriptions
- **Assessment boundary** Scientific content, experimental design, data interpretation, and claims as presented in the provided manuscript
- **Shared manuscript claim summary** The authors propose that Claspin undergoes a phosphorylation-dependent conformational transition from a disordered "closed" state, where the N- and C-terminal segments interact via the acidic patch (AP), to a structured "open" state that promotes DNA binding and replication factor interactions while relieving MCM helicase inhibition, thereby regulating DNA replication initiation.
- **Visible evidence base** Figures 1-8 as referenced in text; Supplementary Figures 1-3 as referenced; Methods section; no raw data or uncropped gels provided
- **Missing materials affecting confidence** Raw gel images, quantification details for PLA signals, statistical analysis details, full experimental replicates, cell line validation data, and supplementary figure data not included in the provided material

## Reviewer
- **Overall assessment** This manuscript addresses an important question regarding how phosphorylation regulates the structure and function of the intrinsically disordered protein Claspin. The authors present a compelling model supported by multiple complementary approaches including DNA binding assays, helicase assays, pull-down experiments, limited proteolysis, and PLA. The central claim that phosphorylation induces a disorder-to-order transition that modulates Claspin's interactions is interesting and potentially significant. However, several technical concerns regarding experimental rigor, quantification, and interpretation need to be addressed before the conclusions can be fully established. The manuscript would benefit from additional controls and more detailed presentation of quantitative data.

- **Who would be interested in the results, and why** Researchers studying DNA replication initiation and replication stress responses, particularly those interested in the regulation of replication fork proteins. The broader community studying intrinsically disordered proteins and how phosphorylation modulates their conformational ensembles and functions would also find this work relevant. The proposed model of phosphorylation-dependent conformational switching in a disordered protein has implications beyond Claspin biology.

- **Major strengths** The study combines multiple biochemical and cell-based approaches to address a mechanistically important question. The use of PLA to demonstrate intramolecular interactions in cells is innovative. The identification of the AP segment as a key regulatory element and the demonstration that phosphorylation state correlates with conformational changes and functional outcomes provides a coherent model. The trypsin sensitivity experiments provide direct evidence for conformational differences between phosphorylated and dephosphorylated states.

- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors claim that "phosphorylation inhibits intramolecular interactions and DNA-binding activity of Claspin through significant conformational change" based on experiments comparing wild-type, ΔAP, and AP(DE/A) mutants.
- **Evidence pointer** Figure 1A-D; Figure 2B-C; Figure 3B-D; location not provided
- **Concern** The manuscript does not provide quantitative analysis of the DNA binding and helicase assay data. The gel shift assays are presented as representative images without quantification across multiple independent experiments. The claim that wild-type Claspin "inhibits the helicase activity of MCM in an AP-dependent manner" is based on a single representative experiment without statistical analysis. Additionally, the stoichiometry of Claspin to MCM in the helicase assays is not clearly stated, making it difficult to assess the physiological relevance of the observed inhibition.
- **Why it matters** Without quantitative data and statistical analysis, it is not possible to determine whether the observed differences between wild-type and mutant Claspin are reproducible and significant. The helicase inhibition claim is central to the proposed model and requires rigorous demonstration.
- **Resolution test** Provide quantification of at least three independent experiments for DNA binding and helicase assays, with appropriate statistical tests. Include titration experiments showing the concentration dependence of Claspin-mediated helicase inhibition and state the molar ratios of Claspin to MCM used.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors state that "the wild-type Claspin inhibits the helicase activity of MCM in an AP-dependent manner" and that "ΔAP and dephosphorylated Claspin exhibit resistance to trypsin digestion compared to wild-type, suggesting the presence of structural domains in the formers."
- **Evidence pointer** Figure 1D; Figure 2C; location not provided
- **Concern** The trypsin digestion experiments are presented without quantification of band intensities over time. The claim that dephosphorylated Claspin is more resistant to trypsin digestion is based on visual inspection of gels. Furthermore, the authors do not address whether the trypsin digestion patterns reflect global conformational changes or local effects at specific cleavage sites. The relationship between trypsin resistance and the presence of "structural domains" is inferred but not directly demonstrated.
- **Why it matters** The conformational change model is a central pillar of the manuscript. The trypsin digestion data is the primary direct evidence for this conformational difference, and it needs to be rigorously quantified and interpreted. Without this, the claim that phosphorylation induces a disorder-to-order transition is not fully supported.
- **Resolution test** Provide quantified time-course data for trypsin digestion with statistical analysis. Consider complementary approaches such as limited proteolysis coupled with mass spectrometry to identify specific regions that become protected upon dephosphorylation. Include circular dichroism or other biophysical methods if feasible.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors claim that "the intramolecular interaction of Claspin is dependent on AP" based on PLA experiments showing strong signals with wild-type but not with ΔAP or AP(DE/A) mutants.
- **Evidence pointer** Figure 4A-C; location not provided
- **Concern** The PLA experiments lack important controls and quantification. The authors do not show negative controls such as cells expressing only one tagged construct or cells where the two tags are on separate proteins that do not interact. The quantification of PLA signals is not described, and it is unclear how many cells were analyzed and whether the difference between wild-type and mutants is statistically significant. Additionally, the authors do not address whether the AP mutations affect protein stability or localization, which could confound the PLA results.
- **Why it matters** The PLA data is presented as key evidence for the intramolecular interaction in cells. Without proper controls and quantification, the conclusion that AP mediates this interaction is not rigorously supported.
- **Resolution test** Include negative controls (e.g., cells expressing only N-terminal or C-terminal tagged constructs alone), provide quantification of PLA signals from multiple fields and experiments with statistical analysis, and confirm that mutant proteins are expressed at similar levels and localize similarly to wild-type.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Scientific importance
- **Claim pointer** The authors propose that "Claspin is converted from disordered (closed) to structured (open) conformation at initiation, which stimulates its DNA binding and interaction with replication factors and counteracts its helicase inhibitory activity to trigger initiation of DNA replication."
- **Evidence pointer** Figure 8; Discussion; location not provided
- **Concern** The model presented in Figure 8 is largely speculative and extends beyond the direct experimental evidence. While the data support phosphorylation-dependent changes in Claspin's interactions and conformation, the specific claim that this transition occurs "at initiation" in a cell cycle-dependent manner is not directly tested. The authors do not examine Claspin conformation or interactions at specific cell cycle stages. The connection between the in vitro biochemical observations and the proposed in vivo regulatory mechanism remains correlative.
- **Why it matters** The broader significance of the work depends on the physiological relevance of the proposed conformational switch. If the model is not directly supported by cell cycle experiments, the importance of the findings is diminished.
- **Resolution test** Perform cell cycle synchronization experiments to examine Claspin phosphorylation status, conformation, and interactions at different cell cycle stages. Alternatively, use phospho-specific antibodies or mass spectrometry to correlate specific phosphorylation events with functional outcomes.

- **Concern ID** R1-M5
- **Severity** Major
- **Blocking** No
- **Axis** Technical soundness
- **Claim pointer** The authors state that "the N-terminal segment (#2) exhibited hyperphosphorylation after Calyculin A treatment" and that phosphorylation of Claspin at the N-terminal segment inhibits intramolecular interactions.
- **Evidence pointer** Figure 2B; Figure 5; location not provided
- **Concern** The kinase assays shown in Figure 5 are not quantified, and the stoichiometry of phosphorylation is not determined. The claim that specific kinases phosphorylate specific regions of Claspin is based on autoradiography without phosphosite mapping. The authors do not identify which specific phosphorylation sites are responsible for the observed effects. The ST/A and ST/D mutations replace all serines and threonines in the N-terminal 350 amino acids, which is a very broad perturbation that may have pleiotropic effects beyond mimicking or eliminating phosphorylation.
- **Why it matters** The specificity of the phosphorylation effects is important for the mechanistic model. Without identifying specific phosphorylation sites, it is difficult to determine whether the observed effects are due to phosphorylation at particular residues or to general changes in the protein's properties.
- **Resolution test** Perform phosphosite mapping by mass spectrometry to identify specific phosphorylation sites in the N-terminal region. Generate more targeted mutants at identified phosphorylation sites and test their effects on DNA binding, intramolecular interactions, and helicase inhibition.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Readability for nonspecialists
- **Affected element** Abstract and Introduction
- **Evidence pointer** Abstract; Introduction; location not provided
- **Issue** The abstract and introduction assume significant background knowledge about DNA replication and Claspin biology. Terms such as "replisome progression complex," "CMG complex," and "fork protection complex" are used without brief explanations. The significance of the disorder-to-order transition for a general audience could be more clearly articulated.
- **Required correction** Provide brief definitions or context for specialized terms in the introduction. Consider adding a sentence in the abstract that explains why the conformational transition is significant for understanding DNA replication regulation.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Technical soundness
- **Affected element** Methods
- **Evidence pointer** Methods section; location not provided
- **Issue** The Methods section lacks detail on several key experiments. For example, the PLA assay description does not specify the number of cells analyzed, the criteria for counting signals, or the statistical methods used. The kinase assay description does not specify the concentrations of kinases and substrates used or the reaction conditions.
- **Required correction** Expand the Methods section to include detailed protocols, including concentrations, incubation times, and statistical analysis methods. This is essential for reproducibility.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Technical soundness
- **Affected element** Figure legends
- **Evidence pointer** Figures 1-8; location not provided
- **Issue** The figure legends are brief and do not fully describe the experimental conditions, the number of replicates, or the statistical analysis. For example, Figure 1D does not state the concentration range of Claspin used in the helicase assay or how the percent unwinding was calculated.
- **Required correction** Expand figure legends to include all experimental details, including concentrations, incubation times, number of replicates, and statistical tests used.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Scientific importance
- **Affected element** Discussion
- **Evidence pointer** Discussion; location not provided
- **Issue** The discussion of the potential role of Claspin as a tumor suppressor and the implications for cancer biology is interesting but not well integrated with the experimental data. The authors mention that "loss of Claspin could be an essential event during carcinogenesis" but do not discuss how their findings relate to this possibility in detail.
- **Required correction** Expand the discussion to more thoroughly explore the implications of the conformational switch model for understanding Claspin's role in cancer and other diseases.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Readability for nonspecialists
- **Affected element** Figure 8
- **Evidence pointer** Figure 8; location not provided
- **Issue** The model figure is complex and may be difficult for nonspecialists to interpret. The transitions between states and the functional consequences are not clearly labeled.
- **Required correction** Simplify the model figure and add clear labels for each state and transition. Consider adding a legend that explains the model in plain language.

## Risk / unsupported claims
- The claim that Claspin is converted from a disordered to a structured conformation at initiation is not directly supported by cell cycle experiments and remains speculative.
- The claim that specific phosphorylation sites in the N-terminal region regulate DNA binding is not supported by phosphosite mapping data.
- The claim that wild-type Claspin inhibits MCM helicase activity in an AP-dependent manner lacks quantitative data and statistical analysis.
- The PLA data supporting intramolecular interactions in cells lacks proper negative controls and quantification.
- The relationship between trypsin resistance and the presence of structured domains is inferred but not directly demonstrated.
- The claim that the ST/A mutant shows higher DNA binding than wild-type is based on limited data without statistical analysis.
- The physiological relevance of the in vitro helicase inhibition by Claspin is not established, as the stoichiometry and conditions may not reflect in vivo conditions.