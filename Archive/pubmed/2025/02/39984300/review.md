## Review setup
- **Input scope** Full manuscript text (abstract, introduction, results, discussion, methods, supplementary figure captions referenced but not provided)
- **Assessment boundary** Technical soundness of the proposed generative deep learning method (ICoN), validity of the conformational sampling approach, biological relevance of the generated Aβ42 conformations, and adequacy of validation against experimental data
- **Shared manuscript claim summary** The authors present ICoN, an autoencoder-based generative deep learning model trained on all-atom Molecular Dynamics (MD) simulation data using a novel vector-based internal coordinate representation (vBAT). The model learns essential dihedral motions in a 3D latent space, and nonlinear interpolation between latent points generates novel, energetically stable, biologically relevant conformations for highly dynamic proteins, demonstrated on αB-crystallin57–69 and the amyloid-β1–42 (Aβ42) monomer. The generated Aβ42 conformations include features (e.g., Arg5-Ala42 contacts, Asp23-Lys28 salt bridge) not present in the training data but supported by published experimental studies.
- **Visible evidence base** Abstract, Introduction, Results (ICoN architecture/training/validation, latent space analysis for αB-crystallin57–69, interpolation-generated conformations for both systems, biological analysis of Aβ42 conformations, comparison with Phanto-IDP), Discussion, Methods (MD simulation details, vBAT representation, model architecture, loss function, generation protocol, analysis methods), Table 1 (referenced), Figures 1–9 and S1–S18 (referenced but not provided)
- **Missing materials affecting confidence** All figures and tables (including Table 1 with quantitative reconstruction metrics and counts of novel conformations), supplementary information (detailed vBAT computation, generation flowchart, reconstruction evaluation), and the referenced comparison data for Phanto-IDP. Without these, quantitative claims about reconstruction accuracy, energy distributions, and novelty of generated conformations cannot be independently verified.

