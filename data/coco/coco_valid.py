import labelme2coco

# set directory that contains labelme annotations and image files
labelme_folder = "valid2017"

# set path for coco json to be saved
save_json_path = "instances_valid2017.json"

# conert labelme annotations to coco
labelme2coco.convert(labelme_folder, save_json_path)
