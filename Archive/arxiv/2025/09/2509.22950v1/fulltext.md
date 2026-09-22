## Twin Peaks: Dual-Head Architecture for Structure-Free Prediction of Protein-Protein Binding Affinity and Mutation Effects

We present a novel dual-head deep learning architecture for protein-protein interaction modeling that enables simultaneous prediction of binding affinity ( Δ ​ G \Delta G ) and mutation-induced affinity changes ( Δ ​ Δ ​ G \Delta\Delta G ) using only protein sequence information. Our approach offers a significant advancement over existing methods by employing specialized prediction heads that operate on a shared representation network, allowing direct and optimized prediction of both values. To ensure robust generalization, we integrated complementary datasets from SKEMPI v2 and PDBbind with a rigorous protein domain-based splitting strategy that prevents information leakage between training and validation sets. This approach yielded 6732 training samples across 2322 unique protein complex and 856 validation samples from 140 unique complexes, which are also from non-overlapping protein families. Our architecture combines transformer-based encoders with a novel cross-attention mechanism that processes paired protein sequences directly, without requiring any structural information. Unlike conventional transformer architectures that process single amino acid changes as noise by reasoning over the whole structure, our model is specifically designed to detect and amplify signals from the critical hotspot residues that contribute to infectivity and binding affinity changes. The network embeds input sequences using ESM3 representations, then employs a learnable sliced window embedding layer to manage variable-length sequences efficiently. A multi-layer transformer encoder with bidirectional self-attention captures intra-protein patterns, while cross-attention layers enable explicit modeling of interactions between protein pairs. This shared representation network feeds into separate Δ ​ G \Delta G and Δ ​ Δ ​ G \Delta\Delta G prediction heads, allowing task-specific optimization while leveraging common features. The model achieves Δ ​ Δ ​ G \Delta\Delta G validation of Pearson correlation at 0.485, while maintaining strong Δ ​ G \Delta G predictions (Pearson: 0.638). While existing approaches require protein structure data and binding interface information, our model eliminates these constraints. This provides a critical advantage for the numerous proteins with unknown structures or those challenging to crystallize, such as viral and intrinsically disordered proteins. Additionally, no structure prediction tool is trained on viral sequences because of regulatory reasons - which makes them unsuitable for immunoinformatic pipelines for vaccine design. The uncertainties from structural prediction and docking propagate to give unreliable function prediction and overshadow large functional outcomes in viral sequences that arise from changes as small as a single amino acid.


## 1 Introduction

Protein-protein interactions (PPIs) form the basis of numerous biological processes and are essential to cellular function. The ability to accurately predict both the binding affinity ( Δ ​ G \Delta G ) between two proteins and how mutations affect this binding ( Δ ​ Δ ​ G \Delta\Delta G ) has profound implications for drug discovery, protein engineering, and understanding disease mechanisms Kastritis2013 . However, this prediction task presents significant challenges, particularly when structural data is unavailable or unreliable Rodrigues2019 .

Existing computational approaches for predicting protein-protein binding affinity and mutation effects predominantly rely on three-dimensional structural information. These structure-dependent methods typically require high-resolution crystal structures of the protein complex, molecular dynamics simulations to model the binding interface, and energy-based calculations to estimate binding free energy. While effective for well-characterized systems, these approaches encounter severe limitations when applied to the vast majority of proteins in nature Antunes2018 .

A significant challenge arises when dealing with proteins lacking solved structures, which represent most of the proteome. Similarly, intrinsically disordered proteins, which lack stable tertiary structures, are poorly suited to structure-based methods despite their critical roles in cellular signaling and regulation Riley2023 . Viral proteins present another major challenge, as they evolve rapidly and are often difficult to crystallize, yet understanding their mutation effects is crucial for public health. Additionally, viral sequences are rarely used to train structure prediction pipelines for regulatory purposes and return unreliable structures predictions Bryant2022 . This makes the structure based pipelines unsuitable for vaccine design immunoinformatics pipelines.

In this work, we introduce Twin Peaks, a novel dual-head architecture that simultaneously predicts protein-protein binding affinity ( Δ ​ G \Delta G ) and mutation-induced changes ( Δ ​ Δ ​ G \Delta\Delta G ) using sequence information alone. Our approach achieves strong performance without requiring structural data through four key innovations: a mutation-aware embedding strategy with a dedicated indicator channel, an enhanced Sliced-Wasserstein Embedding pooling mechanism that preserves mutation signals, a specialized cross-attention mechanism for modeling inter-chain interactions, and a dual-head prediction network that jointly optimizes both tasks. Our contributions include: (1) the first sequence-only architecture to simultaneously predict Δ ​ G \Delta G and Δ ​ Δ ​ G \Delta\Delta G with high accuracy, (2) mutation-specific attention mechanisms that explicitly model mutation impacts, (3) strong performance on proteins with limited structural information, and (4) a tool applicable to previously challenging targets including viral and intrinsically disordered proteins.


