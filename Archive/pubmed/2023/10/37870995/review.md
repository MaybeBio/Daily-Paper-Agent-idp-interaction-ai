## Review setup
- **Input scope** Full manuscript text, including abstract, introduction, methods, results, discussion, and conclusions. No supplementary figures or tables were provided.
- **Assessment boundary** Scientific soundness, methodological rigor, validity of conclusions relative to the presented evidence, and alignment with Nature-style criteria. Editorial or stylistic recommendations are limited to readability.
- **Shared manuscript claim summary** The authors use replica-exchange molecular dynamics (REMD) simulations to explore the conformational space of two RNA Polymerase II C-terminal domain (CTD) models, a 44-residue human CTD fragment and a 14-residue two-heptad-repeat construct, in nonphosphorylated and various phosphorylated states. They report that phosphorylation induces extension in the longer CTD, while effects in the shorter CTD are position-dependent, with some phosphorylated variants contracting due to Na+ ion coordination by phosphate groups. A qualitative model is proposed linking CTD length, phosphorylation spacing, counterion condensation, and entropic costs to conformational outcomes.
- **Visible evidence base** Main text figures (Figures 1–7) and tables (Table 1) are referenced. Supplementary figures and tables (Figures S1–S22, Tables S1–S5) are mentioned but not provided.
- **Missing materials affecting confidence** All supplementary information, including convergence analyses (Figures S4, S5), force field comparisons (Figures S2, S3), secondary structure per-residue data (Figure S10), time evolution of secondary structure (Figure S11), distance maps (Figures S19, S22), Na+ density maps (Figure S20), rotational entropy data (Figure S21), system composition (Table S1), replica exchange parameters (Table S2), statistical tests (Table S3), hydrogen bond data (Table S4), and phosphorylation density data (Table S5). Without these, several quantitative claims cannot be independently verified.

## Reviewer
- **Overall assessment** This manuscript presents a systematic computational study of phosphorylation effects on CTD conformation using REMD, a well-suited enhanced sampling method for IDPs. The work addresses a relevant question in transcription regulation and phase separation biology. The main findings, that phosphorylation generally extends a 44-residue CTD but can contract a 14-residue model via Na+ bridging, are plausible and partially supported by the presented data. However, the evidence base is incomplete, with critical validation and convergence data relegated to inaccessible supplementary materials. The proposed model, while heuristic, is not quantitatively tested. The manuscript is technically sound in its simulation setup but falls short of the broad significance and methodological novelty expected for a Nature-caliber publication.
- **Who would be interested in the results, and why** Researchers studying intrinsically disordered proteins, particularly those investigating post-translational modification effects on IDP conformation. The work is also relevant to the transcription field, given the central role of Pol II CTD phosphorylation in transcription cycle regulation, and to the phase separation community, as CTD phosphorylation is implicated in condensate formation. Computational biophysicists using enhanced sampling methods may find the methodological comparisons useful.
- **Major strengths**  
  1. Use of REMD, an appropriate and rigorous method for sampling IDP conformational ensembles.  
  2. Systematic exploration of multiple phosphorylation patterns, including single, double, and higher-order states, for both CTD lengths.  
  3. Validation of force field choice against experimental NMR chemical shifts, with explicit comparison of two CHARMM variants.  
  4. Clear presentation of free energy landscapes and structural metrics (Rg, H-bonds, distance maps) that support the qualitative conclusions.  
  5. The proposed model, while simple, provides a testable framework linking sequence, modification state, and conformational response.
