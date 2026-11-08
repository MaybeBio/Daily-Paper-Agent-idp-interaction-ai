# A compact generative language model learns the compositional grammar of phase-separating proteins


## Abstract
  Liquid–liquid phase separation (LLPS) of intrinsically disordered proteins drives the formation of biomolecular condensates, yet the sequence-level grammar that promotes condensation remains difficult to specify from first principles. Existing protein language models are typically trained on large, folded-protein-rich sequence corpora and may not optimally capture the compositional biases of LLPS-prone disordered proteins. Here, we show that a compact generative language model, with an architecture and size (∼17 M parameters) selected via systematic hyperparameter optimization and cross-validation, trained from scratch on a small set of phase-separating protein sequences, can learn sequence features associated with condensate formation. The model generates thousands of sequences that reproduce length-dependent trends in disorder, charge decoration, hydropathy patterning, and sequence entropy, with training and generative behavior stable across independent seeds. Homology analysis indicates that generated sequences are not full-length copies of known proteins, but instead combine short segments matching natural proteins with a novel, model-generated sequence. Descriptor-based screening of short generated sequences yielded a pool of disordered candidates, from which five synthetically feasible peptides were selected for experimental testing. Four of them show condensate-like signatures under near-physiological conditions, including droplet-like assemblies and increased turbidity. Coarse-grained phase-coexistence simulations of a subset of generated sequences with longer lengths show a broad range of phase-separation tendencies, with 12 of 89 sequences comparable to the strongly phase-separating hnRNPA1 low-complexity domain. These results suggest that compact, task-specific generative models can learn information-rich sequence grammars from small curated datasets and propose experimentally testable condensate-forming peptides.


## Introduction
  Biomolecular condensates formed by liquid–liquid phase separation (LLPS) are fundamental organizers of cellular biochemistry, concentrating specific proteins, nucleic acids, and small molecules into dynamic, membrane-less compartments that regulate signal transduction, RNA metabolism, and transcription.1–4 Aberrant condensate formation or dissolution is implicated in neurodegeneration, cancer, and viral infection, motivating an intense search for the sequence-level principles that govern LLPS.4

  Intrinsically disordered proteins (IDPs) constitute a major class of LLPS drivers. Lacking stable secondary or tertiary structure, IDPs sample heterogeneous conformational ensembles and frequently contain low-complexity regions (LCRs) enriched in polar and glycine residues.5–7 Several sequence-level descriptors—including aromatic residue fraction, net charge per residue, and charge-patterning indices—correlate with LLPS propensity,8,9 and the “sticker-and-spacer” framework provides a useful conceptual model in which short adhesive motifs (stickers) mediate intermolecular contacts while intervening linker regions (spacers) modulate valency and flexibility.10,11 Recent proteome-wide analyses have begun to formalize these patterns as “molecular grammars”—non-random amino acid compositions and patterning rules that define functionally distinct classes of disordered regions.12 However, many IDPs deviate from known descriptors, and microenvironmental factors such as crowding and post-translational modifications further modulate phase boundaries,13–15 making the grammar of phase separation difficult to specify from first principles alone. A data-driven generative approach that learns sequence–function relationships directly could therefore complement existing heuristics.

  Protein language models (PLMs) based on transformer architectures have achieved remarkable success in protein structure prediction and evolutionary analysis.16–20 However, large PLMs trained on millions of predominantly globular protein sequences encode limited information about the compositional features specific to LLPS-prone IDPs—a consequence of their training bias toward folded proteins and the small size of curated LLPS datasets (on the order of a few hundred sequences). Fine-tuning such models on limited LLPS data risks overfitting and may obscure disorder-specific signals. Indeed, UMAP projections of ProtT5-XL embeddings for LLPS+ and PDB* sequences show no clear separation in the reduced 2D space (Fig. S1), consistent with recent evidence that pretrained PLM representations are not always well aligned with specific downstream biological tasks.21 Growing evidence suggests that small, specialized language models trained on a narrowly defined task can outperform large, general-purpose foundation models at that same task.22–24

  These observations motivated us to take a different approach: rather than fine-tuning a large, general-purpose PLM, we developed compact, task-focused nano-GPT models trained from scratch on two non-overlapping, curated sequence sets from Saar et al.:25 LLPS+ (137 IDPs known to phase-separate) and PDB* (1562 well-folded, LLPS-resistant proteins). Training separate model instances on each dataset allows the models to internalize the compositional grammar of their respective class—the patterns of amino acid co-occurrence, charge arrangement, hydropathy patterning, and low-complexity motif usage that collectively characterize each class. After training, new sequences are sampled autoregressively (one residue at a time, conditioned on all preceding residues), yielding synthetic libraries for downstream analysis and experimental testing.

  Three questions organize the results that follow:

  (1) Has the model learned the compositional grammar of phase-separating IDPs? Do sequences from LLPS+ GPT reproduce the physicochemical signatures of disordered, phase-separating polypeptides across different sequence lengths?

  (2) Are the generated sequences novel, or merely memorized? To what extent do generated sequences represent chimeric recombinations of natural LLPS-driving motifs rather than copies of training proteins?

  (3) Do generated peptides form condensates? Do selected LLPS+ GPT peptides undergo condensation under near-physiological conditions, and does a PDB* GPT control sequence behave as a stably folded, non-condensing protein?


