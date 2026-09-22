## Enhanced Protein Intrinsic Disorder Prediction Through Dual-View Multiscale Features and Multi-objective Evolutionary Algorithm

Intrinsically disordered regions of proteins play a crucial role in cell signaling and drug discovery. However, their high structural flexibility makes accurate residue-level prediction challenging. Existing methods often rely on single-view representations or rigid manual fusion strategies, which fail to effectively balance the complex interplay between local amino acid preferences and long-range sequence patterns. To address these limitations, we propose D2MOE, a Dual-View Multiscale Features and Multi-objective Evolutionary Algorithm, which consists of two stages. First, a dual-view multiscale feature extraction method is introduced. This method integrates evolutionary views with deep semantic views and employs multiscale extractors to capture structural information across diverse receptive fields. Second, a multi-objective evolutionary algorithm is designed to adaptively discover optimal fusion architectures. By co-evolving discrete feature selection and continuous fusion weights, the algorithm adaptively explores optimal cross-feature architectures to enhance predictive accuracy while maintaining model compactness. Experimental results across three benchmark datasets demonstrate that D2MOE consistently outperforms state-of-the-art methods. D2MOE combines the feature extraction capabilities of deep learning with the global search advantages of evolutionary algorithms, enabling efficient feature integration without manual design, and providing a robust computational tool for protein disorder prediction.


## I Introduction

Intrinsically disordered regions (IDRs) lack a single, stable three-dimensional structure under physiological conditions and instead populate heterogeneous conformational ensembles [ 1 , 2 ] . This structural plasticity enables context-dependent recognition and regulation in signalling and transcription, and has been linked to human disease and higher-order cellular organization [ 3 , 4 ] . Accurate IDRs prediction is therefore important for functional annotation and for interpreting the effects of proteome-wide sequence variation.

Experimental techniques provide accurate IDR characterization, however they are inherently costly and low-throughput [ 1 , 2 ] . The exponential growth of sequence databases has vastly outpaced these experimental capabilities, creating a gap between available sequences and structural annotations [ 5 , 6 ] . As a result, computational predictors have become indispensable tools for large-scale IDR identification and proteome analysis [ 7 ] .

Early computational approaches predominantly relied on physics-based energy estimation and machine learning classifiers utilizing hand-crafted features. Energy-based methods, exemplified by the IUPred series, quantify disorder propensity via pairwise interaction potentials, with IUPred3 [ 8 ] further integrating experimental annotations and AIUPred [ 9 ] coupling this energy-centric view with deep learning. In parallel, sequence-based machine learning predictors evolved from integrating evolutionary information to constructing complex, multi-level sequence profiles. A notable example is flDPnn [ 10 ] , which maps high-dimensional, complementary sequence descriptors to disorder scores through a deep feed-forward network. However, these methods remain limited by their reliance on expert-designed features or fixed sliding windows, which may fail to capture long-range dependencies and global context essential for complex disorder modeling [ 11 , 12 ] .

Recent advances have shifted IDRs prediction toward deep learning and protein language models (PLMs). Large pre-trained PLMs learn residue-level contextual semantics via self-supervision, thereby enabling a semantic view for disorder modeling [ 13 , 14 ] . Current PLM-based predictors primarily rely on ESM and ProtTrans. Regarding methods utilizing ESM embeddings, NetSurfP-3.0 [ 15 ] adopts ESM residue embeddings as semantic inputs and applies a lightweight CNN–BiLSTM multitask backbone to jointly predict local structural properties, such as secondary structure, disorder, and solvent accessibility. ADOPT [ 16 ] trains an ESM-based bidirectional Transformer under the supervision of NMR chemical-shift Z-scores. In comparison, other approaches leverage the ProtTrans series. For instance, LMDisorder [ 17 ] employs ProtTrans embeddings with a Transformer-based predictor. DisoFLAG [ 18 ] combines ProtT5 embeddings with GRU-based sequence modeling and a graph convolutional head to jointly predict disorder states and disorder-related functions. These PLM-based models demonstrate superior accuracy compared to prior methods.

Despite these advances, most predictors rely on single-view and single-scale feature extraction, which limits the richness of the representation and hinders the capture of both short and long disordered domains. Furthermore, the fusion of views and features is often overlooked, leading to inadequacies in selecting and integrating them for information complementarity. Given the complexity of biological information, diverse views and features may exhibit inherent intersections or complementarities. However, current models typically rely on manual feature selection and fusion, which is not only time-consuming and labor-intensive but also hinders effective information utilization and limits prediction performance. Evolutionary algorithms has shown promise for automating feature subset selection and fusion; however, most efforts limited to specific domains, such as image classification and other bioinformatics tasks [ 19 , 20 ] . Moreover, unlike standardized image data, protein data are highly complex, and residue-level IDR prediction poses substantially different challenges.

To address the aforementioned challenges we propose D2MOE, a dual-view multiscale feature and multi-objective evolutionary algorithm, for enhancing protein intrinsic disorder prediction. The dual-view multiscale feature strategy is designed to extract complementary representations and capture the sequence patterns of both short and long disordered regions. Additionally, the multi-objective evolutionary algorithm is introduced to adaptively perform feature selection and fusion, thereby reducing model complexity and improving prediction performance. The main contributions of this work are as follows:

