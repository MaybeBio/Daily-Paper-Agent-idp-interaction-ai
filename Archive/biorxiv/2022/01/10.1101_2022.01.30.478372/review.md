## Review setup
- **Input scope** Full manuscript text, including summary, highlights, introduction, results, discussion, limitations, and methods.
- **Assessment boundary** Scientific validity, technical soundness, and support of claims based solely on the provided manuscript text. No external data or figures were available for direct inspection.
- **Shared manuscript claim summary** The authors propose that glucose starvation in yeast triggers the formation of nuclear Nab2-containing RNA-dependent condensates, which retain poly(A) mRNA in the nucleus. This retention is linked to reduced Dbp5 at the nuclear pore complex (NPC), and the degree of condensation correlates with the extent of mRNA retention, suggesting a regulatory role for condensation in mRNA export during stress.
- **Visible evidence base** Text descriptions of results, including FRAP, RNA FISH, smFISH, live-cell imaging, in vitro droplet assays, RNA-seq, and growth recovery assays. Figures and tables are referenced but not directly viewable.
- **Missing materials affecting confidence** Actual figures, supplementary figures, videos, and tables are not provided. This limits verification of quantitative data, image quality, and statistical analyses. Specific numerical values for FRAP recovery, RNA quantification, and sequencing data are largely absent from the text.

## Reviewer
- **Overall assessment** This manuscript presents a compelling and novel hypothesis that Nab2 condensation mediates mRNA retention during glucose stress, linking a physiological stress response to a biophysical mechanism. The combination of in vivo imaging, in vitro reconstitution, and mutant analysis is a strength. However, the current text lacks sufficient quantitative detail and direct evidence for several key claims, particularly the causal relationship between Dbp5 loss and Nab2 condensation, and the specificity of mRNA retention. The manuscript would be significantly strengthened by providing more rigorous quantitative data and addressing alternative explanations.
- **Who would be interested in the results, and why** Researchers in the fields of RNA biology, nuclear transport, and biomolecular condensates. The work is relevant to those studying stress responses, gene expression regulation, and the biophysical principles of phase separation. The potential conservation of this mechanism in higher eukaryotes would broaden its appeal to cell biologists.
- **Major strengths**
    1.  The study addresses a fundamental and poorly understood question: how is mRNA export regulated during stress?
    2.  The use of a multi-pronged approach (in vivo imaging, in vitro biochemistry, and genetics) is robust.
    3.  The identification of a specific mutant (interface mutant) that reduces condensation and alters mRNA retention provides a strong causal link.
    4.  The finding that IDR deletion leads to more solid-like condensates and increased retention is counterintuitive and interesting, challenging simple models of IDR-driven phase separation.
- **Major Concerns**
    - **Concern ID** R1-M1
    - **Severity** Major
    - **Blocking** Yes
    - **Axis** Causal link between Dbp5 loss and Nab2 condensation
    - **Claim pointer** The authors state that "Dbp5 depletion... is necessary and sufficient to trigger Nab2 condensation" and that glucose stress causes "reduced abundance of the DEAD-box ATPase Dbp5 at the nuclear pore," which is implied to be the trigger for Nab2 condensation.
    - **Evidence pointer** Results section "Acute Dbp5 depletion causes nuclear mRNA accumulation and Nab2 mobility reduction" and "Glucose stress causes reduction of nuclear Nab2 dynamics and bulk nuclear mRNA retention".
    - **Concern** The text shows a correlation between Dbp5 depletion and Nab2 condensation, but the causal link is not fully established. The "Dbp5 tether" experiment (Figure 2I) shows that preventing Dbp5 loss reduces Nab2 foci, but it is unclear if this is due to restored mRNA export or a direct effect on Nab2. The manuscript does not demonstrate that Dbp5's ATPase activity or its interaction with Nab2 is directly responsible for preventing condensation. The sufficiency claim is also not directly tested; the authors do not show that simply removing Dbp5 from the NPC in the absence of other stress signals is enough to induce condensation.
    - **Why it matters** This is a central claim of the paper. If the link is indirect (e.g., through mRNA accumulation), the model is less specific. The paper's title and abstract imply a direct regulatory mechanism, which is not fully supported.
    - **Resolution test** The authors should perform experiments to distinguish between a direct and indirect role for Dbp5. For example, they could tether Dbp5 to the NPC during glucose stress and show that this is sufficient to prevent Nab2 condensation and mRNA retention. Alternatively, they could acutely inactivate Dbp5's ATPase activity without depleting it and assess Nab2 condensation. A more direct test would be to show that Dbp5 can remodel or dissolve Nab2-RNA condensates in vitro.
    - **Concern ID** R1-M2
    - **Severity** Major
    - **Blocking** Yes
    - **Axis** Specificity of mRNA retention
    - **Claim pointer** The authors claim that "glucose stress leads to poly(A) RNA retention in the nucleus" and that this is affected by the state of the Nab2 condensate. They further suggest a "dose-dependent effect of the Nab2 condensate on nuclear mRNA retention."
    - **Evidence pointer** Results section "In glucose stress Nab2 condensation leads to RNA retention in an RNA dose-dependent manner and affects survival after prolonged stress".
    - **Concern** The manuscript does not clearly demonstrate whether the retention is specific to certain mRNAs or a general block of all poly(A) RNA. The RNA-seq data from nuclear fractions shows a global increase in reads for the IDR mutant, but the smFISH data suggests differential retention of specific transcripts (e.g., BTN2, HSP42, HXT6) versus others (DED1). The authors attribute this to abundance, but it could also reflect sequence-specific or mRNP-composition-specific retention. The claim of "dose-dependent" retention is based on the correlation between condensate formation and retention, but a direct titration of condensate "dose" is not performed.
    - **Why it matters** The model proposes a general mechanism for mRNA storage during stress. If retention is selective, it suggests a more sophisticated regulatory mechanism that is not fully explored. The discrepancy between RNA-seq and smFISH results is a concern that is not fully resolved.
    - **Resolution test** The authors should perform a more detailed analysis of the retained mRNAs. For example, they could identify the full set of retained transcripts in the IDR mutant and compare their features (length, codon bias, etc.) to non-retained transcripts. They could also perform a time-course experiment to see if retention is dynamic and if certain mRNAs are preferentially released upon recovery.
    - **Concern ID** R1-M3
    - **Severity** Major
    - **Blocking** No
    - **Axis** In vivo relevance of in vitro condensate properties
    - **Claim pointer** The authors state that "The state of Nab2 condensation influences the extent of nuclear mRNA accumulation" and use in vitro droplet assays to define the material properties of wild-type and mutant condensates.
    - **Evidence pointer** Results section "Nab2 forms condensates in vitro" and "Nab2 condensation properties influence the degree of nuclear mRNA retention".
    - **Concern** The in vitro droplet assays are performed with purified components and may not accurately reflect the complex environment of the nucleus. The authors show that the IDR mutant forms more solid-like condensates in vitro and larger foci in vivo, but the link between these two observations is correlative. The text does not provide a quantitative comparison of the in vitro material properties (e.g., viscosity, FRAP recovery rates) with the in vivo behavior (e.g., foci size, mobility). It is unclear if the "solid-like" nature of the IDR mutant condensates is the direct cause of increased mRNA retention or if other factors are involved.
    - **Why it matters** The paper aims to establish a mechanistic link between condensation and mRNA retention. If the in vitro properties do not directly translate to in vivo function, the model is weakened.
    - **Resolution test** The authors could perform FRAP experiments on the in vivo foci to directly measure their material properties and compare them to the in vitro data. They could also test whether the in vitro condensates can sequester mRNA in a manner that prevents its release, and if this is altered by the mutations.
