## Review setup
- **Input scope** Full manuscript text including abstract, results, discussion, and experimental procedures
- **Assessment boundary** Scientific validity, technical soundness, and significance of the claims as presented in the provided text
- **Shared manuscript claim summary** The authors develop modular MAP-IDR condensates (synMAPs) that enable inducible assembly of higher-order microtubule structures in vitro and in mammalian cells, using the TPPP microtubule-binding domain fused to orthogonal phase-separating IDR sequences, with regulation achieved through small molecules or cell signaling inputs
- **Visible evidence base** Figures 1-6 referenced in text, Supplemental Figures S1-S9, Videos S1-S8, experimental procedures
- **Missing materials affecting confidence** Actual figure images, supplemental data files, numerical source data, statistical analysis details, and video files were not provided for independent verification

## Reviewer
- **Overall assessment** This manuscript presents a conceptually interesting synthetic biology approach to controlling microtubule architecture through engineered condensate-forming proteins. The central idea, that a weak microtubule-binding domain can be rewired by fusion to unrelated phase-separating IDR sequences to generate regulatable higher-order structures, is novel and potentially impactful for the synthetic biology and cytoskeleton fields. The systematic comparison of different IDR sequences and TPPP truncation variants provides a useful framework for understanding how condensate properties relate to microtubule bundling activity. However, several technical concerns regarding the quantitative rigor of the assays, the mechanistic interpretation of the results, and the generalizability of the findings need to be addressed before the case is fully established.

- **Who would be interested in the results, and why** Researchers in synthetic biology, cytoskeleton biology, and phase separation fields would find this work of interest. The demonstration that arbitrary IDR sequences can functionally replace native MAP IDRs to drive microtubule organization provides a platform for engineering cellular structures. The inducible circuit designs, particularly the rapamycin and PKA-responsive systems, offer tools for dynamic control of cytoskeletal architecture that could be applied in cell engineering and synthetic morphology contexts.

- **Major strengths** The modular design strategy is elegant and well-executed, with a clear progression from in vitro characterization to cellular implementation. The systematic comparison of multiple IDR sequences and TPPP variants provides a useful parameter space for understanding design rules. The demonstration of regulatable systems, including both small-molecule and signaling-responsive circuits, significantly extends the utility of the approach. The compatibility of the synthetic structures with cell division is a notable and somewhat surprising finding that suggests potential for long-term cellular applications.

- **Major Concerns**

- **Concern ID** R1-M1
- **Severity** Major
- **Blocking** Yes
- **Axis** Technical soundness of quantitative assays
- **Claim pointer** The authors claim that "bundling activity quantitatively correlates with its propensity (size and number) to form droplets" and use EC50 values from bundling assays as a quantitative metric for comparison across variants.
- **Evidence pointer** Figures 1E-G, 2F-G, Experimental procedures "Single-MT binding and MT-bundling assays"
- **Concern** The quantitative basis for comparing bundling activity across variants relies on EC50 values derived from a bundling assay where "bundled structure was defined as any structure with intensity greater than two SDs above the mean-value for the single MT distribution." This threshold-based classification may be sensitive to imaging conditions, protein aggregation state, and the presence of large condensate clusters that could be misclassified as microtubule bundles. The authors do not provide validation that this intensity-based metric accurately distinguishes true microtubule bundles from protein aggregates or condensates that happen to colocalize with microtubules. Additionally, the EC50 values are reported without confidence intervals or goodness-of-fit statistics, making it difficult to assess whether differences between variants are statistically meaningful.
- **Why it matters** The central claim of the paper, that condensate-forming propensity controls microtubule bundling activity, depends entirely on the reliability of these quantitative comparisons. If the assay cannot reliably distinguish true bundling from condensate-mediated clustering artifacts, the correlation between droplet formation and bundling activity may be overstated.
- **Resolution test** Provide validation of the bundling assay using independent methods such as electron microscopy quantification, demonstrate that the intensity threshold reliably distinguishes bundles from aggregates across all variants tested, and report EC50 values with confidence intervals and statistical comparisons between variants.