A dual-view multiscale feature strategy is developed for intrinsic disorder prediction. The dual-view approach integrates HMM profiles to extract evolutionary information of proteins and ProtT5 embeddings to capture protein semantics, yielding complementary information. RNNs and multiscale CNNs capture global and local features, enriching protein representations and enhancing prediction performance.

A multi-objective evolutionary algorithm (MOEA) is introduced to adaptively perform feature selection and fusion. A differential evolution (DE) strategy introduces optimizable fusion weights, enhancing fusion flexibility. MOEA simultaneously maximizes predictive performance and minimizes the number of selected features, thereby improving predictive accuracy while reducing model complexity.

D2MOE consistently outperforms baselines across multiple evaluation metrics on three benchmark datasets. Dual-view and multiscale features are superior to alternative designs, and MOEA fusion exceeds fixed manual rules and its single-objective variant, with DE-based weight refinement providing additional gains.

The paper is organized as follows. Section II reviews related disorder predictors and motivates the proposed design. Section III describes the proposed framework and methodological details. Section IV introduces the datasets, implementation details, and metrics. Section V presents the main results and ablations. Finally, Section VI concludes the paper.


## II Related Work


## II-A Dual-View Multiscale Features Strategy

Multi-view and multi-feature learning have improved representation quality and predictive accuracy in vision and NLP, and are increasingly being adopted in bioinformatics [ 21 , 22 ] . For protein tasks, multi-view frameworks have been developed for subcellular localization [ 23 ] , drug–target interaction via multi-graph encoders [ 24 ] , and site prediction through the fusion of language-model embeddings with sequence descriptors [ 25 ] . However, these methods typically focus on modeling relationships across different views, while largely overlooking that each view itself can be represented by multiple heterogeneous features, thereby limiting multi-feature integration and adaptive feature selection within each view.

Meanwhile, multiscale feature extraction has also been shown to be valuable for modeling complex biomolecular systems. This is particularly relevant to IDRs, where short irregular segments and long disordered domains co-occur and require both local and long-range receptive fields. Multiscale convolutions and hierarchical extractors have been used to capture patterns across receptive-field scales in drug–target interaction prediction [ 26 ] , antigen–antibody binding modeling [ 27 ] , and protein model-quality assessment [ 28 ] . Collectively, these studies demonstrate that multiscale convolutions and hierarchical feature extractors are effective in capturing structural and interaction patterns across different spatial ranges. These methods motivate the application of multi-view, multiscale feature strategies to intrinsic disorder prediction; however, existing approaches often remain constrained by inadequate feature selection and inflexible fusion. These limitations further motivate adaptive cross-feature fusion strategies for intrinsic disorder prediction.


## II-B Multi-objective Evolutionary Algorithm

Information fusion is central to multi-view and multiscale learning because it links heterogeneous feature representations to the final predictor. Most existing approaches are based on hand-crafted, fixed heuristics, such as element-wise maximum or direct concatenation [ 21 ] . Such designs may not sufficiently model inter-feature dependencies and typically require manual selection of fusion rules, which can limit cross-view interactions and propagate redundant information to downstream predictors [ 29 , 30 ] . To address these limitations, global optimization methods, including evolutionary algorithms, particle swarm optimization, and genetic programming, have been employed to automatically search feature subsets and fusion structures [ 19 , 20 ] . In particular, the MOEA is commonly adopted to balance predictive performance against model complexity and to obtain compact models with competitive accuracy [ 31 , 32 ] . Nevertheless, most evolutionary fusion frameworks target generic representations or image-centric pipelines and are seldom tailored to IDRs prediction.

Multi-objective evolutionary feature selection is typically formulated as a discrete subset search that maximizes predictive performance while minimizing the number of selected features [ 20 ] . By contrast, fusion coefficients are continuous variables and are more appropriately optimized in continuous spaces, thereby supporting the coupling of subset selection with continuous weight optimization and the adoption of mixed-variable evolutionary designs with type-specific variation operators for discrete and continuous components [ 33 ] . DE is a classical optimizer for continuous parameter spaces and has been widely used to tune feature weights and fusion coefficients in biomedical and engineering applications [ 34 , 35 , 36 ] . However, when the candidate feature set is large, using DE alone to perform both subset selection and weight optimization can substantially expand the search space and exacerbate redundancy. Therefore, coupling multi-objective subset selection with DE-based continuous weight optimization is justified for adaptive, compact, and accurate fusion in dual-view multiscale IDRs prediction, and this NSGA-II–DE co-evolution scheme jointly optimizes the feature subset and fusion weights to improve accuracy while controlling complexity.


## III Methodology

The proposed D2MOE framework consists of two stages. In the first stage, a dual-view multiscale feature strategy is adopted to extract protein representations from complementary views and multiscale sequence features. In the second stage, a multi-objective evolutionary algorithm is employed to adaptively perform feature subset selection and weighted fusion, thereby improving predictive performance while reducing model complexity.


## III-A Dual-View Multiscale Features

The dual-view multiscale feature strategy comprises two steps: constructing complementary sequence representations and extracting features across multiple receptive-field scales as shown in Fig. 1 (A).

IDRs exhibit heterogeneous sequence cues that are difficult to capture using a single information source. DV-MsF therefore represents each residue from two complementary views: an evolutionary view derived from HHblits-based HMM profiles and a semantic view derived from ProtT5 embeddings. These residue-wise representations are used as inputs to the subsequent multiscale feature extractors.

