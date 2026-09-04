def caesar_encrypt(plaintext, shift):
	uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	lowercase = "abcdefghijklmnopqrstuvwxyz"
	result = ""


	shift = shift % 26

	for char in plaintext:
		if char in uppercase:
			position = uppercase.index(char)
			new_position = (position + shift) % 26
			result += uppercase[new_position]

		elif char in lowercase:
			position = lowercase.index(char)
			new_position = (position + shift) % 26
			result += lowercase[new_position]

		else:

			result += char

	return result

def caesar_decrypt(ciphertext,shift):
	uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	lowercase = "abcdefghijklmnopqrstuvwxyz"
	result = ""

	shift = shift % 26

	for char in ciphertext:
		if char in uppercase:
			position = uppercase.index(char)
			new_position = (position - shift) % 26
			result += uppercase[new_position]

		elif char in lowercase:
			position = lowercase.index(char)
			new_position = (position - shift) % 26
			result += lowercase[new_position]

		else:
			result += char

	return result



def rail_fence_encrypt(plaintext, rails):
	if rails == 1:
		return plaintext

	fence = [""] * rails
	rail = 0
	direction = 1

	for char in plaintext:
		fence[rail] += char

		rail += direction

		if rail == 0 or rail == rails - 1:
			direction *= -1

	return "".join(fence)


def rail_fence_decrypt(ciphertext, rails):
	if rails == 1:
		return ciphertext

	pattern = []
	rail = 0
	direction = 1

	# Figure out the zigzag pattern
	for char in ciphertext:
		pattern.append(rail)


		rail += direction

		if rail == 0 or rail == rails - 1:
			direction *= -1

	# Count how many letters belong to each rail
	counts = []

	for i in range(rails):
		counts.append(pattern.count(i))

	# Divide the ciphertext among the rails
	fence = []
	position = 0

	for count in counts:
		fence.append(list(ciphertext[position:position + count]))
		position += count

	# Follow the zigzag pattern to rebuild the message
	result = ""
	rail_positions = [0] * rails

	for rail in pattern:
		result += fence[rail][rail_positions[rail]]
		rail_positions[rail] += 1

	return result


# Required Test Cases


# Caesar Cipher
print(caesar_encrypt("ATTACK AT DAWN", 5))
print(caesar_decrypt("FXXF?K?F?I?", 5))
print(caesar_encrypt("COMP301", 7))
print(caesar_decrypt(caesar_encrypt("COMP301", 7), 7))


# Rail Fence Cipher
print(rail_fence_encrypt("HELLO WORLD", 3))
print(rail_fence_decrypt("HOLEL WDLRO", 3))
print(rail_fence_encrypt("SECRETSHARED", 4))
print(rail_fence_decrypt(rail_fence_encrypt("SECRETSHARED", 4), 4))
