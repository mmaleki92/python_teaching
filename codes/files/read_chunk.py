with open("example.bin", "rb") as f:
    chunk_size = 16
    while True:
        chunk = f.read(chunk_size)
        if not chunk:
            break
        print(chunk)