## Review setup
- **Input scope** Full manuscript text including abstract, introduction, methods, results, discussion, and supplementary figure references
- **Assessment boundary** Scientific validity, technical soundness, and support of claims based on the provided manuscript text and referenced figures
- **Shared manuscript claim summary** The authors use atomistic molecular simulations of RNA tetranucleotides to show that Mg2+ ions promote lower critical solution temperature (LCST) behavior in RNA condensates through local order-disorder transitions, that base-specific interactions (hydrogen bonding, pi-stacking, base pairing) produce a thermal stability hierarchy Poly(G) > Poly(A) > Poly(C) > Poly(U), and that N6-methylation of adenine suppresses phase separation
- **Visible evidence base** Main text figures 1-5 as described in the results sections, supplementary figures SI 1-18 as referenced, methods description of simulation protocols
- **Missing materials affecting confidence** Actual figure data and numerical values are not provided, only figure descriptions; simulation convergence criteria are described qualitatively; force field validation details are not provided; no error bars or statistical analysis are shown in the text

## Reviewer
- **Overall assessment** The manuscript addresses an important and timely question in the field of RNA phase separation, namely the molecular origins of base-specific LCST behavior and the role of divalent cations. The simulation approach is appropriate and the systematic variation of sequence, ion conditions, and chemical modification is commendable. However, the evidence presented in the text is largely qualitative, with key quantitative data (phase diagrams, density profiles, interaction energies) only described verbally rather than shown with numerical values. The claim that Mg2+ drives LCST through local order-disorder transitions requires more direct structural evidence. The connection between tetranucleotide simulations and biologically relevant longer RNAs is not adequately discussed. The m6A result, while interesting, appears to contradict some experimental observations, and this discrepancy is not fully resolved.

- **Who would be interested in the results, and why** Researchers studying biomolecular condensates, RNA biology, and phase separation mechanisms would be interested. The work is also relevant to the broader biophysics community interested in the molecular determinants of liquid-liquid phase separation and the role of ions in modulating biomolecular interactions. The findings on base-specific interaction hierarchies could inform the design of RNA-based synthetic condensates and the understanding of RNA repeat expansion disorders.

- **Major strengths** The systematic approach comparing four homopolymeric RNAs under controlled ionic conditions is well designed. The use of explicit solvent simulations with a modern force field and optimized Mg2+ parameters is technically appropriate. The study addresses a gap in the literature by focusing on RNA-only condensates, which are less studied than protein-RNA systems. The inclusion of m6A modification provides a biologically relevant perturbation. The connection between microscopic interaction analysis (hydrogen bonding, pi-stacking, phosphate-base contacts) and macroscopic phase behavior is a strength.

- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence quality and quantitative support
- **Claim pointer** The authors claim that Mg2+ ions promote LCST behavior by inducing local order-disorder transitions within RNA structures, and that this is the key mechanism driving temperature-dependent phase separation
- **Evidence pointer** Results section "On the role of mono- and divalent ions in RNA condensate formation", Figure 1 and Figure 2
- **Concern** The claim that Mg2+ drives LCST through local order-disorder transitions is not supported by direct structural evidence in the text. The authors describe cluster size and density changes with temperature, and show shifts from outer-sphere to inner-sphere Mg2+ coordination, but do not provide quantitative measures of RNA structural order or disorder (e.g., base pairing fractions, stacking geometries, conformational entropy estimates) as a function of temperature. The term "order-disorder transition" implies a structural characterization that is not presented.
- **Why it matters** The central mechanistic claim of the paper rests on this order-disorder transition concept. Without direct structural evidence, the proposed mechanism remains speculative. The distinction between a true order-disorder transition and simply increased compaction due to enhanced ion coordination is not established.
- **Resolution test** Provide quantitative structural order parameters (e.g., fraction of stacked bases, hydrogen bond occupancy, backbone dihedral distributions) as a function of temperature for each system. Show that these parameters change cooperatively at the LCST and that the changes correlate with Mg2+ coordination state. Alternatively, provide free energy decompositions showing the entropic and enthalpic contributions to phase separation.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Quantitative data presentation
- **Claim pointer** The authors map "equilibrium thermodynamic profiles" and "phase diagrams" for RNA condensates across temperatures and ionic conditions
- **Evidence pointer** Results sections, Figures 1, 3, and supplementary figures SI 1-7, SI 13
- **Concern** The manuscript text describes phase behavior qualitatively (e.g., "cluster size and density consistently increase with temperature", "cluster size order follows Poly G ~ Poly A > Poly C ~ Poly U") but does not present actual phase diagrams, coexistence curves, or quantitative thermodynamic quantities (e.g., critical temperatures, free energies of transfer, chemical potentials). The convergence assessment is described as "bootstrapping on the time series of cluster sizes" but no convergence metrics or error estimates are reported.
- **Why it matters** The claim of mapping "equilibrium thermodynamic profiles" requires quantitative phase diagrams with defined coexistence regions and critical points. Without numerical values, the reader cannot assess the precision of the reported LCSTs, the width of coexistence regions, or the statistical significance of differences between sequences. This limits the utility of the data for comparison with experiments or other simulations.
- **Resolution test** Present phase diagrams with temperature on the y-axis and density or concentration on the x-axis, with coexistence boundaries clearly marked. Report critical temperatures with uncertainties. Provide convergence metrics (e.g., block averages, autocorrelation times) for cluster size distributions. Include error bars on all reported quantities.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Biological relevance and extrapolation
- **Claim pointer** The authors state that their findings "provide a conceptual framework for understanding how cellular factors regulate RNA phase behavior" and that insights "are expected to enhance our understanding of the mechanisms underlying the formation of various cellular membraneless condensates"
- **Evidence pointer** Discussion section
- **Concern** The simulations use tetranucleotides at approximately 160 mg/mL, which is far from physiological conditions in terms of RNA length, concentration, and sequence complexity. The authors acknowledge the concentration is "pragmatically" chosen, but do not discuss how results from tetranucleotides extrapolate to biologically relevant RNAs (hundreds to thousands of nucleotides) with complex secondary structures and protein interactions. The claim of providing a framework for cellular condensates is therefore overstated.
- **Why it matters** The biological relevance of the findings depends on whether the interaction hierarchies and ion effects observed in short homopolymers persist in longer, sequence-diverse RNAs. Without discussion of length effects, crowding, or the presence of proteins, the extrapolation to cellular condensates is not justified.
- **Resolution test** Add a discussion section addressing the limitations of tetranucleotide models and how the identified interaction hierarchies might scale with RNA length. If possible, include preliminary simulations of longer RNAs (e.g., 10-20 nucleotides) to test whether the trends hold. Alternatively, temper the claims about cellular relevance and focus on the fundamental biophysics of RNA-RNA interactions.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Interpretation of m6A results
- **Claim pointer** The authors claim that N6-methylation of adenine suppresses phase separation by reducing hydrogen bonding and pi-stacking interactions
- **Evidence pointer** Results section "Effects of Adenine Methylation on RNA LLPS", Figure 5
- **Concern** The finding that m6A suppresses phase separation in the simulations is presented as a straightforward result, but the discussion notes that experimental studies show m6A enhances RNA-protein interactions and can promote condensate formation. The authors do not reconcile this apparent contradiction. The m6A modification could have different effects on RNA-RNA versus RNA-protein interactions, and the relevance of the simulation result to cellular contexts where m6A is known to promote condensate assembly is unclear.
- **Why it matters** The m6A result is presented as a key finding, but its biological interpretation is ambiguous given the experimental literature. Without addressing the discrepancy, the claim that m6A suppresses phase separation could be misleading to readers.
- **Resolution test** Add a more detailed discussion of how m6A affects RNA-RNA versus RNA-protein interactions, and clarify that the simulation result applies specifically to RNA-only condensates. If possible, simulate m6A-modified RNA in the presence of a peptide or protein to test whether the effect is reversed.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity and completeness
- **Affected element** Methods section, force field description
- **Evidence pointer** Methods section
- **Issue** The methods state that the Amber RNA force field parameters (parmBSC0χOL3) and OPC water model were used, and that optimized Mg2+ parameters (microMg) were employed. However, no citation or validation data for the microMg parameters is provided, and the choice of these parameters over alternatives is not justified.
- **Required correction** Add citations for the microMg parameters and briefly justify the choice. If validation data exists (e.g., comparison with experimental ion binding affinities), include it.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Data availability
- **Affected element** Data Availability statement
- **Evidence pointer** Data Availability section
- **Issue** The data availability statement says data are available in the article and supplementary material, but the supplementary material is not provided with the manuscript. The specific simulation input files, trajectories, and analysis scripts are not mentioned.
- **Required correction** Specify what data will be made available (e.g., input files, trajectories, analysis scripts) and where they will be deposited (e.g., Zenodo, GitHub). Consider depositing simulation inputs to enable reproducibility.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Consistency
- **Affected element** Discussion section, sequence list
- **Evidence pointer** Discussion section
- **Issue** The discussion states "Four distinct RNA tetranucleotides U4, G4, C4, and U4 were simulated" which lists U4 twice and omits A4. This appears to be a typographical error.
- **Required correction** Correct the sequence list to "U4, G4, C4, and A4".

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Figure quality
- **Affected element** Figure 1D
- **Evidence pointer** Results section, Figure 1D
- **Issue** The water density profile is described as displaying "an irregular well at lower temperatures" that "sharpens into a distinct single well" at higher temperatures. This description is vague and does not convey the quantitative nature of the change.
- **Required correction** Provide quantitative measures of the water density profile (e.g., depth of the well, width at half maximum) and consider showing the profiles for all temperatures in a single panel for direct comparison.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Statistical rigor
- **Affected element** Results section, cluster size analysis
- **Evidence pointer** Results section, Figure 3C
- **Issue** The cluster size analysis is described without any mention of statistical uncertainty. Given that the simulations are stochastic, replicate simulations or block averaging should be used to estimate errors.
- **Required correction** Report standard errors or confidence intervals for cluster size and density measurements. If only single trajectories were used, acknowledge this limitation.