## Results

### A compact nano-GPT framework for LLPS-prone sequence generation
  We trained two instances of a lightweight, decoder-only GPT on the contrasting LLPS+ and PDB* datasets from Saar et al.25 The architecture comprises 2 stacked self-attention layers with 2 heads each, a 1024-dimensional token embedding, and a context window of 128 residues (Fig. 1a; full details in Methods and SI). We refer to the resulting models as LLPS+ GPT and PDB* GPT, respectively. Each model learns which amino-acid patterns co-occur along a sequence and generates new sequences autoregressively, proposing one residue at a time conditioned on all preceding context (Fig. 1b).

  To ensure that generated sequences span the full length distribution of each training set, we partitioned training-set lengths into 50 bins and sampled 64 sequences per bin with lengths drawn uniformly within each bin, yielding 3200 sequences each for LLPS+ GPT and PDB* GPT (see Methods for details). SI files S1 and S2 provide these sequences in FASTA format.


### The models capture length-dependent sequence grammar
  To test whether the GPT models learn higher-order compositional rules beyond matching global averages, we performed a length-ablation analysis comparing training sequences to generated sequences across sequence-length bins (Fig. 2, S2 and S3). Sequences were partitioned into 50 length bins (64 generated sequences per bin, 3200 in total). Bins with fewer than two training sequences were excluded from the comparison, leaving 21 bins spanning 117–766 residues (21 × 64 generated sequences in Fig. 2). Within each bin, we computed eight sequence-based, physicochemical properties for both the training data and newly generated sequences, namely, hydropathy, sequence charge decoration (SCD), probability of disorder using AIUPred,26 Shannon entropy of the sequence, fraction of charged residues (FCR), kappa (κ), net charge per residue (NCPR) and FINCHES homotypic mean-field interaction energy (ε).27 These features were calculated using localcider28 and FINCHES.27

  LLPS+ GPT faithfully reproduces the training-set trends for all the calculated sequence properties (Fig. 2 and S2). Crucially, within the error range (shaded regions), the predicted and training curves are statistically indistinguishable across nearly the entire length range for all eight descriptors.

  The same analysis for PDB* GPT was performed except for FINCHES ε (Fig. S3). FINCHES ε was excluded since it cannot be calculated for folded proteins. They likewise show strong agreement between training and generated sequences, confirming that both models capture the relevant compositional constraints of their respective sequence classes across the full range of sampled lengths. These results indicate that the models have internalized higher-order sequence correlations sufficient to reproduce dataset-like physicochemical statistics at each length scale.


### Model ablation reveals the importance of the first attention layer
  Post-training model ablation was used to assess the contribution of individual transformer components to the biophysical fidelity of generated sequences (Fig. 3). Layer- and head-level contributions were removed from the trained model by skip-connection bypass (layers) or by zeroing the corresponding output-projection weights (heads), and 1024 sequences were regenerated under each ablated condition and compared to the unablated baseline via the Jensen–Shannon divergence (JSD) of the FCR/|NCPR| density.

  The baseline model reproduces the dense, low-FCR core of the training distribution (Region 1 of the Das–Pappu diagram-of-states29); the sparse, fragmented structure visible at higher FCR in the training-data density (Fig. 3a) reflects the limited size of the training set (137 sequences) rather than genuine multi-modal structure in the underlying distribution, and is not expected to be reproduced by the model. Ablating layer-0 produced the largest deviation from baseline (JSD = 0.48), substantially exceeding layer-1 (JSD = 0.29), identifying layer-0 as the dominant contributor to the charge composition of the generated ensemble. Within layer-0, no single head accounted for the layer's full effect (JSD = 0.35 and 0.37 for heads-0 and -1, respectively, both below the full-layer value), consistent with charge-related information being distributed across heads within that layer rather than concentrated in one. Notably, this was not the case for layer-1. Ablating head-0 of layer-1 alone (JSD = 0.39) produced a larger deviation than removing the entire layer (JSD = 0.29), a non-monotonic result suggesting a compensatory interaction between the two heads of layer-1 that is disrupted by single-head removal but not by full-layer bypass. This pattern indicates that component-level importance in this model is not strictly additive, and that at least one head–layer interaction warrants further mechanistic characterization beyond the scope of the present ablation grid.

  Taken together, these results indicate that the generative fidelity of the model with respect to charge composition is not uniformly distributed across the network but is concentrated in specific components, with layer 0 playing an outsized role and layer 1 exhibiting head-level interdependence rather than redundancy. All examined sequences, generated and training alike, fall within Region-1 of the Das–Pappu diagram (FCR < 0.25), consistent with the weak-polyampholyte character expected of LLPS-driving IDPs. Since all sequences fall within Region-1, differences between models appear as shifts of the density within Region-1 rather than as transitions between regions. This motivates a sequence-level compositional and patterning comparisons between LLPS+ and PDB* derived generated sequences presented in the following section.


