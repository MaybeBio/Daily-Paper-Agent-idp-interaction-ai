## Review setup
- **Input scope** Full manuscript text, including abstract, introduction, results, discussion, conclusions, computational methods, and supplemental figure references.
- **Assessment boundary** Scientific content, methodological rigor, validity of claims, and presentation quality. No assessment of formatting or journal fit beyond Nature-style criteria.
- **Shared manuscript claim summary** The authors use a β-variational autoencoder (β-VAE) and Markov State Models (MSMs) to analyze molecular dynamics (MD) simulations of α-synuclein (αS) in water and in the presence of the small molecule fasudil. They report that fasudil induces an "ensemble expansion" mechanism, increasing the number of metastable states from three (in water) to six (with fasudil), and that this is accompanied by changes in protein backbone entropy, while water entropy remains unperturbed. They propose this as a general mechanism for small-molecule binding to intrinsically disordered proteins.
- **Visible evidence base** Main text figures 1–9 (referenced), supplemental figures S1–S32 (referenced, not provided), computational methods section, and code availability statement.
- **Missing materials affecting confidence** Supplemental figures S1–S32 are referenced but not provided. The original 1500 µs trajectory from Robustelli et al. is not available for independent verification. Raw data, hyperparameter search details, and convergence criteria for the β-VAE and MSM are not fully described.

## Reviewer
- **Overall assessment** The manuscript presents a novel analytical pipeline combining β-VAE and MSM to dissect the conformational ensemble of an IDP in the presence of a small molecule. The central claim of "entropic expansion" is interesting and potentially significant, but the evidence provided is insufficient to fully establish this mechanism. The analysis relies heavily on a single, externally generated trajectory, and the comparison between apo and bound states is complicated by unequal simulation lengths (62 µs vs 1500 µs). The entropy calculations, while suggestive, are based on a single snapshot per state and may not be representative. The manuscript would benefit from clearer validation of the ML models, more robust statistical analysis, and a more critical discussion of limitations.
- **Who would be interested in the results, and why** Researchers in the fields of intrinsically disordered proteins, drug discovery for neurodegenerative diseases, and computational biophysics. The methodological combination of deep learning and MSM for IDP ensemble analysis will be of interest to computational chemists and biophysicists. The proposed "entropic expansion" mechanism could inform future drug design strategies targeting IDPs, which is a high-impact area.
- **Major strengths**
  1. The application of β-VAE for dimensionality reduction of IDP conformational ensembles is a modern and appropriate methodological choice, addressing the non-linear nature of the data.
  2. The study tackles a significant and challenging problem: understanding small-molecule interactions with IDPs, which are often considered "undruggable."
  3. The use of a long, state-of-the-art MD trajectory (1500 µs) from D. E. Shaw Research provides a high-quality dataset for the bound state.
  4. The analysis is multi-faceted, combining structural characterization, contact map analysis, entropy calculations, and kinetic information (MFPT), providing a comprehensive view.
- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence sufficiency
- **Claim pointer** The claim that fasudil induces an "ensemble expansion" mechanism, increasing the number of metastable states from three to six, is a central finding.
- **Evidence pointer** Section "2. Markov State Model delineates distinct binding competing states of α S in presence of the small-molecule drug", Figures 3c-d, Figure S10-S13.
- **Concern** The comparison between the apo (62 µs) and bound (1500 µs) ensembles is confounded by the vastly different simulation lengths. The authors attempt to address this by building an MSM on a 60 µs chunk of the fasudil trajectory (Figure S10), but this is not a sufficient control. A 60 µs chunk from a single continuous trajectory may not sample the same regions of phase space as 23 independent simulations starting from diverse conformations. The increased number of states in the fasudil system could simply reflect the more extensive sampling of the longer trajectory, not a genuine physical effect of the ligand. The authors must demonstrate that the six-state model is robust and not an artifact of sampling depth.
- **Why it matters** The "ensemble expansion" mechanism is the core scientific claim of the paper. If it is an artifact of unequal sampling, the entire premise of the study collapses.
- **Resolution test** The authors should perform a rigorous subsampling analysis. For example, they could build MSMs on multiple, independent 60 µs chunks of the fasudil trajectory and show that the six-state model is consistently recovered. They could also perform a "matching" experiment by running 23 independent simulations of the fasudil system for a total of 62 µs, mirroring the apo setup, and show that the six-state model still emerges. Alternatively, they could use a more sophisticated approach to compare the phase space sampled, such as spectral clustering or a direct comparison of the stationary distributions.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical validation
- **Claim pointer** The β-VAE is used to generate a 2D latent space that is the basis for the MSM construction.
- **Evidence pointer** Section "Computational Methods: Dimension reduction using β-Variational Autoencoder", Figure 1c-d, Figure S7-S8.
- **Concern** The validation of the β-VAE is insufficient. The choice of β = 1 × 10⁻¹² is extreme and essentially makes the model a standard VAE, which is known to suffer from posterior collapse. The authors state they chose this value based on minimum reconstruction RMSE, but this metric does not guarantee that the latent space is physically meaningful or that it preserves the slow dynamical features relevant for MSM construction. The VAMP-2 score comparison with tICA is a good start, but it is not a substitute for a thorough validation of the latent space. The authors should show that the latent space is smooth, continuous, and that the reconstruction error is uniformly low across the entire conformational space, not just on average.
- **Why it matters** The MSM is built on the 2D latent space. If the latent space is poorly conditioned or has artifacts (e.g., "dead zones" with high reconstruction error), the resulting MSM states and their populations will be unreliable, undermining all downstream analysis.
- **Resolution test** The authors should provide a more detailed analysis of the latent space. This could include: (1) a plot of reconstruction error as a function of position in the latent space; (2) a comparison of the latent space with other non-linear dimensionality reduction methods (e.g., UMAP, t-SNE); (3) a demonstration that the latent space preserves the known structural features of αS (e.g., by coloring the latent space with radius of gyration or secondary structure content); (4) a sensitivity analysis showing that the number of MSM states is robust to the choice of β and the number of latent dimensions.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Claim support
- **Claim pointer** The claim that "the entropy of the water remains unperturbed" upon fasudil binding.
- **Evidence pointer** Section "6. Entropic Signatures of Small Molecule Binding", Figure S22.
- **Concern** The water entropy calculation is based on a single snapshot from each macrostate, which is then re-solvated and simulated for only 20 ps. This is a very short timescale and a single configuration is unlikely to be representative of the entire macrostate. The 2PT method is sensitive to the local environment, and 20 ps may not be sufficient to equilibrate the water around the protein. The conclusion that water entropy is unperturbed is therefore based on very weak evidence.
- **Why it matters** The paper's title emphasizes "entropic expansion," and the claim that the effect is protein-centric (backbone entropy) rather than solvent-centric is an important part of the proposed mechanism. If the water entropy calculation is unreliable, this part of the mechanism is not established.
- **Resolution test** The authors should perform water entropy calculations on multiple snapshots from each macrostate (e.g., 10-20 snapshots spread across the trajectory) and run longer simulations (at least 100 ps, ideally longer) to ensure convergence. They should also report the standard error of the mean across these independent calculations. If the water entropy is indeed unperturbed across all states and snapshots, the claim would be much stronger.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Interpretability
- **Claim pointer** The claim that the "entropy expansion" mechanism is a general principle for small-molecule binding to IDPs.
- **Evidence point** Conclusions section.
- **Concern** The study is based on a single protein (αS) and a single ligand (fasudil). While the authors discuss the "entropic expansion" model, they do not provide any evidence that this is a general mechanism. The observed increase in metastable states could be specific to the αS-fasudil pair. The authors should temper their conclusions or provide additional evidence, such as analysis of a second ligand or a second IDP, to support the generality of their claim.
- **Why it matters** The broader significance of the work, and its potential impact on drug design, depends on the generality of the proposed mechanism. Overstating the findings could mislead future research.
- **Resolution test** The authors should either (1) soften the language in the conclusions to clearly state that this is a case study, or (2) provide additional data, even preliminary, on another system to support the generality of the "entropic expansion" mechanism.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Figure 1d
- **Evidence point** Section "1. Modulation of free energy landscape of α S in presence of fasudil", Figure 1d.
- **Issue** The description of the β-value selection is unclear. The text says "A β value of 1 × 10⁻¹² was chosen as this value gave us the minimum RMSE between the original and the reconstructed data." It is not clear if this is the minimum RMSE on the training set, validation set, or test set. If it is the training set, this could be a sign of overfitting.
- **Required correction** Clarify which dataset was used for the β selection. If it was the training set, also report the RMSE on the test set to demonstrate generalization.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Statistical rigor
- **Affected element** Figure 3d
- **Evidence point** Section "2. Markov State Model delineates distinct binding competing states of α S in presence of the small-molecule drug", Figure 3d.
- **Issue** The bootstrapping analysis for the MSM state populations is mentioned, but the details are sparse. It is not clear how many bootstrap samples were used, or whether the reported uncertainties are standard deviations or confidence intervals.
- **Required correction** Provide more details on the bootstrapping procedure, including the number of resamples and the type of uncertainty reported.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Reproducibility
- **Affected element** Computational Methods section.
- **Evidence point** Section "Computational Methods: Building a Markov State Model of monomer ensemble".
- **Issue** The number of microstates (180) is stated, but the criteria for choosing this number are vague. The text says "the VAMP-2 score saturated at higher numbers," but it is not clear what "saturated" means quantitatively.
- **Required correction** Provide a plot of VAMP-2 score versus number of microstates, and state a clear criterion for the selection (e.g., the number at which the increase in VAMP-2 score falls below a certain threshold).

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Presentation
- **Affected element** Figure 7
- **Evidence point** Section "5. Fasudil exhibits conformation-dependent interactions with individual metastable states", Figure 7.
- **Issue** The contact probability maps in Figure 7a are described, but the color scale is not defined in the text. It is unclear what values correspond to "strong" vs. "weak" interactions.
- **Required correction** Add a color bar to the figure and describe the scale in the figure legend.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Discussion of limitations.
- **Evidence point** Conclusions section.
- **Issue** The manuscript does not discuss the limitations of using a single, albeit very long, MD trajectory. Force field inaccuracies, especially for IDPs, are a known concern and are not addressed.
- **Required correction** Add a paragraph in the Conclusions or Discussion acknowledging the limitations of the MD simulations, including the use of a single trajectory and the potential for force field bias.

## Risk / unsupported claims
- The claim that fasudil induces "ensemble expansion" is not fully supported due to the unequal sampling between apo and bound states (R1-M1).
- The claim that "the entropy of the water remains unperturbed" is based on insufficient sampling (R1-M3).
- The claim that the "entropic expansion" mechanism is a general principle for IDP-small molecule interactions is not supported by the data, which only covers one protein-ligand pair (R1-M4).
- The claim that the β-VAE latent space is a reliable representation of the slow dynamical processes is not fully validated (R1-M2).
- The biological significance of the "entropic expansion" mechanism for the anti-aggregation effect of fasudil is not directly demonstrated. The authors do not connect the observed ensemble changes to the experimentally known anti-aggregation activity of fasudil.