ProtT5 is used to provide a residue-wise semantic representation learned from large-scale self-supervised pretraining, enabling contextual modeling of non-local dependencies [ 13 , 14 ] . For a protein sequence of length L L , ProtT5 yields E T5 ∈ ℝ L × 1024 , E_{\text{T5}}\in\mathbb{R}^{L\times 1024}, where each row is a 1024-dimensional contextual embedding. Such embeddings have been shown to encode disorder-relevant biochemical and structural cues and to generalize without requiring multiple sequence alignments [ 17 , 16 , 15 ] .

An evolutionary representation is constructed from HHblits-derived HMM profiles to capture conservation patterns and substitution preferences. For a sequence of length L L , HHblits produces an L × 30 L\times 30 profile; following common practice, the first 20 substitution-statistics channels are retained as E HMM ∈ ℝ L × 20 . E_{\text{HMM}}\in\mathbb{R}^{L\times 20}. This view provides explicit family-level constraints that complement the contextual semantics encoded by E T5 E_{\text{T5}} .

The goal of multiscale feature extraction is to improve IDRs prediction performance by capturing a broader range of sequence-derived characteristics. According to the properties of disordered regions and the respective strengths of CNNs and RNNs, six base extractors, CNN1, CNN2, CNN3, CNN4, RNN1, and RNN2, are employed in each view. The formation of IDRs is typically governed by both local amino-acid composition and global structural flexibility, making local and global information equally important. IDRs are governed by both short-range compositional irregularities and long-range conformational flexibility. Therefore, multiscale CNNs capture local motifs across varying receptive fields, while RNNs integrate sequential context to model global dynamics and long-range dependencies. To accommodate the large variability in IDRs lengths, CNNs with different receptive fields are adopted to cover sequence features at different scales. As summarized in Algorithm 1 , these six extractors jointly extract global and local features from inputs of the two views, and their corresponding architectures are illustrated in Fig. 1 (A).

All feature extractors follow a unified processing pipeline that includes protein sequence preprocessing, feature extraction, dimensionality reduction, and output generation. Samples from the training set 𝒟 tr \mathcal{D}_{\text{tr}} and validation set 𝒟 val \mathcal{D}_{\text{val}} are used as inputs to train the six extractors CNN1, CNN2, CNN3, CNN4, RNN1, and RNN2 in each view. For a protein sequence of length L L , the corresponding view input is first concatenated with residue one-hot encodings along the feature dimension to obtain a view-specific sequence representation. This representation is then projected by a fully connected layer with ReLU activation into an L × 256 L\times 256 intermediate feature matrix. The intermediate features are fed into one of the six CNN or RNN extractors to learn multiscale sequence patterns. Subsequently, stacked fully connected layers are applied for channel integration and dimensionality reduction, yielding a 256-dimensional high-level feature vector. The prediction head outputs logits for order and disorder, which are mapped to residue-wise probabilities via a softmax layer. Finally, for each extractor, the 256-dimensional penultimate representation is concatenated with the 2-dimensional logits to form a 258-dimensional candidate feature vector. Applying this pipeline to all six extractors in both views yields 12 candidate descriptors: HMM-CNN1, HMM-CNN2, HMM-CNN3, HMM-CNN4, HMM-RNN1, HMM-RNN2, T5-CNN1, T5-CNN2, T5-CNN3, T5-CNN4, T5-RNN1, and T5-RNN2. These twelve descriptors jointly constitute the candidate feature pool used by the subsequent MOEA-based adaptive fusion module.

Input: Training and Validation dataset with dual views 𝒟 tr = { ( 𝒳 HMM , 𝒴 ) , ( 𝒳 T5 , 𝒴 ) } \mathcal{D}_{\text{tr}}=\{(\mathcal{X}_{\text{HMM}},\mathcal{Y}),(\mathcal{X}_{\text{T5}},\mathcal{Y})\} ; 𝒟 val = { ( 𝒳 ~ HMM , 𝒴 ~ ) , ( 𝒳 ~ T5 , 𝒴 ~ ) } \mathcal{D}_{\text{val}}=\{(\tilde{\mathcal{X}}_{\text{HMM}},\tilde{\mathcal{Y}}),(\tilde{\mathcal{X}}_{\text{T5}},\tilde{\mathcal{Y}})\} . Output: Multi-feature set ℱ = { ϕ t } t = 1 12 \mathcal{F}=\{\phi_{t}\}_{t=1}^{12} . 1: Concatenate the view information with a residue one-hot encoding to obtain the view embedding; 2: Input the view embedding to a fully connected layer with ReLU activation, output a 256 256 -dimensional vector; 3: Input the obtained vector to the following extractors: - Option 1: One small-kernel CNN layer (CNN1); - Option 2: Two small-kernel CNN layers (CNN2); - Option 3: One large-kernel CNN layer (CNN3); - Option 4: Two large-kernel CNN layers (CNN4); - Option 5: One BiLSTM layer (RNN1); - Option 6: Two BiLSTM layers (RNN2); 4: Input the obtained vector to: - Case 1 (CNN1–CNN4): Three fully connected layers with ReLU activation, resulting in outputs of 256, 256, and 2 dimensions, respectively; - Case 2 (RNN1 or RNN2): Three fully connected layers with ReLU activation, resulting in outputs of 512, 256, and 2 dimensions, respectively; 5: Apply the Softmax function to the 2-dimensional logits, output residue-wise order or disorder predictions; 6: return ϕ t \phi_{t} obtained by concatenating the 256-dimensional penultimate fully connected layer output and the 2-dimensional logits, yielding a 258-dimensional feature vector.