### Generated sequences are predominantly chimeric recombinations of natural motifs
  A generative model could, in principle, produce sequences by memorizing and reproducing training examples or by learning transferable compositional rules. To distinguish between these possibilities, we performed DIAMOND BLASTp30,31 homology searches (E-value ≤ 10−3) against the SwissProt protein database, obtained from UniProt,32 and the LLPS+ training set, classifying each of the 3200 generated sequences into one of four categories, the details of which are discussed in Methods:

  • Novel (391 sequences, 12.22%): no BLAST hit meeting the E-value threshold in either database.

  • Chimeric (2793 sequences, 87.28%): no single near-full-length, high-identity match (coverage ≥90% and identity ≥90% to one subject), but one or more non-overlapping segments (≥8 aa, ≤10 aa overlap tolerance) match natural sequences, whether from a single source protein or several. The remainder of the query has no detectable match and is novel.

  • Reproduced natural (1 sequence, 0.03%): a single SwissProt hit spans the full query length but the sequence is absent from the training set.

  • Memorized (15 sequences, 0.47%): a full-length, near-identical match to a training-set sequence.

  From Fig. 4a, it can be observed that the overwhelming majority of generated sequences (87.28%) fall into the chimeric category, with genuine memorization confined to a negligible fraction (0.47%) and one case of single-protein full-length reproduction (0.03%). This distribution indicates that the model is not reproducing training examples. The vast majority of generated sequences are not explained by a single near-full-length, high-identity match to one natural protein, and instead show only partial, fragmentary similarity to one or more natural proteins rather than copying or lightly editing a single template.

  The fragment-level coverage analysis (Fig. 4b) makes the recombinatorial logic explicit. The best single fragment typically accounts for only a modest share of the query; the single-fragment distribution peaks around 10–20% coverage while combining all fragments shifts the distribution rightward, with total coverage peaking around 30–40% and extending out toward full-length matches. The persistent gap between the single-fragment and total-coverage distributions across nearly the entire range confirms that no individual alignment explains a chimeric sequence on its own. Rather, the total coverage peaking at 30–40% (Fig. 4b) indicates that most chimeric sequences consist mainly of novel sequence interspersed with natural-like segments.

  This is corroborated by the fragment-count distribution (Fig. 4c). While a majority of chimeric sequences are assembled from 2–4 non-overlapping fragments (each bin accounting for roughly 500–715 sequences), a substantial fraction (approximately 690 sequences, ∼25% of the chimeric set) retain only a single fragment. These single-fragment cases are classified as chimeric not because they combine multiple natural fragments, but because their sole matching region falls short of the ≥90% coverage and ≥90% identity threshold required for a full-length reproduction, that is, they show partial, imperfect similarity to one natural protein rather than either an exact copy or a multi-motif recombination. In the multi-fragment cases, a smaller tail (5–7 fragments) reflects more extensive recombination across several source proteins. Together, these results indicate that the model's departures from natural sequences span a spectrum, from single imperfect partial matches, through combinations of a handful of fragments, to extensive multi-protein recombination, with genuine full-length reproduction or memorization essentially absent (Fig. 4a).

  Sequences generated by PDB* GPT show a sharply contrasting profile. All 3200 sequences (100%) returned no SwissProt hit at the applied E-value threshold. This contrast confirms that the two models have learned qualitatively distinct sequence distributions. One recombining known LLPS motifs into novel chimeras, the other generating sequences that are globally unrelated to any catalogued protein.


