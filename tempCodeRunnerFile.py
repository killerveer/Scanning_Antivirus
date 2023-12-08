

# get hash of a file
def sha256_hash(filename):
    try:
    
        with open(filename, "rb") as f:
            bytes = f.read()
            sha256hash = hashlib.sha256(bytes).hexdigest()
            
            f.close()
            # print(sha256hash)

        return sha256hash
    except:
        return 0

# malware detection by hash
def malware_checker(pathofFile):
    global malware_hashes
    global virusinfo