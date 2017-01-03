def reverse_string(string):
  for i in range(len(string) - 1, -1, -1):
    print(string[i], end="")
  print()

def main():
    reverse_string("this was a triumph")
    reverse_string("hello world")
    reverse_string("42")
  
if __name__ == "__main__":
  main()
