## Review setup
- **Input scope** Full manuscript text (abstract, introduction, results, discussion, conclusion, experimental section)
- **Assessment boundary** Scientific content, methodology, data interpretation, and claims as presented in the provided text; no access to figures, tables, or supplementary materials beyond what is described
- **Shared manuscript claim summary** The authors use real-time NMR to quantify JNK1-dependent phosphorylation of all eleven S/T-P sites in the 450-residue intrinsically disordered JIP1 IDR. By mutating the D- and F-docking motifs, they dissect contributions from docking-site-dependent and -independent mechanisms, finding that the D-motif enhances phosphorylation of C-terminal sites up to ~120 residues away, the F-motif primarily affects T205, and docking-site-independent phosphorylation correlates with intrinsic JNK1 sequence preferences. Structural ensemble calculations of local effective concentrations support the observed spatial range of D-motif effects.
- **Visible evidence base** Text descriptions of results, figures (Figure 1–5 referenced), tables (Table S1–S2 referenced), equations (1–3), experimental methods
- **Missing materials affecting confidence** All figures, tables, supplementary information, raw kinetic data, structural ensemble details, and statistical analyses are not directly accessible; confidence in quantitative claims is therefore limited

## Reviewer

- **Overall assessment** This manuscript addresses an important and timely question in MAPK signaling: how docking motifs and local sequence context jointly determine phosphorylation efficiency across a long intrinsically disordered substrate. The experimental design is thoughtful, combining real-time NMR with targeted mutations and computational modeling. The finding that the D-motif exerts long-range directional effects on phosphorylation efficiency is novel and mechanistically informative. However, the manuscript has several technical and interpretive weaknesses that need to be addressed, particularly regarding the quantitative analysis of kinetic data, the interpretation of F-motif contributions, and the robustness of the computational predictions. The work is potentially suitable for a high-impact venue, but the current evidence does not fully establish all claims.

- **Who would be interested in the results, and why** Researchers in cell signaling, particularly those studying MAPK pathways, kinase-substrate specificity, and scaffold proteins. The work also has relevance for the intrinsically disordered protein community, as it provides quantitative insights into how disorder and docking motifs cooperate in enzyme-substrate recognition. Additionally, those interested in quantitative phosphoproteomics and NMR-based kinetic analysis of post-translational modifications would find the methodological approach valuable.

- **Major strengths**
  1. The use of real-time NMR to monitor phosphorylation at all eleven S/T-P sites simultaneously in a long IDR is technically impressive and provides unprecedented site-specific kinetic resolution.
  2. The systematic mutation of D- and F-motifs, individually and in combination, allows clean dissection of docking-site-dependent versus -independent contributions.
  3. The integration of structural ensemble calculations with experimental kinetic data provides a mechanistic framework for interpreting the observed spatial range of D-motif effects.
  4. The identification of a defined phosphorylation order within the S197/T201/T205 cluster adds mechanistic detail to the distributive phosphorylation model.

- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Data analysis and interpretation
- **Claim pointer** "The phosphorylation kinetics of all eleven S/T-P sites show no discernible latency phase" and "Analysis of the data using Equation (2) shows that some sites fail to reach full phosphorylation, likely due to ATP depletion"
- **Evidence pointer** Results section "The S/T-P Sites in JIP1 are Phosphorylated with Different Efficiencies"; Figure 1D; Equation (2)
- **Concern** The kinetic analysis relies on fitting intensity data to a single-exponential model (Equation 2). However, for a distributive mechanism with multiple phosphorylation events, the kinetics of individual sites could be more complex, especially if sites are phosphorylated in a defined order (as shown for the S197/T201/T205 cluster). The authors do not demonstrate that the single-exponential model adequately fits the data for all sites, nor do they report goodness-of-fit statistics or residuals. Additionally, the claim of "no discernible latency phase" is made without showing the raw kinetic traces or providing statistical evidence for the absence of a lag.
- **Why it matters** The quantitative rate constants derived from this analysis underpin all subsequent comparisons between wild-type and mutant constructs. If the kinetic model is inappropriate or the fits are poor, the reported rate ratios and conclusions about D- and F-motif contributions could be quantitatively unreliable.
- **Resolution test** Provide representative kinetic traces with fitted curves and residuals for at least a subset of sites (e.g., fast, intermediate, slow). Report goodness-of-fit metrics (e.g., R², chi-squared) for all sites. Justify the use of a single-exponential model, particularly for sites within the clustered region where ordered phosphorylation occurs.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Evidence sufficiency
- **Claim pointer** "The D-motif selectively promotes phosphorylation in the C-terminal direction, remarkably enhancing the phosphorylation efficiency of S/T-P sites located at sequence distances exceeding 120 amino acids"
- **Evidence pointer** Results section "The D-Motif Strongly Directs the Phosphorylation Pattern of JIP1"; Figures 2B, 2C, 3; Table S2
- **Concern** The claim of a 120-amino-acid range for D-motif effects is based on comparing rate ratios between JIP1F-mut and JIP1D-F-mut + peptide. However, the authors do not provide a clear statistical framework for determining when a rate difference is significant. For sites with very slow phosphorylation rates (e.g., those far from the D-motif), the signal-to-noise ratio in the NMR measurements may be low, making rate estimates unreliable. Additionally, the comparison between JIP1F-mut and JIP1D-F-mut + peptide assumes that the D-motif peptide fully saturates the DRS and does not have off-target effects, but this is not explicitly validated.
- **Why it matters** The 120-amino-acid range is a central quantitative claim of the paper. If the rate measurements for distant sites are noisy or the peptide saturation is incomplete, the apparent spatial range could be over- or underestimated.
- **Resolution test** Provide confidence intervals or error estimates for the rate ratios at each site. Validate DRS saturation by the peptide (e.g., using a binding assay or showing that higher peptide concentrations do not further change rates). Consider alternative explanations for rate differences, such as changes in local sequence context or phosphorylation-dependent feedback.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Computational modeling validation
- **Claim pointer** "The influence of the D-motif on phosphorylation rates can be predicted by local effective concentrations" and "the D-motif enhances the effective concentration of residues up to around 140 amino acids in the C-terminal direction"
- **Evidence pointer** Results section "The Influence of the D-Motif on Phosphorylation Rates can be Predicted by Local Effective Concentrations"; Figure 4B; Equation (3)
- **Concern** The structural ensemble calculations are described only briefly. The authors state that 400,000 conformations were generated using MoMA, but no details are provided on the force field, sampling protocol, or convergence criteria. The comparison between calculated Ceff values and experimental rate ratios is described as "qualitative," but the degree of agreement is not quantified. It is unclear whether the model can distinguish between different sites with similar Ceff values or whether the correlation is driven by a few outliers.
- **Why it matters** The computational model is used to support the mechanistic interpretation of D-motif effects. Without proper validation and quantitative comparison, the predictive power of the model remains uncertain, and the claim that Ceff predicts phosphorylation rates is not firmly established.
- **Resolution test** Provide details of the ensemble generation and demonstrate convergence. Quantify the correlation between Ceff and experimental rate ratios (e.g., Spearman rank correlation with confidence intervals). Show that the model can recapitulate the observed directionality and spatial range. Discuss limitations of the model, such as the assumption of a static kinase structure and the neglect of electrostatic or dynamic effects.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Interpretation of F-motif function
- **Claim pointer** "The F-motif primarily promotes phosphorylation of a site located immediately N-terminal to the F-motif" and "T205 shows the most pronounced reduction in phosphorylation rate, decreasing by 2-fold"
- **Evidence pointer** Results section "The F-Motif Mainly Impacts Phosphorylation of T205"; Figure 2B, 2C; Table S2
- **Concern** The authors conclude that the F-motif mainly affects T205, but the mechanism is not fully explored. The F-motif has low intrinsic affinity (Kd = 2.2 mM) and only achieves high occupancy (78%) when the D-motif is also bound. The authors do not discuss whether the F-motif effect on T205 is due to direct tethering or to allosteric changes in the kinase. Additionally, the modest effects on other sites (1.2-1.4-fold reductions) are described as "smaller reductions" but are not statistically distinguished from no effect.
- **Why it matters** Understanding the specific role of the F-motif is important for the general model of bipartite substrate binding. If the F-motif only affects one site, this has implications for how F-motifs function in other substrates.
- **Resolution test** Perform additional experiments to dissect the F-motif mechanism, such as using a phosphomimetic or phosphoablative mutation at T205 to test for feedback effects. Provide statistical comparisons of rate ratios for all sites between JIP1WT and JIP1F-mut. Discuss whether the F-motif effect is consistent with a simple tethering model or requires additional explanations.

