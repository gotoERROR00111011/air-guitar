import torch
import torch.nn as nn
import torch.nn.functional as F

class Net(nn.Module):
    def __init__(self,inp=42,out=2):
        super(Net,self).__init__()
        self.relu=nn.ReLU()
        
        self.layer=nn.Sequential(
            nn.Linear(inp,64,bias=True),
            self.relu,
            nn.Linear(64,64,bias=True),
            self.relu,
            nn.Linear(64,32,bias=True),
            self.relu,
            nn.Linear(32,out,bias=True),
            nn.Sigmoid()
        )
    def forward(self,inp):
        inp=self.avg(inp)
        return self.layer(inp)

    def avg(self,X):
        for x in X:
            minX=min(x[::2])
            minY=min(x[1:2])
            for i in range(len(x)):
                if i%2==0:
                    x[i]-=minX
                else:
                    x[i]-=minY
        return X


if __name__ == '__main__':
    t=Net()
    r=torch.rand(1,40)
    print(t.forward(r))