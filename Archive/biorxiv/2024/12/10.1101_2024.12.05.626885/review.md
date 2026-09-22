## Review setup
- **Input scope** Full manuscript text including abstract, main text, supplementary methods, and figure captions as provided
- **Assessment boundary** Scientific claims, methodological soundness, validation approach, and reproducibility as presented in the provided manuscript text
- **Shared manuscript claim summary** The authors present BioEmu, a generative deep learning system based on a denoising diffusion model, designed to emulate equilibrium ensembles of protein conformations. The system is trained on a combination of static protein structures from the AlphaFold database, over 200 milliseconds of all-atom molecular dynamics simulations, and experimental protein stability measurements. The authors claim that BioEmu can generate thousands of statistically independent protein conformations per hour on a single GPU, sample functionally relevant conformational changes including domain motions, local unfolding, and cryptic pocket formation, and predict protein stabilities with errors around 1 kcal/mol.
- **Visible evidence base** Main text figures referenced as Fig. 1, Fig. 2, Fig. 3, Fig. 4; supplementary figures S1-S8; supplementary tables S1-S4; algorithmic descriptions in Section S.2 and S.3
- **Missing materials affecting confidence** Actual figure images and supplementary data files were not provided for direct inspection. Quantitative results tables with exact numerical values for all benchmarks are not fully visible in the text. Details on the MEGAscale dataset filtering and the exact composition of training versus test splits require the supplementary data files. The precise architecture hyperparameters and training compute requirements are only partially specified.

