## Review setup
- **Input scope** Full manuscript text (abstract, introduction, results, discussion, materials and methods) and supplementary figure/table captions as referenced in the text. No supplementary PDF content was provided.
- **Assessment boundary** Scientific validity, technical soundness, and significance of the computational design algorithm and its experimental validation. The review is based solely on the provided manuscript text.
- **Shared manuscript claim summary** The authors present a general algorithm for designing intrinsically disordered protein (IDP) variants with specified conformational properties, such as compaction (radius of gyration, Rg) and phase separation propensity. The algorithm combines coarse-grained molecular dynamics simulations (CALVADOS) with alchemical free-energy calculations (MBAR) in a Monte Carlo sampling scheme. The authors validate the approach experimentally on variants of the A1-LCD domain of hnRNPA1, showing agreement between predicted and measured Rg and saturation concentrations (csat). They also demonstrate a machine learning (SVR) surrogate model for faster sequence design.
- **Visible evidence base** Main text figures (Fig. 1-7) and tables (Table S1-S3) are referenced but not directly viewable. The text provides quantitative results (e.g., average error of 1.5% for Rg predictions, correlation between predicted and observed csat) and qualitative descriptions of experimental outcomes.
- **Missing materials affecting confidence** The actual figures, supplementary figures (fig. S1-S14), and supplementary tables (Table S1-S3) are not provided. This limits the ability to independently assess the quality of the data, the statistical significance of the results, and the robustness of the experimental validation. The full methodological details of the SVR model training and the MBAR implementation are only partially described.

## Reviewer
- **Overall assessment** This manuscript presents a novel and potentially impactful computational method for designing IDPs with targeted conformational properties. The combination of MCMC sampling with an efficient coarse-grained model and alchemical free-energy calculations is a logical and promising approach. The experimental validation on A1-LCD variants, showing a high correlation between predicted and measured Rg and csat, is a significant strength. However, the manuscript's impact is currently tempered by several technical concerns, including the limited generalizability demonstrated (only one protein family experimentally tested), the unexplained outlier (V5) in the csat predictions, and the lack of detailed analysis of the designed sequences' novelty and functional relevance. The computational cost of the method, despite the MBAR acceleration, may also limit its broad applicability. The manuscript is well-written and accessible, but the evidence provided is not yet sufficient to fully establish the method's general utility and predictive accuracy.
- **Who would be interested in the results, and why** Researchers in the fields of computational protein design, biophysics of intrinsically disordered proteins, and biomolecular condensates. The method offers a new tool for engineering IDPs with specific properties, which could be used to create novel biomaterials, study sequence-ensemble-function relationships, and design proteins with tailored phase separation behavior. The machine learning surrogate model also makes the approach more accessible to a broader community.
- **Major strengths**
    1.  **Novel computational approach**: The integration of MCMC sequence sampling with coarse-grained simulations and alchemical free-energy calculations is a novel and elegant strategy for IDP design.
    2.  **Prospective experimental validation**: The authors provide a strong experimental test of their predictions on A1-LCD variants, including Rg from SAXS and csat from turbidity/microscopy, which is a critical and commendable step.
    3.  **Insight into sequence determinants**: The analysis linking charge patterning (κ) to compaction and phase separation provides valuable insights into the physical principles governing IDP behavior.
    4.  **Practical acceleration**: The development and validation of an SVR-based surrogate model demonstrates a clear path to making the design process much faster and more accessible.
