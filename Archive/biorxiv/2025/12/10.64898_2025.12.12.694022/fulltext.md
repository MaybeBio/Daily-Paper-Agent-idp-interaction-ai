## Abstract

Biomolecular condensates underpin the spatial and temporal organization of cellular biochemistry in the cell. Their architectures often arises from complex, multicomponent mixtures whose behavior is governed by weak, multivalent interactions, frequently mediated by intrinsically disordered regions (IDRs) of proteins. However, current approaches lack generalizable metrics to determine whether IDRs will mix or segregate within condensates. Here, we show that our domain decomposition method can both accurately determine concentrations in the dense/dilute phases, and provide a continuous metric for characterizing IDR mixing in molecular dynamics simulations. Applying this methodology to 1,963 binary mixtures, we find that mixing at equimolar ratios is rare. Most condensate-forming pairs favoring one dominant scaffold and minority client molecules. We found that hydrophobic IDRs mix promiscuously with most sequences, while the mixing of charged sequences is sensitive to the charge and complementarity of the partner. When applied to experimental protein interaction networks, our simulations successfully distinguish IDR-mediated partitioning from those requiring additional factors such as RNA or site specific binding. Our results provide a foundation for determining condensate composition in complex cellular environments and for designing synthetic IDRs that can infiltrate or modulate biomolecular condensates.


## I. I ntroduction

Biomolecular condensates allow cells to organize biomolecules without enclosing them in a lipid membrane. The intrinsically disordered regions (IDRs) of proteins can drive the formation of these membraneless organelles, resulting in local enrichment of specific proteins, nucleic acids, and other species[ 1 ]. The resulting condensates can then exchange material with their surroundings, enabling their composition to be rapidly modulated by temperature, pH, and the surrounding concentration of molecular components.[ 2 ], [ 3 ].

Theoretical work has demonstrated that when condensates share components, the number of distinct, coexisting condensates can grow super-linearly with the number of molecular species[ 4 ], [ 5 ]. For instance, a system with 200 distinct proteins could theoretically give rise to 250 unique condensate compositions. The flexible nature of IDRs can create a dense network of contacts between copies of the same protein, or other species[ 6 ], [ 7 ]. While some IDRs can form condensates without other proteins present, these same IDRs may be distributed throughout other condensates in the cell[ 8 ], [ 9 ]. Of the human proteome’s 20,000+ proteins, between 50-75% contain IDRs, making the combinatorial space of potential partners staggeringly vast[ 10 ], [ 11 ]. Consequently, a single disease-associated mutation could subtly alter a protein’s interaction preferences, causing it to incorrectly partition into a new condensate or disrupt the composition of its native one. These effects have been increasingly identified as a molecular hallmark of numerous human diseases, including neuro-degenerative disorders and cancers[ 12 ] –[ 17 ]

Assessing these IDR networks experimentally can be challenging. The protein buffer, fluourescent tags, or the concentration and type of molecular crowder, can all influence the interaction between two IDRs[ 18 ], [ 19 ]. Computational approaches offer a way to simulate IDR interactions when no other molecules are present[ 20 ]. Despite their simplified nature, coarse-grained molecular dynamics forcefields have excelled at reproducing individual IDR characteristics, like radius of gyration, but also bulk condensate properties such as the saturation concentration and viscosity[ 10 ], [ 21 ]–[ 25 ].

Unfortunately, current approaches to quantify IDR mixing have been designed for specific studies, and thus have limitations in sequence length, maximum number of phases, or concentration ratio of the mixture[ 26 ]–[ 29 ] We are missing a generalizable method that can characterize the spatial organization of components—whether they mix homogeneously, form distinct domains, or fully segregate into separate condensates. Understanding the interaction network between IDRs could lead towards the development of small molecules or synthetic peptides that dissolve aberrant condensates, or stabilize essential ones[ 30 ], [ 31 ].

In this manuscript, we present a methodology for both calculating an IDR’s propensity for phase separation and quantifying IDR mixing from direct coexistence simulations. Our method is designed to be simple and uniform, eliminating user-defined choices of surface thicknesses or phase boundaries. We accomplish this by adapting a method developed for characterizing liquid-liquid phase transitions in simple Lennard-Jones fluids, and extending them to the more complex case of multi-component biomolecular condensates[ 32 ], [ 33 ]. Our methodology is tested against a chemically diverse set of IDRs, and allows us to state general rules for determining whether two IDRs will mix.


## II. R esults & D iscussion


## A. Phase Identification with Domain Decomposition

In direct coexistence simulations, multiple copies of one or more IDRs are placed in an elongated box, and allowed to equilibrate. IDR interactions across the periodic boundary can stabilize the formation of a dense slab of protein, the concentration of which ( c den ) can be measured along with the concentration of the dilute phase ( c dil ).

