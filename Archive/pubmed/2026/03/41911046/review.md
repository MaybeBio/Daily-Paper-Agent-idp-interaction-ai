## Review setup
- **Input scope** Full manuscript text (abstract, introduction, main sections, acknowledgements) without figures, tables, or references
- **Assessment boundary** Scientific content, logical coherence, and evidentiary support as presented in the supplied text; figure and table content cannot be independently verified
- **Shared manuscript claim summary** The authors present a feature article synthesizing physicochemical principles governing the intrinsically disordered salivary peptide Histatin 5, focusing on ensemble structure, electrostatics, charge regulation, environmental responsiveness, and multiscale interactions, with emphasis on the role of histidine chemistry and the utility of Hst5 as a benchmark system for IDP research
- **Visible evidence base** Textual descriptions of SAXS, DLS, neutron scattering, QCM-D, neutron reflectometry, Monte Carlo simulations, atomistic and coarse-grained simulations, and integrative modeling approaches; figure and table references are cited but their content is not available
- **Missing materials affecting confidence** All figures, tables, references, experimental protocols, and quantitative data; the manuscript is a feature article and the absence of these materials prevents verification of specific claims

## Reviewer
- **Overall assessment** This feature article provides a broad and conceptually coherent synthesis of the physicochemical behavior of Histatin 5, an intrinsically disordered salivary peptide. The authors frame Hst5 as a model system for understanding how sequence-encoded properties, particularly histidine-mediated charge regulation, govern ensemble behavior and environmental responsiveness. The scope is ambitious and the integration of experimental and computational approaches is commendable. However, the manuscript is largely descriptive and qualitative in its current form. The absence of quantitative data, specific methodological details, and direct figure/table content makes it impossible to assess the evidentiary basis for many specific claims. The article reads more as a narrative review of the authors' own body of work than as a critical synthesis of the broader field. The general principles section is somewhat generic and does not fully distinguish Hst5-specific findings from well-established IDP behavior. The future directions section is brief and lacks specificity. For a feature article, the level of technical depth is appropriate for a broad readership, but the scientific rigor of the claims cannot be evaluated without the missing materials.

- **Who would be interested in the results, and why** Researchers in the intrinsically disordered protein field, particularly those interested in charge regulation, polyelectrolyte physics, and ensemble-based descriptions of IDP function. The article would also appeal to investigators studying antimicrobial peptides, salivary proteins, and metal-ion interactions with histidine-rich sequences. Those developing or applying IDP-specific force fields and integrative modeling approaches would find the methodological discussion relevant. The broader soft-matter and biophysics communities interested in polyelectrolyte behavior, reentrant condensation, and surface interactions may also find value.

- **Major strengths** The article provides a coherent conceptual framework linking sequence composition, electrostatics, and environmental responsiveness in an IDP. The emphasis on histidine-mediated charge regulation as a central organizing principle is well articulated. The integration of multiple experimental techniques (SAXS, DLS, neutron scattering, QCM-D, reflectometry) with multiscale simulations is presented in a logical manner. The discussion of PPII propensity and its coupling to global ensemble properties is a useful contribution. The treatment of zinc-mediated oligomerization and reentrant condensation connects IDP behavior to broader polyelectrolyte physics, which is conceptually valuable. The article is generally well written and accessible to nonspecialists.

- **Major Concerns** The following concerns are identified.

- **Minor Comments** The following comments are identified.

- **Technical failings that need to be addressed before the case is established** R1-M1, R1-M2, R1-M3, R1-M4

- **Assessment against Nature-style criteria** Originality: The article presents a synthesis of the authors' own work on Hst5, and while the specific system is of interest, the general principles discussed (charge regulation, ensemble heterogeneity, environmental responsiveness) are well established in the IDP field. The originality lies primarily in the specific system and the integration of techniques, not in conceptual novelty. Scientific importance: Hst5 is a biologically relevant antimicrobial peptide, and understanding its physicochemical behavior has potential translational relevance. However, the article does not establish broader importance beyond the specific system, and the general principles section does not clearly articulate what new insights Hst5 provides beyond existing IDP knowledge. Interdisciplinary readership: The article bridges biophysics, soft-matter chemistry, and peptide biology, which could appeal to a broad audience. However, the level of technical detail in some sections may be challenging for nonspecialists, and the absence of quantitative context limits accessibility. Technical soundness: The technical soundness cannot be fully assessed without the figures, tables, and references. The textual descriptions suggest a reasonable methodological approach, but specific claims about quantitative agreement between simulations and experiments cannot be verified. Readability for nonspecialists: The article is generally well written and the conceptual framework is accessible. However, some sections assume familiarity with IDP-specific concepts and techniques. Overall, the article is more suited to a specialized journal such as the Journal of Physical Chemistry B than to Nature, given its focus on a specific system and the absence of broadly transformative findings.

