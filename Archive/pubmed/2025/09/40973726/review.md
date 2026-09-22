## Review setup
- **Input scope** Full manuscript text (abstract, introduction, results, discussion, methods) with figure legends and supplementary figure/table references; no raw data files, no supplementary information files, no source data.
- **Assessment boundary** Scientific content, experimental design, data interpretation, and claims as presented in the provided text. No assessment of editorial quality, formatting, or literature coverage beyond what is visible.
- **Shared manuscript claim summary** The authors propose that transient contacts between the intrinsically disordered N-terminus (NT) of the neuropeptide Y2 receptor (Y2R) and its peptide ligand NPY regulate arrestin-3 recruitment, but not Gi protein activation. Using cross-linking mass spectrometry (XL-MS), molecular dynamics (MD) simulations, and functional assays, they identify acidic clusters in the NT that electrostatically control the conformational ensemble, prolong ligand residence time, and thereby modulate arrestin-3 binding.
- **Visible evidence base** XL-MS data (40 cross-links, 34 to extracellular regions, 16 to NT), competition experiments, isolated NT peptide XL-MS, NMR chemical shift perturbations, AlphaFold2/Rosetta modeling with cross-link constraints, 10 × 1 µs MD simulations, BRET-based Gi1/GoA activation assays, arrestin-3 recruitment assays, NanoBRET ligand binding assays, live-cell microscopy, and mutagenesis data (neutral, charge-reversal, deletion, and membrane-proximal mutants).
- **Missing materials affecting confidence** Supplementary figures (1–12), Supplementary Tables (1–7), Supplementary Data 1, raw mass spectra, MD trajectory files, and source data. These are referenced but not provided, limiting verification of key quantitative claims.

## Reviewer

- **Overall assessment** This manuscript addresses a genuinely under-explored question in GPCR biology: the functional role of the intrinsically disordered N-terminus in a peptide-activated receptor. The combination of XL-MS, MD simulations, and functional assays is ambitious and appropriate. The data support a nuanced model in which the NT contributes to ligand residence time and arrestin-3 recruitment without strongly affecting Gi activation. However, several claims outpace the visible evidence, particularly regarding the electrostatic mechanism, the causal link between residence time and arrestin-3 recruitment, and the structural interpretation of the membrane-proximal mutants. The manuscript is technically sophisticated but would benefit from clearer presentation of controls and quantitative rigor in places.

- **Who would be interested in the results, and why** GPCR biologists studying arrestin-biased signaling, researchers interested in intrinsically disordered regions in membrane proteins, and structural biologists using XL-MS to study dynamic protein complexes. The work also has relevance for drug discovery efforts targeting NPY receptors, where understanding ligand residence time and arrestin recruitment could inform therapeutic design.

- **Major strengths**
  1. The study addresses a previously intractable question with a well-integrated multi-technique approach.
  2. The XL-MS data are extensive and include competition experiments and independent validation with an isolated NT peptide.
  3. The functional assays cover multiple readouts (BRET, IP accumulation, internalization) and include appropriate controls for expression levels.
  4. The MD simulations are long (10 × 1 µs) and appear well-designed to sample the disordered NT ensemble.
  5. The differential effects on Gi versus arrestin-3 are biologically interesting and potentially important.

- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Causal inference
- **Claim pointer** "Transient ligand contacts of the intrinsically disordered N-terminus of neuropeptide Y(2) receptor regulate arrestin-3 recruitment" (title) and "transient contacts of Y2R NT to NPY modulate recruitment of arrestin-3 to the receptor by prolonging ligand residence time" (abstract).
- **Evidence pointer** Results sections "XL-MS identifies direct interactions between NPY and Y2R NT", "Y2R NT modulates arrestin-3 binding, but not Gi activation"; Figures 4 and 5.
- **Concern** The causal chain from NT-NPY contacts to prolonged residence time to enhanced arrestin-3 recruitment is not directly demonstrated. The data show correlations: mutations that alter NT charge affect both residence time and arrestin-3 recruitment, and the NT makes contacts with NPY. However, no experiment directly manipulates residence time independently of NT structure, and no experiment shows that the specific cross-linked contacts are required for the residence time effect. The Δ2–41 deletion removes the entire flexible NT, which could affect receptor dynamics, oligomerization, or membrane interactions beyond simply removing the acidic patches. The charge-reversal mutants could alter the conformational ensemble in ways unrelated to the specific cross-linked contacts.
- **Why it matters** The title and abstract make a strong mechanistic claim. If the causal link is not established, the central conclusion of the paper is weakened. The distinction between "NT modulates arrestin-3 recruitment" (well supported) and "NT regulates arrestin-3 recruitment via transient ligand contacts that prolong residence time" (incompletely supported) is important for the field.
- **Resolution test** Provide an experiment that separates the contact-mediated effect from the electrostatic/ensemble effect. For example, a mutant that preserves NT charge but disrupts specific cross-linked contacts (e.g., alanine substitution at cross-linked NT residues) could test whether the specific contacts are required. Alternatively, a kinetic analysis of arrestin-3 recruitment at varying ligand concentrations that directly correlates residence time with recruitment amplitude across a panel of mutants would strengthen the causal link.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** No
- **Axis** Mechanistic interpretation
- **Claim pointer** "We speculate that the negatively charged patches from these acidic residues - due to their repulsive forces – might keep the ligand binding pocket of the Y2R NT in an 'open' conformation" (Results, "Conformational ensembles of the disordered Y2R NT").
- **Evidence pointer** Results section "Conformational ensembles of the disordered Y2R NT"; Figure 2; Supplementary Figure 7.
- **Concern** The electrostatic repulsion hypothesis is presented as speculation, which is appropriate, but the MD data are not shown to directly support this specific mechanism. The observation that acidic patches fluctuate around a mean distance of 24 Å does not demonstrate that repulsion keeps the pocket open. No control simulations with neutralized charges are described, and no analysis of the electrostatic potential or free energy landscape is presented. The functional data with charge-reversal mutants are consistent with an electrostatic effect, but the "open conformation" model is not directly tested.
- **Why it matters** The proposed mechanism is central to the model. If the electrostatic repulsion hypothesis is incorrect, the interpretation of the charge-reversal mutant phenotypes changes substantially. The field would benefit from a clearer distinction between the observed correlation and the proposed mechanism.
- **Resolution test** Perform MD simulations with the acidic residues neutralized (in silico) and compare the conformational ensemble, particularly the distance between the acidic patches and the accessibility of the ligand-binding pocket. Alternatively, use a biophysical probe (e.g., FRET or EPR) to measure NT conformation in the presence and absence of NPY for wild-type and charge-reversal mutants.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Quantitative rigor
- **Claim pointer** "The cross-links provide distance constraints for deriving structural models of the interaction" (Abstract) and "All distance constraints are fulfilled within a Cβ-Cβ distance of 13 Å" (Results, "Conformational ensembles of the disordered Y2R NT").
- **Evidence pointer** Results section "Conformational ensembles of the disordered Y2R NT"; Supplementary Figures 5 and 6; Supplementary Table 4.
- **Concern** The use of XL-MS distance constraints in modeling is described, but the validation of the resulting model is not fully presented. The statement that all constraints are fulfilled within 13 Å is encouraging, but it is unclear how many constraints were used, how the model selection was performed, and whether the model was validated against independent data (e.g., the cryo-EM structure). The AlphaFold2 model selection criteria (lowest RMSD to cryo-EM plus lowest cross-link distances) could introduce bias. The Rosetta refinement with constraints is described, but the convergence and reproducibility of the modeling are not discussed.
- **Why it matters** The structural model underpins the interpretation of the cross-links and the functional data. If the model is not robustly validated, the specific contacts identified may be artifacts of the modeling procedure rather than genuine features of the complex.
- **Resolution test** Provide a more detailed description of the modeling pipeline, including the number of constraints, the distribution of constraint violations, and a comparison of the final model to the cryo-EM structure in the regions that are resolved. Consider cross-validation by splitting the constraints into training and test sets.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Data interpretation
- **Claim pointer** "Charge reversal of the acidic clusters by mutation to lysine reduced the BRETmax to 49% for D35–E39NT, and 77% for E15–E20NT" and "for these two variants the BRET signal clearly decayed faster, starting after about 4 min, suggesting an overall destabilized complex" (Results, "Y2R NT modulates arrestin-3 binding, but not Gi activation").
- **Evidence pointer** Results section "Y2R NT modulates arrestin-3 binding, but not Gi activation"; Figure 4f, g; Supplementary Table 1.
- **Concern** The interpretation of reduced BRETmax as reduced recruitment and the decay as complex destabilization is reasonable, but alternative explanations are not fully excluded. Reduced BRETmax could also result from altered conformation of the arrestin-3-receptor complex (e.g., different orientation of the Nanoluc and YFP tags) rather than reduced recruitment. The decay could reflect receptor internalization, arrestin-3 ubiquitination, or other downstream events rather than complex destabilization per se. The authors do not present a direct measure of arrestin-3 binding (e.g., co-immunoprecipitation or total internal reflection fluorescence microscopy).
- **Why it matters** The differential effect on arrestin-3 versus Gi is a key finding. If the BRET changes reflect conformational differences rather than recruitment differences, the conclusion that the NT specifically modulates arrestin-3 recruitment would need revision.
- **Resolution test** Use an orthogonal assay for arrestin-3 recruitment, such as a complementation assay with a different readout, or measure arrestin-3 binding directly by co-immunoprecipitation. Alternatively, use a BRET assay with the Nanoluc and YFP tags in different positions to control for orientation effects.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Figure 1b
- **Evidence pointer** Results section "XL-MS identifies direct interactions between NPY and Y2R NT"; Figure 1b.
- **Issue** The figure legend states that each cross-link is represented by a green line, but the inset mentions that the majority of cross-links were found for L24NPY and L30NPY to Y2R NT. It is unclear how the cross-links to ECL2 are distinguished visually and whether the 16 NT contacts are all from L24 and L30 or also from L17.
- **Required correction** Clarify in the figure legend which cross-links correspond to which NPY position and how the NT versus ECL2 cross-links are visually distinguished.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Statistical reporting
- **Affected element** Figure 4g and Supplementary Table 1
- **Evidence pointer** Results section "Y2R NT modulates arrestin-3 binding, but not Gi activation"; Figure 4g; Supplementary Table 1.
- **Issue** The statistical analysis for the kinetic parameters (kobs) is not described in the text. It is unclear whether the comparisons are made against wild-type with appropriate multiple testing correction, and whether the n numbers for each variant are consistent.
- **Required correction** Provide a clear description of the statistical tests used, including the number of independent experiments for each variant and the correction method for multiple comparisons.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Completeness
- **Affected element** NMR experiments
- **Evidence pointer** Methods section "Solution NMR experiments"; Supplementary Figure 4.
- **Issue** The NMR experiments are described briefly, and the results are only mentioned in the context of confirming interactions. The specific residues of NPY that show chemical shift perturbations upon binding to the NT peptide are not listed, and the magnitude of the shifts is not quantified.
- **Required correction** Provide a summary of the NMR results, including the residues with significant chemical shift perturbations and the magnitude of the shifts, to allow comparison with the XL-MS data.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Interpretation
- **Affected element** Discussion of low-affinity binding state
- **Evidence pointer** Results section "Ligand binding at Y2R NT variants"; Figure 5.
- **Issue** The authors interpret the reduced low-affinity binding in the Δ2–41 variant as evidence for NT contribution to NPY binding. However, the Δ2–41 deletion also removes the N-terminal signal peptide region, which could affect receptor folding or membrane insertion. The authors note that the variant is expressed and trafficked, but a more detailed characterization of receptor conformation (e.g., by a conformation-sensitive antibody or by assessing NPY binding to a receptor with a scrambled NT sequence) would strengthen the interpretation.
- **Required correction** Discuss this alternative interpretation and, if possible, provide additional data to exclude it.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Reproducibility
- **Affected element** MD simulation details
- **Evidence pointer** Methods section "Molecular dynamics simulation"; Supplementary Tables 5 and 6.
- **Issue** The MD simulation methods are described, but the analysis of the trajectories is not fully detailed. Specifically, the contact frequency analysis (Figure 3) and the RMSD calculations (Figure 2) are not described in the methods, and the criteria for defining a "contact" are not stated.
- **Required correction** Add a description of the trajectory analysis, including the definition of contacts, the RMSD fitting procedure, and the software used for these analyses.

