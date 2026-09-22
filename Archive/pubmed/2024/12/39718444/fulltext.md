# Searching and Using MobiDB Resource 6 to Explore Predictions and Annotations for Intrinsically Disordered Proteins


## Abstract
  Intrinsically disordered proteins (IDPs) make up around 30% of eukaryotic proteomes and play a crucial role in cellular processes and in pathological conditions such as neurodegenerative disorders and cancers. However, IDPs exhibit dynamic conformational ensembles and are often involved in the formation of biomolecular condensates. Understanding the function of IDPs is critical to research in many areas of science. MobiDB is a unique resource that serves as a comprehensive knowledgebase of IDPs and intrinsically disordered regions (IDRs), combining disorder annotations from experimental evidence and predictions for a broad range of protein sequences. Over the past decade, MobiDB has evolved with a focus on expanding annotation coverage, standardizing annotation provenance, and enhancing database accessibility. The latest MobiDB, version 6, released in July 2024, includes significant improvements, such as the integration of AlphaFoldDB predictions and a new homology transfer pipeline that has substantially increased the number of entries with high‐quality annotations. The user interface has also been updated, highlighting annotation features, clarifying the entry page, and providing an immediate overview of disorder, binding, and disorder functions information in the protein sequence. This protocol guides the user through applications of the MobiDB, including disorder prediction, curated data analysis, and exploration of interaction data. This guide covers how to perform a search in MobiDB annotations using the web interface and the MobiDB REST API for programmatic access. The protocols use a step‐by‐step walkthrough using the human growth hormone receptor to demonstrate MobiDB's functions for visualization and interpretation of protein disorder data. © 2024 The Author(s). Current Protocols published by Wiley Periodicals LLC.

  Basic Protocol 1: Searching MobiDB query formats

  Basic Protocol 2: Searching MobiDB selected datasets and selected proteomes

  Basic Protocol 3: Performing a search on the Statistics page in MobiDB

  Support Protocol: Programmatic access with MobiDB REST API

  Basic Protocol 4: Visualizing and interpreting a MobiDB Entry: The GHR use case


## INTRODUCTION
  The term “intrinsically disordered proteins” (IDPs) refers to biologically active proteins that lack a stable three‐dimensional structure under physiological conditions and do not adopt a fixed 3D conformation. IDPs, and intrinsically disordered regions (IDRs) within proteins generally, are enriched in uncharged and polar amino acids, allowing them to exhibit dynamic behavior (van der Lee et al., 2014). Eukaryotic proteomes contain approximately 30% intrinsically disordered proteins or regions. Many IDPs are involved in protein‐protein and protein‐DNA/RNA interactions, and they play key roles in biological mechanisms such as liquid‐liquid phase separation (Martin et al., 2020) and in various pathological conditions, such as neurodegenerative disorders (Venati & Uversky, 2024) and cancers.

  MobiDB is a comprehensive resource for IDPs and IDRs, which has evolved significantly since its development more than a decade ago, providing an integrated database that combines manually curated, experimentally derived, and predicted data on IDPs. MobiDB utilizes disorder predictions propagated through the MobiDB‐lite software, which is a distinct component of the MobiDB resource (Necci et al., 2017; Necci, Piovesan, Clementel, et al., 2021). The latest update of MobiDB (version 6, released in July 2024; Piovesan et al., 2024)) represents a substantial enhancement in both its functionality and user interface, further establishing its utility as an essential resource for researchers in the field of IDPs.

  A notable enhancement in MobiDB since the version published in 2022 (Piovesan, Del Conte, et al., 2022) is the integration of AlphaFoldDB predictions (Jumper et al., 2021), which have shown high correlation with experimental disorder data and state‐of‐the‐art disorder predictors according to the Critical Assessment of Intrinsic protein Disorder (CAID) assessment (Del Conte et al., 2023), extension of processed data, and propagation of methodological and functional ontologies terms such as the Evidence and Conclusion Ontology (ECO), Gene Ontology (GO) (Gene Ontology Consortium, 2023), and Intrinsically Disordered Proteins Ontology (IDPO). This integration not only enriches the database with accurate predictions but also allows the visualization of positional annotations in protein structures, even in the absence of experimental coordinates from the Protein Data Bank (PDB; Armstrong et al., 2020).

  The process of homology transfer in MobiDB involves transferring annotations of particular proteins that have been manually curated to a wider array of proteins based on their homology. As a result, both the specificity and the extent of the annotations in the database have been increased substantially.

  The entry page has also undergone substantial improvements. It has been redesigned to provide a more intuitive and informative user experience.

  These significant updates to MobiDB motivate the publication of these protocol, which are designed to guide users through the enhanced features for analyzing and characterizing IDPs. This article provides a guide for efficiently accessing and utilizing the vast data repository within the MobiDB resource. The first two Basic Protocols provide an overview of the MobiDB webpage and illustrate the various search options available on the MobiDB website. In particular, Basic Protocol 1 describes how to perform a search on the MobiDB homepage using different entry formats, whereas Basic Protocol 2 refers to a more specific and advanced search, such as for selected datasets and selected proteomes. Basic Protocol 3 focuses on how to perform searches using the Statistics page of MobiDB. Finally, Basic Protocol 4 describes how to visualize and interpret annotations of a MobiDB entry, providing insights into the structural and functional characteristics of IDPs using the human growth hormone receptor (GHR) protein as a case study. Additionally, a Support Protocol describes the process of accessing MobiDB programmatically through its REST API.