## 2 Related Work


## 2.1 Structure-Based Approaches

Structure-dependent methods like Prodigy, binding-ddg-predictor, and FoldX rely on 3D protein structures to estimate energy changes upon binding or mutation. While these methods can achieve moderate accuracy in well-characterized systems, they face several critical limitations Xue2016 ; Schymkowitz2005 . Their performance significantly degrades with missing residues, low-resolution models, or intrinsically disordered regions, creating a fundamental barrier for many proteins of interest, especially viral proteins that evolve rapidly. Tools like binding-ddg-predictor Luo2024 require not only the 3D structures but also explicit identification of binding interfaces and active site residues. This pre-processing step can be as time-consuming as the prediction itself, requiring expert knowledge and often manual curation. Similarly, this adds constrain to docking-based tools like HADDOCK Giulini2025 .

Furthermore, high-performing structure-based calculations typically involve molecular dynamics simulations or extensive energy minimization processes that can take hours per protein complex, making them impractical for high-throughput screening of mutation effects. Many structure-based methods also show highly variable performance across different protein families, particularly when applied to proteins outside their training distribution, such as viral proteins or intrinsically disordered regions.

Recent machine learning approaches like MutaBind2, DDMUT-ppi, and mmcsm-ppi have improved accuracy by combining structural features with learned representations Zhang2020 ; Zhou2024 . However, these methods still fundamentally depend on structure availability and quality. The rise of protein structure prediction tools like AlphaFold and esmFold has partially addressed this limitation by providing predicted structures, but introduces additional uncertainty through compounding errors Jumper2021 ; Lin2023 .


## 2.2 Sequence-Based Methods

Sequence-based approaches offer an alternative that doesn’t require structural information. Traditional methods relied on evolutionary information through multiple sequence alignments (MSAs), which can effectively capture co-evolutionary patterns indicating interacting residues. However, these approaches struggle with recently evolved or fast-evolving proteins that lack sufficient evolutionary data, such as viral antigens.

Recent advancements in protein language models (PLMs) have revolutionized sequence-based approaches. Models like ESM learn contextual representations of amino acids from millions of protein sequences, capturing both evolutionary and functional information Lin2023 . Sequence-only tools such as DDGemb and DeepPPAPred leverage these powerful representations Savojardo2024 . However, these newer tools face struggles to capture complex interactions, and often need additional details (i.e., Uniprot ID for DeepPPAPred Nikam2024 ). Additionally, their performance is poor outside the highly utilized SKEMPIv2 Jankauskaite2019 training set.

A significant limitation of current approaches is their focus on either Δ ​ G \Delta G or Δ ​ Δ ​ G \Delta\Delta G prediction, but not both simultaneously. This creates a methodological inconsistency when researchers must use different tools for related analyses, potentially introducing bias and error propagation. Despite these advances, most sequence-based methods struggle with predicting the effects of mutations on binding affinity. They often treat mutations as noise when reasoning over the entire sequence instead of focusing on the critical hotspot residues that contribute disproportionately to binding and function. Additionally, our previous work, Seq2Bind, predicts binding affinity based on the sequences too. This work is a continuation from Seq2Bind ma2025seq2bindwebserverdecodingbinding .


## 2.3 The Need for an Integrated Approach

Our work addresses these challenges by developing a unified sequence-only architecture that explicitly models mutation effects while simultaneously predicting both binding affinity and mutation-induced changes. Existing approaches require using separate tools for the predictions of Δ ​ G \Delta G and Δ ​ Δ ​ G \Delta\Delta G , introducing inconsistent biases and compounding errors. Many Δ ​ Δ ​ G \Delta\Delta G predictors need both mutant and wild-type structures and cannot handle insertions or deletions, further limiting their applicability. Additionally, this creates challenges for predicting complexes with no prior binding affinity data. Our dual-head architecture ensures internal consistency by deriving both predictions from a shared representation. By eliminating structural prerequisites and reducing computation time from hours to minutes, our approach enables screening at scales previously unattainable with structure-based methods, while maintaining competitive accuracy through mutation-aware representation learning.


## 3 Methods


## 3.1 Problem Formulation

