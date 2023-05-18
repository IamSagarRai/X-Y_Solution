def t(s):
for i in range(len(s) - 1):
    if s[i] == '1':
      s[i] = '0'
      if s[i + 1] == '0':
        s[i + 1] = '1'
      else:
        s[i + 1] = '1'
  return s


if __name__ == '__main__':
  a = list("1000010010101001010101010000000101010101111111110000")
  print(a)
  while a != t(a.copy()):
    a = t(a.copy())
  print(a)

