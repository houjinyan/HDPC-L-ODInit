import torch
import numpy as np
from typing import Sequence, Dict, Union, Tuple
from torch_geometric.data import HeteroData


Edge_Index = Union[Dict[Tuple[str, str, str], np.ndarray], None]
Edge_Weight = Union[Dict[Tuple[str, str, str], np.ndarray], None]
Node_Features = Sequence[Union[Dict[str, np.ndarray], None]]
Targets = Sequence[Union[Dict[str, np.ndarray], None]]
Additional_Features = Sequence[Union[Dict[str, np.ndarray], None]]


class StaticHeteroGraphTemporalSignal(object):
    r"""A data iterator object to contain a static heterogeneous graph with a dynamically
    changing constant time difference temporal feature set (multiple signals).
    The node labels (target) are also temporal. The iterator returns a single
    constant time difference temporal snapshot for a time period (e.g. day or week).
    This single temporal snapshot is a Pytorch Geometric HeteroData object. Between two
    temporal snapshots the features and optionally passed attributes might change.
    However, the underlying graph is the same.

     .. code-block:: python
        from torch_geometric_temporal.signal import StaticHeteroGraphTemporalSignal

        edge_index_dict = {
            ("author", "writes", "paper"): np.array([[0, 0, 1], [0, 1, 2]])
        }

        feature_dicts = [
            {"author": np.array([[0], [0]]),
             "paper": np.array([[0], [0], [0]])},
            {"author": np.array([[0.1], [0.1]]),
             "paper": np.array([[0.1], [0.1], [0.1]])},
            {"author": np.array([[0.2], [0.2]]),
             "paper": np.array([[0.2], [0.2], [0.2]])}
        ]

        target_dicts = [
            {"author": np.array([0, 0]),
             "paper": np.array([0, 0, 0])},
            {"author": np.array([1, 1]),
             "paper": np.array([1, 1, 1])},
            {"author": np.array([2, 2]),
             "paper": np.array([2, 2, 2])}
        ]

        # Create heterogeneous graph snapshots with same structure but different features
        # and labels (in this example node types "paper" and "author"):
        graph_snapshots = StaticHeteroGraphTemporalSignal(edge_index_dict, None, feature_dicts, target_dicts)

    Note that in this example all feature and target dicts have the same keys.

    * To skip initializing nodes of all types in a specific snapshot simply
      pass :obj:`None` instead of a dictionary:

    .. code-block:: python
        feature_dicts = [
            {"author": np.array([[0], [0]]),
             "paper": np.array([[0], [0], [0]])},
            None,
            {"author": np.array([[0.2], [0.2]]),
             "paper": np.array([[0.2], [0.2], [0.2]])}
        ]

    * To skip initializing node features of type :obj:`"paper"` in a specific snapshot simply
      pass :obj:`None` as dictionary value or omit this feature type:

    .. code-block:: python
        feature_dicts = [
            {"author": np.array([[0], [0]]),
             "paper": np.array([[0], [0], [0]])},
            {"author": np.array([[0.1], [0.1]]),
             "paper": None}, # pass None as value
            {"author": np.array([[0.2], [0.2]])} # omit type in dict
        ]

    Args:
        edge_index_dict (Dictionary of keys=Tuples and values=Numpy arrays): Relation type tuples
         and their edge index tensors.
        edge_weight_dict (Dictionary of keys=Tuples and values=Numpy arrays): Relation type tuples
         and their edge weight tensors.
        feature_dicts (Sequence of dictionaries where keys=Strings and values=Numpy arrays): Sequence of node
         types and their feature tensors.
        target_dicts (Sequence of dictionaries where keys=Strings and values=Numpy arrays): Sequence of node
         types and their label (target) tensors.
        **kwargs (optional Sequence of dictionaries where keys=Strings and values=Numpy arrays): Sequence
         of node types and their additional attributes.
    """

    def __init__(
        self,
        edge_index_dict: Edge_Index,
        edge_weight_dict: Edge_Weight,
        feature_dicts: Node_Features,
        target_dicts: Targets,
        **kwargs: Additional_Features
    ):
        self.edge_index_dict = edge_index_dict
        self.edge_weight_dict = edge_weight_dict
        self.feature_dicts = feature_dicts
        self.target_dicts = target_dicts
        self.additional_feature_keys = []
        for key, value in kwargs.items():
            setattr(self, key, value)
            self.additional_feature_keys.append(key)
        self._check_temporal_consistency()
        self._set_snapshot_count()

    def _check_temporal_consistency(self):
        assert len(self.feature_dicts) == len(
            self.target_dicts
        ), "Temporal dimension inconsistency."
        for key in self.additional_feature_keys:
            assert len(self.target_dicts) == len(
                getattr(self, key)
            ), "Temporal dimension inconsistency."

    def _set_snapshot_count(self):
        self.snapshot_count = len(self.feature_dicts)

    def _get_edge_index(self):
        if self.edge_index_dict is None:
            return self.edge_index_dict
        else:
            return {key: torch.LongTensor(value) for key, value in self.edge_index_dict.items()}

    def _get_edge_weight(self):
        if self.edge_weight_dict is None:
            return self.edge_weight_dict
        else:
            return {key: torch.FloatTensor(value) for key, value in self.edge_weight_dict.items()}

    def _get_features(self, time_index: int):
        if self.feature_dicts[time_index] is None:
            return self.feature_dicts[time_index]
        else:
            return {key: torch.FloatTensor(value) for key, value in self.feature_dicts[time_index].items()
                    if value is not None}

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
            snapshot = StaticHeteroGraphTemporalSignal(
                self.edge_index_dict,
                self.edge_weight_dict,
                self.feature_dicts[time_index],
                self.target_dicts[time_index],
                **{key: getattr(self, key)[time_index] for key in self.additional_feature_keys}
            )
        else:
            x_dict = self._get_features(time_index)
            edge_index_dict = self._get_edge_index()
            edge_weight_dict = self._get_edge_weight()
            y_dict = self._get_target(time_index)
            additional_features = self._get_additional_features(time_index)

            snapshot = HeteroData()
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
            if additional_features:
                for feature_name, feature_dict in additional_features.items():
                    if feature_dict:
                        for key, value in feature_dict.items():
                            snapshot[key][feature_name] = value
        return snapshot

    def __next__(self):
        if self.t < len(self.feature_dicts):
            snapshot = self[self.t]
            self.t = self.t + 1
            return snapshot
        else:
            self.t = 0
            raise StopIteration

    def __iter__(self):
        self.t = 0
        return self
