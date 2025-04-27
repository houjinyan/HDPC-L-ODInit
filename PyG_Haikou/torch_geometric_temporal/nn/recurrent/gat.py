import torch
from torch import nn
import torch.nn.functional as F
class GraphAttentionLayer(nn.Module):
    def __init__(self, in_c, out_c, alpha=0.2):
        """
        graph attention layer
        :param in_c:
        :param out_c:
        :param alpha:
        """
        super(GraphAttentionLayer, self).__init__()
        self.in_c = in_c
        self.out_c = out_c
        self.alpha = alpha

        self.W = nn.Parameter(torch.empty(size=(in_c, out_c)))
        nn.init.xavier_uniform_(self.W.data, gain=1.414)
        self.a = nn.Parameter(torch.empty(size=(2 * out_c, 1)))
        nn.init.xavier_uniform_(self.a.data, gain=1.414)
        self.leakyrelu = nn.LeakyReLU(self.alpha)

    def forward(self, features, adj):
        B, N = features.size(0), features.size(1)
        adj = adj + torch.eye(N, dtype=adj.dtype).cuda()  # A+I
        h = torch.matmul(features, self.W)  # [B,N,out_features]
        # [B, N, N, 2 * out_features]
        a_input = torch.cat([h.repeat(1, 1, N).view(B, N * N, -1), h.repeat(1, N, 1)], dim=2).view(B, N, -1, 2 * self.out_c)
        e = self.leakyrelu(torch.matmul(a_input, self.a).squeeze(3))  # [B,N, N, 1] => [B, N, N]
        zero_vec = -1e12 * torch.ones_like(e)
        attention = torch.where(adj > 0, e, zero_vec)  # [B,N,N]
        attention = F.softmax(attention, dim=2)  # softmax [N, N]
        # attention = F.dropout(attention, 0.5)
        h_prime = torch.matmul(attention, h)  # [B,N, N]*[N, out_features] => [B,N, out_features]
        return h_prime

    def __repr__(self):
        return self.__class__.__name__ + ' (' + str(self.in_features) + ' -> ' + str(self.out_features) + ')'


class GAT(nn.Module):
    def __init__(self, in_c, hid_c, out_c, n_heads=2):
        """
        :param in_c: int, number of input channels.
        :param hid_c: int, number of hidden channels.
        :param out_c: int, number of output channels.
        :param K:
        """
        super(GAT, self).__init__()
        self.attentions = nn.ModuleList([GraphAttentionLayer(in_c, hid_c) for _ in range(n_heads)])
        # self.conv1 = GraphAttentionLayer(in_c, hid_c)
        self.conv2 = GraphAttentionLayer(hid_c * n_heads, out_c)
        self.act = nn.ReLU()

    def forward(self, x, adj):
        # data prepare
        #adj = data["graph"][0]  # [N, N]
        #x = data["flow_x"]  # [B, N, H, D]
        B, N = x.size(0), x.size(1)
        x = x.view(B, N, -1)  # [B, N, H*D]

        # forward
        outputs = torch.cat([attention(x, adj) for attention in self.attentions], dim=-1)
        outputs = self.act(outputs)
        # output_1 = self.act(self.conv1(flow_x, adj))
        output_2 = self.act(self.conv2(outputs, adj))

        return torch.squeeze(output_2.unsqueeze(2))  # [B,1,N,1]
