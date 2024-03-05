# Add import files
import pickle



# -----------------------------------------------------------
def question1():
    answers = {}

    # type: bool (True/False)
    answers["(a)"] = True

    # type: explanatory string (at least four words)
    answers["(a) explain"] = "As in hierarchical clustering , outliers or small groups of outliers tend to form singleton or small clusters that do not merge with any other clusters until much later in the merging process.By discarding singleton or small clusters that are not merging with other clusters, outliers can be removed easily but this is not same with k-means as it assigns each outlier to some clusters thus we can remove the centroid of the cluster."

    # type: bool (True/False)
    answers["(b)"] = True

    # type: explanatory string (at least four words)
    answers["(b) explain"] = "There is no random element in the algorithms for agglomerative hierarchical techniques unless there are ties in proximity values."

    # type: bool (True/False)
    answers["(c)"] = True

    # type: explanatory string (at least four words)
    answers["(c) explain"] = "For large datasets it may take  more time also other than k-means DBSCAN is more efficient"

    # type: bool (True/False)
    answers["(d)"] = False

    # type: explanatory string (at least four words)
    answers["(d) explain"] = "SSE of the clustering increases as splitting creates an additional variance."

    # type: bool (True/False)
    answers["(e)"] = True

    # type: explanatory string (at least four words)
    answers["(e) explain"] = "For K-means SSE is an inverse measure of cohesion of clusters and thus as SSE decreases,cohesion increases and vice-versa."

    # type: bool (True/False)
    answers["(f)"] = True

    # type: explanatory string (at least four words)
    answers["(f) explain"] = "For k-means SSB is a direct measure of the seperation of clusters and thus as SSB increases ,seperation also increases and vice-versa."

    # type: bool (True/False)
    answers["(g)"] = True

    # type: explanatory string (at least four words)
    answers["(g) explain"] = "Cohesion and separation are two distinct concepts in clustering. Improving cohesion (decreasing SSE) within clusters doesn't necessarily mean improving separation (increasing SSB) between clusters."

    # type: bool (True/False)
    answers["(h)"] = True

    # type: explanatory string (at least four words)
    answers["(h) explain"] = "SSE + SSB (between sum of squares) is  constant."

    # type: bool (True/False)
    answers["(i)"] = False

    # type: explanatory string (at least four words)
    answers["(i) explain"] = "Cohesion and separation are independent measures in clustering. Increasing cohesion (decreasing SSE) within clusters doesn't necessarily imply an increase in separation (SSB) between clusters"

    return answers




# -----------------------------------------------------------
def question2():
    answers = {}

    # type: bool (True/False)
    answers["(a)"] = True

    # type: explanatory string (at least four words)
    answers["(a) explain"] = "each circle has one centroid at its center once it completes the k-eans algorithm"

    # type: bool (True/False)
    answers["(b)"] = False

    # type: explanatory string (at least four words)
    answers["(b) explain"] = "2 clusters have points from the both shaded regions"

    # type: bool (True/False)
    answers["(c)"] = True

    # type: explanatory string (at least four words)
    answers["(c) explain"] = "contains an empty cluster"


    return answers




# -----------------------------------------------------------
def question3():
    answers = {}

    # type: a string that evaluates to a float
    answers["(a) SSE"] = "4*R**2"

    # type: a string that evaluates to a float
    answers["(b) SSE"] = "4*squart(a**2 + b**2 + c**2)"

    # type: a string that evaluates to a float
    answers["(c) SSE"] = "10* R **2"

    return answers




# -----------------------------------------------------------
def question4():
    answers = {}

    # type: int
    answers["(a) Circle (a)"] = 1

    # type: int
    answers["(a) Circle (b)"] = 1

    # type: int
    answers["(a) Circle (c)"] = 1

    # type: explanatory string (at least four words)
    answers["(a) explain"] = "As the distance from A to B and B to C  is same despite the data  K-means clustering converge to 1 centroid per circle"

    # type: int
    answers["(b) Circle (a)"] = 1

    # type: int
    answers["(b) Circle (b)"] = 1

    # type: int
    answers["(b) Circle (c)"] = 1

    # type: explanatory string (at least four words)
    answers["(b) explain"] = "Since no centroids are initially placed within circle C, it's probable that one centroid will eventually move towards circle C, capturing the data points within it and forming a cluster."

    # type: int
    answers["(c) Circle (a)"] = 0

    # type: int
    answers["(c) Circle (b)"] = 0

    # type: int
    answers["(c) Circle (c)"] = 2

    # type: explanatory string (at least four words)
    answers["(c) explain"] = "For this optimal clustering, The disctribution of every centroid is closest to its initial cluster it started with."

    return answers




# -----------------------------------------------------------
def question5():
    answers = {}

    # type: set
    answers["(a)"] = {"Group A", "Group B"}

    # type: explanatory string (at least four words)
    answers["(a) explain"] = "Groups A and B will be merged since they have the smallest single link distance(between the last point of a and 1st point of b)as compared to groups A,C and Groups B and C"

    # type: set
    answers["(b)"] = {"Group A", "Group C"}

    # type: explanatory string (at least four words)
    answers["(b) explain"] = "Since group A and c has smallest complete distance as compared to complete link distance of groups A,B and B,C"

    return answers




