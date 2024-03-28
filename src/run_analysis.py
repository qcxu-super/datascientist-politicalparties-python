from pathlib import Path

from matplotlib import pyplot

from political_party_analysis.loader import DataLoader
from political_party_analysis.dim_reducer import DimensionalityReducer
from political_party_analysis.visualization import scatter_plot

if __name__ == "__main__":

    data_loader = DataLoader()
    # Data pre-processing step
    ##### YOUR CODE GOES HERE #####
    data_process = data_loader.preprocess_data()
    print(data_process.head())

    # Dimensionality reduction step
    ##### YOUR CODE GOES HERE #####
    dimentionality_reducer = DimensionalityReducer(data=data_process, n_components=2)
    reduced_dim_data = dimentionality_reducer.reduce_dimensionality()
    print("before reduce: ", data_process.shape, ", after reduce: ", reduced_dim_data.shape)
    print(reduced_dim_data.head())

    ## Uncomment this snippet to plot dim reduced data
    pyplot.figure()
    splot = pyplot.subplot()
    scatter_plot(
        reduced_dim_data,
        color="r",
        splot=splot,
        label="dim reduced data",
    )
    # pyplot.savefig(Path(__file__).parents[1].joinpath(*["plots", "dim_reduced_data.png"]))
    pyplot.savefig("../plots/dim_reduced_data.png")

    # Density estimation/distribution modelling step
    ##### YOUR CODE GOES HERE #####

    # Plot density estimation results here
    ##### YOUR CODE GOES HERE #####
    pyplot.savefig(Path(__file__).parents[1].joinpath(*["plots", "density_estimation.png"]))

    # Plot left and right wing parties here
    pyplot.figure()
    splot = pyplot.subplot()
    ##### YOUR CODE GOES HERE #####
    pyplot.savefig(Path(__file__).parents[1].joinpath(*["plots", "left_right_parties.png"]))
    pyplot.title("Lefty/righty parties")

    # Plot finnish parties here
    ##### YOUR CODE GOES HERE #####

    print("Analysis Complete")
