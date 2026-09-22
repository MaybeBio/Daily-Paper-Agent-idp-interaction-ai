## Spin glass model of in-context learning

Large language models show a surprising in-context learning ability—being able to use a prompt to form a prediction for a query, yet without additional training, in stark contrast to old-fashioned supervised learning. Providing a mechanistic interpretation and linking the empirical phenomenon to physics are thus challenging and remain unsolved. We study a simple yet expressive transformer with linear attention and map this structure to a spin glass model with real-valued spins, where the couplings and fields explain the intrinsic disorder in data. The spin glass model explains how the weight parameters interact with each other during pre-training, and further clarifies why an unseen function can be predicted by providing only a prompt yet without further training. Our theory reveals that for single-instance learning, increasing the task diversity leads to the emergence of in-context learning, by allowing the Boltzmann distribution to converge to a unique correct solution of weight parameters. Therefore the pre-trained transformer displays a prediction power in a novel prompt setting. The proposed analytically tractable model thus offers a promising avenue for thinking about how to interpret many intriguing but puzzling properties of large language models.

Introduction. — Thanks to earlier breakthroughs in processing natural languages (e.g., translation), vector representation and attention concepts were introduced into machine learning [ 1 , 2 , 3 , 4 ] , which further inspired a recent breakthrough of implementing the self-attention as a feedforward model of information flow, namely transformer [ 5 ] . The self-attention captures dependencies between different parts of the input (e.g., image or text), coupled with a simple cost of next-token prediction [ 6 , 7 ] , leading to a revolution in the field of natural language processing [ 8 ] , so-called large language model (LLM).

One of the astonishing abilities of the transformer is the in-context learning [ 9 ] , i.e., the pre-trained transformer is able to accomplish previously-unseen complicated tasks by showing a short prompt in the form of instructions and a handful of demonstrations, especially without a need for updating the model parameters. LLMs thus develop a wide range of abilities and skills (e.g., question answering, code generation) [ 10 ] , which are not explicitly contained in the training dataset and are not specially designed to optimize. This remarkable property is achieved only by training for forecasting the next tokens and only if corpus and model sizes are scaled up to a huge number [ 11 , 12 ] . The above characteristics of transformer and the in-context learning (ICL) are in stark contrast to perceptron models in the standard supervised learning context, presenting a formidable challenge for a mechanistic interpretation [ 13 , 14 ] .

To achieve a scientific theory of ICL, previous works focused on optimization via gradient descent dynamics [ 15 , 16 ] , representation capacity [ 17 ] , Bayesian inference [ 18 , 19 ] , and in particular the pre-training task diversity [ 20 , 19 , 21 , 22 ] . The theoretical efforts were commonly based on a single-layer linear attention [ 23 , 15 , 21 , 24 ] , which revealed that a sufficient pre-training task diversity guarantees the emergence of ICL, i.e., the model can generalize beyond the scope of pre-training tasks.

However, rare connections are established to physics models, which makes a physics model of ICL lacking so far, preventing us from a deep understanding of how ICL emerges from pre-trained model parameters. Here, we treat the transformer learning as a statistical inference problem, and then rephrase the inference problem as a spin glass model, where the transformer parameters are turned into real-valued spins, and the input sequences act as a quenched disorder, which makes the spins strongly interact with each other to lower down the ICL error. A unique spin solution exists in the model, guaranteeing that the transformer can predict the unknown function embedded in test prompts. The derived formulas specify the intelligence boundary of ICL and how this can be achieved.

Transformer with linear attention. — We consider a simple transformer structure—a single-layer self-attention transforming an input sequence to an output one. Given an input sequence 𝐗 ∈ ℝ D × N \mathbf{X}\in\mathbb{R}^{D\times N} , where D D is the embedding dimension and N N is the context length, the self-attention matrix is a softmax function Softmax ​ ( 𝐐 ⊤ ​ 𝐊 / D ) \text{Softmax}(\mathbf{Q}^{\top}\mathbf{K}/\sqrt{D}) , where 𝐐 = 𝐖 Q ​ 𝐗 \mathbf{Q}=\mathbf{W}_{\text{Q}}\mathbf{X} , 𝐊 = 𝐖 K ​ 𝐗 \mathbf{K}=\mathbf{W}_{\text{K}}\mathbf{X} . 𝐖 Q \mathbf{W}_{\rm Q} and 𝐖 K \mathbf{W}_{\rm K} are the query and key matrices ( ∈ ℝ D × D \in\mathbb{R}^{D\times D} ), respectively. D \sqrt{D} inside the softmax function makes its argument order of unity. The self-attention refers to the attention matrix generated from the input sequence itself and allows each element (query) to attend to all other elements in one input sequence, being learnable through pre-training. The softmax function is thus calculated independently for each row. Taking an additional transformation 𝐕 = 𝐖 V ​ 𝐗 \mathbf{V}=\mathbf{W}_{\text{V}}\mathbf{X} , where 𝐖 V ∈ ℝ D × D \mathbf{W}_{\rm V}\in\mathbb{R}^{D\times D} is the value matrix, one can generate the output 𝐘 = 𝐕 ⋅ Softmax ​ ( 𝐐 ⊤ ​ 𝐊 / D ) \mathbf{Y}=\mathbf{V}\cdot\text{Softmax}(\mathbf{Q}^{\top}\mathbf{K}/\sqrt{D}) . Hence, this simple transformer implements a function φ TF ​ ( 𝐗 ) : ℝ D × N → ℝ D × N \varphi_{\rm TF}(\mathbf{X}):\mathbb{R}^{D\times N}\to\mathbb{R}^{D\times N} .