- **Concern ID** R1-m6
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Figure 5c
- **Evidence pointer** Results section "Ligand binding at Y2R NT variants"; Figure 5c.
- **Issue** The dissociation kinetics are shown for selected variants, but the figure legend does not specify which variants are shown and whether the data are representative or averaged. The text mentions "faster for Δ2–41 and acidic patch charge reversal mutants," but the quantification is not shown.
- **Required correction** Clarify the figure legend and provide quantification of the dissociation rates with appropriate statistics.

## Risk / unsupported claims
- The causal link between NT-NPY contacts, prolonged residence time, and enhanced arrestin-3 recruitment is not directly demonstrated (R1-M1).
- The "electrostatic repulsion keeps the pocket open" model is speculative and not directly tested (R1-M2).
- The structural model derived from XL-MS constraints is not fully validated (R1-M3).
- The interpretation of reduced BRETmax as reduced arrestin-3 recruitment is not confirmed by an orthogonal assay (R1-M4).
- The claim that the NT "regulates" arrestin-3 recruitment implies a regulatory role that is not fully distinguished from a permissive or modulatory role.
- The statement that "the NT engages in transient contacts to the peptide and prolongs ligand residence time, which is required for efficient interaction of Y2R with arrestin-3" is not fully supported, as the requirement is not demonstrated by a loss-of-function experiment that abolishes the contacts without other effects.
- The NMR data are described as confirming interactions, but the quantitative details are not provided, making the strength of this confirmation difficult to assess.
- The MD simulation contact frequencies are presented as supporting the cross-linking data, but the criteria for contacts and the statistical significance of the enrichment are not described.

