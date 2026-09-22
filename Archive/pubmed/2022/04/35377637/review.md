## Review setup
- **Input scope** Abstract only
- **Assessment boundary** Claims and conclusions as stated in the abstract; no methods, figures, or quantitative results were available for evaluation
- **Shared manuscript claim summary** The authors report that Martini 3 underestimates the global dimensions of intrinsically disordered proteins and multidomain proteins relative to small-angle X-ray scattering data, and that increasing protein-water interaction strength by approximately 10% improves agreement with SAXS data, self-association behavior, and paramagnetic relaxation enhancement data for most IDPs, while noting residual deviations for some systems.
- **Visible evidence base** Abstract text only; no methods section, figures, tables, or supplementary materials were provided
- **Missing materials affecting confidence** Full methods, force field parameter details, simulation protocols, SAXS data sources and fitting procedures, PRE data analysis, system list, error estimates, and comparison statistics; without these, quantitative claims cannot be independently assessed

## Reviewer
- **Overall assessment** The abstract presents a potentially valuable empirical correction to a widely used coarse-grained force field, with clear relevance to the biomolecular simulation community. The central claim, that a 10% increase in protein-water interaction strength improves agreement with multiple experimental observables, is plausible and mechanistically reasonable. However, the abstract alone does not provide sufficient detail to evaluate the robustness of this correction, the magnitude of reported improvements, the consistency across systems, or the potential for unintended consequences in other applications. The work appears to be a useful incremental contribution, but the strength of the claims as stated cannot be fully verified from the supplied material.
- **Who would be interested in the results, and why** Researchers using coarse-grained simulations to study intrinsically disordered proteins, multidomain proteins, and protein self-assembly would find this work directly applicable. Developers of coarse-grained force fields and those interested in transferable parameter optimization would also benefit. The findings may be of interest to experimentalists using SAXS or PRE to benchmark simulations, as the improved force field could enhance the utility of Martini 3 for interpreting conformational ensembles.
- **Major strengths** The study addresses a recognized limitation of a widely used force field, namely the compaction of disordered and multidomain proteins. The proposed correction is simple and physically motivated, targeting protein-water interactions rather than introducing system-specific adjustments. The use of multiple experimental observables, including SAXS, self-association behavior, and PRE data, provides a broad benchmark. The authors acknowledge residual deviations, indicating a balanced assessment of the correction's scope.
- **Major Concerns**  
  - **Concern ID** R1-M1  
    **Severity** Major  
    **Blocking** Yes  
    **Axis** Technical soundness  
    **Claim pointer** The claim that increasing protein-water interaction strength by approximately 10% results in improved agreement with SAXS data for IDPs and multidomain proteins.  
    **Evidence pointer** Abstract only; no figures or tables provided  
    **Concern** The abstract does not report the magnitude of improvement, the number of proteins tested, the range of system sizes, or the statistical significance of the improvements. Without these details, it is unclear whether the 10% correction is broadly applicable or tuned to a limited set of cases.  
    **Why it matters** A force field correction must demonstrate consistent performance across a diverse test set to be considered a general improvement. If the improvement is marginal or system-dependent, the claim of substantial improvement is not supported.  
    **Resolution test** Provide a table or figure showing per-protein changes in radius of gyration or scattering profiles before and after correction, with error bars and a statistical test comparing agreement with SAXS data.  
  - **Concern ID** R1-M2  
    **Severity** Major  
    **Blocking** Yes  
    **Axis** Technical soundness  
    **Claim pointer** The claim that the revised force field results in a more accurate description of self-association of IDPs and folded proteins.  
    **Evidence pointer** Abstract only; no methods or results provided  
    **Concern** Self-association is a complex property that depends on both interaction strengths and sampling. The abstract does not specify which systems were tested, what experimental data were used for comparison, or how self-association was quantified.  
    **Why it matters** If the correction improves dimensions but alters self-association in unintended ways, the net benefit of the force field change is unclear. The claim of improved self-association requires explicit evidence.  
    **Resolution test** Describe the self-association assay, list the proteins tested, and show quantitative comparison to experimental association constants or cluster size distributions.  
  - **Concern ID** R1-M3  
    **Severity** Major  
    **Blocking** No  
    **Axis** Scientific importance  
    **Claim pointer** The claim that the revised force field is a substantial improvement for coarse-grained simulations of soluble proteins.  
    **Evidence pointer** Abstract only; no comprehensive benchmark provided  
    **Concern** The abstract notes residual deviations for some systems, but does not indicate the proportion of systems showing improvement versus those showing no change or worsening. The overall assessment of "substantial improvement" may be overstated if a significant fraction of systems do not benefit.  
    **Why it matters** The generalizability of the correction is central to its utility. If the improvement is limited to a subset of proteins, the claim of a broad improvement is not justified.  
    **Resolution test** Provide a summary of performance across all tested systems, including cases where agreement did not improve, and discuss potential reasons for these outliers.