We formulate the problem as follows: Given a pair of protein sequences ( S 1 , S 2 ) (S_{1},S_{2}) and a set of mutation positions and types, we aim to predict the binding affinity Δ ​ G \Delta G between the mutant proteins and predict the change in binding affinity Δ ​ Δ ​ G \Delta\Delta G caused by the mutations relative to the wild-type.

Formally, we define the two prediction tasks as:

where S 1 m ​ u ​ t S_{1}^{mut} and S 2 m ​ u ​ t S_{2}^{mut} represent the mutant sequences, S 1 w ​ t S_{1}^{wt} and S 2 w ​ t S_{2}^{wt} represent the wild-type sequences, and f θ f_{\theta} is the prediction function parameterized by θ \theta .

Our innovation is to directly predict both values simultaneously using a dual-head architecture:

where g ϕ g_{\phi} is our proposed model with parameters ϕ \phi .


## 3.2 Model Architecture

Our Twin Peaks architecture (Figure 1 ) addresses the fundamental challenge of detecting mutation effects without structural information through a design that prioritizes mutation sensitivity. Rather than treating mutations as ordinary sequence variations, we explicitly track mutation positions and their effects throughout the network. This mutation-aware processing flows from protein language model embeddings through specialized pooling and cross-attention mechanisms, culminating in a dual-head prediction framework. The architecture’s key innovation lies in its ability to amplify mutation signals while modeling protein-protein interactions from sequence alone.

We leverage the ESM3 protein language model to generate contextualized embeddings for each amino acid in the input sequences. ESM3 is a transformer-based model pre-trained on millions of protein sequences, capturing evolutionary and structural information that would be difficult to learn from scratch Hayes2025 .

For each protein sequence S S of length L L , we obtain embeddings E ∈ ℝ L × d E\in\mathbb{R}^{L\times d} , where d = 1152 d=1152 is the embedding dimension. To explicitly encode mutation information, we augment these embeddings with a mutation indicator channel:

where M ∈ ℝ L × 1 M\in\mathbb{R}^{L\times 1} is a binary channel with M i = 1 M_{i}=1 if position i i is mutated and 0 otherwise.

To handle variable-length sequences efficiently while preserving mutation information, we adapt the Sliced Wasserstein Embedding (SWE) pooling method NaderiAlizadeh2024 for mutation sensitivity in protein sequences. The original SWE method conceptualizes token-level embeddings as samples from a probability distribution, projecting them onto random directions (slices), sorting these projections, and measuring distances to reference points:

where θ \theta contains learnable projection directions, R R represents learnable reference points, and W W is a weight matrix, and interp1d is a differentiable 1D interpolation function that maps the sorted slice projections to a fixed set of reference points, enabling gradient-based learning through the sorting operation.

Our key innovation is a mutation-aware weighting mechanism that amplifies signals from mutation positions:

where f m ​ u ​ t f_{mut} and f p ​ o ​ s f_{pos} generate importance weights based on mutation status and position information. Through hyperparameter optimization, we determined the number of slices and reference points for optimal performance in our mutation-sensitive embeddings. This adaptation produces fixed-length representations that preserve mutation information while handling the variable-length nature of protein sequences, making it particularly effective for detecting the subtle effects of point mutations on protein function.

Beyond preserving mutation information, our enhanced SWE pooling captures global sequence patterns critical for binding affinity prediction, establishing a foundation for both accurate Δ ​ G \Delta G prediction and sensitive detection of mutation-induced changes.

To model the interactions between protein pairs explicitly, we introduce a novel mutation-specific cross-attention mechanism. Given embeddings for two protein chains C 1 ∈ ℝ L 1 × D C_{1}\in\mathbb{R}^{L_{1}\times D} and C 2 ∈ ℝ L 2 × D C_{2}\in\mathbb{R}^{L_{2}\times D} , we first split the ESM embeddings from the mutation channel:

We compute a position-aware mutation encoding:

The standard attention scores are computed as:

Our key innovation is the addition of a mutation-position attention bias:

While designed for mutation sensitivity, our cross-attention mechanism simultaneously models fundamental protein-protein interactions by capturing residue-pair relationships, benefiting both Δ ​ G \Delta G and Δ ​ Δ ​ G \Delta\Delta G predictions. The mutation-specific attention bias focuses on functionally critical regions that influence both absolute binding affinity and mutation-induced changes.

