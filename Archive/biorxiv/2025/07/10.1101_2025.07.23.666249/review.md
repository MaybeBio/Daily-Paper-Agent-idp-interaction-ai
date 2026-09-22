## Review setup
- **Input scope** Full manuscript text (abstract, introduction, results, discussion, conclusion, methods, and supplementary figure captions as referenced)
- **Assessment boundary** Scientific validity, technical soundness, and significance of the claims as presented in the provided manuscript text. No assessment of the supplementary figures or movies is possible as they were not provided.
- **Shared manuscript claim summary** The authors present all-atom molecular dynamics simulations of the full translocation of wild-type α-synuclein and two pathogenic mutants (A30P, E46K) through MoS₂ nanopores. They claim this is the first atomistic simulation of full-length protein sequencing through a 2D solid-state nanopore, and that their ionic current traces, stepwise signal analysis, and volume-based fingerprinting can differentiate the wild-type from mutant proteins, offering a roadmap for experimental validation.
- **Visible evidence base** Main text figures (Figures 1–4), Tables (Table 1), Methods section, and references to supplementary figures and movies. The supplementary materials themselves were not provided.
- **Missing materials affecting confidence** Supplementary figures (S1–S3), supplementary movies (S1–S2), the exact ionic current calculation equation (referenced but not shown), the exact volume calculation equation (referenced but not shown), and the DTW distance matrix data underlying Figure 2c.

## Reviewer
- **Overall assessment** This manuscript presents a substantial computational effort, with over 22 µs of cumulative all-atom MD simulation time, to model the translocation of a full-length intrinsically disordered protein through a MoS₂ nanopore. The work addresses a timely and important problem in nanopore-based protein sequencing. The authors employ a multi-faceted analytical approach, including ionic current prediction, stepwise signal segmentation, clustering, and volume-based fingerprinting. However, the manuscript has several significant technical and conceptual issues that must be addressed before the central claims can be considered established. The most critical concerns are the use of biased simulation methods (umbrella pulling) that may dominate the translocation dynamics, the lack of a clear demonstration that the simulated ionic current signals can uniquely identify sequence features or mutations, and the absence of key methodological details and validation metrics. The claim of being the "first" such simulation is also difficult to verify from the provided text. While the work is potentially interesting to the nanopore and single-molecule biophysics community, the current evidence does not fully support the strong conclusions drawn.
- **Who would be interested in the results, and why** Researchers in the fields of nanopore sensing, single-molecule biophysics, computational biophysics, and neurodegenerative disease biomarkers. The work is relevant to those developing protein sequencing technologies and those interested in the dynamics of intrinsically disordered proteins under confinement. The methodological approach to analyzing MD-derived ionic current traces may also be of interest to computational scientists.
- **Major strengths**
    1.  The scale of the simulations is impressive, with a cumulative simulation time exceeding 22 µs for a full-length protein, which is a significant computational undertaking.
    2.  The study addresses a clinically relevant problem, namely the detection of pathogenic mutations in α-synuclein, a key protein in Parkinson's disease.
    3.  The analytical framework, combining DTW, stepwise segmentation, and clustering, is a sophisticated approach to extracting information from complex MD trajectories.
    4.  The use of volume-based fingerprinting to link structural features to ionic current signals is a novel and insightful computational approach.
