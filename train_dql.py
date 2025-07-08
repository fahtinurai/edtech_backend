import pandas as pd
import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim
import random
from collections import deque

# Load dataset
df = pd.read_csv("data/edtech_combined_dataset.csv")

# Buat reward: performa tinggi = 1, lainnya = 0
df['reward'] = df['performa'].apply(lambda x: 1 if x in ['Baik', 'Sangat Baik'] else 0)

features = ["nilai_mtk", "nilai_ipa", "jam_belajar", "klik_video"]
X = df[features].values
y = df["reward"].values

# Deep Q-Network
class DQN(nn.Module):
    def __init__(self, input_dim, output_dim):
        super(DQN, self).__init__()
        self.fc1 = nn.Linear(input_dim, 64)
        self.fc2 = nn.Linear(64, 64)
        self.fc3 = nn.Linear(64, output_dim)

    def forward(self, x):
        x = torch.relu(self.fc1(x))
        x = torch.relu(self.fc2(x))
        return self.fc3(x)

# Simulasi lingkungan belajar
class LearningEnv:
    def __init__(self, X, y):
        self.X = X
        self.y = y
        self.index = 0

    def reset(self):
        self.index = 0
        return self.X[self.index]

    def step(self, action):
        reward = self.y[self.index] if action == 1 else 0
        self.index += 1
        done = self.index >= len(self.X)
        next_state = self.X[self.index] if not done else np.zeros_like(self.X[0])
        return next_state, reward, done

# Hyperparameter
episodes = 100
gamma = 0.9
epsilon = 0.1
lr = 0.001
batch_size = 32
input_dim = len(features)
output_dim = 2

model = DQN(input_dim, output_dim)
optimizer = optim.Adam(model.parameters(), lr=lr)
loss_fn = nn.MSELoss()
memory = deque(maxlen=1000)
env = LearningEnv(X, y)

# Training loop
for ep in range(episodes):
    state = env.reset()
    total_reward = 0

    while True:
        if random.random() < epsilon:
            action = random.randint(0, output_dim - 1)
        else:
            with torch.no_grad():
                q_vals = model(torch.tensor(state, dtype=torch.float32))
                action = torch.argmax(q_vals).item()

        next_state, reward, done = env.step(action)
        memory.append((state, action, reward, next_state, done))
        total_reward += reward
        state = next_state

        if len(memory) >= batch_size:
            batch = random.sample(memory, batch_size)
            states, actions, rewards, next_states, dones = zip(*batch)

            states = torch.tensor(states, dtype=torch.float32)
            actions = torch.tensor(actions, dtype=torch.int64).unsqueeze(1)
            rewards = torch.tensor(rewards, dtype=torch.float32)
            next_states = torch.tensor(next_states, dtype=torch.float32)
            dones = torch.tensor(dones, dtype=torch.bool)

            curr_q = model(states).gather(1, actions).squeeze()
            next_q = model(next_states).max(1)[0]
            expected_q = rewards + gamma * next_q * (~dones)

            loss = loss_fn(curr_q, expected_q)
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

        if done:
            print(f"Episode {ep+1}/{episodes} - Total Reward: {total_reward}")
            break

# Simpan model
torch.save(model.state_dict(), "app/model_dql.pth")
print("✅ Model DQL berhasil disimpan di app/model_dql.pth")
