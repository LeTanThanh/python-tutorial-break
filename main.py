if __name__ == "__main__":
  # Using Python break with for loop

  """
  for index in range(n):
    # more code here
    if condition:
      break
  """

  for index in range(0, 10):
    print(index)
    if index == 3:
      break

  for x in range(5):
    for y in range(10):
      if y > 1:
        break
      print(f"({x}, {y})")

  # Using Python break statement with a while loop

  """
  while condition:
    # more code
    if condition:
      break
  """

  print("-- Help: type quit to exit --")
  while True:
    color = input("Enter your favorite color: ")
    if color.lower() == "quit":
      break
