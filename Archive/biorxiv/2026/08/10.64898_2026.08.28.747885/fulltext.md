## Abstract

Proteins are dynamic molecules existing in diverse conformational states underlying their biological functions. Although recent approaches have enabled diverse conformational sampling by emulating molecular dynamics simulations, perturbing evolutionary information, or steering internal mechanisms of structure prediction models, predicting conformations resulting from major domain motions or motions that occur over long timescales still remains a challenge. To this end, we introduce GNMCADS, a conformational sampling strategy that enhances the diversity of protein diffusion models by selectively annealing the conditioning signal guided by the intrinsic dynamical organization of the sampled protein. Further, we implement GNMCADS in the diffusion module of AlphaFold3, enabling the generation of diverse protein conformations. When benchmarked across 92 proteins that include 54 class A GPCRs, 15 transporters, and 23 proteins with major domain movements, GNMCADS exhibits improved sampling diversity compared to other current conformational sampling methods.


## 1 Introduction

Proteins are the essential machines that regulate and execute cellular activities. With the recent advent of deep learning methods such as AlphaFold2 [ 1 ], and its successor AlphaFold3 (AF3) [ 2 ], it has become possible to generate the three-dimensional structure of a protein from its sequence. However, proteins are inherently dynamic molecules adopting multiple conformational states which dictate their biological functions. Hence, the characterization of the conformation landscapes of proteins is crucial for understanding their biological functions [ 3 ].

Recent machine-learning based approaches aiming to tackle the problem of conformational sampling from sequence and evolutionary information alone can be classified into three main categories. The first category includes methods trained or fine-tuned using molecular dynamics (MD) simulations to learn to sample protein conformations from their underlying free energy landscapes [ 4 – 7 ]. However, the prohibitive cost of MD simulations limits the availability of training data that capture conformational changes occurring in large protein complexes or over long timescales. Consequently, these methods may have difficulty sampling biologically relevant conformational changes that are underrepresented in their training data. In contrast to methods in the first category, methods in the second and third categories do not require training with MD simulations and increase the conformational sampling diversity of already trained protein structure prediction models such as AlphaFold. Methods in the second category accomplish this by modifying the multiple sequence alignments (MSAs) used as the source of coevolutionary information by structure prediction models. Specifically, they generate an ensemble of structures by altering the coevolutionary information provided to the structure prediction models by subsampling MSAs while varying the number of aligned sequences [ 8 ], clustering aligned sequences by their sequence similarity, and generating new MSAs from these clusters [ 9 ], or performing column-wise MSA modifications [ 10 – 12 ]. Whereas the second category increases diversity by manipulating the inputs of the prediction models, the third category achieves diversity by internal interventions in the prediction models by steering latent representations [ 13 ] or guiding the diffusion sampling process [ 14 ]. Compared to increasing sampling diversity by MSA perturbations, operating on internal model representations allows these methods to avoid relying directly on the availability of evolutionary information in terms of MSA depth or heterogeneity which is advantageous for proteins with low evolutionary information such as de novo designed proteins.

In this study, we introduce GNMCADS, a diffusion sampler that enhances the conformational sampling diversity of protein diffusion models by annealing the pairwise conditioning signal in a selective manner based on the intrinsic dynamical organization of sampled proteins ( Fig. 1a ). Although condition annealed sampling has been successfully used to increase the diversity of image diffusion models by adding a progressively decreasing amount of noise to the conditioning signal during the denoising process [ 15 ], the addition of noise directly to the conditioning signal of protein diffusion models can substantially disrupt the quality and accuracy of the generated structures as will be illustrated below. To this end, GNMCADS anneals the diffusion conditioning signal selectively by taking the intrinsic dynamical properties of the sampled protein into account. Specifically, this is achieved by generating a reference structure using default sampling, and leveraging the Gaussian Network Model’s (GNM) ability to predict the equilibrium fluctuations and identify large-scale biologically functional collective motions that are intrinsically embedded in the sampled reference structure [ 16 – 19 ]. Subsequently, GNMCADS divides the given protein into distinct “dynamical domains” based on the cross-correlations of residue fluctuations inferred from GNM such that the residues in a dynamical domain tend to exhibit correlated motions whereas the residues in different dynamical domains tend to exhibit anti-correlated movements. Finally, the calculated dynamical domains are used to guide the annealing process with the addition of noise specifically to the inter-dynamical domain and non-diagonal elements of the pairwise conditioning signal.

