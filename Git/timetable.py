# Define the activities and their corresponding time slots
activities = {
    'Home works': ['8:00-12:00', '13:00-17:00'],
    'Python': ['7:00-8:00'],
    'Meal Times': ['8:00-9:00', '12:00-13:00', '18:00-19:00'],
    'Python Sinhala': ['19:00-20:00'],
    'Other Tasks': ['9:00-10:00']
}

# Define the time slots for the day
time_slots = ['7:00-8:00', '8:00-9:00', '9:00-10:00', '10:00-11:00', '11:00-12:00',
              '12:00-13:00', '13:00-14:00', '14:00-15:00', '15:00-16:00', '16:00-17:00',
              '17:00-18:00', '18:00-19:00', '19:00-20:00']

# Create a table to hold the schedule
schedule = {}
for slot in time_slots:
    schedule[slot] = []

# Fill in the schedule with the activities
for activity, slots in activities.items():
    for slot in slots:
        if slot in time_slots:
            schedule[slot].append(activity)
        else:
            print("Error: {} is not a valid time slot.".format(slot))

# Print out the schedule
for slot, activities in schedule.items():
    print(slot, ':', activities)