## III-B Multi-objective Evolutionary Algorithm

The MOEA module is employed to adaptively perform feature selection and feature fusion while reducing model complexity and improving predictive accuracy. As shown in Fig. 1 (B) and (C), the procedure consists of three components: encoding, evolutionary search, and decoding. First, candidate features are encoded into individual representations. NSGA-II is then employed to jointly optimize two objectives, prediction performance and the number of selected features, thereby adaptively selecting feature subsets and determining the fusion structure. Finally, solutions on the Pareto front are decoded to obtain concrete fusion models. In this way, NSGA-II avoids the limitations of manually designed architectures and alleviates the negative effects of feature redundancy, whereas the DE algorithm optimizes fusion weights across features, highlighting informative features and further improving the overall predictive performance of the model.

Let ℱ \mathcal{F} denote the set of 12 candidate features produced by DV–MsF, and let Ω = { A ​ d ​ d , M ​ u ​ l , M ​ a ​ x , M ​ i ​ n } \Omega=\{Add,Mul,Max,Min\} be the set of basic element-wise fusion operators, where Add/Mul/Max/Min correspond to weighted summation, Hadamard product, element-wise maximum, and element-wise minimum, respectively. Let 𝐚 \mathbf{a} be the fusion weight matrix whose elements are aligned with the corresponding features during fusion. Each individual is represented as χ = [ 𝐬 , 𝐪 , 𝐚 ] , \chi=[\mathbf{s},\mathbf{q},\mathbf{a}], where 𝐬 = ( s 1 , … , s n ) \mathbf{s}=(s_{1},\ldots,s_{n}) is a sequence of selected features from ℱ \mathcal{F} , and a feature may be selected more than once, 𝐪 = ( q 1 , … , q n − 1 ) \mathbf{q}=(q_{1},\ldots,q_{n-1}) is the operator sequence, and 𝐚 = ( a 1 , 1 , a 1 , 2 , … , a n − 1 , 1 , a n − 1 , 2 ) \mathbf{a}=(a_{1,1},a_{1,2},\ldots,a_{n-1,1},a_{n-1,2}) is the corresponding fusion-weight vector. The number of features, n n , is individual-specific with n ∈ [ 1 , n max ] n\in[1,n_{\max}] and n max = 12 n_{\max}=12 .

Given an individual χ \chi , it is decoded into a left-fold fusion tree, as illustrated in Fig. 1 (B). We first initialize 𝐜 1 = 𝐬 1 \mathbf{c}_{1}=\mathbf{s}_{1} . For t = 2 , … , n t=2,\ldots,n , we iteratively compute

The final descriptor 𝐜 n \mathbf{c}_{n} is then mapped to a probability vector y ^ \hat{y} through a fully connected layer whose weight matrix is estimated by the least-squares method; a subsequent Softmax function is applied to y ^ \hat{y} to obtain the final prediction 𝒴 ~ \tilde{\mathcal{Y}} .

In this representation, 𝐬 \mathbf{s} and 𝐪 \mathbf{q} jointly determine which features and operators are selected in the fusion network and how they are combined. For implementation convenience, we index the 12 candidate features by integers ∼ 11 0\!\sim\!11 and map the four operators to integers ∼ 3 0\!\sim\!3 ; in what follows, we still use s t s_{t} and q t q_{t} to denote the selected feature and operator, respectively.

As illustrated in Algorithm 2 , follows an NSGA-II + DE co-evolution scheme: NSGA-II optimizes ( 𝐬 , 𝐪 ) (\mathbf{s},\mathbf{q}) under a multi-objective selection mechanism, while DE refines 𝐚 \mathbf{a} in the continuous space. It consists of four major steps: population initialization (line 1), fitness evaluation (lines 3 and 10), mutation and crossover (lines 8–9), and new population generation plus optimal solution selection (lines 13 and 17).

Given a population size N N and maximal generation G max G_{\max} , the initial population 𝒫 ( 0 ) \mathcal{P}^{(0)} is randomly generated. Each individual is represented as χ k = [ 𝐬 k , 𝐪 k , 𝐚 k ] \chi_{k}=[\mathbf{s}_{k},\mathbf{q}_{k},\mathbf{a}_{k}] , where the feature number n k = length ⁡ ( 𝐬 k ) n_{k}=\mathrm{length}(\mathbf{s}_{k}) may vary across individuals.

The fitness of each individual is evaluated using two objectives: maximizing accuracy and minimizing the feature number. Accuracy is measured by the AUC metric, whereas the feature number is used to reduce the number of selected features, avoid redundancy, and lower model complexity.

Accuracy: For a given individual χ k \chi_{k} , predictions 𝒴 ~ \tilde{\mathcal{Y}} are first computed according to the decoding procedure. The AUC is defined as

where y j ∈ { 0 , 1 } y_{j}\in\{0,1\} and y ^ j ∈ [ 0 , 1 ] \hat{y}_{j}\in[0,1] denote the ground-truth labels and predicted disorder probabilities, and N res N_{\mathrm{res}} is the total number of residues.