- **Major Concerns**
    - **Concern ID** R1-M1
    - **Severity** Major
    - **Blocking** Yes
    - **Axis** Generalizability and scope of validation
    - **Claim pointer** The authors claim the algorithm is "general" and can be used to design IDPs with "specific structural properties." The experimental validation, however, is limited to a single protein, A1-LCD, and its variants.
    - **Evidence pointer** Results section "Experimental characterization of A1-LCD variants", Fig. 5
    - **Concern** The central claim of a "general algorithm" is not fully supported by the evidence. The experimental validation is performed exclusively on A1-LCD, a protein that is already relatively compact and has a strong phase separation propensity. While the authors show computational results for other proteins (αSyn, FUS-PLD, LAF-1-RGG), these are not experimentally tested. The manuscript would be significantly strengthened by experimental validation on at least one other IDP with different sequence characteristics (e.g., a more expanded or charge-balanced protein) to demonstrate the method's broad applicability and the accuracy of CALVADOS for diverse designed sequences.
    - **Why it matters** The claim of generality is a key part of the manuscript's significance. Without experimental evidence on a second, distinct system, it is unclear if the success on A1-LCD is a special case or a general feature of the method. This limits the confidence in the method's utility for the broader IDP design community.
    - **Resolution test** The authors should experimentally validate their design algorithm on at least one additional IDP from a different family with distinct sequence composition and conformational properties. If this is not feasible, the claims of generality should be appropriately tempered.
    - **Concern ID** R1-M2
    - **Severity** Major
    - **Blocking** No
    - **Axis** Predictive accuracy and outlier analysis
    - **Claim pointer** The authors state "We find a high correlation between predicted and observed values of csat (Fig. 5C), with the only outlier being V5, which is the sole variant expected to be more expanded than the WT."
    - **Evidence pointer** Results section "Experimental characterization of A1-LCD variants", Fig. 5C
    - **Concern** The manuscript identifies V5 as an outlier but does not provide a satisfactory explanation for the discrepancy between its predicted and measured csat. The authors state that additional simulations with different setups (more chains, CALVADOS 2) gave comparable results, and repurification gave comparable experimental results, but the root cause of the discrepancy remains unresolved. This is a critical point, as it suggests a potential limitation of the model for predicting the behavior of more expanded sequences.
    - **Why it matters** An unexplained outlier in the key validation dataset raises questions about the model's predictive power, particularly for the design goal of creating more expanded proteins. Understanding the source of this discrepancy (e.g., a specific sequence feature, a limitation of the force field, or an experimental artifact) is crucial for establishing the reliability of the method.
    - **Resolution test** The authors should provide a more in-depth analysis of V5's sequence and simulated ensemble to identify potential reasons for the discrepancy. This could include a detailed comparison of the contact maps, secondary structure propensities, or specific interactions in V5 versus the other variants. If no clear explanation is found, the authors should explicitly acknowledge this as a limitation of the current model.
    - **Concern ID** R1-M3
    - **Severity** Major
    - **Blocking** No
    - **Axis** Functional relevance and novelty of designed sequences
    - **Claim pointer** The authors state the work "will facilitate the design of proteins whose functions exploit the many properties afforded by protein disorder."
    - **Evidence pointer** Abstract, Discussion
    - **Concern** The manuscript focuses on structural properties (Rg, csat) but does not demonstrate any functional consequences of the designed variants. The claim that this will facilitate the design of functional proteins is speculative. The designed variants are not tested for any biological or biochemical function, and the analysis does not show whether the designed sequences represent novel functional solutions or simply recapitulate known sequence-ensemble relationships.
    - **Why it matters** The ultimate value of a protein design method lies in its ability to create proteins with new or improved functions. While designing for structural properties is a logical first step, the manuscript's impact would be significantly enhanced by demonstrating that the designed variants can perform a specific function (e.g., as a linker, a scaffold, or a regulator of phase separation) in a way that differs from the wild-type protein.
    - **Resolution test** The authors could perform a simple functional assay on a subset of the designed variants (e.g., their ability to bind a partner, their effect on a biochemical reaction, or their behavior in a cellular context). Alternatively, they could provide a more detailed bioinformatic analysis showing that the designed sequences explore regions of sequence space not occupied by natural IDPs, suggesting novel functional potential.
