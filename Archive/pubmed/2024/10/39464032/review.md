## Review setup
- **Input scope** Full manuscript text (preprint, bioRxiv)
- **Assessment boundary** Scientific content, methodology, data interpretation, and claims as presented in the provided text; no external validation or replication attempted
- **Shared manuscript claim summary** The authors propose that phosphorylation of the SARS-CoV-2 nucleocapsid protein (N) toggles its condensate behavior at membranes between two states: phosphorylated N forms liquid condensates that wet membranes (associated with RNA replication), while unmodified N forms viscoelastic condensates that can be engulfed by membranes (associated with genome packaging). This switch is attributed to phosphorylation-induced conformational changes that alter condensate material properties and protein-protein interactions.
- **Visible evidence base** In vitro reconstitution assays; fluorescence microscopy of condensate-membrane interactions; FRAP; passive microrheology; micropipette aspiration; fluorescence polarization binding assays; SAXS; coarse-grained molecular dynamics simulations with Bayesian Maximum Entropy reweighting; mass spectrometry and Phos-Tag SDS-PAGE for phosphorylation confirmation
- **Missing materials affecting confidence** Figures and supplementary figures referenced but not provided; Supplementary Tables S1; Movies S1–6; full experimental details for some assays (e.g., exact lipid compositions, buffer conditions for specific experiments); raw data and analysis code not accessible; details of the Bayesian reweighting implementation

## Reviewer
- **Overall assessment** This manuscript addresses a timely and important question in SARS-CoV-2 biology: how phosphorylation of the nucleocapsid protein regulates its dual functions at membranes. The authors combine a wide range of biophysical techniques to build a mechanistic model linking phosphorylation state to condensate material properties and membrane interaction modes. The central claim, that phosphorylation toggles N between two membrane-associated condensate states, is well-supported by the in vitro data presented. The integration of experiments and simulations is commendable. However, several technical concerns, particularly regarding the interpretation of the SAXS and simulation data, the physiological relevance of the in vitro conditions, and the lack of direct evidence for the proposed conformational mechanism, temper the strength of the conclusions. The manuscript would benefit from additional controls and a more cautious framing of the mechanistic model.
- **Who would be interested in the results, and why** Virologists studying SARS-CoV-2 replication and assembly; cell biologists interested in biomolecular condensates and their regulation; biophysicists working on phase separation, membrane interactions, and protein-RNA interactions; researchers in the growing field of condensate-membrane crosstalk. The findings have potential implications for understanding viral lifecycle regulation and identifying new therapeutic targets.
- **Major strengths**
  1. The study addresses a significant gap in understanding how N protein function is regulated, directly linking phosphorylation to condensate behavior at membranes.
  2. The combination of multiple orthogonal biophysical techniques (FRAP, microrheology, micropipette aspiration, fluorescence polarization, SAXS, simulations) provides a comprehensive and cross-validated dataset.
  3. The use of in vitro phosphorylated N protein, rather than a phosphomimetic mutant, enhances the physiological relevance of the findings.
  4. The proposed model is clear and testable, providing a framework for future studies.
- **Major Concerns**
  - **Concern ID** R1-M1
  - **Severity** Major
  - **Blocking** Yes
  - **Axis** Technical soundness / Data interpretation
  - **Claim pointer** The authors claim that SAXS data and simulations support a phosphorylation-induced conformational change that "softens" condensate material properties by promoting intra-dimer interactions.
  - **Evidence pointer** Results section "Phosphorylation weakens binding between N and RNA by promoting intra-dimer interactions"; Figures 5 and 6 (not provided); Supplementary Figures 11–18
  - **Concern** The mechanistic link between the observed decrease in radius of gyration (Rg) from SAXS and the proposed "new interactions between monomers within pN dimers" is not rigorously established. The Rg change (60.2 Å to 54.4 Å) is modest and could be explained by other factors, such as changes in flexibility or solvation, rather than specific new inter-domain contacts. The coarse-grained simulations, while supporting the idea of increased inter-monomer contacts, rely on phosphomimetic mutations (S to D, T to E) which may not fully recapitulate the effects of actual phosphorylation (e.g., charge, size, hydrogen bonding). The Bayesian Maximum Entropy reweighting is mentioned but its implementation and the quality of the fit to the SAXS data are not described in sufficient detail to assess its validity. The claim that this conformational change "weakens binding between N and RNA" is supported by fluorescence polarization, but the causal link to the conformational change is inferred, not directly demonstrated.
  - **Why it matters** The proposed conformational mechanism is a central pillar of the paper's model. If this mechanism is not robustly supported, the link between phosphorylation, molecular conformation, and macroscopic condensate properties is weakened. The manuscript's novelty partly rests on providing this mechanistic insight.
  - **Resolution test** Provide a more detailed analysis of the SAXS data, including fits of the reweighted ensembles to the experimental scattering profiles with quantitative goodness-of-fit metrics. Include control simulations with actual phosphorylated residues (e.g., using a phosphorylated amino acid model) rather than only phosphomimetics. Directly test the proposed intra-dimer interactions by, for example, mutating the identified interacting residues and showing that the effect on condensate properties or RNA binding is lost. Show that the conformational change is specifically due to phosphorylation and not just the addition of negative charge.

  - **Concern ID** R1-M2
  - **Severity** Major
  - **Blocking** Yes
  - **Axis** Technical soundness / Experimental design
  - **Claim pointer** The authors claim that unmodified N condensates can be "engulfed by membranes" and that this resembles the engulfment of the RNP complex during viral budding.
  - **Evidence pointer** Results section "N condensate composition determines interaction with membranes"; Figure 2E; Movies S5–6
  - **Concern** The observation of "membrane wrapping" or engulfment is based on a limited number of events (4/10 for N with M-coated GUVs). The authors attribute the difference between binding and wrapping to "membrane tension of the GUVs," but this parameter is not systematically varied or measured. The physiological relevance of using GUVs with a simplified lipid composition (60% DOPC, 25% DOPE, 10% DOPS, 5% Ni-NTA lipids) to model the complex ER or ERGIC membrane is not fully addressed. The claim that this in vitro observation "resembles the direction of membrane bending required for encapsidation" is speculative and not supported by direct evidence of the molecular events during budding.
  - **Why it matters** The functional distinction between the two condensate states relies on their different interactions with membranes. If the engulfment phenotype is not robust or is an artifact of the simplified in vitro system, the functional significance of the phosphorylation toggle is weakened.
  - **Resolution test** Quantify the frequency of each interaction type (binding, wrapping, wetting) across many independent experiments and GUVs. Systematically vary membrane tension (e.g., by osmotic deflation) and show a clear correlation with the observed phenotype. Use a more complex lipid composition that better mimics the ER/ERGIC membrane. Provide a more detailed discussion of the limitations of the GUV model and how the observed behavior might translate to the cellular context.

  - **Concern ID** R1-M3
  - **Severity** Major
  - **Blocking** No
  - **Axis** Scientific importance / Physiological relevance
  - **Claim pointer** The authors propose that their findings "suggest potential therapeutic targets for COVID infection."
  - **Evidence pointer** Discussion section
  - **Concern** While the study provides valuable mechanistic insight, the direct therapeutic implications are overstated. The experiments are entirely in vitro, and no evidence is provided that modulating N phosphorylation or its condensate properties would be a viable therapeutic strategy in cells or in vivo. The link between the proposed mechanism and disease outcome is speculative.
  - **Why it matters** Overstating therapeutic potential can mislead readers and detract from the solid basic science contributions of the study.
  - **Resolution test** Soften the therapeutic claims in the discussion, framing them as speculative and requiring further validation in cellular and animal models. Alternatively, include preliminary data in cells (e.g., effect of kinase inhibitors on N localization or condensate formation) to support the translational potential.

