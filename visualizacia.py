import matplotlib.pyplot as plt

# Read text from file
with open('ascii_art.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Define the characters of interest
characters_of_interest = ".:-=+*#%@"

# Set up plot
fig, ax = plt.subplots(figsize=(12, 6))

# Batch process lines for visualization
for y, line in enumerate(lines):
    if y % 14 == 0:  # Process every 20th line (adjust as needed)
        for x, char in enumerate(line.strip()):
            if char in characters_of_interest:
                ax.text(x, y, char, fontsize=2, ha='center', va='center', color='blue')
        plt.draw()  # Update plot incrementally

# Customize plot
ax.set_xlim(-1, len(max(lines, key=len)))  # Adjust x-axis limit based on the longest line
ax.set_ylim(0, len(lines) + 1)  # Adjust y-axis limit to accommodate all lines
ax.set_aspect('equal')  # Ensure equal aspect ratio for better visualization

# Hide axes
ax.axis('off')

# Enable zooming
plt.gca().invert_yaxis()  # Invert y-axis to display from top to bottom
plt.tight_layout()
plt.show()
