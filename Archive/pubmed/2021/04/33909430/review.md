## Review setup
- **Input scope** Full manuscript text
- **Assessment boundary** Scientific content, methodology, and conclusions as presented in the provided manuscript text
- **Shared manuscript claim summary** The authors investigate phosphorylation-induced folding of the intrinsically disordered protein 4E-BP2 (pT37pT46 4E-BP218–62) using coarse-grained UNRES molecular dynamics simulations. They identify key residues and interactions driving folding, describe two distinct folding pathways, and demonstrate that a kink-based analysis of the experimental structure alone can identify phosphorylation sites and regions governing folding and stability.
- **Visible evidence base** Abstract, full Methods, full Results and Discussion, Conclusions, Acknowledgments
- **Missing materials affecting confidence** Figures 1–13 referenced but not provided; Supporting Information (including Principal Component Analysis details, Eq. S11–S19, Figures S1–S3) not provided; simulation trajectory data not available for independent verification

## Reviewer

- **Overall assessment** This manuscript presents a detailed computational analysis of phosphorylation-induced folding in an intrinsically disordered protein using coarse-grained simulations. The work combines multiple analytical approaches (MREMD, PCA, free-energy landscapes, contact analysis, kink analysis) to provide a multi-faceted view of the folding mechanism. The identification of two distinct folding pathways and the correlation between local and global motions are potentially valuable contributions. However, the absence of all figures and supporting information severely limits the ability to evaluate the technical soundness of the analyses and the validity of the conclusions. The kink-based analysis, while conceptually interesting, requires more rigorous validation to establish its predictive power beyond post-hoc description.

- **Who would be interested in the results, and why** Researchers in the fields of intrinsically disordered proteins, protein folding mechanisms, phosphorylation regulation, and coarse-grained simulation methodology would find this work relevant. The identification of specific residues and interaction patterns governing phosphorylation-induced folding could inform experimental studies of 4E-BP2 and similar IDP systems. The application of kink-based analysis to predict functionally important sites without simulations may interest researchers developing simplified models of protein structure and dynamics.

- **Major strengths** 
  1. The study addresses a biologically important question (how phosphorylation induces folding in IDPs) with potential implications for understanding cell signaling regulation.
  2. The combination of multiple analytical techniques (MREMD, PCA, FEL, contact analysis, kink analysis) provides a comprehensive approach to studying the folding mechanism.
  3. The comparison between phosphorylated and wild-type proteins helps isolate the specific effects of phosphorylation.
  4. The identification of two distinct folding pathways adds nuance to the understanding of IDP folding.
  5. The attempt to connect simulation results with experimental structural data (NMR structure 2MX4) grounds the work in empirical observations.

- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors claim that MREMD simulations reveal that pT37pT46 4E-BP218–62 folds into the experimentally determined structure while WT does not fold, with RMSD values of 5.21 Å and 9.93 Å respectively.
- **Evidence pointer** Results and Discussion, "Weighted Histogram Analysis with Clustering of MREMD Trajectories" section; Figure 2 (not provided)
- **Concern** The central claim of successful folding rests entirely on RMSD values and cluster probabilities, but the corresponding figure is not available for inspection. An RMSD of 5.21 Å for a 45-residue fragment is relatively high and may not convincingly demonstrate that the simulated structure matches the experimental fold. The authors do not report the distribution of RMSD values, the fraction of conformations within a specified threshold, or any statistical comparison against unfolded ensembles. Without this information, it is difficult to assess whether the observed "folding" is statistically significant or merely represents a low-probability event captured in the simulations.
- **Why it matters** The demonstration that the simulations reproduce the experimental folded state is foundational to all subsequent analyses. If the folding event is not robustly established, the identified pathways, key residues, and mechanistic conclusions lose their evidentiary basis.
- **Resolution test** Provide the missing figure and additional quantitative metrics: distribution of RMSD values across all replicas, comparison of simulated ensembles against the experimental structure using multiple structural similarity measures (e.g., TM-score, contact map overlap), and statistical significance testing against a null model of unfolded conformations.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors claim that analysis of distances between Cα atoms of selected residue pairs reveals the order of formation of β-hairpins and the role of hydrophobic interactions in folding and stabilization.
- **Evidence pointer** Results and Discussion, "Mechanisms of Hairpin Folding and Protein Stabilization" section; Figure 6 (not provided)
- **Concern** The selection of residue pairs for distance analysis appears arbitrary, and the criteria for choosing these specific pairs are not stated. The authors mention that pairs contain "both hydrophobic and phosphorylated residues" but do not explain how these pairs were selected from the many possible combinations. The interpretation of distance time series as evidence for specific folding mechanisms requires more rigorous analysis, such as statistical correlation with folding events, comparison against control pairs, or validation through perturbation studies. The claim that hydrophobic interactions "enforce" β-hairpin formation is a causal statement that distance correlations alone cannot support.
- **Why it matters** The proposed folding mechanism (phosphorylation initiates loop formation, followed by hydrophobic collapse and salt bridge stabilization) is a key conclusion of the paper. If the evidence for this mechanism is based on selective and potentially biased analysis of residue pairs, the mechanistic claims are not adequately supported.
- **Resolution test** Justify the selection of residue pairs using objective criteria (e.g., all pairs within a distance threshold in the experimental structure, or pairs identified through systematic screening). Provide statistical analysis of distance correlations, including significance testing and control comparisons. Consider mutational or perturbation analyses to test causal claims about specific interactions.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors claim that kink analysis of the experimental structure alone can identify phosphorylated sites, key residues governing folding, and reasons for weak stability, without requiring MD simulations.
- **Evidence pointer** Results and Discussion, "Investigation of the experimental structure of the pT37pT46 4E-BP218–62 in terms of kinks" section; Figures 10–13 (not provided)
- **Concern** The kink analysis is presented as a predictive tool, but the methodology appears to be applied post-hoc to the known folded structure. The authors state that "multi-kink structures that are combinations of 7 individual kinks" were obtained, and that kink centers at positions 37 and 48 (corresponding to phosphorylation sites) were found in all structures. However, the selection of 7 kinks, the fitting procedure, and the criteria for determining kink centers are not described in sufficient detail. The claim that kinks "capture" phosphorylation sites and regions governing folding requires validation against a null hypothesis: would kink analysis of any protein structure identify functionally important sites at a rate exceeding chance? The comparison between the three representative structures and the experimental structure (RMSD < 1.0 Å) is noted, but the significance of this agreement is unclear without understanding the degrees of freedom in the fitting procedure.
- **Why it matters** The kink-based analysis is presented as a complementary, model-independent approach that can identify functionally important regions without simulations. If this claim is not rigorously validated, the broader applicability of the method is questionable, and the connection between the kink analysis and the MD simulation results is weakened.
- **Resolution test** Provide a detailed description of the kink fitting procedure, including the number of free parameters and the optimization criteria. Validate the predictive power of kink analysis on a test set of proteins with known functional sites, comparing against random expectation. Demonstrate that the kink centers at phosphorylation sites are statistically significant and not an artifact of the fitting procedure.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Reproducibility
- **Claim pointer** The authors state that "80 canonical MD trajectories" and "40 multiplexed replica exchange molecular dynamics simulations" were carried out with the UNRES force field, with specific simulation lengths and temperature conditions.
- **Evidence pointer** Methods, "Molecular Dynamics Simulations" section
- **Concern** The simulation parameters are described, but essential details for reproducibility are missing. The authors do not specify the version of the UNRES force field used, the exact simulation protocol (e.g., equilibration procedure, integration time step, cutoff schemes), or the criteria for determining convergence. The statement that "the time used in the Results and Discussion section is the UNRES time" is confusing, as the relationship between UNRES time and physical time is not clearly explained. The selection of only two folding trajectories and one nonfolding trajectory for detailed analysis from the 80 canonical simulations raises questions about selection bias and representativeness.
- **Why it matters** Reproducibility is a fundamental requirement for computational studies. Without complete simulation details, other researchers cannot replicate the results or assess the robustness of the findings. The selective analysis of a small number of trajectories without clear selection criteria undermines confidence in the generality of the conclusions.
- **Resolution test** Provide complete simulation protocols, including force field version, equilibration procedures, and convergence criteria. Justify the selection of trajectories for detailed analysis using objective criteria. Clarify the relationship between UNRES time and physical time, or avoid claims that imply direct physical interpretation.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Abstract
- **Evidence pointer** Abstract, first sentence
- **Issue** The opening sentence states that phosphorylation is "the most common mechanism of regulating protein function" without qualification. While phosphorylation is indeed a major regulatory mechanism, the claim of being "the most common" is debatable and not supported by a citation.
- **Required correction** Qualify the statement (e.g., "one of the most common mechanisms") or provide a supporting reference.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Technical soundness
- **Affected element** Methods, "Molecular Dynamics Simulations" section
- **Evidence pointer** Methods section, simulation length description
- **Issue** The simulation lengths are reported in steps (8 × 10^7 and 4 × 10^7 steps) and converted to UNRES time, but the conversion factor and its basis are not explained. The statement that UNRES time should be multiplied by ~1000 to compare with actual time is presented without justification.
- **Required correction** Provide a clear explanation of the time conversion, including the physical basis for the ~1000 factor, or present results in a way that avoids potential confusion about time units.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Results and Discussion, "Free-energy Landscape and Folding/Nonfolding Pathways" section
- **Evidence pointer** Figure 5 (not provided)
- **Issue** The authors state that the first two PCs capture ~35% of total fluctuations in the first folding trajectory and ~25% in the other two trajectories, and note that previous work suggested at least 40% is needed for accurate FEL description. They then state that examining 3D and 5D PC spaces did not reveal new major basins. However, the results of this higher-dimensional analysis are not shown or described in sufficient detail.
- **Required correction** Provide the results of the higher-dimensional PC analysis, either in the main text or Supporting Information, to support the claim that 2D FELs are sufficient.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Results and Discussion, "FEPs Along θi and γi Angles" section
- **Evidence pointer** Figure 9 (not provided)
- **Issue** The comparison between folding and nonfolding trajectories identifies differences in specific residues (e.g., "i = 27 – 29" and "i = 57"), but the biological or structural significance of these specific residues is not discussed. The reader is left to infer why these particular positions matter.
- **Required correction** Provide structural context for the identified residues, such as their location in the folded structure or their proximity to phosphorylation sites, to help readers understand the significance of the findings.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Technical soundness
- **Affected element** Results and Discussion, "Investigation of the experimental structure" section
- **Evidence pointer** Figure 12 (not provided)
- **Issue** The heating/cooling analysis using the Glauber algorithm is described, but the relationship between the Glauber temperature and physical temperature is not explained. The interpretation of the results in terms of protein stability requires this connection.
- **Required correction** Clarify the relationship between Glauber temperature and physical temperature, or present the results in a way that does not require this mapping for interpretation.

## Risk / unsupported claims
- The claim that pT37pT46 4E-BP218–62 folds into the experimentally determined structure based on MREMD simulations cannot be fully evaluated without the referenced figures and quantitative structural comparison metrics.
- The claim that kink analysis can identify phosphorylation sites and regions governing folding without MD simulations is not validated against null hypotheses or control analyses.
- The mechanistic model of folding (phosphorylation initiates loop formation, followed by hydrophobic collapse and salt bridge stabilization) is based on selective trajectory analysis and lacks statistical rigor.
- The correlation between local and global motions is asserted but the quantitative measure of correlation and its statistical significance are not reported.
- The claim that the protein exhibits "weak stability" is supported by simulation observations and kink analysis, but no quantitative free energy barriers or stability measures are provided.
- The biological implications of the two distinct folding pathways are not discussed in terms of functional consequences or regulation.