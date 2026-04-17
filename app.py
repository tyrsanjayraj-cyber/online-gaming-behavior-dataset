import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Title
st.title("🎮 Gaming Analytics Dashboard")

st.write("This dashboard analyzes player behaviour, retention, purchase trends, and leaderboard statistics.")

# Load Dataset
df = pd.read_csv("online_gaming_behavior_dataset.csv")

# Show Dataset
st.subheader("Dataset Preview")
st.dataframe(df.head())

# -------------------------------
# Player Retention Analysis
# -------------------------------

st.subheader("Player Retention Analysis")

retention = df.groupby("PlayerID")["SessionsPerWeek"].sum()

fig1, ax1 = plt.subplots()
ax1.hist(retention)

ax1.set_title("Player Retention Distribution")
ax1.set_xlabel("Sessions per Player")
ax1.set_ylabel("Number of Players")

st.pyplot(fig1)

# -------------------------------
# In-Game Purchase Trends
# -------------------------------

st.subheader("In-Game Purchase Trends")

purchase = df.groupby("PlayerLevel")["InGamePurchases"].sum()

fig2, ax2 = plt.subplots()

purchase.plot(kind="bar", ax=ax2)

ax2.set_title("In-Game Purchases by Player Level")
ax2.set_xlabel("Player Level")
ax2.set_ylabel("Total Purchases")

st.pyplot(fig2)

# -------------------------------
# Leaderboard Analytics
# -------------------------------

st.subheader("Top 10 Players Leaderboard")

leaderboard = df.groupby("PlayerID")["PlayTimeHours"].sum().sort_values(ascending=False)

top_players = leaderboard.head(10)

fig3, ax3 = plt.subplots()

top_players.plot(kind="bar", ax=ax3)

ax3.set_title("Top 10 Players by Play Time")
ax3.set_xlabel("Player ID")
ax3.set_ylabel("Play Time Hours")

st.pyplot(fig3)

# Footer
st.success("Gaming Analytics Dashboard Loaded Successfully!")