For simplicity, we replace the computationally expensive softmax with linear attention, which is still expressive [ 25 ] . Defining 𝐖 ≡ 𝐖 Q ⊤ ​ 𝐖 K \mathbf{W}\equiv\mathbf{W}_{\text{Q}}^{\top}\mathbf{W}_{\text{K}} , and choosing 𝐖 V = 𝟙 D \mathbf{W}_{\text{V}}=\mathds{1}_{D} ( 𝟙 D \mathds{1}_{D} indicates a D × D D\times D identity matrix) for our focus on the query and key matrices, we re-express the linear transformer as 𝐘 = N − 1 ​ 𝐗𝐗 ⊤ ​ 𝐖𝐗 \mathbf{Y}=N^{-1}\mathbf{X}\mathbf{X}^{\top}\mathbf{W}\mathbf{X} , where 𝐗 \mathbf{X} contains prompts and the query (to be predicted by the transformer), and 𝐖 ∈ ℝ D × D \mathbf{W}\in\mathbb{R}^{D\times D} is the equivalent weight matrix to be trained, and N − 1 N^{-1} is a normalization coefficient (see more explanations in SM [ 26 ] which also discusses a separate training of query and key matrices ).

We next design the training task as a high-dimensional linear regression. Each example consists of the data 𝒙 ∼ 𝒩 ⁡ ( 0 , 𝟙 D ) \bm{x}\sim\mathcal{N}(0,\mathds{1}_{D}) and the corresponding label y = 𝒘 ⊤ ​ 𝒙 / D y=\bm{w}^{\top}\bm{x}/\sqrt{D} , where the latent task weight 𝒘 ∼ 𝒩 ⁡ ( 0 , 𝟙 D ) \bm{w}\sim\mathcal{N}(0,\mathds{1}_{D}) . To construct the μ \mu -th input matrix 𝐗 μ \mathbf{X}^{\mu} , we use N N samples as prompts using the same 𝒘 μ \bm{w}^{\mu} yet different 𝒙 \bm{x} within the input sequence. An additional sample 𝒙 ~ μ \bm{\tilde{x}}^{\mu} is regarded as the query whose true label y ~ \tilde{y} is masked yet to be predicted by the transformer. The structure of each input matrix 𝐗 μ \mathbf{X}^{\mu} is thus represented as

Due to this form of the input matrix, the number of trainable elements in 𝐖 \mathbf{W} becomes ( D + 1 ) 2 (D+1)^{2} . The last element of 𝐘 \mathbf{Y} corresponds to the predicted label of the query 𝒙 ~ μ \bm{\tilde{x}}^{\mu} , i.e., y ^ μ = 𝐘 D + 1 , N + 1 μ \hat{y}^{\mu}=\mathbf{Y}_{D+1,N+1}^{\mu} . The goal of ICL is to use the prompt to form a prediction for the query, and the true function governing the linear relationship for the testing prompt is hidden during pre-training because each μ \mu is generated by an independently drawn 𝒘 \bm{w} during both training and test phases. This is in stark contrast to standard supervised learning in perceptron networks that learn a single 𝒘 \bm{w} (in both training and testing) from examples [ 27 ] . We consider an ensemble of P P sequences, and P P is thus called the task diversity. This setting is a bit different from that in recent works [ 19 , 21 ] .

The pre-training is carried out by minimizing the mean squared error function, and the total training loss is given by

where λ \lambda controls the weight-decay strength. The generalization error on unseen tasks is written as ϵ g = 𝔼 𝒙 ~ , 𝒘 , 𝐖 | 𝒟 , 𝒟 ​ ( y ~ − y ^ ) 2 \epsilon_{g}=\mathbb{E}_{\bm{\tilde{x}},\bm{w},\mathbf{W}|\mathcal{D},\mathcal{D}}(\tilde{y}-\hat{y})^{2} , where the ensemble average over all disorders including the pre-training tasks 𝒟 \mathcal{D} is considered .

Spin-glass model mapping. — Equation ( 2 ) can be treated as a Hamiltonian in statistical physics. The linear attention structure makes the spin-model mapping possible. This proceeds as follows. The prediction to the μ \mu -th input matrix can be recast as y ^ μ = N − 1 ​ ∑ m , n 𝐂 D + 1 , m μ ​ 𝐖 m , n ​ 𝐗 n , N + 1 μ \hat{y}^{\mu}=N^{-1}\sum_{m,n}\mathbf{C}_{D+1,m}^{\mu}\mathbf{W}_{m,n}\mathbf{X}_{n,N+1}^{\mu} , where 𝐂 μ ≡ 𝐗 μ ​ 𝐗 μ ⊤ \mathbf{C}^{\mu}\equiv\mathbf{X}^{\mu}\mathbf{X}^{\mu\top} . Then we define an index mapping Γ : ( m , n ) → i \Gamma:(m,n)\to i to flatten a matrix into a vector. Therefore, one can write σ i = Γ ​ 𝐖 m , n \sigma_{i}=\Gamma\mathbf{W}_{m,n} , and s i μ = Γ ​ 𝐒 m , n μ s_{i}^{\mu}=\Gamma\mathbf{S}_{m,n}^{\mu} , where 𝐒 m , n μ = N − 1 ​ 𝐂 D + 1 , m μ ​ 𝐗 n , N + 1 μ \mathbf{S}^{\mu}_{m,n}=N^{-1}\mathbf{C}_{D+1,m}^{\mu}\mathbf{X}_{n,N+1}^{\mu} , and i = ( D + 1 ) ​ ( m − 1 ) + n i=(D+1)(m-1)+n , and finally the prediction as y ^ μ = ∑ i s i μ ​ σ i \hat{y}^{\mu}=\sum_{i}s_{i}^{\mu}\sigma_{i} . Consequently, the mean-squared error for each input matrix reads

where we omit the constant term ( y ~ μ ) 2 / 2 (\tilde{y}^{\mu})^{2}/2 .

Upon defining J i ​ j μ ≡ − s i μ ​ s j μ J_{ij}^{\mu}\equiv-s_{i}^{\mu}s_{j}^{\mu} , h i μ ≡ y ~ μ ​ s i μ h_{i}^{\mu}\equiv\tilde{y}^{\mu}s_{i}^{\mu} , and λ i μ ≡ λ − J i ​ i μ \lambda_{i}^{\mu}\equiv\lambda-J_{ii}^{\mu} , one can rewrite the total loss ℒ = ( 1 / P ) ​ ∑ μ ℓ μ + 1 2 ​ λ ​ ‖ 𝐖 ‖ 2 \mathcal{L}=(1/P)\sum_{\mu}\ell^{\mu}+\frac{1}{2}\lambda\|\mathbf{W}\|^{2} as