Feature number: The second objective aims to minimize redundant features in the fusion tree so as to avoid performance degradation and reduce model complexity. For an individual χ k = [ 𝐬 k , 𝐪 k , 𝐚 k ] \chi_{k}=[\mathbf{s}_{k},\mathbf{q}_{k},\mathbf{a}_{k}] , the feature number is defined as

where n k n_{k} denotes the number of features used in individual χ k \chi_{k} .

Input: Candidate feature set ℱ \mathcal{F} ; fusion operator set Ω \Omega ; population size N N ; maximal generation G max G_{\max} ; labels 𝒴 \mathcal{Y} ; mutation probability P mu P_{\text{mu}} ; population 𝒫 \mathcal{P} maximum number of features in an individual n max n_{\max} . Output: Best individual χ best \chi_{\text{best}} and its corresponding fusion network. 1: Initialize the population 𝒫 ( 0 ) = { χ k = [ 𝐬 k , 𝐪 k , 𝐚 k ] } k = 1 N \mathcal{P}^{(0)}=\{\chi_{k}=[\mathbf{s}_{k},\mathbf{q}_{k},\mathbf{a}_{k}]\}_{k=1}^{N} according to the encoding scheme and set the current generation index g = 0 g=0 . 2: for each individual χ k \chi_{k} in 𝒫 ( 0 ) \mathcal{P}^{(0)} do 3: Decode χ k \chi_{k} into its corresponding fusion network, and compute fitness values F 1 ​ ( χ k ) F_{1}(\chi_{k}) and F 2 ​ ( χ k ) F_{2}(\chi_{k}) . 4: end for 5: while g < G max g<G_{\max} do 6: 𝒰 = COPY ⁡ ( 𝒫 ( g ) ) \mathcal{U}=\mathrm{COPY}(\mathcal{P}^{(g)}) ; 7: for k = 1 k=1 to N N do 8: χ m = HYBRID ​ _ ​ MUTATION ​ ( χ k , P mu , 𝒫 ( g ) ) \chi_{m}=\mathrm{HYBRID\_MUTATION}(\chi_{k},P_{\text{mu}},\mathcal{P}^{(g)}) ; 9: χ c = HYBRID ​ _ ​ CROSSOVER ​ ( χ k , χ m ) \chi_{c}=\mathrm{HYBRID\_CROSSOVER}(\chi_{k},\chi_{m}) ; 10: Decode χ m \chi_{m} and χ c \chi_{c} into their corresponding fusion networks, and compute the fitness of χ m \chi_{m} and χ c \chi_{c} ; 11: 𝒰 = 𝒰 ∪ { χ m } ∪ { χ c } \mathcal{U}=\mathcal{U}\cup\{\chi_{m}\}\cup\{\chi_{c}\} ; 12: end for 13: 𝒫 ( g + 1 ) = GET ​ _ ​ NEXT ​ _ ​ GENERATION ​ ( 𝒰 ) \mathcal{P}^{(g+1)}=\mathrm{GET\_NEXT\_GENERATION}(\mathcal{U}) ; 14: 𝒰 = ∅ \mathcal{U}=\emptyset ; 15: g = g + 1 g=g+1 ; // Update generation index 16: end while 17: χ best ← \chi_{\text{best}}\leftarrow Select the individual with the best fitness from the final Pareto front. 18: return the fusion network decoded from χ best \chi_{\text{best}} .

Hybrid mutation and crossover are adopted in MOEA. Hybrid mutation simultaneously modifies the integer part of the chromosome (feature selection 𝐬 \mathbf{s} and operator selection 𝐪 \mathbf{q} ) and the real-valued part (fusion weight matrix 𝐚 \mathbf{a} ). Integer mutation randomly perturbs selected features or operators, whereas real-valued mutation updates the weights using the DE strategy. Hybrid crossover performs single-point crossover between parent chromosomes by exchanging segments of features, operators, and weights to generate offspring.

The detailed procedures of hybrid mutation and hybrid crossover used in Algorithm 2 are given below.

i) Hybrid Mutation. Since an individual χ k \chi_{k} contains both an integer part ( 𝐬 k \mathbf{s}_{k} and 𝐪 k \mathbf{q}_{k} ) and a real-valued part ( 𝐚 k \mathbf{a}_{k} ), different mutation strategies are applied to generate a new chromosome vector χ m = [ 𝐬 m , 𝐪 m , 𝐚 m ] \chi_{m}=[\mathbf{s}_{m},\mathbf{q}_{m},\mathbf{a}_{m}] , where χ m \chi_{m} is initialized as a copy of χ k \chi_{k} , and n m = length ⁡ ( 𝐬 m ) n_{m}=\mathrm{length}(\mathbf{s}_{m}) denotes the current number of selected features.

Integer Component Mutation: For the feature sequence 𝐬 m \mathbf{s}_{m} and operator sequence 𝐪 m \mathbf{q}_{m} , integer mutation consists of three operations:

