# perceptron.py
# -------------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


# Perceptron implementation
import util
import operator
PRINT = True

class PerceptronClassifier:
    """
    Perceptron classifier.

    Note that the variable 'datum' in this code refers to a counter of features
    (not to a raw samples.Datum).
    """
    def __init__( self, legalLabels, max_iterations):
        self.legalLabels = legalLabels
        self.type = "perceptron"
        self.max_iterations = max_iterations
        self.weights = {}
        for label in legalLabels:
            self.weights[label] = util.Counter() # this is the data-structure you should use

    def setWeights(self, weights):
        assert len(weights) == len(self.legalLabels);
        self.weights = weights;

    def train( self, trainingData, trainingLabels, validationData, validationLabels ):
        """
        The training loop for the perceptron passes through the training data several
        times and updates the weight vector for each label based on classification errors.
        See the project description for details.

        Use the provided self.weights[label] data structure so that
        the classify method works correctly. Also, recall that a
        datum is a counter from features to values for those features
        (and thus represents a vector a values).
        """

        self.features = trainingData[0].keys() # could be useful later
        # DO NOT ZERO OUT YOUR WEIGHTS BEFORE STARTING TRAINING, OR
        # THE AUTOGRADER WILL LIKELY DEDUCT POINTS.
        print self.weights
        print self.legalLabels
        #print "features ", self.features
        #print "trainingData0: ",trainingData[0]
        for iteration in range(self.max_iterations):
            print "Starting iteration ", iteration, "..."
            for i in range(len(trainingData)):
                instance = util.Counter()
                for label in self.legalLabels:
                    #print "What is each? : ", each
                    instance[label]=self.weights[label]*trainingData[i]
                    #print "trainingdata[i]: ",trainingData[i]
                    #print " instance[label] ", instance[label]
                estimate = instance.argMax()
                if(estimate == trainingLabels[i]):
                    continue
                self.weights[trainingLabels[i]]=self.weights[trainingLabels[i]]+trainingData[i]
                self.weights[estimate] = self.weights[estimate] - trainingData[i]

    def classify(self, data ):
        """
        Classifies each datum as the label that most closely matches the prototype vector
        for that label.  See the project description for details.

        Recall that a datum is a util.counter...
        """
        guesses = []
        for datum in data:
            vectors = util.Counter()
            for l in self.legalLabels:
                vectors[l] = self.weights[l] * datum
            guesses.append(vectors.argMax())
        return guesses


    def findHighWeightFeatures(self, label):
        """
        Returns a list of the 100 features with the greatest weight for some label
        """
        featuresWeights = []
        #print "Weights at start: ", self.weights

        #get the counter that holds the weights for the label given
        weights_for_label = self.weights[label]
        #print "Weight for label: ", weights_for_label

        #use the sortedKeys method to get a list of the keys sorted high to low then
        #take the first 100 values
        featuresWeights = weights_for_label.sortedKeys()
        featuresWeights = featuresWeights[:100]





        "*** YOUR CODE HERE ***"
        #util.raiseNotDefined()

        return featuresWeights


