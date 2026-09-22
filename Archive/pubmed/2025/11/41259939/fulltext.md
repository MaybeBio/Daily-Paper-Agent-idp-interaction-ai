# Development of an EPR-based methodology to study protein-lipid interaction☆


## Abstract
  The interaction of protein with other biomolecules is central to all cellular processes. In particular, protein-lipid interactions play an essential role in regulating soluble and membrane protein function, structure, and dynamics. However, probing these interactions remains challenging due to the complexity and heterogeneity of membranes. Various methods have been developed to characterize protein-membrane interaction, each presenting advantages and limitations. This study presents a robust methodology based on continuous-wave Electron Paramagnetic Resonance (CW-EPR) spectroscopy to characterize protein–membrane interactions. We focused on the protein Tau, an intrinsically disordered protein associated with neurodegenerative diseases. We show that the interaction of labelled Tau with lipids gives rise to a very distinct lineshape, which can be used to quantify the fraction of bound protein. This allows to obtain the apparent binding mode and affinity through titration experiments. In addition, we show that a single measurement provides the absolute concentration of free and bound protein. We argue that this information, which is rarely obtained by other methods providing relative signals, is very useful for mechanistic studies. Furthermore, we developed a minimal-data approach and demonstrated that a single EPR measurement can be used to estimate an apparent binding constant. The approach is applied to the Tau-membrane interaction occurring in different conditions affecting the binding behavior. The presented methodology is expected to be applicable to other proteins.


## Introduction
  Binding affinity is a central aspect of biological function, as most physiological and pathological processes rely on interactions between biomolecules. Gaining insight into these interactions requires not only structural characterization, but also a quantitative understanding of the energetic forces driving complex formation. Over the years, a wide range of biophysical techniques have been developed to measure protein–ligand binding affinities, based on diverse principles such as calorimetry (isothermal titration, ITC), optics (fluorescence; Förster resonance energy transfer, FRET), diffusion (microscale thermophoresis, MST), interferometry (surface plasmon resonance, SPR; biolayer interferometry, BLI), and magnetism (nuclear magnetic resonance, NMR; electron paramagnetic resonance, EPR), among others. Each method offers specific advantages in terms of sensitivity, sample requirements, kinetic resolution, and compatibility with different systems and buffer conditions.

  ITC measures heat changes upon ligand binding, providing direct and label-free access to thermodynamic parameters such as enthalpy, entropy and dissociation constants (KD) [1,2]. ITC is frequently applied in the characterization of protein-small molecule, protein-DNA/RNA, or protein-protein interactions.

  Fluorescence spectroscopy techniques utilize fluorescent labeling to detect changes in emission intensity, polarization, or energy transfer efficiency upon ligand binding, allowing highly sensitive, real-time measurements even at low analyte concentrations [3]. In particular, FRET, which relies on the non-radiative transfer of energy between two fluorophores, can be used to quantify protein interaction [4]. MST enables sensitive, low-volume quantification of interactions in the pM to mM range by tracking the movement of fluorescently labelled molecules along a temperature gradient, which reflects binding-induced changes in size, charge, or solvation [5].

  SPR and BLI are label-free techniques used to quantify binding affinities and kinetics in real time. SPR detects changes in refractive index near a sensor surface where the ligand is immobilized and analytes are flowed over via microfluidics [6]. Plasmon-waveguide resonance (PWR) is a notable variation of SPR spectroscopy that has proven powerful to characterize membrane-protein interaction [7]. BLI, in contrast, measures shift in light interference from an optical biosensor tip as analyte binds, without requiring flow systems. Both methods enable precise analysis of biomolecular interactions, with BLI offering greater simplicity and tolerance to complex samples [8].

  Magnetic resonance techniques, including NMR and EPR, probe atomic environments and spin dynamics, offering structural and dynamic information simultaneously. NMR can be used to measure apparent affinity, typically by tracking chemical shift perturbation obtained with a ligand titration [9]. EPR is sensitive to unpaired electrons found in radicals or metal centers and can provide insights into molecular dynamics, local environments, and intermolecular interactions [10]. By analyzing changes in the mobility of the spin-labelled molecule upon complex formation, EPR enables the characterization of protein-protein interaction [11]. In particular, EPR has been used to study protein-lipid interactions, describing for instance the location and the relative affinity of these interactions [12]. These studies have predominantly relied on spin-labelled lipids, enabling the precise characterization of the lipid environment and its perturbation upon protein binding [13]. A key parameter extracted from continuous-wave EPR spectra is the rotational correlation time (τc), which describes how fast a spin label reorients and thus reflects its local environment: fast motion (τc<1ns) yields sharp three-line spectra, restricted motion (1–20 ns) produces broadened asymmetric lines, and immobilization (> 100 ns) gives a broad powder pattern.

  In this study, we develop and implement an EPR-based methodology to quantitatively assess the interaction between the protein Tau and lipid membranes. Tau is an intrinsically disordered protein implicated in neurodegenerative diseases such as Alzheimer’s disease in which it forms highly ordered aggregates known as amyloid fibrils [4]. Beyond its canonical microtubule-binding function, Tau localizes near neuronal membranes [14] where its interaction with specific lipids might play a role in its pathological activity [15]. Tau is overall positively charged, whereas the POPS membranes studied here are negatively charged, creating favorable electrostatic interactions.

  By monitoring changes in the mobility of a spin-labelled Tau variant upon lipid binding, we demonstrated that the binding modes and apparent binding affinities KD can be determined by titration. We further discuss how a single measurement, which provides the absolute quantity of bound protein, can be used to estimate apparent affinity. This article provides a robust framework for studying protein–membrane interactions with EPR in complex systems.