## Assessment against Nature-style criteria
- **Originality** High. The study addresses a genuinely novel question about the functional role of an intrinsically disordered NT in a peptide-activated GPCR. The application of XL-MS to capture transient ligand-NT contacts is innovative.
- **Scientific importance** Moderate to high. The findings have implications for understanding GPCR signaling bias and the role of disordered regions in receptor function. However, the generalizability to other GPCRs is not established, and the mechanistic depth is limited by the correlative nature of some key claims.
- **Interdisciplinary readership** Moderate. The work will appeal to GPCR biologists, structural biologists, and researchers studying disordered proteins. The methods are specialized, but the conclusions are broadly accessible.
- **Technical soundness** Generally sound, but with gaps. The XL-MS and functional assays appear well-executed, but the modeling and MD analyses are not fully described, and the causal claims are not fully supported. The lack of orthogonal validation for the arrestin-3 recruitment data is a concern.
- **Readability for nonspecialists** Good. The manuscript is clearly written, and the figures are well-designed. The abstract and introduction provide sufficient context for a broad audience. The discussion is accessible and appropriately cautious in places.

## Recommendation posture
Supportive if technical concerns are resolved. The manuscript presents a novel and potentially important finding, but the central causal claim requires additional experimental support. Specifically, the authors should either (1) provide direct evidence that the specific NT-NPY contacts are required for the residence time and arrestin-3 effects, or (2) temper the claims to reflect the correlative nature of the data. The modeling and MD analyses should be more fully described and validated. With these revisions, the manuscript would be suitable for publication in a high-impact journal.