By moving the elements for i = j i=j in the first term to the regularization term, and defining an anisotropic regularization coefficient λ i μ ≡ λ − J i ​ i μ \lambda_{i}^{\mu}\equiv\lambda-J_{ii}^{\mu} , we can formally define the effective interaction J i ​ j ≡ ( 1 / P ) ​ ∑ μ J i ​ j μ J_{ij}\equiv(1/P)\sum_{\mu}J_{ij}^{\mu} , the external field h i ≡ ( 1 / P ) ​ ∑ μ h i μ h_{i}\equiv(1/P)\sum_{\mu}h_{i}^{\mu} and the regularization factor λ i ≡ ( 1 / P ) ​ ∑ μ λ i μ \lambda_{i}\equiv(1/P)\sum_{\mu}\lambda_{i}^{\mu} . Finally, we obtain a spin glass model with the following Hamiltonian

where the total number of spins is given by ( D + 1 ) 2 (D+1)^{2} . According to Eq. ( 2 ), this is precisely the Hamiltonian for a high-dimensional ridge regression interpretation of ICL .

The disorder in the pre-training dataset including the diversity in the latent task vectors 𝒘 \bm{w} is now encoded into the interactions between spins, and random fields the spins feel. In fact, this is a densely connected spin glass model, while the coupling and field statistics do not have an analytic expression [ 28 ] , as they bear a fat tail (Fig. 1 ). This reminds us of the two-body spherical spin model studied in spin glass theory [ 29 , 30 ] , but the current glass model of ICL seems much more complex than the spherical model. By construction, this model reflects the nature of associative memory [ 31 ] , yet the spin variable is now the underlying parameter of the transformer. To conclude, we derive a spin glass model of ICL, opening a physically appealing route towards the mechanistic interpretation of ICL and even more complex transformers (see extra experiments in [ 26 ] ).

The specific form of J i ​ j J_{ij} and h i h_{i} rely on 𝐒 m , n \mathbf{S}_{m,n} defined as 𝐒 m , n = N − 1 ​ 𝐂 D + 1 , m ​ 𝐗 n , N + 1 \mathbf{S}_{m,n}=N^{-1}\mathbf{C}_{D+1,m}\mathbf{X}_{n,N+1} . The index μ \mu is omitted here. The matrix 𝐒 \mathbf{S} is divided into three blocks: the last column is an all-zero vector [due to the masked label in Eq. ( 1 )], while the other two blocks are labeled as 𝒜 \mathcal{A} ( m < D + 1 , n ≠ D + 1 m<D+1,n\neq D+1 ) and ℬ \mathcal{B} ( m = D + 1 , n ≠ D + 1 m=D+1,n\neq D+1 ). As h i = 1 P ​ ∑ μ y ~ μ ​ s i μ h_{i}=\frac{1}{P}\sum_{\mu}\tilde{y}^{\mu}s_{i}^{\mu} , the field matrix has the same block structure with 𝐒 \mathbf{S} [Fig. 1 (a)]. In addition the interaction matrix 𝐉 \mathbf{J} , generated by the outer product of the flattened 𝐒 \mathbf{S} with itself, has three main blocks, labeled as 𝒞 \mathcal{C} , 𝒟 \mathcal{D} , and ℰ \mathcal{E} respectively in Fig. 1 (b).

In contrast to traditional spin glass models [ 29 ] , P ⁡ ( 𝐉 ) P(\mathbf{J}) [or P ⁡ ( 𝒉 ) P(\bm{h}) ] does not have an analytic form [ 28 ] , as the coupling or field can be expressed as a complex function of a sum of products of two i.i.d. standard Gaussian random variables (see details in [ 26 ] ). Therefore, we provide the numerical estimation of the coupling distribution, which all bear a fat tail not captured by a Gaussian fitting [Fig. 1 (c)] . We thus define a new type of spin glass model corresponding to ICL, or a metaphor of transformer in large language models.

Statistical mechanics analysis. — The probability of each weight configuration is given by the Gibbs-Boltzmann distribution P ⁡ ( 𝝈 ) = e − β ​ ℋ ​ ( 𝝈 ) / Z P(\bm{\sigma})=e^{-\beta\mathcal{H}(\bm{\sigma})}/Z , where Z Z is the partition function, and β \beta is an inverse temperature tuning the energy level. Because the statistics of couplings and fields have no analytic form, one has to use the cavity method widely used in spin glass theory [ 32 ] . The cavity method is also known as the belief propagation algorithm, working by iteratively solving a closed equation of cavity quantity, i.e., a spin is virtually removed [ 31 ] . The cavity method can thus be used on single instances of ICL. Different weight components are likely strongly correlated, but the cavity marginal η i → j ​ ( σ i ) \eta_{i\to j}(\sigma_{i}) becomes conditionally independent in the absence of spin j j , which facilitates our derivation of the following self-consistent iteration (namely mean-field equation, see [ 26 ] for more details):

where z i → j z_{i\to j} is a normalization constant, and η i → j \eta_{i\to j} is defined as the cavity probability of spin σ i \sigma_{i} in the absence of the interaction between spins i i and j j . After the iteration reaches a fixed point, the marginal probability η i ​ ( σ i ) \eta_{i}(\sigma_{i}) of each spin can be calculated by

Because of the continuous nature of spin and weak but dense interactions among spins, we can further simplify the mean-field equation [Eq. ( 6 )], and derive the approximate message passing (AMP) by assuming η i ​ ( σ i ) ∼ 𝒩 ⁡ ( m i , v i ) \eta_{i}(\sigma_{i})\sim\mathcal{N}(m_{i},v_{i}) , where ( m i , v i ) (m_{i},v_{i}) is the fixed point of the following iterative equation:

which is also rooted in the Thouless–Anderson–Palmer equation in glass physics [ 33 , 31 ] . Technical details of deriving the AMP and the self-consistent justification of the Gaussian approximation are given in the appendix (an expanded one is given in [ 26 ] ).

Results. — In this paper, we consider a non-asymptotic setting: D D is kept finite and independent of P P and N N .

To see whether our spin glass model captures the correct structure of the weight matrix in the simple transformer, we first divide the weight matrix 𝐖 \mathbf{W} into blocks in the same way as we do for the input matrix, i.e.,