## Methods

### Tau expression and purification
  Expression of the recombinant Tau 2N4R isoform harboring the P301L pathogenic mutation and a C291S substitution was performed in E. coli BL21(DE3) cells transformed with a pET28-based plasmid. A starter culture (10 mL) was grown overnight and used to inoculate 1 L of LB medium containing kanamycin (30μg/mL). Cells were cultivated at 37 °C with orbital shaking (200 rpm) until reaching mid-log phase (OD600 = 0.6–0.8), at which point expression was triggered by the addition of 1 mM IPTG. After 3 h of induction, cells were collected by centrifugation (5000 rpm, 20 min, 4 °C) and resuspended in a lysis buffer composed of 50 mM Tris-HCl (pH 7.4), 100 mM NaCl, and 0.1 mM EDTA, supplemented with 1 mM PMSF, 5 mM DTT, 20μg/mL DNase, 10 mM MgCl2, and protease inhibitors. Lysis was carried out by lysozyme incubation (30 min, room temperature, agitation), followed by three freeze–thaw cycles using liquid nitrogen. After removal of cellular debris (9500 rpm, 10 min, 4 °C), the clarified lysate was subjected to a heat-treatment step (75 °C for 12 min), rapidly cooled on ice, and centrifuged again. The final supernatant was filtered and loaded onto a cation exchange column (UNO Sphere S, Bio-Rad), pre-equilibrated with 20 mM sodium phosphate buffer (pH 7.4) containing 0.1 mM EDTA and 100 mM NaCl. After washing, proteins were eluted using a linear gradient of NaCl up to 500 mM. Relevant fractions were pooled, concentrated, and further purified by gel filtration on a Superdex 200 Increase 16/600 pg column (Cytiva) equilibrated in 20 mM HEPES pH 7.4, 100 mM NaCl. The concentration of the purified Tau protein was determined spectrophotometrically at 274 nm using a molar extinction coefficient of 7.5 mM−1⋅cm−1. Samples were stored at −20 °C until use.


