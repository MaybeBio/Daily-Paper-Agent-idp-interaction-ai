## Review setup
- **Input scope** Full manuscript text (abstract, introduction, results, discussion, methods, data availability)
- **Assessment boundary** Scientific claims, methodological soundness, and interpretational validity as presented in the provided text
- **Shared manuscript claim summary** The authors use a β-variational autoencoder (β-VAE) and Markov state models (MSMs) to analyze long-timescale molecular dynamics simulations of α-synuclein (αS) in water and in aqueous fasudil solution. They report that fasudil binding expands the conformational ensemble of αS from three metastable states (in water) to six (in fasudil), with state-specific interaction patterns and a decrease in backbone entropy at binding hotspots, consistent with an "entropic expansion" mechanism.
- **Visible evidence base** Text descriptions of results, figures referenced (Figures 1–9 and supplements), methods descriptions, data availability statement
- **Missing materials affecting confidence** Actual figure images, numerical values for key quantities (e.g., populations, entropies, contact probabilities), simulation convergence metrics, force field validation details, and the full 1500 µs trajectory analysis details are not available in the provided text

## Reviewer

### Overall assessment
This manuscript presents a potentially interesting application of machine learning-based dimensionality reduction combined with Markov state modeling to dissect the conformational ensemble of an intrinsically disordered protein in the presence of a small molecule. The central claim—that fasudil induces an entropic expansion of the αS ensemble—is mechanistically plausible and relevant to the growing field of IDP-targeting drug design. However, the manuscript as presented has several significant weaknesses. The comparison between the apo and fasudil-bound ensembles is confounded by vastly different simulation lengths (62 µs vs 1500 µs), which could trivially explain the observation of more states in the fasudil system. The entropy analysis is described at a level that prevents assessment of its statistical robustness. The claim of "entropic expansion" is inferred from state counting and per-residue entropy differences, but the manuscript does not provide a direct, quantitative comparison of total conformational entropy between the two ensembles. The machine learning methodology is described in reasonable detail, but the validation of the latent space and the MSM is incomplete. The writing is generally clear but contains some typographical errors and occasional lapses in precision.