Further, we present AF3 GNMCADS, an implementation of GNMCADS in the diffusion module of AlphaFold3 and benchmark its conformational sampling capabilities over three datasets that consist of 92 proteins across 54 class A GPCRs, 15 transporters and 23 proteins with major conformational changes. We compare AF3 GNMCADS sampling against AlphaFold3’s default sampling; Boltz2 in its MD emulation mode [ 6 ] and BioEmu [ 4 ], both of which are methods trained on MD simulations; AFSample2 [ 11 ] and AFSample3 [ 11 ], which perform column-wise MSA randomizations in AlphaFold2 and AlphaFold3 respectively; and ConforMix [ 14 ] which employs RMSD-based bias potentials during the diffusion process.


## 2 Results


## 2.1 AF3 GNMCADS captures biologically relevant conformations

For increased diversity in protein generative models to be useful, the generated structures must represent distinct biologically relevant conformations of the sampled protein. We assess AF3 GNMCADS’ ability to generate such conformations by projecting the generated structures of calmodulin, adenylate kinase, AT1aR GPCR, and AtSWEET13 transporter onto their respective MD simulation derived free-energy landscapes parameterized by the collective variables that are crucial for their biological functions ( Fig. 1b-e ) [ 20 – 23 ]. Across all four proteins, AF3 GNMCADS samples a broader range of biologically relevant conformational states and more thoroughly populates their respective free-energy landscapes compared to AF3.

Notably, AF3 GNMCADS captures extended, compact, and intermediate conformations of calmodulin; closed, open, and PCS–CPMG NMR-derived [ 24 ] high energy conformations of adenylate kinase; open, intermediate, and closed conformations of AT1aR GPCR; and inward-facing, occluded, and outward-facing conformations of AtSWEET13 transporter. Moreover, AF3 GNMCADS sampled structures populate regions of the free-energy landscapes that span between these conformational states, indicating that AF3 GNMCADS also captures intermediate conformations along functionally relevant transitions.


## 2.2 AF3 GNMCADS recovers diverse conformations along GPCR activation

We evaluated the ability of AF3 GNMCADS to capture long-timescale conformational transitions by benchmarking it against AF3 and other conformational sampling methods across 54 class A GPCRs, as the conformational state transitions of GPCRs occur on multi-microsecond timescales [ 26 ]. Subsequently, we categorized the conformational states of the sampled structures according to their TM2 to TM6 helix distance, a collective variable that represents the opening of the internal cavity during activation of a GPCR [ 25 , 26 ] (see Section 4.4 ).

Across the 54,000 GPCR structures sampled with each method, AF3 GNMCADS substantially broadens per-GPCR TM2-TM6 distance ranges by generating an increased number of structures in open and intermediate conformations than AF3, which predominantly generates GPCR structures in closed conformations. Specifically, 81.1% of the AF3 sampled GPCR structures were classified as closed, whereas only 15.1% and 3.8% were classified as intermediate and open conformations, respectively. In contrast, AF3 GNMCADS captures considerably more diverse GPCR conformations than AF3, with 53.9%, 31.0%, and 15.1% of the sampled structures being classified as closed, intermediate, and open conformational states, respectively. Furthermore, when compared against other benchmarked conformational sampling methods, AF3 GNMCADS also samples the largest number of GPCRs in their intermediate conformations.