### Liposome formulation into multilamellar vesicles (MLVs)
  Multilamellar vesicles (MLVs) were prepared from 1-palmitoyl-2-oleoyl-sn-glycero-3-phospho-l-serine (POPS) alone or from mixtures of POPS and 1-palmitoyl-2-oleoyl-glycero-3-phosphocholine (POPC) with a 50/50 M ratio. The lipids, initially dissolved in chloroform, were combined at the desired molar ratio and dried under a stream of nitrogen to form a thin lipid film. To ensure complete removal of residual chloroform, the film was then placed under vacuum in a desiccator overnight. The resulting dry lipid film was rehydrated in 20 mM HEPES buffer pH 7.4, leading to the formation of multilamellar vesicles.


### Spin labeling of Tau
  Tau mutant was labelled on cysteine residue (C322) using the nitroxide spin label MTSL (CAS 81213-52-7). Tau was first reduced with TCEP for at least 2 h. TCEP was then removed using a PD-10 desalting column. A 10-fold molar excess of MTSL was added, and the mixture was incubated for 2 h under continuous stirring at room temperature. Excess spin label was eliminated by two successive PD-10 columns. The concentration of spin-labelled Tau was determined using a standard curve generated with TEMPO (10μM to 500μM range), and signal integration (single and double integrals) was performed using SpinToolbox with a labeling efficiency of 60 %.


### Continuous-wave electron paramagnetic resonance (CW-EPR)
  CW-EPR measurements were acquired using a Ciqtek EPR200M X-Band spectrophotometer operating at a microwave frequency of 9.8 GHz with modulation frequency of 100 kHz and a modulation amplitude of 1 G. The microwave power was set to 1 mW with an attenuation of 20 dB. The conversion time and time constant were set to 50 ms. The measurements were done at room temperature.

  Samples were prepared by first mixing 50μM labelled Tau with 0 to 25 mM of MLVs in 20 mM HEPES pH 7.4 buffer a few minutes prior to the measurement. Then, 6.4μL were transferred in two 0.8 mm diameter quartz capillaries. 1D CW-EPR spectrum were acquired for 30 min. CW-EPR spectra at room temperature were fitted using SimLabel software [16].

  The decomposition of experimental spectra with the two components described in Table 1 was done by fitting a relative weigh of each component, p1 and p2. The fraction of bound protein θ was defined as  θ=p2p1+p2

  The uncertainty on θ,Δθ was obtained from the uncertainty on p1 and p2, Δp1 and Δp2 respectively, provided by the fitting procedure:  Δθ=∂θ∂p1Δp1+∂θ∂p2Δp2   Δθ=p2p1+p22Δp1+p1+p2-p2p1+p22Δp2   Δθ=p2p1+p22Δp1+1p1+p2Δp2-p2p1+p22Δp2   Δθ=θΔp2p2+Δp1+Δp2p1+p2

  To determine the hyperfine coupling constants, CW EPR spectra were recorded under frozen conditions. Measurements on Tau monomer were performed on a Bruker ESP300E X-band spectrometer operating at 9.54 GHz, equipped with a TE102 rectangular resonator and an Oxford Instruments ESR900 helium-flow cryostat (30K). For Tau in the presence of POPS, spectra were acquired on a Ciqtek EPR200M X-band spectrometer operating at 9.42 GHz and 150 K. For these experiments, samples containing 50μM spin-labelled Tau were prepared in the presence or absence of POPS at a Tau:lipid molar ratio of 1:125. Spectra were simulated using the pepper function from easyspin in order to obtain the hyperfine coupling Az.


## Results

