import torch.nn as nn
import torch.optim as optim
import mdn

# initialize the model
model = nn.Sequential(
    nn.Linear(5, 6),
    nn.Tanh(),
    mdn.MDN(6, 7, 20)
)
optimizer = optim.Adam(model.parameters())

# train the model
for minibatch, labels in train_set:
    model.zero_grad()
    pi, sigma, mu = model(minibatch)
    loss = mdn.mdn_loss(pi, sigma, mu, labels)
    loss.backward()
    optimizer.step()

# sample new points from the trained model
minibatch = next(test_set)
pi, sigma, mu = model(minibatch)
samples = mdn.sample(pi, sigma, mu)