Generate a random number R R . If R ≤ P mu R\leq P_{\text{mu}} , resample n ∼ U ⁡ ( 1 , n max ) n\sim U(1,n_{\max}) . If n < n m n<n_{m} , truncate 𝐬 m , 𝐪 m , 𝐚 m \mathbf{s}_{m},\mathbf{q}_{m},\mathbf{a}_{m} to length n n ; if n > n m n>n_{m} , extend 𝐬 m \mathbf{s}_{m} with random features from ℱ \mathcal{F} , extend 𝐪 m \mathbf{q}_{m} with random operators from Ω \Omega , and initialize the newly added weights uniformly in [ 0.1 , 2 ] [0.1,2] .

Generate another random number R R . If R ≤ P mu R\leq P_{\text{mu}} , randomly select an index t ∈ [ 1 , n m ] t\in[1,n_{m}] and replace the corresponding feature s m ​ [ t ] s_{m}[t] with another candidate in ℱ \mathcal{F} .

Generate another random number R R . If R ≤ P mu R\leq P_{\text{mu}} , randomly select an index j ∈ [ 1 , n m − 1 ] j\in[1,n_{m}-1] and replace the corresponding operator q m ​ [ j ] q_{m}[j] with an operator in Ω \Omega .

Real-Valued Component Mutation: To update the continuous fusion weights, an improved DE-based mutation is adopted:

where 𝐚 1 , 𝐚 2 , 𝐚 3 \mathbf{a}^{1},\mathbf{a}^{2},\mathbf{a}^{3} are the real-valued parts of three individuals χ 1 , χ 2 , χ 3 \chi^{1},\chi^{2},\chi^{3} , respectively. The three individuals χ 1 , χ 2 , χ 3 \chi^{1},\chi^{2},\chi^{3} are randomly sampled from the population 𝒫 ( 0 ) \mathcal{P}^{(0)} and sorted in descending order according to F 1 F_{1} . The differential weight decays linearly with the generation index g g :

ii) Crossover Operation. Crossover is applied between two parent individuals χ k = [ 𝐬 k , 𝐪 k , 𝐚 k ] \chi_{k}=[\mathbf{s}_{k},\mathbf{q}_{k},\mathbf{a}_{k}] and χ m = [ 𝐬 m , 𝐪 m , 𝐚 m ] \chi_{m}=[\mathbf{s}_{m},\mathbf{q}_{m},\mathbf{a}_{m}] to generate a new chromosome vector χ c = [ 𝐬 c , 𝐪 c , 𝐚 c ] \chi_{c}=[\mathbf{s}_{c},\mathbf{q}_{c},\mathbf{a}_{c}] .

Step 1: Randomly select a crossover point n c n_{c} such that n c ∈ { 1 , … , min ⁡ ( n k , n m ) } n_{c}\in\{1,\ldots,\min(n_{k},n_{m})\} .

Step 2: Perform synchronized single-point crossover on the three components:

The resulting χ c \chi_{c} is taken as the offspring produced by hybrid crossover.

At each generation, the parent, mutated, and crossover populations are merged into a joint pool 𝒰 \mathcal{U} . Under the two objectives of maximizing predictive accuracy and minimizing feature number, NSGA-II performs fast non-dominated sorting and crowding-distance based selection, retaining the top N N individuals to form the next generation. After reaching G max G_{\max} or satisfying a convergence criterion, the solution with the highest fitness score on the final Pareto front is selected as χ best \chi_{\text{best}} , which encodes the final feature subset, operator sequence, and weight configuration for compact and accurate IDRs prediction.


## IV Experiments


## IV-A Datasets

The training and validation protocol of NetSurfP - 3.0 was followed [ 15 ] , and model performance was evaluated on three established benchmark test sets:

TS115 [ 37 ] : Consisting of 115 non-redundant PDB proteins with low sequence similarity, TS115 is widely used for stringent evaluation, as reduced redundancy and structural diversity provide a more demanding test of robustness.

CASP12 [ 38 ] : Originating from the CASP12 blind assessment (21 targets), CASP12 contains proteins of varying complexity and thereby better reflects realistic test conditions, offering a challenging scenario for IDRs prediction.

CB513 [ 39 ] : Comprising 513 segments from 434 proteins, CB513 covers diverse structural and functional contexts and serves as a standard benchmark for assessing generalization in residue-level IDRs prediction.

For efficient mini-batch training, each protein sequence was standardized to a maximum length of 700 residues. Sequences shorter than 700 residues were padded, while longer sequences were split into 700-residue segments. To prevent padded positions from affecting the training objective, we applied loss masking, and this padding-aware strategy aligns with prior work [ 15 ] . Specifically, we used a PDB-derived non-redundant split with standard filtering: proteins shorter than 20 residues were excluded and clusters containing validation sequences were removed, yielding 10,837 proteins; 500 were randomly selected for validation and 10,337 for training.


## IV-B Experimental Setting

All experiments were run on a single NVIDIA GeForce RTX 3090 GPU with 24 GB memory, using Python 3.9 and PyTorch 2.0.0 with CUDA 11.8. The Adam optimizer implemented in PyTorch was used for training. The training was stopped when the validation loss did not improve for 10 epochs, and the checkpoint with the lowest validation loss across all epochs was selected as the final model. Such early stopping was used to avoid potential overfitting on smaller datasets. All hyperparameters were selected through empirical testing and established best practices to optimize performance and ensure training stability. Table I summarizes the key hyperparameters used in this study.


## IV-C Evaluation Metrics

