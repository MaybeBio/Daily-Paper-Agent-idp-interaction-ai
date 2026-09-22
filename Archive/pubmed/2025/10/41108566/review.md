## Review setup
- **Input scope** Full manuscript text (abstract, introduction, results, discussion, methods, figure legends not provided)
- **Assessment boundary** Structural and functional claims regarding RIβ N3A motifs, allosteric crosstalk between cAMP and ATP, and the RIβ:C heterodimer structure
- **Shared manuscript claim summary** The authors report a new 3.7 Å crystal structure of an RIβ:C heterodimer obtained by co-crystallization with an AKAP peptide. They propose that the N3A motifs in RIβ mediate allosteric crosstalk between cAMP and ATP binding during PKA activation, and identify W260 as a dynamic sensor for cAMP-mediated activation.
- **Visible evidence base** Abstract, Introduction, Results (sections on AKAP binding effects, heterodimer structure, N3A motif characterization, allosteric hotspots), Discussion, Methods (purification, crystallization, structure solution, mass spectrometry), accession number (PDB 9O7V)
- **Missing materials affecting confidence** Figure panels referenced but not provided (Figures 1–6, S1–S10), Table S1 (crystallographic statistics) and Table S2 (functional residue analysis) not provided, no electron density maps or validation metrics beyond a brief statement, no experimental validation of W260 function (e.g., mutagenesis), no quantitative binding or activity data

## Reviewer
- **Overall assessment** The manuscript presents a new crystal structure of an RIβ:C heterodimer and proposes a mechanistic model for allosteric crosstalk between cAMP and ATP in PKA activation. The structural work appears technically sound at the level described, but the central claims regarding N3A-mediated allosteric communication and W260 as a dynamic sensor are largely inferential and lack direct experimental support. The comparison between the RIβ2C2 and RIβ:C structures is potentially valuable, but the absence of key figures, tables, and validation data limits the ability to fully assess the conclusions. The manuscript would benefit from additional functional experiments to substantiate the proposed mechanism.

- **Who would be interested in the results, and why** Structural biologists studying cAMP-dependent protein kinase and related signaling proteins; researchers investigating allosteric regulation in multidomain proteins; neuroscientists interested in RIβ function given its brain enrichment and links to neurodevelopmental disorders; medicinal chemists targeting PKA for therapeutic intervention in neurological conditions.

- **Major strengths** The manuscript addresses an understudied PKA regulatory subunit (RIβ) with clear biomedical relevance. The comparison between two RIβ-containing structures (holoenzyme vs. heterodimer) provides a basis for understanding conformational changes associated with nucleotide release. The identification of N3A motifs as stable multivalent interaction hubs is a conceptually useful framework. The authors acknowledge limitations and propose testable hypotheses.

- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence sufficiency
- **Claim pointer** The claim that the RIβ:C structure represents a distinct conformational state relevant to cAMP activation, with the rotation of W260 as "the first step in cAMP activation"
- **Evidence pointer** Results section "C-terminal tail in the RIβ subunit is disordered in the RIβ:C complex"; Figures 4 and 5 (not provided)
- **Concern** The manuscript presents a single crystal structure of a proteolyzed RIβ fragment (cleaved prior to the inhibitor site) co-crystallized with an AKAP peptide that is not visible in the density. The structure lacks ATP and has a disordered C-terminus. The authors interpret this as capturing an intermediate state in cAMP activation, but alternative explanations are equally plausible: the proteolysis itself may have destabilized the C-terminal regions, or the crystallization conditions (high ammonium sulfate, low pH) may have induced a non-physiological conformation. The claim that W260 rotation represents the "first step in cAMP activation" is speculative without supporting biochemical or biophysical data.
- **Why it matters** The central mechanistic conclusion of the manuscript rests on the interpretation of a single, potentially artifactual structure. Without functional validation, the claim that this structure captures a physiologically relevant activation intermediate is not established.
- **Resolution test** Provide evidence that the proteolyzed RIβ fragment retains functional properties comparable to full-length RIβ (e.g., cAMP binding affinity, inhibition of C-subunit activity). Alternatively, obtain a structure of full-length RIβ:C without proteolysis under similar conditions, or provide mutational analysis of W260 (e.g., W260A/F) demonstrating altered cAMP activation kinetics or cAMP binding affinity.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical validation
- **Claim pointer** The claim that the structure is well-determined and supports detailed mechanistic interpretation
- **Evidence pointer** Methods section "Data collection and processing" and "Structure solution and refinement"; Table S1 (not provided)
- **Concern** The structure is reported at 3.7 Å resolution, which is moderate for detailed mechanistic interpretation. The manuscript states that "density for many of the side chains is poorly resolved or missing" in the C-terminal tail, yet the authors make specific claims about side chain rotations (W260) and interactions (R366-E261). The crystallographic statistics (R-free, completeness, B-factors, Ramachandran outliers) are not provided in the main text, and Table S1 is not available for assessment. The molecular replacement used RIα(91-379):C as a search model, and the final model includes residues 91-366 of RIβ, but the quality of the density for the regions central to the claims is not documented.
- **Why it matters** The mechanistic conclusions depend on specific side chain conformations and interactions. At 3.7 Å resolution, side chain rotamers are often ambiguous, and the authors themselves note missing density for key residues. Without validation metrics and density maps, the structural basis for the proposed mechanism is not verifiable.
- **Resolution test** Provide Table S1 with complete crystallographic statistics, including R-free, resolution shells, B-factors, and coordinate error estimates. Show representative electron density (2Fo-Fc and Fo-Fc maps) for W260, R366, E261, and the N3A motifs in both the RIβ2C2 and RIβ:C structures. If side chain conformations are ambiguous at this resolution, temper the mechanistic claims accordingly.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Functional validation
- **Claim pointer** The claim that N3A motifs mediate allosteric crosstalk between cAMP and ATP, and that the linker regions play distinct roles in this process
- **Evidence pointer** Results sections "N-terminal and C-terminal linkers" and "Structural and functional characterization of the N3A motifs"; Figures 2, 3, and 5 (not provided)
- **Concern** The manuscript describes the N3A motifs as "stable multivalent hubs" and proposes specific roles for the N-terminal and C-terminal linkers in ATP sensing and cAMP gating, respectively. However, no functional experiments are presented to test these proposals. The only experimental data beyond the structure are Western blots showing RIβ expression and disulfide bonding in tissues (Figure S2) and mass spectrometry confirming proteolysis (Figure S10). The allosteric model is built entirely on structural comparisons between two different crystal forms.
- **Why it matters** Allosteric mechanisms require dynamic and functional evidence. Structural snapshots alone cannot establish that the observed conformational differences are causally related to cAMP/ATP binding or that they represent the pathway of activation. The field of PKA regulation has a rich history of biochemical and biophysical studies that could be leveraged to test these predictions.
- **Resolution test** Perform mutational analysis of key residues in the N3A motifs (e.g., N3AA hydrophobic core residues, N3AB interface residues) and the linker regions, and assess effects on cAMP binding affinity, ATP binding, holoenzyme stability, and activation kinetics. Use techniques such as isothermal titration calorimetry, surface plasmon resonance, or fluorescence-based activity assays. Alternatively, use hydrogen-deuterium exchange mass spectrometry or NMR to probe conformational dynamics in solution.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Interpretive rigor
- **Claim pointer** The claim that oxidation or AKAP binding causes nucleotide release, based on crystal soaking experiments
- **Evidence pointer** Results section "Effect of AKAP binding on the RIβ holoenzyme crystals"; Methods section "Soaking diamide, peptide, and cAMP into the crystals"
- **Concern** The authors state that adding diamide or AKAP peptide to crystals "led to the release of nucleotide" and caused crystals to dissolve. However, no data are shown for these experiments beyond a qualitative description. The original crystals diffracted to only 3.7 Å, and the soaked crystals were of even lower quality. The conclusion that oxidation or AKAP binding causes nucleotide release is inferred from crystal instability, which could have many causes (e.g., changes in crystal packing, pH shifts, or general destabilization).
- **Why it matters** This observation is presented as motivation for the co-crystallization strategy and contributes to the narrative that AKAP binding and oxidation are functionally linked to nucleotide release. If this claim is not well-supported, the rationale for the structural work is weakened.
- **Resolution test** Provide experimental data supporting nucleotide release upon oxidation or AKAP binding, such as nucleotide occupancy determined from crystal structures before and after soaking, or solution-based assays measuring ATP/cAMP dissociation in the presence of oxidants or AKAP peptides.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Abstract
- **Evidence pointer** Abstract, final sentence
- **Issue** The abstract states "we may have actually captured the first step in cAMP activation" which is appropriately hedged, but the title claims "N3A motifs in RIβ mediate allosteric crosstalk between cAMP and ATP in PKA activation" as an established fact. The title overstates the evidence presented.
- **Required correction** Consider revising the title to reflect the structural and hypothesis-generating nature of the work, e.g., "Structural insights into N3A motif-mediated allosteric crosstalk between cAMP and ATP in RIβ PKA activation."

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Results section "Effect of AKAP binding on the RIβ holoenzyme crystals"
- **Evidence pointer** Results, first paragraph
- **Issue** The description of the original RIβ2C2 structure and its features (D/D domain, C-tail packing) is brief and relies heavily on a previous publication. The relationship between the previous structure and the new one is not fully contextualized.
- **Required correction** Provide a more detailed comparison of the two structures, including a superposition figure or at least a quantitative measure of conformational differences (e.g., RMSD values for the C-subunit and RIβ regions).

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Methodology
- **Affected element** Methods section "Soaking diamide, peptide, and cAMP into the crystals"
- **Evidence pointer** Methods, soaking experiments
- **Issue** The methods for soaking experiments are described only briefly. No concentrations, incubation times, or success rates are given for the diamide and cAMP soaking attempts. The statement "no diffraction data were collected" for lower cAMP concentrations is ambiguous.
- **Required correction** Provide complete details of all soaking experiments, including the number of crystals tested, the range of conditions explored, and the outcomes. If these experiments were unsuccessful, state this explicitly and describe what was learned from the attempts.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Interpretation
- **Affected element** Discussion, paragraph on disease mutations
- **Evidence pointer** Discussion, final paragraph
- **Issue** The discussion mentions disease mutations in RIβ and RIα but does not map any specific mutations to the N3A motifs or the W260 region. The relevance of the structural findings to disease is asserted but not demonstrated.
- **Required correction** Either identify specific disease-associated mutations that map to the N3A motifs or W260 and discuss their potential impact, or temper the claim that these insights "may ultimately enable targeted therapeutic strategies."

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Data availability
- **Affected element** Data availability statement
- **Evidence pointer** Data availability statement
- **Issue** The data availability statement only references the previously deposited RIα structure (2QCS) and does not mention the new RIβ:C structure deposited as PDB 9O7V, despite the accession number being listed in the manuscript.
- **Required correction** Update the data availability statement to include the new structure (PDB 9O7V) and any associated experimental data.

## Risk / unsupported claims
- The claim that W260 rotation represents "the first step in cAMP activation" is unsupported by direct experimental evidence; it is an interpretation of a single crystal structure at moderate resolution.
- The claim that N3A motifs "mediate allosteric crosstalk between cAMP and ATP" is presented as a conclusion but is not tested functionally; it is a hypothesis derived from structural comparisons.
- The claim that oxidation or AKAP binding causes nucleotide release is based on qualitative crystal behavior and is not quantitatively supported.
- The statement that the RIβ:C structure "represents an RIβ:C heterodimer" formed from a proteolyzed fragment is accurate, but the physiological relevance of this proteolyzed state is unclear and not addressed.
- The claim that the N3A:N3A' dimer interface is "the major dimer interface" in the RIβ:C complex is based on crystal packing analysis, but the biological relevance of this interface is not experimentally validated.
- The assertion that the C-linker "shields the active site of the C-subunit from activation in the absence of cAMP" is a functional interpretation not directly tested.
- The statement that "the removal of ATP can also help to 'prime' W260 for recognition of the second cAMP" is speculative and not supported by experimental data.
- The relevance of the findings to disease mutations is asserted but no specific disease-associated mutations are mapped to the identified structural elements.