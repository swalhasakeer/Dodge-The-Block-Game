# 🧩 Dodge the Blocks – A Beginner-Friendly Pygame Game

"Dodge the Blocks" is a fun, user-controlled arcade-style game built with Python and Pygame. The player moves a blue block left and right to **dodge falling red blocks**. The longer you survive, the higher your score climbs!

---

## 🎮 Gameplay Overview

- 👤 **Control the Player:** Use the **left (←)** and **right (→)** arrow keys.
- 💣 **Avoid Collisions:** Red blocks fall from the top—don't get hit!
- 🧠 **Goal:** Survive as long as possible and build up your score.

---

## 🚀 Features

✅ Simple and clean interface  
✅ Real-time keyboard controls  
✅ Increasing score system  
✅ Game over condition on collision  
✅ Easy to customize and expand

---

## 🖥️ Screenshot

![Screenshot 2025-06-23 123957](https://github.com/user-attachments/assets/5d852aa6-72b1-4a8c-a8d0-520d48aadcc2)


---

## 🛠️ Setup and Installation

Follow these steps to run the game on your local machine.

### 1. 📦 Clone the Repository
```bash
git clone https://github.com/your-username/dodge-the-blocks.git
cd dodge-the-blocks
```

### 2. 🐍 Create a Virtual Environment (Optional but Recommended)

```bash
python -m venv venv
source venv/bin/activate     # On Windows: venv\Scripts\activate
```

### 3. 📥 Install Required Library

```bash
pip install pygame
```

### 4. ▶️ Run the Game
```bash
python dodge_game.py
```

## 📂 Project Structure

```bash
Dodge The Blocks/
│
├── dodge_game.py         # Main game logic
└── README.md             # Project documentation
```

## 🧾 Game Logic Summary
- The player rectangle starts at the bottom center.

- One enemy block falls from the top.

- Every time the player avoids it, the score increases.

- If the enemy collides with the player, the game ends.

## 🌟 Support

- If you like this project, feel free to ⭐ star it on GitHub!