Our domain decomposition method (DDM) divides the simulation cell into equally sized voxels, and keeps track of the running-average concentration in each voxel over time. We then fit the probability density of these concentrations using a kernel density estimator. One peak appears for each phase present in the system, with the center of the peak marking the phase concentration. An example of this can be seen in Figure 1A , where a snapshot of the trajectory, the concentration in each voxel, and the time averaged probability density are shown.

The DDM shows excellent agreement in c den and c dil when compared to the common protocol of fitting a Gibbs’ dividing surface to the average slab density[ 34 ]. In the dividing surface method, the dense region in each frame is centered, and a 1-dimensional profile is fit to the time-averaged density[ 25 ], [ 35 ]. The concentration of both phases are then measured by averaging the density away from the dividing surface between the two regions. To compare these methods, we used a repository from von Bülow et al. containing both the raw MD trajectories and the calculated concentrations for 216 phase separating IDRs[ 36 ]. To determine the optimal voxel size for the DDM, we measured the correlation (R 2 ) between the two methods for all 216 proteins for voxel side lengths ranging from 5 −60Å ( Figure 1B ). In smaller voxels, the DDM underestimates c dil because many of the voxels will have only a few residues at a time. This skews the distribution of c dil towards 0. Based on this convergence behavior, we selected a voxel side length of 35Å for further analysis. This value was chosen to ensure the calculation is performed comfortably above the plateau for c dil ( ∼ 25Å ), while avoiding the loss of resolution from larger bin sizes. Figure 1C&D shows the agreement between the methods with the selected voxel size.

Gray points in Figure 1C&D , are simulations where no dense phase is identified by the Gibbs’ dividing surface method, but two peaks are still identified using DDM. This is due to the formation of IDR clusters, which form higher density domains but are not stabalized across the periodic boundaries. In these cases, the concentration of the two identified peaks is roughly equal, with the average ratio of = 0.86. When studying phase separation, this fraction becomes inconsequential because the propensity for phase separation (Δ G = k B T ln( c dil /c den ), −10 ≤ Δ G/k B T ≤ 0) will be roughly −0.15 k B T [ 36 ], [ 37 ]. While it may allow us to better study the nucleation of condensates in silico , this is outside the scope of the current study, which focuses on stable dense phases.

The main benefit of the DDM, is that it makes no assumptions about the number or spatial arrangement of phases. The analysis can determine phase concentrations, even if there are multiple, spatially separated dense regions. This property becomes essential when analyzing multi-component systems where IDRs mix, form distinct domains, or fully segregate. In short, the DDM does not require explicit interface fitting, a process which can introduce variability between studies.

The DDM can effectively characterize the spatial organization of binary mixtures using the individual IDR concentration in each voxel. We demonstrate this in Figure 1E-H by applying the method to simulations where two IDRs mix (E/F) and demix (G/H). In the mixed system, decomposing the total probability density ( Fig. 1E ) reveals that IDR-1 (UniProt: Q96K19200 2 58) and IDR-2 (UniProt: Q3LI601 4 4) contribute roughly equally to the dense phase. The dilute and dense phases are highlighted in the voxel concentration space ( Fig. 1F ), where scatter points represent the average concentration of each IDR in a single voxel.

When two IDRs demix into separate condensates ( Fig 1G&H ), distinct peaks for both dense phases appear in the density distribution. However, the second peak, Dense (ii), is hardly visible in this simulations setup, because there are fewer voxels with this density. This shows that for small system sizes, there may be insufficient copies of each protein to accurately capture the concentration of all phases present. Nevertheless, we show that it is possible to identify the IDRs demixing using the concentration space.

The following sections are dedicated to exploring the mixing tendencies of two-component IDR systems using this method.


## B. Contents of Protein Set

To investigate the principles of IDR mixing and demixing, we curated a diverse set of 32 IDRs and performed direct coexistence simulations on all 496 unique combinations. Our selection of IDRs prioritized two key dimensions of diversity: sequence composition and propensity for homotypic phase separation. To span the compositional space, we selected proteins from different ‘grammar clusters’[ 38 ]. These are groups of IDRs with similar sequence patterns defined by their amino acid composition (Supplementary Table I). To span a range of self-interaction strengths, we selected proteins with varying Δ G , a measure of homotypic phase separation propensity calculated from direct coexistence simulations[ 37 ]. All proteins were drawn from the von Bülow et al. dataset[ 36 ], allowing us to use simulated Δ G values from their published trajectories. This approach both ensures accuracy and reduces the computational expense of simulating homotypic systems. More details on the selection criteria are provided in the Methods section.