Model performance was evaluated using four metrics: Matthews Correlation Coefficient (MCC), area under the ROC curve (AUC), area under the Precision–Recall curve (AUPR), and F1. MCC and F1 were computed on binarized predictions using a fixed threshold τ = 0.5 \tau=0.5 (a residue is predicted as disordered if its propensity ≥ τ \geq\tau ).

where TP \mathrm{TP} , TN \mathrm{TN} , FP \mathrm{FP} , and FN \mathrm{FN} are the numbers of true positives, true negatives, false positives, and false negatives, respectively.

where Precision reflects the reliability of predicted disordered residues and Recall reflects the coverage of true disordered residues.

where TPR captures sensitivity to disordered residues and FPR captures the propensity to misclassify ordered residues as disordered.

where all symbols follow the definitions above.


## V Results

The results are presented in four parts: first, D2MOE is benchmarked against seven representative IDRs predictors on CB513, TS115, and CASP12; second, the impact of the dual-view design is evaluated; third, the benefit of multiscale and hybrid feature extraction is examined; and finally, the effectiveness of the proposed multi-objective evolutionary fusion is assessed.


## V-A Comparison With State-of the-Art Methods

D2MOE was benchmarked against seven representative IDRs predictors on CB513, TS115, and CASP12, including energy-based methods IUPred3 [ 8 ] and AIUPred [ 9 ] , a profile and descriptor integration model flDPnn [ 10 ] , and four PLM-driven predictors NetSurfP - 3.0 [ 15 ] , LMDisorder [ 17 ] , DisoFLAG [ 18 ] , and ADOPT [ 16 ] . Results are summarized in Fig. 2 (a–c), with CASP12 ROC and PR curves in Fig. 2 (d,e).

D2MOE ranks first in MCC and AUPR on all three benchmarks. The gain is most pronounced on CASP12, improving MCC by 7.9% over NetSurfP - 3.0 and AUPR by 13.9% over LMDisorder, consistent with the ROC and PR curves in Fig. 2 (d,e). On TS115, MCC and AUPR reach 0.677 and 0.773, while AUC and F1 remain close to NetSurfP - 3.0; on CB513, MCC and AUPR increase by 7.6% and 4.7% over NetSurfP - 3.0. Notably, LMDisorder attains the highest AUC on CB513, yet its lower MCC and AUPR indicate that improved ranking does not necessarily yield a favourable PR trade-off under imbalance. More broadly, PLM-based predictors NetSurfP - 3.0, LMDisorder, DisoFLAG, and ADOPT generally outperform energy-based methods IUPred3 and AIUPred and the profile and descriptor integration model flDPnn in MCC and AUPR, highlighting the value of contextual semantic representations. Building on this advantage, D2MOE augments ProtT5-derived semantics with an explicit evolutionary view from HHblits-HMM profiles and exploits complementary evidence across multiple receptive-field scales and long-range dependencies. In addition, MOEA-based adaptive fusion searches for compact, discriminative feature combinations and calibrates cross-view contributions, which can suppress redundancy and stabilize PR performance. Collectively, these results suggest that combining PLM semantics with complementary evolutionary constraints and adaptive fusion yields more reliable residue-level disorder prediction across diverse benchmarks.

(a) TS115

(b) CASP12

(c) CB513

(a) TS115

(b) CASP12

(c) CB513


## V-B Validation of the Dual-view Design

To assess whether jointly modeling semantic and evolutionary evidence benefits residue-level disorder prediction, the dual-view D2MOE was compared with two single-view variants, T5 and HMM, on CB513, TS115 and CASP12 (Fig. 3 ). D2MOE performs best on TS115 and CASP12, achieving the highest MCC and AUPR while remaining competitive in AUC and F1. In particular, on TS115, D2MOE attains an MCC of 0.677 and an AUPR of 0.773, exceeding T5; on CASP12, it reaches an MCC of 0.646 and an AUPR of 0.739, again outperforming T5. On CB513, D2MOE yields the best MCC and F1, with an AUPR comparable to T5 and a marginally lower AUC. Overall, T5 consistently outperforms HMM across all four metrics, indicating that ProtT5-derived semantic representations provide stronger discriminative evidence than evolutionary statistics alone. Moreover, the additional gains obtained by D2MOE over T5 on TS115 and CASP12 support the complementarity between ProtT5 semantics and HHblits-HMM evolutionary profiles, and show that their integration leads to more accurate and stable disorder prediction across benchmarks.


## V-C Validation of Multiscale and Hybrid Feature Extraction

To evaluate the contribution of multiscale convolutions, D2MOE was compared with two single-scale hybrid variants, DV-SSF and DV-BSF, in Table II . DV-SSF combines small-kernel convolutions with an RNN module, whereas DV-BSF adopts large-kernel convolutions while keeping the same hybrid backbone. On CB513, D2MOE achieves the best MCC and F1, while AUC and AUPR are slightly lower than those of the single-scale hybrids. More importantly, D2MOE achieves the best overall performance on TS115, reaching an AUC of 0.954, an AUPR of 0.773, an MCC of 0.677, and an F1 of 0.696. On CASP12, D2MOE also achieves the best overall performance, attaining an MCC of 0.646 and an AUPR of 0.739. These results suggest that integrating multiple receptive fields better accommodates disordered segments of varying lengths, improves feature expressiveness, and improves prediction performance.