- **Concern ID** R1-M2
- **Severity** Major
- **Blocking** Yes
- **Axis** Mechanistic interpretation
- **Claim pointer** The authors state that "a function for condensates in this system could be to create the multimerization and high-valency needed to bridge multiple weak-binding events across multiple MTs into bundles" and that "synthetic modulation of TPPP condensate formation correlates with synMAP MT bundling activity."
- **Evidence pointer** Figures 1-2, Discussion
- **Concern** The proposed mechanism, that condensate formation provides multivalency to bridge weak microtubule-binding events, is plausible but not directly tested. The correlation between droplet formation and bundling activity could also be explained by other mechanisms, such as increased local concentration of the TPPP domain at the microtubule surface, changes in protein conformation upon IDR fusion, or non-specific hydrophobic interactions between condensate material and microtubules. The authors do not perform experiments that would distinguish between these possibilities, such as testing whether non-phase-separating multimerization domains (e.g., coiled-coil oligomerization domains) can substitute for IDRs, or whether the IDR sequence itself contributes to microtubule binding independent of phase separation.
- **Why it matters** The mechanistic interpretation is central to the broader claim that condensation is a general biophysical strategy for organizing microtubules. Without direct evidence for the proposed mechanism, the significance of the findings for understanding native MAP function and for guiding future design efforts is limited.
- **Resolution test** Perform control experiments with multimerization domains that do not phase separate, test whether IDR sequences alone (without TPPP) can promote bundling when artificially clustered, or use mutants that separate phase separation from microtubule binding to directly test the proposed mechanism.

- **Concern ID** R1-M3
- **Severity** Major
- **Blocking** No
- **Axis** Cellular relevance and generalizability
- **Claim pointer** The authors claim that synMAPs "enable inducible assembly of higher-order microtubule structures for synthetic exploration in vitro and in mammalian cells" and that the approach provides "a modular starting point for the design of higher-order microtubule systems."
- **Evidence pointer** Figures 3-6, Discussion
- **Concern** While the demonstration of inducible bundling in cells is impressive, the physiological relevance and generalizability of the approach remain unclear. The experiments are performed in 3T3 fibroblasts, which do not natively express TPPP or exhibit the specialized microtubule architectures found in oligodendrocytes. The authors do not demonstrate that the synMAP approach can generate specific, functionally relevant microtubule structures (e.g., the parallel arrays found in oligodendrocyte processes) or that the structures formed have any functional consequences for cell behavior. Additionally, the reliance on overexpression and the potential for off-target effects of large condensate formation in cells are not addressed.
- **Why it matters** The stated goal of the work is to provide a platform for engineering microtubule structures. To establish this, it is important to demonstrate that the approach can generate structures with defined geometry and function, and that the approach is not limited to a single cell type or context.
- **Resolution test** Demonstrate formation of specific microtubule architectures in a cell type with polarized morphology, show functional consequences of the engineered structures, or provide evidence that the approach can be generalized to other microtubule-binding domains and IDR sequences.

- **Concern ID** R1-M4
- **Severity** Major
- **Blocking** No
- **Axis** Missing controls and validation
- **Claim pointer** The authors state that "TPPP-FL phase-separated to form droplets under a wide range of different molecular crowding conditions" and that "no droplets were observed for TPPP-CORE under any conditions tested."
- **Evidence pointer** Figure 1C, Supplemental Figure S1
- **Concern** The droplet formation assays appear to lack important controls. The authors do not report testing whether the GFP tag itself contributes to phase separation, whether the observed droplets are indeed liquid-like (e.g., through fusion events, circularity measurements, or rheological characterization), or whether the droplets represent specific interactions or non-specific aggregation. The FRAP experiments show recovery, which is suggestive of liquid-like behavior, but quantitative recovery fractions and mobile fractions are not reported. Additionally, the claim that TPPP-CORE shows "no droplets under any conditions tested" is a negative result that would benefit from positive controls demonstrating that the assay conditions are capable of supporting droplet formation.
- **Why it matters** The phase separation behavior of the constructs is central to the proposed mechanism. Without proper characterization of the material properties of the droplets and appropriate controls, it is difficult to assess whether the observed phenomena are specific to the designed constructs or represent non-specific aggregation.
- **Resolution test** Include GFP-only and GFP-IDR controls in droplet assays, perform quantitative FRAP analysis with reported mobile fractions, test for liquid-like properties through droplet fusion and circularity measurements, and include positive controls for droplet formation conditions.

