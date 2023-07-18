filename = input("File name: ")


if filename.strip().lower().endswith('.gif') == True:
    print("image/gif")
elif filename.strip().lower().endswith('.jpg') == True:
    print("image/jpeg")
elif filename.strip().lower().endswith('.jpeg') == True:
    print("image/jpeg")
elif filename.strip().lower().endswith('.png') == True:
    print("image/png")
elif filename.strip().lower().endswith('.pdf') == True:
    print("application/pdf")
elif filename.strip().lower().endswith('.txt') == True:
    print("text/plain")
elif filename.strip().lower().endswith('.zip') == True:
    print("application/zip")
else:
    print("application/octet-stream")