where 𝐖 11 ∈ ℝ D × D \mathbf{W}_{11}\in\mathbb{R}^{D\times D} , 𝐖 12 ∈ ℝ D × 1 \mathbf{W}_{12}\in\mathbb{R}^{D\times 1} , 𝐖 21 ∈ ℝ 1 × D \mathbf{W}_{21}\in\mathbb{R}^{1\times D} , and 𝐖 22 ∈ ℝ \mathbf{W}_{22}\in\mathbb{R} . With a large N N , the actual prediction of the transformer to the test query 𝒙 ~ \tilde{\bm{x}} can be written as

Hence, to get rid of post-training for a new task vector 𝒘 \bm{w} , the weight matrix of a well-pretrained transformer must satisfy

To derive the above equations, we have used 2 × 2 2\times 2 block matrix form of 𝐗 \mathbf{X} , the task y = 𝒘 ⊤ ​ 𝒙 / D y=\bm{w}^{\top}\bm{x}/\sqrt{D} , and 𝐗 0 ​ 𝐗 0 ⊤ ≈ N ​ 𝟙 D \mathbf{X}_{0}\mathbf{X}_{0}^{\top}\approx N\mathds{1}_{D} for large N N but finite D D , where 𝐗 0 = [ 𝒙 1 , 𝒙 2 , ⋯ , 𝒙 N ] \mathbf{X}_{0}=[\bm{x}_{1},\bm{x}_{2},\cdots,\bm{x}_{N}] . (see technical details in SM [ 26 ] ). In the case of P > 1 P>1 , the weights have a unique optimal solution 𝐖 11 = 𝟙 D \mathbf{W}_{11}=\mathds{1}_{D} and 𝐖 21 = 0 \mathbf{W}_{21}=0 . However, the minimum of the loss is not guaranteed to be unique if the Hamiltonian has zero modes, bearing similarity with Boltzmann machine learning [ 35 ] . The number of zero modes decreases with P P (see SM [ 26 ] ), supported by the following results (Fig. 2 and Fig. 3 ) as well.

In the standard stochastic gradient descent (SGD) training process minimizing Eq. ( 2 ), a large value of P P is needed to make the weight matrix converge to the unique solution. In Fig. 2 , we show the learning curves and the weight matrix after the training when the amount of training data P = 10 P=10 and P = 1 000 P=1\,000 respectively. By iterating the AMP equations [Eq. ( 8a ) and Eq. ( 8b )], we get a fixed point of { m i } \{m_{i}\} and { v i } \{v_{i}\} , transformed back into the matrix form by inverting Γ \Gamma . We find that the 𝐦 \mathbf{m} matrix exhibits the same property as the weight matrix that is well-trained by the SGD. Since the last column of 𝐖 \mathbf{W} is initialized as 𝒩 ⁡ ( 0 , 1 ) \mathcal{N}(0,1) and does not participate in the training, the solution of AMP retains the structure of m = 0 m=0 and v = 1 v=1 . This result shows that our spin glass model captures the properties of practical SGD training [ 24 , 36 , 37 ] . However, a separate training of query and key matrices makes the learning dynamics different, while yielding the same performance. Even if using a rough Gaussian fitting [Fig. 1 (c)] to the model parameters (the bulk is captured but not the tail), we get the diagonal structure of the weight matrix (see details in SM [ 26 ] ).

In Fig. 3 , we show the energy landscape of our spin glass model. When the task diversity P P is large enough, there is only one global minimum in the energy landscape, and the learning can easily reach the lowest energy. When P P is small, there emerge multiple local minima in the energy landscape, and the learning gets easily trapped by metastable states, which prevents the transformer from accurate in-context inference. We also support this observation by an analysis of the spectral density of the Hamiltonian’s Hessian matrix which displays a number of zero modes in SM [ 26 ] .

To get the phase diagram for single instance pre-training of the transformer, we define the contrast ratio as the cosine similarity between the 𝐦 \mathbf{m} matrix and the identity matrix: 𝒞 = [ ⟨ 𝐦 , 𝟙 D ⟩ / ( ‖ 𝐦 ‖ 2 ​ ‖ 𝟙 D ‖ 2 ) ] \mathscr{C}=\left[\langle\mathbf{m},\mathds{1}_{D}\rangle/(\|\mathbf{m}\|^{2}\|\mathds{1}_{D}\|^{2})\right] , where ⟨ 𝐀 , 𝐁 ⟩ = ∑ i ​ j 𝐀 i ​ j ​ 𝐁 i ​ j \langle\mathbf{A},\mathbf{B}\rangle=\sum_{ij}\mathbf{A}_{ij}\mathbf{B}_{ij} , ‖ 𝐀 ‖ 2 \|\mathbf{A}\|^{2} is the matrix Frobenius norm, and [ ⋯ ] [\cdots] denotes the average over different realizations. 𝒞 \mathscr{C} measures whether the model is well trained according to the transformed 𝐦 \mathbf{m} matrix. 𝒞 = 1 \mathscr{C}=1 means that the model converges to the unique solution, while 𝒞 = 0 \mathscr{C}=0 indicates that the model does not learn the features at all. We show a heat map of the contrast ratio with the task diversity P P and the prompt length N N in Fig. 4 (a). The heat map suggests that when the task diversity increases, a smooth transition to perfect generalization occurs, while keeping a large value of task diversity, increasing the prompt length further lowers the generalization error, which is consistent with recent empirical works [ 19 ] and theoretical works [ 21 ] based on random matrix theory (despite a slightly different setting). In addition, the AMP result coincides perfectly with the SGD (Fig. 4 (b), see also the case of non-i.i.d. data in SM [ 26 ] ), which verifies once again that our spin-glass model of ICL is able to predict an unseen embedded function in the test prompts, which is determined by the ground states of ℋ ⁡ ( 𝝈 ) \mathcal{H}(\bm{\sigma}) . We finally remark that our theory carries over to more complex situations of ICL (see further experiments in [ 26 ] ).