### Who would be interested in the results, and why
Researchers working on intrinsically disordered proteins, particularly those interested in small-molecule binding to IDPs and the development of computational methods for analyzing disordered protein ensembles. The work may also appeal to method developers in the machine learning for molecular simulation community, as it demonstrates an application of β-VAE for dimensionality reduction of IDP conformational data. The potential therapeutic relevance of fasudil in Parkinson's disease adds translational interest.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Experimental design / confound
- **Claim pointer** The authors claim that the presence of fasudil increases the number of metastable states from three (in water) to six (in fasudil), and interpret this as evidence of ensemble expansion.
- **Evidence pointer** Results section "MSM elucidates distinct binding competing states of αS in presence of the small-molecule drug"; Figure 3
- **Concern** The apo ensemble was generated from 23 independent simulations totaling ~62 µs, while the fasudil-bound ensemble derives from a single 1500 µs trajectory. The observation of more states in the fasudil system may simply reflect the much greater sampling depth of that trajectory. The authors address this partially by building an MSM on a 60 µs segment of the fasudil trajectory (Figure 3—figure supplement 4), but this is insufficient. A 60 µs segment of a single trajectory is not equivalent to 62 µs of sampling from 23 independent starting points. The authors need to demonstrate that the six-state model is robust when the fasudil trajectory is subsampled to match the apo simulation length and starting-condition diversity.
- **Why it matters** The central claim of the paper—that fasudil expands the αS ensemble—depends entirely on the comparison of state counts between the two systems. If the difference is a sampling artifact, the conclusion is unsupported.
- **Resolution test** Provide an MSM built on a matched-length, matched-diversity subsample of the fasudil trajectory (e.g., 23 independent segments of ~2.7 µs each, or a comparable design). If six states are still recovered under these conditions, the claim is strengthened. Alternatively, provide a statistical test showing that the number of states is not sensitive to trajectory length.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Quantitative support for central claim
- **Claim pointer** The authors claim that fasudil binding leads to "entropic expansion" and that the effect is "mainly manifested at the backbone level with a decrease in entropy at the fasudil binding hotspots."
- **Evidence pointer** Results section "Entropic signatures of small molecule binding"; Figure 8
- **Concern** The manuscript does not provide a quantitative comparison of total conformational entropy between the apo and fasudil-bound ensembles. The entropy values are reported per state (Figure 8), but no aggregate measure is given. The claim of "entropic expansion" requires a demonstration that the total entropy of the fasudil-bound ensemble exceeds that of the apo ensemble, not merely that more states are identified. Furthermore, the per-residue entropy differences are described qualitatively; no statistical significance testing is reported. The correlation between binding hotspots and entropy decrease is asserted but not quantified.
- **Why it matters** The title and abstract emphasize "entropic expansion" as the key mechanism. Without a direct, quantitative entropy comparison, the central mechanistic claim is not established.
- **Resolution test** Compute and report the total conformational entropy (e.g., via the MIST approach or a comparable method) for both ensembles, with uncertainty estimates. Provide a statistical comparison (e.g., bootstrap or permutation test) of per-residue entropy differences between apo and fasudil-bound states, and quantify the correlation between binding probability and entropy change.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Methodological validation
- **Claim pointer** The authors claim that the β-VAE latent space provides a suitable representation for building MSMs, and that it outperforms linear methods (tICA) based on VAMP2 scores.
- **Evidence pointer** Results section "Modulation of free energy landscape of αS in presence of fasudil"; Figure 3—figure supplements 1–2
- **Concern** The VAMP2 score comparison between β-VAE and tICA is mentioned but not shown in the provided text. The choice of β = 1×10⁻¹² is justified by minimum reconstruction error, but this does not necessarily imply that the latent space is optimal for capturing slow dynamical processes. The manuscript does not report the reconstruction error values or the VAMP2 scores. Additionally, the sensitivity of the MSM results to the choice of latent space dimensionality (2D) and the number of k-means clusters (180) is not explored.
- **Why it matters** The methodological framework is a key contribution of the paper. If the latent space or MSM parameters are not adequately validated, the reliability of the identified states is questionable.
- **Resolution test** Report the VAMP2 scores for both β-VAE and tICA. Perform a sensitivity analysis varying latent dimensionality (e.g., 2, 3, 4) and number of clusters, and show that the number of metastable states and their properties are robust.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Interpretation of water entropy
- **Claim pointer** The authors state that "the presence of fasudil has an insignificant impact on the entropy of water."
- **Evidence pointer** Results section "Entropic signatures of small molecule binding"; Figure 8—figure supplement 1
- **Concern** The water entropy analysis is based on 20 ps simulations per state. This is an extremely short timescale for converged entropy estimates of water, especially in the vicinity of a protein surface. The manuscript does not report convergence tests or error bars for the water entropy values. The claim of "insignificant impact" is made without statistical support.
- **Why it matters** The authors use the water entropy result to argue that the entropic effect is dominated by protein conformational entropy. If the water entropy calculation is unreliable, this part of the argument is weakened.
- **Resolution test** Extend the water entropy simulations to longer timescales (e.g., 100–200 ps) and report convergence of the entropy values. Provide error estimates and a statistical comparison between bulk water and water in the presence of αS with and without fasudil.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Abstract
- **Evidence pointer** Abstract
- **Issue** The phrase "entropic expansion mechanism" is used without a clear definition. The abstract would benefit from a one-sentence explanation of what this mechanism entails.
- **Required correction** Add a brief definition, e.g., "an increase in the number and diversity of accessible conformational states."

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Technical detail
- **Affected element** Methods, "Monomer simulation protocol"
- **Evidence pointer** Methods section
- **Issue** The text states "23 different conformations from previously reported (Robustelli et al., 2018) multi-µs αS trajectory in water" but does not specify how these conformations were selected (e.g., random, evenly spaced, clustering-based).
- **Required correction** Specify the selection criteria for the 23 starting conformations.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Statistical reporting
- **Affected element** Results, "Entropic signatures of small molecule binding"
- **Evidence pointer** Figure 8
- **Issue** The entropy values are reported without error bars or uncertainty estimates.
- **Required correction** Report standard deviations or confidence intervals for all entropy values, and specify the number of independent samples used.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Typographical
- **Affected element** Results, "MSM elucidates distinct binding competing states of αS in presence of the small-molecule drug"
- **Evidence pointer** Results section
- **Issue** The word "Addidtionally" is misspelled.
- **Required correction** Correct to "Additionally".

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Results, "Exploring interplay of conformational entropy and mean first passage time in protein conformational transitions"
- **Evidence pointer** Figure 9
- **Issue** The correlation between entropy and MFPT is described qualitatively ("strong degree of correlation") but no correlation coefficient or statistical test is reported.
- **Required correction** Report the correlation coefficient (e.g., Pearson or Spearman) and its significance.

- **Concern ID** R1-m6
- **Severity** Minor
- **Axis** Reproducibility
- **Affected element** Methods, "Building the denoising convolutional variational autoEncoder"
- **Evidence pointer** Methods section
- **Issue** The description of the DCVAE architecture is incomplete. The number of strides listed (1, 2, 2, 2, 2, 1) does not match the number of convolutional layers (five).
- **Required correction** Clarify the architecture, including the number of strides per layer and any pooling or upsampling operations.

## Risk / unsupported claims
- The claim that fasudil induces "entropic expansion" of the αS ensemble is not quantitatively supported, as no total conformational entropy comparison is provided.
- The claim that the increase in metastable states (from 3 to 6) is due to fasudil binding rather than sampling differences is not adequately established.
- The claim that water entropy is "insignificantly" affected by fasudil is based on very short simulations without reported convergence or error analysis.
- The claim that the β-VAE latent space is superior to tICA for this system is not verifiable from the provided text, as the VAMP2 scores are not reported.
- The assertion that "the state with the highest population also has the highest protein entropy" is presented without a formal statistical test.
- The claim that fasudil "may potentially trap the protein conformations in the intermediate states" is speculative and not directly supported by the presented data.