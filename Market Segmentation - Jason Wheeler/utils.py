# import libraries
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from sklearn.metrics import silhouette_score, silhouette_samples
from time import time 
from sklearn import metrics 
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import QuantileTransformer 
from sklearn.cluster import KMeans

kmeans = KMeans()

def visualize_data(x,y,cats,lbl):
  fig, ax = plt.subplots(figsize=(8, 6))
  colors = cm.rainbow(np.linspace(0, 1, len(cats)))
  
  for cat, co in zip(cats, colors):
      loc=np.where(y==cat)
      ax.scatter(x[loc,0], x[loc,1], color=co,label=cat)
  ax.set_xlabel('Component 1')
  ax.set_ylabel('Component 2')
  ax.set_title(lbl)
  ax.legend()
  ax.grid(False)

  plt.show()


def silscore_pipe(X_scaled, num_clusters):
	range_n_clusters = list(range(2, num_clusters))

	for n_clusters in range_n_clusters: 
	    # Create a subplot with 1 row and 2 columns 
	    fig, (ax1, ax2) = plt.subplots(1, 2)
	    fig.set_size_inches(18, 7)

	    # The 1st subplot is the silhouette plot
	    # The silhouette coefficient can range from -1, 1
	    ax1.set_xlim([-1, 1])
	    # The (n_clusters+1)*10 is for inserting blank space between silhouette
	    # plots of individual clusters, to demarcate them clearly.
	    ax1.set_ylim([0, len(X_scaled) + (n_clusters + 1) * 10])
	    
	    # Initialize the clusterer with n_clusters value and a random generator
	    # seed of 10 for reproducibility.
	    clusterer = KMeans(n_clusters=n_clusters, random_state=42)
	    cluster_labels = clusterer.fit_predict(X_scaled)
	    
	    # The silhouette_score gives the average value for all the samples.
	    # This gives a perspective into the density and separation of the formed
	    # clusters
	    silhouette_avg = silhouette_score(X_scaled, cluster_labels)
	    print("For n_clusters =", n_clusters,
	          "The average silhouette_score is :", silhouette_avg)

	    # Compute the silhouette scores for each sample
	    sample_silhouette_values = silhouette_samples(X_scaled, cluster_labels)
	    
	    y_lower = 10
	    for i in range(n_clusters):
	        # Aggregate the silhouette scores for samples belonging to
	        # cluster i, and sort them
	        ith_cluster_silhouette_values = \
	            sample_silhouette_values[cluster_labels == i]

	        ith_cluster_silhouette_values.sort()

	        size_cluster_i = ith_cluster_silhouette_values.shape[0]
	        y_upper = y_lower + size_cluster_i

	        color = cm.nipy_spectral(float(i) / n_clusters)
	        ax1.fill_betweenx(np.arange(y_lower, y_upper),
	                          0, ith_cluster_silhouette_values,
	                          facecolor=color, edgecolor=color, alpha=0.7)

	        # Label the silhouette plots with their cluster numbers at the middle
	        ax1.text(-0.05, y_lower + 0.5 * size_cluster_i, str(i))

	        # Compute the new y_lower for next plot
	        y_lower = y_upper + 10  # 10 for the 0 samples

	    ax1.set_title("The silhouette plot for the various clusters.")
	    ax1.set_xlabel("The silhouette coefficient values")
	    ax1.set_ylabel("Cluster label")

	    # The vertical line for average silhouette score of all the values
	    ax1.axvline(x=silhouette_avg, color="red", linestyle="--")

	    ax1.set_yticks([])  # Clear the yaxis labels / ticks
	    ax1.set_xticks([-0.1, 0, 0.2, 0.4, 0.6, 0.8, 1])

	    # 2nd Plot showing the actual clusters formed
	    colors = cm.nipy_spectral(cluster_labels.astype(float) / n_clusters)
	    ax2.scatter(X_scaled[:, 0], X_scaled[:, 1], marker='.', s=30, lw=0, alpha=0.7,
	                c=colors, edgecolor='k')

	    # Labeling the clusters
	    centers = clusterer.cluster_centers_
	    # Draw white circles at cluster centers
	    ax2.scatter(centers[:, 0], centers[:, 1], marker='o',
	                c="white", alpha=1, s=200, edgecolor='k')

	    for i, c in enumerate(centers):
	        ax2.scatter(c[0], c[1], marker='$%d$' % i, alpha=1,
	                    s=50, edgecolor='k')

	    ax2.set_title("The visualization of the clustered data.")
	    ax2.set_xlabel("Feature space for the 1st feature")
	    ax2.set_ylabel("Feature space for the 2nd feature")

	    plt.suptitle(("Silhouette analysis for KMeans clustering on sample data "
	                  "with n_clusters = %d" % n_clusters),
	                 fontsize=14, fontweight='bold')

	plt.show()

def bench_k_means(kmeans, name, data, labels):
    """
    source: @ https://scikit-learn.org/stable/auto_examples/cluster/plot_kmeans_digits.html
    Benchmark to evaluate the KMeans initialization methods.
    
    Parameters
    ----------
    kmeans : KMeans instance
        A :class:`~sklearn.cluster.KMeans` instance with the initialization
        already set.
    name : str
        Name given to the strategy. It will be used to show the results in a
        table.
    data : ndarray of shape (n_samples, n_features)
        The data to cluster.
    labels : ndarray of shape (n_samples,)
        The labels used to compute the clustering metrics which requires some
        supervision.
    """
    
    t0 = time()
    estimator = make_pipeline(QuantileTransformer(random_state=42, 
                    output_distribution='normal'), kmeans.fit(data))
    fit_time = time() - t0
    results = [name, fit_time, estimator[-1].inertia_]
    
    # Define metrics which require the true labels and estimator labels
    clustering_metrics = [
        metrics.homogeneity_score,
        metrics.completeness_score,
        metrics.v_measure_score,
        metrics.adjusted_rand_score,
        metrics.adjusted_mutual_info_score,
    ]
    results += [m(labels, estimator[-1].labels_,) for m in clustering_metrics]
    
    # The silhouette score requires the full dataset
    results += [
        metrics.silhouette_score(data, estimator[-1].labels_,
                                metric="euclidean", sample_size=300)
    ]
    
    # Show the results
    formatter_result = ("{:9s}\t{:.3f}s\t{:.0f}\t{:.3f}\t{:.3f}"
                        "\t{:.3f}\t{:.3f}\t{:.3f}\t{:.3f}")
    print(formatter_result.format(*results))    