Conclusion. — A fundamental question in large language models is what contributes to the emergence ability of ICL, i.e., why simple next-token prediction-based pre-training leads to in-context learning of previously unseen tasks, especially without further tuning the model parameters. Here, we turn the ICL into a spin glass model and verify the equivalence between the standard SGD training and our statistical mechanic inference. We observe the fat tail distribution of coupling that determines how the model parameters of the transformer interact with each other. The transformer parameters are akin to an ensemble of real-valued spins in physics whose ground state suggests that the model can infer an unknown function from the shown test prompts after a pre-training of input sequences of sufficient task diversity. The phase diagram for single instance learning is also derived by our method, suggesting a continuous ICL transition.

The spin-glass model mapping of the linear transformer establishes a toy model of understanding emergent abilities such as ICL of large language models. The ground state determines the intelligence boundary, while the task diversity guarantees the accessibility of the ground state. Without a clear understanding of this toy model, it is hard to imagine what is really computed inside the black box of a general transformer in more complex tasks. Future exciting directions include explaining the chain-of-thought prompting [ 12 ] , i.e., decomposition of a complex task into intermediate steps, and more challenging case of hallucination [ 38 ] , i.e., the model could not distinguish the generated outputs from factual knowledge, or it could not understand what they generate [ 14 ] . We speculate that this hallucination may be intimately related to the solution space of the spin glass model given a fixed complexity of training dataset, e.g., spurious states in a standard associative memory model, as implied by Eq. ( 5 ). These open questions are expected to be addressed in the near future by considering this intriguing physics link, thereby enhancing the robustness and trustworthiness of AI systems.


## Acknowledgments

This research was supported by the National Natural Science Foundation of China for Grant number 12475045 and 12122515, and Guangdong Provincial Key Laboratory of Magnetoelectric Physics and Devices (No. 2022B1212010008), and Guangdong Basic and Applied Basic Research Foundation (Grant No. 2023B1515040023).


## Appendix A Comparison of trainings with merged weight and separated weight matrices

In this section, we discuss the difference in training between the merged weight matrix 𝐖 \mathbf{W} used in the main text and the separated weight matrix 𝐖 Q \mathbf{W}_{\rm Q} and 𝐖 K \mathbf{W}_{\rm K} in the linear attention model. To be more precise, we consider the linear attention with the merged weight as

and the linear attention with the separated weight as

The generalization error of the two schemes shows the expected double descent phenomenon, in the ridgeless limit λ → 0 \lambda\to 0 , as shown in Fig. S1 (b). In the data-poor case, i.e., the data density α ≡ P / D 2 < 1 \alpha\equiv P/D^{2}<1 , the scheme with separated weights ultimately exhibits lower generalization errors, while the dynamics of the training process are similar for both schemes [see Fig. S1 (a)]. In the data-rich case, the performances of the two schemes are highly similar, except that the scheme with separated weights converges a bit faster on the test tasks [see Fig. S1 (c)]. Note also that we fix D = 20 D=20 and thus this is not an asymptotic limit, being the same setting we focus on in the main text.

For the trained weight matrices, we find that in the data-poor case, neither scheme captures the correct weight structure [see Fig. S1 (d)]; while in the data-rich case, the two training schemes lead to a similar diagonal structure, which is the optimal solution of the problem [see Fig. S1 (e)]. This justifies the use of the scheme of the merged matrix in the main text.


## Appendix B Statistical properties of the interactions and external fields

In this section, we provide detailed statistical analyses of the interaction matrix 𝐉 \mathbf{J} and the external field 𝐡 \mathbf{h} and also test the robustness of our spin-glass mapping against the non-i.i.d. data setting.


## B.1 Explicit formulation of the model parameters

We present here the explicit formulation of the elements in each block in Fig. 1 (c) in the main text. The input matrix 𝐗 \mathbf{X} can be written into a 2 × 2 2\times 2 block matrix:

where 𝐗 0 = [ 𝒙 1 , 𝒙 2 , ⋯ , 𝒙 N ] ∈ ℝ D × N \mathbf{X}_{0}=[\bm{x}_{1},\bm{x}_{2},\cdots,\bm{x}_{N}]\in\mathbb{R}^{D\times N} denotes the data used for the prompts, 𝒚 0 = 𝐗 0 ⊤ ​ 𝒘 / D \bm{y}_{0}=\mathbf{X}_{0}^{\top}\bm{w}/\sqrt{D} is the corresponding label vector, and 𝒙 ~ \bm{\tilde{x}} is the testing prompt whose label needs to be predicted by the transformer. Thus, we can calculate

Recalling the definition of 𝐒 m ​ n μ = N − 1 ​ ∑ i 𝐗 D + 1 , i μ ​ 𝐗 m , i μ ​ 𝐗 n , N + 1 μ \mathbf{S}^{\mu}_{mn}=N^{-1}\sum_{i}\mathbf{X}_{D+1,i}^{\mu}\mathbf{X}_{m,i}^{\mu}\mathbf{X}_{n,N+1}^{\mu} , we can rewrite the 𝐒 \mathbf{S} matrix as

where ⊗ \otimes denotes an outer product of two vectors. Since h i = 1 P ​ ∑ μ y ~ μ ​ s i μ h_{i}=\frac{1}{P}\sum_{\mu}\tilde{y}^{\mu}s_{i}^{\mu} , where s i μ s_{i}^{\mu} is a vectorization of 𝐒 μ \mathbf{S}^{\mu} , we can write expressions for the elements in blocks 𝒜 \mathcal{A} and ℬ \mathcal{B} , which we denote as A A and B B respectively:

All the variables w , x , x ~ w,x,\tilde{x} used above are i.i.d. standard Gaussian random variables. We denote the distribution of elements { A i ​ j } \{A_{ij}\} in block 𝒜 \mathcal{A} as P ⁡ ( A ) P(A) , and those in block ℬ \mathcal{B} as P ⁡ ( B ) P(B) , which are both complex combinations of the sum and product of two i.i.d. Gaussian random variables. It is computationally challenging to conclude an analytic form for the distribution of random variables specified in Eq ( S6 ). In this way, we can also write the elements in other blocks as: C = A 1 ​ A 2 C=A_{1}A_{2} , D = A 1 ​ B 1 D=A_{1}B_{1} and E = B 1 ​ B 2 E=B_{1}B_{2} , where A 1 , A 2 ∼ P ⁡ ( A ) A_{1},A_{2}\sim P(A) , B 1 , B 2 ∼ P ⁡ ( B ) B_{1},B_{2}\sim P(B) .