### EPR spectral lineshape in the absence and presence of lipids
  We performed site-specific spin labeling on tau 2N4R harboring the mutations P301L and C291S. The former is a disease-associated mutation whereas the later mutation removes one of the two native cysteines, enabling to only label the cysteine at position 322 with a nitroxide spin label MTSL. This mutant is referred to as Tau throughout the manuscript.

  We measured the continuous-wave electron paramagnetic resonance (CW-EPR) spectrum of monomeric labelled Tau at a concentration of 50μM (Fig. 1A dark blue). The spectral lineshape exhibits narrow peaks, indicative of a highly mobile spin label, which is consistent with a nitroxide label attached to an intrinsically disordered protein [17]. We titrated Tau with increasing concentration of multilamellar vesicles (MLVs) composed of 1-palmitoyl-2-oleoyl-sn-glycero-3-phospho-l-serine (POPS) (Fig. 1A blue to red). This titration shows that the spectral lineshape of monomeric Tau converges to a second well-defined lineshape at high lipid concentration (Fig. 1A red), characteristic of restricted spin-label mobility. This change in lineshape reflects a direct interaction between Tau and POPS, as previously reported by other methods [18].

  We fitted the experimental data corresponding to the first lineshape (Tau monomer) and the second lineshape (Tau in excess of POPS), using SimLabel software (Fig. 1C & D) [19]. Following established guidelines, we first measured the Az component from the spectra of frozen samples (Fig. 1B) and determined gx according to [19]:  gx=fAz=-0.0025xAz+2.0175

  The g-tensor components gy,gz were fixed to 2.0061 and 2.0022 respectively following the guidelines [19]. The spectra were fitted by varying the correlation time, axial hyperfine coupling Ax=Ay and a Lorentzian line broadening (representing peak spacing). The fitted values for each condition are summarized in Table 1 and the corresponding simulation are shown in Fig. 1C,D.


### CW-EPR spectra of tau in presence of lipids can be decomposed into two components
  Fig. 2A shows the presence of two characteristic spectral lineshapes, with one progressively shifting toward the other upon addition of anionic lipids, POPS. These two components differ in their rotational correlation time (Table 1), which reflects the local dynamics of the nitroxide spin label. The first component corresponds to a fast-motion regime (Fig. 1C), while the second reflects slower dynamics (Fig. 1D). The fast component arises from unstructured, highly dynamic monomeric Tau in solution, whereas the slow component results from a direct interaction between spin label and a large object that restricts its motion, here POPS MLVs. Based on this, we define two distinct states: monomeric Tau in solution, referred to as “free”, and Tau interacting with MLVs, referred to as “bound”. According to this definition, one expects that the titration of lipids should shift the populations of the free and bound states, which are in thermodynamic equilibrium.

  Consistently with this prediction, all spectra can be accurately modeled using this two-component approach by simply changing the population of the free and bound components (Fig. 2). A representative example is shown in Fig. 2B, where the individual contributions of the free (blue) and bound (orange) components are explicitly highlighted.

  From the above analysis, we extracted the fraction of bound protein θ, defined as  θ=p2p1+p2  where p1 and p2 are the weight of the free and bound component, respectively. This fraction θ is plotted as a function of each lipid concentration, in Fig. 3. This EPR-derived binding curve can then be fitted by conventional interaction model to obtain information on binding modes and constants, as described below.


