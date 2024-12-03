import hashlib

def hash_id(identifier):
    return hashlib.sha256(identifier.encode()).hexdigest()

original_id = "Neftali Barrera Rodriguez"
anonymous_id = hash_id(original_id)
print(anonymous_id)

# ef1c0d040a48e9b8798f9bcc38b98715005dcdcd722d9f1d6abe8b2192330c59