- **Minor Comments**
    - **Concern ID** R1-m1
    - **Severity** Minor
    - **Axis** Clarity and completeness of methods
    - **Affected element** Materials and Methods, "Alchemical free-energy calculations with MBAR"
    - **Evidence pointer** Materials and Methods section
    - **Issue** The description of the MBAR implementation is brief. The text mentions a "maximum size of the MBAR pool to 10" and a threshold for the "number of effective frames (Neff)" but does not provide details on how the pool is initialized, how the "oldest simulation is discarded," or the computational cost of the reweighting step.
    - **Required correction** Provide a more detailed description of the MBAR implementation, including the initialization, update, and discarding procedures, as well as the computational time required for a typical design run. This will allow others to reproduce the method more easily.
    - **Concern ID** R1-m2
    - **Severity** Minor
    - **Axis** Presentation of results
    - **Affected element** Results section "Experimental characterization of A1-LCD variants"
    - **Evidence pointer** Fig. 5
    - **Issue** The text states that "we find a high correlation between predicted and observed values of csat" but does not provide the correlation coefficient or the statistical significance of this correlation. Similarly, the agreement between predicted and experimental Rg is described as "good" but without quantitative metrics.
    - **Required correction** Include the correlation coefficient (e.g., Pearson's r) and a measure of statistical significance (e.g., p-value) for the csat comparison. For the Rg comparison, provide the mean absolute error or a similar metric to quantify the agreement.
    - **Concern ID** R1-m3
    - **Severity** Minor
    - **Axis** Discussion of limitations
    - **Affected element** Discussion
    - **Evidence pointer** Discussion section
    - **Issue** The Discussion does not explicitly address the limitations of the approach, such as the computational cost of the simulations, the potential inaccuracies of the coarse-grained model for certain sequence features, or the challenges in designing for more complex properties like specific binding interfaces.
    - **Required correction** Add a paragraph to the Discussion acknowledging the limitations of the method and outlining potential avenues for future improvement, such as the use of more accurate models or the integration of experimental data to guide the design process.
- **Technical failings that need to be addressed before the case is established**
    - R1-M1: The lack of experimental validation on a second, distinct IDP system is a significant gap that prevents the case for a "general algorithm" from being fully established.
    - R1-M2: The unexplained outlier (V5) in the csat predictions needs to be resolved or explicitly acknowledged as a limitation to ensure confidence in the model's predictive power.
- **Assessment against Nature-style criteria**
    - **Originality**: High. The combination of MCMC sampling with alchemical free-energy calculations for IDP design is a novel and creative approach that goes beyond simple sequence permutation or rule-based design.
    - **Scientific importance**: High. The ability to design IDPs with specific structural and phase separation properties has broad implications for understanding IDP biology and for engineering new biomolecules. The work directly addresses a major challenge in protein design.
    - **Interdisciplinary readership**: High. The work bridges computational biophysics, protein engineering, and cell biology (via phase separation). The findings will be of interest to researchers in all these areas.
    - **Technical soundness**: Medium. The computational approach is sound, and the experimental validation is a major strength. However, the limited scope of validation (one protein) and the unresolved outlier (V5) are significant technical concerns that need to be addressed.
    - **Readability for nonspecialists**: Good. The manuscript is well-written and logically structured. The concepts are explained clearly, and the figures (as described) appear to be informative. The abstract is accessible.
- **Recommendation posture** Supportive if technical concerns are resolved. The manuscript presents a novel and promising method with strong initial validation. However, the claims of generality and predictive accuracy are not yet fully established from the provided evidence. The authors should address the concerns regarding the scope of validation and the unexplained outlier to make the case for the method's broad utility.

## Risk / unsupported claims
- The claim that the algorithm is "general" is not fully supported by the evidence, as experimental validation is limited to a single protein (A1-LCD).
- The claim that the work "will facilitate the design of proteins whose functions exploit the many properties afforded by protein disorder" is speculative, as no functional properties of the designed variants were tested.
- The statement that the SVR model "can be used to drive the design of disordered proteins" is only a proof of principle, and its accuracy for a wide range of targets is not established.
- The claim that the method can design for "other target properties than chain dimensions" is not demonstrated, as only Rg and csat were used as targets.