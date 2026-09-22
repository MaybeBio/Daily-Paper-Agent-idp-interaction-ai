## Review setup
- **Input scope** Full manuscript text including abstract, results, discussion, experimental procedures, and supporting information references.
- **Assessment boundary** Scientific content, methodological rigor, validity of claims, and alignment with stated conclusions. Editorial quality and formatting are not assessed.
- **Shared manuscript claim summary** The authors combine AlphaFold2 (AF2) structural predictions with circular dichroism (CD) spectroscopy and molecular dynamics (MD) simulations to generate models of the phagocyte NADPH oxidase (NOX2) complex, including its interactions with cytosolic subunits p47phox, p67phox, and Rac1. They propose that AF2 predicts an active-like conformation of the cytochrome b558 (cytb558) with a compact dehydrogenase (DH) domain, identify novel lipid interaction sites, and suggest specific roles for disordered regions in complex assembly and stabilization.
- **Visible evidence base** Abstract, full results section with figure descriptions, discussion, conclusion, and experimental procedures. Figures and tables are described but not directly viewable. Supporting information is referenced but not provided.
- **Missing materials affecting confidence** Actual figure images, supporting information files, MD simulation trajectories and analysis outputs, AF2 model confidence metrics (pLDDT scores per residue), and raw CD spectra. These are essential for fully evaluating structural claims and simulation quality.

