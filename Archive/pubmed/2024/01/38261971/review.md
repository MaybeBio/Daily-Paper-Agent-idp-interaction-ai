## Review setup
- **Input scope** Full manuscript text, including abstract, introduction, methods, results, discussion, and data availability statements.
- **Assessment boundary** Scientific content, technical soundness, and internal consistency of the reported findings. No assessment of literature novelty beyond the provided text.
- **Shared manuscript claim summary** The authors report the discovery of a second PCNA-binding motif (a PIP-box) in the intrinsically disordered protein Spd1 from S. pombe. They propose that two tandem, low-affinity PCNA-binding motifs (PIP-degron and PIP-box) exchange rapidly on the same PCNA binding site, and that this competition-based system is functionally important for Spd1-mediated checkpoint activation in vivo. The authors further suggest that such tandem disordered motifs may be widespread in PCNA-binding ligands.
- **Visible evidence base** NMR spectroscopy (chemical shift assignments, CSPs, Kd determinations, diffusion measurements), X-ray crystallography (PCNA–Spd1 peptide complex), ITC, Monte Carlo simulations, and in vivo yeast assays (checkpoint activation, BiFC, Western blotting).
- **Missing materials affecting confidence** Supplementary figures and tables (referenced but not provided), full NMR assignment details, crystallographic data quality metrics (beyond summary statistics), simulation input parameters and convergence criteria, and detailed strain construction information.

## Reviewer
- **Overall assessment** This manuscript presents a well-structured and technically diverse study identifying a second PCNA-binding motif in Spd1 and proposing a competition-based model for checkpoint activation. The combination of biophysical, structural, and in vivo approaches is commendable. However, several technical concerns, particularly regarding the quantitative interpretation of binding data, the functional significance of the two motifs, and the speculative nature of the proposed model, need to be addressed before the case is fully established.
- **Who would be interested in the results, and why** Researchers studying PCNA-interacting proteins, intrinsically disordered proteins, DNA replication and repair checkpoints, and the molecular basis of protein–protein interactions involving short linear motifs. The findings may also be of interest to those investigating the evolution of disordered binding regions and the role of avidity in cellular signaling.
- **Major strengths** The study uses a multidisciplinary approach, combining NMR, crystallography, ITC, simulations, and in vivo assays. The identification of a second PCNA-binding motif in Spd1 is a clear advance. The functional validation through mutagenesis and in vivo checkpoint assays strengthens the relevance of the biophysical findings. The discussion of allovalency and the potential for tandem disordered motifs in other PCNA ligands is thought-provoking.
- **Major Concerns** See detailed items below.
- **Minor Comments** See detailed items below.
- **Technical failings that need to be addressed before the case is established** R1-M1 (Kd estimation for full-length Spd1), R1-M2 (functional interpretation of mutant phenotypes), R1-M3 (simulation limitations and interpretation).
- **Assessment against Nature-style criteria**  
  - **Originality** High. The identification of a second PCNA-binding motif in Spd1 and the proposal of a competition-based exchange model are novel contributions.  
  - **Scientific importance** Moderate to high. The findings have implications for understanding PCNA-mediated processes and the role of disordered motifs in protein interactions, but the broader significance beyond Spd1 remains speculative.  
  - **Interdisciplinary readership** Moderate. The study bridges structural biology, biophysics, and cell biology, but the detailed technical nature may limit appeal to a very broad audience.  
  - **Technical soundness** Generally sound, but with notable concerns regarding quantitative binding analysis and the interpretation of in vivo data.  
  - **Readability for nonspecialists** The manuscript is clearly written, but the technical depth in NMR and simulation methods may be challenging for nonspecialists. The abstract and introduction are accessible.
- **Recommendation posture** Supportive if technical concerns are resolved, particularly regarding the quantitative binding analysis and the functional interpretation of the mutant phenotypes.

### Major Concerns

- **Concern ID** R1-M1  
- **Severity** Major  
- **Blocking** Yes  
- **Axis** Quantitative binding analysis  
- **Claim pointer** The authors estimate a Kd of approximately 300 μM for full-length Spd1 binding to PCNA, based on comparison of chemical shifts rather than a full titration.  
- **Evidence pointer** Results section, "The two PCNA-binding motifs of Spd1 bind to and exchange rapidly in the same site"; Figure 3D.  
- **Concern** The Kd for full-length Spd1 is estimated by comparing chemical shifts at a single concentration, rather than by a full titration to saturation. This approach is not standard and may introduce significant error. The authors state that a full titration was not possible due to low solubility, but the reliability of the estimate is unclear.  
- **Why it matters** The proposed model of a "neatly balanced competition-based system" relies on the relative affinities of the two motifs and the full-length protein. An unreliable Kd for full-length Spd1 weakens the quantitative basis of the model.  
- **Resolution test** Provide a more rigorous estimation of the Kd, such as using a competition binding assay or ITC with full-length Spd1, or clearly state the limitations and error bars associated with the current estimate.