### LLPS+ and PDB* GPT generate sequences with distinct physicochemical signatures
  Having established that generated sequences are predominantly not reproductions of natural proteins, we next compare the physicochemical features between sequences generated using LLPS+ and PDB*. Fig. 5a compares disorder-probability distributions (AIUPred26) for sequences from the two models. LLPS+ GPT sequences are overwhelmingly predicted to be disordered, with density concentrated at high disorder values, whereas PDB* GPT sequences cluster at low disorder probabilities consistent with folded proteins.

  Mean hydropathy (Fig. 5b) is shifted toward higher values for PDB* sequences relative to LLPS+, consistent with the hydrophobic cores that stabilize folded globular proteins. LLPS+ sequences instead occupy a lower, broader hydropathy range, in line with the reduced overall hydrophobicity typical of disordered, phase-separating sequences.

  LLPS+ GPT sequences show a modest but consistent shift toward positive net charge per residue (NCPR) relative to PDB* sequences, which are centered slightly negative (Fig. 5c). Both distributions remain narrow and overlapping near zero, indicating that neither class is strongly net-charged on average, though the shift is consistent with the established role of electrostatic interactions in mediating phase separation.

  Amino acid composition analysis (Fig. 5d) reveals that LLPS+ GPT sequences are enriched in polar residues and are depleted in aliphatic residues relative to PDB* GPT, while aromatic residue content is low and comparable in both, a feature inherited from the training data25 and consistent with recent findings that aromatic residues are not strictly required for LLPS.15 Anionic and cationic residue fractions are broadly similar between the two sets, with a slight enrichment of anionic residues in PDB* GPT sequences.

  Collectively, these analyses reveal stark differences between sequences constituting disordered proteins prone to LLPS and those of folded, non-phase-separating proteins. High disorder ensures conformational flexibility and solvent-exposed residues needed to sample the multivalent, transient interactions that drive condensate formation, rather than folding into a fixed hydrophobic core. Near-zero NCPR reflects a balance of anionic and cationic residues that supports electrostatic complementarity and transient charge–charge contacts between chains without net repulsion that would disfavor self-association. A higher fraction of polar residues further promotes weak interactions characteristic of the low-affinity, multivalent contacts that underlie liquid–liquid phase separation, as opposed to the specific, high-affinity packing that stabilizes folded structures. Together, these features suggest that sequences generated by LLPS+ GPT are condensation-prone. Confirming this requires direct computational and experimental investigation into their condensation tendencies, which we address next.


### Validation of phase separation tendency for sequences generated by LLPS+ GPT
  Sequence lengths in the training dataset span 69–1337 residues, with the majority exceeding 400 residues. Full-length validation at this scale is impractical. Phase-coexistence simulations of long, disordered chains are computationally expensive, and experimental synthesis of long, aggregation-prone peptides at the purity required for monomeric starting material is not currently feasible. We therefore assessed phase-separation propensity across three length regimes: short peptides (20–25 residues), for which experimental assessment was performed; intermediate-length peptides (60–80 residues) and longer peptides (120–180 residues), both assessed computationally only, to probe trends closer to the training-set length distribution than experimental validation currently allows. To this end, we generated 32 000 sequences spanning 20 to 200 residues (see Methods) and filtered them by length regime for validation. Details are provided in the respective subsections.

  To quantify phase-separation tendency from the concentration profiles obtained from our slab simulations using a single scalar, we calculate the Gini coefficient (Cg) of each profile:1where ci and cj denote the concentration in bins i and j along the slab's elongated (z) dimension, n is the number of bins, and c̄ is the mean bin concentration. Cg is bounded between [0, 1], where 0 denotes a spatially uniform (non-phase-separated) profile and 1 denotes the highest possible phase-separation tendency (not achievable in practice, as it would require the entire density to collapse into a single bin). We benchmark all sequences against the hnRNPA1 low-complexity domain (A1-LCD), a well-documented, strongly phase-separating protein used as a positive control in all simulations. A Cg value comparable to that of A1-LCD indicates a very high phase-separation tendency, whereas a low but non-zero Cg value indicates a phase-separation propensity that could not be fully captured under the simulation conditions (298.15 K, 150 mM NaCl-equivalent ionic strength, pH 7.4).


#### Short peptides (20–25 residues)
  With experimental validation in mind, we filtered the pool of 32 000 generated sequences (Methods) for those with lengths between 20–25 residues. From this subset, we retained sequences with disorder probability >0.5, rank-ordered them by SCD and pseudo-SHD (see Methods) scores, and selected five sequences (seq-0–seq-4) based on their feasibility for solid-phase peptide synthesis. These sequences are provided in the FASTA format in SI file S3.

  We synthesized seq-0–seq-2 at ≥87% purity from GenScript, USA; seq-3 was obtained via solid-phase peptide synthesis at ∼70% purity; and seq-4 was obtained from Galore TX, India at >95% purity (Fig. S4–S8). CD spectra confirmed that all five peptides adopt disordered conformations in solution (Fig. S9). Turbidity and DIC microscopy assays at 1 mM peptide in 1× PBS revealed clear condensation signatures for four of the five sequences (Fig. 6). seq-0 and seq-1 each formed abundant micron-scale, spherical droplets with steadily rising OD600 over the full 24 hour observation window, with seq-1 ultimately overtaking seq-0. seq-2 likewise formed micron-scale droplets but plateaued at a lower OD600 considerably more rapidly, suggesting weaker overall condensation propensity. seq-3, despite its reduced purity, exhibited the strongest turbidity signal of the four, roughly ten-fold higher than the others, with DIC imaging showing larger, irregular, partially coalesced assemblies rather than the more uniform droplets seen for seq-0–seq-2. However, because impurities can contribute to turbidity and irregular assemblies, this result is qualitative. seq-4 showed no detectable condensation under these conditions.

  Therefore, four of the five sequences undergo phase separation. While this is promising, it represents a statistically small sampling of the LLPS-forming sequence space. We therefore explore how longer sequences fare with regard to condensation propensity. We note, however, that the droplet morphologies observed here are consistent with liquid-like condensates, though definitive confirmation of liquid-state properties (e.g., via fluorescence recovery after photobleaching or reversibility assays) would require additional experiments beyond the scope of this initial demonstration.