## Reviewer
- **Overall assessment** This manuscript presents a computationally driven structural model of the phagocyte NADPH oxidase complex, integrating AF2 predictions with experimental CD data and MD simulations. The work addresses a biologically important and technically challenging problem, and the authors demonstrate thoughtful use of multiple computational tools. However, the central claims regarding the "active" conformation of cytb558 and the functional significance of specific interactions rest heavily on AF2 predictions that are not experimentally validated. The comparison with the cryo-EM structure 8WEJ is encouraging but limited, and the MD simulation analysis is presented at a descriptive level without quantitative rigor. The manuscript would benefit from clearer articulation of the novelty relative to existing experimental structures and from additional validation of the key structural findings.
- **Who would be interested in the results, and why** Researchers studying NADPH oxidase structure and function, particularly those interested in the molecular mechanisms of NOX2 activation and assembly. The work may also appeal to computational biologists using AF2 for multi-subunit membrane protein complexes and to investigators studying protein-lipid interactions in immune signaling. The methodological approach of combining AF2 with experimental filtering criteria could serve as a template for similar studies on other challenging membrane protein complexes.
- **Major strengths** 1) The study addresses a significant gap in understanding the full architecture of the phagocyte NADPH oxidase complex, which has been difficult to capture experimentally. 2) The authors thoughtfully integrate multiple computational methods (AF2, AF3, MD, PPM) with experimental data (CD spectroscopy, known biochemical constraints) to generate and filter structural models. 3) The comparison of AF2 predictions with subsequently published cryo-EM structures provides a valuable benchmark for the accuracy of AF2 on this system. 4) The identification of specific lipid interaction sites and the proposed role of disordered regions in complex assembly offer testable hypotheses for future experimental work.
- **Major Concerns** 
- **Minor Comments** 
- **Technical failings that need to be addressed before the case is established** R1-M1, R1-M2, R1-M3, R1-M4
- **Assessment against Nature-style criteria** **Originality**: Moderate. The application of AF2 to the NOX2 complex is novel, but the approach of combining computational predictions with experimental filtering is not new. The specific findings, such as the compact DH domain conformation and lipid interaction sites, are original but require experimental validation. **Scientific importance**: High. Understanding the structural basis of NOX2 activation is important for innate immunity and inflammatory disease. A reliable structural model of the full complex would be a significant advance. **Interdisciplinary readership**: Moderate. The work bridges computational biology, structural biology, and immunology, but the technical focus on AF2 and MD may limit accessibility to a broad audience. **Technical soundness**: The computational methods are generally appropriate, but the lack of quantitative validation for MD simulations and the reliance on AF2 confidence metrics without independent verification weaken the technical case. **Readability for nonspecialists**: The manuscript is clearly written but assumes familiarity with NADPH oxidase biology and computational structural biology. The abstract effectively summarizes the key findings, but the results section is dense and would benefit from more explicit connections between methods and conclusions.
- **Recommendation posture** Supportive if technical concerns are resolved. The manuscript presents a potentially valuable structural model, but the central claims require stronger validation and clearer presentation of quantitative evidence.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Validity of central claim
- **Claim pointer** The authors claim that "AF2 generated a model that does not correspond to cytb558 in its resting state" and that the DH domain position in the AF2 model resembles the active conformation observed in the cryo-EM structure 8WEJ.
- **Evidence pointer** Results section, "AF2-generated cytb558 model"; Figures 1 and 2
- **Concern** The central claim that AF2 predicts an active-like conformation of cytb558 is based on a comparison with a single cryo-EM structure (8WEJ) that was not available during AF2 training. The authors report a 17.6° deviation between the AF2 and resting (8GZ3) DH domain orientations, but the significance of this difference is not established. The comparison with 8WEJ is qualitative, and the authors do not provide a quantitative measure of similarity between the AF2 model and the active structure. Furthermore, the authors acknowledge that AF2 was trained on resting-state structures, so the prediction of an active-like state is surprising and requires stronger evidence. The claim that AF2 "modeled an active configuration" is not sufficiently supported by the data presented.
- **Why it matters** This claim is central to the manuscript's thesis that the AF2 model represents the active state of the enzyme. If this is not convincingly demonstrated, the entire structural model and its implications for activation mechanisms are called into question.
- **Resolution test** Provide a quantitative comparison (e.g., RMSD or domain-domain angle) between the AF2 model and the active cryo-EM structure 8WEJ, and demonstrate that the AF2 model is significantly closer to the active state than to the resting state. Additionally, discuss why AF2 would predict an active-like state given its training data, or provide independent evidence (e.g., cross-linking data, mutagenesis) supporting the active-like conformation.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness of MD simulations
- **Claim pointer** The authors state that "phosphorylation enhances the anchoring of both NOX2 and p47phox to the membrane" based on MD simulations comparing phosphorylated and unphosphorylated p47phox.
- **Evidence pointer** Results section, "Molecular dynamic simulations of the membrane-embedded cytb558-p47phox complex"; Figure 6
- **Concern** The MD simulation analysis is presented at a purely descriptive level. The authors report qualitative observations about lipid occupancy and residence times but do not provide quantitative data, statistical analysis, or error estimates. The claim that phosphorylation enhances membrane anchoring is based on a comparison of two 500 ns replicas per condition, which is a limited sampling time for such a large and complex system. No information is provided on the convergence of the simulations, the equilibration protocol, or the reproducibility of the observed interactions across replicas. The use of a single force field and the absence of control simulations (e.g., with mutated phosphorylation sites) further weaken the conclusions.
- **Why it matters** The MD simulations are used to support key claims about the role of phosphorylation in stabilizing the complex and the specific lipid interactions that anchor the complex to the membrane. Without quantitative and statistically robust analysis, these claims are not established.
- **Resolution test** Provide quantitative metrics (e.g., lipid occupancy percentages, residence times with standard deviations) for the key interactions in both phosphorylated and unphosphorylated conditions, with statistical testing to demonstrate significant differences. Include convergence analysis (e.g., RMSD over time, block averaging) and consider additional replicas or extended simulation times to ensure robustness.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Validity of model selection criteria
- **Claim pointer** The authors selected the "best" AF2 model based on "two consensual criteria described in the literature" for p47phox-cytb558 interactions: (i) interaction of the PRR region of p22phox with the SH3 of p47phox, and (ii) orientation of the PX domain towards the membrane.
- **Evidence pointer** Results section, "AF2-generated model of cytb558 with p47phox"; Table 1
- **Concern** The model selection criteria are presented as if they are well-established, but the authors do not critically evaluate the strength of the evidence for these criteria. The references cited in Table 1 include a mix of functional studies, mutagenesis data, and structural predictions, but the authors do not assess the reliability of each criterion. Furthermore, the authors acknowledge that "we cannot exclude that they could represent transitional/primarily interacting forms" for the discarded models, which raises the question of whether the selected model is truly representative or simply the one that best matches prior expectations. The selection process is therefore circular to some degree, as the model is chosen based on criteria that are themselves derived from the same body of literature the model is meant to explain.
- **Why it matters** The validity of the final structural model depends on the objectivity and robustness of the selection criteria. If the criteria are biased or incomplete, the model may not accurately represent the biologically relevant conformation.
- **Resolution test** Provide a more systematic and transparent model selection procedure, including a scoring scheme that weights different criteria based on the strength of experimental evidence. Discuss the possibility of multiple biologically relevant conformations and how the selected model relates to them. Consider validating the selected model against additional experimental data not used in the selection process.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** Yes
- **Axis** Support for functional claims
- **Claim pointer** The authors propose that specific regions of p47phox, particularly the Trp80-Phe81 residues of the PX domain, are involved in membrane anchoring and that the C-terminus of p47phox interacts with the 491-500 loop of NOX2, with functional implications for complex assembly and activation.
- **Evidence pointer** Results section, "AF2-generated model of cytb558 with p47phox" and "Molecular dynamic simulations"; Figures 4, 5, and 6
- **Concern** The functional significance of the identified interactions is inferred primarily from the structural models and MD simulations, without direct experimental validation. For example, the claim that the Trp80-Phe81 hydrophobic insertion is important for membrane anchoring is based on the observation of this interaction in the model and simulations, but no mutagenesis or functional assays are presented to test this hypothesis. Similarly, the interaction between the p47phox C-terminus and the 491-500 loop of NOX2 is described as important, but the authors do not provide experimental evidence (e.g., cross-linking, co-immunoprecipitation) to confirm this interaction in a biological context. The discussion of the 8WEJ structure is used to support the model, but the authors do not systematically compare their model with the experimental structure to identify similarities and differences.
- **Why it matters** The manuscript aims to provide structural insights into the activation mechanism of NADPH oxidase. Without experimental validation of the key interactions, the functional claims remain speculative and the impact of the work is diminished.
- **Resolution test** Include experimental validation of at least one key predicted interaction, such as mutagenesis of the Trp80-Phe81 residues followed by membrane binding assays, or cross-linking experiments to confirm the p47phox C-terminus-NOX2 interaction. Alternatively, provide a more detailed comparison with the 8WEJ structure to strengthen the case that the model captures functionally relevant features.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity of figure descriptions
- **Affected element** Figures 1-9
- **Evidence pointer** Results section
- **Issue** The figure descriptions are detailed but often lack specific information about how the models were generated and what exactly is shown. For example, in Figure 1, it is unclear whether the "five models" are superimposed or shown separately, and the color scheme for pLDDT scores is not defined in the text.
- **Required correction** Add explicit descriptions of the figure contents, including the number of models shown, the color scales used, and the specific interactions highlighted. Consider adding a table summarizing the key structural features of each model.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Completeness of methods
- **Affected element** Experimental procedures, "Molecular dynamics" section
- **Evidence pointer** Experimental procedures
- **Issue** The MD simulation methods are described briefly, but key parameters such as the simulation temperature, pressure coupling, and the specific protocol for system setup are not fully detailed. The choice of the CHARMM36m force field is justified, but the source of the lipid parameters and the method for building the membrane system are not described.
- **Required correction** Provide a more complete description of the MD simulation setup, including all relevant parameters, the software versions used, and the steps for system preparation and equilibration. This will allow others to reproduce the simulations.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Interpretation of CD data
- **Affected element** Results section, "AF2-generated model of cytb558 with p47phox"; Figure 7
- **Evidence pointer** Results section
- **Issue** The comparison between the theoretical CD spectrum calculated from the AF2 model and the experimental CD spectrum is presented as evidence for the model's validity. However, the authors do not discuss the limitations of this comparison, such as the sensitivity of CD to secondary structure content and the potential for different conformations to produce similar spectra.
- **Required correction** Add a discussion of the strengths and limitations of using CD spectroscopy to validate structural models, and consider additional validation methods (e.g., small-angle X-ray scattering) to strengthen the case.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Accessibility of data
- **Affected element** Data availability section
- **Evidence pointer** Data availability
- **Issue** The authors state that "the coordinates of the AF2 models are available upon request," which is not in line with best practices for scientific reproducibility. The models should be deposited in a public repository (e.g., ModelArchive, Zenodo) to ensure accessibility.
- **Required correction** Deposit the AF2 models and MD simulation trajectories in a public repository and provide the accession numbers in the manuscript.

## Risk / unsupported claims
- The claim that AF2 predicts an active-like conformation of cytb558 is not quantitatively supported and requires comparison with the active cryo-EM structure.
- The claim that phosphorylation enhances membrane anchoring of the complex is based on descriptive MD analysis without statistical validation.
- The functional significance of the Trp80-Phe81 membrane insertion and the p47phox C-terminus-NOX2 interaction is inferred from models without experimental validation.
- The use of CD spectroscopy to validate the AF2 model is presented without discussion of its limitations.
- The model selection criteria are based on literature-derived expectations, which introduces potential circularity in the validation process.