### Fitting EPR-based binding curves
  In order to elucidate the binding mechanism governing the interaction between Tau and POPS, the concentration of bound protein as a function of lipid concentration was fitted to different binding models: quadratic, non-stoichiometric quadratic, and cooperative binding models.

  A quadratic model assumes a 1:1 binding stoichiometry between Tau and POPS, consistent with a simple, non-cooperative interaction [20]. It is described by the equation:  (1) θ=[P]+[L]+KDquad-[P]+[L]+KDquad2-4[P][L]122[P]  where [P] is the total protein concentration, [L] is the total lipid concentration and KD is the apparent binding affinity constant.

  The non-stoichiometric quadratic model indicates a non-linear behavior, where Tau binds to multiple POPS molecules (1:X stoichiometry, with X > 1). This model, described by the following equation, was previously used to describe protein interacting with multiple lipid molecules on a membrane [21].  (2) θ=12[P][P]+[L]STO+KDnon–st-[P]+[L]STO+KDnon–st2-4[L][P]STO12  where KDnon-st refers to the apparent binding affinity and STO to the stoichiometry (i.e., number of interacting lipids per protein molecule).

  Finally, cooperativity refers to a behavior in which the binding properties of each protein molecule are interdependent, i.e., initial binding events influence subsequent ones. It is often described by the simplified model of the Hill equation:  (3) θ=[L]nHK50nH+[L]nH  where K50 is the lipid concentration at half-maximal protein binding, rather than a true dissociation constant, due to the cooperative nature of the interaction. K50 is used in the Hill equation as an empirical affinity constant. nH is a cooperativity parameter. The higher nH is, the more cooperative is the system.

  Fig. 4 shows the fit of each model to the experimental data and the output fitted parameters are shown in Table 2. The data are best described by the non-stoichiometric quadratic model or Hill model, indicating that our system tau-POPS is not optimally described by the simple quadratic model. The non-stoichiometric model, used previously for a very similar system [21], has the advantage of using a physical parameter directly interpretable, which is the number of lipid molecules interacting with one protein molecule (STO). However, the apparent binding constant obtained from this model cannot be directly compared to those derived from the other models, since it reflects an affinity per lipid cluster rather than per lipid molecule. The lower apparent affinity value therefore arises from the rescaling of the lipid concentration by the stoichiometric factor (STO ≈ 28 in our case). As shown in Table 2, the variance of the apparent binding affinity is high (almost 100 %), making this model intrinsically unprecise to determine the affinity. In contrast, the cooperative binding provides a more accurate affinity, although hill coefficient has no direct physical meaning.


### EPR provides absolute population quantification
  The approach presented above exploits a typical binding curve, which can be built from any physical parameter that is proportional to the bound population (fluorescence, absorption, calories, chemical shift, etc… see introduction). The good fit of common interaction models (Fig. 3) reinforces the finding that the two-component decomposition of the EPR spectrum, developed in Section 2, can indeed probe the bound/free protein population.

  However, the EPR-based population extracted here provides much richer information, which is the absolute concentration of bound protein. This contrasts with most methods used to investigate interactions that rely on relative readouts, which can only be interpreted through a full titration curve.

  Indeed, since EPR is a quantitative method, every spectrum is decomposed into absolute concentrations of bound and free protein. This absolute quantification is particularly useful for mechanistic studies. For instance, directly assessing the absolute concentration of interacting protein is valuable for studies that aim to link a relevant mechanism (such as functional or pathological activity, aggregation, etc…) to the quantity of protein bound to a target. This capability is particularly advantageous when screening different environmental conditions (e.g., buffers, crowding) that can influence binding affinity. In such scenarios, EPR can directly assess the quantity of protein effectively bound in each condition, eliminating the need for a full affinity characterization through an entire titration curve.

  The first implication of this absolute quantification is that binding affinity can be obtained from a minimal number of measurements, ideally one or two, according to Eqs. (1)–(3). We specifically detail this approach below.