The core innovation of our approach is the dual-head architecture that simultaneously predicts both Δ ​ G \Delta G and Δ ​ Δ ​ G \Delta\Delta G . Rather than treating these as separate tasks, our architecture leverages their inherent relationship through shared representations. This creates a powerful synergy where Δ ​ G \Delta G prediction benefits from mutation-aware components that identify critical binding residues, while Δ ​ Δ ​ G \Delta\Delta G prediction improves through the model’s understanding of baseline binding energetics. In general, this can resemble how experimental worlflows use wild-type binding measurements to contextualize mutation effects.

The model employs two specialized heads (Figure 1 ):

Δ ​ G \Delta G Head : Directly predicts the absolute binding affinity of the mutant complex

Δ ​ Δ ​ G \Delta\Delta G Head : Explicitly models the difference in binding affinity between mutant and wild-type

Formally, for the Δ ​ G \Delta G prediction:

where diff represents element-wise vector subtraction between embeddings.

For the Δ ​ Δ ​ G \Delta\Delta G prediction:

Overall, this dual-head approach enables direct optimization of both prediction, and creates an inductive bias that explicitly models the relationship between absolute binding and mutation effects.


## 3.3 Loss Function and Training

We train our model using a weighted combination of mean squared error (MSE) losses for Δ ​ G \Delta G and Δ ​ Δ ​ G \Delta\Delta G predictions:

where λ \lambda is a hyperparameter that controls the relative importance of the two prediction tasks. For samples where wild-type data is unavailable (and thus Δ ​ Δ ​ G \Delta\Delta G cannot be calculated), we scale the Δ ​ G \Delta G loss by ( 1 + λ ) (1+\lambda) to maintain consistent loss magnitudes across batches:

This adaptive loss formulation allows our model to train effectively on heterogeneous datasets containing both complete mutation pairs and standalone binding affinity measurements.

Additionally, to enhance our training data, we implemented a symmetry-based augmentation technique. For each protein pair ( A , B ) (A,B) with mutation from sequence S A S_{A} to S B S_{B} and corresponding Δ ​ Δ ​ G \Delta\Delta G value, we create an additional training example with the roles reversed and the sign of Δ ​ Δ ​ G \Delta\Delta G inverted:

This augmentation effectively doubles our training data while reinforcing the physical constraint that the energy change when mutating from A to B must be the inverse of mutating from B to A.


## 4 Experimental Setup


## 4.1 Datasets

We constructed our dataset by integrating SKEMPI v2 ( Δ ​ Δ ​ G \Delta\Delta G values for protein-protein mutations) and PDBbind (experimental binding affinities), yielding 8,653 total samples. Using Evolutionary Classification of Protein Domains (ECOD) based family-level splitting to prevent information leakage, we allocated 6,732 Cheng2014 samples (77.8%) to training, representing 2,322 unique PDB complexes. The validation set contains 856 samples (9.9%) from 140 complexes in non-overlapping protein families, with the remaining 1,065 samples (12.3%) reserved as hold-out set. SKEMPI contributed 4,681 samples (69.5%) to training and 746 samples (87.1%) to validation, with PDBbind providing the remainder. This domain-based splitting strategy ensures a realistic evaluation scenario by maintaining structural separation between training and evaluation data.

For rigorous evaluation, we incorporated two challenging benchmarks. First, we utilized the PPB-Affinity-AF Liu2024 dataset containing protein complexes without experimental structures but with AlphaFold predictions, representing a practical test case for proteins with limited structural information. Second, a SARS-CoV-2 Spike-ACE2 dataset curated from deep mutational scanning experiments, featuring mutations observed in variants of concern (Q493R, S477N, E484K, N501Y). This balanced benchmark includes both binding-enriching and depleting mutations at the RBD-ACE2 interface, providing an unbiased assessment of mutation impact prediction Ozden2024 .


## 4.2 Implementation Details

While employing ESM3 embeddings paired with mutation-aware SWE pooling, a key preprocessing step involved handling multi-chain protein complexes in SKEMPI. For complexes with notation like 1abc_CDE_FGI (indicating chains C,D,E interact with F,G,I), we concatenated chains belonging to each interaction partner. This concatenation was necessary for 2,466 cases (28.5% of our dataset) and preserved valuable protein-protein affinity data that would otherwise be discarded. While this approach potentially introduced some noise into validation metrics, retaining these scarce interaction examples was crucial for enhancing model generalization.

We implemented hyperparameter optimization across learning rate, dropout rate, architecture depth, embedding dimensions, and loss weighting. The model was trained using AdamW optimizer with OneCycleLR scheduler, applying a weighted loss function that balances Δ ​ G \Delta G and Δ ​ Δ ​ G \Delta\Delta G prediction tasks, with batch size 32 and gradient accumulation for stability.


