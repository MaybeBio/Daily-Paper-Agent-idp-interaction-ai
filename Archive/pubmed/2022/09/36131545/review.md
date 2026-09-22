## Review setup
- **Input scope** Full manuscript text including abstract, main text, and references to supporting material
- **Assessment boundary** Scientific content, methodological soundness, data interpretation, and claims as presented in the provided manuscript
- **Shared manuscript claim summary** The authors combine high-field NMR relaxation, high-resolution relaxometry, and MD simulations to characterize ps-ns backbone dynamics of the disordered C-terminal domain of the delta subunit of RNA polymerase from Bacillus subtilis. They report that three motional timescales are sufficient to model most data, that relaxometry extends sensitivity to slower motions, and that the folded N-terminal domain does not increase dynamic complexity of the IDR.
- **Visible evidence base** Main text figures (Figures 1-4), tables referenced in supporting material, and methodological descriptions in the Materials and methods section
- **Missing materials affecting confidence** Supporting figures S1-S15 and tables S1-S9 are referenced but not provided; specific numerical values for relaxation rates, fitted parameters, and simulation details are not fully visible; no access to raw data or analysis scripts

## Reviewer
- **Overall assessment** This manuscript presents a technically demanding combination of high-resolution relaxometry, high-field NMR relaxation, and MD simulations applied to a biologically relevant partially disordered protein. The dataset, spanning 12 magnetic fields, is impressive and potentially valuable to the IDP dynamics community. However, the central claims regarding the sufficiency of three motional timescales and the added value of relaxometry are only partially supported by the visible evidence. The manuscript would benefit from clearer quantitative comparisons between experimental and simulated data, and from a more critical discussion of the limitations of the analysis. The work is likely of interest to specialists in NMR relaxation and IDP dynamics, but its broader impact is currently limited by the narrow scope of the conclusions and the lack of a fully established methodological advance.

- **Who would be interested in the results, and why** Researchers working on intrinsically disordered proteins, NMR relaxation methodology, and molecular dynamics simulations of proteins. The combination of relaxometry with high-field data is of particular interest to those seeking to extend the timescale sensitivity of NMR dynamics studies. The biological context of the delta subunit of RNA polymerase may also attract investigators studying transcription regulation in Gram-positive bacteria.

- **Major strengths**
  1. The experimental effort is substantial: collecting relaxation data at 12 magnetic fields, including high-resolution relaxometry, is technically challenging and represents a valuable contribution to the field.
  2. The combination of experimental NMR and MD simulations provides a complementary view of protein dynamics, which is a strength of the study design.
  3. The use of the ICARUS correction protocol and the ABSURD selection method demonstrates methodological awareness and rigor.
  4. The biological relevance of the system, particularly the K-tract region involved in electrostatic interactions, adds significance to the work.

- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence sufficiency
- **Claim pointer** The authors claim that "the analysis of such data provides a consistent description of dynamics and confirms the validity of so far used protocols of the analysis of dynamics of IDPs also for a partially folded protein."
- **Evidence pointer** Results and discussion, Figures 2-4; location not provided
- **Concern** The claim that the data confirm the validity of existing analysis protocols is not fully supported by the visible evidence. The manuscript reports that MD simulations systematically overestimate relaxation rates at high field and underestimate the CSA/dipole-dipole cross-correlated rate ηxy, indicating a quantitative disagreement between experiment and simulation. The authors attribute this to the water model, but this admission undermines the claim of a "consistent description." Furthermore, the ABSURD selection produced only four out of 44 segments, and the authors themselves describe the selection as "very inefficient." The visible figures do not allow a quantitative assessment of the agreement between experimental and simulated data, nor between the IMPACT and MF analyses.
- **Why it matters** The central conclusion of the manuscript rests on the consistency between experimental and computational approaches. If the agreement is only qualitative or partial, the claim of validation is overstated. This affects the overall message of the paper and its utility to the community.
- **Resolution test** Provide quantitative measures of agreement between experimental and simulated relaxation rates (e.g., reduced chi-squared values, RMSD per residue). Show a direct comparison of spectral density functions derived from experiment and simulation. Clarify the criteria used to judge the consistency of the three-timescale model.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Methodological transparency
- **Claim pointer** The authors state that "the potential to access detailed description of motions at the timescale of tens of ns with the help of relaxometry data is discussed" and that relaxometry data provide "novel information" beyond high-field data.
- **Evidence pointer** Results and discussion, Figures 2 and 4; location not provided
- **Concern** The added value of relaxometry data is not convincingly demonstrated. The comparison between MF analysis with and without relaxometry data (Figure 4) shows differences in parameters in the region 105-137, but the authors note that the high-field dataset is "relatively sparse" and that "it is again difficult to make any meaningful comparison because of the limited size of the high-field data set." This admission weakens the claim that relaxometry provides novel information. The manuscript does not show a clear statistical test or information-theoretic comparison demonstrating that the relaxometry data significantly improve the model fit or constrain parameters beyond what high-field data alone can achieve.
- **Why it matters** The methodological advance of the paper is the combination of relaxometry with high-field data. If the added value is not clearly established, the paper becomes a case study rather than a methodological contribution.
- **Resolution test** Perform a quantitative comparison of model fits with and without relaxometry data, including information criteria (e.g., AIC or BIC) or F-tests. Show that the relaxometry data constrain parameters that are otherwise poorly determined by high-field data alone. Provide a clear statement of what specific motions or timescales are uniquely accessible via relaxometry.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Biological relevance
- **Claim pointer** The authors state that the K-tract region (residues 96-104) and the region 105-140 are involved in electrostatic interactions critical for the biological function of the delta subunit, and that the dynamics of this region are "of particular interest."
- **Evidence pointer** Introduction, Results and discussion; location not provided
- **Concern** The biological significance of the dynamics findings is not developed. The manuscript identifies the K-tract and surrounding regions as biologically important, but does not connect the observed dynamics to functional implications. For example, the authors mention that motions with timescales of 10 ns or more "could be related to the formation of a temporarily compacted conformation," but this is speculative and not supported by additional data or analysis. The paper would benefit from a more explicit discussion of how the dynamics described relate to the known function of the delta subunit in transcription regulation.
- **Why it matters** The stated significance of the work includes biological relevance. Without a clear link between dynamics and function, the impact of the study is limited to a methodological demonstration.
- **Resolution test** Add a discussion section that explicitly connects the observed dynamics to the known functional roles of the delta subunit. If possible, relate the timescales and amplitudes of motions to specific functional processes, such as binding or conformational selection.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity
- **Affected element** Abstract
- **Evidence pointer** Abstract; location not provided
- **Issue** The abstract states that the study provides "an unprecedented data set" of relaxation data at 12 magnetic fields. While this is likely true, the claim is not qualified. The abstract also uses the phrase "tantalizing indications," which is informal for a scientific paper.
- **Required correction** Rephrase to be more precise and formal. For example, "a data set spanning 12 magnetic fields, which is, to our knowledge, the most extensive reported for a disordered protein to date." Replace "tantalizing indications" with a more neutral phrase such as "suggestive evidence."

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Reproducibility
- **Affected element** Materials and methods, MD simulations
- **Evidence pointer** Materials and methods, MD simulations; location not provided
- **Issue** The description of the MD simulations is brief. The authors state that 13 trajectories were calculated with various initial conformations, but do not provide details on the length of each trajectory, the total simulation time, the temperature and pressure coupling schemes, or the equilibration protocol. The statement that "each trajectory was divided into 22 nonoverlapping segments of variable length (100-120 ns)" implies a total simulation time of approximately 2.2-2.6 microseconds per trajectory, but this is not explicitly stated.
- **Required correction** Provide a more complete description of the simulation setup, including total simulation time per trajectory, ensemble (NVT or NPT), thermostat and barostat parameters, and any constraints applied. This is essential for reproducibility.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Statistical rigor
- **Affected element** Results and discussion, Figure 1
- **Evidence pointer** Figure 1; location not provided
- **Issue** The correlation between relaxometry rates and two-field NMR rates is shown in Figure 1, but no correlation coefficients or goodness-of-fit statistics are reported in the text. The authors state that the ICARUS correction "effectively restore[s] a quantitative agreement," but this is not quantified.
- **Required correction** Report the Pearson correlation coefficient, the slope and intercept of the linear fit, and the root-mean-square deviation between the two datasets. This would strengthen the claim of quantitative agreement.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Interpretation
- **Affected element** Results and discussion, Figure 3
- **Evidence pointer** Figure 3; location not provided
- **Issue** The comparison of timescales derived from MD simulations (Figure 3) with those from IMPACT analysis (Figure 2) is qualitative. The authors note that the simulation finds a minor component at ~5 ns and most ns dynamics at ~3 ns, but do not directly compare these values with the IMPACT-derived timescales (T4, T5, T6, T7). A direct tabular comparison would be helpful.
- **Required correction** Provide a table comparing the timescales and amplitudes derived from IMPACT, MF, and MD analyses for representative residues or regions.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Completeness
- **Affected element** Results and discussion, Conclusions
- **Evidence pointer** Conclusions; location not provided
- **Issue** The conclusion states that "three timescales and their associated amplitudes are in general sufficient to model most observations in vitro and in silico." However, the manuscript also reports small but significant contributions from a fourth timescale (T7) in the ICARUS-IMPACT analysis and from a ~5 ns component in the MD analysis. The conclusion would benefit from a more nuanced statement acknowledging these deviations.
- **Required correction** Revise the conclusion to acknowledge that while three timescales capture the dominant features, minor contributions from slower timescales are observed and may be biologically relevant.

## Risk / unsupported claims
- The claim that the data "confirm the validity of so far used protocols" is not fully supported given the reported quantitative disagreements between experiment and simulation.
- The claim that relaxometry data provide "novel information" beyond high-field data is not quantitatively demonstrated.
- The statement that motions with timescales of 10 ns or more "could be related to the formation of a temporarily compacted conformation" is speculative and not supported by direct evidence.
- The assertion that the dataset is "unprecedented" is plausible but not verified against the literature in the visible text.
- The biological significance of the dynamics findings is asserted but not developed or supported with functional data.