## 2.3 Benchmarking AF3 GNMCADS against other conformational sampling methods

Next, we benchmarked AF3 GNMCADS against AF3 and other conformational sampling methods on the open-closed [ 11 ] and transporter [ 29 ] datasets, comprising 23 proteins with major domain motions and 15 transporters with inward-facing and outward-facing structures, respectively ( Fig. 3 ). Because both datasets were originally curated to include only single-chain targets, they were expanded to preserve the obligate multimeric complexes for model evaluation. Further details on the preparation of the datasets can be found in Sections A.3 and A.4 . The diversity of the sampled structures was quantified by the unweighted fill ratio calculated as shown in Section 4.5 , which measures the sampling contiguity by leveraging TM similarity scores between the predicted and experimentally determined structures [ 11 , 30 ]. Across the 38 targets across both datasets, AF3 GNMCADS achieved considerably higher fill ratio scores than AF3. Similarly, AF3 GNMCADS improved the fill ratio by more than 5% for the majority of targets across all other conformation sampling methods.


## 3 Discussion

Protein structure models can accurately generate protein structures from their sequences, yet they remain limited in capturing their conformational variability. GNMCADS addressed this by incorporating a physically motivated description of intrinsic collective dynamics into the diffusion sampling process by selectively relaxing pairwise constraints between GNM-identified dynamical domains while preserving internal coupling via condition annealing. This targeted strategy enhances sampling along collective structural rearrangements.

When evaluated against molecular dynamics (MD) derived free-energy landscapes of calmodulin, adeny-late kinase, AT1aR GPCR, and AtSWEET13 transporter, AF3 GNMCADS, the AlphaFold3 implementation of GNMCADS, achieves substantially broader coverage along the functionally relevant regions of their respective free-energy landscapes and generates a greater number of distinct biologically relevant conformational states compared to AlphaFold3. The increased sampling of intermediate states is particularly notable, as biologically relevant conformational transitions often involve coordinated rearrangements between partially populated states. The GPCR analysis further illustrates this effect: AF3 strongly favored closed conformations, whereas sampling with GNMCADS substantially increased the representation of intermediate and open states and sampled intermediate conformations across more receptors.

Moreover, when benchmarked across 92 targets including class A GPCRs, transporters, and proteins that undergo major domain movements, AF3 GNMCADS achieves state-of-the-art conformational sampling performance compared to other conformational sampling methods based on multiple sequence alignment (MSA) modification, MD emulation, and twisted diffusion sampling. The consistent improvement across these distinct approaches suggests the value of selectively relaxing structural constraints according to the intrinsic dynamical organization of each protein.

Together, these results demonstrate that the incorporation of intrinsic dynamic properties of proteins into the diffusion sampling via GNMCADS provides an effective way towards enhancing the conformational sampling diversity of protein diffusion models.


## 4 Methods


## 4.1 Determination of dynamical domains by GNM

The Gaussian Network Model (GNM) is a minimalist physics-based coarse-grained normal mode model that describes the equilibrium dynamics of proteins [ 16 , 17 ]. In GNM, a protein structure is represented as an elastic network in which C α atoms that lie within a cutoff distance are connected by uniform harmonic springs. Under the assumption of Gaussian-distributed fluctuations, this representation enables the characterization of equilibrium motions within a statistical thermodynamics framework, where collective residue fluctuations are decomposed into intrinsic normal modes of the network. This formulation enables the equilibrium cross-correlations of fluctuations between residues i and j to be expressed as: where R i is the position vector of the i th residue’s C α atom, k B is the Boltzmann constant, T is the absolute temperature, γ is the force constant, and Γ is the Kirchhoff matrix representing the connectivity of the protein such that where R ij is the distance between the C α atoms of the residues i and j .

The pseudo-inverse of Γ can be represented by the sum of the N − 1 non-zero modes 2 ≤ k ≤ N using where λ k and u k are the eigenpairs of Γ . The first mode k = 1 is the trivial mode with λ 1 = 0 and is omitted.

