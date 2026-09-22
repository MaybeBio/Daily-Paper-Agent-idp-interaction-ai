## Abstract

Physical interactions of proteins play key roles in many important cellular processes. Therefore, it is crucial to determine the structure of protein complexes to understand molecular mechanisms of interactions. To complement experimental approaches, which usually take a considerable amount of time and resources, various computational methods have been developed to predict the structures of protein complexes. In computational modeling, one of the challenges is to identify near-native structures from a large pool of generated models. Here, we developed a deep learning-based approach named Graph Neural Network-based DOcking decoy eValuation scorE (GNN-DOVE). To evaluate a protein docking model, GNN-DOVE extracts the interface area and represents it as a graph. The chemical properties of atoms and the inter-atom distances are used as features of nodes and edges in the graph. GNN-DOVE was trained and validated on docking models in the Dockground database. GNN-DOVE performed better than existing methods including DOVE, which is our previous development that uses convolutional neural network on voxelized structure models.


## 1 Introduction

Experimentally determined protein structures provide fundamental information about the physicochemical nature of biological function of protein complexes. With the recent advances in cryo-electron microscopy, the number of experimentally determined protein complex structures has been increasing rapidly. However, experimental methods are costly in terms of money and time. To aid the experimental efforts, computational modeling approaches for protein complex structures, often referred to as protein docking ( 1 ), have been extensively studied over the past two decades.

Protein docking methods aim to build the overall quaternary structure of a protein complex from the tertiary structure information of individual chains. Similar to other protein structure modeling methods, protein docking can also be divided into two main categories: template-based methods ( 2 , 3 ), which use a known structure as a scaffold of modeling, and ab initio methods, which assemble individual structures and score generated models to choose most plausible ones. In ab initio methods, various approaches were used for molecular structure representations ( 4 ) ( 5 ). These include docking conformational searches, such as Fast Fourier Transform ( 6 , 7 ), geometric hashing ( 4 , 8 ), and particle swarm optimization ( 9 ), and for considering protein flexibility ( 10 , 11 ). Development of new methods aim to extend and surpass the capabilities of simple pairwise docking, such as multi-chain docking ( 12 - 14 ), peptide-protein docking ( 15 - 17 ), docking with disordered proteins ( 18 ), docking order prediction ( 19 , 20 ), and docking for cryo-EM maps ( 21 , 22 ). Researchers have also applied recent advances in deep learning to further boost docking performance ( 23 - 25 ).

Although substantial improvements have been made in ab initio protein docking, selecting near-native (i.e. correct) models out of a large number of produced models, which are often called decoys, is still challenging. The difficulty is partly due to a substantial imbalance of the number of near-native models and incorrect decoys in a generated decoy pool. The accuracy of scoring decoys certainly determines the overall performance of protein docking, and thus there are active developments of scoring functions ( 26 ) for docking models. Recognizing the importance of scoring, the Critical Assessment of PRediction of Interactions (CAPRI) ( 27 ), which is the community-based protein docking prediction experiments, has arranged a specific category of evaluating scoring methods, where participants are asked to select 10 plausible decoys from over thousands of decoys provided by the organizers. Over the last two decades, various approaches have been developed for scoring decoys. The main categories include physics-based potentials ( 11 ), scoring based on interface shape ( 4 , 28 ), knowledge-based statistical potentials ( 29 , 30 ), machine learning methods ( 31 ), evolutionary profiles of interface residues ( 32 ), and deep learning methods using interface structures ( 33 ).

In our previous work, we developed a model selection method for protein docking, DOVE ( 33 ), which uses Convolutional deep Neural Network (CNN) as the core of its architecture. DOVE captures atoms and interaction energies of atoms located at the interface of a docking model using a cube of 20 3 or 40 3 Å 3 and judges if the model is correct or incorrect according to the CAPRI criteria ( 34 ). We showed that DOVE performed better than existing methods. However, DOVE has a critical limitation - since it captures an interface with a fixed-size cube, only a part of the interface is captured when the interface region is too large. This often caused an erroneous prediction. In addition, a 3D grid representation of an interface often includes voxels of void space where no atoms exist inside, which is not efficient in memory usage and may even be detrimental for accurate prediction. In this work, we address this limitation of DOVE by applying a graph neural network (GNN)( 35 , 36 ), which has previously been successful in representing molecular properties ( 37 - 40 ). Using GNN allows the capturing of all interface atoms in a more flexible and natural fashion. To the best of our knowledge, this is the first method that applies GNNs to the protein docking problem. Compared to DOVE and other existing methods, GNN-DOVE demonstrated substantial improvement in a benchmark study.