A surprising observation is that the distributions of blocks 𝒜 \mathcal{A} , 𝒞 \mathcal{C} and 𝒟 \mathcal{D} seem sensitive to the change of the prompt length N N (see Fig. S2 , but a weaker effect for ℬ \mathcal{B} and ℰ \mathcal{E} ). However, once P P is sufficiently large, the correct weight solution will be learned, and thus the transformer achieves a nearly perfect in-context inference, which captures the essence of ICL explained in the main text. This demonstrates that even if the parameters of the Hamiltonian vary, the ground state remains the same for the ICL.


## B.2 Running AMP given a fitted distribution of model parameters

Although an analytic form of the model parameters is unknown, we fit the experimental data by a Gaussian (or mixture) distribution (not accurate due to the tail, but the Cauchy distribution does not capture the bulk very well). Then we sample the couplings and fields from the fitted distribution and run the AMP equation to solve the spin model Eq. (5) in the main text. This is the standard setting of a spin glass problem as the model parameters are sampled from an analytic distribution. However, in the ICL, the model parameters are directly constructed from the supplied dataset, reflecting the intrinsic structural disorder in the training tasks. We address how different these two scenarios are.

The fitting distributions are shown by the red line in Fig. 1 (c) in the main text, in the case of P = 1 000 P=1\,000 , D = 10 D=10 , N = 100 N=100 . Then we resample randomly from the fitting distribution to generate 𝐉 \mathbf{J} and 𝒉 \bm{h} , as shown in Fig. S3 (a)(b). We then run the AMP equation on these parameters, and the results are shown in Fig. S3 (c)(d), which indicates that AMP still captures the diagonal structure of the optimal solution, although there are some numerical deviations in the diagonal elements. Even if we discard some information in the real distribution, we recover the basic feature of the spin glass model for ICL.


## B.3 Robustness of the spin model mapping to non-i.i.d. data

We test whether our spin model is still valid on a correlated data set. The columns in the data matrix 𝐗 0 \mathbf{X}_{0} are no longer i.i.d., but correlated, which models the intrinsic relationship between tokens in real language tasks. Specifically, the correlated data samples are constructed by the following rule [ 39 ] :

where μ \mu indicates different columns in the input 𝐗 \mathbf{X} , and i i indicates different rows. This correlation design means that elements in different rows are independent of each other for each column, and the covariance of elements in the same row is regulated by c c . Keeping the other settings unchanged, we plot the performances of SGD and AMP in Fig. S4 . Even though the generalization error is not simply monotonic with c c , the results of AMP are still able to match those of SGD. The distributions of couplings and fields for the spherical spin model mapping look similar to the i.i.d. scenario.


## Appendix C Derivation of cavity method and approximate message passing equation

The spin glass model of the transformer we consider in the main text reads

and the Boltzmann distribution of weight configuration can be written as

where Z Z serves as the partition function. Taking each interaction pair as a factor node and each site term as an external field in Eq. ( S9 ), one can write the following cavity iteration in an explicit form according to the standard format of the cavity method (e.g., see the textbook [ 31 ] ).

which is also called the belief propagation equation. The notation i ​ j ij denotes an interaction (or factor node in a factor graph representation of the model). Since our model only involves two-body interactions, which means that ∂ i ​ j \ i \partial ij\backslash i contains only one element j j , the product notation ∏ j ∈ ∂ i ​ j \ i \prod_{j\in\partial ij\backslash i} can be omitted, and we can simplify the notation i → i ​ j i\to ij by i → j i\to j and i ​ j → i ij\to i by j → i j\to i . Therefore, we can combine Eq. ( S10 ) and Eq. ( S11 ) together into

After the iteration reaches a fixed point, the marginal probability η i ​ ( σ i ) \eta_{i}(\sigma_{i}) of each spin can be calculated based on the converged cavity marginals as follows


## C.1 Relaxed belief propagation

The space complexity to run Eq. ( S12 ) is of 𝒪 ⁡ ( D 4 ) \mathcal{O}(D^{4}) , since i = 1 , ⋯ , ( D + 1 ) 2 i=1,\cdots,(D+1)^{2} . To reduce the space complexity, an intuitive approach is to approximate the cavity marginal by a Gaussian distribution 𝒩 ⁡ ( m i → j , v i → j ) \mathcal{N}(m_{i\to j},v_{i\to j}) , and then derive the iterative equations for the first two moments. To validate this intuition, we start from Eq. ( S12 ) and apply the Fourier transform and Taylor expansion.

To proceed, we first define ξ i → j = ∑ k ≠ i , j β ​ J i ​ k ​ σ k \xi_{i\to j}=\sum_{k\neq i,j}\beta J_{ik}\sigma_{k} , and G ⁡ ( ξ i → j ) = e σ i ​ ξ i → j G(\xi_{i\to j})=\mathrm{e}^{\sigma_{i}\xi_{i\to j}} , and then Eq. ( S12 ) can be written as

In Eq. ( S14b ), we insert the Fourier transform of G ⁡ ( ξ ) G(\xi) , i.e., G ^ ​ ( ξ ^ i → j ) \hat{G}(\hat{\xi}_{i\to j}) , and absorb irrelevant constants into z i → j z_{i\to j} . Let us calculate the last integral in Eq. ( S14c ):

In Eq. ( S15b ), we use the Taylor expansion of an exponential function, and in Eq. ( S15c ), we define the mean m k → i m_{k\to i} and the variance v k → i v_{k\to i} of the message (the cavity marginal probability) as

In Eq. ( S15e ), we use the fact that the high order power of J i ​ j J_{ij} are negligible and thus recover the exponential form. Then, we substitute Eq. ( S15 ) back to Eq. ( S14 ) and obtain

Then, we re-express G ^ ​ ( ξ ^ i → j ) \hat{G}(\hat{\xi}_{i\to j}) by G ⁡ ( ξ ) G(\xi) and obtain

We can then define the mean and variance of ξ i → j \xi_{i\to j} as