- **Major Concerns**
    - **Concern ID** R1-M1
    - **Severity** Major
    - **Blocking** Yes
    - **Axis** Technical soundness
    - **Claim pointer** The authors claim to have simulated the "full translocation" of α-synuclein and that the resulting ionic current traces can be used for sequencing and mutation discrimination.
    - **Evidence pointer** Methods: "Molecular Dynamics Simulations of Protein Translocation"; Results: Figure 2
    - **Concern** The simulations use a strong external electric field (0.1 V/nm, corresponding to 1 V bias) and, critically, an umbrella pulling potential applied to the N-terminal methionine to "promote translocation." This introduces a significant external biasing force that likely dominates the translocation dynamics. The manuscript does not adequately discuss how this bias affects the conformational sampling, the translocation pathway, and the resulting ionic current signals. The observed differences between the wild-type and mutants could be an artifact of the pulling protocol interacting with local sequence properties, rather than a reflection of the intrinsic translocation behavior under a realistic experimental driving force. The authors must demonstrate that the key features of the ionic current traces are robust to the pulling protocol, for example by comparing with simulations using only the electric field or with different pulling parameters.
    - **Why it matters** The central premise of the paper is that the simulated ionic current traces provide a realistic and predictive model for experimental nanopore sequencing. If the translocation process is largely dictated by an artificial pulling force, the physiological and experimental relevance of the results is severely compromised. The conclusions about mutation discrimination and sequence fingerprinting would be built on a potentially flawed foundation.
    - **Resolution test** The authors should provide a detailed analysis of the force exerted by the umbrella potential over time and along the protein sequence. They should also perform control simulations (or provide existing data) with a lower pulling force or no pulling at all to show that the qualitative features of the ionic current traces and the clustering results are not qualitatively dependent on the biasing protocol. A discussion of the free-energy landscape of translocation and the role of the bias would be necessary.
    - **Concern ID** R1-M2
    - **Severity** Major
    - **Blocking** Yes
    - **Axis** Technical soundness
    - **Claim pointer** The authors claim that the stepwise signals and clustering analysis can identify "sequence motifs" and that the "sequence fingerprints" can differentiate wild-type from mutant proteins.
    - **Evidence pointer** Results: "Stepwise Signals of Ionic Current Traces...", Figure 3, Table 1, Figure 4
    - **Concern** The manuscript does not provide a rigorous, quantitative demonstration that the identified "sequence fingerprints" are unique or specific enough to be used for sequencing. The analysis shows that the wild-type and mutants have different cluster distributions, but it does not show that a given ionic current trace can be unambiguously mapped back to a specific sequence or mutation. The correlation between the volume-based fingerprints and the ionic current is moderate (e.g., -0.61 for WT), and the manuscript does not address the predictive power or error rate of this mapping. The claim of "sequencing" implies a level of base-by-base or residue-by-residue identification that is not demonstrated. The authors need to provide a more quantitative assessment of the information content and discriminative power of their fingerprints, such as a confusion matrix for classifying the three variants based on their simulated traces.
    - **Why it matters** The title and abstract promise "sequencing" of a protein. The current analysis demonstrates that different proteins produce different ensemble statistics of ionic current blockade, which is a much weaker claim. Without a clear demonstration of the ability to identify specific sequence features or mutations from a single trace or a small set of traces, the central claim of the paper is overstated.
    - **Resolution test** The authors should perform a classification analysis. For example, they could train a classifier on the stepwise features (dwell time, I/I0) from a subset of the reads and test it on the remaining reads to see if the three variants can be reliably distinguished. They should also provide a measure of how well the sequence fingerprints can predict the presence of specific amino acids or motifs, perhaps by comparing the predicted sequence from the ionic current trace to the known sequence.
    - **Concern ID** R1-M3
    - **Severity** Major
    - **Blocking** No
    - **Axis** Scientific importance
    - **Claim pointer** The authors claim this is the "first atomistic simulation of a full-length protein sequencing through a 2D solid-state nanopore."
    - **Evidence pointer** Abstract; Introduction
    - **Concern** This claim of priority is difficult to verify from the provided text. The authors do not provide a comprehensive comparison with prior computational studies of protein translocation through 2D nanopores. While they cite some previous work, they do not explicitly state what distinguishes their work from any prior full-length protein simulations, if they exist. The claim is bold and requires a more thorough literature review to substantiate.
    - **Why it matters** The novelty and significance of the work are partly predicated on this claim of being the first. If this is not the case, the impact of the work is diminished. A clear and verifiable statement of novelty is essential for a high-impact claim.
    - **Resolution test** The authors should expand the introduction and discussion to explicitly compare their work with all relevant prior simulation studies of protein translocation through 2D nanopores, clearly stating the novelty of their approach (e.g., full-length protein, unbiased vs. biased, specific analysis methods). They should also be more cautious in their language, perhaps stating "to the best of our knowledge" and providing a more detailed justification for this claim.
