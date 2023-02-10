import touchcontrol as tc

# Simulate a simple tap on the screen
tc.tap((1400, 400))

# Simulate a finger swipe on the screen
start = (1000, 600)
end = (1800, 700)
tc.swipe(start, end, num_steps=30)

# simulate two fingers swiping away from each other on screen
# zooming gesture
finger_1_start = (1800, 600)
finger_1_end = (1800, 400)
finger_2_start = (1800, 700)
finger_2_end = (1800, 900)
tc.spread(finger_1_start, finger_1_end, finger_2_start, finger_2_end, num_steps=50)