#### Measurement of affinity constants
  For each model, KD (or K50 in the case of Hill model) can be expressed analytically as a function of θ, the experimentally measured fraction of bound protein. These equations allow direct computation of the apparent binding constant from a single measurement.

  For the quadratic binding model, Eq. (1) can be rearranged to isolate the square root  [P]+[L]+KDquad2-4[P][L]12=[P]+[L]+KDquad-2[P]θ

  Squaring both sides and simplifying the equation:  -4[P][L]=-4[P]θ[P]+[L]+KDquad+4[P]2θ

  Finally, rearrange and solve to obtain KDquad for quadratic model  KDquad=([L]-[P]θ)(1-θ)θ   KD quad=[L]1θ-1-[P](1-θ)   (4) KDquad=(1-θ)([L]-θ[P])θ

  For the non-stoichiometric quadratic model, the KDnon–st can be extracted by rearranging the equation. First isolating square root term from Eq. (2)  [P]+[L]STO+KDnon–st-2[P]θ=[P]+[L]STO+KDnon–st2-4[L][P]STO12

  Squaring both sides and simplifying  -4LPSTO=-4[P]θ[P]+[L]STO+KDnon–st+4[P]2θ

  Rearranging and solving for KD  (5) KDnon–st=(1-θ)|L|Sto-θ[P]θ

  For the cooperative (Hill-type) model, the K50 is extracted by rearranging Eq. (3)  K50nHθ=[L]nH-[L]nHθ   K50nH=[L]nH(1-θ)θ

  Therefore K50 for cooperative equation can be expressed as  (6) K50=[L]1-θθ1/nH  where nH is the Hill coefficient. Note that in this model K50 is independent of [P] and is purely lipid-centric.

  In these equations, [L] and [P], the concentrations of lipid and protein, respectively, are experimental input; θ, the fraction of bound protein, is measured by EPR; and KD,K50,nH and STO are unknown parameters characterizing the affinity of the protein and the lipid.

  Fig. 4 illustrates the relationship between the dissociation constant KD and the bound fraction (θ) for each model described by Eqs. (4), (5) and (6). At the extremes of the binding curve, when θ approaches 0 (mostly unbound) or 1 (nearly saturated), the slopes of the curves are exceptionally steep. Consequently, even minor experimental uncertainties in θ in these regions can result in significant errors in the estimated KD.

  In the Hill model (Fig. 4C), curves corresponding to different values of nH around the experimental value intersect at θ=0.5. This implies that K50 can be determined independently of nH when θ is measured near 0.5.

  To further assess the reliability of single-point or minimal-point affinity measurements, we next derived analytical expressions for error propagation in each model. This analysis allowed us to identify the θ range where experimental uncertainty has the least impact on the calculated KD, thereby establishing a robust window for accurate affinity determination.


#### Analysis of error propagation
  To evaluate the reliability of single-point KD estimation across different models, we derived and analyzed the propagation of experimental error in the bound fraction θ to the calculated binding constants. Mathematically, this is expressed as the relationship between the relative error on KD,ΔKDKD, and the experimental uncertainty Δθ. For that, we defined a propagation factor A as ΔKDKD=Amodel×Δθ.

  For the quadratic model, the error propagation can be derived from the Eq. (4) by differentiating KD with respect to θ:  δKD quadδθ=δδθL1θ-1-δδθ([P](1-θ))   δKD quadδθ=-[L]θ2+[P]

  Dividing both sides by Kd  ΔKD quadKDquad=1KDquad-[L]θ2+[P]Δθ

  Substituting KD from the Eq. (8) and solving for the final equation  (7) ΔKDquadKDquad=-[L]+θ2Pθ(1-θ)([L]-θ[P])Δθ   ⟺ΔKDquadKDquad=Aquad(θ)×Δθ

  For the non-stoichiometric quadratic model, the expression of the error propagation factor A is obtained by differentiating KD with respect to θ from Eq. (5) to get δKDnon-stδθ.

  The error propagation formula for relative error is given by:  ΔKDnon–stKDnon–st=1KDnon–stδKDδθΔθ

  We get the final equation as:  (8) ΔKDnon–stoKDnon–sto=-[L]+STOθ2[P]STOθ(1-θ)[L]STO-θ[P]Δθ   ⟺ΔKDKD=AnonSto(θ)×Δθ

  Finally, for the Hill model, the propagation can be calculated by first taking the log of Eq. () and then differentiating it with respect to theta:  lnK50=ln(L)+1nH(ln(1-θ)-ln(θ))   1K50δK50δθ=1nH-11-θ-1θ   1K50δK50δθ=1nHθ1-θ   (9) ΔK50K50=ΔθnHθ(1-θ)   ⟺ΔK50K50=Ahill(θ)×Δθ

  Our analysis of the error propagation factor, shown in Fig. 5, provides crucial insights into the precision of parameter determination. All models exhibit a U-shaped curve with errors increased drastically near θ=0 and θ=1, but minimized in the central region around θ=0.5.

  In the non-stoichiometric quadratic model (Fig. 5B), the stoichiometry coefficient (STO) has a significant impact on error propagation. A higher STO is not favorable and increase the error propagation factor. In the Hill model (Fig. 5C), the error propagation is inversely proportional to the Hill coefficient nH, making the measurement of K50 more accurate in high cooperativity systems.

  It should be noted that we analyze in detail the error propagation only from θ because this is the parameter extracted from the decomposition of the EPR spectra, which we thus expect to present the most uncertainty. Nonetheless, the reactant concentration [L] and [P], chosen in the experimental design, should also be controlled as precisely as possible in order to best estimate affinity. Note that from Eqs. (4)–(6), the affinity uncertainty will vary linearly with the uncertainty on [L] and [P].

  Altogether, these results support a general recommendation: to minimize uncertainty on affinity constants from minimal data, θ should ideally be measured within the 0.4–0.6 range, where error propagation is lowest.


