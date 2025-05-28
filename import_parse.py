import csv

# figure out folder
# 1.array[0] // assume deafault and split by spaces
frame_list = []
f = open('Baselight_export_spring2025.txt', 'r')
frame_data = f.read()

# 2.split() again by '/' i.e "baselightfilesystem1,' 'dogman', etc
for line in frame_data.split('\n'):
    part = line.split()
    if part:
        base_path = part[0]
        path = base_path.split('/')

# 3.combine them again with '/' starting from array location 1 (i.e. dogman) so you create a string /dogman/reel1/partA/1920x1080

    if 'dogman' in path:
        dogman_index = path.index('dogman')
        rest_of_path = path[dogman_index:]
        match_path = '/' + '/'.join(rest_of_path)

# 4.take list from xytech file of JUST locations
    xytech_locations = [
        'reel1/partA/1920x1080',
        'reel1/VFX/Hydraulx',
        'reel1/VFX/Framestore',
        'reel1/VFX/AnimalLogic',
        'reel1/partB/1920x1080',
        'pickups/shot_1ab/1920x1080',
        'pickups/shot_2b/1920x1080',
        'reel1/partC/1920x1080'
    ]

    path_update = {
        'reel1/partA/1920x1080': '/hpsans13/production/dogman/reel1/partA/1920x1080',
        'reel1/VFX/Hydraulx': '/hpsans12/production/dogman/reel1/VFX/Hydraulx',
        'reel1/VFX/Framestore': '/hpsans13/production/dogman/reel1/VFX/Framestore',
        'reel1/VFX/AnimalLogic': '/hpsans14/production/dogman/reel1/VFX/AnimalLogic',
        'reel1/partB/1920x1080': '/hpsans13/production/dogman/reel1/partB/1920x1080',
        'pickups/shot_1ab/1920x1080': '/hpsans15/production/dogman/pickups/shot_1ab/1920x1080',
        'pickups/shot_2b/1920x1080': '/hpsans11/production/dogman/pickups/shot_2b/1920x1080',
        'reel1/partC/1920x1080': '/hpsans17/production/dogman/reel1/partC/1920x1080'
    }

    # 5.lastly check if now string exists in xytech locations list, if so switch as new folder
    full_path = base_path
    for location in xytech_locations:
        if location in match_path:
            full_path = path_update[location]
            break


    # Get all frame numbers from this line
    for frame in part[1:]:
        frame_list.append((int(frame), full_path))

frame_list.sort()

# figure out frame and frame ranges
var1past = 0
var1previous = 0
current_path = ""

with open('output.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(['Path', 'Frames'])
    # Start frame or start path
    for frame, path in frame_list:
        if var1past == 0 or path != current_path:
            if var1past != 0:
                if var1past == var1previous:
                    range = str(var1past)
                    writer.writerow([current_path, range])
                else:
                    range = str(var1past) + "-" + str(var1previous)
                    writer.writerow([current_path, range])
            var1past = frame
            var1previous = frame
            current_path = path

        # Frame in range continue
        elif frame == var1previous + 1:
            var1previous = frame

        # Frame not in range
        else:
            if var1past == var1previous:
                range = str(var1past)
                writer.writerow([current_path, range])
            else:
                range = str(var1past) + "-" + str(var1previous)
                writer.writerow([current_path, range])

            # New range
            var1past = frame
            var1previous = frame