- **Major Concerns**  
  - **Concern ID** R1-M1  
  - **Severity** Major  
  - **Blocking** Yes  
  - **Axis** Evidence sufficiency  
  - **Claim pointer** The authors claim that "phosphorylation restricted the conformational space of CTD models" for the 44-residue systems, based on PCA free energy landscapes.  
  - **Evidence pointer** Figure 2, Section "Phosphorylation Caused Extended Conformations in CTD Sequences with 44 Residues"  
  - **Concern** The PCA plots in Figure 2 are presented as evidence of reduced conformational breadth with increasing phosphorylation. However, PCA projections can be misleading for IDPs, and the claim of "restricted" space is not quantified. No quantitative metrics (e.g., PCA eigenvalue spectra, conformational entropy estimates, or cluster analysis) are provided in the main text. The supplementary figures that might support this (e.g., convergence and sampling metrics) are not available for review.  
  - **Why it matters** The central conclusion that phosphorylation restricts conformational space underpins the proposed model. Without quantitative support, the claim remains qualitative and potentially overinterpreted from PCA visualizations.  
  - **Resolution test** Provide quantitative measures of conformational space breadth (e.g., effective number of states, entropy estimates, or PCA variance explained) for each system, and show that differences are statistically significant.  
  - **Concern ID** R1-M2  
  - **Severity** Major  
  - **Blocking** Yes  
  - **Axis** Evidence sufficiency  
  - **Claim pointer** The authors state that "Na+ ion coordination by the negatively charged phosphorylated Ser residues and bending of the structure as a result of this coordination" explains contraction in specific 2CTD variants.  
  - **Evidence pointer** Figure 6, Section "Phosphorylation had Diverse Effects on the Conformation of CTD Sequences with 14 Residues"  
  - **Concern** Figure 6 shows Na+ density isosurfaces on representative structures, but no quantitative analysis of ion coordination (e.g., radial distribution functions, coordination numbers, or residence times) is presented. The claim that Na+ bridging causes contraction is inferred from visual inspection. Alternative explanations, such as hydrogen bonding between phosphate oxygens and backbone amides, are not systematically ruled out.  
  - **Why it matters** The proposed model hinges on ion coordination as the mechanism for contraction. Without quantitative ion binding data, the mechanism is not established.  
  - **Resolution test** Provide radial distribution functions or coordination number analyses for Na+ around phosphate oxygens for all 2CTD variants, and correlate these with Rg changes.  
  - **Concern ID** R1-M3  
  - **Severity** Major  
  - **Blocking** Yes  
  - **Axis** Reproducibility  
  - **Claim pointer** The authors claim convergence of REMD simulations based on "small standard errors" and one extended simulation for a single system.  
  - **Evidence pointer** Section "Replica-Exchange Molecular Dynamics Simulations", Figures S4, S5 (not provided)  
  - **Concern** Convergence is a critical issue for REMD simulations of IDPs. The main text states that convergence was confirmed for one system (2CTD-nonphos) by extending to 400 ns, but no convergence analysis is shown for any phosphorylated system or for the 44-residue systems. The claim of convergence for all systems is therefore unsupported.  
  - **Why it matters** If simulations are not converged, the reported conformational ensembles and derived conclusions may be artifacts of insufficient sampling.  
  - **Resolution test** Provide convergence metrics (e.g., block averaging of Rg, PCA overlap between independent runs, or replica exchange statistics) for all systems, not just one representative case.  
  - **Concern ID** R1-M4  
  - **Severity** Major  
  - **Blocking** No  
  - **Axis** Conceptual novelty  
  - **Claim pointer** The proposed model (Figure 7) suggests that CTD length and phosphorylation spacing determine whether extension or contraction occurs.  
  - **Evidence pointer** Figure 7, Section "Length of CTD and Relative Positions of Phosphorylation Sites Affect the Conformations"  
  - **Concern** The model is presented as a general framework, but it is derived from only two sequence lengths and a limited set of phosphorylation patterns. The model is not tested against any independent data, such as published experimental or computational results on CTD or other IDP systems. The distinction between "entropic cost" and "electrostatic repulsion" is invoked qualitatively without quantitative estimates.  
  - **Why it matters** A model that is not quantitatively tested or generalized beyond the specific systems studied has limited predictive value.  
  - **Resolution test** Apply the model to predict conformations of additional CTD lengths or phosphorylation patterns not used in model development, and validate against simulations or experiments.  
