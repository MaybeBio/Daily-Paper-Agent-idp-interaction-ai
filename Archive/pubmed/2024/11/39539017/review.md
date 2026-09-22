## Review setup
- **Input scope** Full manuscript text (abstract, significance, introduction, methods, results, discussion, acknowledgments, author contributions, declaration of interests)
- **Assessment boundary** Technical soundness of the parameter implementation, validation strategy, agreement with published experimental/computational data, and interpretation of simulation results
- **Shared manuscript claim summary** The authors implement parameters for phosphoserine and phosphothreonine in the ABSINTH-OPLS implicit solvent model within the CAMPARI Monte Carlo simulation engine, and validate these parameters against published experimental and computational data for four intrinsically disordered protein systems, demonstrating near-quantitative agreement for phosphorylation-induced changes to local secondary structure and global ensemble dimensions.
- **Visible evidence base** Main text, Figures 1-5, Tables 1, references to Supporting Material (Figures S1-S6, Tables S1-S6)
- **Missing materials affecting confidence** Supporting Material (Figures S1-S6, Tables S1-S6) not provided; specific simulation parameters (number of replicates for Ash1 and PAGE4, simulation length, convergence criteria) not fully detailed in main text; exact fitting procedures for persistence length and chi-square free calculations not fully described

## Reviewer
- **Overall assessment** This manuscript addresses a timely and important need in the disordered protein simulation community: the development and validation of parameters for phosphorylated residues in the widely used ABSINTH implicit solvent model. The authors have selected four well-characterized test systems that collectively probe both local and global conformational changes upon phosphorylation, and the reported agreement with published experimental data is encouraging. The work is clearly presented and the methodological choices are generally well justified. However, several technical aspects require clarification and additional analysis before the parameter set can be considered fully validated and broadly useful to the community. In particular, the treatment of the charge state of the phosphoryl group, the handling of salt bridges and ion interactions, and the quantitative metrics used for validation need more careful scrutiny. The manuscript would also benefit from a more explicit discussion of the limitations of the ABSINTH model for highly charged moieties and from additional validation against experimental data that directly probes local conformational preferences.

- **Who would be interested in the results, and why** Researchers in the intrinsically disordered protein community, particularly those who use molecular simulation to study post-translational modifications. The work will also be of interest to computational biophysicists developing force field parameters for modified amino acids, and to experimentalists who study phosphorylation-dependent conformational changes in IDRs and seek complementary computational tools. The practical guidance on the use of phosphomimetic mutations will be valuable to a broad audience.

- **Major strengths**
  1. The manuscript addresses a clear gap in available simulation tools: phosphorylated residue parameters for ABSINTH, a widely used implicit solvent model for IDR simulations.
  2. The validation strategy is thoughtful, using four test systems with published experimental and computational data that collectively probe both local (helix stabilization, chain stiffness) and global (radius of gyration) conformational changes.
  3. The authors provide a practical and honest assessment of the limitations of their parameters, including the issue of Na+ chelation and the caveats of fixed-charge models for phosphate-arginine interactions.
  4. The discussion of phosphomimetic mutations is nuanced and provides useful guidance for the community.
  5. The manuscript is clearly written and the figures are informative.

- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness of parameter derivation
- **Claim pointer** The authors state that the free energy of solvation (FOS) values for the phosphoryl groups were calculated from experimental methods using the protocol described in reference 58, and that the z = -1 charge state with a FOS corresponding to a deprotonated (z = -2) phosphoryl group (pSer2-* and pThr2-*) was used for the production simulations.
- **Evidence pointer** Methods section, "Phosphoserine and -threonine parameter implementation in CAMPARI"; Results section, "All-atom MC simulations of phosphorylated IDRs in ABSINTH"
- **Concern** The rationale for combining a -1 charge with a -2 FOS value is not fully explained. The authors state that the z = -2 parameters led to "trapped" salt bridges and poorly sampled trajectories, and that the z = -1 with -2 FOS combination enabled robust sampling. However, the physical justification for this hybrid approach is not clearly articulated. Is this a pragmatic compromise to avoid known artifacts of fixed-charge models, or is there a physical basis for this parameter combination? The authors should provide a more detailed discussion of the trade-offs involved and the sensitivity of their results to this choice. Additionally, the authors should clarify whether this hybrid approach is intended to represent a specific protonation state or is an effective parameterization that implicitly accounts for effects not captured by the fixed-charge model.
- **Why it matters** The choice of charge state and FOS values fundamentally determines the behavior of the phosphorylated residues in the simulation. If the hybrid approach is not well justified, users may not understand when and how to apply these parameters, and the transferability of the parameters to other systems may be questionable.
- **Resolution test** The authors should provide a more detailed justification for the hybrid charge/FOS combination, including a discussion of the physical basis (if any) and the sensitivity of their results to this choice. They should also provide guidance on when this parameter combination is appropriate and when it may not be.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Validation rigor
- **Claim pointer** The authors claim "near-quantitative agreement with published findings" for the four test systems, based on metrics including radius of gyration, transient helicity, and persistence length.
- **Evidence pointer** Results section, "Local phosphorylation-induced changes to the conformational ensemble" and "Effects of multisite phosphorylation on IDR ensemble dimensions"; Figures 2-4
- **Concern** The quantitative metrics used to support the claim of "near-quantitative agreement" are not consistently reported. For TH4, the authors report per-residue helical fractions and compare them to published values, but the quantitative comparison is presented qualitatively ("we observe helix stabilization"). For Tau, the persistence length values are reported in Figure 3D, but the comparison to published values is not quantified in the text. For Ash1, the chi-square free values are reported (0.67 and 3.95), but the threshold for "good agreement" is not defined. For PAGE4, the comparison to published data is described qualitatively. The authors should provide a more systematic and quantitative comparison to published values for all four systems, including appropriate statistical measures of agreement.
- **Why it matters** The central claim of the manuscript is that the new parameters reproduce published experimental and computational results. Without a rigorous quantitative comparison, the strength of this claim cannot be properly evaluated.
- **Resolution test** The authors should provide a table or figure that quantitatively compares simulation results to published experimental/computational values for all four test systems, with appropriate uncertainty estimates and statistical measures of agreement.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Completeness of validation
- **Claim pointer** The authors state that "our simulations of four well-studied phospho-IDRs show near-quantitative agreement with published findings for these systems via metrics including changes to radius of gyration, transient helicity, and persistence length."
- **Evidence pointer** Results section; Figures 2-4
- **Concern** The validation is limited to four test systems, all of which are relatively short IDRs or peptides. The authors do not test their parameters on systems with known phosphorylation-dependent compaction or on systems where phosphorylation is known to disrupt specific intramolecular interactions. Additionally, the authors do not compare their results to simulations using other available parameter sets for phosphorylated residues (e.g., those developed for CHARMM or AMBER force fields). A more extensive validation, including a comparison to other parameter sets, would strengthen the claims of the manuscript.
- **Why it matters** The utility of the new parameters depends on their transferability to a wide range of IDR systems. Validation on a limited set of test systems may not capture the full range of behaviors that users may encounter.
- **Resolution test** The authors should either expand the validation to include additional test systems or provide a more detailed discussion of the expected limitations of their parameters and the types of systems for which they are likely to be most applicable.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Interpretation of results
- **Claim pointer** The authors state that "phosphorylation can rewire that charge patterning" and that "the same underlying amino acid sequence can occupy distinct phospho-dependent conformational ensembles."
- **Evidence pointer** Discussion section
- **Concern** The authors' exploration of phosphorylation site combinations in Ash1 and PAGE4 (Figure 5) is interesting but somewhat limited. The authors identify combinations of phospho-sites that alter the NCPR and simulate these sequences, but the analysis of how specific phosphorylation patterns affect local versus global conformational changes is largely descriptive. A more systematic analysis of the relationship between phosphorylation pattern and conformational outcome, perhaps using a more quantitative framework, would strengthen the conclusions.
- **Why it matters** The manuscript aims to provide insights into how phosphorylation tunes intramolecular interactions in IDRs. A more rigorous analysis of the relationship between phosphorylation pattern and conformational outcome would increase the impact of the work.
- **Resolution test** The authors should provide a more quantitative analysis of the relationship between phosphorylation pattern and conformational changes, perhaps using correlation analysis or a more systematic exploration of phosphorylation site combinations.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity of methods
- **Affected element** Methods section, "Phosphoserine and -threonine parameter implementation in CAMPARI"
- **Evidence pointer** Methods section
- **Issue** The description of the parameter implementation is somewhat brief. The authors state that parameters were implemented in CAMPARI v3 with parameter sets abs3.5_opls_phos.prm or abs3.5_charm36_phos.prm, but do not provide details on the specific atom types, bond, angle, and torsion parameters that were added or modified.
- **Required correction** The authors should provide more detail on the parameter implementation, either in the main text or in the Supporting Material, including the specific parameters that were added or modified and how they were derived.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Statistical reporting
- **Affected element** Results section, "Effects of multisite phosphorylation on IDR ensemble dimensions"
- **Evidence pointer** Figure 4
- **Issue** The radius of gyration distributions in Figure 4C and 4D are presented as histograms, but the number of independent samples and the statistical uncertainty in the distributions are not reported.
- **Required correction** The authors should report the number of independent samples and the statistical uncertainty in the reported distributions, either in the figure caption or in the text.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Completeness of comparison
- **Affected element** Results section, "Local phosphorylation-induced changes to the conformational ensemble"
- **Evidence pointer** Figure 2D
- **Issue** The comparison of per-residue helical content between simulations and published values for TH4 is presented graphically, but the published values are not shown in the same figure.
- **Required correction** The authors should include the published values in Figure 2D for direct comparison, or provide a separate figure that overlays the simulation results with the published data.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Accessibility of data
- **Affected element** Code and data availability
- **Evidence pointer** Methods section, "Code and distribution"
- **Issue** The authors state that data and code are available on GitHub, but the specific repository structure and the exact contents of the repository are not described.
- **Required correction** The authors should provide a brief description of the contents of the GitHub repository, including the parameter files, simulation input files, and analysis scripts.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Discussion of limitations
- **Affected element** Discussion section, "Limitations and caveats"
- **Evidence pointer** Discussion section
- **Issue** The discussion of limitations focuses primarily on the ABSINTH model and fixed-charge force fields. The authors do not discuss the limitations of their validation approach, such as the reliance on published data from different laboratories and the potential for systematic differences between experimental and computational methods.
- **Required correction** The authors should add a brief discussion of the limitations of their validation approach and the potential for systematic biases in the comparison to published data.