## Reviewer
- **Overall assessment** This manuscript presents a conceptually interesting approach to conformational sampling of highly dynamic proteins using a generative deep learning model with a novel internal coordinate representation. The core idea, using latent space interpolation to generate novel conformations that follow learned physical motions, is timely and potentially useful for the IDP community. However, the manuscript as provided has several significant gaps that prevent full assessment. The absence of all figures and quantitative data (Table 1) makes it impossible to evaluate the strength of the central claims. The validation strategy, while including comparison to experimental observations, appears incomplete in several respects: the energy evaluation relies on MM/GBSA rather than more rigorous approaches; the novelty of generated conformations is assessed only by RMSD-based comparison to training data; and the biological relevance claims, while supported by literature citations, would benefit from more direct experimental validation. The comparison with Phanto-IDP is described but the quantitative results are not visible. The method's scalability to larger proteins is acknowledged as a limitation but not addressed. Overall, the work has merit and the authors are clearly expert in the domain, but the current evidence base is insufficient to fully establish the case.
- **Who would be interested in the results, and why** Computational biophysicists and structural biologists studying intrinsically disordered proteins and conformational ensembles would be the primary audience. Researchers developing generative models for molecular conformations would also find the vBAT representation and latent space interpolation approach of interest. The demonstrated ability to generate biologically relevant conformations (e.g., salt bridges, hydrophobic contacts) that are absent from training data could be valuable for generating hypotheses about aggregation-prone states. The method's speed (minutes of training on a single GPU) may appeal to those needing rapid conformational sampling. The work could also interest experimentalists studying Aβ42 aggregation, as the generated conformations provide atomistic models for interpreting EPR and mutagenesis data.
- **Major strengths** 1) The vBAT representation is a thoughtful solution to the periodicity problem in dihedral angle representation, and the use of internal coordinates provides a strong inductive bias for protein conformational sampling. 2) The latent space interpolation approach is conceptually elegant, leveraging the autoencoder's learned nonlinear manifold to generate conformations that follow natural motions. 3) The demonstration that generated conformations include features (Arg5-Ala42 contacts, Asp23-Lys28 salt bridge) absent from training data but supported by literature is compelling evidence of the method's generative power. 4) The comparison with an independent MD run (Seed 2) and with Phanto-IDP shows awareness of the need for rigorous benchmarking. 5) The computational efficiency (minutes of training, GPU-accelerated coordinate conversion) is practically attractive.
- **Major Concerns**
- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The model "learns the physical principles of conformational changes from MD simulation data" and generates "energetically stable" conformations.
- **Evidence pointer** Results section "ICoN model architecture, training, and validation"; Figure 4 (energy distributions); location not provided for specific quantitative values
- **Concern** The claim that generated conformations are "energetically stable" is supported only by MM/GBSA energy calculations. MM/GBSA is an approximate method that may not accurately rank conformations for highly flexible IDPs, where entropic contributions and solvent effects are critical. The manuscript does not report whether the generated conformations were validated by more rigorous methods (e.g., explicit solvent MD relaxation, free energy perturbation, or comparison with experimental observables beyond those cited). The energy distributions shown in Figure 4 are described as "similar" to MD, but the statistical significance of this similarity is not reported.
- **Why it matters** The central value proposition of the method is generating novel, physically realistic conformations. If the energy validation is weak, the biological relevance of the generated conformations is questionable. For IDPs, where the energy landscape is flat and many conformations are accessible, approximate energy functions may not discriminate between realistic and unrealistic states.
- **Resolution test** Provide quantitative comparison of energy distributions (e.g., mean, standard deviation, statistical tests) between MD and generated conformations. Ideally, select a subset of generated conformations and subject them to short explicit-solvent MD simulations to confirm stability. If experimental data are available (e.g., chemical shifts, FRET distances, SAXS profiles), compare generated ensembles against these observables.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness
- **Claim pointer** The method "rapidly identify novel synthetic conformations with sophisticated and large-scale sidechains and backbone arrangements" and "provided a comprehensive sampling of Aβ42's conformational landscape."
- **Evidence pointer** Results section "Latent space interpolation-generated synthetic conformations of Aβ42"; Table 1 (counts of novel conformations); location not provided
- **Concern** The novelty of generated conformations is assessed by RMSD-based comparison to training data and to independent MD runs. However, RMSD is a global metric that may miss local structural differences (e.g., sidechain rotamer changes, local backbone rearrangements) that are biologically important. The manuscript does not report whether the generated conformations were assessed for physical validity (e.g., Ramachandran plots, steric clashes, bond geometry). The claim of "comprehensive sampling" is difficult to evaluate without seeing the coverage of conformational space (e.g., Rg-RMSD plots) for both MD and generated ensembles.
- **Why it matters** If the novelty metric is too coarse, the method may be generating conformations that are trivially different from training data. If the generated conformations contain unphysical geometries, their biological interpretation is compromised. The "comprehensive sampling" claim requires demonstration that the generated ensemble covers the same or broader conformational space than the MD simulations.
- **Resolution test** Report additional structural validation metrics (e.g., Ramachandran outliers, clash scores, bond length/angle deviations). Provide quantitative comparison of conformational space coverage (e.g., clustering, dimensionality reduction) between MD and generated ensembles. For a subset of novel conformations, demonstrate that they are not simply interpolations between existing training points but represent genuinely new regions of conformational space.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Scientific importance
- **Claim pointer** "New synthetic conformations showed distinct sidechain rearrangements that are probed by our electron paramagnetic resonance (EPR) and amino acid substitution studies."
- **Evidence pointer** Results section "Analysis and biological implications of novel synthetic Aβ42 conformation ensembles"; Figure 7 (EPR data); location not provided
- **Concern** The EPR and amino acid substitution studies are mentioned as validating the biological relevance of the generated conformations, but the details are not provided in the manuscript text. It is unclear whether these experiments were performed specifically to test predictions from ICoN, or whether they are pre-existing data that happen to be consistent with the generated conformations. The manuscript does not describe the EPR methodology, the specific mutations tested, or the quantitative agreement between predictions and experiments.
- **Why it matters** The biological validation is a key differentiator of this work. If the experiments were designed based on ICoN predictions, this would be strong evidence of the method's utility. If the experiments are post-hoc rationalizations, the claim is weaker. The lack of experimental detail prevents assessment of the strength of this validation.
- **Resolution test** Provide a clear description of the EPR and mutagenesis experiments, including whether they were designed based on ICoN predictions. Report quantitative agreement between predicted and experimentally observed features (e.g., distances, line shapes, aggregation rates). If possible, include a prospective validation where ICoN predictions are tested experimentally.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Technical soundness
- **Claim pointer** "The model can identify novel conformations with important interactions in atomistic details that are not included in the training data."
- **Evidence pointer** Results section "Analysis and biological implications of novel synthetic Aβ42 conformation ensembles"; Figures 6, 8, 9; location not provided
- **Concern** The claim that generated conformations contain "important interactions not included in the training data" is central to the method's value. However, the manuscript does not provide a systematic analysis of what fraction of generated conformations contain such novel interactions, nor does it quantify the diversity of generated conformations relative to the training set. The examples shown (Arg5-Ala42 contacts, Asp23-Lys28 salt bridge) are compelling but may be cherry-picked. The manuscript also does not address whether the autoencoder's latent space interpolation can generate conformations that are truly outside the manifold of training data, or whether it merely interpolates between existing conformations.
- **Why it matters** If the method only interpolates between training conformations, its utility for discovering genuinely new states is limited. The claim of novelty needs to be quantified and demonstrated systematically, not just with selected examples.
- **Resolution test** Provide a systematic analysis of the fraction of generated conformations that contain interactions (e.g., specific contacts, salt bridges) not present in the training set. Compare the distribution of generated conformations in a suitable reaction coordinate space to the training distribution. Consider testing the method on a system where the true conformational landscape is known (e.g., a small peptide with well-characterized states) to assess whether the method can discover states not sampled in training.