- **Minor Comments**
    - **Concern ID** R1-m1
    - **Severity** Minor
    - **Axis** Readability for nonspecialists
    - **Affected element** Introduction
    - **Evidence pointer** Introduction, paragraph 1
    - **Issue** The introduction is dense and assumes significant background knowledge. The transition from the clinical problem of Parkinson's disease to the technical details of nanopore sequencing could be smoother for a general scientific audience.
    - **Required correction** Consider adding a brief, clear explanation of how a nanopore works for protein sequencing (e.g., the resistive pulse technique) in simpler terms before diving into the specifics of 2D materials and MD simulations.
    - **Concern ID** R1-m2
    - **Severity** Minor
    - **Axis** Technical soundness
    - **Affected element** Methods: "Ionic Current Traces recorded during Molecular Dynamics"
    - **Evidence pointer** Methods section
    - **Issue** The equation for calculating ionic current is referenced but not shown. The text states "given the equation:" but the equation itself is missing from the provided text. This is a critical methodological detail.
    - **Required correction** The full equation for ionic current calculation must be included in the Methods section.
    - **Concern ID** R1-m3
    - **Severity** Minor
    - **Axis** Technical soundness
    - **Affected element** Methods: "Monitoring Amino Acid Volume Occupancy in the Pore during Molecular Dynamics"
    - **Evidence pointer** Methods section
    - **Issue** Similar to the ionic current equation, the equation for the volume of the spherical cap is referenced but not shown. The text states "is given by:" but the equation is missing.
    - **Required correction** The full equation for the spherical cap volume must be included in the Methods section.
    - **Concern ID** R1-m4
    - **Severity** Minor
    - **Axis** Technical soundness
    - **Affected element** Results: "Ionic Current Traces from Nanopore Sequencing..."
    - **Evidence pointer** Figure 2c
    - **Issue** The DTW analysis is mentioned, and a distance matrix is shown, but the specific values or a statistical measure of the significance of the differences between the variants is not provided in the text. It is unclear if the observed differences in DTW distances are statistically significant given the small number of reads (n=5 per variant).
    - **Required correction** Provide a quantitative measure of the variability within and between groups (e.g., mean and standard deviation of DTW distances) and a statistical test to support the claim that the traces from different variants are significantly different.
    - **Concern ID** R1-m5
    - **Severity** Minor
    - **Axis** Readability for nonspecialists
    - **Affected element** Results: "Sequence Fingerprints from Ionic Current..."
    - **Evidence pointer** Figure 4
    - **Issue** The description of the "sequence fingerprints" is somewhat abstract. The text describes correlations and moving averages but does not provide a clear, intuitive explanation of what a "fingerprint" looks like and how it is interpreted.
    - **Required correction** Consider adding a more explicit description of the fingerprint plots, perhaps with a schematic or a more detailed walk-through of a specific example, to make the concept more accessible.

## Risk / unsupported claims
- The claim of being the "first atomistic simulation of a full-length protein sequencing through a 2D solid-state nanopore" is unverifiable from the provided text and requires a more thorough literature comparison.
- The claim that the approach offers a "roadmap for validating 2D nanopore-based protein sequencing" is an extrapolation, as the manuscript does not provide a clear experimental validation strategy or discuss potential experimental challenges (e.g., noise, bandwidth, protein capture) in sufficient detail.
- The claim that the identified "sequence fingerprints" can "differentiate the wild-type from the mutant proteins" is only weakly supported by the qualitative description of clustering and correlation analyses. A quantitative classification or prediction test is missing.
- The physiological relevance of the simulations is questionable due to the use of a strong pulling bias, and the manuscript does not adequately address the impact of this bias on the conclusions.