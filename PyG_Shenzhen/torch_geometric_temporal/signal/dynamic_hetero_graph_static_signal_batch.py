import torch
import numpy as np
from typing import Sequence, Dict, Union, Tuple
from torch_geometric.data import HeteroData, Batch


Edge_Indices = Sequence[Union[Dict[Tuple[str, str, str], np.ndarray], None]]
Edge_Weights = Sequence[Union[Dict[Tuple[str, str, str], np.ndarray], None]]
Node_Feature = Union[Dict[str, np.ndarray], None]
Targets = Sequence[Union[Dict[str, np.ndarray], None]]
Batches = Sequence[Union[Dict[str, np.ndarray], None]]
Additional_Features = Sequence[Union[Dict[str, np.ndarray], None]]


class DynamicHeteroGraphStaticSignalBatch(object):
    r"""A batch iterator object to contain a dynamic heterogeneous graph with a
    changing edge set and weights . The node labels
    (target) are also dynamic. The iterator returns a single discrete temporal
    snapshot for a time period (e.g. day or week). This single snapshot is a
    Pytorch Geometric Batch object. Between two temporal snapshots the edges,
    batch memberships, edge weights, target matrices and optionally passed
    attributes might change.

    Args:
        edge_index_dicts (Sequence of dictionaries where keys=Tuples and values=Numpy arrays):
         Sequence of relation type tuples and their edge index tensors.
        edge_weight_dicts (Sequence of dictionaries where keys=Tuples and values=Numpy arrays):
         Sequence of relation type tuples and their edge weight tensors.
        feature_dict (Dictionary of keys=Strings and values=Numpy arrays): Node type tuples
         and their node feature tensor.
        target_dicts (Sequence of dictionaries where keys=Strings and values=Numpy arrays):
         Sequence of node types and their label (target) tensors.
        batch_dicts (Sequence of dictionaries where keys=Strings and values=Numpy arrays):
         Sequence of batch index tensor for each node type.
        **kwargs (optional Sequence of dictionaries where keys=Strings and values=Numpy arrays): Sequence
         of node types and their additional attributes.
    """

    def __init__(
        self,
        edge_index_dicts: Edge_Indices,
        edge_weight_dicts: Edge_Weights,
        feature_dict: Node_Feature,
        target_dicts: Targets,
        batch_dicts: Batches,
        **kwargs: Additional_Features
    ):
        self.edge_index_dicts = edge_index_dicts
        self.edge_weight_dicts = edge_weight_dicts
        self.feature_dict = feature_dict
        self.target_dicts = target_dicts
        self.batch_dicts = batch_dicts
        self.additional_feature_keys = []
        for key, value in kwargs.items():
            setattr(self, key, value)
            self.additional_feature_keys.append(key)
        self._check_temporal_consistency()
        self._set_snapshot_count()

    def _check_temporal_consistency(self):
        assert len(self.edge_index_dicts) == len(
            self.edge_weight_dicts
        ), "Temporal dimension inconsistency."
        assert len(self.target_dicts) == len(
            self.edge_index_dicts
        ), "Temporal dimension inconsistency."
        assert len(self.batch_dicts) == len(
            self.edge_index_dicts
        ), "Temporal dimension inconsistency."
        for key in self.additional_feature_keys:
            assert len(self.target_dicts) == len(
                getattr(self, key)
            ), "Temporal dimension inconsistency."

    def _set_snapshot_count(self):
        self.snapshot_count = len(self.target_dicts)

    def _get_edge_index(self, time_index: int):
        if self.edge_index_dicts[time_index] is None:
            return self.edge_index_dicts[time_index]
        else:
            return {key: torch.LongTensor(value) for key, value in self.edge_index_dicts[time_index].items()
                    if value is not None}

    def _get_batch_index(self, time_index: int):
        if self.batch_dicts[time_index] is None:
            return self.batch_dicts[time_index]
        else:
            return {key: torch.LongTensor(value) for key, value in self.batch_dicts[time_index].items()
                    if value is not None}

    def _get_edge_weight(self, time_index: int):
        if self.edge_weight_dicts[time_index] is None:
            return self.edge_weight_dicts[time_index]
        else:
            return {key: torch.FloatTensor(value) for key, value in self.edge_weight_dicts[time_index].items()
                    if value is not None}

    def _get_feature(self):
        if self.feature_dict is None:
            return self.feature_dict
        else:
            return {key: torch.FloatTensor(value) for key, value in self.feature_dict.items()}

    def _get_target(self, time_index: int):
        if self.target_dicts[time_index] is None:
            return self.target_dicts[time_index]
        else:
            return {key: torch.FloatTensor(value) if value.dtype.kind == "f" else torch.LongTensor(value)
                    if value.dtype.kind == "i" else value for key, value in self.target_dicts[time_index].items()
                    if value is not None}

    def _get_additional_feature(self, time_index: int, feature_key: str):
        feature = getattr(self, feature_key)[time_index]
        if feature is None:
            return feature
        else:
            return {key: torch.FloatTensor(value) if value.dtype.kind == "f" else torch.LongTensor(value)
            if value.dtype.kind == "i" else value for key, value in feature.items()
                    if value is not None}

    def _get_additional_features(self, time_index: int):
        additional_features = {
            key: self._get_additional_feature(time_index, key)
            for key in self.additional_feature_keys
        }
        return additional_features

    def __getitem__(self, time_index: Union[int, slice]):
        if isinstance(time_index, slice):
            snapshot = DynamicHeteroGraphStaticSignalBatch(
                self.edge_index_dicts[time_index],
                self.edge_weight_dicts[time_index],
                self.feature_dict,
                self.target_dicts[time_index],
                self.batch_dicts[time_index],
                **{key: getattr(self, key)[time_index] for key in self.additional_feature_keys}
            )
        else:
            x_dict = self._get_feature()
            edge_index_dict = self._get_edge_index(time_index)
            edge_weight_dict = self._get_edge_weight(time_index)
            batch_dict = self._get_batch_index(time_index)
            y_dict = self._get_target(time_index)
            additional_features = self._get_additional_features(time_index)

            snapshot = Batch.from_data_list([HeteroData()])
            if x_dict:
                for key, value in x_dict.items():
                    snapshot[key].x = value
            if edge_index_dict:
                for key, value in edge_index_dict.items():
                    snapshot[key].edge_index = value
            if edge_weight_dict:
                for key, value in edge_weight_dict.items():
                    snapshot[key].edge_attr = value
            if y_dict:
                for key, value in y_dict.items():
                    snapshot[key].y = value
            if batch_dict:
                for key, value in batch_dict.items():
                    snapshot[key].batch = value
            if additional_features:
                for feature_name, feature_dict in additional_features.items():
                    if feature_dict:
                        for key, value in feature_dict.items():
                            snapshot[key][feature_name] = value
        return snapshot

    def __next__(self):
        if self.t < len(self.target_dicts):
            snapshot = self[self.t]
            self.t = self.t + 1
            return snapshot
        else:
            self.t = 0
            raise StopIteration

    def __iter__(self):
        self.t = 0
        return self