- **Concern ID** R1-M5
- **Severity** Major
- **Blocking** No
- **Axis** Technical soundness
- **Claim pointer** "The method is highly transferable and can be used for any available data for training."
- **Evidence pointer** Discussion section; location not provided
- **Concern** The transferability claim is made without systematic demonstration. The method is tested on two peptide systems (αB-crystallin57–69 and Aβ42), both relatively small and highly flexible. It is unclear how the method would perform on larger proteins, proteins with more structured conformational ensembles, or systems where the training data is less comprehensive. The choice of 3D latent space is also not justified; higher-dimensional latent spaces might be needed for more complex systems.
- **Why it matters** The practical utility of the method depends on its applicability to a wide range of systems. If the method only works for small, highly flexible peptides, its impact is limited.
- **Resolution test** Test the method on at least one additional system with different characteristics (e.g., a larger protein, a protein with multiple well-defined conformational states, or a system with slower dynamics). Report performance metrics (reconstruction accuracy, novelty of generated conformations, computational cost) for these additional systems.

- **Minor Comments**
- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity and reproducibility
- **Affected element** Methods section "Protein Structure Representation"
- **Evidence pointer** Methods section, subsection "Vector Representation of BAT (vBAT)"; location not provided
- **Issue** The description of the vBAT representation is dense and would benefit from a clearer step-by-step explanation. The relationship between the vector features (nˆijk, nˆjkl, v→ij, v→jk) and the resulting bond angles and torsions is not immediately obvious. The supplementary information is referenced but not provided.
- **Required correction** Expand the description of vBAT computation with a concrete numerical example for a small molecule. Clarify how the vector features are converted back to bond angles and torsions during decoding. Ensure the supplementary information provides pseudocode or a flowchart of the complete vBAT computation and reconstruction process.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Statistical rigor
- **Affected element** Results section "Validation of the models by conformation reconstruction"
- **Evidence pointer** Table 1 (referenced); location not provided
- **Issue** The reconstruction accuracy is reported as average RMSD values, but the distribution of RMSD across the validation set is not described. It is unclear whether the average is representative or driven by a few outliers. The number of validation conformations used is not stated.
- **Required correction** Report the distribution of reconstruction RMSD (e.g., histogram, percentiles) and the number of validation conformations. If outliers exist, discuss their characteristics and potential causes.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Completeness of comparison
- **Affected element** Results section "Comparing ICoN with Phanto-IDP"
- **Evidence pointer** Figure S15 and S16 (referenced); location not provided
- **Issue** The comparison with Phanto-IDP is described qualitatively. The manuscript states that ICoN samples a broader range of conformations, but quantitative metrics (e.g., number of novel conformations, coverage of conformational space, computational cost) are not reported in the text.
- **Required correction** Provide a quantitative comparison table or figure showing the number of novel conformations, the range of Rg and RMSD covered, and the computational time for both methods. Discuss the trade-offs between the two approaches.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Terminology precision
- **Affected element** Throughout
- **Evidence pointer** Abstract, Introduction, Discussion; location not provided
- **Issue** The term "physical principles" is used repeatedly to describe what the model learns. This is potentially misleading, as the model learns from MD simulation data, which itself is an approximation of physical reality. The model does not directly learn physics but rather learns patterns in MD-generated conformations.
- **Required correction** Rephrase to "learns conformational patterns from MD simulation data" or "learns the effective dynamics encoded in MD trajectories" to be more precise about what the model actually learns.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Experimental validation detail
- **Affected element** Results section "Analysis and biological implications of novel synthetic Aβ42 conformation ensembles"
- **Evidence pointer** Figure 7 (EPR data); location not provided
- **Issue** The EPR experiments are mentioned but not described. The reader cannot assess the quality of the data or the interpretation without seeing the spectra and the experimental conditions.
- **Required correction** Provide a brief description of the EPR methodology (e.g., spin label position, measurement conditions, spectral analysis) in the main text or refer to a detailed methods section in the supplementary information.

## Risk / unsupported claims
- The claim that ICoN "learns the physical principles of conformational changes" is not fully supported; the model learns patterns from MD data, which is an approximation of physical reality.
- The claim of "comprehensive sampling of Aβ42's conformational landscape" cannot be evaluated without seeing the conformational space coverage plots (Figure 5) and quantitative comparison to MD ensembles.
- The claim that generated conformations are "energetically stable" relies solely on MM/GBSA calculations, which may not be reliable for IDPs.
- The biological relevance claims based on EPR and amino acid substitution studies cannot be assessed without experimental details.
- The comparison with Phanto-IDP is described qualitatively; quantitative metrics are not provided in the text.
- The transferability claim is based on only two peptide systems and is not systematically demonstrated.
- The novelty of generated conformations is assessed only by RMSD-based comparison, which may miss locally important structural differences.
- The manuscript does not report whether generated conformations were checked for physical validity (e.g., Ramachandran outliers, steric clashes).