- **Concern ID** R1-M2  
- **Severity** Major  
- **Blocking** Yes  
- **Axis** Functional interpretation of in vivo data  
- **Claim pointer** The authors state that "increasing or decreasing the binding affinity between Spd1 and PCNA through mutations of either motif compromised the ability of Spd1 to cause checkpoint activation in yeast."  
- **Evidence pointer** Results section, "Checkpoint activation by Spd1"; Figure 4C.  
- **Concern** The interpretation that both increased and decreased affinity compromise checkpoint activation is based on a limited set of mutants. The 2F1 and 2F2 mutants, designed to increase affinity, were not fully characterized in vitro (2F1 was insoluble), and the in vivo phenotypes may be influenced by other factors such as protein stability, localization, or altered interactions with Suc22R2.  
- **Why it matters** The conclusion that a "fine-tuned balance" of affinities is required for function is a central claim of the paper. If the mutant phenotypes are due to off-target effects, this conclusion is not supported.  
- **Resolution test** Provide additional characterization of the 2F1 and 2F2 mutants, including protein stability, Suc22R2 binding, and localization. Alternatively, use a more systematic mutagenesis approach to map the functional landscape of the two motifs.

- **Concern ID** R1-M3  
- **Severity** Major  
- **Blocking** No  
- **Axis** Simulation methodology and interpretation  
- **Claim pointer** The Monte Carlo simulations suggest that in the PIP-degron-bound state, the PIP-box binds to the interdomain connecting loop, and in the PIP-box-bound state, the PIP-degron binds to the interior cavity of PCNA.  
- **Evidence pointer** Results section, "Molecular dynamics simulations"; Figure 6.  
- **Concern** The simulations are performed at low salt concentrations (5 and 20 mM), which are not physiologically relevant. The authors acknowledge this limitation but do not discuss how it might affect the conclusions. Additionally, the simulations fix the PCNA structure and only allow the C-terminal eight residues to move, which may bias the results.  
- **Why it matters** The proposed dynamic exchange model relies on the simulated conformations. If the simulations are not representative of physiological conditions, the model may be incorrect.  
- **Resolution test** Perform simulations at more physiologically relevant salt concentrations, or at least discuss the potential impact of the low salt conditions on the conclusions. Also, consider allowing more flexibility in the PCNA structure.

### Minor Comments

- **Concern ID** R1-m1  
- **Severity** Minor  
- **Axis** Clarity of writing  
- **Affected element** Results section, "Spd1 is intrinsically disordered but compact"  
- **Evidence pointer** Figure 1B.  
- **Issue** The description of the secondary chemical shift analysis is brief, and the criteria for defining "transient helicity" are not explicitly stated.  
- **Required correction** Provide a brief description of the criteria used to identify transient helical regions, or refer to a previous publication where this is described in detail.

- **Concern ID** R1-m2  
- **Severity** Minor  
- **Axis** Data presentation  
- **Affected element** Results section, "The two PCNA-binding motifs of Spd1 bind to and exchange rapidly in the same site"  
- **Evidence pointer** Figure 3C.  
- **Issue** The statement that chemical shift changes are "sometimes in the same direction and sometimes in opposite directions" is vague. It would be helpful to show a quantitative comparison or statistical analysis.  
- **Required correction** Provide a more quantitative comparison of the CSP patterns, such as a correlation plot or a table of affected residues.

- **Concern ID** R1-m3  
- **Severity** Minor  
- **Axis** Discussion of limitations  
- **Affected element** Discussion section  
- **Evidence pointer** Not applicable.  
- **Issue** The discussion of the potential role of post-translational modifications is speculative and not directly supported by data presented in this manuscript.  
- **Required correction** Clearly distinguish between findings from this study and speculative suggestions for future work.

- **Concern ID** R1-m4  
- **Severity** Minor  
- **Axis** Referencing  
- **Affected element** Introduction and Discussion  
- **Evidence pointer** Not applicable.  
- **Issue** Some statements about the prevalence of tandem PCNA-binding motifs in other proteins are made without specific references.  
- **Required correction** Add appropriate references to support these claims, or soften the language to indicate that this is a hypothesis.

## Risk / unsupported claims
- The claim that the two motifs "exchange rapidly" on PCNA is inferred from NMR data but not directly measured. The timescale of exchange is not quantified.
- The suggestion that "similar mechanisms may be relevant in other PCNA binding ligands" is speculative and not supported by data presented in this manuscript.
- The statement that the PIP-degron mutant "probably not only loses its ability to bind PCNA, but also compromises interaction with Suc22R2" is presented as a proposal, but the data supporting this are indirect.
- The functional significance of the "compactons" observed in simulations is not experimentally validated.