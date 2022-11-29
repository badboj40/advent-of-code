import time

alphabet = "abcdefghijklmnopqrstuvwxyz"

def increment_password(password):
  password_value = 0
  for i in range(len(password)):
    char = password[len(password)-i-1]
    password_value += len(alphabet) ** i * alphabet.find(char)
  
  password_value += 1
  new_password = ""
  for i in range(len(password)):
    char_value = int(password_value % len(alphabet))
    password_value = (password_value - char_value) / len(alphabet)
    new_password = alphabet[char_value] + new_password
  return new_password


def is_valid(password):
  # can't contain letters 'i', 'o' or 'l'
  if 'i' in password or 'o' in password or 'l' in password:
    return False

  # must contain increasing straight
  for i in range(len(password)-2):
    if password[i:i+3] in alphabet:
      break # Found it
  else:
    return False

  # must contain two different pairs
  i = 0
  pairs = 0
  while i < len(password)-1:
    if password[i] == password[i+1]:
      pairs += 1
      i += 2
    else:
      i += 1
  
  return pairs >= 2


def generate_new_password(previous_password):
  password = previous_password
  while True:
    password = increment_password(password)
    if is_valid(password):
      return password


if __name__ == "__main__":
  indata = "vzbxkghb"
  t0 = time.time()

  new_password = generate_new_password(indata)

  print("part1:", new_password)
  print("part2:", generate_new_password(new_password))

  print("time:", time.time()-t0)
