# Cloning, expression, purification, and structural modeling of the Chandipura virus matrix protein


## Abstract
  The Chandipura virus matrix protein plays a crucial role in virus assembly, budding, and the cytopathic effects observed in infected cells by interacting with several host proteins. The protocol presented here outlines the expression and purification of full‐length Chandipura virus matrix protein and two N‐terminally truncated constructs produced in Escherichia coli. This protocol results in high yields of monomeric matrix protein, which is suitable for structural studies. Additionally, GFP‐fused Chandipura virus matrix protein constructs can be expressed in mammalian cells for examination of intracellular localization. The Chandipura virus matrix protein model, generated using AlphaFold, features an intrinsically disordered N terminus and a structured C‐terminal core, similar to other Vesiculovirus matrix proteins.


## Materials

### Cloning and plasmid purification
  Synthetic CHPV M gene purchased from Twist Bioscience (UniProtKB Q9WH76).pET28a(+) (Merck‐Millipore #69864) and pcDNA3.1 (Thermo Fisher #V79020) vectors.Superfolder GFP [13].In‐Fusion Snap Assembly cloning kit and Stellar chemically competent cells (Takara Bio #638945).Thermocycler.Agarose Gel Electrophoresis.Gel and PCR Clean‐up kit (Macherey‐Nagel #740609).42 °C water bath.Sterile 1.5 and 15 mL centrifuge tubes.LB (Luria‐Bertani) liquid medium: 10 g tryptone, 5 g NaCl, 5 g yeast extract in 1 L ddH2O, and pH 7.2–7.5 (autoclave for 15 min at 120 °C).LB agar (Luria–Bertani broth with 1.5% agar–agar) plates supplemented with antibiotics.Antibiotics: ampicillin (BioChemica #A0839) and kanamycin (Gerbu #1091).Glass Erlenmeyer flasks.Laboratory shaker with thermoregulation.Refrigerated centrifuge and centrifuge tubes.NucleoSpin Plasmid kit (Macherey‐Nagel #740588).NucleoBond Xtra Midi EF kit (Macherey‐Nagel #740420).Spectrophotometer (DeNovix DS‐11).


### Protein expression in E. coli
  Rosetta‐gami™ 2(DE3) (Merck‐Millipore #71351).LB agar plates supplemented with antibiotics.TB (Terrific Broth) liquid medium: 12 g tryptone, 24 g yeast extract, 4 mL glycerol, 2.313 g potassium dihydrogen phosphate, 12.54 g potassium phosphate dibasic in 1 L ddH2O (autoclave for 15 min at 120 °C).Antibiotics: kanamycin and chloramphenicol (SERVA #16785).Glass Erlenmeyer flasks.Laboratory shaker with thermoregulation.Isopropyl β‐d‐1‐thiogalactopyranoside (IPTG) (Gerbu #1043).Refrigerated centrifuge and centrifuge tubes.


### Protein expression in Expi293F
  Laminar flow cabinet.One vial of cryopreserved Expi293F mammalian cells (Thermo Fisher #A14527).FreeStyle™ 293 Expression Medium (Thermo Fisher #12338018).37 °C water bath.Corning® Erlenmeyer cell culture flasks (Merck‐Millipore #CLS431143).Sterile serological pipettes.Sterile and filtered pipette tips.Sterile 1.5, 2, 15, and 50 mL centrifuge tubes.ExpiFectamine 293 transfection kit (Thermo Fisher #A14525).PEI STAR™ transfection reagent (Tocris #7854).CO2 orbital shaker with thermoregulation.Automated cell counter (Countess II, Invitrogen).


### Protein purification
  Continuous flow cell disruptor (Constant Systems).Syringes and PES Membrane Filters (SARSTEDT #83.1826.001) for sterile filtration of buffers.Sterile 1.5, 2, 15, and 50 mL centrifuge tubes.Tobacco etch virus (TEV) protease [14].Buffer A: 50 mm HEPES pH 7.5, 500 mm NaCl, 5% glycerol, Roche cOmplete EDTA‐free protease inhibitor cocktail, 100 μg·mL−1 DNAse I.Buffer B: 50 mm HEPES pH 7.5, 500 mm NaCl, 5% glycerol, 5 mm imidazole.Buffer C: 50 mm HEPES pH 7.5, 500 mm NaCl, 5% glycerol, 500 mm imidazole.Buffer D: 50 mm HEPES pH 7.5, 500 mm NaCl, 5% glycerol.Buffer E: 20 mm HEPES pH 7.5, 200 mm NaCl.n‐dodecyl‐ß‐D‐maltoside (DDM) (Carl Roth #CN26.1).Refrigerated centrifuge and centrifuge tubes.Empty chromatography column.TALON® Metal Affinity Resin (Takara Bio #635502).PD MidiTrap™ G‐25 columns (Merck‐Millipore #28918008).Amicon® Ultra Centrifugal Filter, 10 kDa MWCO (Merck‐Millipore #UFC5010).Superdex® 200 Prep Grade (Merck‐Millipore #GE17‐1043‐01).Spectrophotometer (DeNovix DS‐11).SDS/PAGE apparatus, 15% SDS/PAGE gels, 5× SDS/PAGE sample loading buffer, and Coomassie Brilliant Blue staining solution.PageRuler™ Plus Prestained Protein Ladder (Thermo Scientific™ #26619).Liquid nitrogen.


### Thermal shift assay
  MicroAmp Fast Reaction tubes and caps (Thermo Fisher #4358293 and #4323032).Refrigerated centrifuge.SYPRO® Orange Protein Gel Stain (Merck‐Millipore #S5692).Applied Biosystems real‐time PCR system.


## Methods

### CHPV M 3D‐structure prediction
  AlphaFold [15, 16] within Tamarind Bio (https://www.tamarind.bio/) [17] was used to predict the three‐dimensional structure of full‐length CHPV M from its amino acid sequence, generating five models. The highest‐scoring model was analyzed further (Fig. 1A). Additionally, the Basic Local Alignment Search Tool (BLAST) [18] in UniProt [19] was utilized to identify sequence similarities with other viral M proteins, thereby identifying analogous structures deposited in the PDB [20] (Fig. 1B). Finally, the Clustal Omega program [21] was used to calculate sequence similarities. Sequence alignment was created with T‐Coffee [22, 23] and illustrated with BOXSHADE (Fig. 1C).


### Cloning of CHPV_M, GFP_CHPV_M, GFP_CHPV_32M, and GFP_CHPV_59M for expression in E. coli
  A synthetic gene of CHPV M was bought from Twist Bioscience and cloned into the pET28a(+) vector using In‐Fusion Snap Assembly, per the manufacturer's instructions (Tips & Tricks 2). The first construct, termed CHPV_M, includes the complete CHPV M sequence, a TEV protease cleavage site, and a His8‐purification tag at the C terminus. In the second cloned construct, the start codon is followed by a FLAG purification tag, a His10‐purification tag, the DNA sequence of superfolder GFP, a TEV cleavage site, and the full‐length sequence of CHPV M. This construct was designated GFP_CHPV_M. Additionally, two N‐terminally truncated CHPV M constructs were cloned to reduce intrinsic disorder, starting at serine 32 (GFP_CHPV_32M) or serine 59 (GFP_CHPV_59M) (Fig. 2A,B). All constructs were transformed into Stellar chemically competent cells (Takara Bio, Japan), and the transformants were grown on LB agar plates supplemented with 35 μg·mL−1 kanamycin (Tips & Tricks 3).


### Plasmid amplification and purification for transformation of E. coli strains
  Pick a single colony of Stellar chemically competent cells transformed with plasmids of CHPV_M, GFP_CHPV_M, GFP_CHPV_32M, and GFP_CHPV_59M from LB agar plates.Inoculate 5 mL of LB liquid medium with a single colony and grow overnight at 37 °C and 180 r.p.m. in the presence of 35 μg·mL−1 kanamycin.Perform plasmid purification using the NucleoSpin Plasmid kit.Confirm the correctness of all constructs through Sanger sequencing.


### Expression screening of CHPV M in E. coli
  For protein expression screening, the cloned plasmids were transformed into Rosetta™(DE3), Rosetta™(DE3)pLysS, and Rosetta‐gami™ 2(DE3), and the transformants were grown on LB agar plates supplemented with 35 μg·mL−1 kanamycin and the E. coli strains' specific antibiotics. Initial small‐scale expression screening of CHPV M constructs identified Rosetta‐gami™ 2(DE3) as the most suitable E. coli protein expression strain among those tested.


### Large‐scale expression of CHPV M in E. coli
  Transform GFP_CHPV_M, GFP_CHPV_32M, and GFP_CHPV_59M into Rosetta‐gami™ 2 (DE3) and grow transformants on LB agar plates supplemented with 35 μg·mL−1 kanamycin.Grow cells from a single colony in LB medium supplemented with 34 μg·mL−1 chloramphenicol and 50 μg·mL−1 kanamycin at 37 °C and 180 r.p.m. overnight.Add 5 mL starter culture to 2 L TB medium supplemented with 34 μg·mL−1 chloramphenicol and 50 μg·mL−1 kanamycin at 37 °C and 220 r.p.m. until an OD600 of 0.6 is reached, and then cool to 20 °C.Add 1 mm IPTG to induce protein expression.Express protein for 14 h at 20 °C and 220 r.p.m.Harvest the cells by centrifugation (30 min at 4000  g  and 4 °C).Freeze cell pellets (4 g each) in liquid nitrogen and store at −80 °C until purification.

  Expression rates of a few milligrams of protein per liter of cell culture (Fig. 2B) were observed for the three constructs fused to a GFP gene on the CHPV M N terminus (GFP_CHPV_M, GFP_CHPV_32M, and GFP_CHPV_59M). The cell pellets collected after centrifugation displayed a strong, visibly vibrant green color, suggesting that the GFP fused to the N terminus minimized the predicted cytopathic effects, which consequently also resulted in increased expression levels of soluble protein. In contrast, CHPV M, which was not fused to GFP, appeared to be cytotoxic.


### Purification of GFP_CHPV_M, GFP_CHPV 32M, and GFP_CHPV 59M
  Resuspend one pellet in 50 mL buffer A and lyse using a cooled cell disruptor at 1.5 kbar in two successive rounds (Tips and Tricks 4).Centrifuge the lysate at 45 000  g  for 60 min and 4 °C.Add TALON® metal affinity resin to the supernatant.Allow all the His‐tagged protein to bind to 1 mL TALON resin in a batch format.Transfer the mixture to an empty chromatography column and wash with 3 column volumes of buffer B.Elute with 2 column volumes of buffer C.Perform buffer exchange into buffer D with a G‐25 desalting column, following the manufacturer's instructions.Add TEV protease at a ratio of 1:30 (w/w).Incubate overnight at 4 °C. This results in the CHPV M protein with an additional serine amino acid at the N terminus.Pass the protein solution through a chromatography column containing 1 mL of TALON resin. Collect the flow‐through (Fig. 3A,C,D).Determine the protein concentration in the flow‐through with a spectrophotometer, according to the user guide (https://www.denovix.com/ds‐11‐series‐user‐guide/). MW and ε can be calculated with the ProtParam online tool (https://web.expasy.org/protparam/) [24].

  Note: The purification was conducted with higher concentrations of NaCl (here 500 mm), as this has been shown to reduce membrane association and the self‐association of other vesiculovirus M proteins [25]. Additionally, 0.01% (w/v) DDM should be added to GFP_CHPV_M and GFP_CHPV 32 M after step 7. This is unnecessary for GFP_CHPV 59 M. The detergent can be removed in subsequent steps.


### Thermal shift assay
  Prepare samples of purified CHPV_M, CHPV_32M, and CHPV_59M at concentrations of 10 μm.Pipette 30 μL of each construct into MicroAmp Fast Reaction tubes. Prepare each sample in triplicate.Add SYPRO® Orange Protein Gel Stain to the sample just before initiating the measurement. The final concentration is 2× in each tube. Seal the tubes with the caps.Using a real‐time PCR system, record the relative fluorescence units while ramping up the temperature from 20 °C to 95 °C in 1 °C steps (Fig. 4).


### Analytical size exclusion chromatography
  An aliquot of the purified CHPV_M was concentrated to 50 μL using a 10 kDa molecular weight cut‐off concentrator to conduct analytical size exclusion chromatography. This concentrated sample was centrifuged for 30 min at 18 000  g  at 4 °C to remove aggregates and then loaded onto a self‐packed Superdex 200 column, which was operated in a cold room at a temperature between 4 and 6 °C. The column's dimensions are 1.5 cm in diameter and 7 cm in height, with an approximate bed volume of 12 mL. Size exclusion chromatography was performed with buffer E. The column's performance was initially assessed by applying gel filtration standards purchased from Bio‐Rad before the concentrated purified CHPV_M was loaded. 500 μL fractions were collected by gravity after sample loading (Fig. 3B).

  Analytical size exclusion chromatography of the purified protein, performed at a reduced NaCl concentration of 200 mm, showed that full‐length CHPV M elutes at a volume between the gel filtration standards Ovalbumin (44 kDa) and Myoglobin (17 kDa), corresponding to monomeric CHPV M. Altogether, no self‐association of the full‐length CHPV M protein after GFP cleavage was observed under the conditions outlined here.


### Sodium dodecyl‐sulfate polyacrylamide gel electrophoresis
  Mix samples with 5× SDS Loading buffer containing DTT.Heat for 10 min at 98 °C.Run 15% SDS/PAGE.Stain gel with Coomassie Brilliant Blue solution (Fig. 3).


### Cloning of CHPV_M, GFP_CHPV_M, and CHPV_M_GFP for expression in mammalian cells
  The CHPV M gene was also cloned into the pcDNA3.1 vector for expression in mammalian cell lines. In the first construct, termed again CHPV_M, the start codon is followed by the full‐length DNA sequence of CHPV, a TEV cleavage site, a His10‐purification tag, and a Twin‐Strep‐tag®. In the second construct, the start codon is followed by a FLAG purification tag, a His10‐purification tag, the sequence of superfolder GFP, a TEV cleavage site, and the full‐length sequence of CHPV M, identical to GFP_CHPV_M. In the third construct, designated CHPV_M_GFP, the start codon is followed by the full‐length DNA sequence of CHPV M, a TEV cleavage site, the sequence of superfolder GFP, a His10‐purification tag, and a Twin‐Strep‐tag® (Fig. 5A,B). All constructs were transformed into Stellar chemically competent cells, and the transformants were grown on LB agar plates supplemented with 100 μg·mL−1 ampicillin.


### Plasmid amplification and purification for transient expression in Expi293F
  Pick a single colony of Stellar chemically competent cells transformed with plasmids of CHPV_M, GFP_CHPV_M, and CHPV_M_GFP from LB agar plates.Inoculate 5 mL of LB liquid medium with a single colony and grow overnight at 37 °C and 180 r.p.m. in the presence of 100 μg·mL−1 ampicillin.Perform plasmid purification using the NucleoSpin Plasmid kit.Confirm the correctness of all constructs through Sanger sequencing.Inoculate 100 mL of LB liquid medium with a single colony for endotoxin‐free plasmid purification and grow overnight at 37 °C and 180 r.p.m. in the presence of 100 μg·mL−1 ampicillin.Perform plasmid purification using the NucleoBond Xtra Midi EF kit.


### Small‐scale expression screening of CHPV_M and GFP_CHPV_M in Expi293F
  Small‐scale expression screening of the constructs CHPV_M and GFP_CHPV_M was performed in Expi293F human cells (Tips & Tricks 5–12). To induce protein expression, 10 mL of Expi293F cell culture (2 × 106 cells·mL−1) was transiently transfected with one of the CHPV M plasmids using the ExpiFectamine™ 293 Transfection Kit. Transfected cells were cultured in an orbital shaker at 37 °C or 30 °C and 120 r.p.m. with 8% CO2. Cells were harvested 48, 72 h, or 5 days post‐transfection by centrifugation at 900 g for 20 min at 4 °C and then flash‐frozen in liquid nitrogen before storage at −80 °C.

  The expression attempts for CHPV_M and GFP_CHPV_M in Expi293F cells resulted in very low expression rates under the tested conditions (not shown). As a result, this expression system is not ideal for structural studies of CHPV M.

  However, the expression rates of GFP_CHPV_M and CHPV_M_GFP in Expi293F are adequate for conducting intracellular localization and co‐localization studies with human host proteins using fluorescence microscopy.


### Expression of GFP_CHPV_M and CHPV_M_GFP in mammalian cells
  Transiently transfected 10 mL of Expi293F cell culture (2 × 106 cells·mL−1) with 10 μg pDNA and 30 μL PEI STAR™ at 1 mg·mL−1, following the manufacturer's instructions (Tips & Tricks 6).Grow cells in an orbital shaker for 24 h at 37 °C and 120 r.p.m. with 8% CO2.


### Fluorescence microscopy
  A few cells from a suspension culture were placed on a microscope glass slide and covered with a glass coverslip. Fluorescence was observed using a fluorescence microscope (Keyence, BZ‐X) and a 100× oil immersion objective (Fig. 5C,D).


## Discussion
  AlphaFold was utilized to generate a model of the CHPV M protein. The three‐dimensional structure of the full‐length CHPV M (pLDDT: 76.2), as predicted by AlphaFold, shows that the N‐terminal tail of the M protein is likely mostly structurally disordered (residues 1–62), whereas the C‐terminus adopts a globular structure. The model suggests that CHPV M exhibits an overall three‐dimensional structure similar to that of the VSV M crystal (PDB ID 1LG7 [25]) and cryo‐EM (PDB ID 7UML [26]) structures, despite the low sequence similarity of approximately 30%. Both the disordered N‐termini of VSV M and CHPV M are thought to interact with membranes and facilitate self‐association [11]. Meanwhile, the C‐terminal regions of both proteins adopt a comparable globular fold. However, despite the overall structural similarity, the differences in the sequences are likely to impact the interaction of CHPV M with host proteins. Therefore, this virus deserves to be studied independently.

  This study presents a protocol for producing full‐length monomeric CHPV M protein and two truncated constructs from E. coli, aimed at facilitating structural studies of CHPV M and its complexes with human host proteins.

  Initial screening revealed that no significant amounts of soluble CHPV_M could be extracted from E. coli or Expi293F cells, indicating a possible membrane association, self‐association, and/or cytotoxicity. Conversely, fusion of a GFP to the N‐terminal disordered tail strongly increased the production of soluble protein in E. coli, probably by sterically hindering the CHPV M N terminus from engaging in associations of any kind. The GFP was chosen because it is believed to effectively inhibit membrane association and the self‐association of CHPV M. Its molecular weight of 27 kDa is expected to occupy a volume sufficient to limit steric access to the N terminus. Tags with similar or higher molecular weights are likely to yield comparable results.

  Additionally, as vesiculovirus M proteins can be post‐translationally modified in mammalian cells [27], using a bacterial expression system to pursue structural studies is more likely to produce the homogeneous sample required for crystallography and single‐particle cryo‐EM.

  From the constructs tested, CHPV_59M is expected to aid in crystallization trials of CHPV M, similar to what was observed with VSV M. Moreover, no self‐association of the purified full‐length CHPV M was detected under the conditions outlined here, and therefore, this construct could also be utilized for crystallization attempts. The production of monomeric full‐length CHPV M also paves the way for conducting protein–protein interaction studies with human host proteins and membranes, where the disordered N‐terminal tail is likely to play a significant role.

  Because CHPV M contributes to CHPV‐induced encephalitis by interacting with host proteins in neurons, it is of scientific interest to study the intracellular localization and co‐localization of CHPV M in mammalian cells. For this purpose, a GFP was fused either to the CHPV M C‐terminus or the N terminus. Expression was detected for CHPV_M_GFP and GFP_CHPV_M by fluorescence microscopy, meaning both constructs can be used to study and validate interactions with host proteins in mammalian cell lines.

  In conclusion, it is of scientific interest to study the interactions of CHPV M with human host proteins because CHPV is an emerging human pathogen causing deadly encephalitis in children, and no treatment is available to date. CHPV M is expected to induce changes in host cell morphology by interacting with various proteins, ultimately leading to apoptosis. Structural studies of these complexes will aid in understanding the nature of these interactions and in the development of an antiviral drug.

  Based upon our findings, the next steps will involve structural studies of CHPV M and complexes of CHPV M with human host proteins, as well as intracellular co‐localization studies of these complexes by fluorescence microscopy. This, however, awaits further investigation.


## Tips and Tricks
  Chemicals for which no specific supplier was specified can be purchased from any vendor. All chemicals should be of cell culture grade or high purity.The user guide for the In‐Fusion Snap Assembly cloning kit is available here: https://www.takarabio.com/learning‐centers/cloning/in‐fusion‐cloning‐general‐information/in‐fusion‐cloning‐overview.All tubes and flasks for culturing E. coli cells must be sterile.All centrifuges and buffers used for protein purification should be pre‐cooled to 4 °C, and the purification should be performed at 4 °C.The user guide that comes with the Expi293F cell vial is available here: https://www.thermofisher.com/order/catalog/product/de/en/A14527.The user guides for the PEI STAR™ transfection reagent are available here: https://www.tocris.com/products/pei‐transfection‐reagent_7854.Researchers must follow laboratory rules and safety guidelines when handling Expi293F cells (https://www.thermofisher.com/de/en/home/references/gibco‐cell‐culture‐basics.html).Expi293F cells in suspension cultures should be maintained between 0.2 x106 cells·mL−1 and 2 × 106 cells·mL−1 in FreeStyle™ 293 Expression Medium at 37 °C and 8% CO2 on a shake platform set to 120 r.p.m..All flasks for culturing Expi293F cells must be sterile and endotoxin‐free.The Expi293F cell culture volume should not exceed 20% of the flask's total volume to allow for aeration and gas exchange.Cell viability at the time of transient transfection should be greater than 95%.Transient transfections must be carried out under sterile conditions and require the use of a laminar flow hood.


## Conflict of interest
  The author declares that she has no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper.


## Author contributions
  MG designed and conducted research, analyzed data, and wrote the paper.


## Data accessibility
  Data will be made available upon request.


## Acknowledgements
  This research received no specific grant from funding agencies in the public, commercial, or not‐for‐profit sectors. The author is grateful to Thomas Krey, Guido Hansen, Jeroen Mesters, and their teams for their support, especially Kumar Nagarathinam and Hera Fatima. The author is especially thankful to Britta Schwarzloh for generously providing reagents and to Lou Plath for acquiring the fluorescence images during a Keyence BZ‐X demonstration. Figures were created with ChimeraX [28, 29], Inkscape (David Burghoff, University of Texas), and BioRender.com [30]. Open Access funding enabled and organized by Projekt DEAL.