## SEARCHING MobiDB QUERY FORMATS
  The MobiDB homepage offers various search options to find the protein of interest (Fig. 1). Users can enter different types of queries in the “Search box” to retrieve relevant output pages. For proteins, users can search using the UniProt accession, protein name, or gene symbol. For organisms, searches can be performed using the organism name or NCBI taxonomy ID. The following steps guide users through exploring the MobiDB using these different query formats.


### Necessary Resources

#### Hardware
  Laptop or desktop computer (best; a smartphone or tablet is an acceptable alternative)Active and stable internet connection


#### Software
  Internet browser: e.g., Firefox (http://www.mozilla.org/firefox), Google Chrome (http://www.google.com/chrome), or Safari (http://www.apple.com/safari)


#### Input data
  None required


### Performing a text search in MobiDB

## SEARCHING MobiDB SELECTED DATASETS AND SELECTED PROTEOMES
  The latest version of MobiDB presents “Selected datasets” and “Selected proteomes” on the MobiDB homepage (Figs. 4 and 5).

  The “Selected datasets” are organized and displayed based on different confidence annotation levels (Gold and Silver stars) characterized by the type of “Evidence,” which indicates the quality of the annotation (Table 1). Each dataset also includes information on “Features” (such as disorder and other supporting information), consensus sources, the number of proteins associated with the specific dataset, and the percentage of annotated residues (Fig. 4A).

  As highlighted in Figure 4A, the two datasets are: Gold, representing all manually curated annotations and their homologs (Fig. 4B).Silver, representing all derived annotations (PDB) and AlphaFold disorder (Fig. 4C).

  The “Selected proteomes” are categorized into the three domains of living organisms: eukaryotes, bacteria, and viruses. For each domain and species (e.g., human), information about protein disorder is visible (Fig. 5).

  The following steps describe how to explore and search proteins among the different “Selected datasets” or “Selected proteomes” within MobiDB.


### Necessary Resources

#### Hardware
  Laptop or desktop computer (best; a smartphone or tablet is an acceptable alternative)Active and stable internet connection


#### Software
  Internet browser: e.g., Firefox (http://www.mozilla.org/firefox), Google Chrome (http://www.google.com/chrome), or Safari (http://www.apple.com/safari)


#### Input data
  None required


### Performing a search on the MobiDB selected datasets

### Performing a search on the MobiDB selected proteomes

## PERFORMING A SEARCH ON THE STATISTICS PAGE IN MobiDB
  The Statistics page provides all data about each type of “Evidence,” “Feature,” and “Source” for the proteins available in MobiDB. Moreover, it allows users to search for statistics of specific organisms and proteomes.


### Necessary Resources

#### Hardware
  Laptop or desktop computer (best; a smartphone or tablet is an acceptable alternative)Active and stable internet connection


#### Software
  Internet browser: e.g., Firefox (http://www.mozilla.org/firefox), Google Chrome (http://www.google.com/chrome), or Safari (http://www.apple.com/safari)


#### Input data
  None required


## PROGRAMMATIC ACCESS WITH MobiDB REST API
  MobiDB can be accessed programmatically through its APIs; refer to the API endpoints description page at https://mobidb.org/help#swagger. The download_page endpoint makes it possible to perform a search on the whole database according to multiple fields. Among them, a list of UniProt accession numbers can be specified, in order to retrieve specific entries. Similarly, the “count” endpoint allows you to determine the number in the database which matches a specific search query. Finally, “statistics” for the current release of the MobiDB can be retrieved to the endpoint named accordingly. Detailed descriptions of the endpoints, including their parameters, input, and output specifications, are provided below. https://mobidb.org/help#swagger


### Necessary Resources

#### Hardware
  Laptop or desktop computer (best; a smartphone or tablet is an acceptable alternative)Active and stable internet connection


#### Software
  Internet browser: e.g., Firefox (http://www.mozilla.org/firefox), Google Chrome (http://www.google.com/chrome), or Safari (http://www.apple.com/safari)


#### Input data
  None required


## VISUALIZING AND INTERPRETING A MobiDB ENTRY: THE GHR USE CASE
  The MobiDB protein entry page, featuring examples such as the Homo sapiens growth hormone receptor (GHR), accessible at https://mobidb.org/P10912, offers comprehensive information, including the protein description, sequence, and all disorder‐related predictions and annotations.

  Using GHR as example, we illustrate the organizational structure common to all entries in MobiDB. At the top of the entry page, users can access general protein information with Features Content, Feature viewer, and AlphaFold structure visualization. Two other sections, Subcellular Locations and Cross References, are available at the bottom of the page (Fig. 8).

  In the middle of the page, users will find the AlphaFold structure, the corresponding protein sequence, and a visualization of the annotations. The annotations dynamically adjust according to the selected tabs. Users can choose an “Overview” of the annotations or explore more detailed information related to “Disorder,” “Binding,” “Interactions,” and “Functions.”


### Necessary Resources

#### Hardware
  Laptop or desktop computer (best; a smartphone or tablet is an acceptable alternative)Active and stable internet connection


#### Software
  Internet browser: e.g., Firefox (http://www.mozilla.org/firefox), Google Chrome (http://www.google.com/chrome), or Safari (http://www.apple.com/safari)


#### Input data
  None required


## COMMENTARY

### Background Information
  MobiDB is a core resource of the IDP Central Consortium and a service of ELIXIR IDP Community (Davey et al., 2019). It was designed to provide structural and functional information about IDPs and IDRs combining annotations from the literature, experimental data, and predictions from multiple resources. MobiDB celebrated ten years of existence as of our previous publication (Piovesan et al., 2022), and for this latest version (v. 6), the updates were designed to enable users to process more data, make the tool faster, and include additional functional features. The recent updates focus on enhancing the database's ability to predict protein ensemble properties, such as conformational diversity and compactness, which are essential for understanding the structural behavior of disordered regions. Moreover, functional annotations (GO and IDPO) from databases like DisProt are propagated using sequence similarity and protein embeddings, which expand MobiDB's coverage of functional predictions.

  In MobiDB, all disorder predictions are generated with MobiDB‐lite, a distinct open source component of MobiDB. It was developed in collaboration with the InterPro (Paysan‐Lafosse et al., 2023) team and is available at https://github.com/BioComputingUP/MobiDB‐lite. It integrates most of the other prediction methods and is used as consensus. Integration pipelines in MobiDB also include FLIPPER (Monzon et al., 2021) and the Residue Interaction Network Generator (RING; Del Conte et al., 2024) software for predicting and characterizing LIP in the PDB and noncovalent interactions at the atomic level in protein structures, respectively. The newly designed entry pages and improved visualization tools allow users to explore the disorder annotations more intuitively, making it easier to access specific disorder‐related features. To provide a comprehensive description of the MobiDB resource, we created training material in collaboration with other consortia such as ELIXIR and PhaseAge. MobiDB remains a critical resource for researchers investigating the roles of disordered proteins in cellular processes and diseases, contributing to a better understanding of the dynamic nature of IDRs in various biological contexts. The MobiDB homepage allows users to search for proteins using a variety of query formats. Whether the search term is a protein or an organism, users can enter data such as the UniProt accession number, protein name, gene symbol, organism name, or NCBI taxonomy ID into the Search box to generate relevant results. Moreover, the MobiDB home page provides direct access to “Selected datasets” and “Selected proteomes.”

  Additional information about MobiDB content is available from the Statistics page (https://mobidb.org/statistics), including the various types of evidence, features, and sources related to the proteins it catalogs. Additionally, the Help page (https://mobidb.org/help) provides a comprehensive guide to MobiDB's key features and functionalities, its structured vocabulary, and how to access its services programmatically. It also includes tutorials on navigating the MobiDB website and utilizing its API for further learning.


### Critical Parameters

#### General considerations
  The main factors influencing the effectiveness of the MobiDB resource include the accuracy of computational prediction models, the completeness and reliability of experimental data, and the integration methods used to consolidate diverse data types.


#### Advanced parameters
  MobiDB offers the possibility of customizing search queries and results views based on specific needs or interests, including filtering data by prediction method, disorder type, or specific protein regions. This allows more targeted analyses and can be helpful when performing research that require specific subsets of the database.


### Troubleshooting
  For a list of potential problems, their causes, and their solutions, please refer to Table 3.


### Guidelines for Understanding Results
  Over its 10‐year history, MobiDB (https://mobidb.org/) has evolved into a comprehensive knowledgebase offering a rich repository of aggregated disorder annotations derived from the literature and experimental evidence, alongside predictions for all available protein sequences. Users of MobiDB can access a wide assortment of selected datasets and selected proteomes directly from the home page of the resource. Selected datasets comprise four types of evidence—curated (C), derived (D), homology (D), and predicted (P)—and a variety of features, including disorder, mobile and missing residues, linear interacting peptides (LIP), and disorder‐to‐disorder (DD) and disorder‐to‐order (DO) binding modes, from different sources. The selected proteome set provides curated (C), derived (D), and predicted (P) annotations for the most prominent organisms among the eukaryotes, bacteria, and viruses. Additional organisms, as well as their annotations, can be found by searching the Statistics page of MobiDB (https://mobidb.bio.unipd.it/statistics). MobiDB now integrates AlphaFoldDB predictions, filling disorder‐annotation gaps for those sequences for which experimental coordinates are lacking, and transfers manually curated annotations through its newly implemented homology transfer pipeline. An updated entry page design provides an enhanced overview of the structural disorder annotations and functions associated with its binding modes. Users interested in a in‐depth exploration of MobiDB and its annotations can find all the essential information about programmatic access, controlled vocabulary, and annotation identifiers, along with user tutorials, on the dedicated Help page (https://mobidb.bio.unipd.it/help). Finally, details on citation, governance, funding, licensing, and policies are available on the About page of MobiDB (https://mobidb.bio.unipd.it/about).


### Author Contributions
  Maria Cristina Aspromonte: Conceptualization; formal analysis; investigation; supervision; writing—original draft. Federica Quaglia: Conceptualization; formal analysis; writing—original draft. Alexander Monzon: Software; conceptualization; formal analysis; Damiano Clementel: Software; writing—original draft. Alessio Del Conte: Software; writing—original draft. Damiano Piovesan: Conceptualization; funding acquisition; project administration; writing—original draft. Silvio Tosatto: Conceptualization; funding acquisition; investigation; project administration; writing—original draft.


### Conflict of Interest
  The authors declare no conflict of interest.


## Data Availability Statement
  The data that support the protocol are openly available in MobiDB at https://mobidb.org/.


## Acknowledgments
  The MobiDB is part of the ELIXIR infrastructure (https://elixir‐europe.org/) and a service of the IDP Community (https://elixir‐europe.org/communities/intrinsically‐disordered‐proteins). This publication is part of a project that has received funding from and funded by the European Union. Horizon Europe MSCA Staff Exchange project IDPfun2, grant agreement no. 101182949 (IDPfun2). Disclaimer: Views and opinions expressed are, however, those of the author(s) only and do not necessarily reflect those of the European Union or the European Research Executive Agency (REA). Neither the European Union nor the granting authority can be held responsible for them. This publication is partially based upon work from COST Action ML4NGP (CA21160), supported by COST (European Cooperation in Science and Technology). Moreover, it received funding from the European Union through the NextGenerationEU PNRR project “ELIXIRxNextGenIT” (IR0000010), PNRR‐PRIN 2022 project “PLANS” (2022W93FTW) and the PNRR project CN‐G.T.RNA SP. 7 project–National Center for Gene Therapy and Drugs based on RNA Technology (CN3)–CN00000041.

  Open access publishing facilitated by Universita degli Studi di Padova, as part of the Wiley ‐ CRUI‐CARE agreement.