- **Minor Comments**

- **Concern ID** R1-m1
- **Severity** Minor
- **Axis** Statistical reporting
- **Affected element** Figures 3C, 6D, 6F, Supplemental Figures S2, S8, S9
- **Evidence pointer** Figure legends, Statistical analysis section
- **Issue** The statistical methods are described only briefly, and the figure legends do not consistently report the number of independent experiments, the specific statistical test used for each comparison, or whether multiple comparisons were corrected for. The n values reported in some figure legends appear to refer to cell numbers rather than independent experimental replicates.
- **Required correction** Provide a detailed description of the statistical methods used for each figure, including the number of independent experiments, the specific tests performed, and the correction method for multiple comparisons. Clarify whether n refers to cells, experiments, or technical replicates.

- **Concern ID** R1-m2
- **Severity** Minor
- **Axis** Clarity of methods
- **Affected element** Experimental procedures, "Single-MT binding and MT-bundling assays"
- **Evidence pointer** Experimental procedures
- **Issue** The description of the single-MT binding assay is incomplete. The authors do not specify how binding was quantified, what concentrations were tested, how the binding constant was determined, or how many replicates were performed. The relationship between the binding assay and the bundling assay is also not clearly explained.
- **Required correction** Provide a complete description of the single-MT binding assay, including the quantification method, concentration range tested, and the number of replicates. Clarify how binding affinity was calculated and how it relates to the bundling activity measurements.

- **Concern ID** R1-m3
- **Severity** Minor
- **Axis** Figure presentation
- **Affected element** Figures 4-6
- **Evidence pointer** Figure legends
- **Issue** The figure legends for the cellular experiments do not clearly indicate the time points at which images were acquired, the number of cells analyzed, or the criteria used to select representative images. The quantification methods for the cellular bundling assays are described only in general terms.
- **Required correction** Provide detailed information about the imaging time points, the number of cells analyzed per condition, the criteria for selecting representative images, and a complete description of the quantification method used for the cellular bundling assays.

- **Concern ID** R1-m4
- **Severity** Minor
- **Axis** Discussion of limitations
- **Affected element** Discussion
- **Evidence pointer** Discussion
- **Issue** The discussion does not adequately address the limitations of the approach, including the potential for non-specific effects of large condensate formation, the lack of functional readouts for the engineered structures, and the uncertainty regarding whether the observed mechanisms reflect those used by native MAPs.
- **Required correction** Add a paragraph discussing the limitations of the current approach and the key questions that remain to be addressed in future work.

## Risk / unsupported claims
- The claim that "bundling activity quantitatively correlates with its propensity (size and number) to form droplets" is based on a limited number of variants and a potentially unreliable intensity-based bundling assay; the quantitative relationship is not rigorously established.
- The claim that the mechanism involves "multimerization and high-valency needed to bridge multiple weak-binding events" is plausible but not directly tested; alternative mechanisms are not excluded.
- The claim that synMAPs provide "a modular starting point for the design of higher-order microtubule systems" is supported by the demonstration of several variants, but the generalizability to other MT-binding domains and IDR sequences is not demonstrated.
- The claim that the approach "provide[s] evidence supporting the sufficiency of condensation as a general biophysical strategy for organizing MTs" is an extrapolation from the specific system studied and is not directly supported by the data.
- The cellular relevance of the findings is limited by the use of a single cell type and the lack of functional readouts; the claim that the approach could be used to generate specific microtubule architectures with defined functions is not demonstrated.