- **Minor Comments**
  - **Concern ID** R1-m1
  - **Severity** Minor
  - **Axis** Clarity / Reproducibility
  - **Affected element** Methods section, "Fluorescence Polarization"
  - **Evidence pointer** Materials and Methods
  - **Issue** The description of the fluorescence polarization assay lacks specific details on the RNA sequences used (beyond "SL4" and "polyrA"), the exact labeling strategy, and the buffer conditions for the binding experiments.
  - **Required correction** Provide the full sequences of the RNA constructs, the position of the fluorophore, and the exact buffer composition (salt, pH, additives) used in the binding assays.

  - **Concern ID** R1-m2
  - **Severity** Minor
  - **Axis** Data presentation
  - **Affected element** Figure 4, panels D–I
  - **Evidence pointer** Results section "Phosphorylation of N modulates the material properties of N condensates"
  - **Issue** The microrheology and micropipette aspiration data are presented as average values with standard deviations. It is unclear how many independent experiments and how many individual measurements (e.g., number of beads, number of aspiration cycles) were performed for each condition.
  - **Required correction** Clearly state the number of independent replicates (n) and the total number of measurements for each reported value in the figure legends or methods.

  - **Concern ID** R1-m3
  - **Severity** Minor
  - **Axis** Interpretation
  - **Affected element** Discussion section
  - **Evidence pointer** Discussion
  - **Issue** The authors discuss the potential role of RNA structure in modulating condensate properties but do not fully integrate this with the phosphorylation-dependent effects. The interplay between RNA sequence/structure and protein phosphorylation state is complex and could be discussed more thoroughly.
  - **Required correction** Add a paragraph in the discussion explicitly addressing how RNA structure and protein phosphorylation might act together or independently to determine condensate properties and membrane interactions.

  - **Concern ID** R1-m4
  - **Severity** Minor
  - **Axis** Reproducibility
  - **Affected element** Methods section, "Molecular dynamics simulations"
  - **Evidence pointer** Materials and Methods
  - **Issue** The description of the simulation protocol is brief. Key parameters such as the number of simulation runs, the length of each run, the system size, and the specific implementation of the Bayesian Maximum Entropy reweighting are not fully detailed.
  - **Required correction** Provide a more complete description of the simulation setup, including all relevant parameters, and cite the specific software and version used for the reweighting analysis.

  - **Concern ID** R1-m5
  - **Severity** Minor
  - **Axis** Clarity
  - **Affected element** Figure 1, panels C–D
  - **Evidence pointer** Introduction and Results
  - **Issue** The schematic in Figure 1C–D is described as a model, but it is not clear if it is a hypothesis or a summary of the findings.
  - **Required correction** Clarify in the figure legend whether the schematic represents a working hypothesis or a summary of the experimental results.

## Risk / unsupported claims
- The claim that the observed in vitro membrane engulfment of N condensates "resembles the direction of membrane bending required for encapsidation" is speculative and not directly supported by the data.
- The statement that the findings "suggest potential therapeutic targets for COVID infection" is not supported by any experimental evidence in the manuscript.
- The mechanistic model proposing that phosphorylation-induced intra-dimer interactions "weaken binding between N and RNA" is inferred from a combination of SAXS, simulations, and binding assays, but a direct causal link is not established.
- The claim that the conformational change "softens" condensate material properties is supported by the material property measurements, but the direct link between the specific conformational change and the macroscopic properties is not fully demonstrated.
- The physiological relevance of the simplified in vitro system (GUVs with a defined lipid composition, specific RNA fragments) to the complex environment of infected cells is not fully established, and the authors acknowledge this limitation but do not provide data to bridge the gap.