To assess the effect of hybrid CNN and RNN modeling, D2MOE was further compared with two constrained variants that use a single feature extractor, CNN-only and RNN-only, under otherwise identical settings in Table II . On CB513, D2MOE again yields the highest MCC and F1, with an MCC of 0.498 and an F1 of 0.503, while AUC is comparable and AUPR is lower than those of the single-extractor variants. On TS115 and CASP12, the hybrid model improves all four metrics over both single-extractor variants. Encouragingly, on CASP12, the MCC increases by approximately 4.5% relative to the CNN-only model, rising from 0.618 to 0.646. Overall, coupling CNN-based local pattern extraction with RNN-based long-range context modeling provides richer representations and yields more consistent gains in residue-level disorder prediction.


## V-D Evaluation of Multi-objective Evolutionary Algorithm

The contribution of the MOEA is examined from three aspects: comparison against fixed element-wise fusion operators, the effect of DE-based fusion weights, and the multi-objective formulation that enforces compact yet complementary feature integration beyond any single descriptor.

To assess whether the MOEA-derived fusion is preferable to hand-crafted element-wise rules, it was compared with four fixed operators (Add, Mul, Max, and Min). As shown in Fig. 4 (a–c), D2MOE forms the outermost radar profile on TS115 and CASP12, fully enclosing the contours of all four fixed operators, indicating consistent advantages across all four metrics. On CB513, D2MOE likewise provides the dominant envelope over most metric dimensions. These results underscore that effective fusion is critical when exploiting the multi-view multiscale feature library, and that automated MOEA-driven fusion is generally preferable to fixed, manually specified element-wise operators.

To evaluate the contribution of DE weight optimization, two independent MOEA searches were performed. In the DE-enabled setting, fusion coefficients were evolved in the continuous space, whereas in the weight-free variant all fusion coefficients were fixed to unity (denoted as W=1). Each setting was assessed using the best individual returned by its corresponding search. As summarized in Table III , enabling DE yields consistently stronger performance across CB513, TS115, and CASP12. These results indicate that learning data-adaptive fusion weights helps calibrate the relative contributions of the selected features, providing greater fusion flexibility than uniform weighting and translating into more reliable predictive quality across benchmarks.

To assess the value of the multi-objective formulation, the D2MOE was compared with the single-objective DV-MsF-EA, which optimises predictive performance alone and does not penalise feature-set size. Table IV shows that the two variants are broadly comparable on the three datasets, whereas D2MOE shows stronger generalization on TS115 and CASP12. On TS115, D2MOE achieves MCC of 0.677 and F1 of 0.696, compared with MCC of 0.675 and F1 of 0.694 for DV-MsF-EA. On CASP12, D2MOE reaches MCC of 0.646 and F1 of 0.667, compared with MCC of 0.623 and F1 of 0.654. Importantly, these gains are obtained with a substantially more compact solution: the selected D2MOE uses seven features, whereas the selected DV-MsF-EA uses twelve, indicating that the multi-objective formulation can reduce redundancy while preserving accuracy.

The best-evolved fusion architecture in Fig. 5 helps explain why a compact solution remains competitive. The selected model integrates semantic and evolutionary representations and combines multiscale local cues with longer-range dependencies, rather than relying on a single view or a single extractor family. This interpretation is supported by the feature-level evidence in Table V . Some single features attain strong threshold-independent scores on CB513, for example, T5-CNN1 reaches AUC of 0.918, yet none delivers uniformly strong threshold-based performance across benchmarks. On TS115, the best single feature reaches MCC of 0.669 and F1 of 0.689, remaining below D2MOE with MCC of 0.677 and F1 of 0.696. CASP12 shows the same trend. Collectively, the gains are best explained by complementary cross-view and cross-scale signals captured through adaptive fusion, rather than by any single descriptor or by expanding the feature set.


## VI Conclusion

This study introduces D2MOE, a Dual-View Multiscale Features and Multi-objective Evolutionary framework for enhancing residue-level intrinsic disorder prediction. The framework integrates two distinct sequence views and employs multiscale CNNs to capture local patterns at varying lengths, together with an RNN to encode long-range dependencies, thereby enriching protein representations. Furthermore, a multi-objective evolutionary search is employed to select informative feature subsets and automatically design cross-feature fusion architectures, reducing the rigidity and redundancy of handcrafted fusion rules. Additionally, DE is used to optimize fusion weights for the selected subset and fusion structure, thereby further improving performance. Overall, the multi-objective formulation better balances predictive performance and compactness by reducing model complexity while maintaining predictive quality. Experiments on three benchmark test sets demonstrate that D2MOE outperforms state-of-the-art methods over multiple evaluation metrics while eliminating dependence on manually specified fusion architectures.

Despite these strengths, limitations remain. First, while the evolved feature subsets and fusion architectures are promising, their interpretation remains challenging, limiting decision traceability and biological insights. Future work will focus on enhancing model interpretability. Second, although the framework performs well on standard tasks, it faces challenges in more complex ones, such as Protein Functional Site Prediction. Future research will explore incorporating topological data and additional features to improve generalization across tasks.


## Acknowledgements

This work was supported in part by the National Natural Science Foundation of China (NSFC) under Grant Nos. 62522309, and in part by the Natural Science Foundation of Liaoning Province under Grant No. 2025JH6/101000012.


## References