The resulting protein set covers a wide range of physicochemical properties, while being enriched in strong phase separators ( Supplementary Fig. S1 E ). Our subset’s median length (95 amino acids) is shorter than that of the source dataset, but more closely reflects that of IDRs found in the human proteome (80 amino acids)[ 39 ]. We deliberately enriched for sequences with higher mean residue hydrophobicity and a stronger homotypic phase separation (more negative Δ G ) to ensure a large proportion of condensate forming mixtures. The subset adequately samples sequences with varying aromatic content, spanning from aromatic-poor to aromatic-rich sequences. Our sampling of the charged sequence space is narrower, with the net charge per residue (NCPR) ≈ 0 where homotypic phase separation is more prevalent.


## C. Quantifying Mixing and Demixing

Binary IDR mixtures can exhibit diverse spatial organizations, from complete mixing in a single condensate to full segregation. Between these extremes lies a continuum of partial demixing behaviors, stemming from differences in the preference for homo and heterotypic interactions. To systematically characterize this mixing landscape across hundreds of binary systems with variable compositions, we developed a quantitative metric based on the spatial distribution of each species within the concentration space.

For each unique pair in our protein set, we performed simulations at equimolar concentration (50:50) with ∼36, 000 amino acids in total. The system size was chosen to ensure that a mixed dense phase could form, while being computationally efficient. Additional concentration ratios were simulated (e.g. 25:75 and 90:10) with the same number of amino acids where protein lengths permitted. In total, we performed 1963 simulations, all of which started in a completely demixed state.

In Figure 2A&B , an example of a mixed system is shown at five different concentration ratios. Although each of these mixtures exhibits only one dense phase, the concentration space shows different behaviors as the concentration of O60229 increases. Noticeably, composition 28:72 shows a narrow distribution of points in the dense phase, while the reciprocal concentration (72:28) shows a greater spread. This wider distribution indicates an increasing preference for homotypic over heterotypic interactions. If the segregation of IDRs were to become stronger, then eventually the distribution may span the entire compositional space, similar to what is seen in the demixed example of Figure 1H .

To quantify the mixing of IDRs, we analyze how the scatter points in the concentration space relate to the composition line. The composition line represents the global average concentration ratio of the two components in the system. If every point fell on this line, then there would be perfect mixing. The degree of demixing is therefore defined as the deviation away from this line. The variance parallel ( λ 1 ) and perpendicular ( λ 2 ) to the composition line, as shown in Figure 2C , are used to calculate the demixing index ( D ): D = 2 λ 2 / ( λ 1 + λ 2 ). This simple metric is not only independent of composition, but also conveniently falls between 0 and 1. Additionally, we are inherently measuring the demixing in the interface and dense region, without the need to explicitly determine their boundaries.

Figure 2D&E show a slightly more complicated system, where there is a large ΔΔ G (2.8 k B T ) between the two IDRs. Here, the mixture ‘leans’ towards a pure dense phase of Q3LI60 (light red). The curve of points, visible in Figure 2F , suggests that there is a significant deviation between the concentration at the surface and in the dense phase of the system. In the trajectory snapshots, we can see that there is a higher concentration of Q92581 (dark red) at the surface, and Q3LI60 at the core of the dense phase.

Since demixing is only relevant in systems where a dense phase forms, we focus on those with Δ G < −3 k B T . Remarkably, our minimal dataset of 32 proteins spans the entire range of demixing values ( Fig. 2G ), which shows compositional dependence ( Fig. 2H ). The demixing index follows a normal distribution across the compositional ranges, with equimolar mixtures exhibiting the highest average demixing. This behavior suggests that binary condensates favor architectures with a dominant scaffold species and a lower concentration client species that partitions within. Non-equimolar mixtures appear to be promiscuous, with very low demixing indicies. This suggests that discriminating client proteins from condensates may rely heavily on factors unrelated to the IDR, such as the size of folded domains or specific interactions[ 40 ]. However, this could be influenced by our datasets preference for IDRs which can undergo phase separation.

Finally, we validated the demixing index against the mixing parameter recently introduced for polymer systems by Chen and Jacobs, which is reproduced in Equation 1 [ 29 ]. This method calculates the cosine similarity between the local composition and the target composition over the one-dimensional density profile. Here, we set to the concentration ratio for all systems. We observe excellent agreement between the methods for equimolar concentrations ( R 2 = 0.97). However, the cosine similarity approach requires the explicit definition of phase boundaries to calculate an average over the dense phase. This dependency results in poor characterization at non-equimolar concentrations ( R 2 < 0.5), where the dense phase of the minority component is often narrow, as exemplified in Supplementary Figure S2 . In these regimes, our demixing index proves to be more robust, as it utilizes the variance across the entire concentration space without the need to define surface boundaries. While significantly larger simulations might mitigate the boundary artifacts affecting the cosine metric, our approach remains effective even for the system sizes typical of high-throughput studies.

In the following sections, we explore why certain IDRs mix while others segregate, and how their mixing affects the thermodynamic stability of the resulting condensates.


## D. Chemical Grammar Influences Mixing Behavior