Since ⟨Δ R i · Δ R j ⟩ is directly proportional to , the cross-correlation of the equilibrium fluctuations between the residues i and j for the mode k can be calculated as:

Using the per mode cross-correlations, a given protein can be divided into two dynamical domains where the residue pairs within the same dynamical domain tend to exhibit correlated motions and have positive cross-correlation values, whereas the residue pairs belonging to the opposing dynamical domains tend to exhibit anti-correlated motions and have negative cross-correlation values.


## 4.2 GNMCADS

GNMCADS employs two masks to perform selective annealing. The first mask, M diag , is used to limit the annealing of the diagonal entries along with the first k diag th superdiagonal and subdiagonal entries of the pairwise conditioning signal as it has been shown that the perturbations of the diagonal entries of the pairwise conditioning signal can have substantial effects on the secondary structure of the generated proteins [ 31 ]. The M diag mask is defined as:

The second mask used by GNMCADS, M GNM , enables the annealing process to become aware of the intrinsic dynamics of the sampled protein. This is achieved by performing the annealing process only for the entries of the pairwise conditioning signal that contain inter dynamical domain information. As the residues in the opposing dynamical domains tend to have anti-correlated motions, annealing of the entries that belong to the inter dynamical domain region of the pairwise conditioning signal allows GNMCADS to sample diverse conformations that are compatible with the sampled protein’s underlying intrinsic dynamical behaviours. The M GNM mask for the GNM mode k is defined as:

These two masks are then combined as a single mask such that:

Low-frequency GNM modes encode the collective functional motions and many experimentally observed conformational transitions can thus be well described by the lowest frequency GNM modes [ 32 – 34 ]. Accordingly, for each diffusion step t , the value of k t , which is the GNM mode that will be used to define dynamical domains and consequently the mask that will be used is selected from a distribution that favors low-frequency modes such that:

Subsequently, the newly selected GNM mode k t is then used to anneal the pairwise conditioning signal where N c is the channel dimension of the pairwise conditioning signal. However, unlike CADS, GNMCADS also scales the noise values n ijc ~ N (0, 1) with the mean and standard deviation of each channel’s selected elements. The complete annealing step of GNMCADS can be shown as: where s is the noise scale, µ c and σ c are the mean and the standard deviation of the elements selected by in the c th channel of the pairwise conditioning signal, and γ ( t ) is the linear annealing schedule defined as: where the values of τ 1 , τ 2 ∈ (0, 1) are the thresholds of the linear annealing schedule.


## 4.3 Inference protocols

Each benchmarked method was used to generate 1000 structures for each target. AF3 predicted structures were generated by rerunning the model with 200 seeds and producing 5 diffusion samples per seed. In contrast, AF3 GNMCADS predicted structures were generated using one seed with 1000 diffusion samples per seed.

AFSample2, AFSample3, and BioEmu were used as described in their original studies. For ConforMix, 1000 structures were generated instead of the 800 structures recommended by its authors. Similarly, the Boltz (MD) method was used to generate 1000 structures by using 200 seeds with 5 diffusion samples per seed.


## 4.4 GPCR state determination

Conformational states of the predicted GPCR structures were determined using the TM2-TM6 distance thresholds proposed by [ 26 ] which are calculated as the distances between the 2 × 46 and 6 × 37 residues in the GPCRdb numbering scheme [ 25 ]. The TM2-TM6 distance thresholds of 13.6 Å and 16.36 Å were used for the intermediate and open conformations, respectively; structures with TM2-TM6 distances less than 13.6 Å are classified as closed structures.

Predicted structures with a 7TM RMSD (excluding the extracellular and intracellular loops) greater than 7 Å relative to both the G protein bound and inactive experimentally determined structures were classified as failed predictions.


## 4.5 Fill ratio