## 5 Results


## 5.1 Performance on Validation Set

Hyperparameter optimization yielded an architecture with a 256-slice SWE layer (64 reference points), 5-layer cross-attention (4 heads), and a deep MLP network (7 hidden layers, dimension 1536). The optimal configuration used dropout rate of 0.106, learning rate of 1.23 × 10 − 3 1.23\times 10^{-3} , and Δ ​ Δ ​ G \Delta\Delta G loss weight of 0.718.

We evaluated our architecture using hyperparameter optimization with early stopping to find optimal configurations. Table 1 presents the best validation metrics achieved.

Further analysis on our ECOD-separated held-out set revealed more modest performance metrics (Pearson: 0.299, Spearman: 0.307). We found that 70% of these complexes contained combined-chain representations, which impairs model performance by obscuring spatial information. Despite lower metrics on our stringent held-out set, Twin-Peaks demonstrated superior generalization on standardized benchmarks compared to other structure and sequence-based approaches. Our rigorous family-level splitting provides a more realistic assessment of how models perform on truly novel protein families—essential for real-world applications where structural similarity cannot be guaranteed.


## 5.2 Performance on Protein-Protein Binding Prediction and Viral-Protein Data

Table 2 shows the performance of our model compared to other methods. For Δ ​ G \Delta G prediction, our model achieves a Pearson correlation of 0.800, significantly outperforming structure-based methods. For Δ ​ Δ ​ G \Delta\Delta G prediction, our model achieves a correlation of 0.496, competitive with structure-based methods while offering advantages in speed, coverage, and not requiring structural information.


## 5.3 Ablation Studies

Table 3 shows that removing SWE pooling nearly eliminates Δ ​ Δ ​ G \Delta\Delta G prediction capability while significantly reducing Δ ​ G \Delta G performance. Using non-learnable reference points and replacing cross-attention with cosine similarity both demonstrate moderate performance drops. Surprisingly, disabling the dual-head architecture improved Δ ​ Δ ​ G \Delta\Delta G correlation but significantly reduced Δ ​ G \Delta G performance, suggesting potential optimization trade-offs between objectives.


## 6 Discussion and Conclusion

We presented Twin Peaks, a novel dual-head architecture for simultaneous prediction of protein-protein binding affinity with mutation-aware SWE pooling, mutation-specific cross-attention, and a dual-head prediction network. Our extensive benchmarking demonstrates that Twin Peaks performs on par with state-of-the-art structural models despite not requiring three-dimensional information. Notably, while many existing tools report high Pearson correlations on standard datasets like SKEMPI, they often fail to generalize outside their training distribution Tsishyn2024 .

In contrast, our model maintains consistent performance across diverse protein families, including those absent from the training data. This generalization capability is particularly evident in our results on viral proteins, where Twin Peaks outperforms structure-based methods, highlighting its value for monitoring emerging variants in rapidly evolving systems.

A significant advancement of our approach is the ability to detect effects of single residue mutations without structural information—a capability previously thought to require detailed 3D modeling. This sensitivity to subtle sequence changes arises from our mutation-aware components that explicitly track mutation positions and their influence throughout the network. Our model achieves the highest performance among sequence-only methods on our independently curated benchmark set for Δ ​ G \Delta G prediction, while closely matching the nuanced mutation capture capabilities of specialized structure-based methods on the COVID dataset.

Overall, Twin Peaks enables rapid screening of thousands of potential mutations in minutes rather than hours or days required by structure-based methods. The model can be seamlessly integrated into computational pipelines with docking and simulation tools, providing valuable initial screening before more computationally expensive methods are applied. By eliminating structural data requirements, our approach dramatically expands the range of proteins that can be studied, including those resistant to crystallization or with highly flexible regions. Our comprehensive analysis provides deeper insights into protein-protein interactions than methods focused on single metrics.

Future work could incorporate graph-based representations to better model long-range dependencies. Additionally, expanding the training data to improve generalization and exploring hybrid approaches that combine sequence-based and structure-based methods can be beneficial.

By providing accurate predictions without structural constraints, Twin Peaks opens new possibilities for studying protein function in systems previously inaccessible to computational methods, enabling novel applications in protein engineering, drug discovery, and understanding disease mechanisms.


## Funding

This work was partially funded by — Iowa State Startup Grant; Building A World of Difference Faculty Fellowship, NSF EPSCoR RII Track-1, Award Number DQDBM7FGJPC5, and Iowa Economic Development Authority Award Number: 24IEC006 to RC


## References