- **Concern ID** R1-M5
- **Severity** Major
- **Blocking** No
- **Axis** Generalizability of findings
- **Claim pointer** "The work highlights how docking site motifs and sequence context synergistically regulate phosphorylation efficiency, emphasizing the critical role of substrate architecture in determining MAPK-mediated signaling outcomes"
- **Evidence pointer** Discussion section; Conclusion
- **Concern** The study is limited to a single substrate (JIP1) and a single kinase (JNK1). While the authors discuss implications for other MAPK substrates, no evidence is provided that the observed principles generalize. The specific spatial range of D-motif effects (120 amino acids) may depend on the intrinsic flexibility and length of JIP1, and may not apply to other IDRs with different sequence properties.
- **Why it matters** The broader significance of the work depends on the generalizability of the findings. If the observed effects are specific to JIP1, the impact on the field is more limited.
- **Resolution test** Discuss the sequence and structural features of JIP1 that may influence the observed spatial range. Compare with existing data on other MAPK substrates where available. Suggest specific predictions that could be tested in other systems.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Clarity of presentation
- **Affected element** Figure 1C description
- **Evidence pointer** Results section "JNK1 Phosphorylates All S/T-P Sites within the IDR of JIP1"; Figure 1C
- **Issue** The text states that "resonances of phosphorylated serines and threonines appear in a distinct region of the 1H-15N HSQC spectrum" but does not specify how many resonances were observed or whether all eleven expected phosphosites were detected in a single experiment.
- **Required correction** Clarify the number of distinct phospho-resonances observed and whether any expected sites were not detected or overlapped.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Methodological detail
- **Affected element** NMR assignment strategy
- **Evidence pointer** Experimental section "NMR Spectroscopy and Data Analysis"
- **Issue** The assignment of phosphorylated resonances relies on triple resonance experiments of phosphorylated sub-constructs, but the text does not specify how the sub-constructs were phosphorylated or whether the phosphorylation patterns in sub-constructs match those in the full-length protein.
- **Required correction** Provide details on the phosphorylation of sub-constructs and justify the assumption that phosphorylation patterns are transferable.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Statistical reporting
- **Affected element** Rate comparisons
- **Evidence pointer** Results sections "The F-Motif Mainly Impacts Phosphorylation of T205" and "The D-Motif Strongly Directs the Phosphorylation Pattern of JIP1"; Table S2
- **Issue** The text reports fold-changes in phosphorylation rates (e.g., "2-fold" for T205) but does not report standard errors, confidence intervals, or p-values for these comparisons.
- **Required correction** Include measures of variability and statistical significance for all reported rate comparisons.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Completeness of model description
- **Affected element** Ceff calculations
- **Evidence pointer** Experimental section "Calculation of Local Effective Concentrations"; Equation (3)
- **Issue** The description of the structural ensemble generation is brief. It is unclear how the "random coil" conformations were sampled, what force field was used, and how steric clashes were defined.
- **Required correction** Provide a more detailed description of the computational methods, including software parameters and validation of the ensemble.

- **Concern ID** R1-m5
- **Severity** Minor
- **Axis** Interpretation of non-canonical sites
- **Affected element** S40 and T201 phosphorylation
- **Evidence pointer** Results section "Two Non-Canonical Sites are Phosphorylated in JIP1"
- **Issue** The identification of two non-canonical phosphorylation sites (S40 and T201) is interesting but not discussed in the context of their potential functional relevance. The authors do not speculate on whether these sites are physiologically important or simply low-efficiency off-target events.
- **Required correction** Add a brief discussion of the potential significance of non-canonical sites, or explicitly state that their functional relevance is unknown.

- **Concern ID** R1-m6
- **Severity** Minor
- **Axis** Literature context
- **Affected element** Discussion of F-motif function
- **Evidence pointer** Discussion section
- **Issue** The discussion of F-motif function could be strengthened by comparing the findings to other systems where F-motifs have been characterized, particularly regarding the spatial relationship between F-motifs and phosphorylation sites.
- **Required correction** Add a brief comparison to relevant literature on F-motif function in other MAPK substrates.

## Risk / unsupported claims
- The claim that the D-motif enhances phosphorylation of sites up to 120 amino acids away is based on rate comparisons that lack statistical rigor; the exact spatial range should be treated as approximate until confidence intervals are provided.
- The claim that "the influence of the D-motif on phosphorylation rates can be predicted by local effective concentrations" is supported only by a qualitative comparison; the predictive power of the model is not quantitatively established.
- The statement that "no discernible latency phase" exists in the kinetic profiles is not supported by shown data or statistical tests.
- The generalizability of the findings to other MAPK substrates is asserted but not demonstrated; this should be framed as a hypothesis rather than a conclusion.
- The functional significance of the two non-canonical phosphorylation sites (S40, T201) is not addressed; any implied physiological relevance is unsupported.
- The claim that dimerization does not alter phosphorylation kinetics is based on a single construct (JIP1SH3) and limited data; the possibility of subtle effects cannot be excluded from the presented evidence.