## Reviewer
- **Overall assessment** This manuscript presents a significant advance in the application of generative deep learning to protein conformational sampling. The core idea of training a diffusion model on a diverse mixture of structural and thermodynamic data to produce an emulator of equilibrium ensembles is timely and potentially impactful. The authors demonstrate qualitative success in sampling known conformational states and quantitative agreement with MD-derived free energy surfaces and experimental stability measurements. However, the manuscript would benefit from clearer articulation of the limitations of the emulator approach, particularly regarding the physical interpretability of the generated ensembles and the generalizability beyond the training distribution. The validation strategy is thoughtful, but the reliance on MD data as ground truth for equilibrium comparisons introduces circularity concerns that are only partially addressed. The PPFT method for incorporating experimental thermodynamic data is a novel contribution, though its convergence properties and potential for bias warrant further discussion. Overall, this is a strong contribution that merits consideration, but several technical concerns need to be addressed to fully establish the claims.
- **Who would be interested in the results, and why** Computational biophysicists and structural biologists interested in protein conformational ensembles and their role in function would find this work directly relevant. Researchers developing generative models for biomolecular systems will be interested in the training methodology and the PPFT algorithm. Drug discovery scientists exploring cryptic pockets and conformational selection mechanisms may find the qualitative sampling capabilities useful for hypothesis generation. The broader machine learning for science community will be interested in the demonstration of training generative models on heterogeneous data sources including experimental thermodynamic measurements.
- **Major strengths** The manuscript addresses a fundamental challenge in protein science with a novel methodological approach. The integration of multiple data modalities, including static structures, MD simulations, and experimental stability measurements, into a single training framework is innovative. The validation across multiple benchmark types, including conformational changes, MD emulation, and stability prediction, provides a comprehensive assessment. The computational efficiency claims, with generation of thousands of samples per hour on a single GPU, represent a substantial practical advantage over MD simulation. The qualitative examples of functional conformational changes, such as cryptic pocket formation and domain motions, are compelling demonstrations of the method's capabilities.
- **Major Concerns**
- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors claim that BioEmu emulates equilibrium distributions of protein conformations, validated against MD simulations and experimental stability measurements.
- **Evidence pointer** Section 4, Fig. 3, Section 5, Fig. 4
- **Concern** The validation of equilibrium emulation relies heavily on comparison to MD simulations that were used in the training data. The DESRS fast-folding proteins are used for leave-one-out cross-validation, which is appropriate, but the main model is trained on a mixture that includes MD data from similar systems. The circularity concern is partially acknowledged but not fully addressed. Specifically, the claim that BioEmu approximates the equilibrium distribution requires demonstration that the model does not simply memorize training conformations but generalizes to new sequences and conditions. The mMAE metric, while reasonable, is computed on a subset of test systems with sufficient MD data, which may bias toward well-sampled systems. The authors should provide a more explicit analysis of the overlap between training and test distributions and demonstrate that the model's performance does not degrade for systems far from the training distribution.
- **Why it matters** The central claim of the manuscript is that BioEmu can emulate equilibrium ensembles. If the validation is confounded by training data overlap, the claim of equilibrium emulation is not established. This is critical for the scientific contribution and for potential users who may rely on the method for systems outside the training distribution.
- **Resolution test** Provide a clear analysis of the sequence and structural similarity between training and test sets. Demonstrate performance on a set of proteins that are maximally distant from the training distribution. Show that the model's equilibrium predictions are robust to the choice of MD force field used for training data generation. If possible, compare model predictions to experimental observables beyond stability, such as NMR order parameters or SAXS profiles, for a set of proteins not in the training set.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The authors claim that PPFT efficiently incorporates experimental thermodynamic measurements into diffusion model training, enabling stability prediction with errors below 1 kcal/mol.
- **Evidence pointer** Section 2, Section 5, Fig. 4, Section S.3.6
- **Concern** The PPFT method is a key novel contribution, but the description of its convergence properties and potential biases is insufficient. The method relies on backpropagating through a stochastic sampling process, which can be numerically unstable and may introduce gradient bias. The authors mention using 8 denoising steps for fast approximate sampling, but the accuracy of the foldedness prediction at this reduced step count is not systematically evaluated. The choice of the cross-term loss function to avoid variance inflation is motivated, but the behavior of the optimization landscape and the risk of mode collapse are not thoroughly analyzed. The authors state that the method works well empirically, but a more rigorous analysis of when PPFT is expected to work and when it may fail would strengthen the contribution.
- **Why it matters** The PPFT method is presented as a general approach for incorporating experimental data into generative model training. If the method has hidden failure modes or requires careful hyperparameter tuning, its utility for the broader community is limited. The stability prediction results are a key quantitative claim, and the reliability of the method directly impacts the validity of these results.
- **Resolution test** Provide a systematic ablation study of PPFT components, including the number of denoising steps, the weight of the loss term, and the choice of foldedness definition. Analyze the convergence of the training process and the variance of the gradient estimates. Demonstrate the method on a synthetic example where the true equilibrium distribution is known, to verify that PPFT correctly recovers the target distribution. Compare PPFT to alternative approaches for incorporating thermodynamic data, such as reweighting or importance sampling.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Reproducibility
- **Claim pointer** The authors claim that BioEmu can generate thousands of statistically independent samples per hour on a single GPU.
- **Evidence pointer** Abstract, Section 2, Section S.2.3
- **Concern** The computational efficiency claim is central to the practical utility of the method, but the manuscript does not provide detailed benchmarking information. The specific GPU model is mentioned as NVIDIA Titan V for some results, but the inference time for generating 10,000 samples is not reported for all model sizes and sequence lengths. The scaling behavior with protein size is not characterized. The memory requirements for inference are not discussed. The claim of statistical independence of samples is not rigorously tested, as autocorrelation analysis of generated samples is not presented.
- **Why it matters** The practical value of BioEmu depends on its computational efficiency and the quality of its samples. If the samples are correlated or the inference time scales poorly with protein size, the claimed advantages over MD simulation may not hold for realistic applications.
- **Resolution test** Provide detailed benchmarking of inference time and memory usage for proteins of varying sizes, including the specific GPU model used. Present autocorrelation analysis of generated samples to support the claim of statistical independence. Compare the computational cost of generating a converged ensemble with BioEmu versus the cost of the MD simulations used for training data generation.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Scientific importance
- **Claim pointer** The authors claim that BioEmu reveals mechanistic insights, such as the causes for fold destabilization of mutants.
- **Evidence pointer** Section 5, Fig. 4d
- **Concern** The mechanistic insights presented are largely qualitative and based on visual inspection of generated structures. The analysis of mutant destabilization is limited to a few examples, and the statistical significance of the observed structural differences is not established. The connection between the generated ensembles and the underlying physical causes of destabilization is not rigorously demonstrated. The authors do not compare their mechanistic interpretations with those derived from experimental structural studies or detailed MD analysis.
- **Why it matters** The claim of providing mechanistic insights is a significant part of the manuscript's impact. If the insights are not robust or are based on superficial analysis, the scientific contribution is diminished.
- **Resolution test** Provide a more quantitative analysis of the structural differences between wild-type and mutant ensembles, including statistical tests. Compare the mechanistic interpretations with those from published experimental or computational studies. Demonstrate that the generated ensembles can be used to make testable predictions that are validated by independent experiments.