- **Recommendation posture** Supportive if technical concerns are resolved and the missing materials are provided for verification. The conceptual framework is sound and the article is likely to be of interest to the IDP community. However, the current form does not allow for a full assessment of the evidentiary basis, and several claims require quantitative support.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence quality
- **Claim pointer** The authors claim that Hst5 exhibits effective Flory exponents exceeding those of neutrally charged IDPs, positioning it near the upper bound of expanded disordered behavior.
- **Evidence pointer** Section "Conformational Ensembles", subsection "Ensemble Properties"; Figure 1 (content not available)
- **Concern** The claim regarding effective Flory exponents is presented without any quantitative values, error estimates, or comparison to specific reference data. The figure that presumably contains this information is not available for review. Without the actual exponent values, the statistical significance of the comparison to neutrally charged IDPs, and the range of conditions under which these exponents were determined, this claim cannot be evaluated.
- **Why it matters** The Flory exponent is a central quantitative descriptor of polymer conformation. If the claim is to support the broader argument that Hst5 is unusually expanded, the reader needs to see the actual values, the methods used to extract them, and the comparison set. Without this, the claim is unverifiable.
- **Resolution test** Provide the effective Flory exponent values with uncertainties, the method of extraction (e.g., from SAXS-derived Rg versus chain length or from simulations), and a clear comparison to reference values for neutrally charged IDPs under matched conditions.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence quality
- **Claim pointer** The authors state that macromolecular crowding has a modest influence on overall expansion, consistent with SAXS and neutron scattering measurements.
- **Evidence pointer** Section "Conformational Ensembles", subsection "Ensemble Properties"; Section "Environmental Modulation and Charge Regulation"; Figures 1 and 4 (content not available)
- **Concern** The claim that crowding has a "modest influence" is qualitative. The text does not provide the magnitude of the effect, the range of crowder concentrations tested, the type of crowder used, or the comparison to theoretical predictions. The figure that presumably shows this data is not available. The statement "consistent with SAXS and neutron scattering measurements" implies a quantitative comparison, but no numbers are given.
- **Why it matters** The response to crowding is a key test of polymer theory and has implications for the in vivo behavior of Hst5 in saliva, which is a crowded environment. A qualitative statement without supporting data does not allow the reader to assess the strength of the conclusion.
- **Resolution test** Provide quantitative Rg values (or changes in Rg) as a function of crowder concentration, specify the crowder type and molecular weight, and show the comparison to theoretical predictions or simulation results.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence quality
- **Claim pointer** The authors claim that zinc ions coordinate histidine imidazole groups, promoting reversible, dynamic oligomerization, and that buffer-independent thermodynamic analyses reveal multiple Zn-Hst5 binding modes and temperature-dependent stoichiometry.
- **Evidence pointer** Section "Electrostatics, Multivalent Cations, and Dynamic Oligomerization"; Figures 5 and 6 (content not available)
- **Concern** The claim of multiple binding modes and temperature-dependent stoichiometry is presented without any thermodynamic parameters (e.g., binding constants, enthalpies, entropies, stoichiometry values). The buffer-independent analysis is mentioned but the method is not described. The figure that presumably contains the binding isotherms or titration data is not available. The spectroscopic identification of specific imidazole donors (H18/H19) is stated without showing the spectra or the assignment methodology.
- **Why it matters** The specific nature of Zn2+ binding is central to the proposed mechanism of metal-ion regulation. Without quantitative binding data and clear spectroscopic evidence, the claim of specific, multiple binding modes is not established. This is particularly important given the authors' assertion that this behavior is distinct from simple electrostatic association.
- **Resolution test** Provide binding constants and stoichiometry as a function of temperature and pH, describe the buffer-independent method (e.g., ITC with buffer variation), and show the spectroscopic data (e.g., NMR or UV-Vis) with clear assignments for the imidazole donors.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence quality
- **Claim pointer** The authors state that reentrant condensation of Hst5 in the presence of trivalent polyphosphate anion (TPP) has been observed, with onset and dissolution boundaries depending sensitively on the number of arginine residues.
- **Evidence pointer** Section "Electrostatics, Multivalent Cations, and Dynamic Oligomerization", subsection "Polyvalent Anions, Reentrant Condensation, and Polyelectrolyte Physics"; Figure 6C,D (content not available)
- **Concern** The reentrant condensation phenomenon is described qualitatively. The text does not provide the phase diagram, the concentration ranges of TPP and Hst5, the salt conditions, or the method used to detect condensation (e.g., turbidity, dynamic light scattering, microscopy). The systematic Arg-to-Lys substitution study is mentioned, but the results are not described quantitatively. The comparison to coarse-grained simulations is stated but no simulation details or quantitative agreement metrics are given.
- **Why it matters** Reentrant condensation is a specific and nontrivial phase behavior. The claim that this is observed and that it depends on arginine content is a key finding. Without the actual phase boundaries, the reader cannot assess the robustness of the phenomenon or the validity of the arginine-specific interpretation.
- **Resolution test** Provide the full phase diagram (Hst5 concentration versus TPP concentration) with clear boundaries, specify the detection method, show the Arg-to-Lys mutant data quantitatively, and provide a quantitative comparison between experiment and simulation.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Abstract
- **Evidence pointer** Abstract, first paragraph
- **Issue** The abstract states that Hst5 "remains disordered across a wide range of conditions" but does not specify the range of conditions studied or the methods used to establish disorder. This is a strong claim that is not qualified.
- **Required correction** Add a brief qualification, such as "across the pH and ionic strength ranges examined here" or specify the conditions in the abstract.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Section "General Physical Principles"
- **Evidence pointer** Section "General Physical Principles", first paragraph
- **Issue** The general principles listed (functional adaptability, charge regulation, ensemble-based binding) are presented as if they are novel insights from Hst5 studies, but these are well-established concepts in the IDP field. The section does not clearly articulate what Hst5 specifically adds to these principles.
- **Required correction** Revise the section to explicitly state which principles are general to IDPs and which are specifically illuminated by Hst5, with reference to the broader literature.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Section "Future Directions and Conclusions"
- **Evidence pointer** Section "Future Directions and Conclusions", first paragraph
- **Issue** The future directions are vague ("deeper characterization of specific ion effects", "continued refinement of IDP-aware force fields") and do not provide specific, testable hypotheses or experimental plans.
- **Required correction** Provide more specific future directions, such as identifying particular ion species, proposed experimental techniques, or specific force field improvements to be tested.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Section "Multiscale Modeling and Methodological Considerations"
- **Evidence pointer** Section "Multiscale Modeling and Methodological Considerations", second paragraph
- **Issue** The discussion of machine-learning approaches is superficial. The text mentions "integrative and machine-learning approaches" but does not describe which specific methods were used, what data they were trained on, or how they were validated.
- **Required correction** Provide specific details on the machine-learning methods used, including input features, training data, and validation metrics, or clearly state that these are future prospects rather than completed work.

