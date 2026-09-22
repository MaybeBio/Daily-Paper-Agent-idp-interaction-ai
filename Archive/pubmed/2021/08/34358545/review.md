## Review setup
- **Input scope** Abstract only
- **Assessment boundary** The review is assessed on the basis of the abstract alone. No full text, figures, tables, or supplementary materials were provided.
- **Shared manuscript claim summary** The abstract claims that AlphaFold cannot predict folding pathways, cannot treat intrinsically disordered proteins (IDPs) or disordered regions, and cannot address protein aggregation. It further claims that molecular dynamics simulations have successfully explored energy landscapes of IDP conformational switching and aggregation, and that these landscapes are multifunneled with multiple competing minima, in contrast to the single-funnel landscapes of simple protein folding. The review is said to discuss these characteristics in detail with illustrative simulations.
- **Visible evidence base** Abstract text only. No figures, tables, references, or methodological details are available.
- **Missing materials affecting confidence** Full text, all figures and tables, reference list, simulation details, and any specific case studies or examples. The absence of these materials prevents verification of the claims made about specific simulations and the depth of the review.

## Reviewer
- **Overall assessment** The abstract presents a clear and timely topic, namely the limitations of AlphaFold for IDPs and aggregation, and the value of molecular dynamics simulations in mapping multifunneled energy landscapes. The writing is accessible and the conceptual framing is sound. However, the abstract is brief and does not provide sufficient detail to evaluate the substantive content of the review. The claims about AlphaFold's limitations are broadly accurate but are stated without nuance, and the assertion that molecular dynamics simulations have "successfully explored" these landscapes is presented without supporting examples or critical assessment. The abstract reads more as an introduction than as a summary of a review's findings, and the absence of any mention of challenges, limitations, or future directions weakens its completeness.
- **Who would be interested in the results, and why** Researchers in computational biophysics, protein folding, and intrinsically disordered proteins would find this review relevant. Those interested in the capabilities and limits of machine learning methods for structural biology, particularly AlphaFold, would also be engaged. The review could serve as a useful entry point for newcomers to the field who seek a conceptual overview of energy landscape theory applied to IDPs and aggregation.
- **Major strengths** The topic is timely and of broad interest. The contrast between single-funnel and multifunneled energy landscapes is a useful conceptual framework. The abstract is clearly written and accessible to nonspecialists. The focus on IDPs and aggregation addresses an important gap in current structure prediction methods.
- **Major Concerns**  
  - R1-M1  
  - R1-M2  
  - R1-M3
- **Minor Comments**  
  - R1-m1  
  - R1-m2  
  - R1-m3
- **Technical failings that need to be addressed before the case is established** The abstract does not provide any specific examples of simulations or results, so the claim that molecular dynamics simulations have "successfully explored" these landscapes is not substantiated. The statement about AlphaFold treating "only about half of the human proteome" is presented without a source or qualification. The abstract also does not mention any limitations of the molecular dynamics approach, which is a notable omission for a review.
- **Assessment against Nature-style criteria**  
  - Originality: The topic is not new, but the framing around multifunneled energy landscapes for IDPs and aggregation is a useful synthesis. The abstract does not demonstrate a novel perspective beyond existing reviews.  
  - Scientific importance: The topic is important, given the growing recognition of IDPs and the limitations of AlphaFold. However, the abstract does not convey a specific advance in understanding.  
  - Interdisciplinary readership: The abstract is accessible to a broad audience, including biochemists, computational biologists, and structural biologists. The relevance to machine learning practitioners is also clear.  
  - Technical soundness: The claims are plausible but not verifiable from the abstract alone. The lack of specific evidence or examples weakens the technical foundation.  
  - Readability for nonspecialists: The abstract is well written and understandable. The concepts are introduced clearly, though the term "meta-folding" is used without definition.
- **Recommendation posture** Supportive if technical concerns are resolved. The topic is appropriate and the framing is promising, but the abstract must be supported by a full text that provides specific examples, critical discussion, and a balanced treatment of limitations.

### Major Concerns

