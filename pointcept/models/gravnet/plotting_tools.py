import plotly.express as px
import dgl
import torch
import pandas as pd
import numpy as np


def PlotCoordinates(g, path, num_layer=0):
    outdir = "/mnt/proj3/dd-23-91/cern/pointcep_models/gravnet"
    outdir = outdir + "/figures"
    name = path
    graphs = dgl.unbatch(g)
    for i in range(0, 1):
        graph_i = graphs[i]
        if path == "input_coords":
            coords = graph_i.ndata["c"]
        if path == "gravnet_coord":
            coords = graph_i.ndata["gncoords"]
        if path == "final_clustering":
            coords = graph_i.ndata["final_cluster"]

        tidx = graph_i.ndata["object"]
        data = {
            "X": coords[:, 0].view(-1, 1).detach().cpu().numpy(),
            "Y": coords[:, 1].view(-1, 1).detach().cpu().numpy(),
            "Z": coords[:, 2].view(-1, 1).detach().cpu().numpy(),
            "tIdx": tidx.view(-1, 1).detach().cpu().numpy(),
        }
        hoverdict = {}
        # if hoverfeat is not None:
        #     for j in range(hoverfeat.shape[1]):
        #         hoverdict["f_" + str(j)] = hoverfeat[:, j : j + 1]
        #     data.update(hoverdict)

        # if nidx is not None:
        #     data.update({"av_same": av_same})

        df = pd.DataFrame(
            np.concatenate([data[k] for k in data], axis=1),
            columns=[k for k in data],
        )
        df["orig_tIdx"] = df["tIdx"]
        rdst = np.random.RandomState(1234567890)  # all the same
        shuffle_truth_colors(df, "tIdx", rdst)

        # hover_data = ["orig_tIdx", "idx"] + [k for k in hoverdict.keys()]
        # if nidx is not None:
        #     hover_data.append("av_same")
        fig = px.scatter_3d(
            df,
            x="X",
            y="Y",
            z="Z",
            color="tIdx",
            # hover_data=hover_data,
            template="plotly_dark",
            color_continuous_scale=px.colors.sequential.Rainbow,
        )
        fig.update_traces(marker=dict(line=dict(width=0)))
        if path == "gravnet_coord":
            fig.write_html(
                outdir + "/" + name + "_" + num_layer + "_" + str(i) + ".html"
            )
        else:
            fig.write_html(outdir + "/" + name + "_" + str(i) + ".html")


def shuffle_truth_colors(df, qualifier="truthHitAssignementIdx", rdst=None):
    ta = df[qualifier]
    unta = np.unique(ta)
    unta = unta[unta > -0.1]
    if rdst is None:
        np.random.shuffle(unta)
    else:
        rdst.shuffle(unta)
    out = ta.copy()
    for i in range(len(unta)):
        out[ta == unta[i]] = i
    df[qualifier] = out