- **Minor Comments**  
  - **Concern ID** R1-m1  
    **Severity** Minor  
    **Axis** Readability for nonspecialists  
    **Affected element** Abstract text  
    **Evidence pointer** Abstract  
    **Issue** The abstract uses terms such as "global dimensions" and "self-association" without defining them in the context of the study, which may be unclear to readers outside the simulation community.  
    **Required correction** Briefly define these terms or provide context, such as "global dimensions, as measured by the radius of gyration" and "self-association, referring to the tendency of proteins to form oligomers."  
  - **Concern ID** R1-m2  
    **Severity** Minor  
    **Axis** Technical soundness  
    **Affected element** Force field modification description  
    **Evidence pointer** Abstract  
    **Issue** The abstract states that protein-water interactions were increased by approximately 10%, but does not specify how this was implemented in the Martini 3 framework, such as which interaction types or parameters were modified.  
    **Required correction** Provide a brief description of the parameter change, such as scaling of specific Lennard-Jones parameters or adjustment of water-protein interaction levels.  
  - **Concern ID** R1-m3  
    **Severity** Minor  
    **Axis** Interdisciplinary readership  
    **Affected element** Experimental data usage  
    **Evidence pointer** Abstract  
    **Issue** The abstract mentions SAXS and PRE data but does not indicate the source or diversity of these experimental datasets, which is relevant for readers assessing the breadth of validation.  
    **Required correction** State the number of proteins with available SAXS and PRE data and the range of sequence properties covered, such as net charge or hydrophobicity.
- **Technical failings that need to be addressed before the case is established** R1-M1 and R1-M2 are blocking because the abstract does not provide sufficient quantitative evidence to support the central claims of improved agreement with SAXS and self-association data. The lack of methodological detail prevents assessment of the correction's implementation and potential artifacts.
- **Assessment against Nature-style criteria**  
  - **Originality** The work is incremental, proposing a simple parameter adjustment to an existing force field. While useful, it does not introduce a fundamentally new approach or conceptual advance.  
  - **Scientific importance** The correction addresses a practical limitation of a widely used tool, which is valuable for the simulation community, but the impact is limited to users of Martini 3 and does not broadly advance the field.  
  - **Interdisciplinary readership** The findings are primarily relevant to computational biophysicists and force field developers. Experimentalists using SAXS or PRE may find the improved force field useful, but the abstract does not frame the work for a broader audience.  
  - **Technical soundness** The central claims are plausible but not verifiable from the abstract alone. The lack of quantitative results and methodological detail prevents a full assessment.  
  - **Readability for nonspecialists** The abstract is concise but uses technical jargon without sufficient context, limiting accessibility to readers outside the immediate field.  
  Overall, the work does not meet the threshold for a Nature-style publication, which requires broad significance and methodological novelty. It is better suited for a specialized journal.
- **Recommendation posture** Currently not established from the provided evidence. The abstract presents a reasonable hypothesis and preliminary support, but the absence of quantitative results and methodological detail means the central claims cannot be evaluated. If the full manuscript provides robust evidence across a diverse test set, the work could be considered a useful contribution to the field, but it would not meet the standards of a high-impact general journal.

## Risk / unsupported claims
- The claim of "substantial improvement" is unsupported without a comprehensive benchmark showing the proportion of systems that improve.
- The claim of improved self-association is unsupported without specific experimental comparisons.
- The claim of better agreement with PRE data for "most IDPs" is unquantified and cannot be assessed.
- The generalizability of the 10% correction to all soluble proteins is not established from the abstract.