- **Concern ID** R1-M1  
- **Severity** Major  
- **Blocking** Yes  
- **Axis** Evidence sufficiency  
- **Claim pointer** The abstract claims that molecular dynamics simulations "already successfully explored the energy landscapes of IDP conformational switching and protein aggregation in multiple cases."  
- **Evidence pointer** Abstract only, location not provided  
- **Concern** The abstract asserts that molecular dynamics simulations have been successful in exploring these energy landscapes, but no specific simulations, systems, or results are cited or described. The claim is presented as a fact without supporting examples or references.  
- **Why it matters** For a review, the credibility of the entire manuscript rests on the quality and representativeness of the simulations discussed. Without any indication of which studies are covered, the reader cannot assess whether the review is comprehensive, balanced, or selective.  
- **Resolution test** The full text must include specific examples of simulations, with details on the systems studied, the methods used, and the key findings. The abstract should be revised to mention at least one or two representative cases, or the claim should be softened to indicate that the review will discuss selected examples.

- **Concern ID** R1-M2  
- **Severity** Major  
- **Blocking** Yes  
- **Axis** Claim accuracy  
- **Claim pointer** The abstract states that AlphaFold "only treats about half of the human proteome, as the remaining proteins are intrinsically disordered or contain disordered regions."  
- **Evidence pointer** Abstract only, location not provided  
- **Concern** This statement is imprecise. AlphaFold's coverage of the human proteome is limited by the availability of evolutionary information and the presence of disordered regions, but the claim that "about half" of the proteome is disordered is an oversimplification. Estimates of the fraction of disordered proteins vary, and the statement conflates fully disordered proteins with those containing disordered regions.  
- **Why it matters** The claim is used to motivate the review's relevance. If it is inaccurate or overstated, the foundation of the argument is weakened. Readers may question the reliability of other statements in the review.  
- **Resolution test** The full text should provide a precise and referenced statement about the fraction of the human proteome that is disordered or contains disordered regions, and should clarify the distinction between these categories. The abstract should be revised to reflect this nuance.

- **Concern ID** R1-M3  
- **Severity** Major  
- **Blocking** No  
- **Axis** Completeness  
- **Claim pointer** The abstract states that the review discusses "the characteristics of these multifunneled energy landscapes in detail, illustrated by molecular dynamics simulations."  
- **Evidence pointer** Abstract only, location not provided  
- **Concern** The abstract does not mention any limitations, challenges, or open questions in the field. A review that only presents successes without critical discussion is incomplete and potentially misleading. The absence of any mention of force field accuracy, sampling limitations, or the difficulty of validating simulations against experiments is a notable gap.  
- **Why it matters** A balanced review is more useful to the community and more credible. The lack of critical perspective suggests that the review may be one-sided, which reduces its value as a reference.  
- **Resolution test** The full text should include a section on limitations and challenges, and the abstract should be revised to indicate that the review also addresses these aspects.

### Minor Comments

- **Concern ID** R1-m1  
- **Severity** Minor  
- **Axis** Clarity  
- **Affected element** Abstract, term "meta-folding"  
- **Evidence pointer** Abstract, location not provided  
- **Issue** The term "meta-folding" is used without definition. It is not a standard term in the field and may confuse readers.  
- **Required correction** Define the term when first used, or replace it with a more standard phrase such as "higher-order assembly" or "aggregation process."

- **Concern ID** R1-m2  
- **Severity** Minor  
- **Axis** Precision  
- **Affected element** Abstract, statement on AlphaFold  
- **Evidence pointer** Abstract, location not provided  
- **Issue** The statement that AlphaFold "is not able to make predictions about the protein folding pathways" is correct but could be more precise. AlphaFold predicts static structures, not dynamics or pathways, and this distinction should be made explicit.  
- **Required correction** Rephrase to state that AlphaFold provides static structure predictions and does not address conformational dynamics or folding pathways.

- **Concern ID** R1-m3  
- **Severity** Minor  
- **Axis** Completeness  
- **Affected element** Abstract, scope of the review  
- **Evidence pointer** Abstract, location not provided  
- **Issue** The abstract does not indicate the scope of the review in terms of the number of studies covered, the types of IDPs discussed, or the range of aggregation processes considered.  
- **Required correction** Add a sentence in the abstract that gives a sense of the breadth of the review, such as the number of systems or the range of methods covered.

## Risk / unsupported claims
- The claim that molecular dynamics simulations have "successfully explored" energy landscapes of IDP conformational switching and aggregation is unsupported in the abstract, as no specific examples are provided.
- The statement that AlphaFold "only treats about half of the human proteome" is presented without a source and is likely an oversimplification.
- The claim that energy landscapes of IDP conformational switching and aggregation "feature a number of minima for different competing low-energy structures" is plausible but not substantiated with examples in the abstract.
- The overall assertion that the review discusses these landscapes "in detail" cannot be evaluated from the abstract alone.