- **Concern ID** R1-m6
- **Severity** Minor
- **Axis** Literature context
- **Affected element** Introduction and Discussion
- **Evidence pointer** Introduction and Discussion sections
- **Issue** The introduction cites recent reports of RNA-only condensates but does not provide specific references for these claims. The discussion references experimental studies on m6A and RNA condensates but does not cite them explicitly.
- **Required correction** Add specific citations for the claims about RNA-only condensates and for the experimental m6A studies mentioned in the discussion.

## Risk / unsupported claims
- The claim that Mg2+ induces "local order-disorder transitions" is not directly supported by structural evidence presented in the text
- The claim of mapping "equilibrium thermodynamic profiles" is not supported by quantitative phase diagrams or thermodynamic quantities
- The claim that the findings provide a "conceptual framework for understanding how cellular factors regulate RNA phase behavior" is overstated given the use of short homopolymeric tetranucleotides at non-physiological concentrations
- The m6A result showing suppression of phase separation is presented without reconciliation with experimental observations showing m6A can promote condensate formation
- The statement that "the overall condensation ability is Poly G > Poly A > Poly C > Poly U" is based on qualitative descriptions of cluster size and density without reported numerical values or statistical significance tests
- The convergence of simulations is claimed but not demonstrated with quantitative metrics
- The biological relevance of the findings to disease contexts mentioned in the discussion is not supported by any direct evidence in the manuscript