- **Minor Comments**
    - **Concern ID** R1-m1
    - **Severity** Minor
    - **Axis** Clarity of model
    - **Affected element** Discussion and model figure (Figure 7H)
    - **Evidence pointer** Discussion section
    - **Issue** The proposed model is somewhat vague regarding the order of events. Does Dbp5 loss directly trigger Nab2 condensation, or does mRNA accumulation in the nucleus (due to export block) provide the RNA substrate that promotes condensation? The text suggests both possibilities but does not clearly distinguish them.
    - **Required correction** The model should be clarified to explicitly state the proposed sequence of events and the role of Dbp5. A more detailed schematic would be helpful.
    - **Concern ID** R1-m2
    - **Severity** Minor
    - **Axis** Quantitative data presentation
    - **Affected element** Results sections
    - **Evidence pointer** Figures 1, 2, 4, 5, 6, 7
    - **Issue** The text frequently refers to qualitative observations (e.g., "reduced," "increased," "more static") without providing specific quantitative values or statistical test results in the main text. This makes it difficult to assess the magnitude and significance of the effects.
    - **Required correction** Include key quantitative data (e.g., mean ± SEM, p-values) in the text or figure legends for all major conclusions.
    - **Concern ID** R1-m3
    - **Severity** Minor
    - **Axis** Technical detail
    - **Affected element** Methods section "Live single molecule RNA analysis"
    - **Evidence pointer** Methods section
    - **Issue** The threshold for classifying mRNAs as "static" or "dynamic" in Figure 7E,F is defined, but the rationale for this specific value is not provided. It is unclear if the results are sensitive to this threshold.
    - **Required correction** Provide a justification for the chosen threshold or show that the results are robust to changes in the threshold.
    - **Concern ID** R1-m4
    - **Severity** Minor
    - **Axis** Data interpretation
    - **Affected element** Results section "In glucose stress Nab2 condensation leads to RNA retention in an RNA dose-dependent manner and affects survival after prolonged stress"
    - **Evidence pointer** Figure 7G
    - **Issue** The growth recovery assay shows a slight growth disadvantage for the IDR mutant, which is exacerbated after stress. However, the text does not discuss whether this is due to the inability to properly release mRNA from condensates, or if it is a general fitness defect of the mutant.
    - **Required correction** Discuss the potential reasons for the growth defect and whether it is specifically linked to the mRNA retention phenotype.

## Risk / unsupported claims
- The claim that Dbp5 depletion is "sufficient" to trigger Nab2 condensation is not directly supported by the provided text, as no experiment shows that Dbp5 depletion alone, in the absence of other stress signals, induces condensation.
- The claim that the "state of Nab2 condensation influences the extent of nuclear mRNA accumulation" is supported by correlation, but a direct causal link is not fully established.
- The physiological relevance of the in vitro droplet properties to the in vivo mechanism is inferred but not directly demonstrated.
- The specificity of mRNA retention (general vs. selective) is not resolved, and the discrepancy between RNA-seq and smFISH data is not fully explained.
- The text mentions "RNA dose-dependent manner" but does not provide a clear experimental design that directly tests this.