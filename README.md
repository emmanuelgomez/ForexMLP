# ForexMLP
Multilayer Perceptron Neuronal Network for Forex Market

Draft:
Development of a neural network that allows to predict the behavior of prices in the FOREX stock market.
Proposal:
-Frame the project and research in three fundamental stages.
-The first stage: will be aimed at developing a software system with the aim of finding the architecture of the neural network that evidences the best results in our problematic situation, that is, predict the behavior of the price of the next session. Training will also begin to find the correct topology.
-From an analysis and synthesizing the information consulted in different bibliographies that address the subject in question, the system will be developed on the following basis:
Unidirectional multilayer perceptron network.
The neuron model uses a sigmoid activation function.
System functions
Unidirectional multilayer perceptron network.
The neuron model of the network uses sigmoid activation function.
1. Iterate over different topologies (travel over a wide range of topologies).
• Number of layers.
• Number of neurons (by layers).
• Designate starting training set.
• Pattern size. Initially (1000 * 4 elements) -> 4000 input neurons, 1 output neuron.
• Iterate by varying the size of the training pattern, directly related to this varies the number of training patterns together.
• Selection of training and validation data set (70% -30%).
• Number of patterns (training sample / standard size).
• Define number of training times. (A greater number of times better results, but taking into account that it implies an increase in training time).
• Define the cost function and the optimization method (which provides the rule for updating the weights).
(Initially, the mean square error and the descent method will be used for the gradient, depending on the results obtained, assess the possibility of using other methods).
•	To train.
• In order to obtain better results, the order in the presentation of the patterns in each period will be random (since if the same order were always followed the training would be flawed in favor of the last pattern of the training set, whose updating , being the last, it would always predominate over the previous ones).
• Register Training error.
• Register Effectiveness.
• Record synaptic weights obtained.
(In each iteration record the error and the effectiveness of the training to finally stay with the average since we will use cross validation technique to analyze results).
Note: I think that the set of synaptic weights obtained is not of great importance to store them in this stage since it is not a relevant information to select the topology.
• Validate
• Validate training with the data selected for this purpose, and compare it with the results of the training (error and effectiveness), thus obtaining the capacity for generalization of the network. (A good generalization is more interesting than a very small error in training).
• Use cross validation technique to evaluate the results:
o Repeat the process of cross-validation during K-iterations. Finally, the arithmetic mean of the results of each iteration is obtained to obtain a single result (Results: average of the error, average of the effectiveness). (If it were of interest to store the weights, I think it would be best to keep those of the iteration that obtained better results)
• Register validation effectiveness.
o (Note: Compare error and effectiveness of training with error and effectiveness of validation, obtaining% of acceptance of the error and% of acceptance of effectiveness of the validation with respect to the training registering these values).
2. Graph stored data of each training carried out so far in order to analyze the results obtained.
-The second stage will consist in the continuation of the trainings. It is only considered if the expected results have not yet been found.
-If after a considerable period of time has elapsed and after consulting the results obtained, values close to those desired are not appreciated (that is, 85% of the time in the predicted output), we will consider the implementation of a new network model, proposal:
• Hybrid multilayer model, which would be composed of an unsupervised layer (of the Kohonen self-organized map type) and a supervised one, which would help us to gain speed in case the learning of the multilayer perceptron is too slow.
• Consider the application of a fuzzy or diffuse system using the closest neighbor grouping as the learning algorithm. Another variant may be to use the learning algorithm back-propagation (retro propagation) obtaining