## 2 Materials and methods

We first introduce the datasets used for training and testing GNN-DOVE. Subsequently, we introduce the graph neural network architecture and the training process of GNN-DOVE.


## 2.1 Dataset

To train and test GNN-DOVE, we used the Dockground dataset ( 41 ). The dataset includes 58 target complexes, each with on average 9.83 correct and 98.5 incorrect decoys. Correct decoys were identified by applying the CAPRI criteria ( 27 ), which considers interface root mean square deviation (iRMSD), ligand RMSD (lRMSD), and the fraction of native contacts (fnat). The iRMSD is the Cα RMSD of interface residues with respect to the native structure. Interface residues in a complex are defined as all the residues within 10.0 Å from any residues of the other subunit. lRMSD is the Cα RMSD of ligands when receptors are superimposed, and fnat is the fraction of contacting residue pairs, i.e. residue pairs with any heavy atom pairs within 5.0 Å, that exist in the native structure.

To remove redundancy, we grouped the 58 complexes using the TM-Score ( 42 ). Two complexes were assigned to the same group if at least one pair of proteins from the two complexes had a TM-score of over 0.5 and sequence identity of 30% or higher. This resulted in 29 groups ( Table 1 ). In Table 1 , complexes (PDB IDs) of the same group are shown in lower case in a parenthesis followed by the PDB ID of the representative. These groups were split into four subgroups to perform four-fold cross-testing, where three subsets were used for the training while one subset was used for testing. Thus, by cross-testing, we have four models tested on four fully independent testing sets. Among the training set, we used 80% of decoys for training a model and the remaining 20% as a validation set, which was used to determine the best hyper-parameter set for training. In the results, the accuracy of targets when treated in the testing set was reported. To have a fair comparison with DOVE ( 33 ), DOVE was also trained and tested using this protocol.


## 2.2 The GNN-DOVE algorithm