- **Technical failings that need to be addressed before the case is established**
  - R1-M1: The physical justification for the hybrid charge/FOS combination (z = -1 with -2 FOS) needs to be more clearly articulated.
  - R1-M2: The quantitative comparison to published data needs to be more rigorous and systematic across all four test systems.

- **Assessment against Nature-style criteria**
  - **Originality**: The work addresses a clear gap in available simulation tools for phosphorylated IDRs. While the general approach of parameter development and validation is not novel, the specific application to phosphoserine and phosphothreonine in the ABSINTH model fills a practical need. The exploration of phosphorylation site combinations in Ash1 and PAGE4 provides some novel insights, though the analysis is somewhat descriptive.
  - **Scientific importance**: The work is of importance to the IDR simulation community, as it provides a validated parameter set for a widely used simulation model. The findings on the differential effects of phosphomimetics versus true phosphorylation are also of practical importance. However, the broader biological implications of the work are somewhat limited, as the manuscript focuses primarily on methodological development and validation.
  - **Interdisciplinary readership**: The work is likely to be of interest primarily to computational biophysicists and researchers in the IDR field. The practical guidance on phosphomimetic usage may also be of interest to experimentalists, but the technical nature of the manuscript may limit its appeal to a broader interdisciplinary audience.
  - **Technical soundness**: The overall approach is technically sound, but several aspects require clarification and additional analysis, as detailed in the Major Concerns. In particular, the justification for the hybrid charge/FOS combination and the rigor of the quantitative validation need to be strengthened.
  - **Readability for nonspecialists**: The manuscript is clearly written and the figures are informative. However, the technical nature of the parameter implementation and validation may be challenging for nonspecialists. The authors make an effort to explain the significance of their work, but the level of detail may be more appropriate for a specialized journal.

- **Recommendation posture** Supportive if technical concerns are resolved. The manuscript addresses a clear need and the reported results are encouraging. However, the concerns regarding the justification of the parameter choices and the rigor of the quantitative validation need to be addressed before the parameter set can be considered fully validated and broadly useful to the community.

## Risk / unsupported claims
- The claim of "near-quantitative agreement" with published findings is not consistently supported by rigorous quantitative comparisons across all four test systems.
- The physical basis for the hybrid charge/FOS combination (z = -1 with -2 FOS) is not clearly established.
- The claim that Na+ chelation is "almost certainly artifactual" is presented as a tentative suggestion, but the evidence supporting this claim is not fully presented.
- The statement that "the same underlying amino acid sequence can occupy distinct phospho-dependent conformational ensembles" is a reasonable interpretation of the results, but the analysis supporting this claim is somewhat descriptive and would benefit from a more quantitative framework.