#### Intermediate-length peptides (60–80 residues)
  To probe phase-separation propensity at a longer length scale than the short-peptide set, we filtered sequences within the 60–80 residue length range for disorder probability >0.5 and selected the top 60 sequences. The sequences are provided in the FASTA format in SI file S4.

  We performed phase-coexistence simulations for these 60 sequences and A1-LCD using the same CALVADOS-3 (ref. 33) protocol described in Methods (concentration profiles in Fig. S10; Cg values in Table S1). The Cg values are plotted in Fig. 7.

  Before interpreting these results, we note a key limitation of CALVADOS-based simulations: they carry significant errors in estimating the free energy of condensation,34 which in turn affects the accurate estimation of critical solution temperatures (Tc) and saturation concentrations (csat values). Under these conditions, only relative phase-separation tendencies can be meaningfully compared, irrespective of the true underlying propensities and actual simulation outcomes. We therefore benchmark against A1-LCD. Sequences exhibiting a Cg comparable to A1-LCD are very strongly phase-separating. However, a low Cg value does not necessarily indicate an inability to phase separate; instead, it may reflect proximity to the sequence's own Tc under our simulation conditions, rather than a genuine absence of phase-separation propensity.

  Fig. 7 shows that two sequences, seq-0 (Cg = 0.83) and seq-2 (Cg = 0.81), are on par with A1-LCD, indicating strong predicted phase-separation tendency; the remaining 58 sequences have Cg ≤ 0.13 suggesting comparatively weaker condensation propensity.


#### Longer peptides (120–180 residues)
  To complement the shorter-sequence sets and probe trends closer to the training-set length distribution, we performed a further computational-only assessment restricted to sequences within the 120–180 residue length range. Within this window, sequences were first filtered for a DeePhase25 score >0.9 and a predicted disorder score >0.9. Among the sequences passing this filter, we selected the top 10 with the highest SCD scores, the top 10 with the highest pseudo-SHD scores, and the top 10 with the highest combined SCD + pseudo-SHD scores, in each case rank-ordering sequences by the relevant criterion before selection. After removing duplicates across these three rankings, 29 unique sequences remained. The sequences are provided in the FASTA format in SI file S5.

  We performed phase-coexistence (slab) simulations for these 29 sequences and A1-LCD using CALVADOS-3 as described in Methods. The concentration profiles are shown in Fig. S11. From those concentration profiles, Cg was calculated and plotted for all 29 sequences in Fig. 8 and Table S2. 10 sequences show phase separation tendency greater than or on par with A1-LCD.

  Together, these three complementary assessments show that sequences generated by the trained model are consistently disordered and disorder-prone which precisely are the features the training set was built upon, and which the model reliably reproduces. Phase-separation propensity, however, varies across generated sequences and across length regimes, underscoring the value of computational screening to prioritize candidates before committing to resource-intensive experimental validation. In this way, our model, combined with complementary computational techniques, offers a route to the rapid generation of novel, condensation-prone IDPs across the length scales we could feasibly assess.


### Sequences from PDB* GPT adopt stably folded conformations
  As a complementary control, we tested whether PDB* GPT generates sequences with the intended folded-protein character. We randomly selected one 67-residue PDB* GPT-generated sequence:

  1 – HNCILYTEGCRWGLIPNMNLNDVRDWWRYWWP – 32.

  33 – MGPLLLHEWTSLKPPNWPLPEPESYTLLFHLEWYL – 67.

  AlphaFold 2.0 35 predicted a well-defined folded conformation for this sequence, which we used as the starting structure for a 1 µs all-atom MD simulation (see Methods). The protein remained stably folded (Fig. 9a), with an RMSD plateau of 0.51 ± 0.03 nm over the final 500 ns (Fig. 9b). This result validates that PDB* GPT generates sequences encoding the structural constraints of folded proteins. In conjunction with the LLPS+ GPT condensation results, this confirms that the two models have internalized the distinct molecular grammars of their respective training classes.


## Conclusion
  This study demonstrates that compact, task-specific generative models can learn and exploit the compositional grammar of liquid–liquid phase separation from small, curated datasets. Three principal findings emerge.

  First, LLPS+ GPT internalizes higher-order sequence correlations—not merely global amino acid frequencies—sufficient to reproduce length-dependent trends in hydropathy, charge decoration, disorder probability, and compositional entropy across the full range of training-set lengths. This indicates that the model captures the same physicochemical constraints that distinguish LLPS-prone IDPs from folded proteins.

  Second, the dominant mode of sequence generation is chimeric recombination: 87.3% of LLPS+ GPT-generated sequences contain one or more segments matching natural proteins, embedded in otherwise novel sequence, and none of these chimeric sequences is a full-length copy of a natural protein. This chimeric architecture suggests that the model has learned to compose sequences using short natural-like segments embedded in novel sequence in a manner consistent with current biophysical understanding of condensate-driving interactions. By contrast, all of PDB* GPT-generated sequences show no detectable homology to any catalogued protein, yet a representative sequence remains stably folded throughout a 1 µs all-atom simulation—demonstrating that both models have learned to generate sequences encoding the physicochemical constraints of their respective training classes.

  Third, five short sequences (20–25 residues) were tested experimentally, without prior phase-coexistence simulations; four of these show experimental signatures of condensation under near-physiological buffer conditions. Separately, across two computational screens spanning intermediate (60–80 residues, n = 60) and longer (120–180 residues, n = 29) length ranges, the simulated sequences show a broad range of phase-separation tendencies, with 12 of the 89 comparable to or exceeding the A1-LCD reference. The remaining sequences have Cgs that indicate weaker phase-separation tendency than A1-LCD under the simulated conditions.

  More broadly, these results conform to the present literature, which suggests that fine-tuning large, general-purpose PLMs may not always be necessary or even optimal for biological tasks defined by small, specialized datasets.22–24 A model with ∼17 M parameters trained on 137 sequences can learn meaningful molecular grammar, provided the training data are well-curated and the architecture is appropriately matched to the task, as established by our hyper-parameter optimization. Fine-tuning a considerably larger, general-purpose PLM on this same small dataset would likely be far more prone to overfitting and memorization, given that increasing depth degraded validation loss, and widening beyond d = 1024 gave no further gain. This finding has implications beyond LLPS, suggesting that compact generative models may be effective for other biological design tasks where curated datasets are small but information-rich.

  We also note that our experimental validation is restricted to short peptides (20–25 residues) at millimolar concentrations, and that even our expanded computational validation remains well short of the upper end of the training-set length distribution (up to 1337 residues). Additionally, definitive confirmation of liquid-like condensate properties through experimental approaches such as fluorescence recovery after photobleaching and reversibility assays, or computational approaches such as multi-chain slab simulations of droplet fusion and coalescence will further strengthen the connection between generated sequences and functional biomolecular condensates.

  Together, these advances establish a foundation for systematically probing the sequence grammar of LLPS and open avenues for rational, AI-guided design of condensates for biomaterials and therapeutic applications.


## Methods

### Training datasets for PLMs
  We utilized the previously reported LLPS+ and PDB* datasets.25 The LLPS+ dataset encompasses 137 amino acid sequences of intrinsically disordered proteins (IDPs) with critical/saturation concentrations ≤100 µM. The PDB* dataset consists of 1562 folded proteins that do not spontaneously undergo liquid–liquid phase separation (LLPS) under normal conditions. We employed character-level tokenization, yielding a vocabulary of: ACDEFGHIKLMNPQRSTUVWXY<blank space>.


### Tokenization and embedding
  We employed character-level tokenization (Table 1). Two embedding layers—token and positional—both built with PyTorch's nn.Embedding, map each amino acid and its sequence position into vectors whose sum gives the final input representation.


### GPT model details
  We employ a decoder-only GPT model (Fig. 1a) with an embedding dimension of Dembed = 1024, 2 layers of multi-headed self-attention each with 2 attention heads (Nl = 2, Nh = 2), and a context window of 128 residues. This architecture was selected via a search over embedding dimension, number of layers, and number of attention heads, performed on a fixed, length-stratified train/validation partition. Given that increasing depth beyond two layers degraded validation loss, and widening beyond d = 1024 gave no further gain (Table S3) the chosen configuration achieved the lowest absolute validation loss among all tested configurations. See SI Methods, SI Results 2.2–2.4, Table S3 and Fig. S12–S15 for details.


### Comparison with a baseline LSTM model
  To create a baseline for the attention based language model, we train an LSTM based model including position and token embeddings as its part. With the same 1024 embedding dimension, we adjusted the hidden dimensions and the number of layers of the LSTM model to generate a ∼17.8 M parameter model. This was performed so as to have a baseline model with the number of parameters comparable to the GPT-based model. Fig. S16 shows that the LSTM based model performs worse than the GPT-based one, indicating that attention improves the model's ability to capture the underlying sequence grammar. More details can be found in SI Results 2.5.


### Training details for PLMs
  All models were trained on a single NVIDIA RTX A5000 ampere GPU (24 GB VRAM) running Ubuntu 22.04 with an AMD Ryzen 7 5800 CPU and 128 GB system memory. We trained all models for 85 epochs using a batch size of 64 sequence chunks each with 128 tokens, cross-entropy loss (eqn (2)), and the AdamW optimizer36 with a learning rate of 1 × 10−5 (see SI Results for more details). The optimum number of epochs was determined via length-stratified 10-fold cross-validation on a fixed reference partition, identifying the point at which validation loss began to systematically diverge from training loss across folds (SI Results, Sections 2.2–2.4).2


### Generation of sequences from the PLMs
  Two distinct generation procedures were used, differing in whether sequences were stratified by length.