#### Practical strategy for reliable KD determination from minimal data
  In practice, each EPR measurement at a given protein concentration [P] and lipid concentration [L] will provide an experimental value of θ. Determining the apparent dissociation constant KD from a minimal number of data points requires the experimental approach to be adapted to the underlying binding model. Experimentally, the species containing the label, here P, is conveniently kept at a constant concentration, usually to compromise between sensitivity and protein consumption (typically tens of μM). The concentration of lipid [L] is then the experimental parameter that can be changed to measure θ within the optimal range. If θ is too small (i.e., not enough bound protein), [L] can be increased. If θ is too large (i.e., too much bound protein), [L] can be decreased.

  For the quadratic model, a single measurement of the bound fraction θ is sufficient as seen in Eq. (4). To ensure low error propagation, θ should be ideally measured between 0.4 and 0.6 (Fig. 5A). Determining KD in this region will be the most robust as it minimizes sensitivity to experimental uncertainty in θ measurements.

  For the non-stoichiometric quadratic and Hill models, it is possible to determine the binding parameters (affinity and stoichiometry/cooper-ativity) from two measurements, as there are two unknown parameters (Eqs. (5) and (6)). The model (non-stoichiometric quadratic or Hill) has to be assumed for the system under investigation.

  The model can in principle be identified from this approach by measuring a third point. In that case the optimal conditions would be to measure one point at a lower concentration (around θ=0.25), one in the mid-range (around θ=0.5), and one at a higher concentration (around θ=0.75). Yet, this minimal data approach is not recommended when the binding model is unknown.

  If the binding mode is unknown, the most pragmatic strategy is to perform a single measurement around θ=0.5. First, this leverages the fact that, across all models, error propagation is minimized at this value (Fig. 5). Moreover, Fig. 4 shows that around θ=0.5, the KD determination is independent of the model between Hill and quadratic models (recalling that nH=1 in the hill model is equivalent to the quadratic model). In that case, the minimal-data approach would be used for qualitative or relative assessment of the affinity. Recommendations are summarized in Table 3.


