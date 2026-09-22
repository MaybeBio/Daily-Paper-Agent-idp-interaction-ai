## Review setup
- **Input scope** Full manuscript text (abstract, introduction, results, discussion, methods) as provided
- **Assessment boundary** Scientific content, experimental logic, internal consistency, and support for claims based solely on the supplied text
- **Shared manuscript claim summary** The authors propose that arbitrarily large particles can partition into biomolecular condensates if particle-condensate interactions are sufficiently strong, and that this partitioning can be made orthogonal to target distinct condensates in multi-component systems
- **Visible evidence base** Experimental results with dextrans, polystyrene beads, PEGylated beads, biotin-functionalized beads, oligonucleotide-conjugated beads; coarse-grained molecular dynamics simulations; analytical theory
- **Missing materials affecting confidence** Figures, supplementary information, methods details, simulation parameters, and raw data are referenced but not provided

## Reviewer
- **Overall assessment** This manuscript addresses a timely and important question in the biology of biomolecular condensates: whether large particles can partition into condensates when interactions are sufficiently strong. The authors combine experiments with polymer nanoparticles, simulations, and theory to argue that size is not an absolute barrier to partitioning. The central claim is plausible and the experimental design is thoughtful, particularly the use of PEGylation to create an inert platform and the subsequent functionalization with specific ligands. However, the provided text lacks the actual data, figures, and methodological detail needed to verify the quantitative claims. Several statements in the results section are presented without supporting numbers or statistical information. The theoretical model is described only briefly, and its assumptions are not fully justified. The manuscript would benefit from clearer presentation of the relationship between the simulations and the experimental system, and from a more careful discussion of the limitations of the model. The orthogonal partitioning result is intriguing but the evidence for it is not visible in the supplied material. Overall, the conceptual advance is significant and the work is likely to interest a broad readership, but the current submission does not allow full evaluation of the technical soundness of the claims.

- **Who would be interested in the results, and why** Researchers studying biomolecular condensates and phase separation, particularly those interested in client partitioning and condensate composition. The work may also appeal to synthetic biologists designing condensate-based systems, drug delivery researchers targeting condensates, and biophysicists studying the physics of particle transport in dense polymer networks. The orthogonal partitioning concept could be of interest to those working on multi-condensate systems in cells.

- **Major strengths** The question is well motivated and addresses a gap in the literature. The experimental strategy is logical, using a modular platform (PEGylated beads) to isolate the effect of specific interactions. The combination of experiments, simulations, and theory is appropriate for the question. The finding that partitioning can be tuned by ligand density and length, and that orthogonal partitioning is possible, is conceptually interesting and potentially useful.

- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence
- **Claim pointer** The authors claim that "arbitrarily large particles can controllably partition into biomolecular condensates given sufficiently strong condensate-particle interactions"
- **Evidence pointer** Results section, Figures 1-4 (figures not provided)
- **Concern** The central claim of the manuscript is that there is no upper size limit for particle partitioning into condensates, provided interactions are strong enough. However, the largest particles tested in the experiments are 1 μm polystyrene beads, and the simulations use particles that are only up to 3 times the size of the protein particles. The text does not provide evidence for particles larger than 1 μm, and the claim of "arbitrarily large" is not supported by the data shown. The theoretical argument suggests a linear scaling of required interaction strength with particle radius, but this is only derived for the simplified LJ model and its applicability to real condensates is not demonstrated.
- **Why it matters** The claim of "arbitrarily large" is a strong statement that goes beyond the presented evidence. If the authors wish to make this claim, they need to either test larger particles or provide a more rigorous theoretical argument that the trend continues indefinitely. As written, the claim is not established from the supplied material.
- **Resolution test** Provide experimental data for particles larger than 1 μm, or provide a theoretical argument with clear assumptions that demonstrates the scaling holds for arbitrarily large particles. Alternatively, soften the claim to reflect the tested size range.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors state that "Particles coated with polyethylene glycol (PEG) did not partition into condensates" and use this as evidence that PEGylation creates an inert surface
- **Evidence pointer** Results section, Figure 1D, SI Appendix Table 1
- **Concern** The text states that PS-PEG beads are "essentially completely excluded" from condensates, but no quantitative data are provided. The zeta-potential measurements are mentioned in SI Appendix Table 1, but the values are not given in the text. The claim that PEGylation creates an inert surface is critical to the experimental design, as it is the baseline against which all functionalized particles are compared. Without quantitative evidence of exclusion, the interpretation of subsequent experiments is weakened.
- **Why it matters** The entire experimental strategy relies on the assumption that PEGylated beads are inert and excluded from condensates. If this is not rigorously demonstrated, the conclusions about specific interactions driving partitioning are less secure.
- **Resolution test** Provide quantitative partitioning data (e.g., partition coefficients with error bars) for PEGylated beads across the range of condensate types and sizes tested. Show that the zeta-potential is near-neutral and that this is sufficient to prevent non-specific interactions.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence
- **Claim pointer** The authors claim that "oligonucleotide-decorated particles exhibited varying degrees of partitioning into condensates, depending on condensate composition" and that partitioning was tuned by salt concentration, oligonucleotide length, and surface density
- **Evidence pointer** Results section, Figure 4, SI Appendix Figures S5-S10
- **Concern** The text describes a series of experiments varying salt, oligonucleotide length, and density, but no quantitative results are presented. The partition coefficients or fractions are not given, and the figures are not available. The claim that partitioning is "tuned" implies a systematic relationship, but the text does not show this relationship. The comparison between different conditions is described qualitatively, which is insufficient to support the quantitative claim of tuning.
- **Why it matters** The tunability of partitioning is a key result of the paper, with implications for both biology and drug delivery. Without quantitative data, the reader cannot assess the strength of the effect or the precision of the tuning.
- **Resolution test** Provide quantitative partitioning data (e.g., partition coefficients or fractions) for each condition tested, with appropriate statistical analysis. Show the relationship between salt concentration, oligonucleotide length, density, and partitioning.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors state that "our coarse-grained molecular dynamics simulations and theory" support the conclusion that arbitrarily large particles can partition into condensates
- **Evidence pointer** Results section, Figure 2, SI Appendix (methods and theory)
- **Concern** The simulation model is described only briefly. The authors use a simple LJ system with "protein" and "bead" particles, but the mapping to the experimental system is not clear. The parameters used, the system size, the equilibration protocol, and the method for calculating partition coefficients are not described in the text. The analytical theory is presented as an equation, but its derivation and assumptions are not given. The relationship between the simulation results and the experimental observations is asserted but not demonstrated in detail.
- **Why it matters** The simulations and theory are used to support the central claim of the paper. If the model is not adequately described or validated, the strength of the conclusion is diminished. The reader cannot assess whether the simulation results are robust or whether the theory captures the essential physics.
- **Resolution test** Provide a detailed description of the simulation model, including parameters, system setup, and analysis methods. Show that the simulation results are converged and robust to parameter choices. Provide a derivation of the theoretical expression and discuss its assumptions and limitations.

- **Concern ID** R1-M5
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence
- **Claim pointer** The authors claim that "beads with distinct surface chemistries partitioned orthogonally into immiscible condensates" and that this was due to the biomolecules on the particle surface
- **Evidence pointer** Results section, Figure 6
- **Concern** The orthogonal partitioning result is presented as a key finding, but the evidence is not visible in the supplied text. The authors state that PS-PEG-biotin partitioned into SA-RGG condensates and PS-PEG-polyA20 into N protein condensates, but no quantitative data are provided. The control experiments to rule out effects of the particle core or fluorescent dyes are mentioned but not shown. The claim of "overwhelmingly" partitioning is not supported by numbers.
- **Why it matters** Orthogonal partitioning is a significant advance with potential applications. If the evidence is not robust, the claim is weakened. The reader needs to see the data to assess the specificity of the targeting.
- **Resolution test** Provide quantitative data showing the fraction of each particle type in each condensate type, with appropriate controls. Show that the orthogonal partitioning is reproducible and specific.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Introduction, statement about "terminally viscous" condensates
- **Evidence pointer** Introduction, paragraph 2
- **Issue** The phrase "terminally viscous" is not standard terminology and is not defined. The concept is important for the argument that particles can diffuse through condensates, but the term is unclear.
- **Required correction** Define what is meant by "terminally viscous" or use more standard terminology such as "viscoelastic" or "viscous on the timescale of particle diffusion."

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Results, section on simulations
- **Evidence pointer** Results, "Simulations demonstrate competing effects of size and protein-particle attraction"
- **Issue** The text states that the simulation results "largely recapitulate the observations from experiments" but does not specify which observations or how the comparison was made. The link between the simplified LJ model and the complex experimental system is not clear.
- **Required correction** Clarify the specific experimental observations that are recapitulated and describe the criteria used for comparison.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Discussion, paragraph on drug delivery
- **Evidence pointer** Discussion, paragraph 4
- **Issue** The discussion of drug delivery implications is speculative and does not address potential challenges, such as the stability of the particles in biological environments or the accessibility of condensates in cells.
- **Required correction** Add a brief discussion of the limitations and challenges of applying this approach to drug delivery in vivo.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Reproducibility
- **Affected element** Methods section
- **Evidence pointer** Methods, paragraph 1
- **Issue** The methods section is very brief and refers to the SI for details. While this is acceptable for a preprint, the text should include enough information for the reader to understand the key experimental procedures.
- **Required correction** Provide a brief description of the key experimental procedures, such as the preparation of condensates, the conjugation of ligands to beads, and the measurement of partitioning.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Internal consistency
- **Affected element** Results, section on dextran partitioning
- **Evidence pointer** Results, "Partitioning into condensates depends on client size and binding interactions"
- **Issue** The text states that the partition coefficient of 70 kDa dextran was "5-fold lower" than that of 10 kDa dextran, but the actual values are not given. It is unclear whether this is a consistent finding across all three condensate types.
- **Required correction** Provide the actual partition coefficient values and indicate the variability across condensate types.

## Risk / unsupported claims
- The claim that "arbitrarily large particles" can partition into condensates is not supported by the provided evidence, as the largest tested particles are 1 μm and the simulations use particles only up to 3 times the protein size.
- The claim that PEGylated beads are "essentially completely excluded" from condensates is not quantitatively supported.
- The claim that partitioning can be "tuned" by salt, oligonucleotide length, and density is not quantitatively supported.
- The claim of "orthogonal partitioning" is not supported by visible data.
- The theoretical model is not described in sufficient detail to assess its validity or applicability to the experimental system.
- The relationship between the simulation results and the experimental observations is asserted but not demonstrated.