import numpy as np
import matplotlib.pyplot as plt


def plot_decision_boundary(clf, X):
    w = clf.coef_.ravel()
    a = -w[0] / w[1]
    xx = np.linspace(np.min(X[:, 0]), np.max(X[:, 0]))
    yy = a * xx - clf.intercept_ / w[1]
    plt.plot(xx, yy)
    plt.xticks(())
    plt.yticks(())

def plotEllipse(pos,P,edge='k',face='none',line_width='.1'):
    from numpy.linalg import svd
    from matplotlib.patches import Ellipse
    import math
    from numpy import pi
    from matplotlib.pyplot import gca
    U, s , Vh = svd(P)
    orient = math.atan2(U[1,0],U[0,0])*180/pi
    ellipsePlot = Ellipse(xy=pos, width=2.0*math.sqrt(s[0]), height=2.0*math.sqrt(s[1]), angle=orient,facecolor=face, edgecolor=edge, lw=line_width)
    ax = gca()
    ax.add_patch(ellipsePlot);
    return ellipsePlot