IDRs with high fractions of aromatic residues or welldistributed charge blocks are generally expected to phase separate[ 41 ], [ 42 ]. Here, we build on this intuition by investigating how sequence-based physicochemical descriptors impact IDR mixing. For each IDR, we calculated: mean residue stickiness , sequence charge decoration (SCD), sequence hydropathy decoration (SHD), net charge per residue (NCPR), fraction of aromatic residues ( F aro ), charge clustering parameter ( κ ), the net charge of the IDR (Q), and sequence length (N)[ 43 ]. For each protein pair, we then constructed pairwise features as the mean or absolute difference of each descriptor between the two IDRs, resulting in 16 features.

We employed an elastic net regularized logistic regression model, to obtain interpretable coefficients, which will describe how important each feature is for mixing or demixing. The average coefficient for each feature was calculated over 1000 random train-test splits (80% train, 20% test, split by protein pair to prevent data leakage). Figure 3A shows how the demixing indices of equimolar mixtures relate to a logistic regression model built with the top 8 features. The averaged coefficients for the standardized features, can be seen in Figure 3B , while the raw values from the model can be found in Supplementary Table S2.

The two most robust predictors are the difference in NCPR and F aro . The disparity in net charge per residue promotes mixing, suggesting that IDRs with opposing charges can form complementary heterotypic interactions. In contrast, a large difference in the fraction of aromatic residues is strongly linked to demixing. Aromatic residues engage in specific π − π and cation − π interactions that are sensitive to partner chemical composition. When one IDR is aromatic-rich and its partner is aromatic-poor, these interaction modes become asymmetric, favoring homotypic over heterotypic contacts. This finding is consistent with experimental observations that aromatic patterning governs the phase behavior of prion-like domains[ 44 ].

While these insights are not necessarily novel, the logistic regression model allows us to determine the relative importance of each factor. For example, the mixing of long IDRs is unfavorable due to the reduced entropy of mixing[ 45 ], [ 46 ]. But this can be overcome by an increase in heterotypic interactions, which can be seen at high [ 47 ]. Using these coefficients, we can determine how a mutation might push two sequences to change their mixing behavior. However, future studies should test the performance of refined models on larger datasets, where the effect of concentration ratio can also be used to predict (de)mixing.

We further examined mixing based on the dominant chemical character of the IDR pairs (e.g., hydrophobic-hydrophobic, charge-polar), which can be found in Supplementary Table S1. Of the categories shown in Figure 3C hydrophobichydrophobic pairs exhibit the lowest demixing scores (median D = 0.012), suggesting these proteins mix promiscuously. This likely stems from the non-specific nature of hydrophobic interactions. Notably, GIN group 10 (well-mixed hydrophobics enriched in methionine) are highly promiscuous when interacting with any other proteins (median D = 0.013, n = 435) regardless of partner chemistry. These IDRs are frequently associated with cancer-driving genes, likely due to their roles in DNA-templated transcription[ 38 ]. A well studied example is the prion-like domain of ARID1A, a chromatin remodeling protein which is frequently mutated in cancers[ 17 ]. The role of ARID1A’s IDR is to compartmentalize with other proteins[ 48 ]. The promiscuous mixing behavior we observe suggests that IDRs in this category may be particularly susceptible to aberrant interactions when mutated or dysregulated.

In contrast, IDR pairs characterized by having charged residues display significantly higher range of demixing behavior. Charge-hydrophobic, charge-charge, and charge-polar pairs all show broad distributions spanning from complete mixing to full demixing. This variability reflects the IDR’s need for both complementary charge patterning and a reduction in absolute net charge of the condensate. Experimental studies have observed that mixing can be inhibited by a mismatch in charge patterning, regardless of the number of charged residues[ 49 ], [ 50 ].


## E. Stability of Mixed Condensates

While the demixing index characterizes the spatial organization of components within the dense phase, it does not directly address the thermodynamic driving force for condensate formation. Two IDRs may mix homogeneously yet form only a marginally stable condensate. Here, we analyze condensate formation using the heterotypic transfer free energy (Δ G ij ) for well-mixed systems ( D < 0.2) at every composition, analogous to how we calculate the homotypic Δ G ii using the DDM.

Figure 3D shows the relationship between Δ G ij and the difference in homotypic transfer free energy (|Δ G ii − Δ G jj |). Strong phase separation predominantly occurs when the two IDRs have similar self-interaction strengths, with differences below 2 k B T . Larger disparities in homotypic Δ G tend to produce weaker heterotypic condensates, likely because the stronger phase separator dominates the dense phase while the weaker partner remains partially excluded. The outliers deviating away from this trend are predominantly hydrophobic sequences, which mix well even when paired with dissimilar partners. A breakdown of the contribution from each chemical interaction group can be seen in Supplementary Figure S3 .