### Application physiological conditions
  Building on the minimal-data approach to estimate apparent dissociation constants, we applied this methodology to two different data sets of the Tau/lipid system. In addition to the conditions used in Fig. 4 (membrane POPS), we performed measurements with a modified membrane composition (membrane POPS:POPC 50:50). We measured the population of bound Tau θ at three different lipid concentrations. The data are summarized in Table 4.

  It is worth noting that, although measuring three distinct points around θ=0.25,0.5and0.75 is theoretically optimal to obtain reliable binding parameters, it is experimentally challenging to precisely obtain these θ values.

  We applied the cooperative binding model that gave the best fit in Fig. 4. We fit three data points around 0.25,0.5 and 0.75 to Eq. (6) and extract the corresponding K50 and nH.

  We obtained K50 = 0.65 ± 0.04mM when three points are used, as compared to 0.64 ± 0.04 mM found for the complete dataset (Table 4). Both values are identical within error, indicating that the three-point approach provides a robust and reliable estimate of K50. A more pronounced difference is observed in the Hill coefficient nH, which reflects binding cooperativity. nH of 1.81 ± 0.04 was found with three points, as compared to 2.30 ± 0.04 obtained using all data (Table 4). Although both values remain close to 2, this difference shows that the minimal-data approach is less robust to evaluate cooperativity.

  Then, we estimated the apparent dissociation constant using a single data point around θ≈0.5. We fixed nH to the one obtained with all data and we extracted K50 and its uncertainty from Eqs. (6) and (9), respectively. K50 was found at 0.71 ± 0.16 mM, exhibiting a remarkable similarity with K50 obtained from the full titration (0.64 ± 0.04). The uncertainty is larger (22 % for single point determination versus 6 % for full titration), but remains within an acceptable range.

  We applied the same approach for the membrane composed of 50/50 % POPS/POPC. From three data points, we could also obtain both K50 and nH, taking the values of 0.67 ± 0.01mM and 1.26 ± 0.03, respectively (Table 4). While the affinity is similar than for POPS membrane, nH was found significantly smaller, indicating less cooperativity when the membrane charges are reduced. Finally, with a single data point, fixing nH to the value obtained with more data, we found a K50 of 0.78 ± 0.15 mM. Similarly to the POPS membrane model, K50 obtained from a single point is similar to the one obtain from more data (0.78 ± 0.15 mM, compared to 0.67 ± 0.01 mM) and only the uncertainty increases (19 % uncertainty with a single data point).

  Altogether, these results demonstrate that we can obtain reliable estimate of binding parameters with minimal experimental points: 3 data points allows to measure both K50 and nH while a single point provides K50 with about 20 % uncertainty if nH is known.


## Conclusion
  In this study, we developed and validated a CW-EPR–based methodology to quantify the apparent binding affinity between an intrinsically disordered protein and lipid membranes. By performing a spectral decomposition of spin-labelled Tau and carefully modeling the free and bound populations, we demonstrated that we can reliably extract the absolute concentration of bound and free protein.

  From the population of bound protein, we showed that we can fit different binding models, quadratic, non-stoichiometric, and cooperative. In our conditions, we demonstrated that the Hill model provides the most reliable description of the Tau–lipid interaction, offering well-defined parameters and capturing potential multivalent or clustering effects at the membrane surface.

  Furthermore, we established a framework for estimating apparent binding affinity from a single or limited number of experimental data points. This is possible by leveraging the fact that EPR-extracted population provides the absolute concentration of bound protein. We provide practical consideration to minimize uncertainty when using the minimal-data approach.

  Altogether, this work introduces a versatile and accessible EPR-based approach for probing protein–membrane interactions. It paves the way for future studies investigating the molecular determinants of membrane recruitment, particularly in the context of intrinsically disordered proteins and their role in pathological aggregation processes. We also expect this approach to be applicable to other system (interaction between any protein and membrane, interaction between proteins), provided that the bound state leads to a change in EPR lineshape.


## Data availability
  Data will be made available on request.


## Acknowledgements
  The authors thank the European Research Council (Grant 101040138), National Institute of General Medical Sciences (Grants R24GM146107 and R35GM151218) the Fondation Vaincre Alzheimer and the Federation of European Biochemical Societies for their financial support.

  The authors declare the following financial interests/personal relationships which may be considered as potential competing interests:

  Yann Fichou reports financial support was provided by National Centre for Scientific Research. Yann Fichou reports financial support was provided by European Research Council. Yann Fichou reports financial support was provided by Federation of European Biochemical Societies. Yann Fichou reports financial support was provided by Foundation Overcoming Alzheimer. If there are other authors, they declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper.