## Review setup
- **Input scope** Full manuscript text including summary, introduction, results, discussion, methods, and supplementary figure legends as provided.
- **Assessment boundary** Scientific content, experimental design, data interpretation, and claims as presented in the provided text. No external data or unpublished materials were consulted.
- **Shared manuscript claim summary** The authors propose that phosphorylation of the FASP serine cluster in PERIOD proteins leads to product inhibition of Casein Kinase 1δ (CK1δ), thereby stabilizing PER and lengthening circadian period. They support this with structural, biochemical, and cellular data, and extend the mechanism to Drosophila PER.
- **Visible evidence base** NMR-based kinase assays, ADP-Glo kinase assays, X-ray crystallography, molecular dynamics simulations, CRISPR-edited cell lines with circadian bioluminescence recordings, co-immunoprecipitation experiments, and Drosophila S2 cell assays.
- **Missing materials affecting confidence** Full figures and supplementary figures were not available for direct inspection. Statistical details for some experiments (e.g., exact n values, error bar definitions) are partially described but not fully verifiable. Structural validation metrics (e.g., Ramachandran statistics, B-factors) are referenced to Table 1 but not provided in the text.

## Reviewer
- **Overall assessment** This manuscript presents a compelling and mechanistically detailed model for how PER phosphorylation feeds back to inhibit CK1 activity, with structural and functional evidence spanning human and Drosophila systems. The work is technically rigorous and conceptually important for the circadian biology field. However, several claims regarding the in vivo relevance and quantitative impact of the feedback inhibition require further support or clarification.
- **Who would be interested in the results, and why** Circadian biologists studying post-translational regulation of clock proteins, kinase researchers interested in substrate-mediated enzyme inhibition, structural biologists studying kinase-peptide interactions, and researchers investigating conserved mechanisms of feedback regulation in signaling pathways.
- **Major strengths** 1) The combination of structural, biochemical, and cellular approaches provides multi-layered support for the proposed mechanism. 2) The identification of a conserved mechanism across mammals and Drosophila strengthens the biological significance. 3) The use of NMR to dissect sequential phosphorylation kinetics is elegant and informative. 4) The CRISPR-based approach in human cells directly links FASP phosphorylation to circadian period.
- **Major Concerns** See detailed items below.
- **Minor Comments** See detailed items below.
- **Technical failings that need to be addressed before the case is established** R1-M1 (in vivo relevance of feedback inhibition), R1-M2 (quantitative contribution of downstream phosphorylation sites), R1-M3 (structural evidence for full-length context).
- **Assessment against Nature-style criteria**  
  *Originality*: High. The concept of substrate-mediated product inhibition of CK1 by PER is novel and provides a new framework for understanding circadian period control.  
  *Scientific importance*: High. The mechanism is likely conserved and has implications for understanding how kinase activity is regulated in multi-site phosphorylation systems.  
  *Interdisciplinary readership*: Moderate to high. The work will appeal to circadian biologists, biochemists, and structural biologists, though the specialized nature may limit broader appeal.  
  *Technical soundness*: Generally strong, with appropriate controls and multiple orthogonal methods. Some concerns about quantitative interpretation and in vivo relevance remain.  
  *Readability for nonspecialists*: The manuscript is well-written but assumes familiarity with circadian biology and kinase mechanisms. The summary and introduction are accessible, but the results section is dense.