Figure 3E shows that for most pairs, the average serves as a reasonable estimate for Δ G ij , particularly when Δ G ij < −3 k B T . Hydrophobic pairs (H-H) have the closest relationship between Δ G ij and , with R 2 = 0.67 and a slope of 0.99 (Supp. Figure S4). This agreement can also be attributed to the non-specific nature of hydrophobic interactions. Polar pairs (P-P, R 2 = 0.50) had the worst agreement overall, which we attribute to a lack of sequences that were able to both mix and phase separate. More interestingly, the next worst agreement came from pairs where both IDRs are categorized based on their charge (C-C, R 2 = 0.52), which is likely due to the need for charge balancing. These results are crucial for understanding how the physical properties of a condensate can be tuned by understanding its chemical composition.

Finally, we more closely examine the role of charged residues in condensate formation. Figure 3F plots Δ G ij against the absolute net charge in the simulation. Each protein pair is represented by connected points spanning different concentration ratios. As the net charge in the system approaches zero, the strength of phase separation increases. To have Δ G < −4 k B T , roughly 7% of the charged amino acids can remain unbalanced. However, the point shading shows that perfect charge balancing does not necessarily yield the strongest phase separation. This suggests that while charge balancing contributes to heterotypic stability, other interactions like the fraction of aromatic and hydrophobic residues provide a larger driving force for condensate formation.

Taken together, these results suggest that heterotypic condensate stability follows simple patterns. Similarity in homotypic Δ G promotes mixing, charge complementarity can enhance phase separation, and non-specific hydrophobic interactions provide a baseline driving force that is insensitive to partner identity.


## F. Comparison to Experiments

Finally, we focus on how the methodology presented here can complement experimental studies.

We start by creating mixtures of fused-in-sarcoma (FUS) and hnRNPA1 (A1) (FUS-A1 W T - red) at three concentration ratios, to compare with the experimental studies done by Farag et al., as seen in Figure 4A&B [ 26 ]. Experimentally, the convex/concave nature of the dilute phase has been shown to accurately quantify the mixing behavior of two IDRs[ 18 ], [ 52 ]. Concave dilute arms are associated with strong heterotypic interactions, while convex curves indicate a preference for homotypic interactions. When Farag et al. mutated A1 by substituting 12 Asp residues into the sequence (A1 p 12 D - blue), the dilute arm became convex, implying homotypic interactions were favored. However, the two IDRs still colocalized, as observed using fluorescence microscopy.

Our simulation results also show colocalization, weaker phase separation, and a higher D for the mutated sequence. However, the dilute arm of the simulated mixtures show the opposite behavior to that in the experimental study. As previously stated, the dilute phase concentration can often be under sampled in MD simulations, while the dense phase converges quickly. The opposite is true for experimental studies, where the dilute phase concentration is easily measured by centrifuging the dense phase out of solution, and then measuring the protein concentration in the supernatant. Therefore, we suggest that the demixing index, and concentration of the dense phase are better metrics to compare with experimental observables. Next, we turn to the study performed by Lyons et al., which mixed the IDR of Mediator-1 (MED1) with soluble nuclear extract[ 49 ]. MED1 is a regulator of transcription, and so the study focused on which proteins would phase separate with the mediator. Everything interacting in the MED1 condensate was segregated (pellet) via centrifugation, while the rest remained in the supernatant. In comparisons with other experiments, the researchers noted that proteins which did not partition with MED1 were likely to partition with NPM1. We simulated the mixing of 13 of these proteins with both MED1 and NPM1, and analyzed the demixing preference for each one ( Fig. 4C ). Ten of the proteins show clear preference for a binding partner, which agrees well with their concentration in the pellet versus the supernatant (Filtered Spearman’s p = 0.83).

However there are three outliers that do not follow this partitioning. The disagreement could suggest that there is another interaction driving the proteins into the MED1 pellet, or causing them to remain in the supernatant. We highlight FUS and EWSR1 (green), because FUS has a very high demixing index for both NPM1 and MED1 (0.94 and 0.82 respectively), suggesting that it would not partition with either IDR. EWSR1 also shows high demixing for both species ( D EW SR 1− MED 1 = 0.44 and D EW SR 1− NP M 1 = 0.89), and a preference for FUS ( D EW SR 1− F US = 0.11). With over 3000 proteins in the soluble nuclear extract, along with RNA, it is possible that other interactions are mediating protein mixing. For example, CTR9 is known to phase separate with MED1 when RNA is present, which may account for its preference for MED1 over NPM1 experimentally[ 53 ], [ 54 ]. The excellent agreement with experiments suggests that we can capture protein mixing as driven by their IDRs. The three exceptions show that when IDRs mix experimentally, but not through simulations, then it is possible that the interaction is mediated by folded domains or other species.

