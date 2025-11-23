log_entries = []

    for root, dirs, files in os.walk(base_path):
        for file in files:
            if file == target_filename:
                full_path = os.path.normpath(os.path.join(root, file))
                try:
                    with open(full_path, "r", encoding="utf-8") as f:
fghjhkj