- **Recommendation posture** Supportive if technical concerns are resolved, particularly regarding the in vivo relevance of the feedback inhibition and the quantitative contribution of individual phosphorylation sites.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** In vivo relevance
- **Claim pointer** The authors claim that "limiting phosphorylation of the FASP serine cluster reduces product inhibition, decreasing PER2 stability and shortening circadian period in human cells." This is a central claim linking the biochemical mechanism to circadian behavior.
- **Evidence pointer** Results section "Circadian rhythms are shortened by small deletions in the conserved FASP region of PER"; Figure 6
- **Concern** The CRISPR-edited cell lines show shortened periods, but the authors do not directly demonstrate that this phenotype is due to loss of feedback inhibition rather than other effects of the deletions (e.g., altered protein stability, disrupted protein-protein interactions, or changes in subcellular localization). The deletions remove multiple amino acids, not just phosphorylation sites, and could have pleiotropic effects.
- **Why it matters** The central thesis of the paper is that feedback inhibition of CK1 by phosphorylated FASP is the mechanism controlling circadian period. Without direct evidence that the period shortening in the edited cells is specifically due to loss of feedback inhibition, the in vivo relevance of the proposed mechanism remains correlative.
- **Resolution test** Rescue experiments where feedback inhibition is restored (e.g., by expressing a phosphomimetic FASP peptide or a CK1 mutant that cannot bind the phosphorylated FASP) should restore normal period. Alternatively, a knock-in mutation that specifically disrupts FASP-CK1 binding without affecting other FASP functions would strengthen the claim.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** No
- **Axis** Quantitative contribution of downstream phosphorylation sites
- **Claim pointer** The authors state that "phosphorylation of C-terminal sites within the FASP region leads to product inhibition of CK1, reducing the overall rate of priming phosphorylation." They also show that mutations of downstream serines (e.g., S671A, S674A) shorten period.
- **Evidence pointer** Results section "Sequential phosphorylation of FASP leads to feedback inhibition of CK1"; Figures 3 and 6
- **Concern** The relative contribution of each phosphorylation site to feedback inhibition is not quantitatively assessed. The alanine mutants that limit phosphorylation to 2 or 3 sites show increased priming rates, but it is unclear whether the effect is additive, synergistic, or dominated by a single site. The period shortening in the S671A and S674A mutants is not compared to the S662A mutant in a way that allows ranking of site importance.
- **Why it matters** Understanding which phosphorylation events are most critical for feedback inhibition would inform models of circadian period regulation and could identify potential therapeutic targets for circadian disorders.
- **Resolution test** A systematic analysis where each serine is individually mutated to alanine (or phosphomimetic) and the effect on CK1 inhibition and circadian period is measured would clarify the hierarchy of site importance.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Structural evidence in full-length context
- **Claim pointer** The authors state that "co-crystal structures in conjunction with accelerated molecular dynamics simulations reveal how pFASP phosphoserines dock into conserved anion binding sites near the active site of CK1δ."
- **Evidence pointer** Results section "pFASP binds to CK1 via conserved anion binding sites to occlude the substrate binding cleft"; Figure 4
- **Concern** The crystal structures are of isolated FASP peptides bound to the CK1δ catalytic domain. It is not clear whether the same binding mode occurs in the context of full-length PER2, where the FASP region is flanked by structured CK1BD-A/B domains and other regions of the protein. The authors do not provide structural or biophysical evidence that the peptide-based structures recapitulate the full-length interaction.
- **Why it matters** The physiological relevance of the proposed binding mode depends on whether it occurs in the context of the full-length PER2-CK1 complex. If the flanking domains alter the conformation or accessibility of the FASP region, the proposed mechanism may not apply in vivo.
- **Resolution test** Mutations in the CK1 anion binding sites (e.g., R178C, K224D, R127E) should be tested in the context of full-length PER2 binding and inhibition assays. Crosslinking or hydrogen-deuterium exchange mass spectrometry could also be used to assess whether the peptide-based binding mode is preserved in the full-length complex.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Statistical reporting
- **Affected element** Figure 6 and Supplementary Figure 6
- **Evidence pointer** Results section "Circadian rhythms are shortened by small deletions in the conserved FASP region of PER"
- **Issue** The statistical comparisons for period differences between mutant and parental cell lines are described as using Student's t-test, but it is unclear whether multiple testing corrections were applied when comparing multiple mutant clones.
- **Required correction** Clarify whether corrections for multiple comparisons were applied, or state that individual comparisons were pre-specified.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Methodological clarity
- **Affected element** Molecular dynamics simulations
- **Evidence pointer** Methods section "Molecular dynamics"
- **Issue** The description of the Gaussian accelerated MD simulations lacks details on the force field parameters for the phosphoserine residues and the treatment of the Na+ ion. This limits reproducibility.
- **Required correction** Provide specific parameters for phosphoserine residues and the ion placement protocol, or cite the relevant parameterization studies.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Data availability
- **Affected element** Structural data
- **Evidence pointer** Methods section "Data and code availability"
- **Issue** The PDB accession codes for the new crystal structures are not listed in the text.
- **Required correction** Include the PDB accession codes for all deposited structures in the Data and code availability section.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Interpretation of structural data
- **Affected element** Figure 4f
- **Evidence pointer** Results section "pFASP binds to CK1 via conserved anion binding sites to occlude the substrate binding cleft"
- **Issue** The statement that the tau mutation "stabilizes an alternate conformation of the activation loop that sterically clashes with the 3pFASP binding mode" is based on a modeled structure, not an experimentally determined structure of the tau mutant with the peptide bound.
- **Required correction** Clarify that this is a modeled prediction and note the limitations of this approach.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Experimental design
- **Affected element** Drosophila experiments
- **Evidence pointer** Results section "The phosphorylated Drosophila PER-Short region binds CK1 to inhibit kinase activity"; Figure 7
- **Issue** The Drosophila experiments use a peptide-based approach and cell-based assays, but the authors do not test whether the S589A mutation affects circadian period in flies.
- **Required correction** Acknowledge this limitation and discuss whether the in vitro data are sufficient to support the claim of conservation.

## Risk / unsupported claims
- The claim that feedback inhibition of CK1 by pFASP is the primary mechanism controlling circadian period in human cells is not fully supported, as the CRISPR deletions may have pleiotropic effects beyond loss of feedback inhibition.
- The structural model of the tau mutant with 3pFASP is based on modeling, not experimental data, and should be presented as a prediction.
- The claim that the mechanism is conserved between mammals and Drosophila is supported by in vitro data but lacks direct in vivo validation in Drosophila.
- The quantitative contribution of individual FASP phosphorylation sites to feedback inhibition is not established.
- The relevance of the peptide-based structural studies to the full-length PER2-CK1 complex is not demonstrated.