#### Length-stratified generation
  For the length–ablation analysis, homology/novelty classification, and physicochemical feature comparisons, we generated 3200 sequences per model (LLPS+ GPT and PDB* GPT) as follows:

  1. Partition the training-set length distribution into 50 bins, and sample a target length uniformly at random within a bin.

  2. Seed the sequence with a uniformly chosen standard amino acid.

  3. Feed the current sequence (truncated to the last 128 residues) into the GPT model.

  4. Generate the next token via multinomial sampling.

  5. Repeat steps 3–4 until the target length is reached.

  6. Remove blank-space tokens and X residues.

  7. Replace any U residues with C.

  Steps 1–7 are repeated 64 times per bin, yielding 3200 sequences each for LLPS+ GPT and PDB* GPT.

  Unstratified generation for candidate selection: For downstream computational and experimental validation, length stratification was not required; instead, we prioritized generating a large pool of sequences from which to select high-confidence candidates. We generated 32 000 sequences using the same procedure above, except that in step 1 a target length was drawn uniformly at random from the interval [20, 200] residues for each sequence, rather than from a length-stratified bin. Candidate sequences for computational and experimental validation were subsequently selected from this pool as described in Section 2.6.


### Sequence homology analysis
  Homology searches were performed using DIAMOND BLASTp30,31 against two reference databases: the SwissProt protein database, obtained from UniProt,32 and a custom BLAST database constructed from the LLPS+ training sequences. For each search, we applied an E-value threshold of 10−3. Generated sequences were classified into one of four categories:

  • Novel: no BLAST hit meeting the E-value threshold in either database.

  • Chimeric: no single hit accounts for the full query (coverage and identity ≥90% to one subject), but one or more non-overlapping fragments (≥8 aa, ≤10 aa overlap tolerance) match natural sequences in SwissProt or the training set. The remaining residues have no detectable match, so the sequence is a combination of natural-like segments and novel sequence.

  • Reproduced natural: a single SwissProt hit spans the full query length, but the sequence is absent from the training set.

  • Memorized: a full-length, near-identical match to a training-set sequence.


### Pseudo sequence hydropathy decoration (pseudo-SHD)
  To quantify the linear patterning of hydropathy along a sequence, we defined the pseudo sequence hydropathy decoration (pseudo-SHD) by analogy with the sequence charge decoration (SCD).37 Each residue i was assigned a hydropathy value hi by linearly rescaling the Kyte–Doolittle (KD) scale38 to the interval [−1, 1].

  Using the functional form of the SCD, as implemented in localcider,28 the pseudo-SHD of a sequence of length N is3

  Positive pseudo-SHD values indicate that residues of similar hydropathy are clustered along the chain, whereas negative values indicate that hydrophobic and hydrophilic residues are interspersed.


### All-atom molecular dynamics simulation details
  All-atom MD simulations were run in GROMACS 2023.2 (ref. 39 and 40) using the CHARMM36m force field41 and modified TIP3P water.42 Electrostatics were treated with PME43 and Lennard-Jones interactions with a 1.2 nm Verlet cutoff;44 protein hydrogen bonds were constrained via LINCS45 and water via SETTLE.46 Systems were solvated, neutralized with Na+/Cl−, and adjusted to 100 mM NaCl. After energy minimization, we performed 100 ps each of NVT and NPT equilibration (2 fs timestep) at 310.15 K and 1 bar using the v-rescale thermostat47 and c-rescale barostat,48 then carried out production runs with a 2 fs timestep.


### Phase co-existence molecular dynamics simulation details
  We perform phase-coexistence (slab) simulations using the CALVADOS-3 force field33 in the NVT ensemble. The simulation box has dimensions Lx = Ly = 12 nm and Lz = 150 nm. Simulations are run at 298.15 K and an ionic strength equivalent to 150 mM NaCl. Following standard CALVADOS protocol,49 we use a 10 fs timestep, a Langevin integrator, and a friction coefficient of 0.01 ps−1. Each system is initialized with 200 copies of the peptide distributed evenly across the simulation box, followed by energy minimization. This is followed by 15 ns of simulation under a biasing potential that pulls all particles toward the box center along the z-dimension only, promoting initial slab formation. A subsequent 500 ns of unbiased molecular dynamics is performed, with configurations saved every 0.1 ns. Four replicate simulations are run for each of the 89 sequences, and the last 1000 frames of each resulting trajectory are used for downstream analysis. As a positive control, the 137-residue IDP from the hnRNPA1 low-complexity domain (A1-LCD) is simulated using the same protocol.


### Materials
  seq-0, seq-1, and seq-2 were purchased from GenScript (New Jersey, USA) with purity ≥87%, with N- and C-terminal acetylated and amidated, respectively. seq-3 was chemically synthesized via solid-phase peptide synthesis (SPPS) with N- and C-terminal acetylated and amidated; the maximum achievable purity was ∼70%. seq-4 was purchased from Galore TX (Bengaluru, India). The mass of each peptide was confirmed by MALDI-TOF-MS (Shimadzu MALDI-8030; 500 scans per run, laser power 20 mV) using α-cyano-4-hydroxycinnamic acid matrix (Bruker Daltonics, MA).