Then, the marginal probability η i → j ​ ( σ i ) \eta_{i\to j}(\sigma_{i}) can be further calculated as

Equation ( S22d ) implies that η i → j ​ ( σ i ) \eta_{i\to j}(\sigma_{i}) follows a Gaussian distribution with the following mean and variance

Now, we have obtained the so-called relaxed belief propagation (r-BP) equation:

Compared to the original belief propagation equation, the r-BP equations do not require a numerical integration, thereby improving the computational efficiency. Moreover, it provides a basis for deriving the AMP equation shown in the main text. After the relaxed belief propagation equation converges, we get further the marginal probability as

As we expected, Eq. ( S26c ) suggests that η i ​ ( σ i ) \eta_{i}(\sigma_{i}) indeed follows a Gaussian distribution 𝒩 ⁡ ( m i , v i ) \mathcal{N}(m_{i},v_{i}) , with the following mean and variance

where m j → i m_{j\to i} and v j → i v_{j\to i} are the fixed points of the r-BP iterative equations [Eq. ( S25 )]. To conclude, the intuition of Gaussian approximation is theoretically justified.


## C.2 Approximate message passing equation

If we can remove the directed arrows (e.g., i → j i\to j ) in the r-BP, the space complexity of the algorithm can be greatly reduced, reducing from 𝒪 ⁡ ( D 4 ) \mathcal{O}(D^{4}) to 𝒪 ⁡ ( D 2 ) \mathcal{O}(D^{2}) . We next show how this can be possible. By using the following identities M i = M i → j + β ​ J i ​ j ​ m j → i M_{i}=M_{i\to j}+\beta J_{ij}m_{j\to i} and V i = V i → j + β 2 ​ J i ​ j 2 ​ v j → i V_{i}=V_{i\to j}+\beta^{2}J_{ij}^{2}v_{j\to i} , we further find that

and

In the large D D limit (or even only D D is not too small), we can further simplify the relaxed belief propagation equation to the AMP equation

In this case, we only need to iterate the above two equations of ( m i , v i ) (m_{i},v_{i}) to obtain the fixed points. This AMP equation saves ( D + 1 ) 2 (D+1)^{2} -fold space complexity for running the algorithm if we record ( D + 1 ) 2 (D+1)^{2} as the number of spins in the system. In different forms, the AMP equation was first discovered in a statistical mechanics analysis of signal transmission problem [ 40 ] , and is also rooted in the Thouless–Anderson–Palmer equation in glass physics [ 33 , 31 , 32 ] .


## Appendix D Derivation of the unique optimal solution to the linear attention transformer

In this section, we provide a detailed derivation of the unique optimal solution to the linear attention transformer (i.e., Eq. (10) and Eq. (11) in the main text). The input matrix 𝐗 \mathbf{X} and the weight matrix 𝐖 \mathbf{W} can be represented as 2 × 2 2\times 2 block matrices

where 𝐗 0 = [ 𝒙 1 , 𝒙 2 , ⋯ , 𝒙 N ] ∈ ℝ D × N \mathbf{X}_{0}=[\bm{x}_{1},\bm{x}_{2},\cdots,\bm{x}_{N}]\in\mathbb{R}^{D\times N} denotes the data used for the prompts, 𝒚 0 = 𝐗 0 ⊤ ​ 𝒘 / D \bm{y}_{0}=\mathbf{X}_{0}^{\top}\bm{w}/\sqrt{D} is the corresponding label vector, and 𝒙 ~ \bm{\tilde{x}} is the testing prompt whose label needs to be predicted by the transformer. The blocks of the weight matrix 𝐖 \mathbf{W} have the same size as the corresponding blocks of 𝐗 \mathbf{X} , with 𝐖 11 ∈ ℝ D × D \mathbf{W}_{11}\in\mathbb{R}^{D\times D} , 𝐖 12 ∈ ℝ D × 1 \mathbf{W}_{12}\in\mathbb{R}^{D\times 1} , 𝐖 21 ∈ ℝ 1 × D \mathbf{W}_{21}\in\mathbb{R}^{1\times D} , and 𝐖 22 ∈ ℝ \mathbf{W}_{22}\in\mathbb{R} . Thus, we can calculate

and

Considering the prediction of the transformer y ^ = 𝐘 D + 1 , N + 1 = 1 N ​ ( 𝐗𝐗 ⊤ ​ 𝐖𝐗 ) D + 1 , N + 1 \hat{y}=\mathbf{Y}_{D+1,N+1}=\frac{1}{N}(\mathbf{XX^{\top}WX})_{D+1,N+1} , using 2 × 2 2\times 2 block matrix multiplication, one obtains the following result:

where 𝒘 ⋆ \bm{w}_{\star} is the task vector, the definition 𝒚 0 = 𝐗 0 ⊤ ​ 𝒘 ⋆ / D \bm{y}_{0}=\mathbf{X}_{0}^{\top}\bm{w}_{\star}/\sqrt{D} is used to obtain Eq. ( S34c ), and the new definition 𝐂 0 ≡ 1 N ​ 𝐗 0 ​ 𝐗 0 ⊤ \mathbf{C}_{0}\equiv\frac{1}{N}\mathbf{X}_{0}\mathbf{X}_{0}^{\top} is used in Eq. ( S34e ). Comparing the actual prediction with the true label 𝒚 ~ = 𝒘 ⋆ ⊤ ​ 𝒙 ~ / D \tilde{\bm{y}}=\bm{w}_{\star}^{\top}\bm{\tilde{x}}/\sqrt{D} corresponding to 𝒙 ~ \bm{\tilde{x}} , one finds that the optimal solution for the weight matrix must satisfy the following condition:

In the asymptotic limit, i.e., N ∝ D N\propto D , C 0 C_{0} is a Wishart random matrix. However, in the non-asymptotic case we consider, D D is kept finite while N N can be independently large, we get an identity matrix of 𝐂 0 \mathbf{C}_{0} , which can be proved by using the central limit theorem. Therefore, Eq. ( S35 ) can be simplified as