- **Minor Comments**  
  - **Concern ID** R1-m1  
  - **Severity** Minor  
  - **Axis** Clarity  
  - **Affected element** Abstract  
  - **Evidence pointer** Abstract, "location not provided"  
  - **Issue** The abstract states that phosphorylation has "complex effects" but does not summarize the key finding that effects are length-dependent and position-dependent.  
  - **Required correction** Add a sentence specifying that extension occurs in the longer CTD while contraction is observed in some shorter variants due to ion coordination.  
  - **Concern ID** R1-m2  
  - **Severity** Minor  
  - **Axis** Statistical rigor  
  - **Affected element** Rg distribution comparisons  
  - **Evidence pointer** Figure 3a, Table S3 (not provided)  
  - **Issue** The text mentions p-values from t-tests but does not report effect sizes or confidence intervals. For IDP ensembles, distributions often overlap substantially, and statistical significance may not imply biological relevance.  
  - **Required correction** Report effect sizes (e.g., Cohen's d) and consider using distribution overlap metrics (e.g., Bhattacharyya coefficient) in addition to p-values.  
  - **Concern ID** R1-m3  
  - **Severity** Minor  
  - **Axis** Methodological detail  
  - **Affected element** Force field selection  
  - **Evidence pointer** Section "System Preparation and Equilibration"  
  - **Issue** The choice of C36mw over C36m is justified by "better agreement with structural properties of IDPs" from earlier studies, but the specific improvement for this system is not quantified beyond Figure S3.  
  - **Required correction** Provide a quantitative comparison (e.g., Rg distributions or chemical shift agreement metrics) for the two force fields for the CTD system studied.  
  - **Concern ID** R1-m4  
  - **Severity** Minor  
  - **Axis** Biological relevance  
  - **Affected element** Discussion  
  - **Evidence pointer** Section "Discussion"  
  - **Issue** The discussion of biological implications, particularly regarding phase separation, is speculative and not connected to specific experimental observations on CTD phase behavior.  
  - **Required correction** Either cite specific experimental studies on CTD phase separation and relate the findings to them, or clearly label the discussion as speculative.  
- **Technical failings that need to be addressed before the case is established**  
  1. Lack of quantitative convergence analysis for all systems (R1-M3).  
  2. Absence of quantitative ion coordination analysis to support the Na+ bridging mechanism (R1-M2).  
  3. No quantitative measure of conformational space restriction for the 44-residue systems (R1-M1).  
  4. The proposed model is not tested against independent data (R1-M4).  
- **Assessment against Nature-style criteria**  
  - **Originality** Moderate. The application of REMD to CTD phosphorylation is not entirely new, and similar studies exist for other IDPs. The systematic comparison of multiple phosphorylation patterns is a useful contribution, but the conceptual framework is not groundbreaking.  
  - **Scientific importance** Moderate. The findings are relevant to understanding CTD function and phase separation, but the study does not resolve a major open question or provide a transformative insight. The proposed model is heuristic and not quantitatively validated.  
  - **Interdisciplinary readership** Limited. The work is primarily of interest to computational biophysicists and IDP researchers. The biological implications are discussed but not developed sufficiently to attract a broad biology audience.  
  - **Technical soundness** The simulation methodology is appropriate, and the use of REMD is justified. However, the lack of accessible convergence and validation data undermines confidence in the results.  
  - **Readability for nonspecialists** The manuscript is generally well-written and accessible, with clear figures. However, the qualitative nature of some claims and the reliance on supplementary materials for key evidence may confuse nonspecialist readers.  
- **Recommendation posture** Currently not established from the provided evidence. The manuscript addresses a relevant question with an appropriate method, but the evidence base is incomplete, and key claims are not quantitatively supported. If the authors provide the missing convergence analyses, quantitative ion coordination data, and a more rigorous test of the proposed model, the work could become a solid contribution to a specialized journal. However, the scope and significance are not aligned with Nature's broad readership and high-impact criteria.

## Risk / unsupported claims
- The claim that phosphorylation "restricted the conformational space" of the 44-residue CTD is not quantitatively supported in the main text.
- The mechanism of Na+ ion coordination causing contraction in specific 2CTD variants is inferred from visual inspection of density maps, not from quantitative analysis.
- The proposed model (Figure 7) is presented as general but is derived from a limited set of systems and is not tested against independent data.
- The assertion that "entropic cost for bending" prevents contraction in longer CTDs is not quantified or directly measured.
- The statement that "counterion condensation" reduces electrostatic repulsion in 2CTD systems is not supported by quantitative ion binding data.
- The biological relevance of the findings to phase separation is discussed speculatively without direct experimental connection.