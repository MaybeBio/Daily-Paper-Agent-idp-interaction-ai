## Review setup
- **Input scope** Full manuscript text (abstract, introduction, methods, results, discussion, conclusion) without figures or supplementary material
- **Assessment boundary** Methodological soundness of the extended ELViM framework; validity of claims regarding conformational landscape differences between wild-type and P301L tau fragment; mechanistic interpretation of early aggregation events
- **Shared manuscript claim summary** The authors present an enhanced Energy Landscape Visualization Method (ELViM) that simultaneously maps monomeric and oligomeric conformational spaces using a distance-based similarity metric and force-based embedding. Applied to replica exchange molecular dynamics simulations of a 19-residue tau fragment (jR2R3) and its P301L mutant, the method reportedly reveals that the mutation preorganizes monomers into compact, β-strand conformations that promote persistent interchain contacts around the PHF6 motif, thereby explaining enhanced aggregation.
- **Visible evidence base** Text descriptions of results; figure references without actual figures; methods section with equations; no numerical data, no statistical analyses, no convergence metrics, no force field validation data
- **Missing materials affecting confidence** All figures (Figures 1–3 and S1–S6); simulation convergence assessments; quantitative density estimates; contact frequency values beyond qualitative descriptions; comparison with existing analysis methods; parameter choices for ELViM (σ0, ε); replica exchange acceptance rates; block error analysis or equivalent

## Reviewer
- **Overall assessment** The manuscript presents a potentially useful extension of an existing visualization method to oligomeric systems, applied to a biologically relevant tau fragment. The conceptual motivation is clear and the methodological extension is logical. However, the current manuscript does not provide sufficient evidence to support the central claims. All quantitative results are embedded in figures that were not provided for review, making it impossible to assess the validity of the density estimates, contact frequency maps, or the claimed differences between wild-type and mutant systems. The mechanistic interpretation, while plausible, rests on qualitative visual inspection rather than quantitative comparison. The manuscript would benefit from explicit validation of the method against known systems, statistical treatment of the observed differences, and a more careful discussion of the limitations of the approach.
- **Who would be interested in the results, and why** Researchers studying intrinsically disordered proteins, protein aggregation, and conformational ensembles of biomolecules. The methodological extension of ELViM to oligomeric systems could be of interest to computational biophysicists developing visualization and analysis tools for molecular dynamics simulations. The specific application to tau and the P301L mutation would interest the neurodegeneration community, though the biological conclusions are preliminary.
- **Major strengths** The conceptual framing of disentangling intrachain folding from interchain assembly is clear and addresses a genuine need in the field. The methodological extension of ELViM to include interchain contact mapping is logical and potentially valuable. The choice of a biologically relevant system with a known disease-associated mutation provides practical motivation. The authors acknowledge limitations of their approach, including the use of capped termini and the nonparametric nature of the method.
- **Major Concerns** See detailed items below.
- **Minor Comments** See detailed items below.
- **Technical failings that need to be addressed before the case is established** R1-M1 (missing figures and quantitative data), R1-M2 (no validation of the extended method), R1-M3 (no statistical treatment of differences), R1-M4 (convergence assessment absent)
- **Assessment against Nature-style criteria** **Originality**: Moderate. The extension of an existing method to oligomeric systems is incremental rather than conceptually novel. **Scientific importance**: Potentially significant if the method proves robust and the biological conclusions hold, but the current evidence is insufficient to establish importance. **Interdisciplinary readership**: The method could appeal to computational chemists, biophysicists, and structural biologists, but the presentation is somewhat narrow. **Technical soundness**: Cannot be fully assessed without figures and quantitative data; the methodological description is clear but lacks validation. **Readability for nonspecialists**: The manuscript is generally well-written and accessible, though some methodological details assume familiarity with dimensionality reduction techniques.
- **Recommendation posture** Currently not established from the provided evidence. The manuscript requires major revisions including provision of all figures, quantitative validation, statistical analysis, and convergence assessment before the claims can be evaluated.