To show how powerful these IDR simulations can be, we take 18 IDRs which have had their interactions studied by Gilat et al., and simulate each unique pair at equimolar concentrations[ 51 ]. The connecting edges between each IDR can be seen in Figure 4E , where the thicker chords indicate a lower demixing index. Chords between IDRs were only drawn if a dense phase was present in the simulation, with low demixing ( D < 0.25). Six of the seven top mixers (hnRNPA1, TAF-15, FUS, RBM-14, HSP88, & TDP-43) were also able to phase separate strongly in homotypic experimental constructs, and exhibited similar promiscuity when mixed with various partners. In the experimental study TDP-43 did not mix with FUS, hnRNPA1, HSP88, RBM-14, or TAF15. However, this discrepancy is due to the α -helical nature of residues 320-343, which were kept disordered in our study and has been noted to greatly increase homotypic interactions when folded[ 55 ]. When the α -helix was removed by Gilat et al., TDP-43 mixed promiscuously with the aforementioned proteins.

For all simulations performed within this section, we tested the model derived in Equations 2 & 3. The results in Figure 4D show poor performance on unseen proteins. This underscores the need not only for explicit simulations of IDRs, but also clear methods to use in their analysis.

The IDRs in Figure 4 are integral components of distinct cellular bodies, including paraspeckles, stress granules, and transcriptional condensates[ 26 ], [ 49 ], [ 51 ]. By successfully reconstructing their mixing preferences in silico , we demonstrate the potential of this methodology to predict IDR interactomes. Scaling this approach would allow for the construction of interaction matrices, providing a clearer understanding of cellular organization. Furthermore, predicting these interactomes offers a crucial filter for therapeutic design, enabling the identification of synthetic IDRs that can precisely target specific condensates while avoiding off-target interactions with other membraneless organelles.


## III. CONCLUSIONS

We have introduced a new methodology for analyzing the phase separation of disordered proteins, and their mixing, in silico . Our domain decomposition method accurately determines the concentrations of both dense and dilute phases in systems with a single component, without the need to identify the condensate surface. In two-component systems, we have shown that the mixing of disordered proteins can be numerically characterized at both equimolar and non-equimolar concentration ratios. By analyzing 1,963 binary mixtures, we found that most condensate-forming pairs favored asymmetric concentrations, with one dominant scaffold accommodating minority clients.

Through these simulations, we were able to establish intuitive design rules that can explain observed condensate compositions. Hydrophobic sequences mix promiscuously across partner chemistries, whereas charged sequences exhibit sensitivity to the complementarity of their partner’s charge. Furthermore, we observed that the strength of phase separation for heterotypic condensates largely follows the average of homotypic values, but charged sequences can exceed this through mixing with charge-complementary species.

Finally, we used this methodology to explain the protein organization seen in experimental studies. By isolating the disordered proteins in simulations, we can identify when colocalization between two sequences is due to affinity between the disordered regions, or additional factors such as RNA or folded domains. Our demonstration shows that simulating larger sets of proteins could help to identify condensate compositions, potential dysregulators, and ideal targeting candidates for condensate modulation.


## IV. METHODS


## A. Protein Dataset

The proteins for our study were selected from those previously simulated in CALVADOS2 to develop a phase separation predictor[ 25 ], [ 36 ]. This dataset contains the IDR sequences of individual proteins, calculated metrics (e.g. the fraction of aromatic residues), and the measured concentrations of the dense ( c den ) and dilute ( c dil ) phase from direct coexistence simulations. The advantage of using a subset of these proteins is that their transfer free energies (Δ G = ln ( c dil /c den )) have already been determined through simulations.

We restricted our pool to IDRs with sequence lengths ( N ) fewer than 250 amino acids, which allowed us to use the same simulation box size for all systems, while maintaining a reasonable computational cost. Proteins were categorized using the 30 distinct GIN (Grammars Inferred using NARDINI+) clusters defined by Ruff et al.[ 38 ] These clusters categorize IDRs based on their “molecular grammars”, which include features like amino acid composition and the patterning of charged or hydrophobic residues.

Within each GIN cluster, proteins were binned by their homotypic Δ G , a measure of a protein’s self-association strength which ranges from −10 k B T (strong phase separation) to 0 k B T (no phase separation). We categorized the GIN clusters as follows:

For GIN clusters that contain at least one protein with Δ G < −5, we selected the shortest sequence within four distinct Δ G bins: (−10, −8], (−8, −6], (−6, −4], and (−4, −2]. For the remaining GIN clusters, where all members exhibited weaker self-association tendencies (Δ G ≥ −5), we selected one protein with less than 100 residues to ensure the group was represented.

This selection process yielded a varied set of 32 IDRs from different GIN clusters, enabling a systematic investigation into how protein length, sequence grammar, and self-affinity influence mixing behavior in two-component condensates.


## B. Concentration Ratios of Simulated Mixtures