The fill ratio metric, introduced in [ 11 ], assesses the protein generative models based on their ability to sample contiguous transitions between two known conformations of a protein using the TM similarity scores [ 30 ]. As the benchmarked protein targets in this study include multimer targets, US-align was used to calculate the TM scores [ 35 ]. The implementation of fill ratio in [ 11 ] uses a fixed TM normalization scale of d 0 = 3.5Å. However, the usage of a fixed d 0 has been shown to create a dependence between the sequence length and the similarity score [ 30 ]. Therefore, the TM scores were calculated without fixing the d 0 ; instead, the optimal d 0 value is calculated by the alignment algorithm depending on the sequence length of the reference structure as suggested by [ 30 ]. Additionally, the weighting of fill ratio which generates a bias towards the end states was omitted to more clearly assess the conformational sampling of intermediate structures.


## Code availability

The source code for AF3 GNMCADS is available at github.com/ahmedselim2017/af3_gnmcads .


## A Datasets


## A.1 Free energy landscapes

The free energy landscapes used in this study and their references are shown in Table S1.


## A.2 GPCR dataset

The GPCR dataset was created by applying the following filters to the GPCRdb database [ 25 ]:

The GPCR must be a class A GPCR.

Both the G protein bound and inactive states of the GPCR must be available.

The inactive state must have a GPCRdb defined activation degree of 10% or less.

The GPCR structures must have a resolution of 9 Å or better.

For GPCRs with multiple active or inactive states after the filtering, the structure with the highest sequence similarity to the canonical sequence was selected. Structure predictions were performed using the canonical 7TM (TM1-H8) sequences including the extracellular and the intracellular loops defined by GPCRdb.


## A.3 Open-closed dataset

The open-closed dataset introduced by [ 11 ] contains proteins that undergo large-scale domain motions. Because the target Q53W80 exists in both monomer and homodimer conformations, its homodimer form has also been included in the dataset. As the target B7IE18 is also included in the transporters dataset, it has been removed from the open-closed dataset. The PDB identifiers for the targets in the dataset can be seen in Table S3.


## A.4 Transporters dataset

The transporters dataset introduced in [ 29 ] contains transporters with experimentally determined inward-facing (IF) and outward-facing (OF) conformations. Although the given dataset uses single chains for each target, for the transporters that form obligate complexes, their complete oligomeric sequences were used to perform predictions.

For the proposed IF and OF conformations of the melB transporter, both the 7L17 and 4M64 structures are classified as OF by the studies that initially reported these structures [ 36 , 37 ] . Hence, the 8T60 cryoEM structure with the inward-facing conformation [ 38 ] has been used with the originally proposed 7L17 outward-facing conformational state.

Similarly, the proposed IF and OF structures for the target AAC3 correspond to different proteins from different organisms where the IF structure is the ADP/ATP translocase protein of Thermothelomyces thermophilus and the OF structure is the ADP/ATP translocase 3 protein of Saccharomyces cerevisiae . Therefore, this target has been replaced with the plastid/parasite ATP/ADP translocator for which both the IF and OF conformations have recently been experimentally determined [ 39 ]. The final list of targets and their PDB identifiers can be seen in Table S4.


## B TM similarity plots


## Acknowledgments

We would like to thank Sergey Ovchinnikov and Ezgi Karaca for their valuable discussions.

The numerical calculations reported in this paper were partially performed using the EuroHPC Joint Undertaking (EuroHPC JU) supercomputer MareNostrum 5, hosted by the Barcelona Supercomputing Center (BSC). Access to MareNostrum 5 was provided through a national access call coordinated by the Scientific and Technological Research Council of Turkiye (TUBITAK). We gratefully acknowledge BSC, TUBITAK, and the EuroHPC JU for providing access to these resources and supporting this research. This work was supported by the Bogazici University BAP Research Fund 25A05P4.


## Funder Information Declared