### Major Concerns

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence sufficiency
- **Claim pointer** The manuscript claims that ELViM effectively captures conformational differences between wild-type and P301L tau fragments across monomeric, dimeric, and tetrameric states, and that the mutation preorganizes monomers into compact ensembles with persistent interchain contacts around PHF6.
- **Evidence pointer** Figures 1–3 and S1–S6; location not provided in text
- **Concern** All quantitative results are presented exclusively in figures that were not included in the review materials. The text provides qualitative descriptions (e.g., "density analysis shows," "contact maps reveal") without any numerical values, error bars, or statistical comparisons. Without access to the figures, it is impossible to verify the density distributions, contact frequency percentages, structural alignments, or the claimed differences between systems. The manuscript cannot be evaluated on its central claims without this evidence.
- **Why it matters** The core contribution of the manuscript is the application of the extended ELViM method to reveal structural differences. If the figures are not available for review, the evidence base is incomplete and the claims are unverifiable.
- **Resolution test** Provide all figures with clear labels, color scales, and annotations. Include quantitative values for density peaks, contact frequencies, and structural parameters in the text or figure captions.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Methodological validation
- **Claim pointer** The manuscript claims that the extended ELViM framework enables "systematic disentanglement of intrachain folding dynamics from the interchain assembly interactions" and that it provides an "unbiased" representation of conformational space.
- **Evidence pointer** Methods section, "Extension of the ELViM Approach"; location not provided
- **Concern** The extended method is introduced without any validation against known systems or comparison with established analysis techniques. There is no demonstration that the distance-based similarity metric and force-based embedding preserve meaningful structural relationships in oligomeric systems, nor that the consensus contact mapping protocol produces results consistent with direct contact analysis. The claim of "unbiased" representation is particularly problematic, as the choice of similarity metric, embedding parameters, and density estimation bandwidth all introduce potential biases that are not discussed or tested.
- **Why it matters** Without validation, the reader cannot assess whether the observed differences between wild-type and mutant are artifacts of the method or genuine biological features. The "unbiased" claim is overstated without systematic parameter sensitivity analysis.
- **Resolution test** Validate the method on a system with known conformational properties (e.g., a peptide with well-characterized folding behavior). Compare ELViM results with established analysis methods (e.g., principal component analysis, time-lagged independent component analysis, or direct contact analysis). Perform sensitivity analysis on key parameters (σ0, ε, density bandwidth).

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** Yes
- **Axis** Statistical rigor
- **Claim pointer** The manuscript claims that jR2R3-P301L exhibits "more persistent interchain contacts around PHF6" and that wild-type shows "weaker and less consistent" interchain interactions.
- **Evidence pointer** Results and Discussions, dimer and tetramer sections; location not provided
- **Concern** The differences between wild-type and mutant are described qualitatively without any statistical analysis. No confidence intervals, significance tests, or effect sizes are reported. The selection of "15000 conformations" from each system is mentioned, but there is no discussion of whether these are independent samples, how autocorrelation was handled, or whether the observed differences are robust to sampling variation. The claim that contact frequencies differ between systems requires quantitative comparison with appropriate uncertainty quantification.
- **Why it matters** The central biological conclusion is that the P301L mutation alters conformational preferences and interchain interactions. Without statistical treatment, the observed differences could be due to sampling noise or insufficient convergence.
- **Resolution test** Report contact frequency differences with confidence intervals or bootstrap estimates. Perform statistical tests (e.g., permutation tests) for differences between wild-type and mutant contact maps. Discuss sampling independence and convergence.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** Yes
- **Axis** Simulation quality
- **Claim pointer** The manuscript claims that REMD simulations were used to generate conformational ensembles, with 64 replicas spanning 292.7–455.6 K, and that exchange probabilities remained within 0.2–0.3.
- **Evidence pointer** Methods, "Application to Tau Protein Simulations"; location not provided
- **Concern** No convergence assessment is provided for the REMD simulations. There is no discussion of whether the simulations reached equilibrium, how many independent samples were obtained, or whether the 300 ns analysis window is sufficient for the systems studied. The exchange probability range is mentioned but not shown as a function of replica index or time. For intrinsically disordered proteins, which sample highly heterogeneous ensembles, convergence is a critical concern that is not addressed.
- **Why it matters** If the simulations are not converged, the conformational landscapes and contact frequencies derived from them are unreliable, and the biological conclusions are unsupported.
- **Resolution test** Provide convergence metrics such as block error analysis, autocorrelation times, or replica exchange acceptance rates. Show that the conformational distributions are stable over the analysis window. Discuss the number of effective independent samples.

### Minor Comments

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Methods, "Structural Similarity Metric and Dissimilarity Matrix"
- **Evidence pointer** Equation 1; location not provided
- **Issue** The parameters σ0 and ε in the similarity metric are introduced but their values are not specified. The choice of these parameters will affect the resulting dissimilarity matrix and hence the projection.
- **Required correction** Specify the values used for σ0 and ε, and justify these choices.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Reproducibility
- **Affected element** Methods, "Application to Tau Protein Simulations"
- **Evidence pointer** Location not provided
- **Issue** The initial structures were extracted from a cryo-EM tau fibril model, but the specific PDB identifier or model details are not provided. The peptide sequence is given, but the exact construct boundaries and any modifications are not fully specified.
- **Required correction** Provide the PDB identifier or accession code for the cryo-EM model, and specify the exact residue range and any terminal modifications.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Interpretation
- **Affected element** Results and Discussions, dimer section
- **Evidence pointer** Location not provided
- **Issue** The text states that jR2R3-P301L dimers in Region I exhibit "strong terminal interactions" while Region II shows "both chains remain in contact along their length." The biological significance of these two distinct dimer populations is not discussed in the context of aggregation mechanisms.
- **Required correction** Provide interpretation of why two distinct dimer populations exist and how they relate to the proposed aggregation pathway.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Conclusion
- **Evidence pointer** Location not provided
- **Issue** The conclusion states that ELViM "offers a rigorous method for selecting discrete structural seeds to optimize ensemble-based sampling protocols," but this application is not demonstrated or discussed in the results.
- **Required correction** Either demonstrate this application or remove the claim from the conclusion.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Literature context
- **Affected element** Introduction
- **Evidence pointer** Location not provided
- **Issue** The introduction mentions prior computational studies on this tau fragment but does not clearly differentiate the current work from those studies beyond the methodological extension. The specific limitations of prior analyses that the current method addresses are not explicitly stated.
- **Required correction** Clarify what prior studies could not capture and how the extended ELViM addresses those gaps.

## Risk / unsupported claims
- The claim that P301L acts as a "structural stabilizer" shifting conformational preferences toward compact, preorganized ensembles is not quantitatively supported without figure data and statistical analysis.
- The claim that ELViM provides an "unbiased" representation of conformational space is unsupported without parameter sensitivity analysis and validation against known systems.
- The mechanistic claim that compact β-strand conformations "shield" the PHF6 motif and limit interchain contacts in certain populations is speculative and not directly tested.
- The claim that the method has "broad applicability" to other IDP systems is plausible but not demonstrated.
- The statement that jR2R3-P301L dimers in Region I show contacts "present in all 50 analyzed structures" is unverifiable without the actual contact maps.
- The claim that the extended ELViM framework "enables systematic disentanglement" of intrachain and interchain contributions is not validated against alternative approaches.