For each unique protein pair, we simulated between 1-5 compositional ratios while maintaining roughly the same total number of residues (36,000). Our procedure begins by defining five target fractions for the total residue count of the first protein (0.9, 0.75, 0.5, 0.25, and 0.1). For each target fraction, we solve for the integer number of molecules of each protein ( n 1 and n 2) that minimizes the deviation from the target fraction while adhering to the total amino acid count.

For example, if IDR-1 has 40 amino acids, and IDR-2 has 120, then for a ratio of 0.75 (concentration ratio 75:25) we would have 675 copies of IDR-1 and 75 copies of IDR-2.

In some cases, this initial approach can lead to degenerate solutions where multiple target fractions yield the same integer number of residues. If the initial method produced fewer than five unique concentrations, the search was expanded to explore different total amino acid counts (varying the initial target by ±15 to 25%). From the resulting pool of unique candidates, a final set of five was selected to maximize compositional diversity by choosing concentrations that represent the extremes and quartiles of the sampled mole fractions.

This approach resulted in 1963 combinations of proteins at varying compositions. A full CSV of all simulated pairs can be found on the GitHub repository here: https://github.com/shakespearemorton/IDRMixing


## C. Forcefield

All simulations employed the CALVADOS2 coarse-grained force field[ 25 ], which represents each amino acid as a single bead centered at the C α position with implicit solvent treatment. The total potential energy of the system is defined by bonded and non-bonded interactions. Adjacent amino-acid beads in a protein were connected by a harmonic potential where r is the distance between the two residues. The equilibrium bond distance is r 0 = 0.38nm, and the force constant is k = 8033 kJ mol −1 nm −2 . Non-bonded interactions are separated into a short-range non-ionic term and a long-range ionic term. Here, interactions between residues separated by one bond are excluded. Non-ionic interactions are described by a truncated and shifted Ashbaugh–Hatch potential, which modifies the Lennard–Jones (LJ) form to incorporate residue-specific hydrophobicity: where the standard LJ potential is The depth parameter is fixed globally at ϵ = 0.8368 kJ mol −1 . Residue-specific parameters σ (size in Å ) and λ (unitless stickiness/hydropathy) follow CALVADOS2 tabulations. A cutoff of r c = 2.0nm is used for all non-ionic interactions.

Salt-screened electrostatics are modeled with a Debye–Hückel potential, truncated and shifted at 4.0nm: where q i and q j are the partial charges, e is the elementary charge, and ε 0 is the vacuum permittivity. The temperature dependence of the solvent dielectric constant is captured by The Debye length D depends on the ionic solution strength c s = 0.15 M and the Bjerrum length B via


## D. Simulation Protocol

All molecular-dynamics simulations were performed in the NVT ensemble using OPENMM 8.2[ 56 ]. A LangevinMiddleIntegrator maintains a temperature of 293 K with a friction coefficient of 0.01 ps −1 and a time step of 10 fs. Simulations use a slab box of size 20 × 20 × 200nm 3 . Initially, all protein chains were placed in the center of the simulation box, with their centers of mass aligned along the Z-axis, to form an initial slab configuration. A weak harmonic restraint ( k = 20 kJ mol −1 nm −2 ) between each residue and the center of the simulation box drives collapse into a single dense slab while the system is at a temperature of 400 K. The system is run with these conditions for 1 nanosecond to relax the chains while localizing them in a dense environment. After energy minimization, simulated annealing raises the temperature from 100 K to 293 K over 1 nanosecond to relax the structure. Each pair of IDRs is simulated for 5 µ s at 293 K, with the first 1 µ s discarded from the analysis as equilibration.


## E. Analysis of Phase Behavior

Protein concentrations in the dense and dilute phases were obtained via domain decomposition. The simulation box was partitioned into cubic voxels by dividing each dimension ( L i for i ∈ { x, y, z }) by an ideal voxel side length ( S ), taking the floor of L i / S to obtain the number of divisions (λ i ). Actual voxel dimensions were s i = L i /λ i , which may form rectangular prisms depending on box geometry.

For each voxel, we calculated the total residue count and the number of residues from IDR-1, then averaged them over time using Welford’s Online Algorithm[ 57 ]. A kernel density estimate with Gaussian kernel was fit to the distribution of voxel concentrations to generate the probability density distribution. Each peak in the distribution corresponds to a distinct phase, with the peak position defining the phase concentration. The number of coexisting phases was determined using scipy.signal.find_peaks , with a minimum peak height threshold of 8 × 10 −5 to exclude noise. The dilute phase was identified as the lowest-concentration peak. We validated this approach against traditional Gibbs dividing surface methods using 216 homotypic simulations from von Bülow et al.[ 36 ] which had both a dense and dilute phase present. For each trajectory, we performed our domain decomposition method on all frames after the first microsecond. Agreement between methods was measured with increasing S , and based on these results (see 1) we used S = 35 Å for our binary simulations.