Equation ( S36 ) is actually a set of linear equations, which can be written in the form of 𝐀 ​ 𝒙 = 𝒃 \mathbf{A}\bm{x}=\bm{b} where { x i } \{x_{i}\} indicates the weight components to be determined. The number of variables in the equations is D 2 + D D^{2}+D . Given an input matrix 𝐗 \mathbf{X} generated by a specific 𝒘 \bm{w} , we can write down D 2 D^{2} equations to solve for the optimal weight. Therefore, the mathematics of linear equations tells us that when the number of input matrices P = 1 P=1 , the weight matrix 𝐖 \mathbf{W} has infinitely many solutions. However, as long as P > 1 P>1 , the set of equations has a unique solution, which can be readily deduced as 𝐖 11 ⋆ = 𝟙 D \mathbf{W}_{11}^{\star}=\mathds{1}_{D} and 𝐖 21 ⋆ = 𝟎 \mathbf{W}_{21}^{\star}=\bm{0} . In practice, the transformer or our spin glass model needs a larger value of P P to identify this optimal matrix.


## Appendix E Convexity and Hessian matrix of the linear attention model

In this section, we discuss the convexity of our model used in the main text by analyzing the spectral density of the Hessian matrix.

After the spin mapping y ^ μ = ∑ i σ i ​ s i μ \hat{y}^{\mu}=\sum_{i}\sigma_{i}s_{i}^{\mu} , the loss function is written as ℒ = ( 2 ​ P ) − 1 ​ ∑ μ = 1 P ( y μ − y ^ μ ) 2 \mathcal{L}=(2P)^{-1}\sum_{\mu=1}^{P}(y^{\mu}-\hat{y}^{\mu})^{2} , where s i μ s_{i}^{\mu} is a vectorization of the matrix 𝐒 μ \mathbf{S}^{\mu} . The Hessian matrix can be calculated as [ 41 ]

where 𝕊 ∈ ℝ P × ( D + 1 ) 2 \mathbb{S}\in\mathbb{R}^{P\times(D+1)^{2}} . It can be thus proved that 𝐇 \mathbf{H} is a positive semidefinite matrix. The spectral density of the Hessian matrix is shown in Fig. S5 . The eigenvalues are all non-negative, which indicates that the Hessian matrix is positive semidefinite. This means that the loss function is (but not strictly) convex, and we find that the task diversity affects the number of zero modes in the energy landscape (Fig. S5 ). The large number of zero eigenvalues implies that the energy landscape of the model is marginally stable in many local regions, resulting in a high-dimensional landscape of many minima [see Fig. 3 (a) for the case of P = 10 P=10 ], which reflects the algorithmic hardness when P P is small. Interestingly, this feature is also observed in Boltzmann machine learning [ 35 ] .


## Appendix F Generalization to more complex attention structures

In this section, we verify whether our spin glass model is robust to more complex attention structures in transformers, by carrying out extensive experimental simulations. The linear attention setting used in the main text is called simplified linear attention (SLA) in this section. The explicit formulation is given below.

where 𝐖 ≡ 𝐖 Q ⊤ ​ 𝐖 K \mathbf{W}\equiv\mathbf{W}_{\rm Q}^{\top}\mathbf{W}_{\rm K} . This SLA will be compared with the case of removing the softmax function yet keeping the value matrix trainable, which we call the full linear attention (FLA) as follows.

The single-head full softmax attention (SA) defined below is also compared.

where 𝐖 Q , 𝐖 K ∈ ℝ H × ( D + 1 ) \mathbf{W}_{Q},\mathbf{W}_{K}\in\mathbb{R}^{H\times(D+1)} and 𝐖 V ∈ ℝ ( D + 1 ) × ( D + 1 ) \mathbf{W}_{V}\in\mathbb{R}^{(D+1)\times(D+1)} , and H H is the internal size of the attention operation and can be equal to the embedding dimension. We also consider a small full transformer encoder, with a feed-forward layer, residual connection, and linear readout head, defined as

with

where SA ⁡ ( 𝐗 ) \mathrm{SA}(\mathbf{X}) is the standard self-attention layer as Eq. ( S40 ), and 𝐖 1 , 𝐖 2 \mathbf{W}_{1},\mathbf{W}_{2} and b 1 , b 2 b_{1},b_{2} are weights and biases of the two feed-forward layers, respectively. The weight matrices in SA ⁡ ( 𝐗 ) \mathrm{SA}(\mathbf{X}) are 𝐖 Q , 𝐖 K ∈ ℝ H × ( D + 1 ) \mathbf{W}_{Q},\mathbf{W}_{K}\in\mathbb{R}^{H\times(D+1)} and 𝐖 V ∈ ℝ ( D + 1 ) × ( D + 1 ) \mathbf{W}_{V}\in\mathbb{R}^{(D+1)\times(D+1)} , respectively, and H H is the internal size of the attention operation. We call this complex layered transformer structure TF.

In addition, the transformer usually employs the multi-head attention structure. Therefore, for comparison, we further consider a multi-head linear attention model (MHLA), where the multiple outputs of Eq. ( S39 ) (one output corresponds to one head) are concatenated and then linearly read through a learnable readout matrix 𝐖 O \mathbf{W}_{O} . The formulation is given by 𝐘 MHLA = ∑ h = 1 M 𝐖 O h ​ 𝐘 FLA h \mathbf{Y}_{\rm MHLA}=\sum_{h=1}^{M}\mathbf{W}_{O}^{h}\mathbf{Y}_{{\rm FLA}}^{h} . We denote the number of attention heads, i.e., the dimension of the linear readout, as M M .

The experimental results of the above different models are shown in Fig. S6 . Figure S6 shows the robustness of our theory against different transformer settings, although SA and TF display a higher test error. This can be understood as the linear attention structure is more suitable for the linear regression task compared to the non-linear softmax attention. For the softmax attention and more advanced structures, it is hard to derive such concise results as in Sec D , and the spherical spin glass model specified in the main text. However, the ground state interpretation of the learning is not a specific picture, and the underlying mechanism for the ICL in the simple but non-trivial setting we consider can be analytically clarified, thereby offering a promising avenue for thinking about how to model many intriguing but puzzling properties of large language models.

We leave the exploration of more complex tasks beyond linear regression and more complex transformers such repeated transformer blocks together with multi-headed structures to future works. The current experiments are sufficient to justify our theory of spin-glass mapping.


## References