## Risk / unsupported claims
- The claim that Hst5 exhibits effective Flory exponents near the upper bound of expanded disordered behavior is unsupported without quantitative values and comparison data (R1-M1).
- The claim that crowding has a "modest influence" on Hst5 ensemble dimensions is unsupported without quantitative data on the magnitude of the effect (R1-M2).
- The claim of multiple Zn-Hst5 binding modes with temperature-dependent stoichiometry is unsupported without thermodynamic parameters and binding data (R1-M3).
- The claim of reentrant condensation with arginine-dependent boundaries is unsupported without the phase diagram and quantitative comparison to simulations (R1-M4).
- The statement that Hst5 "remains disordered across a wide range of conditions" is not qualified with the specific conditions examined.
- The claim that Hst5 exhibits "pronounced local structure in the form of PPII helices" is presented without quantitative measures of PPII content or comparison to other IDPs.
- The statement that "charge regulation theory provides a quantitative framework" is not supported by specific theoretical predictions or quantitative comparisons to experimental data.
- The claim that Hst5 "exemplifies how an intrinsically disordered polyelectrolyte can generate rich collective behavior" is a broad generalization that is not fully supported by the specific evidence presented.
- The assertion that Hst5 "serves as a model system for methodological development in IDP simulation" is plausible but not critically evaluated in the text.