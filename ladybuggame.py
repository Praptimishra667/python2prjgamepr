import matplotlib.pyplot as plt
import numpy as np
import random
import time

# Function to display the ladybug
def display_ladybug(positions):
    for pos in positions:
        plt.scatter(pos[0], pos[1], color='blue', s=100)
    plt.scatter(positions[0][0], positions[0][1], color='black', s=200)  # Fix the color name

# Function to display the leaf
def display_leaf(position):
    plt.scatter(position[0], position[1], color='green', marker='^', s=400)

# Function to check if the ladybug is outside the window
def outside_window(position):
    x, y = position
    return x < -200 or x > 200 or y < -200 or y > 200

# Function to check if the ladybug collided with the leaf
def check_collision(ladybug_head, leaf_position):
    return np.linalg.norm(np.array(ladybug_head) - np.array(leaf_position)) < 20

# Function to move the ladybug
def move_ladybug(positions, direction):
    head = positions[0]
    if direction == 'up':
        new_head = (head[0], head[1] + 20)
    elif direction == 'down':
        new_head = (head[0], head[1] - 20)
    elif direction == 'left':
        new_head = (head[0] - 20, head[1])
    elif direction == 'right':
        new_head = (head[0] + 20, head[1])
    positions.insert(0, new_head)
    return positions[:-1]

# Function to initialize game parameters
def init_game():
    plt.figure(figsize=(8, 8))
    plt.xlim(-220, 220)
    plt.ylim(-220, 220)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.axis('off')

    initial_position = [(0, 0)]
    direction = 'right'
    leaf_position = (random.randint(-9, 9) * 20, random.randint(-9, 9) * 20)
    return initial_position, direction, leaf_position

# Function to run the game
def run_game():
    positions, direction, leaf_position = init_game()
    score = 0
    test_score = 0  # Initialize test score

    while True:
        plt.clf()

        display_ladybug(positions)
        display_leaf(leaf_position)

        if outside_window(positions[0]) or len(positions) != len(set(positions)):
            plt.title("GAME OVER! Score: " + str(score))
            plt.draw()
            plt.pause(2)  # Longer pause for game over screen
            break

        if check_collision(positions[0], leaf_position):
            score += 10
            leaf_position = (random.randint(-9, 9) * 20, random.randint(-9, 9) * 20)
            positions.append(positions[-1])  # Extend ladybug length
        else:
            # Check if the ladybug is moving
            old_position = positions[0]
            positions = move_ladybug(positions, direction)
            new_position = positions[0]
            if old_position != new_position:
                test_score += 1  # Increment test score only if ladybug moves

        plt.title("Score: " + str(score) + " Test Score: " + str(test_score))  # Display test score
        plt.draw()
        plt.pause(0.2)

# Run the game
run_game()