In this section, we describe GNN-DOVE, which uses the graph neural network. The GNN-DOVE algorithm is inspired by a recent work in drug-target interactions ( 38 ), which designed two graph-representation for capturing intermolecular interactions for protein-ligand interactions. We will first explain how the 3D structural information of a protein-complex interface is embedded as a graph. Then, we describe how we used a graph attention mechanism to focus on the intermolecular interaction between a receptor and a ligand protein. The overall protocol is illustrated in Figure 1 . For an input protein docking decoy, the interface region is identified as a set of residues located within 10.0 Å of any residues of the other protein. A residue-residue distance is defined as the shortest distance among any heavy atom pairs across the two residues. Using the extracted interface region, two graphs are built representing two types of interactions: the graph G 1 describes heavy atoms at the interface region, which only considers the covalent bonds between atoms of interface residues within each subunit as edges. Another graph G 2 connects both covalent (thus includes G 1 and non-covalent residue interaction as edges, where a non-covalent atom pair is defined as those which are closer than 10.0 Å from each other. Both graphs will be processed by graph neural network (GNN) to output a score, which is a probability that the docking decoy has a CAPRI acceptable quality (thus making higher scores better).

A key feature of this work is the graph representation of an interface region of a complex model. Graph G is defined by G = (V, E, A) , where V denotes the node set, E is a set of edges, and A is the adjacency matrix, which numerically represents the connectivity of the graph. For a graph G with N nodes, the adjacency matrix A has a dimension of N*N , where A ij > 0 if the i- th node and the j- th node are connected and A ij = 0 otherwise. The adjacency matrix A 1 for graph G 1 describes covalent bonds at the interface, and thus defined as follows:

The matrix A 2 for G 2 describes both covalent bonds and non-covalent interactions between atoms within 10.0 Å to each other. It is defined as follows: where d ij denotes the distance between the i- th and the j- th atoms. μ and σ are learnable parameters, whose initial value is 0.0 and 1.0. The formula decays as the distance increases between atoms.

Compared to the previous voxel representation used in DOVE, the graph representation encodes the distance information more flexibly and naturally. Note that the representation is rotationally invariant. Also, memory usage is more efficient as void spaces are not represented as is needed for the voxel representation.

As for the node features in the graph, we considered the physicochemical properties of atoms. We used the same features as used in previous works ( 38 , 43 ) as shown in Table 2 .

The constructed graphs are used as the input to the GNN. More formally, graphs are the adjacency matrix A 1 and A 2 , and the node features, with x ∈ ℝ F , where F is the dimension of the node feature.

We first explain the attention mechanism of GNN. With the input graph of x i , the pure graph attention coefficient is defined in Eq. (3) , which denotes the relative importance between the i- th and the j- th node: where and is the transformed feature representation defined by and . W, E ∈ ℝ F × F are learnable matrices in GNN. e ij and e ji become identical to satisfy the symmetrical property of the graph by adding and . The coefficient will only be computed for i and j where A ij > 0.

Attention coefficients will be also computed for elements in the adjacency matrices. They are formulated in the following form for the element ( i, j ): where a ij is the normalized attention coefficient for the i- th and the j- th node pair, e ij is the symmetrical graph attention coefficient computed in Eq. (3) , N i is the set of neighbors of the i- th node that includes interacting nodes j where A ij > 0.

Based on the attention mechanism, the new node feature of each node is updated by considering its neighboring nodes, which is a linear combination of the neighboring node features with the final attention coefficient a ij :

Furthermore, the gate mechanism is further applied to update the node feature since it is known to significantly boost the performance of GNN. The basic idea is similar to that of ResNet ( 44 ), where the residual connection from the input helps to avoid information loss, alleviating the gradient collapse problem of the conventional backpropagation. The gated graph attention can be viewed as a linear combination of and , as defined in Eq. (6) : where , where D ∈ ℝ 2 F is a weight vector that is multiplied (dot product) with the vector and b is a constant value. Both D and b are learnable parameters and share among different nodes. denote the concatenation vector of x i and .

We refer the Attention and Gate-Augmented Mechanism as a layer, the gate augmented graph attention layer (GAT). Then, we can simply denote . The node embedding can be iteratively updated by GAT , which aggregates information from neighboring nodes.

Using the GAT mechanism described before, we adopted four layers of GAT in GNN-DOVE to process the node embedding information from neighbors and to output the updated node embedding ( Figure 1B ). For the two adjacency matrices A 1 and A 2 , we used the shared (i.e. the same) GAT. The initial input of the network is atom features. With two matrices, A 1 and A 2 , we have x 1 = GAT(x in , A 1 ) and x 2 = GAT(x in , A 2 ) . To focus only on the intermolecular interactions within an input protein complex model, we subtracted the embedding of the two graphs as the final node embedding. By subtracting the updated embedding x 1 from x 2 , we can capture the aggregation information that only comes from the intermolecular interactions with other nodes in the protein complex model. Thus, the output node feature is defined as:

Then, the updated x out will become x in to iteratively augmented the information through three following GAT layers. After the node embeddings were updated by the four GAT layers, the node embedding of the whole graph was summed up as the entire graph representation, which is considered as the overall intermolecular interaction representation of the protein complex model:

Finally, fully connected (FC) layers were applied to x graph to classify whether the protein-complex model is correct or incorrect. In total, four FC layers were applied. RELU activation functions were used between the FC layers, and a sigmoid function was applied for the last layer to output a probability value.

The source code of GNN-DOVE is available at https://github.com/kiharalab/GNN_DOVE .


## 2.3 Training nets

Since the dataset was highly imbalanced with more incorrect decoys than acceptable ones, we balanced the training data by sampling the same number of acceptable and incorrect decoys in each batch for training.

The dimension of the graph attention layer (GAT) is 140, while the fully connected layer (FC) is 128. For training, cross-entropy loss ( 45 ) was used as the loss function optimize the GNN. The Adam optimizer ( 46 ) with a learning rate of 0.002 was used. Each model of different folds was trained for 100 epochs with a batch size of 32. To avoid overfitting, a dropout ( 47 ) of 0.3 was applied for every layer except the last FC layer. Weights of every layer were initialized using the Glorot-uniform ( 48 ) to have a zero-centered Gaussian distribution, and bias was initialized to 0 for all layers. For different fold training, we adopted the same hyper-parameters. The training process generally converged after approximately 30 epochs.


## 2.4 DOVE

We compared the performance of GNN-DOVE with its predecessor, DOVE. Here we briefly describe the DOVE algorithm. DOVE is a CNN-based method for evaluating protein docking models. It first extracts the interface region of an input protein complex model, and the region is put into a 40*40*40 Å 3 cube as input. A seven-layer CNN, which consists of three convolutional layers, two pooling layers, and two fully connected layers, was adopted to process the voxel input. The output of DOVE is the probability that indicates whether the input model is acceptable or not. For input features, DOVE took atom types as well as atom-based interaction energy values from GOAP ( 49 ) and ITScore ( 29 ). Since voxelized structure input is not rotation invariant, DOVE needed to augment training data by rotations.


## 3 Results


## 3.1 Performance on the Dockground dataset

We evaluated the performance of GNN-DOVE on the Dockground dataset. GNN-DOVE was compared with DOVE and five other existing structure model scoring methods, GOAP ( 49 ), ITScore ( 29 ), ZRANK ( 50 ), ZRANK2 ( 51 ), and IRAD ( 52 ). The test set results were reported for GNN-DOVE and DOVE. Both GOAP and ITScore were run in two different ways. First, as originally designed, the entire complex structure model was input. The other way was to input only the interface residues that are within 10 Å from the interacting protein (denoted as GOAP-Interface, ITScore-Interface). Thus, GNN-DOVE was compared with a total of eight methods. As for DOVE, we used DOVE with a cube size of 40 3 Å 3 and heavy atom distribution as input feature because this setting performed the best among other settings tested on the Dockground dataset in the original paper ( 53 ) ( Figure 4 in the paper, the setting was named as DOVE-Atom40). For this work, DOVE was newly retrained using the same four-fold cross-testing as GNN-DOVE.

Figure 2 shows the hit rate of GNN-DOVE in comparison with the other methods. A hit rate of a method is the fraction of target complexes where the method ranked at least one acceptable model based on the CAPRI criteria within each top rank. In Figure 2 , we show two panels. Panel A shows the fraction of targets where a method had at least one hit among each rank cutoff, while in Panel B, the hit rates for a method were averaged first within each of the 29 groups then re-averaged over the groups.

It is clear from Figure 2 that GNN-DOVE (dotted line in light green) performed better than the other methods. GNN-DOVE was able to rank correct models within earlier ranks in many target complexes. Within the top 10 rank, GNN-DOVE achieved a hit rate of 89.7% while the next best method, DOVE, achieved 81.0% and the third best method, GOAP, obtained 70.7% ( Figure 2A ). When we further compared the hit rates considering the target groups ( Figure 2B ), GNN-DOVE consistently outperformed other methods. The gap between GNN-DOVE and DOVE against the other existing methods also increased. Among the other seven existing methods, GOAP showed the highest hit rate at 5 th ranks followed by Zrank2 in both panels while ITScore-Interface had the lowest hit rates on this dataset.

In Figure 3 , we compared iRMSD, lRMSD, and fnat values of the methods. These metrics are used for defining the quality levels in CAPRI. The best value among the top 10 ranked decoys was plotted. For the majority of the cases (49 out of the 58 targets) GNN-DOVE selected a decoy within an iRMSD of 4 Å (one of the criteria for the acceptable quality level in CAPRI). This is in sharp contrast with the other methods ( Figure 3A ), where the iRMSD of many targets they selected was larger (worse) than GNN-DOVE. In terms of iRMSD, the second best method was DOVE, where 44 targets were within an iRMSD of 4 Å. A similar situation was observed for lRMSD. GNN-DOVE selected a decoy within a lRMSD of 10 Å (one of the criteria for the acceptable quality level in CAPRI) for 50 targets, while the second-best method, DOVE, selected 45 targets within 10 Å lRMSD. In terms of fnat (larger being more accurate), GNN-DOVE only missed 5 targets in selecting at least one model with an fnat over 0.1 (one of the criteria for acceptable quality level in CAPRI). The plot shows that GNN-DOVE had a larger fnat value than the other existing methods for most of the targets, as indicated by many data points below the diagonal line.

Figure 3B compares GNN-DOVE against DOVE. In terms of iRMSD, lRMSD, and fnat, GNN-DOVE outperformed DOVE for 26 (22 ties), 27 (20 ties), and 27 (17 ties), respectively. Overall, GNN-DOVE outperforms the eight existing methods for all the three metrics.


## 3.2 T-SNE analysis

To illustrate how GNN-DOVE classified decoys, we used t-SNE ( 54 ) to visualize GNN-DOVE’s encoding of decoys in Figure 4 . t-SNE is a dimension reduction method to visualize similarities of high-dimensional data points. Since we employed a four-fold cross-testing, a plot was provided for each of the four testing sets. In all the plots, particularly in Fold 3 and Fold 4, most of the acceptable decoys (black circles) were distinguished from incorrect ones (gray crosses), which indicates a good representation and generalization ability of the graph neural networks for this problem.


## 3.3 Examples of decoys for comparison with DOVE

We mentioned above that a limitation of DOVE is that its usage of a fix-sized cube of 40 3 Å 3 , which cannot capture the entire interface region if the interface is too large to fit in the cube. Here we show two examples of such cases, which led to a misclassification by DOVE but correctly classification by GNN-DOVE. In Figure 5 , the interface region of a decoy is shown in blue and green, and the atoms that did not fit in the cube are shown in a sphere representation in red.

The first example ( Fig. 5A ) shows a decoy of a protein complex of plasminogen and staphylokinase (PDB ID: 1bui), which has an acceptable quality by the CAPRI criteria. For this decoy, 59 atoms (in red) out of 1022 atoms at the interface were not included in the cube. Because of this, it was ranked the 65 th out of 110 decoys by DOVE, while it was ranked 15 th by GNN-DOVE. For this target, GNN-DOVE ranked five hits within the top 10 scoring decoys and eight hits within the top 20. In contrast, DOVE could not rank any hit within the top 20. The first hit by DOVE was found at the 35 th rank.

The second example ( Fig. 5B ) is an acceptable model for the nitrogenase complex (PDB ID: 1g20). As shown, many interface atoms, 497 out of 1843, were outside the cube. DOVE ranked this decoy 28 th , while GNN-DOVE ranked this decoy 10 th . DOVE had 0 hits within the top 10 and had only one hit within top 20. On the other hand, GNN-DOVE was very successful for this target, where all the top 10 selections were correct models.


## 4 Discussion

In this work, we developed GNN-DOVE for protein docking decoy selection, which used a Graph Neural Network (GNN). We used the gated augmented attention mechanism to capture the atom interaction pattern at the interface region of protein docking models. The benchmark on the Dockground dataset demonstrated that GNN-DOVE outperformed DOVE, along with other existing scoring functions compared.

To assess the quality of structure models, considering multi-body (atom or residue) interactions ( 55 - 58 ) have been proven to be an effective approach. GNNs consider patterns of multi-atom interactions by representing the interactions as a graph structure. Since a graph is a natural representation of molecular structures, GNNs may be applied in various problems in structural bioinformatics and cheminformatics.

The performance of GNN-DOVE likely would be improved by considering other physicochemical properties of atoms such as atom-wise binding energies, as well as sequence conservation of residues that can be computed from a multiple sequence alignment of homologous proteins. Application to multi-chain complexes remains a potential path for future work.


## Authors Contributions

XW and STF conceived the initial version of the study. XW and DK designed this work in the current form. XW developed the codes in communication with STF. XW performed the computation and XW and DK analyzed the results. XW wrote the initial draft of the manuscript and DK critically edited it. All authors have read and approved the manuscript.


## Acknowledgements

The authors are grateful to Jacob Verburgt for proofreading the manuscript and Sai Raghavendra Maddhuri Venkata Subramaniya and Aashish Jain for testing the GNN-DOVE code on GitHub. This work was partly supported by the National Institutes of Health (R01GM133840, R01GM123055), and the National Science Foundation (DMS1614777, CMMI1825941, MCB1925643, DBI2003635).


## Reference