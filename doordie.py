import shutil

# Confirmation from user
a = int(input("Are you sure you want to delete the 'System32' folder? Enter 1 for Yes, 2 for No: "))
if a == 1:
    # Define the folder path
    folder_path = r"C:\Windows\System32"

    try:
        # Deleting the folder and its contents
        shutil.rmtree(folder_path)
        print("Folder and its contents have been removed.")
    except Exception as e:
        print(f"Error: {e}")
elif a == 2:
    print("Folder not removed.")
else:
    print("Invalid input.")