For binary mixtures, voxel-averaged species fractions ( f s 1 ) were calculated as: where N s 1 and N s 2 are the residue counts of each species in a given voxel.


## F. Demixing Analysis via Compositional Projection

To characterize the spatial organization of the dense phase, we analyzed the distribution of voxel compositions relative to the concentration ratio of the system. For each simulation, we defined a composition unit vector, , derived from the average composition : An orthogonal unit vector, , was defined to represent the axis of demixing. We then projected the centered voxel compositions onto these axes to calculate the variance along the composition line (λ 1 ) and the variance perpendicular to it (λ 2 ): The demixing index ( D ) was calculated as the variance along the orthogonal (demixing) axis normalized by the total variance: This metric ranges from 0 (perfect mixing, where variance is dominated by density fluctuations along the composition axis) to 1 (complete demixing, where variance is dominated by segregation). By using a fixed basis defined by the concentration rather than a data-dependent basis (as in PCA), this method correctly penalizes deviations from the expected mixing ratio even when the dense phase is uniform but off-target.


## G. Calculation of Local Order Parameters

To validate our demixing index, we compared our results against the local mixing order parameter (q) introduced by Chen and Jacobs[ 29 ]. The z-axis was discretized into 100 bins. Time-averaged number densities for each species, ρ 1 (z) and ρ 2 (z), were calculated over the production run. The local composition vector was derived from these densities. The local order parameter q(z) was calculated as the cosine similarity between (z) and the concentration ratio ( Eq. 1 ).


## H. Logistic Regression Modeling

To identify robust predictors of demixing behavior, we employed elastic net regularized logistic regression with repeated cross-validation. The model was trained on a filtered dataset containing only binary mixtures where heterotypic interactions were strong enough to support a dense phase (Δ G ij < −3 k B T ).

For each IDR, we calculated eight physicochemical descriptors: mean residue stickiness , sequence charge decoration (SCD), sequence hydropathy decoration (SHD), net charge per residue (NCPR), fraction of aromatic residues (F aro ), charge clustering parameter (κ), total number of charged residues (N charged ), and sequence length (N)[ 43 ]. For each protein pair, we constructed pairwise features as either the arithmetic mean or absolute difference of each descriptor between the two IDRs. This yielded 16 candidate features, which were standardized (zero mean, unit variance) prior to training.

To handle class imbalance between mixed ( D ≤ 0.5) and demixed ( D > 0.5) systems, samples were weighted inversely proportional to their class frequency. We used the SAGA solver with an elastic net mixing parameter of 0.5 and a regularization strength of C=0.1.

Feature stability and importance were assessed across 1,000 independent train-test splits (80% train, 20% test). To prevent data leakage, splits were generated using a GroupShuffleSplit strategy, ensuring that all concentration ratios for a specific protein pair remained within the same fold. Features were ranked based on the absolute magnitude of their mean coefficients across all seeds.

Binary classification performance was assessed by thresholding the predicted demixing probability at 0.5, with systems classified as mixed ( D ≤ 0.5) or demixed ( D > 0.5).


## I. Software and Libraries

MD simulations: OpenMM 8.2[ 56 ]

Trajectory analysis: MDAnalysis 2.9.0

Scientific computing: NumPy 1.26.4, SciPy 1.13.0

Machine learning: scikit-learn 1.5.2

Data manipulation: Pandas 2.1.1

Visualization: Matplotlib 3.9.3

Rendering: Blender 4.2.1

All analysis code is available at https://github.com/shakespearemorton/IDRMixing .


## V. AUTHOR CONTRIBUTIONS

Both W.M. and R.V. designed the research, and wrote/edited the manuscript. W.M. performed the research and analysis.


## VI. FUNDING SOURCES

This project has received funding from the European Union’s Horizon Europe research and innovation programme under the Marie Sklodowska-Curie grant agreement No 101180586, the European Research Council (ERC) under the European Union’s Horizon 2020 research and innovation programme (grant agreement No 101001470) and the project National Institute of virology and bacteriology (Programme EXCELES, ID Project No. LX22NPO5103) - Funded by the European Union - Next Generation EU.

Computational resources were provided by the Ministry of Education, Youth and Sports of the Czech Republic through the e-INFRA CZ (ID:90254).

VII. ACKNOWLEDGMENTS

Several people helped to evaluate this work, making sure it would be useful and interpretable for larger audiences. Therefore, the following deserve our thanks:

Francesco Luca Falginella for discussions and reading the full first-draft.

Soren von Bülow for taking the time to meet and talk about the figures/findings.

Salomé Bodet-Lefevre for applying an experimental eye to molecular dynamics figures.

Erin Spearing for letting me talk about this work incessantly, and providing experimental insights.


## Footnotes

(e-mail: 250711{at}mail.muni.cz ).

https://github.com/shakespearemorton/IDRMixing