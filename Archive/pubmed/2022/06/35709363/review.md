## Review setup
- **Input scope** Abstract only
- **Assessment boundary** Claims and evidence as presented in the abstract; no access to full text, figures, tables, or supplementary materials
- **Shared manuscript claim summary** The authors use all-atom molecular dynamics simulations to investigate how phosphorylation in the FUS low-complexity domain (FUS-LC) disrupts liquid-liquid phase separation (LLPS) and aggregation. They report three main findings: (1) phosphorylation shifts FUS(37-97) conformations from beta-rich, fibril-competent states toward helix-rich, fibril-incompetent states; (2) phosphorylation weakens protein-protein interactions and enhances protein-water interactions, disfavoring LLPS and aggregation and facilitating dissolution of preformed fibrils; (3) residues 52-67 show high beta-strand probability, and phosphorylation at S54 and S61 is critical for the inhibitory effects.
- **Visible evidence base** Abstract text only; no simulation details, force field parameters, system setup, convergence criteria, or quantitative results are provided
- **Missing materials affecting confidence** Full manuscript, all figures and tables, simulation methodology, force field validation, convergence analysis, quantitative interaction energy data, and any experimental validation

## Reviewer
- **Overall assessment** The abstract presents a potentially interesting computational study addressing a mechanistically important question in the field of phase separation and neurodegeneration. The three reported findings are coherent and plausible within the framework of molecular dynamics simulations. However, the abstract alone provides insufficient detail to evaluate the technical rigor of the simulations, the statistical significance of the results, or the robustness of the conclusions. The claim that phosphorylation can disrupt preformed fibrils is particularly strong and would require careful demonstration of simulation convergence and appropriate sampling. The study may be of interest to computational biophysicists and researchers studying FUS-related pathology, but the current evidence base is too limited to establish the case.
- **Who would be interested in the results, and why** Computational biophysicists studying protein phase separation and aggregation would be interested in the methodological approach and mechanistic insights. Researchers working on FUS biology and amyotrophic lateral sclerosis or frontotemporal lobar degeneration pathology would be interested in the potential therapeutic implications of site-specific phosphorylation. The findings may also appeal to those studying post-translational modification effects on protein conformational ensembles.
- **Major strengths** The study addresses a clinically relevant and mechanistically important question. The use of all-atom molecular dynamics simulations to investigate both monomeric and dimeric states as well as fibril structures is comprehensive in scope. The identification of specific phosphorylation sites (S54 and S61) within a defined beta-strand region provides a testable hypothesis. The reported shift from beta-rich to helix-rich conformations offers a clear mechanistic framework.
- **Major Concerns**  
  - R1-M1  
  - R1-M2  
  - R1-M3  
  - R1-M4
- **Minor Comments**  
  - R1-m1  
  - R1-m2  
  - R1-m3
- **Technical failings that need to be addressed before the case is established** R1-M1, R1-M2, R1-M3
- **Assessment against Nature-style criteria**  
  Originality: The question of how phosphorylation disrupts FUS LLPS and aggregation is not entirely new, but the atomistic mechanistic detail and the specific focus on fibril dissolution may offer original contributions. The originality cannot be fully assessed from the abstract alone.  
  Scientific importance: The topic is of high importance given the connection between FUS phase separation and neurodegeneration. If the claims are well supported, the findings could have significant implications for understanding disease mechanisms and designing therapeutic strategies.  
  Interdisciplinary readership: The work bridges computational biophysics, protein chemistry, and neurobiology, which could attract readers across these fields. However, the abstract is written in a way that is accessible to specialists but may be challenging for nonspecialists without additional context.  
  Technical soundness: Cannot be evaluated from the abstract. Critical details regarding simulation methodology, force field choice, sampling adequacy, and validation are absent.  
  Readability for nonspecialists: The abstract is reasonably clear but uses field-specific terminology (e.g., "fibril-competent state," "beta-strand probability") that may require background knowledge. The logical flow is coherent.
- **Recommendation posture** Currently not established from the provided evidence. The abstract presents plausible claims, but the absence of methodological detail and quantitative results prevents assessment of technical soundness. A supportive posture would require access to the full manuscript and verification of simulation rigor.

### Major Concerns

- **Concern ID** R1-M1  
- **Severity** Major  
- **Blocking** Yes  
- **Axis** Technical soundness  
- **Claim pointer** The claim that phosphorylation shifts FUS(37-97) conformations from beta-rich, fibril-competent states toward helix-rich, fibril-incompetent states.  
- **Evidence pointer** Abstract, finding (1); location not provided  
- **Concern** The abstract reports a conformational shift but provides no quantitative data on the populations of beta-rich versus helix-rich states, no error estimates, and no information on how these populations were calculated from the simulations. Without convergence analysis or replica sampling details, it is unclear whether the observed shift is statistically robust or an artifact of insufficient sampling.  
- **Why it matters** The central mechanistic claim rests on this conformational shift. If the sampling is inadequate or the analysis is biased, the entire interpretation of phosphorylation effects on LLPS and aggregation would be compromised.  
- **Resolution test** Provide population distributions with error bars, convergence metrics (e.g., block averaging, multiple independent runs), and details on how conformational states were defined and classified.