# -----------------------------------------------------------
def question6():
    answers = {}

    # type: set
    answers["(a) core"] = {'E', 'B', 'F', 'G', 'C', 'L', 'M', 'I'}

    # type: set
    answers["(a) boundary"] = {'D', 'G'}

    # type: set
    answers["(a) noise"] = {'A', 'H'}

    # type: set
    answers["(b) cluster 1"] = {'B', 'C', 'E', 'F', 'G', 'D'}

    # type: set
    answers["(b) cluster 2"] = {'I', 'J', 'L', 'M'}

    # type: set
    answers["(b) cluster 3"] = set()

    # type: set
    answers["(b) cluster 4"] = set()

    # type: set
    answers["(c)-a core"] = {'B', 'C', 'D', 'E', 'F', 'G', 'I', 'J', 'L', 'M'}

    # type: set
    answers["(c)-a boundary"] = {'A', 'H'}

    # type: set
    answers["(c)-a noise"] = set()

    # type: set
    answers["(c)-b cluster 1"] = {'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'L', 'M'}

    # type: set
    answers["(c)-b cluster 2"] = {'A'}

    # type: set
    answers["(c)-b cluster 3"] = set()

    # type: set
    answers["(c)-b cluster 4"] = set()

    return answers




# -----------------------------------------------------------
def question7():
    answers = {}

    # type: string
    answers["(a)"] = "cluster 4"

    # type: explanatory string (at least four words)
    answers["(a) explain"] = "The overall entropy for cluster 4 is high and has the highest uncertainty or variability in its distribution of objects across different categories."

    # type: string
    answers["(b)"] = "cluster 1"

    # type: explanatory string (at least four words)
    answers["(b) explain"] = "The overall entropy for cluster 1 is low and has the lowest uncertainty or variability."

    return answers




# -----------------------------------------------------------
def question8():
    answers = {}

    # type: string
    answers["(a) Matrix 1"] = "Dataset-z"

    # type: explanatory string (at least four words)
    answers["(a) explain diag entries, Matrix 1"] = "The blue indicates low distances, which suggests well-separated clusters."

    # type: explanatory string (at least four words)
    answers["(a) explain non-diag entries, Matrix 1"] = "Different patterns of colors suggest the another set of cluster distributions."

    # type: string
    answers["(a) Matrix 2"] = "Dataset-x"

    # type: explanatory string (at least four words)
    answers["(a) explain diag entries, Matrix 2"] = "The blue indicates low distances, suggesting well-separated clusters."

    # type: explanatory string (at least four words)
    answers["(a) explain non-diag entries, Matrix 2"] = "All other colours indicates high distances, implying clear boundaries between clusters."

    # type: string
    answers["(a) Matrix 3"] = "Dataset-y"

    # type: explanatory string (at least four words)
    answers["(a) explain diag entries, Matrix 3"] = "Diagonal entry corresponds to the distance of a point from itself."

    # type: explanatory string (at least four words)
    answers["(a) explain non-diag entries, Matrix 3"] = "Some of the green and yellow regions indicates  overlapping or less distinct clusters."

    # type: string
    answers["(b) Row 1"] = "A"

    # type: string
    answers["(b) Row 2"] = "B"

    # type: string
    answers["(b) Row 3"] = "C"

    # type: string
    answers["(b) Row 4"] = "D"

    # type: explanatory string (at least four words)
    answers["(b) Row 1 explain"] = ""

    # type: explanatory string (at least four words)
    answers["(b) Row 2 explain"] = ""

    # type: explanatory string (at least four words)
    answers["(b) Row 3 explain"] = ""

    # type: explanatory string (at least four words)
    answers["(b) Row 4 explain"] = ""

    return answers




# -----------------------------------------------------------
def question9():
    answers = {}

    # type: list
    answers["(a)"] = ['hierarchical', 'overlapping','complete']

    # type: list
    answers["(b)"] = ['partitional', 'exclusive', 'complete']

    # type: list
    answers["(c)"] = ['partitional', 'fuzzy', 'complete']

    # type: list
    answers["(d)"] = ['hierarchical','overlapping', 'partial']

    # type: list
    answers["(e)"] = ['partitional', 'exclusive', 'complete']

    # type: explanatory string (at least four words)
    answers["(e) explain"] = ""

    return answers




# -----------------------------------------------------------
def question10():
    answers = {}

    # type: string
    answers["(a) Figure (a)"] = "No"

    # type: string
    answers["(a) Figure (b)"] = "Yes"

    # type: explanatory string (at least four words)
    answers["(a) explain"] = "In FIG B,the approach is effective in finding facial representation by accessing the spatial density of datapoints"

    # type: string
    answers["(b) Figure (a)"] = "No"

    # type: string
    answers["(b) Figure (b)"] = "Yes"

    # type: explanatory string (at least four words)
    answers["(b) explain"] = "it is a technique that groups together comparable data points to identify patterns within a dataset. Regarding face characteristics l, k-means can be utilized to find patterns within them depending on dimensions, positions, and shapes."

    # type: string
    answers["(c)"] = "DBSCAN"

    return answers

# --------------------------------------------------------
if __name__ == '__main__':
    answers_dict = {}
    answers_dict['question1'] = question1()
    answers_dict['question2'] = question2()
    answers_dict['question3'] = question3()
    answers_dict['question4'] = question4()
    answers_dict['question5'] = question5()
    answers_dict['question6'] = question6()
    answers_dict['question7'] = question7()
    answers_dict['question8'] = question8()
    answers_dict['question9'] = question9()
    answers_dict['question10'] = question10()
    print('end code')

    with open('answers.pkl', 'wb') as f:
        pickle.dump(answers_dict, f)