### Turbidity assay
  The absorbance of 1 mM peptide solutions (1× PBS, pH 7.4) was measured at λ = 600 nm using a BioTek Synergy H1 Microplate Reader over 24 h. Readings were taken at 30 min intervals with 5 s orbital shaking before each measurement. Each data point represents biological replicates of two days with n = 3.


### DIC microscopy
  Condensation behavior of 1 mM peptides in 1× PBS was examined using a Leica DMC4500 microscope in reflection mode with differential interference contrast (DIC) and a 20× optical zoom lens. Images were acquired with a DMC4500 camera under LEICA LAS X software (Version 3.4.2).


### CD spectra measurement
  CD spectra were recorded on a Jasco J-815 spectrometer. Spectra (average of 3 scans) were collected from 200 to 260 nm with 1.00 nm bandwidth and 0.5 nm step size. Solvent (1× PBS) background was subtracted from each spectrum of 0.25 mM peptide.


### List of software
  All simulations were performed using GROMACS.39,40 Snapshots were generated using PyMOL 2.5.4.50 Analyses were performed using Python51 and MDAnalysis.52,53 Figures were prepared using Matplotlib,54 Jupyter,55 and Inkscape.56 All deep neural network models were built using PyTorch.57


## Author contributions
  Abdul Wasim: conceptualization, methodology, software, formal analysis, data curation, visualization, writing. Ushasi Pramanik: investigation and analysis (experiments), validation, writing. Anirban Das: investigation and analysis (experiments), validation, writing. Pikaso Latua: investigation (experiments). Jai S. Rudra: supervision (experimental work), resources, funding acquisition, project administration (experimental work), writing. Jagannath Mondal: conceptualization, methodology, supervision, project administration, funding acquisition, resources, writing.


## Conflicts of interest
  The authors declare no conflicts of interest.


## Supplementary Material

## Data availability
  The scripts and models used to train GPT models and predict sequences have been uploaded to GitHub (https://github.com/SerpentByte/LLPS-plus-GPT). SI files S1–S5 can be found in the GitHub repository as well. A Google Colab notebook for generating new sequences is available here (https://tinyurl.com/3kmy5xbt).

  Supporting information: SI methods: §1.1 GPT model details, including the multi-headed self-attention formulation, causal masking and final architecture. SI results: §2.1 screening of the LLPS+ and PDB* training sets for seven established LLPS-associated motif classes, with an unbiased k-mer enrichment scan and hydrophobic-moment autocorrelation analysis of PDB*, and Table R1 giving motif prevalence across the 137-sequence LLPS+ training set; §2.2 length-stratified 10-fold cross-validation and selection of fold-0 as the fixed reference partition; §2.3 grid-search hyper-parameter optimization over heads, layers and embedding dimension, and determination of the 85-epoch training budget; §2.4 seed-stability analysis across five random seeds, with Jensen–Shannon divergences between the resulting phase diagrams; §2.5 comparison against a parameter-matched LSTM model trained on the same fold-0 split. SI Tables: Table S1 Gini coefficients for the 60 screened 60–80 residue sequences; Table S2 Gini coefficients for the 29 screened 120–180 residue sequences; Table S3 minimum validation and corresponding training losses for all tested architecture configurations. SI Figures: Fig. S1 UMAP projections of ProtT5-XL embeddings for UniRef50, LLPS+ and PDB* sequences; Fig. S2 extended length-ablation analysis for LLPS+ GPT; Fig. S3 length-ablation analysis for PDB* GPT; Figs. S4–S8 MALDI-TOF mass spectra for the five synthesized peptides; Fig. S9 circular dichroism spectra for seq0–seq4; Fig. S10 and S11 concentration profiles along the elongated dimension z for the 60–80 and 120–180 residue generated sequences, respectively; Fig. S12 and S13 cross-entropy loss and perplexity versus epochs across the ten dataset splits at the initial and optimized architectures, respectively; Fig. S14 the same across five random seeds; Fig. S15 Das–Pappu-style FCR vs. |NCPR| plots for the training data and each seeded model; Fig. S16 training and validation losses for the LSTM and GPT models. See DOI: https://doi.org/10.1039/d6sc03816f.


## Acknowledgements
  We thank Prof. Anand Srivastava and Mr Santosh Prajapati for insights on phase-coexistence simulations, Dr Aneesh Tazhe Veetil for guidance on experiments, and Prof. Kalyaneshwar Mandal and Mr Anandhmuthiah V for discussions on LLPS propensities. We acknowledge support of the Department of Atomic Energy, Government of India, under Project Identification No. RTI 4007. J. M. acknowledges Core Research Grants from the Department of Science and Technology (DST) of India (CRG/2023/001426). The studies in the Rudra Lab were supported by WashU start-up funds.