- **Concern ID** R1-M2  
- **Severity** Major  
- **Blocking** Yes  
- **Axis** Technical soundness  
- **Claim pointer** The claim that phosphorylation significantly weakens protein-protein interactions and enhances protein-water interactions, which disfavor LLPS and aggregation and facilitate dissolution of preformed fibrils.  
- **Evidence pointer** Abstract, finding (2); location not provided  
- **Concern** The abstract states that phosphorylation weakens protein-protein interactions and enhances protein-water interactions but provides no quantitative interaction energy values, no comparison to non-phosphorylated controls, and no statistical analysis. The claim that phosphorylation facilitates dissolution of preformed fibrils is particularly strong and requires demonstration that the simulations captured the relevant timescales and that the observed dissociation is not a simulation artifact.  
- **Why it matters** This is the second major mechanistic claim and directly supports the potential therapeutic relevance. Without quantitative evidence, the claim remains speculative.  
- **Resolution test** Provide interaction energy decomposition (electrostatic, van der Waals, hydrogen bonding) with standard errors, comparison between phosphorylated and non-phosphorylated systems, and evidence of fibril dissociation from multiple independent simulations with sufficient length.

- **Concern ID** R1-M3  
- **Severity** Major  
- **Blocking** Yes  
- **Axis** Technical soundness  
- **Claim pointer** The claim that residues 52-67 display high beta-strand probability and that phosphorylation at S54 and S61 is crucial for disruption of LLPS and aggregation.  
- **Evidence pointer** Abstract, finding (3); location not provided  
- **Concern** The abstract identifies specific residues as critical but provides no quantitative beta-strand probability values, no comparison of phosphorylation effects at S54 and S61 versus other serine residues, and no mutational or control simulations to establish specificity. The term "crucial" implies a level of certainty that cannot be supported without systematic residue-by-residue analysis.  
- **Why it matters** This claim has potential therapeutic implications, as it suggests specific targets for intervention. Overstating the importance of specific residues without rigorous evidence could mislead subsequent experimental efforts.  
- **Resolution test** Provide per-residue beta-strand probability profiles with confidence intervals, systematic phosphorylation scans across all serine residues in the region, and control simulations with phospho-mimetic or phospho-dead mutations.

- **Concern ID** R1-M4  
- **Severity** Major  
- **Blocking** No  
- **Axis** Reproducibility  
- **Claim pointer** The overall study claims to provide mechanistic insights into phosphorylation effects on FUS-LC LLPS and aggregation.  
- **Evidence pointer** Abstract; location not provided  
- **Concern** The abstract does not mention the force field used, the water model, the simulation length, the number of replicas, or the system size. These details are essential for reproducibility and for assessing whether the simulation timescales are appropriate for the processes being studied.  
- **Why it matters** Molecular dynamics results are highly sensitive to force field parameters and sampling protocols. Without this information, other researchers cannot reproduce the work or evaluate its reliability.  
- **Resolution test** Include full simulation parameters in the methods section, including force field version, water model, salt concentration, temperature control, simulation length, and number of independent runs.

### Minor Comments

- **Concern ID** R1-m1  
- **Severity** Minor  
- **Axis** Clarity  
- **Affected element** Abstract, finding (1)  
- **Evidence pointer** Abstract; location not provided  
- **Issue** The term "fibril-competent state" is used without definition. It is unclear whether this refers to a specific conformational ensemble, a structural motif, or a thermodynamic state.  
- **Required correction** Define "fibril-competent" explicitly, for example by referencing specific structural features or free energy basins.

- **Concern ID** R1-m2  
- **Severity** Minor  
- **Axis** Completeness  
- **Affected element** Abstract, finding (2)  
- **Evidence pointer** Abstract; location not provided  
- **Issue** The abstract states that phosphorylation "facilitate[s] the dissolution of the preformed FUS-LC fibril" but does not specify the timescale over which this occurs or whether complete dissolution was observed.  
- **Required correction** Provide quantitative information on the extent and rate of fibril dissociation observed in the simulations.

- **Concern ID** R1-m3  
- **Severity** Minor  
- **Axis** Context  
- **Affected element** Abstract, overall framing  
- **Evidence pointer** Abstract; location not provided  
- **Issue** The abstract does not mention any comparison with experimental data on FUS phosphorylation, which would help contextualize the simulation findings.  
- **Required correction** Add a brief statement in the abstract or introduction referencing relevant experimental observations on FUS phosphorylation and phase separation.

## Risk / unsupported claims
- The claim that phosphorylation "facilitate[s] the dissolution of the preformed FUS-LC fibril" is unsupported from the abstract alone, as no quantitative dissociation data or simulation details are provided.
- The claim that phosphorylation at S54 and S61 is "crucial" is unsupported without systematic residue scanning or mutational controls.
- The claim that phosphorylation shifts conformations from beta-rich to helix-rich states is unquantified and cannot be evaluated without population data and error analysis.
- The overall mechanistic conclusions cannot be assessed for robustness without information on force field choice, simulation length, sampling convergence, and statistical treatment.