- **Minor Comments**
- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Abstract
- **Evidence pointer** Abstract
- **Issue** The abstract states that BioEmu generates samples from the protein equilibrium ensemble, but the limitations of the emulator approach, particularly the coarse-grained representation and the fixed temperature of 300K, are not mentioned.
- **Required correction** Add a brief statement in the abstract acknowledging the coarse-grained nature of the model and the fixed simulation conditions.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Reproducibility
- **Affected element** Section 2
- **Evidence pointer** Section 2, Section S.2
- **Issue** The description of the model architecture refers to Algorithm 1, but the algorithm pseudocode is not included in the provided text.
- **Required correction** Ensure that Algorithm 1 is included in the final manuscript or supplementary materials.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Section 3
- **Evidence pointer** Section 3, Fig. 2
- **Issue** The definition of success for the cryptic pocket benchmark uses a strict 1.5 Å RMSD threshold, but the rationale for this specific threshold is not provided.
- **Required correction** Provide a brief justification for the chosen RMSD threshold, or cite relevant literature supporting this choice.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Technical soundness
- **Affected element** Section 4
- **Evidence pointer** Section 4, Fig. 3
- **Issue** The comparison of computational costs between MD and BioEmu does not account for the cost of generating the training data, which is a significant upfront investment.
- **Required correction** Acknowledge the upfront cost of MD data generation in the comparison and discuss the amortization of this cost over many inference runs.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Section 5
- **Evidence pointer** Section 5, Fig. 4
- **Issue** The description of the stability prediction results does not clearly specify the exact metric used for the reported error of 0.8 kcal/mol.
- **Required correction** Clearly state whether the reported error is mean absolute error, root mean square error, or another metric, and specify the units.

- **Concern ID** R1-m6
- **Severity** Minor
- **Axis** Reproducibility
- **Affected element** Section S.3.6
- **Evidence pointer** Section S.3.6
- **Issue** The description of the PPFT algorithm mentions that the foldedness prediction is performed after 8 out of 35 denoising steps, but the sensitivity of the results to this specific choice is not discussed.
- **Required correction** Provide a brief analysis of the sensitivity of the PPFT results to the number of denoising steps used for foldedness prediction.

- **Concern ID** R1-m7
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Section 6
- **Evidence pointer** Section 6
- **Issue** The conclusion states that BioEmu can be used for "dynamical protein design," but the manuscript does not demonstrate this capability.
- **Required correction** Either provide a demonstration of the use of BioEmu for protein design or temper the claim to reflect the current capabilities of the method.

- **Concern ID** R1-m8
- **Severity** Minor
- **Axis** Technical soundness
- **Affected element** Section S.1.5.4
- **Evidence pointer** Section S.1.5.4
- **Issue** The description of the MEGAscale data processing mentions that the foldedness threshold is set based on the minimum of the kernel density estimate, but the robustness of this choice is not evaluated.
- **Required correction** Provide a brief analysis of the sensitivity of the results to the choice of foldedness threshold.

## Risk / unsupported claims
- The claim that BioEmu emulates equilibrium distributions is not fully established due to potential circularity in validation against training data.
- The claim of providing mechanistic insights into mutant destabilization is based on limited qualitative analysis.
- The claim of generating statistically independent samples is not supported by autocorrelation analysis.
- The claim of computational efficiency is not fully supported by detailed benchmarking data.
- The claim that BioEmu can be used for "dynamical protein design" is not demonstrated in the manuscript.
- The generalizability of the model to proteins with post-translational modifications, non-standard residues, or cofactors is not addressed.
- The performance of the model for proteins larger than those in the test set is not characterized.
- The sensitivity of the PPFT method to the choice of foldedness definition and threshold is not fully evaluated.