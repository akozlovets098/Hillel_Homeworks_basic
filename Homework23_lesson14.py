import os

def ten_biggest_files(path_to_folder):
    result = []
    for root, dirs, files in os.walk(path_to_folder):
        for file in files:
            result.append([file, os.path.getsize(os.path.join(root, file))])
    result = sorted(result, reverse=True, key=lambda x: x[1])[:10]
    return [i[0] for i in result]


print(ten_biggest_files(input('Insert the path to the destination folder:\n')))